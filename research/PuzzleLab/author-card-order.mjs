// SPDX-License-Identifier: MPL-2.0
import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {validate} from './rules.mjs';
import {prepareCardOrder} from './card-order.mjs';
const [input,output,newId,seedText]=process.argv.slice(2);
if(!input||!output||!newId||resolve(input)===resolve(output))throw new Error('Usage: node author-card-order.mjs private-input.json private-new-output.json NEW-ID [SEED]');
const f=JSON.parse(await readFile(input,'utf8'));validate(f);
if(newId===f.id)throw new Error('A reordered fixture requires a fresh immutable identity');
const {fixture,audit}=prepareCardOrder(f,{seed:seedText===undefined?20261010:Number(seedText)});fixture.id=newId;validate(fixture);
await writeFile(output,JSON.stringify(fixture,null,2)+'\n',{flag:'wx'});
// Audit is a facilitator artifact: keep next to the private model, outside Git.
await writeFile(output+'.order-audit.json',JSON.stringify(audit,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({prepared:true,candidates:audit.candidates,uniformExpectedPenalty:audit.uniformExpectedPenalty,weightedExpectedPenalty:audit.weightedExpectedPenalty}));
