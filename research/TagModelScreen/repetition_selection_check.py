"""Compare accepted soft repetition preference on the frozen 209-package pool."""
import argparse
import json
import random
import statistics
from pathlib import Path
import generator_route_ranking as ranking


def run(original, gap, output):
    a=json.loads(original.read_text(encoding='utf-8'))
    b=json.loads(gap.read_text(encoding='utf-8'))
    options=[rows for rows in a['pool'] if rows]+[b['candidates']]
    def freeze(value):
        return tuple(freeze(x) for x in value) if isinstance(value,list) else value
    for rows in options:
        for row in rows:row['semantics']=freeze(row['semantics'])
    assert len(options)==19 and sum(map(len,options))==209
    def summary(records):
        rows=[options[r['target']][r['index']] for r in records]
        means=[r['validation'][0]['mean'] if 'validation' in r else r['route'][1]['mean'] for r in rows]
        return dict(meanHeldOutChecks=statistics.mean(means), above5=sum(m>5 for m in means),
                    meanRepetition=statistics.mean(ranking.structural_repetition(r) for r in rows),
                    symmetricDoubleXor=sum(sum(c[0]=='xor' and c[2]==c[4] for c in r['clues'])>=2 for r in rows),
                    crossSlotClauses=statistics.mean(r['structure']['crossSlotClauses'] for r in rows))
    comparisons=[]
    for preferred in (3,5):
        old=[];new=[];changed=0
        for seed in (20261008,20261009,20261010):
            order=list(range(19));random.Random(seed).shuffle(order)
            before=ranking.select_sequence(options,order,seed,.25,preferred,0,repetition_strength=0)
            after=ranking.select_sequence(options,order,seed,.25,preferred,0)
            old.extend(before);new.extend(after)
            changed+=sum(x['index']!=y['index'] for x,y in zip(before,after))
        comparisons.append(dict(preferred=preferred,selections=57,changed=changed,
                                before=summary(old),after=summary(new)))
    single=[]
    for strength in (0,ranking.REPETITION_STRENGTH):
        record=ranking.select_sequence([b['candidates']],[0],20301013,.25,3,0,strength)[0]
        r=b['candidates'][record['index']]
        single.append(dict(repetitionStrength=strength,repetition=ranking.structural_repetition(r),
                           heldOutMean=r['route'][1]['mean'],clueCount=len(r['clues'])))
    result=dict(complete=True,records=209,targets=19,freshKnowledgeOnly=True,
                routeStrength=.25,repetitionStrength=ranking.REPETITION_STRENGTH,
                comparisons=comparisons,case11TargetCounterfactual=single,
                inputHashes={p.name:ranking.sha(p) for p in (original,gap)},
                sourceHashes={p.name:ranking.sha(p) for p in (Path(__file__),Path(ranking.__file__))},
                caveat='Finite ranking preference only; no fields, rules or simulated routes changed. Human benefit uncalibrated.')
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('original','gap','output'):parser.add_argument(name,type=Path)
    args=parser.parse_args();run(args.original,args.gap,args.output)
