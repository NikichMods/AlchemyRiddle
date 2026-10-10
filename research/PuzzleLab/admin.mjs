// SPDX-License-Identifier: MPL-2.0
import http from 'node:http';
import {readFileSync,readdirSync,writeFileSync,renameSync,existsSync,openSync,closeSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFile,spawn} from 'node:child_process';
import {promisify} from 'node:util';
import {sessionKey,newTelemetry,summarize} from './telemetry.mjs';
const run=promisify(execFile),root=new URL('./',import.meta.url);
function runControl(directory,nodePath,mode){
  // Background grandchildren may retain pipe handles on Windows. Use files
  // and the launcher's exit event, rather than waiting for inherited pipe EOF.
  const out=join(directory,'ngrok/control.stdout.log'),err=join(directory,'ngrok/control.stderr.log');
  return new Promise((resolve,reject)=>{
    const outFd=openSync(out,'w'),errFd=openSync(err,'w');let child;
    try {child=spawn('powershell.exe',['-NoProfile','-ExecutionPolicy','Bypass','-File',fileURLToPath(new URL('./ngrok-playtest.ps1',root)),'-Mode',mode,'-PrivateDirectory',directory,'-NodePath',nodePath],{windowsHide:true,stdio:['ignore',outFd,errFd]});}
    finally{closeSync(outFd);closeSync(errFd);}
    const timeout=setTimeout(()=>{child.kill();reject(new Error('Control timeout'));},60000);
    child.once('error',error=>{clearTimeout(timeout);reject(error);});
    child.once('exit',code=>{clearTimeout(timeout);const stdout=readFileSync(out,'utf8'),stderr=readFileSync(err,'utf8');if(code===0)resolve({stdout});else reject(Object.assign(new Error('Control failed'),{stdout,stderr}));});
  });
}
function read(path,fallback){try{return JSON.parse(readFileSync(path,'utf8').replace(/^\uFEFF/,''));}catch{return fallback;}}
export function snapshot(directory,now=Date.now()) {
  const fixture=read(join(directory,'fixture.json'),{}),qa=read(join(directory,'ngrok/qa.json'),{});
  const qaKeys=new Set([qa.cookieA,qa.cookieB].filter(Boolean).map(c=>sessionKey(c.match(/__Host-lab=([^;]+)/)?.[1]??'')));
  const tags=read(join(directory,'panel-tags.json'),{}),sessions=[],warnings=[];
  for(const filename of readdirSync(join(directory,'sessions')).filter(n=>/^[a-f0-9-]{36}\.json$/.test(n))) {
    const data=read(join(directory,'sessions',filename),null);
    if(!data?.state){warnings.push('Одна сессия не прочитана; повторите обновление.');continue;}
    const id=filename.slice(0,-5),key=sessionKey(id),log=data.telemetry??newTelemetry(id,true);
    if(!data.telemetry){log.recordingStartedAt=null;}
    const kind=tags[key]??(qaKeys.has(key)?'test':'player');
    const profile=data.state.schema===1&&data.state.campaignId?data.state:null;
    const state=profile?profile.active.state:data.state;
    const summary=summarize(log,state,now);
    sessions.push({key,kind:profile?.mode==='sandbox'?'test':kind,...summary,selection:state.selected,history:state.history,events:log.events,
      ...(profile?{campaign:{id:profile.campaignId,worldId:profile.worldId,mode:profile.mode,
        puzzleId:profile.active.fixture.id,stage:profile.active.stage.id,rung:profile.active.stage.rung,band:profile.active.stage.band,
        initialKnowledge:profile.active.initialKnowledge,totalSpent:profile.spent,refills:profile.refills,
        completed:profile.completed,knowledge:profile.knowledge}}:{})});
  }
  sessions.sort((a,b)=>(b.lastEventAt??'').localeCompare(a.lastEventAt??''));
  const players=sessions.filter(s=>s.kind==='player'&&s.participant);
  return {fixture:{id:fixture.id,title:fixture.title,slots:fixture.slots?.map(s=>({id:s.id,name:s.name,cards:s.cards.map(c=>({id:c.id,name:c.name}))}))},sessions,warnings,
    totals:{sessions:players.length,solved:players.filter(s=>s.status==='solved').length,exhausted:players.filter(s=>s.status==='exhausted').length,playing:players.filter(s=>s.status==='playing').length,online:players.filter(s=>s.online).length},
    checkedAt:new Date(now).toISOString(),running:read(join(directory,'ngrok/running.json'),null)};
}
export function createAdmin({privateDirectory,nodePath,control,processStatus}={}) {
  let busy=false;
  return http.createServer(async(req,res)=>{
    const host=req.headers.host,port=res.socket.localPort;
    const origin=`http://${host}`;
    if(![`127.0.0.1:${port}`,`localhost:${port}`].includes(host)||req.headers['sec-fetch-site']==='cross-site'||
       (req.headers.origin&&req.headers.origin!==origin)||(req.method==='POST'&&req.headers.origin!==origin)){res.writeHead(403).end();return;}
    res.setHeader('Cache-Control','no-store');res.setHeader('X-Content-Type-Options','nosniff');
    res.setHeader('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'");
    const json=(data,status=200)=>{res.writeHead(status,{'Content-Type':'application/json; charset=utf-8'});res.end(JSON.stringify(data));};
    const path=new URL(req.url,origin).pathname;
    try {
      const assets={'/':'admin.html','/admin-ui.mjs':'admin-ui.mjs','/admin.css':'admin.css'};
      if(req.method==='GET'&&assets[path]){res.writeHead(200,{'Content-Type':path==='/'?'text/html; charset=utf-8':path.endsWith('.mjs')?'text/javascript; charset=utf-8':'text/css; charset=utf-8'});res.end(readFileSync(new URL(assets[path],root)));return;}
      if(req.method==='GET'&&path==='/api/overview'){
        const data=snapshot(privateDirectory);data.busy=busy;
        data.processes=processStatus?await processStatus():null;json(data);return;
      }
      if(req.method==='GET'&&path==='/api/export'){
        res.setHeader('Content-Disposition','attachment; filename="puzzle-lab-playtest.json"');
        const data=snapshot(privateDirectory);delete data.running;json(data);return;
      }
      if(req.method!=='POST'||!['/api/control','/api/tag'].includes(path)){json({error:'Not found'},404);return;}
      if(req.headers['content-type']?.split(';')[0]!=='application/json'){json({error:'Expected JSON'},415);return;}
      let text='';for await(const chunk of req){text+=chunk;if(text.length>2000)throw new Error('Large request');}
      const body=JSON.parse(text);
      if(path==='/api/tag'){
        if(!['player','test','owner'].includes(body.kind)||!snapshot(privateDirectory).sessions.some(s=>s.key===body.key))throw new Error('Invalid session category');
        const target=join(privateDirectory,'panel-tags.json'),tags=read(target,{});tags[body.key]=body.kind;
        writeFileSync(target+'.tmp',JSON.stringify(tags,null,2));renameSync(target+'.tmp',target);json({ok:true});return;
      }
      if(!['Start','Stop','Status'].includes(body.mode))throw new Error('Invalid command');
      if(busy){json({error:'Другая команда ещё выполняется'},409);return;}
      busy=true;
      try {
        const result=control?await control(body.mode):await runControl(privateDirectory,nodePath,body.mode);
        json({ok:true,message:result.stdout??String(result)});
      } finally {busy=false;}
    } catch(error){json({error:error.stdout||error.stderr||'Не удалось выполнить запрос; повторите проверку состояния.'},400);}
  });
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const arg=name=>process.argv.slice(2).find(a=>a.startsWith(`--${name}=`))?.slice(name.length+3);
  const privateDirectory=resolve(arg('private-dir')??''),nodePath=arg('node')??process.execPath,port=Number(arg('port')??4185);
  if(!arg('private-dir')||!existsSync(join(privateDirectory,'sessions'))||[4183,4184].includes(port))throw new Error('Separate admin port and private directory required');
  const processStatus=async()=>{
    const script=`$r=Get-Content -LiteralPath '${join(privateDirectory,'ngrok/running.json').replaceAll("'","''")}' -Raw | ConvertFrom-Json; $o=@{}; foreach($name in @('server','tunnel')) {$e=$r.$name;$p=Get-Process -Id $e.id -ErrorAction SilentlyContinue;$o[$name]=[bool]($p -and $p.Path -eq $e.path -and $p.StartTime.ToUniversalTime().ToString('o') -eq ([DateTime]$e.startedAt).ToUniversalTime().ToString('o'))};$o|ConvertTo-Json -Compress`;
    try {const result=await run('powershell.exe',['-NoProfile','-Command',script],{windowsHide:true,timeout:5000});return JSON.parse(result.stdout);}catch{return {server:false,tunnel:false};}
  };
  const server=createAdmin({privateDirectory,nodePath,processStatus});
  server.listen(port,'127.0.0.1',()=>console.log(`Private facilitator panel: http://127.0.0.1:${port}/`));
}
