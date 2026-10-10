// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, mkdtempSync, rmSync, readdirSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {act, createState, publicView, validate} from './rules.mjs';
import {createLab} from './server.mjs';
const historical = JSON.parse(readFileSync(new URL('./fixtures/harbor-06.json',import.meta.url)));
const shared = {...historical,science:7,pairTestCost:2,submissionCost:5,
  economy:{mode:'sharedScience',refillAmount:10}};

test('shared Science pays for pairs and whole formula; known pair stays free', () => {
  validate(shared); const state=createState(shared);
  assert.equal(state.research,undefined);
  state.selected={...shared.answer};
  act(shared,state,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(state.science,5);
  act(shared,state,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(state.science,5);assert.equal(state.history.length,1);
  act(shared,state,{type:'submit'});
  assert.equal(state.science,0);assert.equal(state.status,'solved');
  assert.throws(()=>act(shared,state,{type:'refill'}));
  assert.equal(publicView(shared,state).economy.refillAmount,10);
});

test('failed whole check at zero Science permits refill, preserving observations', () => {
  const f={...shared,science:5};const state=createState(f);
  state.selected={powder:'p1',fluid:'f3',essence:'e2'};
  act(f,state,{type:'submit'});
  assert.equal(state.status,'playing');assert.equal(state.science,0);
  const before=structuredClone(state);
  assert.throws(()=>act(f,state,{type:'submit'}));assert.deepEqual(state,before);
  act(f,state,{type:'refill'});
  assert.equal(state.science,10);assert.deepEqual(state.knownRelations,before.knownRelations);
  assert.deepEqual(state.selected,before.selected);assert.equal(state.history.length,2);
  assert.throws(()=>act(historical,createState(historical),{type:'refill'}));
});

test('shared partial/invalid actions do not spend Science or reveal outcomes', () => {
  const state=createState(shared);const before=structuredClone(state);
  assert.throws(()=>act(shared,state,{type:'pairTest',slots:['powder','essence']}));
  assert.throws(()=>act(shared,state,{type:'pairTest',slots:['powder','fluid']}));
  assert.throws(()=>act(shared,state,{type:'submit'}));
  assert.deepEqual(state,before);
  const broken={...shared,economy:{mode:'sharedScience',refillAmount:-1}};
  assert.throws(()=>validate(broken));
});

test('finite shared Science denies refill and ends after unaffordable final check', () => {
  const f={...shared,economy:{mode:'sharedScience',refillAmount:0}};
  validate(f);const state=createState(f),before=structuredClone(state);
  assert.throws(()=>act(f,state,{type:'refill'}),/недоступно/);
  assert.deepEqual(state,before);
  state.selected={...f.answer};
  act(f,state,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(state.science,5);assert.equal(state.status,'playing');
  state.selected.essence=f.slots.find(s=>s.id==='essence').cards.find(c=>
    !state.knownRelations.some(r=>r.tuple.fluid===state.selected.fluid && r.tuple.essence===c.id)).id;
  act(f,state,{type:'pairTest',slots:['fluid','essence']});
  assert.equal(state.science,3);assert.equal(state.status,'exhausted');
  assert.throws(()=>act(f,state,{type:'submit'}));
});

test('finite shared Science preserves failure observations and permits success on last Science', () => {
  const f={...shared,science:10,economy:{mode:'sharedScience',refillAmount:0}};
  const state=createState(f);
  state.selected={powder:'p1',fluid:'f3',essence:'e2'};
  act(f,state,{type:'submit'});assert.equal(state.status,'playing');
  state.selected={...f.answer};act(f,state,{type:'submit'});
  assert.equal(state.status,'solved');assert.equal(state.science,0);
  assert.equal(state.history.length,2);
  const failed=createState({...f,science:5});
  failed.selected={powder:'p1',fluid:'f3',essence:'e2'};
  act(f,failed,{type:'submit'});assert.equal(failed.status,'exhausted');
});

test('persisted HTTP state resumes with cookie and cannot restore under changed fixture', async t => {
  const dir=mkdtempSync(join(tmpdir(),'alchemy-lab-state-'));
  t.after(()=>rmSync(dir,{recursive:true,force:true}));
  const fixturePath=new URL('./fixtures/harbor-06.json',import.meta.url);
  const start=async path=>{
    const server=createLab({fixturePath:path,stateDirectory:dir});
    await new Promise(r=>server.listen(0,'127.0.0.1',r));
    const close=()=>new Promise(r=>{server.close(r);server.closeAllConnections();});
    return {server,close,base:`http://127.0.0.1:${server.address().port}`};
  };
  const first=await start(fixturePath);
  const response=await fetch(first.base+'/api/state');
  const cookie=response.headers.get('set-cookie').split(';')[0];
  const headers={Cookie:cookie,'Content-Type':'application/json'};
  const changed=await (await fetch(first.base+'/api/action',{method:'POST',headers,
    body:JSON.stringify({type:'select',slot:'powder',card:'p1'})})).json();
  await first.close();
  const second=await start(fixturePath);
  const restored=await (await fetch(second.base+'/api/state',{headers})).json();
  assert.deepEqual(restored.state,changed.state);
  for (const path of ['/api/debug','/facilitator','/rules.mjs'])
    assert.equal((await fetch(second.base+path)).status,404);
  assert.equal(readdirSync(dir).filter(x=>x.endsWith('.json')).length,1);
  await second.close();
  const third=await start(new URL('./fixture.json',import.meta.url));
  try {
    const fresh=await (await fetch(third.base+'/api/state',{headers})).json();
    assert.deepEqual(fresh.state.selected,{});
  } finally {await third.close();}
});
