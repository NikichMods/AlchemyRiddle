// SPDX-License-Identifier: MPL-2.0
import http from 'node:http';
import {readFileSync, watch} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
import {randomUUID} from 'node:crypto';
import {act, candidates, createState, publicView, satisfies, validate} from './rules.mjs';
const root = new URL('./', import.meta.url);
export function createLab({fixturePath = new URL('fixture.json', root), debug = false, liveReload = false} = {}) {
  let fixture = JSON.parse(readFileSync(fixturePath, 'utf8'));
  validate(fixture);
  const sessions = new Map();
  const assets = {'/': 'index.html', '/app.mjs': 'app.mjs', '/style.css': 'style.css'};
  const server = http.createServer(async (req, res) => {
    const host = req.headers.host;
    const port = server.address().port;
    if (![ `127.0.0.1:${port}`, `localhost:${port}` ].includes(host)) {res.writeHead(403).end(); return;}
    if (req.headers.origin && req.headers.origin !== `http://${host}`) {res.writeHead(403).end(); return;}
    res.setHeader('Cache-Control', 'no-store');
    res.setHeader('X-Content-Type-Options', 'nosniff');
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
      if (!((path === '/api/state' && req.method === 'GET') || (path === '/api/action' && req.method === 'POST'))) {json({error:'Not found'}, 404); return;}
      let id = req.headers.cookie?.match(/(?:^|; )lab=([^;]+)/)?.[1];
      if (!sessions.has(id)) {
        id = randomUUID(); sessions.set(id, createState(fixture));
        res.setHeader('Set-Cookie', `lab=${id}; HttpOnly; SameSite=Strict; Path=/`);
      }
      const state = sessions.get(id);
      if (req.method === 'POST') {
        let body = ''; for await (const chunk of req) {body += chunk; if (body.length > 20000) throw new Error('Слишком большой запрос');}
        act(fixture, state, JSON.parse(body));
      }
      json(publicView(fixture, state));
    } catch (error) {json({error: error.message}, 400);}
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
  const port = portArg ? Number(portArg.slice(7)) : 4173;
  const server = createLab({debug: args.includes('--debug'), liveReload: true,
    ...(fixtureArg ? {fixturePath: resolve(fixtureArg.slice(10))} : {})});
  server.on('error', e => {console.error(e.message); process.exitCode = 1;});
  server.listen(port, '127.0.0.1', () => console.log(`Puzzle Lab: http://127.0.0.1:${server.address().port}${args.includes('--debug') ? ' (facilitator enabled at /facilitator)' : ''}`));
}
