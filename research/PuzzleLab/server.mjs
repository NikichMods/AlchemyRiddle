// SPDX-License-Identifier: MPL-2.0
import http from 'node:http';
import {readFileSync, watch, mkdirSync, existsSync, writeFileSync, renameSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
import {randomUUID, createHash} from 'node:crypto';
import {act, candidates, createState, publicView, satisfies, validate} from './rules.mjs';
import {newTelemetry, recordAction, recordPage} from './telemetry.mjs';
const root = new URL('./', import.meta.url);
export function createLab({fixturePath = new URL('fixture.json', root), debug = false, liveReload = false, stateDirectory, publicOrigin, approvedNgrokOrigin} = {}) {
  let external;
  if (publicOrigin) {
    external = new URL(publicOrigin);
    if (external.origin !== publicOrigin || external.protocol !== 'https:' ||
        !(/^[a-z0-9-]+\.trycloudflare\.com$/.test(external.hostname) ||
          (publicOrigin === approvedNgrokOrigin && /^[a-z0-9-]+\.(?:ngrok-free\.dev|ngrok-free\.app|ngrok\.app)$/.test(external.hostname))) || external.port ||
        debug || liveReload || !stateDirectory) throw new Error('Public Lab requires an exact HTTPS Quick Tunnel origin, durable state, no debug and no reload');
  }
  let fixture = JSON.parse(readFileSync(fixturePath, 'utf8'));
  validate(fixture);
  const sessions = new Map();
  const telemetry = new Map();
  if (stateDirectory) mkdirSync(stateDirectory,{recursive:true});
  const modelHash = () => createHash('sha256').update(JSON.stringify(fixture)).digest('hex');
  const persist = (id,state,log=telemetry.get(id)) => {
    if (!stateDirectory) return;
    const path = resolve(stateDirectory,`${id}.json`);
    writeFileSync(path+'.tmp',JSON.stringify({fixtureHash:modelHash(),state,...(log?{telemetry:log}:{})},null,2));
    renameSync(path+'.tmp',path);
  };
  const assets = {'/': 'index.html', '/app.mjs': 'app.mjs', '/style.css': 'style.css', '/support.mjs':'support.mjs'};
  const server = http.createServer(async (req, res) => {
    const host = req.headers.host;
    const port = server.address().port;
    const externalRequest = external && host === external.host;
    if (!externalRequest && ![ `127.0.0.1:${port}`, `localhost:${port}` ].includes(host)) {res.writeHead(403).end(); return;}
    const origin = externalRequest ? external.origin : `http://${host}`;
    if ((req.headers.origin && req.headers.origin !== origin) ||
        req.headers['sec-fetch-site'] === 'cross-site' ||
        (externalRequest && req.method === 'POST' && req.headers.origin !== origin)) {res.writeHead(403).end(); return;}
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('Referrer-Policy', 'no-referrer');
    res.setHeader('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'");
    const path = new URL(req.url, `http://${host}`).pathname;
    const json = (value, status = 200) => {res.writeHead(status, {'Content-Type': 'application/json; charset=utf-8'}); res.end(JSON.stringify(value));};
    try {
      if (req.method === 'GET' && assets[path]) {
        const ext = assets[path].split('.').pop();
        res.writeHead(200, {'Content-Type': {html:'text/html; charset=utf-8', mjs:'text/javascript; charset=utf-8', css:'text/css; charset=utf-8'}[ext]});
        res.end(readFileSync(new URL(assets[path], root))); return;
      }
      if (req.method === 'GET' && path === '/facilitator' && debug) {
        res.writeHead(200, {'Content-Type':'text/html; charset=utf-8'});
        res.end('<!doctype html><html lang="ru"><meta charset="utf-8"><title>Facilitator — spoilers</title><h1>Только для ведущего — содержит ответ</h1><p>Открытие данных нарушит слепоту прохождения.</p><a href="/api/debug">Открыть скрытую модель и таблицу проверок</a></html>'); return;
      }
      if (req.method === 'GET' && path === '/api/debug' && debug) {
        json({fixture, rows: candidates(fixture).map(tuple => ({tuple, clues: fixture.clues.map(c => satisfies(fixture, tuple, c))})), sessions: [...sessions.values()]}); return;
      }
      if (!((path === '/api/state' && req.method === 'GET') || (path === '/api/action' && req.method === 'POST') || (stateDirectory && path === '/api/events' && req.method === 'POST'))) {json({error:'Not found'}, 404); return;}
      if (req.method === 'POST' && req.headers['content-type']?.split(';')[0].trim() !== 'application/json') {json({error:'Expected application/json'},415);return;}
      // Cookies do not isolate localhost ports: the public instance must not
      // replace the preserved owner's cookie while being checked locally.
      const cookieName = external ? (externalRequest ? '__Host-lab' : 'lab_playtest') : stateDirectory ? `lab_${createHash('sha256').update(fixture.id).digest('hex').slice(0,12)}` : 'lab';
      let id = req.headers.cookie?.match(new RegExp(`(?:^|; )${cookieName}=([^;]+)`))?.[1];
      if (stateDirectory && /^[a-f0-9-]{36}$/.test(id ?? '') && !sessions.has(id)) {
        const path = resolve(stateDirectory,`${id}.json`);
        if (existsSync(path)) {
          const saved = JSON.parse(readFileSync(path,'utf8'));
          if (saved.fixtureHash === modelHash()) {sessions.set(id,saved.state);telemetry.set(id,saved.telemetry??newTelemetry(id,true));}
        }
      }
      if (!sessions.has(id)) {
        if (external && sessions.size >= 500) {json({error:'Лимит сессий; обратитесь к ведущему'},503);return;}
        id = randomUUID(); sessions.set(id, createState(fixture));
        if(stateDirectory)telemetry.set(id,newTelemetry(id));
        persist(id,sessions.get(id));
        res.setHeader('Set-Cookie', `${cookieName}=${id}; HttpOnly; SameSite=Strict; Path=/${externalRequest ? '; Secure' : ''}${external ? '; Max-Age=2592000' : ''}`);
      }
      let state = sessions.get(id);
      if (req.method === 'POST') {
        let body = ''; for await (const chunk of req) {body += chunk; if (body.length > 20000) throw new Error('Слишком большой запрос');}
        // Another tab can finish an action while this request body is arriving.
        const next = structuredClone(sessions.get(id));
        const action=JSON.parse(body);
        const log=telemetry.has(id)?structuredClone(telemetry.get(id)):null;
        if(path==='/api/events') {
          recordPage(log,action);persist(id,next,log);telemetry.set(id,log);json({ok:true});return;
        }
        try {act(fixture, next, action);} catch(error) {
          if(log){recordAction(log,action,sessions.get(id),sessions.get(id),error.message);persist(id,sessions.get(id),log);telemetry.set(id,log);}
          throw error;
        }
        if(log)recordAction(log,action,sessions.get(id),next);
        persist(id,next,log); if(log)telemetry.set(id,log); sessions.set(id,next); state=next;
      }
      json(publicView(fixture, state));
    } catch (error) {
      if (external && (error.code || error instanceof SyntaxError || error instanceof TypeError)) {
        json({error:'Не удалось обработать запрос'}, error.code ? 500 : 400);
      } else json({error: error.message}, 400);
    }
  });
  const watchers = [];
  if (liveReload) {
    const refresh = () => {
      try {
        const next = JSON.parse(readFileSync(fixturePath, 'utf8')); validate(next);
        if (JSON.stringify(next) !== JSON.stringify(fixture)) {fixture = next; sessions.clear();}
      } catch (e) {console.error('Fixture reload rejected:', e.message);}
    };
    watchers.push(watch(fixturePath, refresh));
  }
  server.on('close', () => {for (const w of watchers) w.close();});
  return server;
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  const fixtureArg = args.find(a => a.startsWith('--fixture='));
  const portArg = args.find(a => a.startsWith('--port='));
  const stateArg = args.find(a => a.startsWith('--state-dir='));
  const port = portArg ? Number(portArg.slice(7)) : 4173;
  const publicArg = args.find(a => a.startsWith('--public-origin='));
  const ngrokArg = args.find(a => a.startsWith('--approved-ngrok-origin='));
  const server = createLab({debug: args.includes('--debug'), liveReload: !publicArg,
    ...(publicArg ? {publicOrigin:publicArg.slice(16)} : {}),
    ...(ngrokArg ? {approvedNgrokOrigin:ngrokArg.slice(24)} : {}),
    ...(stateArg ? {stateDirectory:resolve(stateArg.slice(12))} : {}),
    ...(fixtureArg ? {fixturePath: resolve(fixtureArg.slice(10))} : {})});
  server.on('error', e => {console.error(e.message); process.exitCode = 1;});
  server.listen(port, '127.0.0.1', () => console.log(`Puzzle Lab: http://127.0.0.1:${server.address().port}${args.includes('--debug') ? ' (facilitator enabled at /facilitator)' : ''}`));
}
