// SPDX-License-Identifier: MPL-2.0
export function candidates(f) {
  return f.slots.reduce((rows, slot) => rows.flatMap(row => slot.cards.map(card => ({...row, [slot.id]: card.id}))), [{}]);
}
function has(f, tuple, term) {
  return f.slots.find(s => s.id === term.slot)?.cards.find(c => c.id === tuple[term.slot])?.tags.includes(term.tag) ?? false;
}
export function satisfies(f, tuple, clue) {
  if (clue.kind === 'sharedTag') {
    const cards = f.slots.map(s => s.cards.find(c => c.id === tuple[s.id]));
    return cards[0].tags.some(tag => cards.every(c => c.tags.includes(tag)));
  }
  if (clue.kind === 'notTogether') return !(has(f, tuple, clue.left) && has(f, tuple, clue.right));
  if (clue.kind === 'exactly') return clue.terms.filter(t => has(f, tuple, t)).length === clue.count;
  if (clue.kind === 'implies') return !has(f, tuple, clue.if) || has(f, tuple, clue.then);
  throw new Error('Unsupported clue kind');
}
export function clueText(f, clue) {
  const term = t => `${f.slots.find(s => s.id === t.slot).name.toLowerCase()} имеет свойство «${t.tag}»`;
  if (clue.kind === 'sharedTag') return 'У выбранных порошка и жидкости есть хотя бы одно общее свойство.';
  if (clue.kind === 'notTogether') {
    const slot = t => f.slots.find(s => s.id === t.slot).name.toLowerCase();
    return `В этой формуле ${slot(clue.left)} со свойством «${clue.left.tag}» и ${slot(clue.right)} со свойством «${clue.right.tag}» не могут быть вместе.`;
  }
  if (clue.kind === 'exactly' && clue.count === 1 && clue.terms.length === f.slots.length &&
      new Set(clue.terms.map(t => t.slot)).size === f.slots.length &&
      f.slots.every(s => clue.terms.some(t => t.slot === s.id)) &&
      new Set(clue.terms.map(t => t.tag)).size === 1) {
    return `Среди компонентов формулы ровно один имеет свойство «${clue.terms[0].tag}».`;
  }
  if (clue.kind === 'exactly') return `Ровно ${clue.count} из следующих утверждений верно: ${clue.terms.map(term).join('; ')}.`;
  if (clue.kind === 'implies') return `Если ${term(clue.if)}, то ${term(clue.then)}.`;
  throw new Error('Unsupported clue kind');
}
export function validate(f) {
  if (f.slots.length !== 2 || new Set(f.slots.map(s => s.id)).size !== 2) throw new Error('V0 requires two distinct slots');
  const ids = f.slots.flatMap(s => s.cards.map(c => c.id));
  if (ids.length !== new Set(ids).size || f.slots.some(s => !s.cards.length)) throw new Error('Invalid cards');
  if (!Number.isInteger(f.science) || f.science < 1 || !Number.isInteger(f.submissionCost) || f.submissionCost < 1) throw new Error('Invalid budget');
  for (const c of f.clues) {
    if (c.kind === 'sharedTag') continue;
    const terms = c.kind === 'exactly' ? c.terms : c.kind === 'implies' ? [c.if, c.then] : c.kind === 'notTogether' ? [c.left,c.right] : [];
    if (!terms.length || terms.some(t => !f.slots.find(s => s.id === t.slot)?.cards.some(card => card.tags.includes(t.tag)))) throw new Error('Invalid clue terms');
    if (c.kind === 'exactly' && (!Number.isInteger(c.count) || c.count < 0 || c.count > terms.length)) throw new Error('Invalid count');
  }
  const live = candidates(f).filter(t => f.clues.every(c => satisfies(f, t, c)));
  if (live.length !== 1 || !f.slots.every(s => live[0][s.id] === f.answer[s.id])) throw new Error('Fixture must have one answer matching all clues');
}
export function createState(f) {
  return {science: f.science, selected: {}, marks: {}, notes: '', history: [], status: 'playing'};
}
export function publicView(f, state) {
  return {id: f.id, title: f.title, description: f.description, slots: f.slots,
    clues: f.clues.map(c => clueText(f, c)), submissionCost: f.submissionCost, state};
}
export function act(f, state, action) {
  if (action.type === 'notes') {
    if (typeof action.text !== 'string' || action.text.length > 4000) throw new Error('Недопустимая заметка');
    state.notes = action.text;
  } else if (action.type === 'select' || action.type === 'mark') {
    const slot = f.slots.find(s => s.id === action.slot);
    if (!slot?.cards.some(c => c.id === action.card)) throw new Error('Неизвестная карточка');
    if (action.type === 'select') state.selected[slot.id] = action.card;
    else state.marks[action.card] = !state.marks[action.card];
  } else if (action.type === 'submit') {
    if (state.status !== 'playing' || state.science < f.submissionCost) throw new Error('Проверки закончены');
    if (!f.slots.every(s => s.cards.some(c => c.id === state.selected[s.id]))) throw new Error('Выберите карточку в каждом слоте');
    state.science -= f.submissionCost;
    const success = f.slots.every(s => state.selected[s.id] === f.answer[s.id]);
    state.history.push({tuple: {...state.selected}, success, cost: f.submissionCost});
    state.status = success ? 'solved' : state.science < f.submissionCost ? 'exhausted' : 'playing';
  } else throw new Error('Неизвестное действие');
}
