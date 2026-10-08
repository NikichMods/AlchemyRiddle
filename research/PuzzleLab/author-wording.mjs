// SPDX-License-Identifier: MPL-2.0
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {authorWording} from './wording.mjs';
import {validate,legacyClueText} from './rules.mjs';
export function authorFile(input,output,options={}) {
  if(resolve(input)===resolve(output)) throw new Error('Author a new case file; never overwrite the source');
  const f=JSON.parse(readFileSync(input,'utf8'));validate(f);
  const next=authorWording(f,legacyClueText,options);validate(next);
  writeFileSync(output,JSON.stringify(next,null,2)+'\n',{flag:'wx'});
  return next.wording.entries.length;
}
if(process.argv[1] && resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const [input,output,...args]=process.argv.slice(2);
  try {
    if(!input || !output || args.some(a=>!a.startsWith('--aside=')&&!a.startsWith('--aside-at=')&&!a.startsWith('--variant-offset=')))
      throw new Error('Usage: author-wording.mjs INPUT NEW_OUTPUT [--aside=ID --aside-at=ZERO_BASED_INDEX] [--variant-offset=N]');
    const asideId=args.find(a=>a.startsWith('--aside='))?.slice(8);
    const at=args.find(a=>a.startsWith('--aside-at='));
    if(at && asideId===undefined) throw new Error('--aside-at requires --aside');
    const offset=args.find(a=>a.startsWith('--variant-offset='));
    const count=authorFile(input,output,{asideId,...(at?{asideAt:Number(at.slice(11))}:{}),...(offset?{variantOffset:Number(offset.slice(17))}:{})});
    console.log(`Persisted ${count} clue wording records. No answer data printed.`);
  } catch(e) {console.error(e.message);process.exitCode=1;}
}
