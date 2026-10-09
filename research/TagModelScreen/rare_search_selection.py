"""Reconstruct paired pools, assert prior aggregates, evaluate unchanged selection."""
import argparse
import collections
import hashlib
import itertools
import json
import random
import statistics
import time
from pathlib import Path

import bounded_quality_diagnostic as quality
from condition_variety_comparison import admissible, CORPUS_SHA256
from field_feasibility import supports_necessary_clues
from intra_package_review import holds
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from rare_opportunity_screen import metrics, opportunity_prior
from rare_search_comparison import proposals, REPEATS
from science_route_comparison import Investigation

RESERVES = (0, 64)
ORDERS = 12


def verify_row(model, row, target):
    triples = list(itertools.product(*row['surface']))
    masks = [{t for t in triples if holds(c, t, model.tags)} for c in row['clues']]
    live = set.intersection(*masks)
    assert live == set(row['triples'])
    compatible = {t for t in triples if all(reasoning.stable_relation(model, e) for e in quality.edges(t))}
    assert live & compatible == {target}
    assert all(len(set.intersection(*(m for j, m in enumerate(masks) if i != j)) & compatible) > 1
               for i in range(len(masks)))


def estimate(model, row, context, target, deadline):
    relevant = {e for t in row['triples'] for e in quality.edges(t)}
    priors = tuple(e for e in context if e in relevant)
    summaries = []
    for start, seeds in ((20000, 16), (90000, 32)):
        counts = []
        for policy in ('balanced', 'candidate_first'):
            investigator = Investigation(row['triples'], priors,
                lambda e: reasoning.stable_relation(model, e), policy, deadline, stop_unique=True)
            for seed in range(seeds):
                if time.monotonic() > deadline:
                    raise RuntimeError('Six-minute route cap exceeded')
                counts.append(investigator.replay(ranking.SEED + start + seed)['tests'])
        summaries.append(dict(mean=statistics.mean(counts), min=min(counts), max=max(counts),
                              above7=sum(n > 7 for n in counts)/len(counts),
                              observedStablePriors=len(priors),
                              initialCertified=all(e in priors for e in quality.edges(target))))
    return summaries


def run(corpus, private_root, previous, private_output, public_output):
    root = Path(__file__).resolve().parents[2]
    if private_output.resolve().is_relative_to(root) or private_output.exists() or public_output.exists():
        raise ValueError('Private witnesses outside Git; completed evidence immutable')
    if hashlib.sha256(corpus.read_bytes()).hexdigest() != CORPUS_SHA256:
        raise ValueError('Unexpected corpus identity')
    previous_report = json.loads(previous.read_text())
    expected = {(r['repeat'], r['reserve']): r for r in previous_report['results']}
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    training_paths = [private_root / f'family-first-private-{n}.json' for n in (0, 100000, 200000)]
    prior, _ = opportunity_prior([json.loads(p.read_text()) for p in training_paths], len(formulas))
    rare = {f for f, value in prior.items() if value > 0}
    relations = sorted([('PF', a, b) for a, b in model.stable_pf]
                       + [('FE', a, b) for a, b in model.stable_fe])
    fields, knowledge = [], []
    for ti, formula in enumerate(formulas):
        rng = random.Random(ranking.SEED + 5000 + ti)
        known = tuple(rng.sample(relations, 4))
        knowledge.append(((), known[:1], known))
        for fi, surface in enumerate(reasoning.sampled_surfaces(model, formula.triple, 8, rng)):
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, formula.triple, surface)
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in quality.edges(t)))
            if supports_necessary_clues(compatible.bit_count(), 2):
                fields.append((ti, fi, surface, raw, triples, target_index, compatible))
    pools, cache = {}, {}
    deadline = time.monotonic() + 360
    for repeat in range(REPEATS):
        for reserve in RESERVES:
            counters, families = collections.Counter(), collections.Counter()
            target_sets = collections.defaultdict(set)
            rare_masks = set()
            pool = [[] for _ in formulas]
            accepted = collections.Counter()
            rngs = {ti: random.Random(ranking.SEED + 800000 + repeat * 100 + ti) for ti in range(len(formulas))}
            for ti, fi, surface, raw, triples, target_index, compatible in fields:
                groups = reasoning.family_groups(raw)
                seen = set()
                seed = ranking.SEED + repeat * 10000 + ti * 100 + fi
                for combo in proposals(groups, compatible.bit_count(), seed, reserve, rare):
                    if time.monotonic() > deadline:
                        raise RuntimeError('Six-minute pool reconstruction cap exceeded')
                    counters['attempts'] += 1
                    if combo is None:
                        counters['unsupportedSize'] += 1
                        continue
                    if combo in seen:
                        counters['duplicate'] += 1
                        continue
                    seen.add(combo)
                    key = (ti, fi, combo)
                    if key not in cache:
                        small, verdict = admissible(model, raw, combo, triples, target_index, compatible)
                        row = None
                        if small is not None:
                            row = reasoning.option_from_combo(model, raw, combo, triples, target_index)
                            live = quality.intersects([raw[i][3] for i in combo], (1 << len(triples)) - 1)
                            row.update(surface=surface, clues=small['clues'], masks=small['masks'],
                                       structure=small['structure'],
                                       triples=[t for i, t in enumerate(triples) if live >> i & 1])
                        cache[key] = row, verdict
                    row, verdict = cache[key]
                    counters[verdict] += 1
                    if row is None:
                        continue
                    roots = reasoning.option_family_set(row)
                    families.update(roots)
                    for f in roots:
                        target_sets[f].add(ti)
                    if roots & rare:
                        rare_masks.add((ti, fi, tuple(sorted(row['masks']))))
                    accepted[ti] += 1
                    if len(pool[ti]) < 12:
                        pool[ti].append(row)
                    else:
                        slot = rngs[ti].randrange(accepted[ti])
                        if slot < 12:
                            pool[ti][slot] = row
            actual = dict(counters=dict(counters), families=dict(families),
                          targetCoverage={f: len(v) for f, v in target_sets.items()},
                          retainedFamilies=dict(collections.Counter(f for rows in pool for r in rows
                                                                    for f in reasoning.option_family_set(r))),
                          retained=sum(map(len, pool)), servedTargets=sum(bool(rows) for rows in pool),
                          rareMaskPackages=len(rare_masks),
                          retainedRareTargets=sum(any(reasoning.option_family_set(r) & rare for r in rows) for rows in pool))
            assert all(actual[k] == expected[repeat, reserve][k] for k in actual), 'Prior aggregate replay mismatch'
            pools[repeat, reserve] = pool
        print(json.dumps(dict(stage='paired pools replayed', repeat=repeat)), flush=True)
    route_cache, verified = {}, set()
    deadline = time.monotonic() + 360
    for (repeat, reserve), pool in pools.items():
        for ti, rows in enumerate(pool):
            for row in rows:
                if id(row) not in verified:
                    verify_row(model, row, formulas[ti].triple)
                    verified.add(id(row))
                row['route'], row['validation'] = [], []
                for context in knowledge[ti]:
                    key = ti, tuple(row['triples']), context
                    if key not in route_cache:
                        route_cache[key] = estimate(model, row, context, formulas[ti].triple, deadline)
                    train, held = route_cache[key]
                    row['route'].append(train)
                    row['validation'].append(held)
        print(json.dumps(dict(stage='routes estimated', repeat=repeat, reserve=reserve,
                             uniqueContexts=len(route_cache))), flush=True)
    comparisons, selections = [], []
    for context in range(3):
        for preferred in (3, 5):
            samples = {reserve: [] for reserve in RESERVES}
            chosen_counts = {reserve: collections.Counter() for reserve in RESERVES}
            rare_opportunities = {reserve: 0 for reserve in RESERVES}
            totals = {reserve: 0 for reserve in RESERVES}
            above5 = {reserve: 0 for reserve in RESERVES}
            above7 = {reserve: 0 for reserve in RESERVES}
            for repeat in range(REPEATS):
                for order_index in range(ORDERS):
                    order = list(range(len(formulas)))
                    random.Random(ranking.SEED + 30000 + order_index).shuffle(order)
                    for reserve in RESERVES:
                        pool = pools[repeat, reserve]
                        records = ranking.select_sequence(pool, order, ranking.SEED + order_index,
                                                          .25, preferred, context)
                        sample = metrics(pool, records, context)
                        samples[reserve].append(sample)
                        chosen_counts[reserve].update(sample['families'])
                        totals[reserve] += len(records)
                        above5[reserve] += sum(pool[r['target']][r['index']]['validation'][context]['mean'] > 5 for r in records)
                        above7[reserve] += sum(pool[r['target']][r['index']]['validation'][context]['mean'] > 7 for r in records)
                        rare_opportunities[reserve] += sum(any(reasoning.option_family_set(r) & rare for r in rows) for rows in pool)
                        selections.append(dict(context=context, preferred=preferred, repeat=repeat,
                                               reserve=reserve, order=order_index, records=records))
            arms = {str(reserve): dict(families=dict(chosen_counts[reserve]), selected=totals[reserve],
                                      availableRareTargetSteps=rare_opportunities[reserve], above5=above5[reserve], above7=above7[reserve],
                                      means={k: statistics.mean(s[k] for s in samples[reserve])
                                             for k in samples[reserve][0] if k != 'families'}) for reserve in RESERVES}
            deltas = {k: [new[k] - old[k] for old, new in zip(samples[0], samples[64])]
                      for k in ('entropy', 'maxSemanticRepeat', 'heldOutMean', 'adjacentFamilyOverlap')}
            comparisons.append(dict(context=context, preferred=preferred, arms=arms,
                                    paired={k: dict(mean=statistics.mean(v), min=min(v), max=max(v),
                                                    increased=sum(x > 1e-10 for x in v),
                                                    decreased=sum(x < -1e-10 for x in v)) for k, v in deltas.items()}))
    report = dict(complete=True, exactPriorAggregateReplay=True, poolRuns=REPEATS, targetOrders=ORDERS,
                  startingKnowledge=(0, 1, 4), preferredChecks=(3, 5), reserves=RESERVES,
                  verifiedDistinctRetainedPackages=len(verified), estimatedUniquePublicContexts=len(route_cache),
                  sampledRouteReplays=len(route_cache)*96, comparisons=comparisons,
                  estimator=dict(policies=['balanced', 'candidate_first'], seedsPerPolicy=16,
                                 heldOutSeedsPerPolicy=32, stop='certified or unique public survivor'),
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          [corpus, previous, Path(__file__), Path(ranking.__file__), *training_paths]},
                  caveat='Unchanged selection weights; no rare bonus. Same frozen fields, dependent target orders. '
                         'Public-policy simulations, not measured human route or interest. Only shared empirically rare.')
    private_output.write_text(json.dumps(dict(pools=[dict(repeat=k[0], reserve=k[1], pool=v) for k, v in pools.items()],
                                             knowledge=knowledge, selections=selections), indent=2), encoding='utf-8')
    public_output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'comparisons'}, indent=2))
    for comparison in comparisons:
        print(json.dumps(comparison))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'private_root', 'previous', 'private_output', 'public_output'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.private_root, args.previous, args.private_output, args.public_output)
