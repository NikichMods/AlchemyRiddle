// SPDX-License-Identifier: MPL-2.0
// Client support uses only paid observations and public budget/selection state.
export function submitBlockReason(view) {
  if(view.state.status!=='playing') return 'Исследование завершено.';
  if(!view.slots.every(s=>view.state.selected[s.id])) return 'Выберите по одному компоненту в каждом столбце.';
  if(view.state.science<view.submissionCost) return `Не хватает Science: нужно ${view.submissionCost}, в запасе ${view.state.science}.${view.economy?.refillAmount>0?' Пополните запас.':''}`;
  return '';
}
export function submissions(view) {return view.state.history.filter(h=>typeof h.success==='boolean');}
export function selectedSubmission(view) {
  return submissions(view).findLast(h=>view.slots.every(s=>h.tuple[s.id]===view.state.selected[s.id]));
}
export function compositionReminder(record) {
  return record?.success===false && record.compositionMismatch===true
    ? 'Сверьте выбранные компоненты со сведениями о составе.' : '';
}
// Presentation only: distinguish a just-observed outcome from a later revisit.
export function submissionFeedback(view, departedAt=0) {
  const history=submissions(view),record=selectedSubmission(view);
  const fresh=Boolean(record && record===history.at(-1) && departedAt<history.length);
  return {fresh,revisited:Boolean(record && !fresh)};
}

// Presentation receives only the player's public observations, never the hidden graph.
export function selectedPairStates(view, slotId) {
  const selected=view.state.selected, index=view.slots.findIndex(s=>s.id===slotId);
  const edge=i=>{
    const slots=view.slots.slice(i,i+2).map(s=>s.id);
    const label=slots.map(s=>({powder:'П',fluid:'Ж',essence:'Э'}[s]??s)).join('–');
    if(!slots.every(s=>selected[s]))return {status:'incomplete',label};
    const known=(view.state.knownRelations??[]).find(r=>r.slots.length===2 && slots.every(s=>r.slots.includes(s)&&r.tuple[s]===selected[s]));
    return {status:known?(known.stable?'stable':'incompatible'):'unknown',label};
  };
  if(!view.pairTestCost)return [{status:'incomplete',label:''},{status:'incomplete',label:''}];
  if(index===0){const e=edge(0);return [e,e];}
  if(index===view.slots.length-1){const e=edge(index-1);return [e,e];}
  return [edge(index-1),edge(index)];
}
