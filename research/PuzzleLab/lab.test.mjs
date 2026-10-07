// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {act, candidates, clueText, createState, publicView, satisfies, validate} from './rules.mjs';
import {createLab} from './server.mjs';
const fixture = JSON.parse(readFileSync(new URL('./fixture.json', import.meta.url)));

test('fifth fixture links opposite-slot implications; every clue removes a plausible alternative', () => {
  const f = JSON.parse(readFileSync(new URL('./fixtures/dew-05.json', import.meta.url)));
  validate(f);
  const rows = candidates(f);
  const alternatives = [
    {powder:'p1',fluid:'f3'}, {powder:'p3',fluid:'f1'},
    {powder:'p2',fluid:'f1'}, {powder:'p3',fluid:'f2'}
  ];
  f.clues.forEach((clue, omitted) => {
    assert.ok(rows.filter(t => satisfies(f,t,clue)).length > 1);
    assert.deepEqual(f.clues.map(c => satisfies(f,alternatives[omitted],c)),
      f.clues.map((_,i) => i !== omitted));
  });
  // The linked implications derive Powder Water for Mineral hypotheses;
  // the count and overlap then reject all such hypotheses, without a literal.
  const chain = rows.filter(t => [f.clues[0],f.clues[2]].every(c => satisfies(f,t,c)));
  assert.ok(chain.filter(t => t.powder === 'p1').length === 0);
  assert.deepEqual(chain.filter(t => t.powder === 'p3').map(t => t.fluid),['f1','f2']);
  assert.equal(satisfies(f,{powder:'p3',fluid:'f1'},f.clues[1]),false);
  assert.equal(satisfies(f,{powder:'p3',fluid:'f2'},f.clues[3]),false);
});
test('fourth fixture is unique, every clue necessary, target condition active without a supplied literal', () => {
  const f = JSON.parse(readFileSync(new URL('./fixtures/ink-04.json', import.meta.url)));
  validate(f);
  const rows = candidates(f);
  for (let omit=0; omit<f.clues.length; omit++) {
    assert.ok(rows.filter(t => f.clues.every((c,i) => i===omit || satisfies(f,t,c))).length>1);
  }
  assert.equal(rows.filter(t => f.clues.slice(0,2).every(c => satisfies(f,t,c))).length,3);
  const implication = f.clues.find(c => c.kind==='implies');
  const powder = f.slots[0].cards.find(c => c.id === f.answer.powder);
  const fluid = f.slots[1].cards.find(c => c.id === f.answer.fluid);
  assert.ok(powder.tags.includes(implication.if.tag));
  assert.ok(fluid.tags.includes(implication.then.tag));
  assert.equal(satisfies(f,{powder:'p1',fluid:'f3'},implication),false);
  assert.equal(satisfies(f,{powder:'p2',fluid:'f3'},implication),true);
});
test('third fixture has distinct necessary constraints and consistent overlap/prohibition semantics', () => {
  const f = JSON.parse(readFileSync(new URL('./fixtures/mist-03.json', import.meta.url)));
  validate(f);
  const rows = candidates(f);
  assert.equal(new Set(f.clues.map(c => c.kind)).size,3);
  for (let omit=0; omit<f.clues.length; omit++) {
    assert.ok(rows.filter(t => f.clues.every((c,i) => i===omit || satisfies(f,t,c))).length>1);
  }
  assert.equal(rows.filter(t => f.clues.slice(0,2).every(c => satisfies(f,t,c))).length,2);
  assert.equal(satisfies(f,{powder:'p1',fluid:'f1'},f.clues[0]),true);
  assert.equal(satisfies(f,{powder:'p1',fluid:'f2'},f.clues[0]),false);
  assert.equal(satisfies(f,{powder:'p1',fluid:'f1'},f.clues[2]),false);
  assert.equal(satisfies(f,{powder:'p3',fluid:'f1'},f.clues[2]),true);
  assert.equal(satisfies(f,{powder:'p1',fluid:'f3'},f.clues[2]),true);
});
test('second fixture is unique, each clue is necessary, compact wording preserves count semantics', () => {
  const f = JSON.parse(readFileSync(new URL('./fixtures/amber-02.json', import.meta.url)));
  validate(f);
  const rows = candidates(f);
  assert.equal(rows.length,9);
  for (let omitted = 0; omitted < f.clues.length; omitted++) {
    assert.ok(rows.filter(t => f.clues.every((c,i) => i === omitted || satisfies(f,t,c))).length > 1);
    assert.ok(rows.filter(t => satisfies(f,t,f.clues[omitted])).length > 1);
    assert.equal((clueText(f,f.clues[omitted]).match(/«/g) ?? []).length,1);
  }
  assert.equal(rows.filter(t => f.clues.every(c => satisfies(f,t,c))).length,1);
});
test('fixture is unique; both clues are necessary and individually partial', () => {
  validate(fixture);
  const all = candidates(fixture);
  assert.equal(all.length, 4);
  assert.equal(all.filter(t => fixture.clues.every(c => satisfies(fixture,t,c))).length, 1);
  for (const c of fixture.clues) assert.ok(all.filter(t => satisfies(fixture,t,c)).length > 1);
  const broken = structuredClone(fixture); broken.answer.powder = 'p2';
  assert.throws(() => validate(broken));
});
test('implication and exact-one implement all four truth combinations', () => {
  const rows = candidates(fixture).map(t => fixture.clues.map(c => satisfies(fixture,t,c)));
  assert.deepEqual(rows, [[true,true], [false,true], [false,true], [true,false]]);
});
test('invalid submissions are free; marks do not solve or narrow automatically', () => {
  const s = createState(fixture);
  assert.throws(() => act(fixture,s,{type:'submit'}));
  assert.equal(s.science, 1);
  act(fixture,s,{type:'mark',slot:'powder',card:'p1'});
  assert.equal(s.marks.p1, true); assert.equal(s.status, 'playing'); assert.deepEqual(s.selected, {});
  assert.throws(() => act(fixture,s,{type:'select',slot:'powder',card:'f1'}));
});
test('failure consumes budget and gives no partial answer; repeated checks are blocked', () => {
  const s = createState(fixture); s.selected = {powder:'p2',fluid:'f2'};
  act(fixture,s,{type:'submit'});
  assert.equal(s.science, 0); assert.equal(s.status, 'exhausted');
  assert.deepEqual(s.history, [{tuple:{powder:'p2',fluid:'f2'},success:false,cost:1}]);
  assert.throws(() => act(fixture,s,{type:'submit'}));
  assert.equal(s.history.length, 1);
});
test('successful submission completes once; public projection omits facilitator fields', () => {
  const s = createState(fixture); s.selected = {...fixture.answer}; act(fixture,s,{type:'submit'});
  assert.equal(s.status, 'solved'); assert.equal(s.science, 0);
  assert.throws(() => act(fixture,s,{type:'submit'}));
  const projected = publicView(fixture,s);
  assert.equal(projected.answer, undefined); assert.ok(projected.clues.every(c => typeof c === 'string'));
});
async function serve(t, debug = false) {
  const server = createLab({debug});
  await new Promise(r => server.listen(0,'127.0.0.1',r));
  t.after(() => new Promise(r => {server.close(r); server.closeAllConnections();}));
  return `http://127.0.0.1:${server.address().port}`;
}
test('HTTP player session survives refresh; source and facilitator routes are unavailable', async t => {
  const base = await serve(t);
  const first = await fetch(base+'/api/state'); const cookie = first.headers.get('set-cookie').split(';')[0];
  assert.equal((await first.json()).answer, undefined);
  const headers = {Cookie:cookie,'Content-Type':'application/json'};
  await fetch(base+'/api/action',{method:'POST',headers,body:JSON.stringify({type:'notes',text:'Моя гипотеза'})});
  const refreshed = await (await fetch(base+'/api/state',{headers})).json(); assert.equal(refreshed.state.notes,'Моя гипотеза');
  for (const path of ['/fixture.json','/rules.mjs','/server.mjs','/api/debug','/facilitator','/../fixture.json']) assert.equal((await fetch(base+path)).status,404);
  assert.equal((await fetch(base+'/api/action',{method:'POST',headers,body:'{'})).status,400);
  assert.equal((await fetch(base+'/api/action',{method:'POST',headers:{...headers,Origin:'http://example.com'},body:'{}'})).status,403);
});
test('facilitator mode reports truth table and live session independently', async t => {
  const base = await serve(t,true);
  await fetch(base+'/api/state');
  const data = await (await fetch(base+'/api/debug')).json();
  assert.deepEqual(data.fixture.answer,fixture.answer); assert.equal(data.rows.length,4); assert.equal(data.sessions.length,1);
  assert.equal(data.rows.filter(r => r.clues.every(Boolean)).length,1);
});
