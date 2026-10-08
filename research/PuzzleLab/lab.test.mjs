// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {act, candidates, clueText, createState, publicView, satisfies, validate, validFormula} from './rules.mjs';
import {createLab} from './server.mjs';
const fixture = JSON.parse(readFileSync(new URL('./fixture.json', import.meta.url)));
const harbor = JSON.parse(readFileSync(new URL('./fixtures/harbor-06.json', import.meta.url)));

test('single property assertions render directly; zero counts preserve negative meaning', () => {
  const term={slot:fixture.slots[0].id,tag:'Трупное'};
  const negative={kind:'exactly',count:0,terms:[term]};
  assert.equal(clueText(fixture,negative),`${fixture.slots[0].name} не имеет свойства «Трупное».`);
  assert.equal(clueText(fixture,{...negative,count:1}),`${fixture.slots[0].name} имеет свойство «Трупное».`);
  assert.match(clueText(fixture,{...negative,terms:[term,{...term,slot:fixture.slots[1].id}]}),/^Ни одно/);
  for(const tuple of candidates(fixture)) {
    const has=fixture.slots[0].cards.find(c=>c.id===tuple[fixture.slots[0].id]).tags.includes(term.tag);
    assert.equal(satisfies(fixture,tuple,negative),!has);
    assert.equal(satisfies(fixture,tuple,{...negative,count:1}),has);
  }
});

test('count clauses may reference a globally known property absent from one slot', () => {
  const f={slots:[{id:'powder',name:'Порошок',cards:[{id:'p',tags:['A']}]},
    {id:'fluid',name:'Жидкость',cards:[{id:'f',tags:['B']},{id:'g',tags:['A']}]}],
    clues:[{kind:'exactly',count:1,terms:[{slot:'powder',tag:'B'},{slot:'fluid',tag:'B'}]}],
    science:1,submissionCost:1,answer:{powder:'p',fluid:'f'}};
  validate(f);assert.equal(satisfies(f,{powder:'p',fluid:'f'},f.clues[0]),true);
  assert.equal(satisfies(f,{powder:'p',fluid:'g'},f.clues[0]),false);
  assert.throws(()=>validate({...f,clues:[{kind:'exactly',count:1,terms:[{slot:'missing',tag:'B'}]}]}));
  assert.throws(()=>validate({...f,clues:[{kind:'exactly',count:1,terms:[{slot:'powder',tag:'unknown'}]}]}));
  const absent={kind:'exactly',count:0,terms:[{slot:'powder',tag:'C'},{slot:'fluid',tag:'C'}]};
  validate({...f,propertyVocabulary:['C'],clues:[...f.clues,absent]});
  assert.equal(satisfies(f,f.answer,absent),true);
  assert.throws(()=>validate({...f,propertyVocabulary:['C','C']}));
});

test('tenth contrast has necessary clues and fits its precommitted investigative budget', () => {
  const f=JSON.parse(readFileSync(new URL('./fixtures/depth-10.json',import.meta.url)));
  validate(f);assert.ok(f.slots.every(s=>s.cards.length===4));
  const s=createState(f);assert.deepEqual(s.selected,{});assert.deepEqual(s.history,[]);
  assert.equal(s.science,3);assert.ok(s.knownRelations.every(r=>r.stable));
  for(let i=0;i<f.clues.length;i++)assert.ok(candidates(f).filter(t=>validFormula({...f,clues:f.clues.filter((_,j)=>j!==i)},t)).length>1);
  const probes=['f2:e1','p1:f2','p2:f1','p4:f2','p4:f4','p1:f4','f4:e1'];
  for(const key of probes){
    const [a,b]=key.split(':');const i=a.startsWith('p')?0:1;
    const slots=[f.slots[i].id,f.slots[i+1].id];s.selected={[slots[0]]:a,[slots[1]]:b};
    act(f,s,{type:'pairTest',slots});
  }
  const compatibleWithKnowledge=candidates(f).filter(t=>f.clues.every(c=>satisfies(f,t,c))&&!s.knownRelations.some(r=>!r.stable&&r.slots.every(id=>t[id]===r.tuple[id])));
  assert.deepEqual(compatibleWithKnowledge,[f.answer]);assert.equal(s.research,2);
  s.selected={...f.answer};act(f,s,{type:'submit'});assert.equal(s.status,'solved');
});

test('ninth fixture starts empty with three checks; every clue matters and branch research fits the budget', () => {
  const f=JSON.parse(readFileSync(new URL('./fixtures/lantern-09.json',import.meta.url)));
  validate(f); const s=createState(f);
  assert.deepEqual(s.selected,{}); assert.deepEqual(s.history,[]);
  assert.equal(s.science,3); assert.equal(s.status,'playing');
  assert.ok(s.knownRelations.every(r=>r.stable));
  for (let i=0;i<f.clues.length;i++) {
    const reduced={...f,clues:f.clues.filter((_,j)=>j!==i)};
    assert.ok(candidates(f).filter(t=>validFormula(reduced,t)).length>1);
  }
  for (const [slots,tuple] of [
    [['fluid','essence'],{fluid:'f1',essence:'e3'}],
    [['fluid','essence'],{fluid:'f1',essence:'e1'}],
    [['powder','fluid'],{powder:'p2',fluid:'f2'}],
    [['fluid','essence'],{fluid:'f2',essence:'e1'}]
  ]) {s.selected=tuple;act(f,s,{type:'pairTest',slots});}
  assert.equal(s.research,2); assert.equal(s.science,3);
  s.selected={...f.answer};act(f,s,{type:'submit'});
  assert.equal(s.status,'solved'); assert.equal(s.science,2);
});

test('three-Science model permits research after failed synthesis and success on the third check', () => {
  const f={...harbor,science:3}; validate(f); const s=createState(f);
  s.selected={powder:'p1',fluid:'f3',essence:'e2'};
  act(f,s,{type:'submit'}); assert.equal(s.science,2); assert.equal(s.status,'playing');
  act(f,s,{type:'pairTest',slots:['fluid','essence']}); assert.equal(s.research,3);
  act(f,s,{type:'submit'}); assert.equal(s.science,1); assert.equal(s.status,'playing');
  s.selected={...f.answer}; act(f,s,{type:'submit'});
  assert.equal(s.science,0); assert.equal(s.status,'solved');
  assert.deepEqual(s.history.filter(h=>h.type!=='pairTest').map(h=>h.success),[false,false,true]);
});

test('eighth fixture links conditionals without requiring their premises and budgets branch-first research', () => {
  const f=JSON.parse(readFileSync(new URL('./fixtures/tide-08.json',import.meta.url)));
  validate(f); const rows=candidates(f), possible=rows.filter(t=>f.clues.every(c=>satisfies(f,t,c)));
  assert.equal(possible.length,5); assert.ok(f.knownRelations.every(r=>r.stable));
  const adjacent=[['powder','fluid'],['fluid','essence']];
  const matches=(r,t,slots)=>r.slots.every((id,i)=>id===slots[i]) && slots.every(id=>r.tuple[id]===t[id]);
  assert.ok(possible.every(t=>!adjacent.every(slots=>f.knownRelations.some(r=>matches(r,t,slots)))));
  for(let i=0;i<f.clues.length;i++) assert.ok(rows.filter(t=>validFormula({...f,clues:f.clues.filter((_,j)=>i!==j)},t)).length>1);
  // The conditionals constrain other branches; neither premise is mandatory in the answer.
  assert.ok(!f.slots[0].cards.find(c=>c.id===f.answer.powder).tags.includes('Растительное'));
  assert.ok(!f.slots[2].cards.find(c=>c.id===f.answer.essence).tags.includes('Животное'));
  const s=createState(f);
  for(const [a,b,x,y] of [['fluid','essence','f3','e1'],['fluid','essence','f1','e1'],['powder','fluid','p2','f1'],['fluid','essence','f1','e2'],['powder','fluid','p2','f2']]) {
    s.selected={[a]:x,[b]:y}; act(f,s,{type:'pairTest',slots:[a,b]});
  }
  assert.deepEqual(s.history.map(h=>h.stable),[false,false,true,false,true]);
  assert.equal(s.research,0); assert.equal(s.science,1);
  assert.deepEqual(possible.filter(t=>s.knownRelations.every(r=>r.stable||!r.slots.every(id=>r.tuple[id]===t[id]))),[f.answer]);
  assert.ok(adjacent.every(slots=>s.knownRelations.some(r=>r.stable&&matches(r,f.answer,slots))));
  s.selected={...f.answer}; act(f,s,{type:'submit'}); assert.equal(s.status,'solved');
});

test('journal pair selection replaces all slots atomically, accepts earned negatives and preserves resources/history', () => {
  const s = createState(harbor); s.selected={...harbor.answer}; s.notes='keep'; s.marks.p3=true;
  const before=structuredClone(s);
  const prior=harbor.knownRelations[0];
  act(harbor,s,{type:'selectPair',slots:prior.slots,tuple:prior.tuple});
  assert.deepEqual(s,{...before,selected:prior.tuple});
  act(harbor,s,{type:'selectPair',slots:prior.slots,tuple:prior.tuple});
  assert.deepEqual(s.selected,prior.tuple);
  const invalid=structuredClone(s);
  assert.throws(()=>act(harbor,s,{type:'selectPair',slots:['powder','essence'],tuple:{powder:'p1',essence:'e1'}}));
  assert.throws(()=>act(harbor,s,{type:'selectPair',slots:['powder','fluid'],tuple:{powder:'p2',fluid:'f2'}}));
  assert.throws(()=>act(harbor,s,{type:'selectPair',slots:['fluid','essence']}));
  assert.deepEqual(s,invalid);
  s.selected={powder:'p2',fluid:'f2',essence:'e1'};
  act(harbor,s,{type:'pairTest',slots:['fluid','essence']});
  const earned=structuredClone(s);
  act(harbor,s,{type:'selectPair',slots:['fluid','essence'],tuple:{fluid:'f2',essence:'e1'}});
  assert.deepEqual(s,{...earned,selected:{fluid:'f2',essence:'e1'}});
  s.status='solved';
  act(harbor,s,{type:'selectPair',slots:prior.slots,tuple:prior.tuple});
  assert.equal(s.status,'solved'); assert.equal(s.research,3); assert.equal(s.science,1); assert.equal(s.history.length,1);
  assert.throws(()=>act(fixture,createState(fixture),{type:'selectPair',slots:['powder','fluid'],tuple:{powder:'p1',fluid:'f1'}}));
});

test('seventh fixture starts with stable bridges, needs every clue and supports complete branch rejection within budget', () => {
  const f = JSON.parse(readFileSync(new URL('./fixtures/lantern-07.json', import.meta.url)));
  validate(f);
  const rows = candidates(f);
  const possible = rows.filter(t => f.clues.every(c => satisfies(f,t,c)));
  assert.equal(possible.length,9);
  assert.ok(f.knownRelations.every(r => r.stable));
  const adjacent = [['powder','fluid'],['fluid','essence']];
  const matches = (r,t,slots) => r.slots.every((id,i) => id === slots[i]) && slots.every(id => r.tuple[id] === t[id]);
  assert.ok(possible.every(t => !adjacent.every(slots => f.knownRelations.some(r => matches(r,t,slots)))));
  for (let omitted=0; omitted<f.clues.length; omitted++) {
    assert.ok(rows.filter(t => validFormula({...f,clues:f.clues.filter((_,i) => i!==omitted)},t)).length>1);
  }
  const s = createState(f);
  const investigations = [
    ['fluid','essence','f2','e1'], ['fluid','essence','f2','e3'],
    ['powder','fluid','p1','f3'], ['powder','fluid','p2','f2'],
    ['fluid','essence','f1','e3'], ['powder','fluid','p3','f2'],
    ['powder','fluid','p3','f3'], ['powder','fluid','p2','f3']
  ];
  for (const [a,b,x,y] of investigations) {
    s.selected = {[a]:x,[b]:y}; act(f,s,{type:'pairTest',slots:[a,b]});
  }
  assert.equal(s.research,0); assert.equal(s.science,1);
  assert.deepEqual(s.history.map(h=>h.stable),[false,false,false,false,false,false,false,true]);
  assert.equal(s.knownRelations.length,11);
  assert.deepEqual(possible.filter(t => s.knownRelations.every(r => r.stable || !r.slots.every(id => r.tuple[id] === t[id]))),[f.answer]);
  assert.ok(adjacent.every(slots => s.knownRelations.some(r => r.stable && matches(r,f.answer,slots))));
  assert.ok(!JSON.stringify(publicView(f,s)).includes('stablePairs'));
  s.selected={...f.answer}; act(f,s,{type:'submit'}); assert.equal(s.status,'solved');
});

test('repeat-click selection clears only its slot, remains free and requires reselecting for submission', () => {
  const s = createState(harbor); s.selected={...harbor.answer};
  act(harbor,s,{type:'toggleSelect',slot:'essence',card:'e2'});
  assert.deepEqual(s.selected,{powder:'p2',fluid:'f2'});
  assert.throws(() => act(harbor,s,{type:'submit'}));
  assert.equal(s.science,1); assert.equal(s.research,4); assert.equal(s.history.length,0);
  act(harbor,s,{type:'toggleSelect',slot:'essence',card:'e2'});
  assert.deepEqual(s.selected,harbor.answer);
  act(harbor,s,{type:'toggleSelect',slot:'essence',card:'e1'});
  assert.equal(s.selected.essence,'e1');
  assert.throws(() => act(harbor,s,{type:'toggleSelect',slot:'essence',card:'p1'}));
  assert.equal(s.selected.essence,'e1');
  const two = createState(fixture);
  act(fixture,two,{type:'toggleSelect',slot:'powder',card:'p1'});
  act(fixture,two,{type:'toggleSelect',slot:'powder',card:'p1'});
  assert.deepEqual(two.selected,{}); assert.equal(two.science,1);
});

test('three-slot model requires clues and both adjacent edges, with four initial hypotheses', () => {
  validate(harbor);
  const all = candidates(harbor);
  assert.equal(all.length,27);
  assert.equal(all.filter(t => validFormula(harbor,t)).length,1);
  const possible = all.filter(t => harbor.clues.every(c => satisfies(harbor,t,c)) &&
    harbor.knownRelations.every(r => r.stable || !r.slots.every(id => r.tuple[id] === t[id])));
  assert.equal(possible.length,4);
  assert.ok(possible.every(t => ![['powder','fluid'],['fluid','essence']].every(slots =>
    harbor.knownRelations.some(r => r.stable && slots.every(id => r.tuple[id] === t[id])))));
  for (let omitted=0; omitted<harbor.clues.length; omitted++) {
    const f = {...harbor,clues:harbor.clues.filter((_,i) => i!==omitted)};
    assert.ok(all.filter(t => validFormula(f,t)).length > 1);
  }
  const broken = structuredClone(harbor); broken.knownRelations[0].stable = false;
  assert.throws(() => validate(broken));
  const nonAdjacent = structuredClone(harbor); nonAdjacent.compatibility.stablePairs.push('p1:e1');
  assert.throws(() => validate(nonAdjacent));
});

test('pair research charges only unknown adjacent pairs, preserves Science and never solves automatically', () => {
  const s = createState(harbor);
  assert.throws(() => act(harbor,s,{type:'pairTest',slots:['powder','essence']}));
  assert.throws(() => act(harbor,s,{type:'pairTest',slots:['powder','fluid']}));
  assert.equal(s.research,4);
  s.selected={...harbor.answer};
  act(harbor,s,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(s.research,3); assert.equal(s.science,1); assert.equal(s.status,'playing');
  assert.equal(s.history[0].stable,true);
  act(harbor,s,{type:'pairTest',slots:['powder','fluid']});
  assert.equal(s.research,3); assert.equal(s.history.length,1);
  s.selected.essence='e1'; act(harbor,s,{type:'pairTest',slots:['fluid','essence']});
  assert.equal(s.history[1].stable,false); assert.equal(s.research,2);
  s.research=0;
  act(harbor,s,{type:'pairTest',slots:['powder','fluid']}); // known pair stays free
  s.selected={powder:'p3',fluid:'f3',essence:'e1'};
  assert.throws(() => act(harbor,s,{type:'pairTest',slots:['powder','fluid']}));
  s.selected={powder:'p2',fluid:'f2'};
  assert.throws(() => act(harbor,s,{type:'submit'})); assert.equal(s.science,1);
  s.selected={...harbor.answer}; act(harbor,s,{type:'submit'});
  assert.equal(s.status,'solved'); assert.equal(s.science,0);
  assert.throws(() => act(harbor,s,{type:'pairTest',slots:['powder','fluid']}));
});

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
async function serve(t, debug = false, fixturePath) {
  const server = createLab({debug,...(fixturePath ? {fixturePath} : {})});
  await new Promise(r => server.listen(0,'127.0.0.1',r));
  t.after(() => new Promise(r => {server.close(r); server.closeAllConnections();}));
  return `http://127.0.0.1:${server.address().port}`;
}
test('three-slot HTTP exposes only prior and earned observations; third slot and final verification work', async t => {
  const base = await serve(t,false,new URL('./fixtures/harbor-06.json',import.meta.url));
  const first = await fetch(base+'/api/state'); const cookie = first.headers.get('set-cookie').split(';')[0];
  const initial = await first.json();
  assert.equal(initial.slots.length,3); assert.equal(initial.compatibility,undefined);
  assert.equal(initial.answer,undefined); assert.equal(initial.state.knownRelations.length,5);
  const headers={Cookie:cookie,'Content-Type':'application/json'};
  const action = body => fetch(base+'/api/action',{method:'POST',headers,body:JSON.stringify(body)});
  assert.equal((await action({type:'pairTest',slots:['powder','essence']})).status,400);
  for (const slot of harbor.slots) await action({type:'select',slot:slot.id,card:harbor.answer[slot.id]});
  await action({type:'toggleSelect',slot:'essence',card:harbor.answer.essence});
  assert.equal((await action({type:'submit'})).status,400);
  await action({type:'toggleSelect',slot:'essence',card:harbor.answer.essence});
  const observed = await (await action({type:'pairTest',slots:['powder','fluid']})).json();
  assert.equal(observed.state.research,3); assert.equal(observed.state.science,1);
  assert.equal(observed.state.knownRelations.length,6); assert.equal(observed.state.status,'playing');
  const refreshed = await (await fetch(base+'/api/state',{headers})).json();
  assert.deepEqual(refreshed.state,observed.state);
  const solved = await (await action({type:'submit'})).json();
  assert.equal(solved.state.status,'solved'); assert.equal(solved.state.history.length,2);
  assert.equal((await fetch(base+'/api/debug')).status,404);
});
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
