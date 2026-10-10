// SPDX-License-Identifier: MPL-2.0
import {readFileSync} from 'node:fs';
import {spawn} from 'node:child_process';
import {randomUUID,createHash} from 'node:crypto';
import {authorWording} from './wording.mjs';
import {act,createState,publicView,validate,legacyClueText} from './rules.mjs';
import {recordAction,recordEvent} from './telemetry.mjs';
const hash=x=>createHash('sha256').update(x).digest('hex');
const slots=['powder','fluid','essence'];
export function createCampaign({bankPath,pythonPath,selectorPath,developer=false,select}={}) {
  const bytes=readFileSync(bankPath),bank=JSON.parse(bytes),bankHash=hash(bytes);
  if(bank.version!==1||!bank.worldId||!bank.packages.length)throw new Error('Invalid campaign bank');
  for(const pkg of bank.packages)validate(pkg.fixture);
  const choose=select??(request=>new Promise((resolve,reject)=>{
    const child=spawn(pythonPath,[selectorPath,'select',bankPath],{windowsHide:true,stdio:['pipe','pipe','pipe']});
    let output='',errors='';
    const timeout=setTimeout(()=>{child.kill();reject(new Error('Подбор превысил лимит; профиль сохранён.'));},35000);
    child.stdout.on('data',c=>{output+=c;if(output.length>2000000)child.kill();});
    child.stderr.on('data',c=>{errors+=c;});
    child.once('error',e=>{clearTimeout(timeout);reject(e);});
    child.once('exit',code=>{clearTimeout(timeout);if(code!==0)reject(new Error('Не удалось подобрать пакет; профиль сохранён.'));else{try{resolve(JSON.parse(output));}catch(e){reject(e);}}});
    child.stdin.end(JSON.stringify(request));
  }));
  function observe(p,edge,stable,source){
    if(typeof stable!=='boolean')throw new Error('Invalid polarity');
    const old=p.knowledge.find(f=>f.edge.every((v,i)=>v===edge[i]));
    if(old&&old.stable!==stable)throw new Error('Knowledge contradiction');
    if(old){if(!old.sources.includes(source))old.sources.push(source);}
    else p.knowledge.push({edge:[...edge],stable,sources:[source]});
  }
  function globalEdge(f,tuple,ids){
    return [ids[0]==='powder'?'PF':'FE',...ids.map(s=>f.slots.find(v=>v.id===s).cards.find(c=>c.id===tuple[s]).globalId)];
  }
  function applyKnowledge(p,f){
    if(!f.compatibility)return;
    f.knownRelations=[];
    for(const fact of p.knowledge){
      const ids=fact.edge[0]==='PF'?slots.slice(0,2):slots.slice(1);
      const cards=ids.map((s,i)=>f.slots.find(v=>v.id===s).cards.find(c=>c.globalId===fact.edge[i+1]));
      if(cards.every(Boolean))f.knownRelations.push({slots:ids,tuple:Object.fromEntries(ids.map((s,i)=>[s,cards[i].id])),stable:fact.stable,source:fact.sources.join('; ')});
    }
  }
  async function start(p,index){
    const stage=bank.stages[index];
    if(!stage){p.finished=true;return;}
    const result=await choose({stage:stage.id,seed:randomUUID(),knowledge:p.knowledge,solved:p.solved,recent:p.recent});
    if(result.status==='known_target'){
      p.skipped.push({stage:stage.id,reason:'known_target'});p.position=index+1;
      if(developer||stage.separate){p.finished=true;return;}
      return start(p,index+1);
    }
    if(result.status!=='selected')throw new Error('Нет подходящего пакета. Критерии сохранены; нужен офлайн-подбор.');
    const f=authorWording(result.fixture,legacyClueText,{variantOffset:parseInt(hash(result.fixture.id).slice(0,6),16)});
    applyKnowledge(p,f);validate(f);
    p.active={fixture:f,state:createState(f),stage:structuredClone(stage),packageId:result.packageId,targetKey:result.targetKey,route:result.route,
              initialKnowledge:structuredClone(p.knowledge),startedAt:new Date().toISOString(),spent:0};
    p.active.state.science=p.science;
    p.position=index;p.finished=false;
  }
  async function create(index=0){
    const p={schema:1,campaignId:bank.id,worldId:bank.worldId,bankHash,revision:0,mode:developer?'sandbox':'player',
      science:20,spent:0,refills:0,refilledScience:0,knowledge:[],solved:[],recent:[],completed:[],skipped:[],position:index,finished:false,receipts:[]};
    if(index===4){
      p.checkpoint='Зрелая лаборатория: 34 явно заданных наблюдения';
      for(const fact of bank.checkpoint)observe(p,fact.edge,fact.stable,fact.source);
    }else if(developer)p.checkpoint='Пустой явно заданный профиль; предыдущие исследования не приписаны';
    await start(p,index);return p;
  }
  function view(p){
    const a=p.active;
    if(!a)throw new Error('No active investigation');
    const result=publicView(a.fixture,a.state);
    result.campaign={id:p.campaignId,worldId:p.worldId,revision:p.revision,puzzleId:a.fixture.id,
      arity:a.stage.arity,band:a.stage.band,rung:a.stage.rung,purpose:a.stage.purpose,mode:p.mode,
      checkpoint:p.checkpoint??null,spent:p.spent,investigationSpent:a.spent,refills:p.refills,refilledScience:p.refilledScience,
      completed:p.completed.length,experience:{two:p.completed.filter(c=>c.arity===2).length,three:p.completed.filter(c=>c.arity===3).length},
      knowledge:{stable:p.knowledge.filter(f=>f.stable).length,incompatible:p.knowledge.filter(f=>!f.stable).length},
      canContinue:a.state.status==='solved'&&!p.finished&&!a.stage.separate&&!developer&&p.position<3,
      sliceComplete:a.state.status==='solved'&&(p.position===3||a.stage.separate),developer,
      ...(developer?{stages:bank.stages.map(s=>({id:s.id,title:s.title,arity:s.arity,rung:s.rung,band:s.band,separate:s.separate})),
        ladders:{
          two:['Лёгкая','Лёгкая','Средняя','Средняя','Высокая','Очень высокая','Максимальная','Высокая','Очень высокая','Максимальная','Средняя','Очень высокая','Босс','Высокая','Максимальная','Босс'],
          three:['Лёгкая','Лёгкая','Средняя','Средняя','Высокая','Очень высокая','Максимальная','Высокая','Босс','Очень высокая','Средняя','Максимальная','Высокая','Очень высокая','Босс','Высокая','Максимальная','Очень высокая','Босс']},startingKnowledge:a.initialKnowledge}: {})};
    return result;
  }
  async function action(p,action){
    if(typeof action.actionId!=='string'||!/^[a-f0-9-]{36}$/.test(action.actionId))throw new Error('Нет идентификатора действия');
    if(p.receipts.includes(action.actionId))return;
    if(action.revision!==p.revision||action.puzzleId!==p.active.fixture.id)throw new Error('Состояние изменилось в другой вкладке. Обновите страницу и повторите выбор.');
    if(action.type==='checkpoint'){
      if(!developer)throw new Error('Только в частной песочнице');
      const index=bank.stages.findIndex(s=>s.id===action.stage);
      if(index<0)throw new Error('Неизвестный сценарий');
      const next=await create(index);next.revision=p.revision+1;next.receipts=[action.actionId];Object.assign(p,next);return;
    }
    if(action.type==='continue'){
      if(developer||p.active.state.status!=='solved'||p.active.stage.separate||p.position>=3)throw new Error('Переход недоступен');
      await start(p,p.position+1);
    }else{
      const a=p.active,before=a.state.history.length;
      act(a.fixture,a.state,action);
      for(const h of a.state.history.slice(before)){
        if(h.type==='refill'){p.refills++;p.refilledScience+=h.amount;}
        else if(h.cost){p.spent+=h.cost;a.spent+=h.cost;}
        if(h.type==='pairTest')observe(p,globalEdge(a.fixture,h.tuple,h.slots),h.stable,`${a.fixture.id}:pair:${a.state.history.length}`);
        if(h.success===true){
          if(a.fixture.compatibility)for(let i=0;i<2;i++)observe(p,globalEdge(a.fixture,h.tuple,slots.slice(i,i+2)),true,`${a.fixture.id}:solved`);
          if(a.fixture.compatibility){const knowledgeFixture=structuredClone(a.fixture);applyKnowledge(p,knowledgeFixture);a.state.knownRelations=knowledgeFixture.knownRelations;}
          if(!p.solved.includes(a.targetKey)){
            p.solved.push(a.targetKey);p.recent.push(a.packageId);
            p.completed.push({puzzleId:a.fixture.id,stage:a.stage.id,arity:a.stage.arity,rung:a.stage.rung,band:a.stage.band,packageId:a.packageId,
              targetKey:a.targetKey,spent:a.spent,completedAt:new Date().toISOString(),fixture:structuredClone(a.fixture),state:structuredClone(a.state)});
          }
        }
      }
      p.science=a.state.science;
    }
    p.revision++;p.receipts.push(action.actionId);if(p.receipts.length>20000)p.receipts.shift();
  }
  function record(log,action,before,after,error){
    if(!['continue','checkpoint'].includes(action.type))recordAction(log,action,before.active.state,after.active.state,error);
    // Individual puzzle completion does not end the whole campaign timeline.
    if(after.active.state.status==='playing'||(!after.active.stage.separate&&after.position<3))log.completedAt=null;
    recordEvent(log,error?'campaign_rejected':'campaign_action',{campaignId:after.campaignId,worldId:after.worldId,
      puzzleId:after.active.fixture.id,stage:after.active.stage.id,rung:after.active.stage.rung,band:after.active.stage.band,
      mode:after.mode,actionType:action.type,totalSpent:after.spent,knowledgeCount:after.knowledge.length,
      revision:after.revision,...(error?{error}: {})});
  }
  return {bankHash,bank,developer,create,view,action,record};
}
