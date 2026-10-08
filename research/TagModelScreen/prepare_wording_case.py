"""Freeze a fresh ordinary winner for the accepted human-wording trial."""
import argparse
import itertools
import json
import random
from pathlib import Path
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from prepare_real_case import TAGS
from prepare_corpus_contrast import convert, SLOTS
from field_feasibility import supports_necessary_clues
from intra_package_review import holds
from science_route_comparison import Investigation


def run(private, case=14, require_xor=False):
    assert case >= 14
    corpus = private / 'ordinary-3.json'
    pool = private / 'generator-route-ranking-private.json'
    fixture_path = private / f'corpus-{case}.raw.json'
    facilitator_path = private / f'corpus-{case}.facilitator.raw.json'
    assert not private.resolve().is_relative_to(ranking.ROOT)
    assert not fixture_path.exists() and not facilitator_path.exists()
    previous = [private / name for name in ('corpus-11-facilitator.json',
                'corpus-12b-facilitator.json', 'corpus-13b-facilitator.json')]
    previous += [private / f'corpus-{n}-facilitator.json' for n in range(14, case)]
    excluded = {tuple(json.loads(p.read_text(encoding='utf-8'))['sourceTarget']) for p in previous}
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    data = json.loads(pool.read_text(encoding='utf-8'))
    choices = []
    for ti, rows in enumerate(data['pool']):
        if not rows or tuple(data['targets'][ti]) in excluded:
            continue
        winner = ranking.select_sequence([rows], [0], 20261008 + ti, .25, 3, 0)[0]
        row = rows[winner['index']]
        # Trial sampling only: preserve ordinary ranking and the prior contrast envelope.
        if (len(row['clues']) == 2 and len(reasoning.option_family_set(row)) == 2
                and len({convert(c)['kind'] for c in row['clues']}) == 2
                and 2 <= row['validation'][0]['mean'] <= 5
                and (not require_xor or any(c[0] == 'xor' for c in row['clues']))):
            choices.append((ti, winner['index'], row))
    assert choices, 'No fresh ordinary winner; do not loosen gates to force a trial'
    ti, ri, row = random.Random(20261008 + case * 1000 + case).choice(choices)
    target = tuple(data['targets'][ti])
    tuples = list(itertools.product(*row['surface']))
    masks = [{t for t in tuples if holds(c, t, model.tags)} for c in row['clues']]
    live = set.intersection(*masks)
    compatible = {t for t in tuples if all(reasoning.stable_relation(model, e)
                  for e in ranking.bounded.edges(t))}
    assert live == set(map(tuple, row['triples'])) and live & compatible == {target}
    assert all(len(m & compatible) > 1 for m in masks)
    assert supports_necessary_clues(len(compatible), len(masks))
    mapping, cards = {}, []
    rng = random.Random(20261008 + case * 1000 + case + 1)
    for slot, label, prefix, source in zip(SLOTS, ('Порошок', 'Жидкость', 'Эссенция'),
                                         ('p', 'f', 'e'), row['surface']):
        order = list(source)
        rng.shuffle(order)
        entries = []
        for i, item in enumerate(order, 1):
            identifier = f'{prefix}{i}'
            mapping[item] = identifier
            entries.append(dict(id=identifier, name=f'{label} №{i}',
                                tags=[TAGS[t] for t in sorted(model.tags[item])]))
        cards.append(dict(id=slot, name=label, cards=entries))
    stable = sorted({f'{mapping[e[1]]}:{mapping[e[2]]}' for t in tuples
                    for e in ranking.bounded.edges(t) if reasoning.stable_relation(model, e)})
    fixture = dict(id=f'lab-v0-corpus-{case}', title=f'Неизвестная смесь · опыт {case}',
        description='Соберите смесь: один порошок, одна жидкость и одна эссенция. '
                    'Все сведения о составе верны одновременно. Свойства перечислены полностью. '
                    'Для искомой формулы нужны две стабильные пары и соблюдение всех условий состава. '
                    'Две стабильные пары сами по себе ещё не гарантируют успех.',
        slots=cards, propertyVocabulary=list(TAGS.values()),
        clues=[convert(c) for c in row['clues']], compatibility=dict(stablePairs=stable),
        knownRelations=[], science=20, pairTestCost=2, submissionCost=5,
        economy=dict(mode='sharedScience', refillAmount=10),
        answer={s: mapping[t] for s, t in zip(SLOTS, target)})
    alias_live = [tuple(mapping[x] for x in t) for t in row['triples']]
    routes = {policy: Investigation(alias_live, (), lambda e: f'{e[1]}:{e[2]}' in stable,
              policy, stop_unique=True).distribution() for policy in ('balanced', 'candidate_first')}
    fixture_path.write_text(json.dumps(fixture, ensure_ascii=False, indent=2), encoding='utf-8')
    record = dict(warning='FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY',
        id=fixture['id'], sourceTarget=target, sourceTargetIndex=ti, sourceRowIndex=ri,
        sourceClues=row['clues'], identityMapping=mapping, publicAliasPolicies=routes,
        sourceHashes={p.name: ranking.sha(p) for p in (corpus, pool, *previous, Path(__file__), Path(ranking.__file__))},
        rawFixtureSha256=ranking.sha(fixture_path),
        conversionTruth=[dict(tuple={s: mapping[x] for s, x in zip(SLOTS, t)},
                             values=[t in m for m in masks]) for t in tuples],
        sampling=f'Fresh targets excluding cases 11 through {case-1}; ordinary per-target winners first, then fixed-seed choice within the prior two-clue mixed-family/display-kind cached-mean 2–5 envelope. Required XOR: {require_xor}. Trial sampling, not a new generator gate.',
        semantics='Complete properties; all clauses AND both adjacent stable pairs. No priors; binary deterministic experiments, no partial synthesis feedback.',
        economy=dict(initialScience=20, pairCost=2, wholeCost=5, refill=10,
                     limit=None, refillBurden='Zero in Lab; game acquisition unmodeled'),
        stopping='Correct submission ends; incorrect stays active. Unlimited refill. Logical deduction can justify submission without certifying every edge.',
        next='Apply versioned wording and one explicit aside; validate and freeze before any player choice.')
    facilitator_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(dict(id=fixture['id'], eligibleWinners=len(choices),
                         rawFixtureSha256=ranking.sha(fixture_path), structuralGatesPassed=True)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('private', type=Path)
    parser.add_argument('--case', type=int, default=14)
    parser.add_argument('--require-xor', action='store_true')
    args = parser.parse_args()
    run(args.private, args.case, args.require_xor)
