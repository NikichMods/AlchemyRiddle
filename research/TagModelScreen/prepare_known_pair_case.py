"""Freeze the previously selected knowledge-aware candidate, without re-selection."""
import argparse
import itertools
import json
import random
from pathlib import Path
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from prepare_real_case import TAGS
from prepare_corpus_contrast import convert,SLOTS
from intra_package_review import holds
from field_feasibility import supports_necessary_clues
from science_route_comparison import Investigation


def run(corpus,pool,selection,fixture_path,facilitator_path):
    for p in (fixture_path,facilitator_path):
        assert not p.resolve().is_relative_to(ranking.ROOT) and not p.exists()
    selected=json.loads(selection.read_text(encoding='utf-8'))
    assert ranking.sha(pool)==selected['poolHash']
    data=json.loads(pool.read_text(encoding='utf-8'))
    ti,ri,ci=(selected[k] for k in ('targetIndex','rowIndex','context'))
    row=data['pool'][ti][ri];target=tuple(data['targets'][ti])
    model=three.load_model(corpus);three.assert_accepted_baseline(model)
    tuples=list(itertools.product(*row['surface']))
    masks=[{t for t in tuples if holds(c,t,model.tags)} for c in row['clues']]
    live=set.intersection(*masks)
    compatible={t for t in tuples if all(reasoning.stable_relation(model,e) for e in ranking.bounded.edges(t))}
    assert live==set(map(tuple,row['triples'])) and live&compatible=={target}
    assert supports_necessary_clues(len(compatible),len(masks))
    assert all(len(set.intersection(*(m for j,m in enumerate(masks) if i!=j))&compatible)>1 for i in range(len(masks)))
    mapping={};cards=[];rng=random.Random(20261008+13014)
    for slot,label,prefix,source in zip(SLOTS,('Порошок','Жидкость','Эссенция'),('p','f','e'),row['surface']):
        order=list(source);rng.shuffle(order);entries=[]
        for i,item in enumerate(order,1):
            identifier=f'{prefix}{i}';mapping[item]=identifier
            entries.append(dict(id=identifier,name=f'{label} №{i}',tags=[TAGS[t] for t in sorted(model.tags[item])]))
        cards.append(dict(id=slot,name=label,cards=entries))
    field_edges={e for t in tuples for e in ranking.bounded.edges(t)}
    known=[tuple(e) for e in selected['globalKnowledge'] if tuple(e) in field_edges]
    assert len(known)==1 and all(reasoning.stable_relation(model,e) for e in known)
    stable=sorted({f'{mapping[e[1]]}:{mapping[e[2]]}' for e in field_edges if reasoning.stable_relation(model,e)})
    priors=[]
    for orientation,a,b in known:
        slots=SLOTS[:2] if orientation=='PF' else SLOTS[1:]
        priors.append(dict(slots=list(slots),tuple={slots[0]:mapping[a],slots[1]:mapping[b]},stable=True))
    fixture=dict(id='lab-v0-corpus-13',title='Неизвестная смесь · опыт 13',
        description='Соберите смесь: один порошок, одна жидкость и одна эссенция.',
        slots=cards,propertyVocabulary=list(TAGS.values()),
        clues=[convert(c) for c in row['clues']],compatibility=dict(stablePairs=stable),
        knownRelations=priors,science=20,pairTestCost=2,submissionCost=5,
        economy=dict(mode='sharedScience',refillAmount=10),answer={s:mapping[t] for s,t in zip(SLOTS,target)})
    alias_live=[tuple(mapping[x] for x in t) for t in row['triples']]
    alias_priors=tuple((e[0],mapping[e[1]],mapping[e[2]]) for e in known)
    routes={policy:Investigation(alias_live,alias_priors,lambda e:f'{e[1]}:{e[2]}' in stable,
        policy,stop_unique=True).distribution() for policy in ('balanced','candidate_first')}
    fixture_path.write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8')
    record=dict(warning='FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY',
        id=fixture['id'],sourceTarget=target,sourceClues=row['clues'],identityMapping=mapping,
        selectedCandidate=selected,publicAliasPolicies=routes,fixtureSha256=ranking.sha(fixture_path),
        sourceHashes={p.name:ranking.sha(p) for p in (corpus,pool,selection,Path(__file__))},
        semantics='All displayed tags complete; both adjacent edges stable AND all clauses hold. Prior observation is true; all unknown outcomes deterministic. No partial failure feedback.',
        economy=dict(initialScience=20,pairCost=2,wholeCost=5,refill=10,limit=None,knownPairCost=0,refillBurden='Zero in Lab; acquisition not modeled'),
        stopping='Correct submission ends play; wrong remains active. Logical deduction can justify submission without personally certifying both edges. No attempt cap or exhaustion stop.',
        next='First player choice; never change frozen model after opening.')
    facilitator_path.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(id=fixture['id'],fixtureSha256=ranking.sha(fixture_path),
        facilitatorSha256=ranking.sha(facilitator_path),knownStablePairs=len(priors),clues=len(masks),gatesPassed=True)))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('corpus','pool','selection','fixture','facilitator'):p.add_argument(name,type=Path)
    a=p.parse_args();run(a.corpus,a.pool,a.selection,a.fixture,a.facilitator)
