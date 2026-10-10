// SPDX-License-Identifier: MPL-2.0
import {createHash} from 'node:crypto';
const traits=['Любопытный','Хитрый','Вдумчивый','Отважный','Задумчивый','Весёлый','Тихий','Бодрый','Зоркий','Смелый','Ловкий','Упорный'];
const animals=['Тетерев','Лис','Барсук','Ёж','Бобр','Филин','Енот','Дрозд','Заяц','Соболь','Хомяк','Кот'];
export const sessionKey=id=>createHash('sha256').update(id).digest('hex').slice(0,16);
export function newTelemetry(id,legacy=false,now=new Date().toISOString()) {
  const hash=createHash('sha256').update(id).digest();
  return {version:1,nickname:`${traits[hash[0]%traits.length]} ${animals[hash[1]%animals.length]}`,legacy,recordingStartedAt:now,startedAt:null,completedAt:null,events:[]};
}
export function recordEvent(log,kind,detail={},at=new Date().toISOString()) {
  log.events.push({seq:(log.events.at(-1)?.seq??0)+1,at,kind,...detail});
  // A bounded playtest file, not an unbounded public logging service.
  if (log.events.length>20000) {log.events.shift();log.truncated=true;}
}
export function recordAction(log,action,before,after,error,at=new Date().toISOString()) {
  const types=['select','toggleSelect','selectPair','pairTest','submit','refill','mark','notes'];
  const safeAction={type:types.includes(action?.type)?action.type:'unknown'};
  for (const field of ['slot','card']) if(typeof action?.[field]==='string') safeAction[field]=action[field].slice(0,80);
  if(Array.isArray(action?.slots)) safeAction.slots=action.slots.slice(0,3).map(v=>String(v).slice(0,80));
  if(action?.type==='notes') safeAction.length=typeof action.text==='string'?action.text.length:0;
  if(!log.startedAt)log.startedAt=at;
  recordEvent(log,error?'action_rejected':'action',{action:safeAction,selection:{...after.selected},science:after.science,status:after.status,...(error?{error:String(error).slice(0,180)}:{}),outcomes:after.history.slice(before.history.length)},at);
  if(!error && before.status==='playing' && after.status!=='playing' && !log.completedAt)log.completedAt=at;
}
export function recordPage(log,event,at=new Date().toISOString()) {
  const kinds=['page','visible','hidden','heartbeat','help_open','help_close'];
  if(!kinds.includes(event?.kind)||typeof event.tab!=='string'||!/^[a-f0-9-]{36}$/.test(event.tab))throw new Error('Invalid page event');
  if(!log.startedAt)log.startedAt=at;
  recordEvent(log,event.kind,{tab:event.tab},at);
}
export function summarize(log,state,now=Date.now()) {
  const events=log?.events??[], tabs=new Map(), intervals=[];
  for(const e of events) {
    if(!e.tab)continue;
    const time=Date.parse(e.at),prev=tabs.get(e.tab);
    if(prev?.visible && time>=prev.time) intervals.push([prev.time,Math.min(time,prev.time+20000,log.completedAt?Date.parse(log.completedAt):Infinity)]);
    if(['hidden'].includes(e.kind))tabs.set(e.tab,{time,visible:false});
    else if(['page','visible','heartbeat'].includes(e.kind))tabs.set(e.tab,{time,visible:true});
    else if(prev)tabs.set(e.tab,{time,visible:prev.visible});
  }
  intervals.sort((a,b)=>a[0]-b[0]);let visibleMs=0,end=0;
  for(const [start,stop] of intervals){visibleMs+=Math.max(0,stop-Math.max(start,end));end=Math.max(end,stop);}
  const actions=events.filter(e=>e.kind==='action');
  const last=events.at(-1)?.at??null;
  return {nickname:log?.nickname??'Старая сессия',legacy:log?.legacy??true,recordingStartedAt:log?.recordingStartedAt??null,
    startedAt:log?.startedAt??null,completedAt:log?.completedAt??null,status:state.status,science:state.science,
    submissions:state.history.filter(h=>typeof h.success==='boolean').length,pairTests:state.history.filter(h=>h.type==='pairTest').length,
    actions:actions.length,rejected:events.filter(e=>e.kind==='action_rejected').length,helpOpens:events.filter(e=>e.kind==='help_open').length,
    elapsedMs:!log?.legacy&&log?.startedAt&&log?.completedAt?Date.parse(log.completedAt)-Date.parse(log.startedAt):null,
    visibleMs:log?.legacy||log?.truncated?null:visibleMs,lastEventAt:last,online:[...tabs.values()].some(t=>t.visible&&now-t.time<25000),
    participant:!!log?.startedAt||state.history.length>0,truncated:!!log?.truncated};
}
