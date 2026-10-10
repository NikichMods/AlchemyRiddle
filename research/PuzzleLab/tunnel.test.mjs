// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import {mkdtempSync, rmSync, readFileSync, readdirSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createLab} from './server.mjs';
const publicOrigin = 'https://bounded-playtest.trycloudflare.com';
const fixturePath = new URL('./fixtures/harbor-06.json',import.meta.url);
const fixture = JSON.parse(readFileSync(fixturePath));
function request(server,path='/api/state',options={}) {
  return new Promise((resolve,reject)=>{
    const req=http.request({hostname:'127.0.0.1',port:server.address().port,path,method:options.body===undefined?'GET':'POST',headers:{Host:new URL(publicOrigin).host,...options.headers}},res=>{
      let body='';res.on('data',c=>body+=c);res.on('end',()=>resolve({status:res.statusCode,headers:res.headers,body}));
    });req.on('error',reject);req.end(options.body);
  });
}
const listen=server=>new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
const close=server=>new Promise(resolve=>server.close(resolve));
test('public configuration rejects wildcard/bad origins, debug, reload and missing persistence',()=>{
  const stateDirectory=tmpdir();
  for(const overrides of [{publicOrigin:'http://bounded-playtest.trycloudflare.com'},{publicOrigin:'https://elsewhere.example'},{publicOrigin:publicOrigin+'/'},{debug:true},{liveReload:true},{stateDirectory:undefined}])
    assert.throws(()=>createLab({fixturePath,publicOrigin,stateDirectory,...overrides}));
});
test('ngrok requires explicit exact approval and keeps other hosts forbidden',async()=>{
  const directory=mkdtempSync(join(tmpdir(),'lab-ngrok-'));
  const origin='https://selected-playtest.ngrok-free.dev';
  assert.throws(()=>createLab({fixturePath,publicOrigin:origin,stateDirectory:directory}));
  assert.throws(()=>createLab({fixturePath,publicOrigin:origin,approvedNgrokOrigin:'https://other.ngrok-free.dev',stateDirectory:directory}));
  const server=createLab({fixturePath,publicOrigin:origin,approvedNgrokOrigin:origin,stateDirectory:directory});await listen(server);
  const headers={Host:new URL(origin).host};
  try {
    const a=await request(server,'/api/state',{headers}),b=await request(server,'/api/state',{headers});
    assert.equal(a.status,200);assert.equal(b.status,200);
    assert.notEqual(a.headers['set-cookie'][0],b.headers['set-cookie'][0]);
    assert.match(a.headers['set-cookie'][0],/; Secure; Max-Age=2592000$/);
    for(const path of ['/api/debug','/facilitator','/fixture.json','/rules.mjs']) assert.equal((await request(server,path,{headers})).status,404);
    for(const altered of [{Host:'other.ngrok-free.dev'},{Origin:'https://other.ngrok-free.dev'},{'Sec-Fetch-Site':'cross-site'}])
      assert.equal((await request(server,'/api/state',{headers:{...headers,...altered}})).status,403);
    const cookie=a.headers['set-cookie'][0].split(';')[0];
    const actionHeaders={...headers,Cookie:cookie,Origin:origin,'Content-Type':'application/json'};
    const body=JSON.stringify({type:'select',slot:'powder',card:'p1'});
    assert.equal((await request(server,'/api/action',{headers:{...actionHeaders,Origin:''},body})).status,403);
    const changed=await request(server,'/api/action',{headers:actionHeaders,body});assert.equal(changed.status,200);
    assert.equal(JSON.parse(changed.body).state.selected.powder,'p1');
    assert.deepEqual(JSON.parse((await request(server,'/api/state',{headers:{...headers,Cookie:b.headers['set-cookie'][0].split(';')[0]}})).body).state,JSON.parse(b.body).state);
  } finally {await close(server);rmSync(directory,{recursive:true,force:true});}
});
test('exact tunnel origin, request boundary, spoiler separation and two durable players',async()=>{
  const directory=mkdtempSync(join(tmpdir(),'lab-tunnel-'));
  let server=createLab({fixturePath,publicOrigin,stateDirectory:directory});await listen(server);
  try {
    const a=await request(server),b=await request(server);
    assert.equal(a.status,200);assert.equal(b.status,200);
    const cookie=a.headers['set-cookie'][0].split(';')[0];
    assert.notEqual(cookie,b.headers['set-cookie'][0].split(';')[0]);
    assert.match(a.headers['set-cookie'][0],/^__Host-lab=.*HttpOnly; SameSite=Strict; Path=\/; Secure; Max-Age=2592000$/);
    assert.equal(a.headers['cache-control'],'no-store');
    const local=await request(server,'/api/state',{headers:{Host:`127.0.0.1:${server.address().port}`}});
    assert.match(local.headers['set-cookie'][0],/^lab_playtest=.*Max-Age=2592000$/);
    for(const secret of ['answer','stablePairs','fixtureHash','sessions']) assert.ok(!Object.hasOwn(JSON.parse(a.body),secret));
    assert.ok(!a.body.includes('stablePairs'));
    for(const path of ['/api/debug','/facilitator','/fixture.json','/rules.mjs','/FACILITATOR.md','/fixtures/harbor-06.json','/sessions/anything.json','/../server.mjs']) assert.equal((await request(server,path)).status,404);
    for(const headers of [{Host:'unselected.trycloudflare.com'},{Host:'evil.example'},{Origin:'https://evil.example'},{'Sec-Fetch-Site':'cross-site'}]) assert.equal((await request(server,'/api/state',{headers})).status,403);
    const headers={Cookie:cookie,Origin:publicOrigin,'Content-Type':'application/json'};
    for(const altered of [{Origin:''},{Origin:'http://bounded-playtest.trycloudflare.com'},{Origin:'https://another.trycloudflare.com'}]) assert.equal((await request(server,'/api/action',{headers:{...headers,...altered},body:'{}'})).status,403);
    assert.equal((await request(server,'/api/action',{headers:{...headers,'Content-Type':'text/plain'},body:'{}'})).status,415);
    const action=async body=>request(server,'/api/action',{headers,body:JSON.stringify(body)});
    assert.equal((await action({type:'select',slot:'powder',card:'p1'})).status,200);
    await action({type:'select',slot:'fluid',card:'f1'});
    await action({type:'pairTest',slots:['powder','fluid']});
    const current=JSON.parse((await request(server,'/api/state',{headers:{Cookie:cookie}})).body);
    assert.equal(current.state.history.length,1);
    assert.deepEqual(JSON.parse((await request(server,'/api/state',{headers:{Cookie:b.headers['set-cookie'][0].split(';')[0]}})).body).state,JSON.parse(b.body).state);
    assert.equal(readdirSync(directory).length,3);
    // Slow request from one tab must not erase an action committed by another.
    const slowBody=JSON.stringify({type:'notes',text:'parallel-tab-check'});
    let slow;
    const slowResult=new Promise((resolve,reject)=>{
      slow=http.request({hostname:'127.0.0.1',port:server.address().port,path:'/api/action',method:'POST',headers:{Host:new URL(publicOrigin).host,...headers}},res=>{
        let body='';res.on('data',c=>body+=c);res.on('end',()=>resolve({status:res.statusCode,body}));
      });slow.on('error',reject);slow.write(slowBody.slice(0,10));
    });
    await action({type:'select',slot:'essence',card:'e1'});
    slow.end(slowBody.slice(10));
    const concurrent=await slowResult;assert.equal(concurrent.status,200);
    assert.equal(JSON.parse(concurrent.body).state.selected.essence,'e1');
    assert.equal(JSON.parse(concurrent.body).state.notes,'parallel-tab-check');
    const bad=await request(server,'/api/action',{headers,body:'{'});assert.equal(bad.status,400);assert.ok(!bad.body.includes(directory));
    await close(server);server=createLab({fixturePath,publicOrigin,stateDirectory:directory});await listen(server);
    assert.deepEqual(JSON.parse((await request(server,'/api/state',{headers:{Cookie:cookie}})).body),JSON.parse(concurrent.body));
  } finally {await close(server);rmSync(directory,{recursive:true,force:true});}
});

test('external links can open only the top-level public document',async()=>{
  for(const origin of [publicOrigin,'https://selected-playtest.ngrok-free.dev']) {
    const directory=mkdtempSync(join(tmpdir(),'lab-navigation-'));
    const server=createLab({fixturePath,publicOrigin:origin,approvedNgrokOrigin:origin,stateDirectory:directory});await listen(server);
    const headers={Host:new URL(origin).host,'Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'navigate','Sec-Fetch-Dest':'document'};
    try {
      const page=await request(server,'/',{headers});assert.equal(page.status,200);assert.ok(page.headers['content-type'].startsWith('text/html'));
      assert.equal(page.headers['content-security-policy'].includes("frame-ancestors 'none'"),true);
      assert.equal(page.headers['set-cookie'],undefined);
      for(const path of ['/api/state','/app.mjs','/api/debug','/facilitator']) assert.equal((await request(server,path,{headers})).status,403);
      for(const altered of [{'Sec-Fetch-Dest':'iframe'},{'Sec-Fetch-Mode':'cors'},{'Sec-Fetch-Dest':''},{Origin:'https://evil.example'},{Host:'other.ngrok-free.dev'}])
        assert.equal((await request(server,'/',{headers:{...headers,...altered}})).status,403);
      for(const path of ['/','/api/action','/api/events']) assert.equal((await request(server,path,{headers:{...headers,Origin:origin,'Content-Type':'application/json'},body:'{}'})).status,403);
    } finally {await close(server);rmSync(directory,{recursive:true,force:true});}
  }
});
