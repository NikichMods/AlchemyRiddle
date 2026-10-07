"""Freeze one already-ranked corpus case, anonymized for blind Lab play."""
import argparse
import itertools
import json
import random
from pathlib import Path

import bounded_quality_diagnostic as bounded
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from field_feasibility import supports_necessary_clues
from science_route_comparison import Investigation

TAGS = dict(Plant='Растительное',Corpse='Трупное',Mineral='Минеральное',
            Insect='Насекомое',Animal='Животное',Fish='Рыбное',Slime='Слизь',
            Water='Водное',Dark='Тёмное',Organ='Орган')


def run(corpus, pool, fixture_path, facilitator_path):
    assert not fixture_path.resolve().is_relative_to(ranking.ROOT)
    assert not facilitator_path.resolve().is_relative_to(ranking.ROOT)
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    data = json.loads(pool.read_text(encoding='utf-8'))
    rows = data['candidates']
    scores = [ranking.baseline_score(r, [], 0)+0.25*ranking.length_penalty(r['route'][0]['mean'],3) for r in rows]
    index = random.Random(20301013).choice([i for i, value in enumerate(scores) if value == min(scores)])
    row = rows[index]
    source_target = tuple(data['target'])
    slots = ('powder','fluid','essence')
    names = ('Порошок','Жидкость','Эссенция')
    cards, mapping = [], {}
    rng = random.Random(20261007+11011)
    for slot, label, prefix, original in zip(slots,names,('p','f','e'),row['surface']):
        order = list(original)
        rng.shuffle(order)
        entries = []
        for i, item in enumerate(order,1):
            identifier = f'{prefix}{i}'
            mapping[item] = identifier
            entries.append(dict(id=identifier,name=f'{label} №{i}',tags=[TAGS[t] for t in sorted(model.tags[item])]))
        cards.append(dict(id=slot,name=label,cards=entries))
    clues = []
    for spec in row['clues']:
        assert spec[0] == 'xor', 'Retained selected package changed; do not improvise conversion.'
        _, a, ta, b, tb = spec
        clues.append(dict(kind='exactly',count=1,terms=[dict(slot=slots[a],tag=TAGS[ta]),dict(slot=slots[b],tag=TAGS[tb])]))
    source_triples = tuple(itertools.product(*row['surface']))
    compatible = [t for t in source_triples if all(reasoning.stable_relation(model,e) for e in bounded.edges(t))]
    assert supports_necessary_clues(len(compatible),len(clues))
    stable = sorted({f'{mapping[e[1]]}:{mapping[e[2]]}' for t in source_triples for e in bounded.edges(t)
                     if reasoning.stable_relation(model,e)})
    fixture = dict(id='lab-v0-corpus-11',title='Неизвестная смесь',
        description='Найдите состав неизвестной смеси. Все сведения о составе верны одновременно. Свойства перечислены полностью; обозначения образцов не добавляют правил. Порошок с жидкостью и жидкость с эссенцией должны образовать стабильные пары. Свойства сами по себе не определяют совместимость. Пара стоит 2 Science, вся смесь — 5 Science; запас общий и пополняемый. Получение науки в игре здесь не моделируется.',
        slots=cards,clues=clues,compatibility=dict(stablePairs=stable),knownRelations=[],
        science=20,pairTestCost=2,submissionCost=5,economy=dict(mode='sharedScience',refillAmount=10),
        answer={s:mapping[t] for s,t in zip(slots,source_target)})
    alias_live = [tuple(mapping[x] for x in t) for t in row['triples']]
    truth = set(stable)
    routes = {policy: Investigation(alias_live,(),lambda e:f'{e[1]}:{e[2]}' in truth,
              policy,stop_unique=True).distribution() for policy in ('balanced','candidate_first')}
    fixture_path.write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8')
    record = dict(warning='FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY',
        id=fixture['id'],sourceTarget=source_target,sourceRow=index,identityMapping=mapping,
        sourceHashes=dict(corpus=ranking.sha(corpus),pool=ranking.sha(pool),builder=ranking.sha(Path(__file__))),
        fixtureSha256=ranking.sha(fixture_path),publicAliasPolicies=routes,
        model='Same field, tags, clauses, complete compatibility graph and answer; only identities/order renamed.',
        economy=dict(initialScience=20,pairCost=2,wholeCost=5,refill=10,
                     limit=None,refillBurden='Zero in Lab; game acquisition burden not tested.'),
        stopping='A correct whole submission acknowledges success; it may follow certification or logical deduction. No automatic inference UI.',
        next='First player choice; do not edit fixture or semantics after opening.')
    facilitator_path.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(id=fixture['id'],fixtureSha256=record['fixtureSha256'],
                        retainedOldGates=True,fieldFloorPassed=True,identitiesAnonymized=True),indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus','pool','fixture','facilitator'):
        parser.add_argument(name,type=Path)
    args = parser.parse_args()
    run(args.corpus,args.pool,args.fixture,args.facilitator)
