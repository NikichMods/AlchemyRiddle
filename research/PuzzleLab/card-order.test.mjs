// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';import assert from 'node:assert/strict';
import {prepareCardOrder,orderPenalty} from './card-order.mjs';
import {selectedPairStates} from './support.mjs';
const f={id:'order-test',slots:['powder','fluid','essence'].map((id,i)=>({id,cards:[1,2,3].map(n=>({id:id+n,tags:[]}))})),clues:[],answer:{powder:'powder1',fluid:'fluid1',essence:'essence1'}};
test('soft order preference reduces expected early-hit score, preserves every model fact and is reproducible',()=>{
  const frozen=structuredClone(f),a=prepareCardOrder(f,{maxCandidates:256,seed:12}),b=prepareCardOrder(f,{maxCandidates:256,seed:12});
  assert.deepEqual(a,b);assert.deepEqual(f,frozen);assert.equal(a.audit.candidates,216);
  assert.ok(a.audit.weightedExpectedPenalty<a.audit.uniformExpectedPenalty);
  for(const s of f.slots)assert.deepEqual(a.fixture.slots.find(x=>x.id===s.id).cards.toSorted((a,b)=>a.id.localeCompare(b.id)),s.cards);
  assert.deepEqual(a.fixture.answer,f.answer);assert.deepEqual(a.fixture.clues,f.clues);
  const neutral=prepareCardOrder(f,{strength:0,maxCandidates:256});assert.equal(neutral.audit.weightedExpectedPenalty,neutral.audit.uniformExpectedPenalty);
  let early=0;for(let seed=0;seed<100;seed++){const r=prepareCardOrder(f,{seed,maxCandidates:256}).audit.selectedRanks[0];if(r.forward===1||r.reverse===1)early++;}
  assert.ok(early>0,'penalty must not become a hard ban');
});
test('public pruning excludes known negatives, does not require all stable priors, and scores both directions',()=>{
  const prior={slots:['powder','fluid'],tuple:{powder:'powder2',fluid:'fluid2'},stable:true};
  const p={...f,knownRelations:[prior,{slots:['fluid','essence'],tuple:{fluid:'fluid2',essence:'essence2'},stable:false}]};
  const a=orderPenalty(p);assert.equal(a.ranks[0].count,24);assert.equal(a.ranks.length,1);assert.equal(a.ranks[0].forward,1);assert.equal(a.ranks[0].reverse,24);
  const relevant={...prior,tuple:{powder:'powder1',fluid:'fluid1'}};
  assert.equal(orderPenalty({...p,knownRelations:[relevant]}).ranks[1].count,3);
});
test('single possible hypothesis and invalid options are handled without changing the puzzle',()=>{
  const single={...f,slots:f.slots.map(s=>({...s,cards:s.cards.slice(0,1)}))};assert.equal(prepareCardOrder(single).audit.selectedPenalty,1);
  assert.throws(()=>prepareCardOrder(f,{strength:Infinity}));assert.throws(()=>prepareCardOrder(f,{maxCandidates:0}));
});
test('liquid has independent public left/right verdicts and unknown/incomplete never inherits another partner',()=>{
  const view={slots:f.slots,pairTestCost:2,state:{selected:{...f.answer},knownRelations:[{slots:['powder','fluid'],tuple:{...f.answer},stable:true},{slots:['fluid','essence'],tuple:{...f.answer},stable:false}]}};
  assert.deepEqual(selectedPairStates(view,'fluid').map(x=>x.status),['stable','incompatible']);
  view.state.selected.essence='essence2';assert.deepEqual(selectedPairStates(view,'fluid').map(x=>x.status),['stable','unknown']);
  delete view.state.selected.powder;assert.deepEqual(selectedPairStates(view,'fluid').map(x=>x.status),['incomplete','unknown']);
  assert.deepEqual(selectedPairStates(view,'essence').map(x=>x.status),['unknown','unknown']);
});
