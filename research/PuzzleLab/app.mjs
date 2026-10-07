// SPDX-License-Identifier: MPL-2.0
const $ = id => document.getElementById(id);
let view;
let queue = Promise.resolve();
const name = id => view.slots.flatMap(s => s.cards).find(c => c.id === id)?.name ?? '—';
const formula = tuple => view.slots.map(s => name(tuple[s.id])).join(' + ');
const pairDescription = r => `${r.slots.map(id => name(r.tuple[id])).join(' + ')} — ${r.stable ? 'СТАБИЛЬНО' : 'НЕСОВМЕСТИМО'}`;
const pairMatches = (r, slots, tuple) => r.slots.length === slots.length &&
  r.slots.every((id,index) => id === slots[index]) && slots.every(id => tuple[id] && r.tuple[id] === tuple[id]);
function relationJournal(s) {
  const tested = s.history.filter(h => h.type === 'pairTest');
  const groups = document.createDocumentFragment();
  for (const fresh of [false,true]) {
    const observations = s.knownRelations.filter(r => tested.some(h => pairMatches(h,r.slots,r.tuple)) === fresh);
    if (!observations.length) continue;
    const section = document.createElement('section'); section.className = `observation-source ${fresh ? 'new' : 'prior'}`;
    const heading = document.createElement('h3'); heading.textContent = fresh ? 'Мои исследования' : 'Было известно'; section.append(heading);
    const columns = document.createElement('div'); columns.className = 'relation-columns';
    for (let i=0; i<view.slots.length-1; i++) {
      const slots = [view.slots[i].id,view.slots[i+1].id];
      const column = document.createElement('section');
      const title = document.createElement('h4'); title.textContent = `${view.slots[i].name} ↔ ${view.slots[i+1].name}`; column.append(title);
      const list = document.createElement('ul');
      for (const r of observations.filter(r => r.slots.every((id,index) => id === slots[index]))) {
        const li = document.createElement('li');
        li.className = `relation ${r.stable ? 'stable' : 'incompatible'} ${pairMatches(r,slots,s.selected) ? 'current' : ''}`;
        const names = document.createElement('span'); names.className = 'relation-names';
        names.textContent = r.slots.map(id => name(r.tuple[id])).join(' + ');
        const verdict = document.createElement('span'); verdict.className = 'verdict'; verdict.textContent = r.stable ? '✓ Стабильно' : '⊘ Несовместимо';
        li.append(names,verdict); list.append(li);
      }
      if (!list.childElementCount) {const li = document.createElement('li'); li.className='empty'; li.textContent='Нет наблюдений'; list.append(li);}
      column.append(list); columns.append(column);
    }
    section.append(columns); groups.append(section);
  }
  return groups;
}
// Presentation palette only: colors carry no additional logical meaning.
const tagStyles = {
  'Растительное':'plant', 'Минеральное':'mineral', 'Тёмное':'dark',
  'Трупное':'corpse', 'Насекомое':'insect', 'Животное':'animal',
  'Рыбное':'fish', 'Слизь':'slime', 'Водное':'water', 'Орган':'organ',
  Plant:'plant', Mineral:'mineral', Dark:'dark', Corpse:'corpse',
  Insect:'insect', Animal:'animal', Fish:'fish', Slime:'slime', Water:'water', Organ:'organ'
};
function tagBadge(tag) {
  const badge = document.createElement('span');
  badge.className = `tag tag-${tagStyles[tag] ?? 'neutral'}`;
  badge.textContent = tag;
  return badge;
}
function clueContents(text) {
  const parts = document.createDocumentFragment();
  for (const part of text.split(/(«[^»]+»)/g)) {
    if (part.startsWith('«') && part.endsWith('»')) parts.append(tagBadge(part.slice(1,-1)));
    else parts.append(document.createTextNode(part));
  }
  return parts;
}
function render() {
  const focused = document.activeElement?.id;
  const s = view.state;
  $('title').textContent = view.title; $('description').textContent = view.description;
  $('task').textContent = view.slots.length === 3 ? 'Соберите смесь: один порошок, одна жидкость и одна эссенция.' : 'Соберите смесь: один порошок и одна жидкость.';
  $('quick-rules').textContent = view.pairTestCost ? 'Все сведения действуют одновременно. Обе соседние пары должны быть стабильны. Теги не определяют совместимость.' : 'Все сведения действуют одновременно. Выбор и пометки бесплатны. Проверка сообщает только успех или неудачу.';
  document.body.classList.toggle('three-slot', view.slots.length === 3);
  $('cards').replaceChildren();
  for (const slot of view.slots) {
    const group = document.createElement('fieldset');
    const legend = document.createElement('legend'); legend.textContent = slot.name; group.append(legend);
    for (const card of slot.cards) {
      const selected = s.selected[slot.id] === card.id;
      const box = document.createElement('div'); box.className = `card ${s.marks[card.id] ? 'excluded' : ''} ${selected ? 'selected' : ''}`;
      const choose = document.createElement('button'); choose.className = 'choose'; choose.id = `select-${card.id}`;
      choose.setAttribute('aria-pressed',String(selected)); choose.setAttribute('aria-label',card.name);
      choose.title = selected ? 'Снять выбор' : 'Выбрать';
      choose.onclick = () => action({type:'toggleSelect',slot:slot.id,card:card.id});
      const dot = document.createElement('span'); dot.className='selection-dot'; dot.setAttribute('aria-hidden','true');
      const text = document.createElement('strong'); text.textContent = card.name;
      choose.append(dot,text);
      const tags = document.createElement('span'); tags.className = 'tags'; tags.append(...card.tags.map(tagBadge)); choose.append(tags); box.append(choose);
      const mark = document.createElement('button'); mark.className = 'mark';
      const markAction = s.marks[card.id] ? 'Вернуть в рассмотрение' : 'Пометить исключённым';
      mark.textContent = s.marks[card.id] ? '↶' : '⊘';
      mark.title = markAction;
      mark.id = `mark-${card.id}`;
      mark.setAttribute('aria-label', `${markAction}: ${card.name}`); mark.setAttribute('aria-pressed', String(Boolean(s.marks[card.id])));
      mark.onclick = () => action({type:'mark', slot:slot.id, card:card.id}); box.append(mark); group.append(box);
    }
    $('cards').append(group);
  }
  $('clues').replaceChildren(...view.clues.map(text => {const li = document.createElement('li'); li.append(clueContents(text)); return li;}));
  $('selection').textContent = formula(s.selected);
  $('pair-research').hidden = !view.pairTestCost;
  $('knowledge').hidden = !view.pairTestCost;
  $('pair-help').hidden = !view.pairTestCost;
  if (view.pairTestCost) {
    $('research-budget').textContent = `Заряды: ${s.research}`;
    $('pair-actions').replaceChildren(...view.slots.slice(0,-1).map((slot,i) => {
      const slots = [slot.id,view.slots[i+1].id];
      const complete = slots.every(id => s.selected[id]);
      const known = s.knownRelations.find(r => pairMatches(r,slots,s.selected));
      const panel = document.createElement('section'); panel.className=`pair-control ${known ? known.stable ? 'stable' : 'incompatible' : complete ? 'unknown' : 'incomplete'}`;
      const heading = document.createElement('h3'); heading.textContent = `${slot.name} ↔ ${view.slots[i+1].name}`;
      const status = document.createElement('span'); status.className='verdict';
      status.textContent = known ? known.stable ? '✓ Стабильно' : '⊘ Несовместимо' : complete ? '? Не исследовано' : '— Выберите пару';
      const names = document.createElement('p'); names.className='pair-names'; names.textContent=slots.map(id=>name(s.selected[id])).join(' + ');
      const button = document.createElement('button'); button.id = `test-${slot.id}`;
      button.textContent = known ? 'Уже известно' : `Исследовать · −${view.pairTestCost} заряд`;
      button.setAttribute('aria-label', `Исследовать: ${slot.name.toLowerCase()} + ${view.slots[i+1].name.toLowerCase()}`);
      button.disabled = s.status !== 'playing' || Boolean(known) || s.research < view.pairTestCost || !complete;
      button.onclick = () => action({type:'pairTest',slots}); panel.append(heading,status,names,button); return panel;
    }));
    $('relations').replaceChildren(relationJournal(s));
  }
  $('budget').textContent = `Science: ${s.science} · Стоимость проверки: ${view.submissionCost}`;
  $('submit').disabled = s.status !== 'playing' || !view.slots.every(slot => s.selected[slot.id]);
  $('result').textContent = s.status === 'solved' ? 'Формула найдена! Ваше исследование завершено.' : s.status === 'exhausted' ? 'Формула не подошла. Бюджет проверок исчерпан; ответ не раскрыт. Сохраните рассуждения для разбора.' : '';
  $('history').replaceChildren(...s.history.map(h => {const li = document.createElement('li'); li.textContent = h.type === 'pairTest'
    ? `${pairDescription(h)} (заряд исследования −${h.cost})`
    : `${formula(h.tuple)} — ${h.success ? 'успех' : 'неудача'} (Science −${h.cost})`; return li;}));
  if (!s.history.length) {const li = document.createElement('li'); li.textContent = 'Проверок пока не было.'; $('history').append(li);}
  if (focused && $(focused) !== document.activeElement) $(focused)?.focus({preventScroll:true});
}
async function request(path, body) {
  const r = await fetch(path, {signal:AbortSignal.timeout(5000), ...(body ? {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)} : {})});
  const data = await r.json(); if (!r.ok) throw new Error(data.error); return data;
}
function action(body) {
  queue = queue.then(async () => {
    try {view = await request('/api/action', body); render(); $('error').textContent = ''; if (body.type === 'notes') $('saved').textContent = 'Сохранено в текущей сессии';}
    catch(e) {$('error').textContent = e.message;}
  });
  return queue;
}
$('submit').onclick = () => action({type:'submit'});
$('notes').oninput = () => {$('saved').textContent = 'Сохранение…'; action({type:'notes', text:$('notes').value});};
$('export').onclick = async () => {
  await queue;
  const blob = new Blob([JSON.stringify({...view, state:{...view.state, notes:$('notes').value}}, null, 2)], {type:'application/json'});
  const url = URL.createObjectURL(blob); const link = document.createElement('a'); link.href = url; link.download = `${view.id}-journal.json`; link.click(); URL.revokeObjectURL(url);
};
try {view = await request('/api/state'); $('notes').value = view.state.notes; render();}
catch(e) {$('error').textContent = `Не удалось загрузить опыт: ${e.message}`;}
// Finite requests keep the embedded browser's navigation from waiting on a
// permanent stream. Read only public presentation files; never reset sessions.
const presentationFiles = ['/', '/app.mjs', '/style.css'];
let revision;
async function checkPresentation() {
  try {
    const files = await Promise.all(presentationFiles.map(async path => {
      const r = await fetch(path, {cache:'no-store', signal:AbortSignal.timeout(3000)});
      if (!r.ok) throw new Error('Presentation unavailable');
      return r.text();
    }));
    const current = await request('/api/state');
    const {state: playerState, ...publicFixture} = current;
    const next = JSON.stringify([files, publicFixture]);
    if (revision && revision !== next) {await queue; location.reload(); return;}
    revision = next;
  } catch {
    // Temporary loss of the dev server must not erase the player's board.
  }
  setTimeout(checkPresentation, 2000);
}
checkPresentation();
