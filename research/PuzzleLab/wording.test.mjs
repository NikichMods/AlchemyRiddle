// SPDX-License-Identifier: MPL-2.0
import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,mkdtempSync,rmSync,writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {authorWording,asides,eligibleTemplates,renderTemplate,validateWording} from './wording.mjs';
import {authorFile} from './author-wording.mjs';
import {createLab} from './server.mjs';
import {legacyClueText,publicView,createState,candidates,validFormula,validate} from './rules.mjs';
const f=JSON.parse(readFileSync(new URL('./fixtures/depth-10.json',import.meta.url)));
const t=(slot,tag='А')=>({slot,tag});
const literal=(slot,count)=>({kind:'exactly',count,terms:[t(slot)]});

test('all fourteen templates cover their admitted shapes and slot grammar',()=>{
  const models=[literal('powder',1),literal('powder',0),
    {kind:'exactly',count:1,terms:[t('powder'),t('essence','Б')]},
    {kind:'implies',if:t('powder'),then:t('essence','Б')},
    {kind:'notTogether',left:t('fluid'),right:t('essence','Б')},
    {kind:'exactly',count:2,terms:f.slots.map(s=>t(s.id))},{kind:'sharedTag'}];
  const ids=new Set();
  for(const c of models) for(const id of eligibleTemplates(f,c,{authoring:true})) {
    ids.add(id);assert.ok(renderTemplate(f,c,id,legacyClueText).endsWith('.'));
  }
  assert.equal(ids.size,14);
  for(const s of f.slots) {
    const c=literal(s.id,0),noun=s.name.toLowerCase();
    assert.match(renderTemplate(f,c,'lacks-note-v1',legacyClueText),new RegExp(`нуж${s.id==='powder'?'ен':'на'} ${noun}`));
    const implication={kind:'implies',if:t('essence'),then:t(s.id)};
    assert.ok(renderTemplate(f,implication,'implies-plain-v1',legacyClueText).includes(`${noun} долж${s.id==='powder'?'ен':'на'}`));
  }
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

test('all thirty unique optional asides persist independently of clause and answer',()=>{
  assert.equal(Object.keys(asides).length,30);assert.equal(new Set(Object.values(asides)).size,30);
  for(const [asideId,asideText] of Object.entries(asides)) {
    const next=authorWording(f,legacyClueText,{asideId});validate(next);
    assert.equal(publicView(next,createState(next)).clueAsides[0],asideText);
    assert.deepEqual(next.wording,authorWording({...f,answer:{}},legacyClueText,{asideId}).wording);
  }
});

test('authoring is deterministic, answer-independent and retains all formula outcomes',()=>{
  const next=authorWording(f,legacyClueText,{asideId:'note-label-v1'});
  validate(next);
  assert.deepEqual(next,JSON.parse(JSON.stringify(next)));
  assert.deepEqual(next.wording,authorWording({...f,answer:{},compatibility:{}},legacyClueText,{asideId:'note-label-v1'}).wording);
  for(const row of candidates(f))assert.equal(validFormula(f,row),validFormula(next,row));
  assert.deepEqual(f,JSON.parse(readFileSync(new URL('./fixtures/depth-10.json',import.meta.url))));
  const view=publicView(next,createState(next));
  assert.deepEqual(view.clues,next.wording.entries.map(e=>e.text));
  assert.equal(view.clueAsides.filter(Boolean).length,1);
  assert.ok(!('wording' in view)&&!('answer' in view));
  const repeated={...f,clues:[literal('powder',1),literal('fluid',1),literal('essence',1)]};
  assert.deepEqual(authorWording(repeated,legacyClueText).wording.entries.map(e=>e.templateId),['has-plain-v1','has-note-v1','has-plain-v1']);
});

test('legacy fixtures remain opt-in and corrupt frozen records fail validation',()=>{
  assert.ok(!('clueAsides' in publicView(f,createState(f))));
  assert.deepEqual(publicView(f,createState(f)).clues,f.clues.map(c=>legacyClueText(f,c)));
  const base=authorWording(f,legacyClueText,{asideId:'note-label-v1'});
  for(const mutate of [x=>x.wording.version=2,x=>x.wording.entries.pop(),
    x=>x.wording.entries[0].text+=' extra',x=>x.wording.entries[0].templateId='unknown',
    x=>x.wording.entries[0].asideId='unknown',x=>x.wording.entries[0].asideText='fake',
    x=>Object.assign(x.wording.entries[1],{asideId:'note-label-v1',asideText:x.wording.entries[0].asideText})]) {
    const altered=structuredClone(base);mutate(altered);assert.throws(()=>validate(altered));
  }
  assert.throws(()=>authorWording(base,legacyClueText));
  assert.throws(()=>authorWording(f,legacyClueText,{asideId:'unknown'}));
  assert.throws(()=>authorWording(f,legacyClueText,{asideId:'note-label-v1',asideAt:-1}));
  validateWording(f,legacyClueText);
});

test('file authoring persists reloadable wording and refuses all source/output overwrites',()=>{
  const dir=mkdtempSync(join(tmpdir(),'alchemy-wording-'));
  try {
    const input=join(dir,'source.json'),output=join(dir,'new.json');
    const source=JSON.stringify(f);writeFileSync(input,source);
    assert.equal(authorFile(input,output,{asideId:'note-underline-v1'}),f.clues.length);
    const loaded=JSON.parse(readFileSync(output,'utf8'));validate(loaded);
    assert.deepEqual(publicView(loaded,createState(loaded)),publicView(authorWording(f,legacyClueText,{asideId:'note-underline-v1'}),createState(f)));
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
    const next=authorWording(f,legacyClueText,{asideId:'note-underline-v1'});
    writeFileSync(fixturePath,JSON.stringify(next));
    const start=async()=>{
      server=createLab({fixturePath,stateDirectory});
      await new Promise(r=>server.listen(0,'127.0.0.1',r));
      return `http://127.0.0.1:${server.address().port}/api/state`;
    };
    const first=await fetch(await start()),cookie=first.headers.get('set-cookie').split(';')[0];
    const before=await first.json();
    assert.deepEqual(before.clues,next.wording.entries.map(e=>e.text));
    assert.equal(before.clueAsides[0],'Подчеркнуть. Лучше дважды.');
    assert.ok(!('answer' in before)&&!('compatibility' in before));
    await new Promise(r=>server.close(r));server=undefined;
    const after=await (await fetch(await start(),{headers:{cookie}})).json();
    assert.deepEqual(after,before);
  } finally {
    if(server)await new Promise(r=>server.close(r));
    rmSync(dir,{recursive:true,force:true});
  }
});
