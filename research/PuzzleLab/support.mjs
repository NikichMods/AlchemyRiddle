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
