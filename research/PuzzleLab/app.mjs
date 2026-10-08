// SPDX-License-Identifier: MPL-2.0
let submitBlockReason,recordedSubmissions,selectedSubmission,compositionReminder;
const $ = id => document.getElementById(id);
let view;
let queue = Promise.resolve();
// Explicit presentation trial; old URLs retain the historical clue rendering.
const showClueRoles = new URLSearchParams(location.search).get('roles') === '1';
const slotShapes = {
  powder:'M1 31 Q6 28 10 20 Q14 10 20 10 Q26 10 30 20 Q34 28 39 31 Z M4 17 h1 M35 18 h1 M29 6 h1',
  fluid:'M14 2 H26 V9 L36 25 Q39 32 31 32 H9 Q1 32 4 25 L14 9 Z',
  essence:'M10 3 H30 L39 17 L30 31 H10 L1 17 Z'
};
const name = id => view.slots.flatMap(s => s.cards).find(c => c.id === id)?.name ?? '—';
function cardRef(id) {
  const slot = view.slots.find(s => s.cards.some(c => c.id === id));
  const badge = document.createElement('span');
  badge.className = `card-ref ref-${slot?.id ?? 'empty'}`;
  const label = document.createElement('span');
  label.textContent = slot ? `${{powder:'П',fluid:'Ж',essence:'Э'}[slot.id]}${slot.cards.findIndex(c => c.id === id)+1}` : '—';
  if (slot) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('viewBox','0 0 40 34'); svg.setAttribute('aria-hidden','true');
    const path = document.createElementNS(svg.namespaceURI,'path');
    path.setAttribute('d', slotShapes[slot.id]);
    svg.append(path); badge.append(svg);
  }
  badge.append(label);
  badge.title = name(id);
  return badge;
}
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
        const refs = document.createElement('span'); refs.className = 'relation-refs';
        const connector = document.createElement('span'); connector.textContent = '↔';
        refs.append(cardRef(r.tuple[r.slots[0]]),connector,cardRef(r.tuple[r.slots[1]]),verdict);
        const choice = document.createElement('button'); choice.className = 'relation-choice';
        choice.id = `pair-${r.slots.map(id=>r.tuple[id]).join('-')}`;
        choice.setAttribute('aria-label',`Выбрать только пару: ${r.slots.map(id=>name(r.tuple[id])).join(' + ')}`);
        choice.title = `${names.textContent} — ${r.stable ? 'стабильно' : 'несовместимо'}. Выбрать только эту пару`;
        choice.onclick = () => action({type:'selectPair',slots:r.slots,tuple:r.tuple});
        const highlight = active => r.slots.forEach(id => $(`select-${r.tuple[id]}`)?.closest('.card').classList.toggle('journal-linked',active));
        choice.onmouseenter = () => highlight(true); choice.onmouseleave = () => highlight(false);
        choice.onfocus = () => highlight(true); choice.onblur = () => highlight(false);
        choice.append(refs); li.append(choice); list.append(li);
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
const roleForms = {
  powder:['порошок','порошка','порошку','порошком','порошке'],
  fluid:['жидкость','жидкости','жидкостью'],
  essence:['эссенция','эссенции','эссенцию','эссенцией']
};
const rolePattern = new RegExp(`(?<![\\p{L}\\p{N}_])(${Object.values(roleForms).flat().join('|')})(?![\\p{L}\\p{N}_])`,'giu');
function roleContents(text) {
  const parts = document.createDocumentFragment();
  for (const part of text.split(rolePattern)) {
    const slot = Object.keys(roleForms).find(id=>roleForms[id].includes(part.toLowerCase()));
    if (!slot || !view.slots.some(s=>s.id===slot)) {parts.append(document.createTextNode(part));continue;}
    const label=document.createElement('strong');label.className=`clue-role role-${slot}`;
    const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('viewBox','0 0 40 34');svg.setAttribute('aria-hidden','true');
    svg.setAttribute('focusable','false');
    const path=document.createElementNS(svg.namespaceURI,'path');path.setAttribute('d',slotShapes[slot]);
    svg.append(path);label.append(svg,document.createTextNode(part));parts.append(label);
  }
  return parts;
}
function clueContents(text) {
  const parts = document.createDocumentFragment();
  for (const part of text.split(/(«[^»]+»)/g)) {
    if (part.startsWith('«') && part.endsWith('»')) parts.append(tagBadge(part.slice(1,-1)));
    else parts.append(showClueRoles ? roleContents(part) : document.createTextNode(part));
  }
  return parts;
}
function render() {
  const focused = document.activeElement?.id;
  const s = view.state;
  const shared = view.economy?.mode === 'sharedScience';
  document.body.classList.toggle('role-preview',showClueRoles);
  // Removed by user decision; wait for fresh-player evidence before adding a lesson.
  $('clue-guide').hidden=true;
  $('clue-guide').textContent='';
  $('compatibility-guide').textContent=showClueRoles
    ? 'Нужны две стабильные пары: порошок + жидкость и жидкость + эссенция. Изучать обе перед ответом не обязательно.'
    : 'Для искомой формулы нужны две стабильные пары и выполнение всех сведений о составе. Не каждая смесь из стабильных пар подходит.';
  $('experiment-guide').hidden=!showClueRoles;
  $('experiment-guide').textContent='Начальных сведений может не хватить. Исследуйте пары: стабильность подтверждает связь, несовместимость исключает её из формулы.';
  $('pair-action-guide').textContent=showClueRoles
    ? 'Выберите соседнюю пару, совместимость которой хотите узнать.'
    : 'Для формулы нужны две стабильные пары. Исследование проверяет одну пару, финальная проверка — всю смесь.';
  $('case-badge').textContent = shared ? 'Корпусный опыт' : 'Синтетический опыт';
  $('title').textContent = view.title;
  $('description').textContent = view.slots.length === 3
    ? 'Найдите смесь из порошка, жидкости и эссенции: её состав должен подходить под условия, а обе соседние пары — быть стабильными.'
    : 'Найдите смесь из порошка и жидкости, которая подходит под все сведения о составе.';
  if (shared) $('description').textContent = view.description;
  $('economy-help').textContent = shared
    ? `Пара стоит ${view.pairTestCost} Science, вся смесь — ${view.submissionCost} Science. Запас общий, лимита попыток нет. Кнопка пополнения добавляет ${view.economy.refillAmount} Science. В лаборатории пополнение бесплатно: получение науки в игре здесь не моделируется. Уже изученные пары повторно оплачивать не нужно.`
    : 'Цена каждого опыта указана на кнопке или рядом с ней. Финальный опыт расходует Science и сообщает успех или неудачу. После ошибки можно продолжать, пока остались финальные попытки. Запас опытов в этой загадке не пополняется.';
  $('pair-help').innerHTML = '<strong>Узнайте совместимость.</strong> Для тройки нужны две стабильные пары: порошок с жидкостью и жидкость с эссенцией. Их состояние показано справа. Кнопка «Исследовать» узнаёт результат одной пары за '+(shared ? 'Science.' : 'заряд.')+' Уже известные результаты сохраняются в «Совместимости пар».';
  $('task').textContent = view.slots.length === 3 ? 'Соберите смесь: один порошок, одна жидкость и одна эссенция.' : 'Соберите смесь: один порошок и одна жидкость.';
  document.body.classList.toggle('three-slot', view.slots.length === 3);
  document.body.classList.toggle('many-candidates',view.slots.some(slot=>slot.cards.length>3));
  $('cards').replaceChildren();
  for (const slot of view.slots) {
    const group = document.createElement('fieldset');
    const legend = document.createElement('legend'); legend.textContent = slot.name;
    if(showClueRoles)legend.className=`role-${slot.id}`;
    group.append(legend);
    for (const card of slot.cards) {
      const selected = s.selected[slot.id] === card.id;
      const box = document.createElement('div'); box.className = `card ${selected ? 'selected' : ''}`;
      const choose = document.createElement('button'); choose.className = 'choose'; choose.id = `select-${card.id}`;
      choose.setAttribute('aria-pressed',String(selected)); choose.setAttribute('aria-label',card.name);
      choose.title = selected ? 'Снять выбор' : 'Выбрать';
      choose.onclick = () => action({type:'toggleSelect',slot:slot.id,card:card.id});
      const text = document.createElement('strong'); text.textContent = card.name;
      choose.append(text,cardRef(card.id));
      const tags = document.createElement('span'); tags.className = 'tags'; tags.append(...card.tags.map(tagBadge)); choose.append(tags); box.append(choose);
      group.append(box);
    }
    $('cards').append(group);
  }
  $('clues').replaceChildren(...view.clues.map((text,i) => {
    const li = document.createElement('li'); li.append(clueContents(text));
    if(view.clueAsides?.[i]) {
      const aside=document.createElement('div');aside.className='keeper-aside';
      aside.textContent=view.clueAsides[i];li.append(aside);
    }
    return li;
  }));
  $('selection').replaceChildren(...view.slots.filter(slot=>s.selected[slot.id]).map(slot => {
    const tile = document.createElement('div'); tile.className = `formula-tile ${s.selected[slot.id] ? 'filled' : 'empty'}`;
    const label = document.createElement('span'); label.textContent = s.selected[slot.id] ? name(s.selected[slot.id]) : `Выберите: ${slot.name.toLowerCase()}`;
    tile.append(cardRef(s.selected[slot.id]),label); return tile;
  }));
  if (!$('selection').childElementCount) $('selection').textContent='Пока ничего не выбрано';
  $('pair-research').hidden = !view.pairTestCost || !view.slots.slice(0,-1).some((slot,i)=>s.selected[slot.id] && s.selected[view.slots[i+1].id]);
  $('knowledge').hidden = !view.pairTestCost;
  $('pair-help').hidden = !view.pairTestCost;
  $('pair-tips').hidden = !view.pairTestCost;
  $('formula-compatibility').hidden = !view.pairTestCost;
  if (view.pairTestCost) {
    $('research-budget').textContent = shared ? `Science: ${s.science}` : `Заряды: ${s.research}`;
    $('pair-actions').replaceChildren(...view.slots.slice(0,-1).map((slot,i) => {
      const slots = [slot.id,view.slots[i+1].id];
      const complete = slots.every(id => s.selected[id]);
      const known = s.knownRelations.find(r => pairMatches(r,slots,s.selected));
      const panel = document.createElement('section'); panel.className=`pair-control ${known ? known.stable ? 'stable' : 'incompatible' : complete ? 'unknown' : 'incomplete'}`;
      const heading = document.createElement('h3'); heading.textContent = `${slot.name} ↔ ${view.slots[i+1].name}`;
      const status = document.createElement('span'); status.className='verdict';
      status.textContent = known ? known.stable ? '✓ Стабильно' : '⊘ Несовместимо' : complete ? '? Не исследовано' : '— Выберите пару';
      const names = document.createElement('p'); names.className='pair-names';
      const arrow = document.createElement('span'); arrow.textContent='↔';
      names.append(cardRef(s.selected[slots[0]]),arrow,cardRef(s.selected[slots[1]]));
      const button = document.createElement('button'); button.id = `test-${slot.id}`;
      button.textContent = known ? 'Уже известно' : `Исследовать · −${view.pairTestCost} ${shared ? 'Science' : 'заряд'}`;
      button.setAttribute('aria-label', `Исследовать: ${slot.name.toLowerCase()} + ${view.slots[i+1].name.toLowerCase()}`);
      button.disabled = s.status !== 'playing' || Boolean(known) || (shared ? s.science : s.research) < view.pairTestCost || !complete;
      button.onclick = () => action({type:'pairTest',slots}); panel.append(heading,status,names,button); return panel;
    }));
    $('relations').replaceChildren(relationJournal(s));
    const summary = $('formula-compatibility'); summary.replaceChildren();
    const complete = view.slots.every(slot => s.selected[slot.id]);
    summary.hidden = !complete;
    const edges = view.slots.slice(0,-1).map((slot,i) => {
      const slots = [slot.id,view.slots[i+1].id];
      return s.knownRelations.find(r => pairMatches(r,slots,s.selected));
    });
    const state = !complete ? 'incomplete' : edges.some(r => r && !r.stable) ? 'incompatible' :
      edges.every(r => r?.stable) ? 'stable' : 'unknown';
    summary.className = `formula-compatibility ${state}`;
    const label = document.createElement('span'); label.className = 'verdict';
    label.textContent = {incomplete:'Выберите по одному компоненту в каждом столбце',incompatible:'⊘ Есть несовместимая пара',stable:showClueRoles?'✓ Обе пары стабильны.':'✓ Обе пары стабильны. Сверьте сведения о составе.',unknown:'Совместимость смеси пока неизвестна.'}[state];
    summary.append(label);
  }
  const submissions = s.history.filter(h=>h.type!=='pairTest' && h.type!=='refill');
  const initialScience = s.science + submissions.reduce((total,h)=>total+h.cost,0);
  $('budget').textContent = shared ? `Science: ${s.science} · проверка смеси: ${view.submissionCost}` : `Финальных проверок: ${Math.floor(s.science/view.submissionCost)} из ${Math.floor(initialScience/view.submissionCost)} · цена ${view.submissionCost} Science`;
  $('budget').hidden=showClueRoles && shared;
  $('lab-supply').hidden=!showClueRoles || !shared;
  if(showClueRoles && shared){
    $('lab-supply').append($('refill'));
    $('supply-budget').textContent=`Запас: ${s.science} Science`;
  }
  if(showClueRoles){
    if(!$('submit').querySelector('.synthesis-label')){
      $('submit').innerHTML='<svg class="synthesis-seal" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><circle cx="32" cy="32" r="29"/><circle class="seal-inner" cx="32" cy="32" r="23"/><path d="M24 16h16m-12 0v13L18 45q-2 4 3 4h22q5 0 3-4L36 29V16M22 38h20M28 10v-3m8 3v-3M10 28H7m3 8H7m47-8h3m-3 8h3M28 54v3m8-3v3"/><path class="seal-liquid" d="M22 39h20l4 7q1 3-3 3H21q-4 0-3-3Z"/><circle class="seal-bubble" cx="29" cy="33" r="1.6"/><circle class="seal-bubble" cx="35" cy="28" r="1.2"/></svg><span class="synthesis-label"><span class="synthesis-title">Смешать и проверить</span><span class="synthesis-cost"></span></span>';
    }
    $('submit').querySelector('.synthesis-cost').textContent=`−${view.submissionCost} Science`;
    $('submit').setAttribute('aria-label',`Смешать и проверить · ${view.submissionCost} Science`);
    $('synthesis-guide').hidden=false;
    $('synthesis-guide').textContent=view.slots.length===3
      ? 'Формула верна, если соблюдены условия состава и обе соседние пары стабильны.'
      : 'Формула верна, если выбранные компоненты соблюдают условия состава.';
  }
  $('refill').hidden = !shared;
  $('refill').textContent = `Пополнить запас · +${view.economy?.refillAmount ?? 0} Science`;
  $('refill').disabled = s.status !== 'playing';
  $('submit').disabled = s.status !== 'playing' || s.science < view.submissionCost || !view.slots.every(slot => s.selected[slot.id]);
  const lastSubmission = submissions.at(-1);
  $('result').textContent = s.status === 'solved' ? 'Формула найдена! Ваше исследование завершено.' : s.status === 'exhausted' ? 'Формула не подошла. Финальных проверок не осталось.' : lastSubmission && !lastSubmission.success ? 'Формула не подошла. Можно продолжить исследование.' : '';
  const support=Boolean(view.researchSupport);
  const previous=support?selectedSubmission(view):undefined;
  $('submit-reason').hidden=!support;
  $('submit-reason').textContent=support?submitBlockReason(view):'';
  $('composition-reminder').hidden=!support || !compositionReminder(previous);
  $('composition-reminder').textContent=support?compositionReminder(previous):'';
  $('selected-history').hidden=!previous;
  $('selected-history').textContent=previous?`Эта смесь уже проверена: ${previous.success?'формула найдена':'формула не подошла'}.${s.status==='playing'?` Повторная проверка стоит ${view.submissionCost} Science.`:''}`:'';
  $('mixture-history').hidden=!support || !recordedSubmissions(view).length;
  $('mixtures').replaceChildren(...(support?recordedSubmissions(view):[]).map((h,i)=>{
    const li=document.createElement('li'),refs=document.createElement('span');refs.className='mixture-refs';
    for(const slot of view.slots)refs.append(cardRef(h.tuple[slot.id]));
    const verdict=document.createElement('span');verdict.textContent=`${h.success?'✓ Формула найдена':'Формула не подошла'} · −${h.cost} Science`;
    li.setAttribute('aria-label',`Проверка ${i+1}: ${view.slots.map(slot=>name(h.tuple[slot.id])).join(' + ')} — ${h.success?'успех':'неудача'}`);
    li.append(refs,verdict);return li;
  }));
  if (focused && $(focused) !== document.activeElement) $(focused)?.focus({preventScroll:true});
}
async function request(path, body) {
  const r = await fetch(path, {signal:AbortSignal.timeout(5000), ...(body ? {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)} : {})});
  const data = await r.json(); if (!r.ok) throw new Error(data.error); return data;
}
function action(body) {
  queue = queue.then(async () => {
    try {view = await request('/api/action', body); await loadSupport(); render(); $('error').textContent = '';}
    catch(e) {$('error').textContent = e.message;}
  });
  return queue;
}
$('submit').onclick = () => action({type:'submit'});
$('refill').onclick = () => action({type:'refill'});
async function loadSupport() {
  if(view.researchSupport && !submitBlockReason) {
    const module=await import('./support.mjs');
    ({submitBlockReason,submissions:recordedSubmissions,selectedSubmission,compositionReminder}=module);
  }
}
try {view = await request('/api/state'); await loadSupport(); render();}
catch(e) {$('error').textContent = `Не удалось загрузить опыт: ${e.message}`;}
// Finite requests keep the embedded browser's navigation from waiting on a
// permanent stream. Read only public presentation files; never reset sessions.
const presentationFiles = ['/', '/app.mjs', '/style.css',...(view?.researchSupport?['/support.mjs']:[])];
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
