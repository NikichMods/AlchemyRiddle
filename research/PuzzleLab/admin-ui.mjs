// SPDX-License-Identifier: MPL-2.0
const $=id=>document.getElementById(id);
let data,selected,busy=false;
const status={playing:'Играет',solved:'Решено',exhausted:'Попытки исчерпаны'};
const duration=ms=>ms==null?'—':`${Math.floor(ms/60000)}:${String(Math.floor(ms/1000)%60).padStart(2,'0')}`;
const date=at=>at?new Date(at).toLocaleString('ru-RU'):'—';
const el=(tag,text)=>{const node=document.createElement(tag);node.textContent=text;return node;};
async function request(path,body){const response=await fetch(path,{...(body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}:{})});const result=await response.json();if(!response.ok)throw new Error(result.error);return result;}
function name(id){return data.fixture.slots?.flatMap(s=>s.cards).find(c=>c.id===id)?.name??id;}
function mixture(tuple){return Object.values(tuple??{}).map(name).join(' + ')||'выбор пуст';}
function showDetail(){
  const session=data?.sessions.find(s=>s.key===selected);$('detail').hidden=!session;if(!session)return;
  $('detail-title').textContent=`${session.nickname} · ${session.key.slice(0,4)}`;
  $('coverage').textContent=session.legacy?'Неполная история: эта сессия существовала до включения журнала. Старые клики и время начала неизвестны.':`Запись с ${date(session.recordingStartedAt)}. Начало: ${date(session.startedAt)}.`;
  if(session.truncated)$('coverage').textContent+=' Достигнут предел журнала: самые ранние события не сохранены.';
  const lines=session.events.filter(e=>$('heartbeats').checked||e.kind!=='heartbeat').map(e=>{
    let text;
    if(e.kind==='action'||e.kind==='action_rejected'){
      const a=e.action;const verbs={toggleSelect:'Нажатие карточки',select:'Выбор карточки',selectPair:'Выбор известной пары',pairTest:'Исследование пары',submit:'Финальная проверка',refill:'Пополнение',mark:'Отметка',notes:'Изменение заметки'};
      text=`${verbs[a.type]??'Неизвестное действие'}${a.card?`: ${name(a.card)}`:''}. Смесь: ${mixture(e.selection)}. Science: ${e.science}.`;
      if(e.kind==='action_rejected')text+=` Отклонено: ${e.error}`;
      for(const result of e.outcomes??[]){if(typeof result.success==='boolean')text+=result.success?' Успех.':' Неудача.';else if(typeof result.stable==='boolean')text+=result.stable?' Совместимо.':' Несовместимо.';}
    }else text={page:'Открыл страницу',visible:'Вернулся к вкладке',hidden:'Скрыл или покинул вкладку',heartbeat:'Вкладка видима: связь со стендом',help_open:'Открыл «Как устроен опыт»',help_close:'Закрыл справку'}[e.kind]??e.kind;
    const li=el('li',text);li.prepend(el('div',`#${e.seq} · ${date(e.at)}`));li.firstChild.className='event-time';return li;
  });
  if(!lines.length)lines.push(el('li','Подробных событий ещё нет.'));
  $('timeline').replaceChildren(...lines);
}
function render(){
  $('puzzle').textContent=`Текущая загадка: ${data.fixture.title??'—'}`;
  $('processes').textContent=`Стенд: ${data.processes?.server?'работает':'остановлен'} · Туннель: ${data.processes?.tunnel?'работает':'остановлен'}`;
  const url=data.running?.url;
  if(url&&/^https:\/\/[a-z0-9-]+\.(ngrok-free\.dev|ngrok-free\.app|ngrok\.app)$/.test(url)){$('public-link').href=url;$('public-link').textContent=url;}
  $('totals').replaceChildren(...[['Сессий',data.totals.sessions],['Решено',data.totals.solved],['Играют',data.totals.playing],['Без попыток',data.totals.exhausted],['Видимая вкладка',data.totals.online]].map(([label,value])=>{const box=el('div',label);box.className='stat';box.prepend(el('strong',value));return box;}));
  const sessions=data.sessions.filter(s=>$('technical').checked||(s.kind==='player'&&s.participant));
  $('sessions').replaceChildren(...sessions.map(s=>{
    const row=document.createElement('tr');
    const title=el('td',s.nickname);const badge=el('span',`${s.key.slice(0,4)}${s.legacy?' · неполная история':''}${s.online?' · вкладка видима':''}`);badge.className='badge';title.append(badge);row.append(title);
    for(const text of [status[s.status]??s.status,duration(s.elapsedMs),duration(s.visibleMs),`${s.pairTests} / ${s.submissions}`])row.append(el('td',text));
    const category=document.createElement('select');category.setAttribute('aria-label',`Категория ${s.nickname}`);
    for(const [value,label] of [['player','Участник'],['owner','Моё прохождение'],['test','Технический тест']]){const option=el('option',label);option.value=value;option.selected=value===s.kind;category.append(option);}
    category.onchange=async()=>{try{await request('/api/tag',{key:s.key,kind:category.value});await refresh();}catch(e){$('warnings').textContent=e.message;}};
    const cell=document.createElement('td');cell.append(category);row.append(cell);
    const detail=el('button','Ход решения');detail.onclick=()=>{selected=s.key;showDetail();$('detail').scrollIntoView({behavior:'smooth'});};const actions=document.createElement('td');actions.append(detail);row.append(actions);return row;
  }));
  $('updated').textContent=`Данные обновлены: ${date(data.checkedAt)}. Автообновление каждые 8 секунд.`;
  $('warnings').textContent=data.warnings.join(' ');
  for(const button of document.querySelectorAll('[data-mode]'))button.disabled=busy||data.busy;
  showDetail();
}
async function refresh(){try{data=await request('/api/overview');render();}catch(e){$('warnings').textContent=e.message;}}
for(const button of document.querySelectorAll('[data-mode]'))button.onclick=async()=>{
  busy=true;render();$('command-result').textContent='Выполняем…';
  try{const result=await request('/api/control',{mode:button.dataset.mode});$('command-result').textContent=result.message;}catch(e){$('command-result').textContent=e.message;}
  finally{busy=false;await refresh();}
};
$('refresh').onclick=refresh;$('technical').onchange=render;$('heartbeats').onchange=showDetail;
await refresh();setInterval(()=>{if(!busy)refresh();},8000);
