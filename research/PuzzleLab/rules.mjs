// SPDX-License-Identifier: MPL-2.0
import {validateWording} from './wording.mjs';
export function candidates(f) {
  return f.slots.reduce((rows, slot) => rows.flatMap(row => slot.cards.map(card => ({...row, [slot.id]: card.id}))), [{}]);
}
function adjacent(f, slots) {
  return Array.isArray(slots) && slots.length === 2 && f.slots.some((s,i) =>
    s.id === slots[0] && f.slots[i+1]?.id === slots[1]);
}
function pairKey(f, tuple, slots) {return slots.map(id => tuple[id]).join(':');}
function stablePair(f, tuple, slots) {return f.compatibility.stablePairs.includes(pairKey(f,tuple,slots));}
export function validFormula(f, tuple) {
  return f.clues.every(c => satisfies(f,tuple,c)) && (!f.compatibility ||
    f.slots.slice(0,-1).every((s,i) => stablePair(f,tuple,[s.id,f.slots[i+1].id])));
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
  const index=f.clues?.indexOf(clue);
  return f.wording && index>=0 ? f.wording.entries[index].text : legacyClueText(f,clue);
}
export function legacyClueText(f, clue) {
  const term = t => `${f.slots.find(s => s.id === t.slot).name.toLowerCase()} имеет свойство «${t.tag}»`;
  if (clue.kind === 'exactly' && clue.terms.length === 1) {
    const t=clue.terms[0], slot=f.slots.find(s=>s.id===t.slot).name;
    return clue.count === 0 ? `${slot} не имеет свойства «${t.tag}».`
      : `${slot} имеет свойство «${t.tag}».`;
  }
  if (clue.kind === 'exactly' && clue.count === 0)
    return `Ни одно из следующих утверждений не выполняется: ${clue.terms.map(term).join('; ')}.`;
  if (clue.kind === 'sharedTag') return f.slots.length === 2
    ? 'У выбранных порошка и жидкости есть хотя бы одно общее свойство.'
    : 'У всех трёх выбранных компонентов есть хотя бы одно общее свойство.';
  if (clue.kind === 'notTogether') {
    const slot = t => f.slots.find(s => s.id === t.slot).name.toLowerCase();
    return `В этой формуле ${slot(clue.left)} со свойством «${clue.left.tag}» и ${slot(clue.right)} со свойством «${clue.right.tag}» не могут быть вместе.`;
  }
  if (clue.kind === 'exactly' && [1,2].includes(clue.count) && clue.terms.length === f.slots.length &&
      new Set(clue.terms.map(t => t.slot)).size === f.slots.length &&
      f.slots.every(s => clue.terms.some(t => t.slot === s.id)) &&
      new Set(clue.terms.map(t => t.tag)).size === 1) {
    return clue.count === 1
      ? `Среди компонентов формулы ровно один имеет свойство «${clue.terms[0].tag}».`
      : `Среди компонентов формулы ровно два имеют свойство «${clue.terms[0].tag}».`;
  }
  if (clue.kind === 'exactly') return `Ровно ${clue.count} из следующих утверждений верно: ${clue.terms.map(term).join('; ')}.`;
  if (clue.kind === 'implies') return `Если ${term(clue.if)}, то ${term(clue.then)}.`;
  throw new Error('Unsupported clue kind');
}
export function validate(f) {
  if (f.propertyVocabulary && (!Array.isArray(f.propertyVocabulary) ||
      f.propertyVocabulary.some(t => typeof t !== 'string' || !t.trim()) ||
      new Set(f.propertyVocabulary).size !== f.propertyVocabulary.length)) throw new Error('Invalid property vocabulary');
  const shared = f.economy?.mode === 'sharedScience';
  if (f.economy && (!shared || !Number.isInteger(f.economy.refillAmount) || f.economy.refillAmount < 1)) throw new Error('Invalid economy');
  if (![2,3].includes(f.slots.length) || new Set(f.slots.map(s => s.id)).size !== f.slots.length) throw new Error('V0 requires two or three distinct slots');
  const ids = f.slots.flatMap(s => s.cards.map(c => c.id));
  if (ids.length !== new Set(ids).size || f.slots.some(s => !s.cards.length)) throw new Error('Invalid cards');
  if (!Number.isInteger(f.science) || f.science < 1 || !Number.isInteger(f.submissionCost) || f.submissionCost < 1) throw new Error('Invalid budget');
  for (const c of f.clues) {
    if (c.kind === 'sharedTag') continue;
    const terms = c.kind === 'exactly' ? c.terms : c.kind === 'implies' ? [c.if, c.then] : c.kind === 'notTogether' ? [c.left,c.right] : [];
    if (!terms.length || terms.some(t => !f.slots.some(s => s.id === t.slot) ||
        !(f.propertyVocabulary?.includes(t.tag) ||
          f.slots.some(s => s.cards.some(card => card.tags.includes(t.tag)))))) throw new Error('Invalid clue terms');
    if (c.kind === 'exactly' && (!Number.isInteger(c.count) || c.count < 0 || c.count > terms.length)) throw new Error('Invalid count');
  }
  validateWording(f,legacyClueText);
  if (f.compatibility) {
    if (f.slots.length !== 3 || (!shared && (!Number.isInteger(f.researchCharges) || f.researchCharges < 1)) ||
        !Number.isInteger(f.pairTestCost) || f.pairTestCost < 1) throw new Error('Invalid pair research budget');
    const legal = new Set(f.slots.slice(0,-1).flatMap((s,i) => s.cards.flatMap(a =>
      f.slots[i+1].cards.map(b => `${a.id}:${b.id}`))));
    if (!Array.isArray(f.compatibility.stablePairs) || new Set(f.compatibility.stablePairs).size !== f.compatibility.stablePairs.length ||
        f.compatibility.stablePairs.some(k => !legal.has(k))) throw new Error('Invalid compatibility pairs');
    const known = new Set();
    for (const r of f.knownRelations ?? []) {
      const key = pairKey(f,r.tuple,r.slots);
      if (!adjacent(f,r.slots) || !legal.has(key) || known.has(key) ||
          typeof r.stable !== 'boolean' || stablePair(f,r.tuple,r.slots) !== r.stable) throw new Error('Invalid prior relation');
      known.add(key);
    }
  }
  const live = candidates(f).filter(t => validFormula(f,t));
  if (live.length !== 1 || !f.slots.every(s => live[0][s.id] === f.answer[s.id])) throw new Error('Fixture must have one answer matching all clues');
}
export function createState(f) {
  return {science: f.science, selected: {}, marks: {}, notes: '', history: [], status: 'playing',
    ...(f.compatibility ? {...(f.economy?.mode === 'sharedScience' ? {} : {research:f.researchCharges}), knownRelations:structuredClone(f.knownRelations ?? [])} : {})};
}
export function publicView(f, state) {
  return {id: f.id, title: f.title, description: f.description, slots: f.slots,
    clues: f.clues.map(c => clueText(f, c)), submissionCost: f.submissionCost, state,
    ...(f.wording ? {clueAsides:f.wording.entries.map(e=>e.asideText??null)} : {}),
    ...(f.economy ? {economy:f.economy} : {}),
    ...(f.compatibility ? {pairTestCost:f.pairTestCost} : {})};
}
export function act(f, state, action) {
  const shared = f.economy?.mode === 'sharedScience';
  if (action.type === 'refill') {
    if (!shared || state.status !== 'playing') throw new Error('Пополнение недоступно');
    state.science += f.economy.refillAmount;
    state.history.push({type:'refill',amount:f.economy.refillAmount});
  } else if (action.type === 'notes') {
    if (typeof action.text !== 'string' || action.text.length > 4000) throw new Error('Недопустимая заметка');
    state.notes = action.text;
  } else if (action.type === 'selectPair') {
    if (!f.compatibility || !adjacent(f,action.slots)) throw new Error('Выберите наблюдение о соседней паре');
    const observed = state.knownRelations.find(r => r.slots.every((id,i) => id === action.slots[i]) &&
      r.slots.every(id => r.tuple[id] === action.tuple?.[id]));
    if (!observed) throw new Error('Такой пары нет в журнале');
    state.selected = {...observed.tuple};
  } else if (action.type === 'select' || action.type === 'toggleSelect' || action.type === 'mark') {
    const slot = f.slots.find(s => s.id === action.slot);
    if (!slot?.cards.some(c => c.id === action.card)) throw new Error('Неизвестная карточка');
    if (action.type === 'select') state.selected[slot.id] = action.card;
    else if (action.type === 'toggleSelect') {
      if (state.selected[slot.id] === action.card) delete state.selected[slot.id];
      else state.selected[slot.id] = action.card;
    }
    else state.marks[action.card] = !state.marks[action.card];
  } else if (action.type === 'pairTest') {
    if (!f.compatibility || !adjacent(f,action.slots)) throw new Error('Исследуйте только соседние пары');
    if (state.status !== 'playing') throw new Error('Опыт завершён');
    if (!action.slots.every(id => f.slots.find(s => s.id === id).cards.some(c => c.id === state.selected[id]))) throw new Error('Выберите обе карточки пары');
    const tuple = Object.fromEntries(action.slots.map(id => [id,state.selected[id]]));
    if (state.knownRelations.some(r => pairKey(f,r.tuple,r.slots) === pairKey(f,tuple,action.slots))) return;
    if ((shared ? state.science : state.research) < f.pairTestCost) throw new Error(shared ? 'Недостаточно Science: пополните запас' : 'Заряды исследования закончились');
    const result = {slots:[...action.slots], tuple, stable:stablePair(f,tuple,action.slots)};
    if (shared) state.science -= f.pairTestCost;
    else state.research -= f.pairTestCost;
    state.knownRelations.push(result);
    state.history.push({type:'pairTest',...result,cost:f.pairTestCost});
  } else if (action.type === 'submit') {
    if (state.status !== 'playing' || state.science < f.submissionCost) throw new Error('Проверки закончены');
    if (!f.slots.every(s => s.cards.some(c => c.id === state.selected[s.id]))) throw new Error('Выберите карточку в каждом слоте');
    state.science -= f.submissionCost;
    const success = f.slots.every(s => state.selected[s.id] === f.answer[s.id]);
    state.history.push({tuple: {...state.selected}, success, cost: f.submissionCost});
    state.status = success ? 'solved' : !shared && state.science < f.submissionCost ? 'exhausted' : 'playing';
  } else throw new Error('Неизвестное действие');
}
