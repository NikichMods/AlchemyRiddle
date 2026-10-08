// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,mkdtempSync,rmSync,writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {authorWording,asides,authoringAsides,eligibleTemplates,renderTemplate,validateWording} from './wording.mjs';
import {clueAsideContexts,clueAsideFits,eventAsides} from './keeper-asides.mjs';
import {authorFile} from './author-wording.mjs';
import {createLab} from './server.mjs';
import {legacyClueText,publicView,createState,candidates,validFormula,validate} from './rules.mjs';
const f=JSON.parse(readFileSync(new URL('./fixtures/depth-10.json',import.meta.url)));
const t=(slot,tag='А')=>({slot,tag});
const literal=(slot,count)=>({kind:'exactly',count,terms:[t(slot)]});
// Adds a true clue without changing the original fixture's unique solution.
const contextModel={...f,clues:[...f.clues,{kind:'exactly',count:1,terms:[t('essence','Орган')]}]};
const contextAt=f.clues.length;
const asideId='clue-has-organ-v1';

test('all twenty-eight active templates cover their admitted shapes and slot grammar',()=>{
  const models=[literal('powder',1),literal('powder',0),
    {kind:'exactly',count:1,terms:[t('powder'),t('essence','Б')]},
    {kind:'implies',if:t('powder'),then:t('essence','Б')},
    {kind:'notTogether',left:t('fluid'),right:t('essence','Б')},
    {kind:'exactly',count:2,terms:f.slots.map(s=>t(s.id))},{kind:'sharedTag'}];
  const ids=new Set();
  for(const c of models) for(const id of eligibleTemplates(f,c,{authoring:true})) {
    ids.add(id);assert.ok(renderTemplate(f,c,id,legacyClueText).endsWith('.'));
  }
  assert.equal(ids.size,28);
  for(const s of f.slots) {
    const c=literal(s.id,0),noun=s.name.toLowerCase();
    assert.match(renderTemplate(f,c,'lacks-note-v1',legacyClueText),new RegExp(`нуж${s.id==='powder'?'ен':'на'} ${noun}`));
    const implication={kind:'implies',if:t('essence'),then:t(s.id)};
    assert.ok(renderTemplate(f,implication,'implies-plain-v1',legacyClueText).includes(`${noun} долж${s.id==='powder'?'ен':'на'}`));
    assert.ok(renderTemplate(f,literal(s.id,1),'has-scope-v1',legacyClueText).includes(`долж${s.id==='powder'?'ен':'на'} входить ${noun}`));
    assert.ok(renderTemplate(f,implication,'implies-choice-v1',legacyClueText).includes(`с ${s.id==='powder'?'порошком':s.id==='fluid'?'жидкостью':'эссенцией'} со свойством`));
    for(const c of [literal(s.id,0),literal(s.id,1),implication]) {
      const texts=new Set();
      for(let variantOffset=0;variantOffset<4;variantOffset++) {
        const next=authorWording({...f,clues:[c]},legacyClueText,{variantOffset});
        validateWording(next,legacyClueText);texts.add(next.wording.entries[0].text);
      }
      assert.equal(texts.size,4);
    }
  }
  for(const c of models) assert.equal(new Set(eligibleTemplates(f,c,{authoring:true}).map(id=>renderTemplate(f,c,id,legacyClueText))).size,4);
  assert.equal(renderTemplate(f,models[4],'forbids-plain-v1',legacyClueText),
    'Для этой смеси нельзя одновременно взять жидкость со свойством «А» и эссенцию со свойством «Б».');
  assert.equal(renderTemplate(f,models[4],'forbids-note-v1',legacyClueText),
    'В этом составе сочетание жидкости со свойством «А» и эссенции со свойством «Б» не допускается.');
});

test('out-of-scope counts, duplicate terms and unfamiliar slot labels use plain fallback',()=>{
  const count={kind:'exactly',count:2,terms:f.slots.map(s=>t(s.id))};
  for(const c of [{...count,count:0},{...count,count:1},
    {...count,terms:[t('powder'),t('fluid'),t('essence','Б')]},
    {...count,terms:[t('powder'),t('powder'),t('fluid')]},
    {kind:'exactly',count:1,terms:[t('powder'),t('powder')]}]) {
    assert.deepEqual(eligibleTemplates(f,c,{authoring:true}),['plain-fallback-v2']);
    assert.equal(renderTemplate(f,c,'plain-fallback-v1',legacyClueText),legacyClueText(f,c));
    assert.ok(!renderTemplate(f,c,'plain-fallback-v2',legacyClueText).includes(';'));
    assert.throws(()=>renderTemplate(f,c,'count-two-note-v1',legacyClueText));
  }
  assert.deepEqual(eligibleTemplates({...f,slots:f.slots.slice(0,2)}, {...count,terms:count.terms.slice(0,2)},{authoring:true}),['plain-fallback-v2']);
  assert.deepEqual(eligibleTemplates({...f,slots:f.slots.map(s=>({...s,name:'Other'}))},literal('powder',1),{authoring:true}),['plain-fallback-v2']);
});

test('new XOR wording uses either/or while frozen v1 wording remains valid',()=>{
  const c={kind:'exactly',count:1,terms:[t('powder'),t('fluid')]};
  const model={...f,clues:[c]};
  const current=authorWording(model,legacyClueText);
  assert.equal(current.wording.entries[0].templateId,'xor-plain-v2');
  assert.equal(current.wording.entries[0].text,'Выполняется ровно одно из двух условий: либо порошок имеет свойство «А», либо жидкость имеет свойство «А».');
  const old={...model,wording:{version:1,entries:[{templateId:'xor-plain-v1',text:'Выполняется ровно одно из двух условий: порошок имеет свойство «А»; жидкость имеет свойство «А».'}]}};
  validateWording(old,legacyClueText);
  assert.deepEqual(publicView(old,createState(old)).clues,[old.wording.entries[0].text]);
});

test('thirteen active clue notes are unique, context-gated, and answer-independent',()=>{
  assert.equal(Object.keys(authoringAsides).length,13);
  assert.equal(new Set(Object.values(authoringAsides)).size,13);
  for(const id of Object.keys(authoringAsides)) {
    const rule=clueAsideContexts[id];
    let c;
    const pair=()=>structuredClone(rule.terms);
    switch(rule.kind) {
      case 'xor':c={kind:'exactly',count:1,terms:pair()};break;
      case 'count-two':c={kind:'exactly',count:2,terms:f.slots.map(s=>t(s.id,rule.tag))};break;
      case 'has':case 'lacks':c={kind:'exactly',count:rule.kind==='has'?1:0,terms:[rule.term]};break;
      case 'implies':c={kind:'implies',if:rule.if,then:rule.then};break;
      case 'forbids':c={kind:'notTogether',left:rule.terms[0],right:rule.terms[1]};break;
      case 'shared':c={kind:'sharedTag'};break;
      default:assert.fail('Unknown context');
    }
    const model={...f,clues:[c]};
    assert.equal(clueAsideFits(model,c,id),true);
    assert.equal(clueAsideFits(f,f.clues[0],id),false);
    const next=authorWording(model,legacyClueText,{asideId:id});
    validateWording(next,legacyClueText);
    assert.equal(publicView(next,createState(next)).clueAsides[0],authoringAsides[id]);
    assert.deepEqual(next.wording,authorWording({...model,answer:{}},legacyClueText,{asideId:id}).wording);
    assert.throws(()=>authorWording(f,legacyClueText,{asideId:id}));
    if(rule.kind==='xor') {
      assert.equal(clueAsideFits(model,{...c,terms:pair().reverse()},id),true);
      assert.equal(clueAsideFits(model,{...c,count:2},id),false);
    }
    if(rule.kind==='forbids')assert.equal(clueAsideFits(model,{...c,left:rule.terms[1],right:rule.terms[0]},id),true);
  }
});

test('nine approved event replies are stored but not exposed as clue notes',()=>{
  assert.equal(Object.keys(eventAsides).length,9);
  for(const e of Object.values(eventAsides)) {
    assert.ok(['pairTest','submit'].includes(e.trigger));
    assert.ok(e.text && typeof e.text==='string');
    if(e.trigger==='pairTest')assert.equal(typeof e.stable,'boolean');
    if(e.trigger==='submit')assert.equal(typeof e.success,'boolean');
  }
  assert.equal(new Set(Object.values(eventAsides).map(e=>e.text)).size,9);
  assert.ok(Object.values(eventAsides).every(e=>!Object.values(authoringAsides).includes(e.text)));
});

test('all retired asides remain valid in old records but are unavailable for new cases',()=>{
  for(const asideId of Object.keys(asides).filter(id=>!Object.hasOwn(authoringAsides,id))) {
    assert.throws(()=>authorWording(f,legacyClueText,{asideId}));
    const old=authorWording(f,legacyClueText);
    Object.assign(old.wording.entries[0],{asideId,asideText:asides[asideId]});validateWording(old,legacyClueText);
  }
});

test('variant offsets select four exact-one phrasings without depending on truth',()=>{
  const c={kind:'exactly',count:1,terms:[t('powder'),t('fluid')]},model={...f,clues:[c]};
  const texts=new Set();
  for(let variantOffset=0;variantOffset<4;variantOffset++) {
    const w=authorWording(model,legacyClueText,{variantOffset});texts.add(w.wording.entries[0].text);
    validateWording(w,legacyClueText);
    assert.deepEqual(w.wording,authorWording({...model,answer:{}},legacyClueText,{variantOffset}).wording);
  }
  assert.equal(texts.size,4);
  for(const variantOffset of [-1,0.5,NaN,Infinity]) assert.throws(()=>authorWording(model,legacyClueText,{variantOffset}));
});

test('authoring is deterministic, answer-independent and retains all formula outcomes',()=>{
  const next=authorWording(contextModel,legacyClueText,{asideId,asideAt:contextAt});
  validate(next);
  assert.deepEqual(next,JSON.parse(JSON.stringify(next)));
  assert.deepEqual(next.wording,authorWording({...contextModel,answer:{},compatibility:{}},legacyClueText,{asideId,asideAt:contextAt}).wording);
  for(const row of candidates(f))assert.equal(validFormula(f,row),validFormula(next,row));
  assert.deepEqual(f,JSON.parse(readFileSync(new URL('./fixtures/depth-10.json',import.meta.url))));
  const view=publicView(next,createState(next));
  assert.deepEqual(view.clues,next.wording.entries.map(e=>e.text));
  assert.equal(view.clueAsides.filter(Boolean).length,1);
  assert.ok(!('wording' in view)&&!('answer' in view));
  const repeated={...f,clues:[literal('powder',1),literal('fluid',1),literal('essence',1)]};
  assert.deepEqual(authorWording(repeated,legacyClueText).wording.entries.map(e=>e.templateId),['has-plain-v1','has-note-v1','has-choice-v1']);
});

test('legacy fixtures remain opt-in and corrupt frozen records fail validation',()=>{
  assert.ok(!('clueAsides' in publicView(f,createState(f))));
  assert.deepEqual(publicView(f,createState(f)).clues,f.clues.map(c=>legacyClueText(f,c)));
  const base=authorWording(contextModel,legacyClueText,{asideId,asideAt:contextAt});
  for(const mutate of [x=>x.wording.version=2,x=>x.wording.entries.pop(),
    x=>x.wording.entries[0].text+=' extra',x=>x.wording.entries[0].templateId='unknown',
    x=>x.wording.entries[0].asideId='unknown',x=>x.wording.entries[0].asideText='fake',
    x=>Object.assign(x.wording.entries[1],{asideId,asideText:x.wording.entries[contextAt].asideText})]) {
    const altered=structuredClone(base);mutate(altered);assert.throws(()=>validate(altered));
  }
  assert.throws(()=>authorWording(base,legacyClueText));
  assert.throws(()=>authorWording(f,legacyClueText,{asideId:'unknown'}));
  assert.throws(()=>authorWording(contextModel,legacyClueText,{asideId,asideAt:-1}));
  validateWording(f,legacyClueText);
});

test('file authoring persists reloadable wording and refuses all source/output overwrites',()=>{
  const dir=mkdtempSync(join(tmpdir(),'alchemy-wording-'));
  try {
    const input=join(dir,'source.json'),output=join(dir,'new.json');
    const source=JSON.stringify(contextModel);writeFileSync(input,source);
    assert.equal(authorFile(input,output,{asideId,asideAt:contextAt}),contextModel.clues.length);
    const loaded=JSON.parse(readFileSync(output,'utf8'));validate(loaded);
    assert.deepEqual(publicView(loaded,createState(loaded)),publicView(authorWording(contextModel,legacyClueText,{asideId,asideAt:contextAt}),createState(contextModel)));
    const bytes=readFileSync(output,'utf8');
    assert.throws(()=>authorFile(input,input));assert.throws(()=>authorFile(input,output));
    assert.throws(()=>authorFile(output,join(dir,'refrozen.json')));
    assert.equal(readFileSync(input,'utf8'),source);assert.equal(readFileSync(output,'utf8'),bytes);
  } finally {rmSync(dir,{recursive:true,force:true});}
});

test('HTTP serves frozen wording and optional aside unchanged after a server restart',async()=>{
  const dir=mkdtempSync(join(tmpdir(),'alchemy-wording-http-'));
  let server;
  try {
    const fixturePath=join(dir,'new.json'),stateDirectory=join(dir,'sessions');
    const next=authorWording(contextModel,legacyClueText,{asideId,asideAt:contextAt});
    writeFileSync(fixturePath,JSON.stringify(next));
    const start=async()=>{
      server=createLab({fixturePath,stateDirectory});
      await new Promise(r=>server.listen(0,'127.0.0.1',r));
      return `http://127.0.0.1:${server.address().port}/api/state`;
    };
    const first=await fetch(await start()),cookie=first.headers.get('set-cookie').split(';')[0];
    const before=await first.json();
    assert.deepEqual(before.clues,next.wording.entries.map(e=>e.text));
    assert.equal(before.clueAsides[contextAt],'„Орган“... Церковный или из морга?');
    assert.ok(!('answer' in before)&&!('compatibility' in before));
    await new Promise(r=>server.close(r));server=undefined;
    const after=await (await fetch(await start(),{headers:{cookie}})).json();
    assert.deepEqual(after,before);
  } finally {
    if(server)await new Promise(r=>server.close(r));
    rmSync(dir,{recursive:true,force:true});
  }
});
