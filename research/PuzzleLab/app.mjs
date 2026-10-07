// SPDX-License-Identifier: MPL-2.0
const $ = id => document.getElementById(id);
let view;
let queue = Promise.resolve();
const name = id => view.slots.flatMap(s => s.cards).find(c => c.id === id)?.name ?? '—';
const formula = tuple => view.slots.map(s => name(tuple[s.id])).join(' + ');
function render() {
  const focused = document.activeElement?.id;
  const s = view.state;
  $('title').textContent = view.title; $('description').textContent = view.description;
  $('cards').replaceChildren();
  for (const slot of view.slots) {
    const group = document.createElement('fieldset');
    const legend = document.createElement('legend'); legend.textContent = slot.name; group.append(legend);
    for (const card of slot.cards) {
      const box = document.createElement('div'); box.className = `card ${s.marks[card.id] ? 'excluded' : ''}`;
      const label = document.createElement('label');
      const radio = document.createElement('input'); radio.type = 'radio'; radio.name = slot.id; radio.checked = s.selected[slot.id] === card.id;
      radio.id = `select-${card.id}`;
      radio.onchange = () => action({type:'select', slot:slot.id, card:card.id});
      const text = document.createElement('strong'); text.textContent = card.name;
      label.append(radio, text); box.append(label);
      const tags = document.createElement('p'); tags.className = 'tags'; tags.textContent = card.tags.join(' · '); box.append(tags);
      const mark = document.createElement('button'); mark.className = 'mark'; mark.textContent = s.marks[card.id] ? 'Вернуть в рассмотрение' : 'Пометить исключённым';
      mark.id = `mark-${card.id}`;
      mark.setAttribute('aria-label', `${mark.textContent}: ${card.name}`); mark.setAttribute('aria-pressed', String(Boolean(s.marks[card.id])));
      mark.onclick = () => action({type:'mark', slot:slot.id, card:card.id}); box.append(mark); group.append(box);
    }
    $('cards').append(group);
  }
  $('clues').replaceChildren(...view.clues.map(text => {const li = document.createElement('li'); li.textContent = text; return li;}));
  $('selection').textContent = formula(s.selected);
  $('budget').textContent = `Science: ${s.science} · Стоимость проверки: ${view.submissionCost}`;
  $('submit').disabled = s.status !== 'playing' || !view.slots.every(slot => s.selected[slot.id]);
  $('result').textContent = s.status === 'solved' ? 'Формула найдена! Ваше исследование завершено.' : s.status === 'exhausted' ? 'Формула не подошла. Бюджет проверок исчерпан; ответ не раскрыт. Сохраните рассуждения для разбора.' : '';
  $('history').replaceChildren(...s.history.map(h => {const li = document.createElement('li'); li.textContent = `${formula(h.tuple)} — ${h.success ? 'успех' : 'неудача'} (Science −${h.cost})`; return li;}));
  if (!s.history.length) {const li = document.createElement('li'); li.textContent = 'Проверок пока не было.'; $('history').append(li);}
  if (focused && $(focused) !== document.activeElement) $(focused)?.focus({preventScroll:true});
}
async function request(path, body) {
  const r = await fetch(path, body ? {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)} : {});
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
let revision;
const events = new EventSource('/events');
events.onmessage = e => {if (revision && revision !== e.data) {queue.then(() => location.reload());} revision = e.data;};
