"""Precommit one fresh target already selected with the accepted research ranking."""
import argparse
import itertools
import json
import random
from pathlib import Path
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from prepare_real_case import TAGS
from field_feasibility import supports_necessary_clues
from intra_package_review import holds
from science_route_comparison import Investigation

SLOTS=('powder','fluid','essence')


def convert(spec):
    def term(i,tag):return dict(slot=SLOTS[i],tag=TAGS[tag])
    if spec[0]=='literal':
        return dict(kind='exactly',count=int(spec[3]),terms=[term(('P','F','E').index(spec[1]),spec[2])])
    if spec[0]=='count':
        return dict(kind='exactly',count=spec[2],terms=[term(i,spec[1]) for i in range(3)])
    if spec[0]=='count_mixed':
        return dict(kind='exactly',count=spec[2],terms=[term(i,tag) for i,tag in enumerate(spec[1])])
    if spec[0]=='shared':
        return dict(kind='sharedTag')
    _,a,ta,b,tb=spec
    if spec[0]=='xor':return dict(kind='exactly',count=1,terms=[term(a,ta),term(b,tb)])
    if spec[0].startswith('imp_pos'):return dict(kind='implies',**{'if':term(a,ta),'then':term(b,tb)})
    if spec[0].startswith('imp_neg'):return dict(kind='notTogether',left=term(a,ta),right=term(b,tb))
    raise ValueError('Unsupported source clause')


def run(corpus,pool,fixture_path,facilitator_path):
    for p in (fixture_path,facilitator_path):
        assert not p.resolve().is_relative_to(ranking.ROOT) and not p.exists(), 'Never overwrite a case'
    model=three.load_model(corpus);three.assert_accepted_baseline(model)
    data=json.loads(pool.read_text(encoding='utf-8'))
    choices=[]
    # Rank each target normally first, then sample a contrast from its winning output.
    for ti,rows in enumerate(data['pool']):
        if not rows:continue
        record=ranking.select_sequence([rows],[0],20261008+ti,.25,3,0)[0]
        row=rows[record['index']]
        if (len(row['clues'])==2 and len(reasoning.option_family_set(row))==2
                and len({convert(c)['kind'] for c in row['clues']})==2
                and 2<=row['validation'][0]['mean']<=5):
            choices.append((ti,record['index'],row))
    assert choices, 'No eligible fresh contrast; do not alter ranking to force one'
    ti,ri,row=random.Random(20261008+12012).choice(choices)
    target=tuple(data['targets'][ti])
    source_triples=list(itertools.product(*row['surface']))
    masks=[{t for t in source_triples if holds(c,t,model.tags)} for c in row['clues']]
    live=set.intersection(*masks)
    assert live==set(map(tuple,row['triples']))
    compatible={t for t in source_triples if all(reasoning.stable_relation(model,e) for e in ranking.bounded.edges(t))}
    assert live & compatible=={target} and all(len(m & compatible)>1 for m in masks)
    assert supports_necessary_clues(len(compatible),2)
    mapping={};cards=[];rng=random.Random(20261008+12013)
    for slot,label,prefix,original in zip(SLOTS,('Порошок','Жидкость','Эссенция'),('p','f','e'),row['surface']):
        order=list(original);rng.shuffle(order);entries=[]
        for i,item in enumerate(order,1):
            identifier=f'{prefix}{i}';mapping[item]=identifier
            entries.append(dict(id=identifier,name=f'{label} №{i}',tags=[TAGS[t] for t in sorted(model.tags[item])]))
        cards.append(dict(id=slot,name=label,cards=entries))
    stable=sorted({f'{mapping[e[1]]}:{mapping[e[2]]}' for t in source_triples for e in ranking.bounded.edges(t)
                   if reasoning.stable_relation(model,e)})
    fixture=dict(id='lab-v0-corpus-12',title='Неизвестная смесь · опыт 12',
        description='Соберите смесь: один порошок, одна жидкость и одна эссенция.',
        slots=cards,clues=[convert(c) for c in row['clues']],
        compatibility=dict(stablePairs=stable),knownRelations=[],science=20,pairTestCost=2,submissionCost=5,
        economy=dict(mode='sharedScience',refillAmount=10),answer={s:mapping[t] for s,t in zip(SLOTS,target)})
    alias_live=[tuple(mapping[x] for x in t) for t in row['triples']]
    routes={policy:Investigation(alias_live,(),lambda e:f'{e[1]}:{e[2]}' in stable,
                                  policy,stop_unique=True).distribution() for policy in ('balanced','candidate_first')}
    fixture_path.write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8')
    record=dict(warning='FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY',
        id=fixture['id'],sourceTarget=target,sourceTargetIndex=ti,sourceRowIndex=ri,
        sourceClues=row['clues'],identityMapping=mapping,
        sourceHashes={p.name:ranking.sha(p) for p in (corpus,pool,Path(__file__),Path(ranking.__file__))},
        fixtureSha256=ranking.sha(fixture_path),publicAliasPolicies=routes,
        sampling='Ordinary per-target winners first; uniform fixed-seed sample of two-clue mixed-family AND distinct displayed-rule-kind winners with held-out mean 2–5. Original pool excludes case-11 target by its empty reserve.',
        economy=dict(initialScience=20,pairCost=2,wholeCost=5,refill=10,limit=None,refillBurden='Zero in Lab'),
        semantics='Complete displayed tags; both adjacent pairs stable AND all clauses simultaneously true. No prior knowledge. Unknown edges deterministic; no additional feedback on failed synthesis.',
        stopping='Correct whole submission stops; incorrect remains active. Refill unlimited. Logical deduction may justify submission without edge certification.',
        next='First player choice; never edit the frozen model after opening.')
    facilitator_path.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(id=fixture['id'],contrastWinners=len(choices),fixtureSha256=record['fixtureSha256'],
                         facilitatorSha256=ranking.sha(facilitator_path),structuralGatesPassed=True)))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('corpus','pool','fixture','facilitator'):parser.add_argument(name,type=Path)
    a=parser.parse_args();run(a.corpus,a.pool,a.fixture,a.facilitator)
