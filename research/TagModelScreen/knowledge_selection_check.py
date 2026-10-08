"""Frozen selection check; only missing knowledge contexts need new replays."""
import argparse
import copy
import itertools
import json
import random
import statistics
import time
from pathlib import Path
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from science_route_comparison import Investigation


def run(corpus,original,gap,private_output,public_output):
    assert not private_output.resolve().is_relative_to(ranking.ROOT)
    assert not private_output.exists() and not public_output.exists()
    started=time.monotonic();deadline=started+60
    model=three.load_model(corpus);three.assert_accepted_baseline(model)
    data=json.loads(original.read_text(encoding='utf-8'))
    extension=json.loads(gap.read_text(encoding='utf-8'))
    missing=data['targets'].index(extension['target']);assert not data['pool'][missing]
    options=copy.deepcopy(data['pool']);options[missing]=extension['candidates']
    assert len(options)==19 and sum(map(len,options))==209
    def freeze(x):return tuple(freeze(v) for v in x) if isinstance(x,list) else x
    for rows in options:
        for row in rows:row['semantics']=freeze(row['semantics'])
    replays=0;covered_fields=[]
    for ti,rows in enumerate(options):
        contexts=[[tuple(e) for e in c] for c in data['knowledge'][ti]]
        for row in rows:
            triples=list(map(tuple,row['triples']))
            live_edges={e for t in triples for e in ranking.bounded.edges(t)}
            field_edges={e for t in itertools.product(*row['surface']) for e in ranking.bounded.edges(t)}
            stats=[]
            for ci,known in enumerate(contexts):
                priors=tuple(e for e in known if e in live_edges)
                assert all(reasoning.stable_relation(model,e) for e in known)
                stats.append(dict(fieldKnown=sum(e in field_edges for e in known),targetRelevantKnown=len(priors)))
                for policy in ('balanced','candidate_first'):
                    instance=Investigation(triples,priors,lambda e:reasoning.stable_relation(model,e),policy,deadline,stop_unique=True)
                    assert not set(instance.edges)&set(priors)
                if ti!=missing:
                    assert row['route'][ci]['observedStablePriors']==len(priors)
                    continue
                if ci==0:
                    fresh=copy.deepcopy(row['route']);row['route']=[fresh[0]];row['validation']=[fresh[1]]
                    continue
                for key,base,seeds in (('route',ranking.SEED+20000,16),('validation',ranking.SEED+90000,32)):
                    counts=[]
                    for policy in ('balanced','candidate_first'):
                        instance=Investigation(triples,priors,lambda e:reasoning.stable_relation(model,e),policy,deadline,stop_unique=True)
                        for seed in range(seeds):
                            assert time.monotonic()<deadline and replays<2304
                            replay=instance.replay(base+seed)
                            assert not any(tuple(h['edge']) in priors for h in replay['history'])
                            assert replay['tests']==len(replay['history'])
                            counts.append(replay['tests']);replays+=1
                    target=tuple(data['targets'][ti])
                    row[key].append(dict(mean=statistics.mean(counts),min=min(counts),max=max(counts),
                        above7=sum(n>7 for n in counts)/len(counts),observedStablePriors=len(priors),
                        initialCertified=all(e in priors for e in ranking.bounded.edges(target))))
            row['knowledgeAudit']=stats;covered_fields.append(stats)
    def summary(records,context):
        rows=[options[r['target']][r['index']] for r in records]
        route=[r['validation'][context] for r in rows]
        return dict(selections=len(rows),heldOutMean=statistics.mean(r['mean'] for r in route),
            meansAbove5=sum(r['mean']>5 for r in route),meansAbove7=sum(r['mean']>7 for r in route),
            meansBelow2=sum(r['mean']<2 for r in route),sampleMinBelow2=sum(r['min']<2 for r in route),
            meanRepetition=statistics.mean(ranking.structural_repetition(r) for r in rows),
            selectedWithRelevantKnowledge=sum(r['observedStablePriors']>0 for r in route),
            meanRelevantKnown=statistics.mean(r['observedStablePriors'] for r in route),
            maxSampledChecks=max(r['max'] for r in route))
    comparisons=[]
    for ci in range(3):
        for preferred in (3,5):
            old=[];new=[];changed=0
            for seed in (20261008,20261009,20261010):
                order=list(range(19));random.Random(seed).shuffle(order)
                before=ranking.select_sequence(options,order,seed,.25,preferred,ci,repetition_strength=0)
                after=ranking.select_sequence(options,order,seed,.25,preferred,ci)
                old.extend(before);new.extend(after)
                changed+=sum(x['index']!=y['index'] for x,y in zip(before,after))
                for r in after:
                    e=options[r['target']][r['index']]['route'][ci]
                    if e['mean']<2 and e['observedStablePriors']>0:
                        assert ranking.length_penalty(e['mean'],preferred,True)==0
            comparisons.append(dict(globalKnown=(0,1,4)[ci],preferred=preferred,changed=changed,
                before=summary(old,ci),after=summary(new,ci),earnedShortcutsPenalized=0))
    public=dict(complete=True,records=209,targets=19,newReplays=replays,knownEdgeQueries=0,comparisons=comparisons,
        knowledgeCoverage=[dict(globalKnown=(0,1,4)[ci],recordsWithFieldKnown=sum(s[ci]['fieldKnown']>0 for s in covered_fields),
            recordsWithTargetRelevantKnown=sum(s[ci]['targetRelevantKnown']>0 for s in covered_fields)) for ci in range(3)],
        inputHashes={p.name:ranking.sha(p) for p in (corpus,original,gap)},
        sourceHashes={p.name:ranking.sha(p) for p in (Path(__file__),Path(ranking.__file__))},
        seconds=round(time.monotonic()-started,3),
        caveat='Sparse global positive priors, full availability; not dense saves, negative memory or human routes.')
    private_output.write_text(json.dumps(dict(targets=data['targets'],knowledge=data['knowledge'],pool=options),indent=2),encoding='utf-8')
    public_output.write_text(json.dumps(public,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(public,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('corpus','original','gap','private_output','public_output'):p.add_argument(name,type=Path)
    a=p.parse_args();run(a.corpus,a.original,a.gap,a.private_output,a.public_output)
