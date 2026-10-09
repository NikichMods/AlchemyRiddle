"""Frozen-pool rarity preference comparison; no production weight mutation."""
import argparse
import collections
import hashlib
import json
import math
import random
import statistics
from pathlib import Path

import generator_route_ranking as ranking
import reasoning_diversity_screen as reasoning


def restore_pool_semantics(pool):
    # JSON turns tuple-based semantic keys (including nested mixed counts) into lists.
    def freeze(value):
        return tuple(freeze(v) for v in value) if isinstance(value, list) else value
    for rows in pool:
        for row in rows:
            row['semantics'] = freeze(row['semantics'])


def opportunity_prior(witness_sets, target_count):
    coverage = collections.defaultdict(set)
    for data in witness_sets:
        for row in data['witnesses']:
            if row['arm'] == 'family_first':
                for family in reasoning.option_family_set(row):
                    coverage[family].add(row['target'])
    # Bounded linear prior; no division by tiny observed frequencies.
    prior = {f: max(0, 1 - len(ids) / (target_count / 4)) for f, ids in coverage.items()}
    return prior, {f: len(ids) for f, ids in coverage.items()}


def opportunity_bonus(row, chosen, prior, strength):
    recent = set().union(*(reasoning.option_family_set(r) for r in chosen[-2:]))
    return strength * max((prior.get(f, 0) for f in reasoning.option_family_set(row)
                           if f not in recent), default=0)


def select(options, order, seed, preferred, context, prior, strength):
    rng = random.Random(seed)
    chosen, records = [], []
    for target in order:
        rows = options[target]
        if not rows:
            continue
        scores = [ranking.selection_score(r, chosen, len(chosen), .25, preferred, context)
                  - opportunity_bonus(r, chosen, prior, strength) for r in rows]
        best = min(scores)
        index = rng.choice([i for i, s in enumerate(scores) if abs(s - best) < 1e-10])
        records.append(dict(target=target, index=index))
        chosen.append(rows[index])
    return records


def metrics(options, records, context):
    rows = [options[r['target']][r['index']] for r in records]
    families = collections.Counter(f for row in rows for f in reasoning.option_family_set(row))
    signatures = collections.Counter(repr(reasoning.abstract_semantics(row)) for row in rows)
    total = sum(families.values())
    entropy = -sum((n / total) * math.log2(n / total) for n in families.values())
    return dict(families=dict(families), selected=len(rows), entropy=entropy,
                distinctFamilies=len(families), maxSemanticRepeat=max(signatures.values()),
                adjacentSemanticRepeats=sum(reasoning.abstract_semantics(a) == reasoning.abstract_semantics(b)
                                            for a, b in zip(rows, rows[1:])),
                adjacentFamilyOverlap=statistics.mean(reasoning.jaccard(reasoning.option_family_set(a),
                                                       reasoning.option_family_set(b)) for a, b in zip(rows, rows[1:])),
                heldOutMean=statistics.mean(r['validation'][context]['mean'] for r in rows),
                selectedAbove5=sum(r['validation'][context]['mean'] > 5 for r in rows) / len(rows),
                selectedAbove7=sum(r['validation'][context]['mean'] > 7 for r in rows) / len(rows))


def run(private_root, public_path):
    if public_path.exists():
        raise ValueError('Never overwrite a completed pass')
    paths = [private_root / f'family-first-private-{n}.json' for n in (0, 100000, 200000)]
    pool_path = private_root / 'family-first-ranking-adopted-private.json'
    training = [json.loads(p.read_text()) for p in paths]
    data = json.loads(pool_path.read_text())
    prior, coverage = opportunity_prior(training, len(data['targets']))
    options = data['pool']
    restore_pool_semantics(options)
    results = []
    for context in range(3):
        for preferred in (3, 5):
            arms = {}
            for strength in (0, .25, .5, 1, 2):
                samples = []
                for variant in range(12):
                    order = list(range(len(options)))
                    random.Random(ranking.SEED + 30000 + variant).shuffle(order)
                    records = select(options, order, ranking.SEED + variant, preferred, context, prior, strength)
                    if strength == 0:
                        expected = ranking.select_sequence(options, order, ranking.SEED + variant,
                                                           .25, preferred, context)
                        assert [(r['target'], r['index']) for r in records] == [(r['target'], r['index']) for r in expected]
                    samples.append(metrics(options, records, context))
                family_counts = collections.Counter()
                for sample in samples:
                    family_counts.update(sample['families'])
                arms[str(strength)] = dict(families=dict(family_counts),
                    means={key: statistics.mean(sample[key] for sample in samples)
                           for key in samples[0] if key != 'families'},
                    originalThreeMeans={key: statistics.mean(sample[key] for sample in samples[:3])
                                        for key in ('entropy', 'heldOutMean', 'distinctFamilies')},
                    additionalNineMeans={key: statistics.mean(sample[key] for sample in samples[3:])
                                         for key in ('entropy', 'heldOutMean', 'distinctFamilies')})
            results.append(dict(context=context, preferred=preferred, arms=arms))
    report = dict(complete=True, targets=len(options), poolCandidates=sum(map(len, options)),
                  opportunityTargetCoverage=coverage, prior=prior, orders=12,
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths + [pool_path, Path(__file__)]},
                  results=results,
                  caveat='Frozen full-availability sample, no new field validation or human-interest proof. '
                         'Sparse prior not a calibrated production weight; repeated target encounters not simulated.')
    public_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(dict(coverage=coverage, prior=prior,
                         freshPreferred3=results[0]['arms']), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('private_root', type=Path)
    parser.add_argument('public', type=Path)
    args = parser.parse_args()
    run(args.private_root, args.public)
