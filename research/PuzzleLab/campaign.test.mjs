// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,readFileSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {randomUUID} from 'node:crypto';
import {createCampaign} from './campaign.mjs';
import {createLab} from './server.mjs';

function fixture(arity=3,changed=false){
  const keys=['powder','fluid','essence'].slice(0,arity);
  const labels=['Порошок','Жидкость','Эссенция'];
  const result={id:'synthetic',title:'Учебный препарат',description:'Синтетическое доказательство контракта',
    slots:keys.map((id,i)=>({id,name:labels[i],cards:['a','b'].map((letter,n)=>({id:`${id}-${changed?'new-':''}${letter}`,globalId:`global-${id}-${letter}`,name:letter,tags:n?['B']:['A']}))})),
    clues:[{kind:'exactly',count:1,terms:[{slot:'powder',tag:'A'}]},{kind:'exactly',count:1,terms:[{slot:keys.at(-1),tag:'A'}]}],
    science:20,submissionCost:5,economy:{mode:'sharedScience',refillAmount:10},researchSupport:{version:1}};
  result.answer=Object.fromEntries(result.slots.map(s=>[s.id,s.cards[0].id]));
  if(arity===3)result.compatibility={stablePairs:[result.slots[0].cards[0].id+':'+result.slots[1].cards[0].id,result.slots[1].cards[0].id+':'+result.slots[2].cards[0].id]},result.knownRelations=[],result.pairTestCost=2;
  if(changed)for(const slot of result.slots)slot.cards.reverse();
  return result;
}
function setup(t,{developer=false,selector}={}){
  const dir=mkdtempSync(join(tmpdir(),'alchemy-campaign-contract-'));t.after(()=>rmSync(dir,{recursive:true,force:true}));
  const stages=Array.from({length:5},(_,i)=>({id:`slice-${i+1}`,arity:i<2?2:3,rung:i<2?i+1:i-1,band:'Лёгкая',purpose:'Проверка',separate:i===4}));
  const bank={version:1,id:'synthetic-campaign',worldId:'synthetic-world',packages:[{fixture:fixture()}],stages,
    checkpoint:[{edge:['PF','global-powder-a','global-fluid-a'],stable:true,source:'seeded:mature-v1'}]};
  const bankPath=join(dir,'bank.json');writeFileSync(bankPath,JSON.stringify(bank));
  const requests=[];
  const select=async request=>{
    requests.push(structuredClone(request));
    if(selector){const result=await selector(request);if(result)return result;}
    const stage=stages.find(s=>s.id===request.stage),f=fixture(stage.arity,request.stage==='slice-4');f.id=request.stage+':'+randomUUID();
    return {status:'selected',fixture:f,packageId:request.stage,targetKey:request.stage,route:{mean:2}};
  };
  const campaign=createCampaign({bankPath,developer,select});return {campaign,dir,requests};
}
async function act(c,p,body){return c.action(p,{...body,revision:p.revision,puzzleId:p.active.fixture.id,actionId:randomUUID()});}
async function solve(c,p){for(const [slot,card] of Object.entries(p.active.fixture.answer))await act(c,p,{type:'select',slot,card});await act(c,p,{type:'submit'});}

test('real paid outcomes, both polarities, formula facts, progression and global identity survive serialization',async t=>{
  const {campaign:c,requests}=setup(t),p=await c.create();
  await solve(c,p);assert.equal(p.spent,5);assert.equal(p.knowledge.length,0);
  await act(c,p,{type:'continue'});assert.equal(p.science,15);assert.equal(p.active.state.science,15);
  await solve(c,p);await act(c,p,{type:'continue'});
  const f=p.active.fixture;
  await act(c,p,{type:'select',slot:'powder',card:f.slots[0].cards[0].id});
  await act(c,p,{type:'select',slot:'fluid',card:f.slots[1].cards[1].id});
  await act(c,p,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(p.knowledge.length,1);assert.equal(p.knowledge[0].stable,false);assert.equal(p.spent,12);
  await act(c,p,{type:'select',slot:'essence',card:f.slots[2].cards[0].id});
  await act(c,p,{type:'submit'});assert.equal(p.knowledge.length,1);assert.equal(p.spent,17);
  await act(c,p,{type:'refill'});assert.equal(p.spent,17);assert.equal(p.refills,1);assert.equal(p.refilledScience,10);
  await solve(c,p);assert.equal(p.knowledge.length,3);assert.equal(p.spent,22);
  assert.ok(p.knowledge.filter(x=>x.stable).every(x=>x.sources.some(s=>s.endsWith(':solved'))));
  await act(c,p,{type:'continue'});
  assert.equal(requests.at(-1).knowledge.length,3);
  assert.equal(p.active.state.knownRelations.length,3);
  assert.ok(p.active.state.knownRelations.every(r=>Object.values(r.tuple).every(id=>id.includes('new-'))));
  assert.deepEqual(JSON.parse(JSON.stringify(p)),p);
  const before=p.spent;
  const observed=p.active.state.knownRelations[0];
  for(const [slot,card] of Object.entries(observed.tuple))await act(c,p,{type:'select',slot,card});
  await act(c,p,{type:'pairTest',slots:observed.slots});assert.equal(p.spent,before);
  assert.equal(p.completed.length,3);
});

test('empty pool leaves frozen investigation intact; known target bypasses without spending',async t=>{
  let mode='normal';const {campaign:c}=setup(t,{selector:r=>r.stage==='slice-2'?{status:mode==='empty'?'empty_suitable_pool':'known_target'}:null});
  const p=await c.create();await solve(c,p);mode='empty';
  const before=structuredClone(p);await assert.rejects(()=>act(c,p,{type:'continue'}),/Нет подходящего/);assert.deepEqual(p,before);
  mode='known';await act(c,p,{type:'continue'});assert.equal(p.active.stage.id,'slice-3');assert.equal(p.spent,5);assert.equal(p.skipped[0].reason,'known_target');
});

test('developer checkpoints are explicitly seeded and isolated; player cannot access them',async t=>{
  const {campaign:c}=setup(t),{campaign:d}=setup(t,{developer:true}),p=await c.create(),sandbox=await d.create(4);
  assert.equal(p.knowledge.length,0);assert.equal(sandbox.knowledge.length,1);assert.equal(sandbox.spent,0);assert.equal(sandbox.completed.length,0);
  assert.match(d.view(sandbox).campaign.checkpoint,/явно заданных/);
  await assert.rejects(()=>act(c,p,{type:'checkpoint',stage:'slice-5'}),/частной/);
  await act(d,sandbox,{type:'checkpoint',stage:'slice-3'});assert.equal(sandbox.knowledge.length,0);assert.equal(sandbox.spent,0);
  assert.equal(c.view(p).campaign.stages,undefined);assert.ok(d.view(sandbox).campaign.stages);
});

test('HTTP isolation, hidden model boundary, duplicate/stale/two-tab actions, denied costs and restart',async t=>{
  const {campaign,dir}=setup(t);
  const storage=join(dir,'sessions');
  let server=createLab({campaign,stateDirectory:storage});
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  let base=`http://127.0.0.1:${server.address().port}`;
  const a=await fetch(base+'/api/state'),cookie=a.headers.get('set-cookie').split(';')[0],initial=await a.json();
  assert.match(a.headers.get('set-cookie'),/Max-Age/);
  const b=await (await fetch(base+'/api/state')).json();assert.notEqual(initial.id,b.id);
  const post=async(body)=>{
    const r=await fetch(base+'/api/action',{method:'POST',headers:{cookie,'content-type':'application/json',origin:base},body:JSON.stringify(body)});return {status:r.status,view:await r.json()};
  };
  const envelope=body=>({...body,revision:initial.campaign.revision,puzzleId:initial.campaign.puzzleId,actionId:randomUUID()});
  const refill=envelope({type:'refill'});
  const [one,two]=await Promise.all([post(refill),post(refill)]);
  assert.equal(one.status,200);assert.equal(two.status,200);assert.equal(two.view.state.science,30);assert.equal(two.view.campaign.refills,1);
  const stale=await post(envelope({type:'refill'}));assert.equal(stale.status,400);
  let current=await (await fetch(base+'/api/state',{headers:{cookie}})).json();
  const denied=await post({type:'submit',revision:current.campaign.revision,puzzleId:current.campaign.puzzleId,actionId:randomUUID()});assert.equal(denied.status,400);
  current=await (await fetch(base+'/api/state',{headers:{cookie}})).json();assert.equal(current.campaign.spent,0);
  const serial=JSON.stringify(current);for(const secret of ['answer','stablePairs','manifest','targetKey','packageId','route','reverse-mapping'])assert.ok(!serial.includes('"'+secret+'"'));
  const debug=await fetch(base+'/api/debug');assert.equal(debug.status,404);
  await new Promise(r=>server.close(r));
  server=createLab({campaign,stateDirectory:storage});await new Promise(r=>server.listen(0,'127.0.0.1',r));base=`http://127.0.0.1:${server.address().port}`;
  const restored=await (await fetch(base+'/api/state',{headers:{cookie}})).json();assert.deepEqual(restored,current);
  await new Promise(r=>server.close(r));
});
