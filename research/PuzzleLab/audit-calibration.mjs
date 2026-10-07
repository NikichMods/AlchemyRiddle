// SPDX-License-Identifier: MPL-2.0
// Offline aggregate audit. Never served to the player; no answer tuples in output.
import assert from 'node:assert/strict';
import {readFileSync, writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {candidates, satisfies, validFormula, validate, createState, act} from './rules.mjs';

const cases = [
  ['fixture.json', 'revise-onboarding', []],
  ['fixtures/amber-02.json', 'rejected-repetition; solution narrated, submission unobserved', []],
  ['fixtures/mist-03.json', 'accepted-initial', []],
  ['fixtures/ink-04.json', 'accepted', []],
  ['fixtures/dew-05.json', 'accepted', []],
  ['fixtures/harbor-06.json', 'accepted', ['f3:e2','f1:e1','p2:f2']],
  ['fixtures/lantern-07.json', 'accepted', ['f2:e1','f2:e3','p2:f3']],
  ['fixtures/tide-08.json', 'failed; UI-confounded', []],
  ['fixtures/lantern-09.json', 'accepted', ['p3:f1','f1:e1','f1:e3','p2:f2','f2:e1']],
  ['fixtures/depth-10.json', 'accepted', ['p1:f2','p1:f3','f3:e1','f3:e3','p1:f4','f4:e1']]
];
const reports = cases.map(([path, humanOutcome, recordedProbes]) => {
  const bytes = readFileSync(new URL(path, import.meta.url));
  const f = JSON.parse(bytes); validate(f);
  const all = candidates(f);
  const tagsFit = (t, clues=f.clues) => clues.every(c=>satisfies(f,t,c));
  const matches = (t,r) => r.slots.every(id=>t[id]===r.tuple[id]);
  const state = createState(f);
  // Positive observations certify local edges; they do not require using those edges.
  const unrefuted = () => all.filter(t=>tagsFit(t) && !(state.knownRelations??[]).some(r=>!r.stable && matches(t,r)));
  const certified = () => unrefuted().filter(t=>f.slots.slice(0,-1).every((s,i)=>
    state.knownRelations.some(r=>r.stable && r.slots[0]===s.id && r.slots[1]===f.slots[i+1].id && matches(t,r))));
  const clueAudit = f.clues.map((clue,i)=>{
    const reduced=f.clues.filter((_,j)=>i!==j);
    const terms=clue.kind==='exactly'?clue.terms:clue.kind==='implies'?[clue.if,clue.then]:clue.kind==='notTogether'?[clue.left,clue.right]:[];
    return {kind:clue.kind, count:clue.count??null,
      tagOnlySurvivorsWhenOmitted:all.filter(t=>tagsFit(t,reduced)).length,
      fullModelSurvivorsWhenOmitted:all.filter(t=>validFormula({...f,clues:reduced},t)).length,
      fixedTerms:terms.map(term=>({slot:term.slot, property:term.tag,
        matches:f.slots.find(s=>s.id===term.slot).cards.filter(c=>c.tags.includes(term.tag)).length,
        candidates:f.slots.find(s=>s.id===term.slot).cards.length})).filter(term=>term.matches===0||term.matches===term.candidates)};
  });
  const report={id:f.id,fixture:path,sha256:createHash('sha256').update(bytes).digest('hex'),humanOutcome,
    cardsPerSlot:f.slots.map(s=>s.cards.length),tuples:all.length,clues:f.clues.length,
    tagOnlySurvivors:all.filter(t=>tagsFit(t)).length,initialPublicSurvivors:unrefuted().length,
    fullModelSolutions:all.filter(t=>validFormula(f,t)).length,
    clueAudit,
    // This is an author-level audit; it is never information granted during play.
    initialStableAnswerEdges:f.compatibility?(f.knownRelations??[]).filter(r=>r.stable&&matches(f.answer,r)).length:null,
    initialCertifiedFormulas:f.compatibility?certified().length:null,
    probes:[]};
  for(const key of recordedProbes){
    const ids=key.split(':');
    const slots=ids.map(id=>f.slots.find(s=>s.cards.some(c=>c.id===id)).id);
    const tuple=Object.fromEntries(slots.map((s,i)=>[s,ids[i]]));
    const before=unrefuted(), supportedBefore=before.filter(t=>matches(t,{slots,tuple})).length;
    state.selected=tuple; const length=state.history.length;act(f,state,{type:'pairTest',slots});
    assert.equal(state.history.length,length+1,'Recorded human probe must be newly charged');
    report.probes.push({step:report.probes.length+1,stable:state.history.at(-1).stable,
      supportedHypothesesBefore:supportedBefore,unrefutedBefore:before.length,unrefutedAfter:unrefuted().length,
      certifiedAfter:certified().length});
  }
  report.recordedPairTests=recordedProbes.length;
  report.probesWithoutTargetHypothesis=report.probes.filter(p=>p.supportedHypothesesBefore===0).length;
  report.afterRecordedPairProbesSurvivors=unrefuted().length;
  report.finalCertifiedFormulas=f.compatibility?certified().length:null;
  report.researchRemainingAfterRecordedProbes=state.research??null;
  if(recordedProbes.length){
    assert.equal(report.finalCertifiedFormulas,1,'Successful trace must certify a tag-valid stable chain');
    state.selected={...f.answer};act(f,state,{type:'submit'});assert.equal(state.status,'solved');
  }
  return report;
});
const output={method:'Static enumeration of frozen synthetic fixtures; recorded paid pair traces from case checkpoints. Counts stop before full synthesis and do not incorporate failed-synthesis exclusions. Public survivors use tags and observed negatives only. Positive edges may certify a solution without eliminating other hypotheses. Author-level clue omission uses full hidden compatibility, not player knowledge. No player-facing solver is added.',cases:reports};
if(process.argv.includes('--write'))writeFileSync(new URL('./calibration-audit.json',import.meta.url),JSON.stringify(output,null,2)+'\n');
console.table(reports.map(r=>({case:r.id,tuples:r.tuples,clues:r.clues,tagRows:r.tagOnlySurvivors,publicRows:r.initialPublicSurvivors,
  necessary:r.clueAudit.every(c=>c.fullModelSurvivorsWhenOmitted>1),answerPriors:r.initialStableAnswerEdges,
  tests:r.recordedPairTests,unsupported:r.probesWithoutTargetHypothesis,remaining:r.afterRecordedPairProbesSurvivors,certified:r.finalCertifiedFormulas})));
