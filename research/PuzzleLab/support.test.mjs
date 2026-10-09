// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {act,candidates,createState,publicView,satisfies,validFormula,validate} from './rules.mjs';
import {submitBlockReason,selectedSubmission,submissions,compositionReminder,submissionFeedback} from './support.mjs';
const fixture=JSON.parse(readFileSync(new URL('./fixture.json',import.meta.url)));
const harbor=JSON.parse(readFileSync(new URL('./fixtures/harbor-06.json',import.meta.url)));
const supported=f=>({...f,science:20,submissionCost:5,economy:{mode:'sharedScience',refillAmount:10},researchSupport:{version:1}});

test('fresh result survives refresh; leaving and reselecting shows repeat warning; paid repeat is fresh',()=>{
  const f=supported(fixture),state=createState(f);
  const wrong=candidates(f).find(t=>!validFormula(f,t));state.selected=wrong;
  assert.deepEqual(submissionFeedback(publicView(f,state)),{fresh:false,revisited:false});
  act(f,state,{type:'submit'});
  assert.deepEqual(submissionFeedback(publicView(f,JSON.parse(JSON.stringify(state)))),{fresh:true,revisited:false});
  state.selected={...f.answer};
  assert.deepEqual(submissionFeedback(publicView(f,state),1),{fresh:false,revisited:false});
  state.selected=wrong;
  assert.deepEqual(submissionFeedback(publicView(f,state),1),{fresh:false,revisited:true});
  act(f,state,{type:'submit'});
  assert.deepEqual(submissionFeedback(publicView(f,state),1),{fresh:true,revisited:false});
});

test('composition reminder is paid-only, post-submission, nonspecific and opt-in',()=>{
  const f=supported(fixture);validate(f);
  const wrong=candidates(f).find(t=>!f.clues.every(c=>satisfies(f,t,c)));
  const state=createState(f);state.selected=wrong;
  assert.deepEqual(submissions(publicView(f,state)),[]);
  assert.ok(!('compositionMismatch' in publicView(f,state)));
  act(f,state,{type:'submit'});
  assert.equal(state.science,15);assert.equal(state.history[0].compositionMismatch,true);
  assert.equal(compositionReminder(state.history[0]),'Сверьте выбранные компоненты со сведениями о составе.');
  assert.ok(!('clueSatisfied' in state.history[0]));
  const old={...f};delete old.researchSupport;
  const legacy=createState(old);legacy.selected=wrong;act(old,legacy,{type:'submit'});
  assert.ok(!('compositionMismatch' in legacy.history[0]));assert.equal(compositionReminder(legacy.history[0]),'');
  assert.throws(()=>validate({...f,researchSupport:{version:2}}));
});

test('tag-valid chemical failure and success receive no composition reminder',()=>{
  const f=supported(harbor);validate(f);
  const wrong=candidates(f).find(t=>f.clues.every(c=>satisfies(f,t,c))&&!validFormula(f,t));
  assert.ok(wrong);
  const state=createState(f);state.selected=wrong;act(f,state,{type:'submit'});
  assert.equal(state.history[0].success,false);assert.equal(state.history[0].compositionMismatch,false);
  assert.equal(compositionReminder(state.history[0]),'');
  state.selected={...f.answer};act(f,state,{type:'submit'});
  assert.equal(state.status,'solved');assert.equal(compositionReminder(state.history[1]),'');
  assert.ok(!('compositionMismatch' in state.history[1]));
});

test('button explains incomplete selection, low Science and completion; refill restores eligibility',()=>{
  const f=supported(fixture),state=createState(f);
  assert.match(submitBlockReason(publicView(f,state)),/Выберите/);
  state.selected={...f.answer};state.science=3;
  assert.equal(submitBlockReason(publicView(f,state)),'Не хватает Science: нужно 5, в запасе 3. Пополните запас.');
  act(f,state,{type:'refill'});assert.equal(submitBlockReason(publicView(f,state)),'');
  act(f,state,{type:'submit'});assert.equal(submitBlockReason(publicView(f,state)),'Исследование завершено.');
});

test('mixture history remembers exact tuples, refresh projection and paid repeat semantics',()=>{
  const f=supported(fixture),state=createState(f);
  const wrong=candidates(f).find(t=>!validFormula(f,t));state.selected=wrong;
  act(f,state,{type:'submit'});let view=publicView(f,state);
  assert.deepEqual(selectedSubmission(view).tuple,wrong);assert.equal(selectedSubmission(view).success,false);
  assert.equal(submitBlockReason(view),'');
  state.selected={...f.answer};assert.equal(selectedSubmission(publicView(f,state)),undefined);
  state.selected=wrong;act(f,state,{type:'submit'});
  view=publicView(f,JSON.parse(JSON.stringify(state)));
  assert.equal(submissions(view).length,2);assert.equal(view.state.science,10);
  assert.deepEqual(submissions(view).map(h=>h.tuple),[wrong,wrong]);
});
