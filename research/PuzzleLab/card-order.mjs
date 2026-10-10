// SPDX-License-Identifier: MPL-2.0
// Authoring only. Never import into public UI or reorder a running fixture.
import {candidates,satisfies} from './rules.mjs';
export const DEFAULT_ORDER_STRENGTH=2;
const same=(a,b,slots)=>slots.every(s=>a[s]===b[s]);
export function orderPenalty(f) {
  const ids=f.slots.map(s=>s.id);
  const live=candidates(f).filter(t=>f.clues.every(c=>satisfies(f,t,c)) &&
    (f.knownRelations??[]).every(r=>r.stable || !same(t,r.tuple,r.slots)));
  const lists=[live,...(f.knownRelations??[]).filter(r=>r.stable).map(r=>live.filter(t=>same(t,r.tuple,r.slots)))];
  // A stable observation allows a branch; it does not oblige the answer to use it.
  const positions=lists.map(rows=>({rows,index:rows.findIndex(t=>same(t,f.answer,ids))})).filter(x=>x.index>=0);
  if(!positions.length)throw new Error('Answer absent from public hypotheses');
  const ranks=positions.map(({rows,index})=>({count:rows.length,forward:index+1,reverse:rows.length-index}));
  return {penalty:ranks.reduce((n,r)=>n+(1/r.forward+1/r.reverse)/2,0)/ranks.length,ranks};
}
function rng(seed){let x=seed>>>0;return ()=>{x=(x+0x6D2B79F5)>>>0;let t=Math.imul(x^(x>>>15),1|x);t^=t+Math.imul(t^(t>>>7),61|t);return ((t^(t>>>14))>>>0)/4294967296;};}
function permutations(xs){if(xs.length<2)return [xs];return xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(rest=>[x,...rest]));}
export function prepareCardOrder(f,{seed=20261010,strength=DEFAULT_ORDER_STRENGTH,maxCandidates=128}={}) {
  if(!Number.isSafeInteger(seed)||!Number.isFinite(strength)||strength<0||strength>10 || !Number.isInteger(maxCandidates)||maxCandidates<1||maxCandidates>4096)throw new Error('Invalid order options');
  const random=rng(seed), shuffle=xs=>{const out=[...xs];for(let i=out.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[out[i],out[j]]=[out[j],out[i]];}return out;};
  let count=1;for(const s of f.slots)for(let i=2;i<=s.cards.length;i++)count*=i;
  let orders;
  if(count<=maxCandidates){orders=f.slots.reduce((rows,s)=>rows.flatMap(row=>permutations(s.cards).map(cards=>[...row,cards])),[[]]);}
  else {const unique=new Map();const add=order=>unique.set(JSON.stringify(order.map(xs=>xs.map(c=>c.id))),order);add(f.slots.map(s=>s.cards));for(let i=0;i<maxCandidates*20 && unique.size<maxCandidates;i++)add(f.slots.map(s=>shuffle(s.cards)));orders=[...unique.values()];}
  const pool=orders.map(order=>{const fixture={...f,slots:f.slots.map((s,i)=>({...s,cards:order[i]}))};return {fixture,...orderPenalty(fixture)};});
  const weights=pool.map(x=>Math.exp(-strength*x.penalty)), total=weights.reduce((a,b)=>a+b,0);
  let draw=random()*total,index=weights.length-1;for(let i=0;i<weights.length;i++){draw-=weights[i];if(draw<0){index=i;break;}}
  const selected=pool[index];
  return {fixture:structuredClone(selected.fixture),audit:{version:1,seed,strength,candidates:pool.length,exhaustive:count<=maxCandidates,selectedPenalty:selected.penalty,selectedRanks:selected.ranks,uniformExpectedPenalty:pool.reduce((n,x)=>n+x.penalty,0)/pool.length,weightedExpectedPenalty:pool.reduce((n,x,i)=>n+x.penalty*weights[i],0)/total}};
}
