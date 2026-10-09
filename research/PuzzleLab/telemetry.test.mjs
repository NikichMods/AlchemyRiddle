// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';import assert from 'node:assert/strict';
import http from 'node:http';import {mkdtempSync,readFileSync,writeFileSync,readdirSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';
import {createLab} from './server.mjs';import {createAdmin,snapshot} from './admin.mjs';
import {newTelemetry,recordPage,summarize,sessionKey} from './telemetry.mjs';
const listen=s=>new Promise(r=>s.listen(0,'127.0.0.1',r)),close=s=>new Promise(r=>s.close(r));
function req(s,path,body,headers={}){return new Promise((resolve,reject)=>{const port=s.address().port;const request=http.request({hostname:'127.0.0.1',port,path,method:body===undefined?'GET':'POST',headers:{Host:`127.0.0.1:${port}`,...(body===undefined?{}:{Origin:`http://127.0.0.1:${port}`,'Content-Type':'application/json'}),...headers}},res=>{let text='';res.on('data',c=>text+=c);res.on('end',()=>resolve({status:res.statusCode,text,headers:res.headers}));});request.on('error',reject);request.end(body===undefined?undefined:JSON.stringify(body));});}
test('visible-time estimate unions tabs, bounds missing heartbeats and marks incomplete history',()=>{
  const log=newTelemetry('session'),tab='11111111-1111-1111-1111-111111111111',tab2='22222222-2222-2222-2222-222222222222';
  recordPage(log,{kind:'page',tab},'2026-01-01T00:00:00Z');recordPage(log,{kind:'page',tab:tab2},'2026-01-01T00:00:05Z');
  recordPage(log,{kind:'heartbeat',tab},'2026-01-01T00:00:15Z');recordPage(log,{kind:'hidden',tab:tab2},'2026-01-01T00:00:20Z');
  recordPage(log,{kind:'heartbeat',tab},'2026-01-01T00:01:00Z');
  const state={status:'playing',science:1,history:[]};assert.equal(summarize(log,state).visibleMs,35000);
  log.completedAt='2026-01-01T00:00:25Z';assert.equal(summarize(log,state).visibleMs,25000);
  log.legacy=true;assert.equal(summarize(log,state).elapsedMs,null);assert.equal(summarize(log,state).visibleMs,null);
  assert.throws(()=>recordPage(log,{kind:'secret',tab}));
});
test('ordered private actions, errors, migration and local admin access survive restart without public leakage',async()=>{
  const directory=mkdtempSync(join(tmpdir(),'lab-admin-')),sessions=join(directory,'sessions');
  const fixturePath=new URL('./fixture.json',import.meta.url),fixture=JSON.parse(readFileSync(fixturePath));writeFileSync(join(directory,'fixture.json'),JSON.stringify(fixture));
  let server=createLab({fixturePath,stateDirectory:sessions});await listen(server);let panel;
  try {
    const first=await req(server,'/api/state'),cookie=first.headers['set-cookie'][0].split(';')[0],id=cookie.split('=')[1];
    const legacy=JSON.parse(readFileSync(join(sessions,id+'.json')));delete legacy.telemetry;writeFileSync(join(sessions,id+'.json'),JSON.stringify(legacy));
    await close(server);server=createLab({fixturePath,stateDirectory:sessions});await listen(server);
    await req(server,'/api/state',undefined,{Cookie:cookie});
    const tab='11111111-1111-1111-1111-111111111111';
    assert.equal((await req(server,'/api/events',{kind:'page',tab},{Cookie:cookie})).status,200);
    const action={type:'toggleSelect',slot:fixture.slots[0].id,card:fixture.slots[0].cards[0].id};
    assert.equal((await req(server,'/api/action',action,{Cookie:cookie})).status,200);
    assert.equal((await req(server,'/api/action',{type:'toggleSelect',slot:'invalid',card:'invalid'},{Cookie:cookie})).status,400);
    const stored=JSON.parse(readFileSync(join(sessions,id+'.json')));
    assert.equal(stored.telemetry.legacy,true);assert.deepEqual(stored.telemetry.events.map(e=>e.seq),[1,2,3]);
    assert.deepEqual(stored.telemetry.events.map(e=>e.kind),['page','action','action_rejected']);
    const publicResult=await req(server,'/api/state',undefined,{Cookie:cookie});assert.ok(!publicResult.text.includes('nickname'));assert.ok(!publicResult.text.includes('recordingStartedAt'));
    for(const path of ['/admin.mjs','/admin-ui.mjs','/telemetry.mjs','/api/overview','/api/export'])assert.equal((await req(server,path)).status,404);
    await close(server);server=createLab({fixturePath,stateDirectory:sessions});await listen(server);
    assert.deepEqual(JSON.parse((await req(server,'/api/state',undefined,{Cookie:cookie})).text).state,stored.state);
    let commands=[];panel=createAdmin({privateDirectory:directory,control:async mode=>{commands.push(mode);return {stdout:'ok'};}});await listen(panel);
    const overview=await req(panel,'/api/overview');assert.equal(overview.status,200);assert.ok(!overview.text.includes(id));
    assert.equal(JSON.parse(overview.text).totals.sessions,1);
    assert.equal((await req(panel,'/api/control',{mode:'Stop'},{Origin:'https://evil.example'})).status,403);assert.equal(commands.length,0);
    assert.equal((await req(panel,'/api/control',{mode:'arbitrary-shell'})).status,400);assert.equal(commands.length,0);
    assert.equal((await req(panel,'/api/control',{mode:'Status'})).status,200);assert.deepEqual(commands,['Status']);
    assert.equal((await req(panel,'/api/overview',undefined,{Host:'public.ngrok-free.dev'})).status,403);
    assert.equal((await req(panel,'/api/tag',{key:sessionKey(id),kind:'test'})).status,200);
    assert.equal(snapshot(directory).totals.sessions,0);assert.equal(snapshot(directory).sessions[0].kind,'test');
    const exported=await req(panel,'/api/export');assert.equal(exported.status,200);assert.ok(!exported.text.includes(id));assert.ok(!Object.hasOwn(JSON.parse(exported.text).fixture,'answer'));
    assert.equal(readdirSync(sessions).length,1);
  }finally{await close(server);if(panel)await close(panel);rmSync(directory,{recursive:true,force:true});}
});
