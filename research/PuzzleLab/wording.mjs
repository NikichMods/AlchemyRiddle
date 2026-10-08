// SPDX-License-Identifier: MPL-2.0
// Versioned authoring templates. Never change v1 text under an existing ID.
import {asides,authoringAsides} from './keeper-asides.mjs';
export {asides,authoringAsides};
const forms = {
  Порошок: {nom:'порошок',gen:'порошка',acc:'порошок',ins:'порошком',need:'нужен',must:'должен'},
  Жидкость: {nom:'жидкость',gen:'жидкости',acc:'жидкость',ins:'жидкостью',need:'нужна',must:'должна'},
  Эссенция: {nom:'эссенция',gen:'эссенции',acc:'эссенцию',ins:'эссенцией',need:'нужна',must:'должна'}
};
const capital = s => s[0].toUpperCase()+s.slice(1);
function family(f,c) {
  if (!f.slots.every(s=>Object.hasOwn(forms,s.name))) return 'fallback';
  if (c.kind==='sharedTag') return 'shared';
  if (c.kind==='implies') return 'implies';
  if (c.kind==='notTogether') return 'forbids';
  if (c.kind!=='exactly') return 'fallback';
  if(c.terms.length===1) return c.count===0?'lacks':c.count===1?'has':'fallback';
  // Two assertions about the very same term are not two independent conditions.
  if(c.terms.length===2 && c.count===1 &&
    (c.terms[0].slot!==c.terms[1].slot || c.terms[0].tag!==c.terms[1].tag)) return 'xor';
  if(f.slots.length===3 && c.count===2 && c.terms.length===3 &&
    new Set(c.terms.map(t=>t.slot)).size===3 &&
    f.slots.every(s=>c.terms.some(t=>t.slot===s.id)) &&
    new Set(c.terms.map(t=>t.tag)).size===1) return 'count-two';
  return 'fallback';
}
export function eligibleTemplates(f,c,{authoring=false}={}) {
  const type=family(f,c);
  if(type==='fallback') return authoring?['plain-fallback-v2']:['plain-fallback-v2','plain-fallback-v1'];
  if(type==='xor') {
    const current=['xor-plain-v2','xor-note-v1','xor-either-v1','xor-one-v1'];
    return authoring?current:[...current,'xor-plain-v1'];
  }
  return [`${type}-plain-v1`,`${type}-note-v1`,`${type}-choice-v1`,`${type}-scope-v1`];
}
export function renderTemplate(f,c,id,fallback) {
  if(!eligibleTemplates(f,c).includes(id)) throw new Error('Ineligible wording template');
  if(id==='plain-fallback-v1') return fallback(f,c);
  if(id==='plain-fallback-v2') {
    if(c.kind!=='exactly') return fallback(f,c);
    const term=t=>`${f.slots.find(s=>s.id===t.slot).name.toLowerCase()} имеет свойство «${t.tag}»`;
    if(c.terms.length===1) return fallback(f,c);
    if(c.count===0) return c.terms.map(t=>`${f.slots.find(s=>s.id===t.slot).name} не имеет свойства «${t.tag}».`).join(' ');
    return `Должно выполняться ровно ${c.count} из этих условий: ${c.terms.map(term).join(', ')}.`;
  }
  const note=id.endsWith('-note-v1');
  const noun=t=>forms[f.slots.find(s=>s.id===t.slot).name];
  const assertion=t=>`${noun(t).nom} имеет свойство «${t.tag}»`;
  const part=(t,gram='nom')=>`${noun(t)[gram]} со свойством «${t.tag}»`;
  if(id==='has-choice-v1') {const t=c.terms[0];return `Для этой смеси ${noun(t).need} ${part(t)}.`;}
  if(id==='has-scope-v1') {const t=c.terms[0];return `В состав ${noun(t).must} входить ${part(t)}.`;}
  if(id==='lacks-choice-v1') {const t=c.terms[0];return `Для этого состава выбирайте ${noun(t).acc} без свойства «${t.tag}».`;}
  if(id==='lacks-scope-v1') {const t=c.terms[0];return `В этой смеси у ${noun(t).gen} не должно быть свойства «${t.tag}».`;}
  if(id==='implies-choice-v1') return `Для этой смеси ${part(c.if)} можно взять только с ${part(c.then,'ins')}.`;
  if(id==='implies-scope-v1') return `Если в смеси используется ${part(c.if)}, у ${noun(c.then).gen} должно быть свойство «${c.then.tag}».`;
  if(id==='forbids-choice-v1') return `Если для этой смеси берёте ${part(c.left,'acc')}, выбирайте ${noun(c.right).acc} без свойства «${c.right.tag}».`;
  if(id==='forbids-scope-v1') return `В этой смеси ${part(c.left)} и ${part(c.right)} не должны встречаться вместе.`;
  if(id==='count-two-choice-v1') return `Два выбранных компонента должны иметь свойство «${c.terms[0].tag}», а один — не иметь его.`;
  if(id==='count-two-scope-v1') return `В этой тройке свойство «${c.terms[0].tag}» есть ровно у двух компонентов.`;
  if(id==='shared-choice-v1') return 'Все выбранные компоненты должны иметь хотя бы одно общее свойство.';
  if(id==='shared-scope-v1') return 'Среди свойств выбранных компонентов хотя бы одно должно встречаться у каждого из них.';
  if(id==='xor-either-v1') return `Для этой смеси нужно одно из двух: ${assertion(c.terms[0])} или ${assertion(c.terms[1])}. Одновременно оба условия выполняться не должны.`;
  if(id==='xor-one-v1') return `Из этих двух условий должно выполняться только одно: ${assertion(c.terms[0])} или ${assertion(c.terms[1])}.`;
  switch(family(f,c)) {
    case 'has': {const t=c.terms[0];return note?`У ${noun(t).gen} в этой смеси должно быть свойство «${t.tag}».`:`${capital(assertion(t))}.`;}
    case 'lacks': {const t=c.terms[0];return note?`Для этой смеси ${noun(t).need} ${noun(t).nom} без свойства «${t.tag}».`:`${capital(noun(t).nom)} не имеет свойства «${t.tag}».`;}
    case 'xor': return note?`В этой смеси либо ${assertion(c.terms[0])}, либо ${assertion(c.terms[1])} — но не оба условия одновременно.`:
      id==='xor-plain-v1'?`Выполняется ровно одно из двух условий: ${c.terms.map(assertion).join('; ')}.`:
      `Выполняется ровно одно из двух условий: либо ${assertion(c.terms[0])}, либо ${assertion(c.terms[1])}.`;
    case 'implies': return note?`При выборе ${part(c.if,'gen')} ${noun(c.then).need} ${part(c.then)}.`:`Если ${assertion(c.if)}, ${noun(c.then).nom} ${noun(c.then).must} иметь свойство «${c.then.tag}».`;
    case 'forbids': return note?`В этом составе сочетание ${part(c.left,'gen')} и ${part(c.right,'gen')} не допускается.`:`Для этой смеси нельзя одновременно взять ${part(c.left,'acc')} и ${part(c.right,'acc')}.`;
    case 'count-two': return note?`Свойство «${c.terms[0].tag}» должно быть у двух выбранных компонентов, а у третьего его быть не должно.`:`Среди трёх выбранных компонентов ровно два имеют свойство «${c.terms[0].tag}».`;
    case 'shared': return note?'Нужно хотя бы одно свойство, которое есть у каждого выбранного компонента.':'У всех выбранных компонентов есть хотя бы одно общее свойство.';
  }
}
export function validateWording(f,fallback) {
  if(f.wording===undefined) return;
  const w=f.wording;
  if(!w || w.version!==1 || !Array.isArray(w.entries) || w.entries.length!==f.clues.length)
    throw new Error('Invalid wording record');
  let asideCount=0;
  for(const [i,e] of w.entries.entries()) {
    if(!e || typeof e.templateId!=='string' ||
      (e.asideId!==undefined && !Object.hasOwn(asides,e.asideId))) throw new Error('Invalid wording entry');
    const text=renderTemplate(f,f.clues[i],e.templateId,fallback);
    if(e.text!==text || e.asideText!==(e.asideId===undefined?undefined:asides[e.asideId]))
      throw new Error('Wording text does not match its versioned template');
    if(e.asideId!==undefined) asideCount++;
  }
  if(asideCount>1) throw new Error('Only one optional Keeper aside per case');
}
export function authorWording(f,fallback,{asideId,asideAt=0,variantOffset=0}={}) {
  if(f.wording!==undefined) throw new Error('Case wording already frozen');
  if(!Number.isSafeInteger(variantOffset) || variantOffset<0) throw new Error('Invalid wording variant offset');
  if(asideId!==undefined && (!Object.hasOwn(authoringAsides,asideId) || !Number.isInteger(asideAt) || asideAt<0 || asideAt>=f.clues.length))
    throw new Error('Invalid authoring aside');
  const occurrences=new Map();
  const entries=f.clues.map(c=>{
    const ids=eligibleTemplates(f,c,{authoring:true}), key=ids[0], n=occurrences.get(key)??0;
    occurrences.set(key,n+1);
    const templateId=ids[(n+variantOffset)%ids.length];
    return {templateId,text:renderTemplate(f,c,templateId,fallback)};
  });
  if(asideId!==undefined) Object.assign(entries[asideAt],{asideId,asideText:asides[asideId]});
  const next={...f,wording:{version:1,entries}};
  validateWording(next,fallback);
  return next;
}
