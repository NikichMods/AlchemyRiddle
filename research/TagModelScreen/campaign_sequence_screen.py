# SPDX-License-Identifier: MPL-2.0
"""Frozen real-corpus packages + actual earned observations across sequences.

This is a coverage/route stress test, not the proposed human curriculum or a
claim that cached sampled fields exhaust all possible generation opportunities.
"""
import argparse
import collections
import copy
import hashlib
import itertools
import json
import random
import statistics
import time
from pathlib import Path

import bounded_quality_diagnostic as bounded
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
import two_slot_tag_constraint_screen as two
from campaign_knowledge import Knowledge
from rare_search_selection import verify_row
from science_route_comparison import Investigation

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261010
ORDERS = 12
ESTIMATION_SEEDS = 8


def freeze_json(value):
    return tuple(freeze_json(x) for x in value) if isinstance(value, list) else value


def resolved_indices(inv, mask, active):
    kind, _, survivors = inv.public_choices(mask, active)
    if kind == 'deduced':
        return survivors
    if kind == 'success':
        known = inv.known(mask)
        return [i for i in survivors if all(known.get(e) is True for e in bounded.edges(inv.triples[i]))]
    return []


def estimate(row, priors, oracle, deadline, seed_start=30000):
    counts = []
    for policy in ('balanced', 'candidate_first'):
        inv = Investigation(row['triples'], priors, oracle, policy, deadline, stop_unique=True)
        for seed in range(ESTIMATION_SEEDS):
            if time.monotonic() > deadline:
                raise RuntimeError('Predeclared screen time cap exceeded')
            counts.append(inv.replay(SEED + seed_start + seed)['tests'])
    return dict(mean=statistics.mean(counts), min=min(counts), max=max(counts),
                observedStablePriors=sum(priors.values()),
                observedIncompatiblePriors=sum(not v for v in priors.values()))


def legacy_replay(corpus, private_pool, deadline):
    """Recompute original 200-package route/held-out summaries, not just compare files."""
    data = json.loads(private_pool.read_text())
    model = three.load_model(corpus)
    oracle = lambda edge: reasoning.stable_relation(model, edge)
    counters = collections.Counter()
    for ti, rows in enumerate(data['pool']):
        for row in rows:
            row['triples'] = list(map(tuple, row['triples']))
            relevant = {e for t in row['triples'] for e in bounded.edges(t)}
            for ci, known in enumerate(data['knowledge'][ti]):
                priors = tuple(tuple(e) for e in known if tuple(e) in relevant)
                for key, offset, seeds in (('route', 20000, 16), ('validation', 90000, 32)):
                    counts = []
                    for policy in ('balanced', 'candidate_first'):
                        inv = Investigation(row['triples'], priors, oracle, policy, deadline, stop_unique=True)
                        for seed in range(seeds):
                            if time.monotonic() > deadline:
                                raise RuntimeError('Legacy replay time cap exceeded')
                            counts.append(inv.replay(ranking.SEED + offset + seed)['tests'])
                    got = dict(mean=statistics.mean(counts), min=min(counts), max=max(counts),
                               above7=sum(x > 7 for x in counts)/len(counts),
                               observedStablePriors=len(priors),
                               initialCertified=row[key][ci]['initialCertified'])
                    if got != row[key][ci]:
                        raise AssertionError('Legacy stable-only route summaries changed')
                    counters['replays'] += len(counts)
            counters['packages'] += 1
    return dict(counters)


def two_slot_capacity(path, deadline):
    model = two.Model(json.loads(path.read_text()))
    result = {}
    for shape in ((2, 2), (3, 3)):
        counts = collections.Counter()
        covered = set()
        for ti, f in enumerate(model.formulas):
            target = (f['powder'], f['fluid'])
            masks = two.clue_masks(model, target, 'composite')
            rng = random.Random(SEED + ti)
            for _ in range(64):
                if time.monotonic() > deadline:
                    raise RuntimeError('Two-slot capacity time cap exceeded')
                ps = (target[0], *rng.sample([p for p in model.powders if p != target[0]], shape[0]-1))
                fs = (target[1], *rng.sample([f for f in model.fluids if f != target[1]], shape[1]-1))
                verdict = two.classify(model, target, model.surface_mask(ps, fs), masks, 'compact')
                counts[verdict] += 1
                if verdict.startswith('unique'):
                    covered.add(ti)
        result['x'.join(map(str, shape))] = dict(attempts=sum(counts.values()),
                                              verdicts=dict(counts), targetsWithUnique=len(covered))
    return result


def run(corpus_dir, pool_path, original_corpus, original_pool, private_output, public_output):
    if private_output.resolve().is_relative_to(ROOT) or private_output.exists() or public_output.exists():
        raise ValueError('Private traces outside Git; completed evidence immutable')
    started = time.monotonic()
    deadline = started + 360
    legacy = legacy_replay(original_corpus, original_pool, deadline)
    print(json.dumps(dict(stage='legacy stable-only replay', **legacy)), flush=True)
    model = three.load_model(corpus_dir / 'ordinary-3.json')
    three.assert_accepted_baseline(model)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    options = json.loads(pool_path.read_text())['pool']
    if len(options) != len(formulas):
        raise ValueError('Pool/corpus target alignment mismatch')
    for ti, rows in enumerate(options):
        for row in rows:
            row['triples'] = list(map(tuple, row['triples']))
            row['semantics'] = freeze_json(row['semantics'])
            verify_row(model, row, formulas[ti].triple)
    oracle = lambda edge: reasoning.stable_relation(model, edge)
    all_edges = sorted({('PF', p, f) for p, f in itertools.product(model.powders, model.fluids)}
                       | {('FE', f, e) for f, e in itertools.product(model.fluids, model.essences)})
    cache = {}
    traces, aggregate = [], collections.defaultdict(list)
    counter = collections.Counter()
    order = list(range(len(formulas)))
    orders = [order, list(reversed(order))]
    for seed in range(ORDERS - 2):
        shuffled = list(order)
        random.Random(SEED + 100 + seed).shuffle(shuffled)
        orders.append(shuffled)
    for density in (0, .2, .6):
        for oi, order in enumerate(orders):
            for policy in ('balanced', 'candidate_first'):
                ledger = Knowledge()
                sampled = random.Random(SEED + oi).sample(all_edges, round(len(all_edges)*density))
                for edge in sampled:
                    ledger.observe(edge, oracle(edge), 'explicit stress-test starting observation')
                chosen, steps = [], []
                spent = 0
                for position, ti in enumerate(order):
                    counter['requestedPositions'] += 1
                    if not options[ti]:
                        counter['unservedPositions'] += 1
                        steps.append(dict(position=position, targetIndex=ti, status='no_sampled_package'))
                        continue
                    candidates = []
                    for ri, frozen in enumerate(options[ti]):
                        relevant = {e for t in frozen['triples'] for e in bounded.edges(t)}
                        priors = ledger.priors(relevant)
                        key = (ti, ri, tuple(sorted(priors.items())))
                        if key not in cache:
                            cache[key] = estimate(frozen, priors, oracle, deadline)
                            counter['routeEstimationReplays'] += 2*ESTIMATION_SEEDS
                        row = copy.copy(frozen)
                        row['route'] = [cache[key]]
                        score = ranking.selection_score(row, chosen, len(chosen), .25, 3, 0)
                        candidates.append((score, ri, row, priors))
                    best = min(c[0] for c in candidates)
                    eligible = [c for c in candidates if abs(c[0]-best) < 1e-10]
                    _, ri, selected, priors = random.Random(SEED + oi*1000 + position).choice(eligible)
                    # Counterfactual fixed-package comparison uses the SAME earned
                    # state, but deliberately hides negatives for diagnosis only.
                    stable_only = {e: value for e, value in priors.items() if value}
                    control = estimate(selected, stable_only, oracle, deadline)
                    counter['controlReplays'] += 2*ESTIMATION_SEEDS
                    inv = Investigation(selected['triples'], priors, oracle, policy, deadline, stop_unique=True)
                    replay = inv.replay(SEED + 900000 + oi*1000 + position)
                    history = replay['history']
                    mask = history[-1]['testedMask'] if history else 0
                    active = history[-1]['active'] if history else -1
                    resolved = resolved_indices(inv, mask, active)
                    if len(resolved) != 1 or selected['triples'][resolved[0]] != formulas[ti].triple:
                        raise AssertionError('Public-state route did not identify target uniquely')
                    for observation in history:
                        edge = tuple(observation['edge'])
                        if edge in ledger.pairs:
                            raise AssertionError('Paid re-test of an earned observation')
                        ledger.observe(edge, observation['stable'], f'position-{position}:pair experiment')
                        if observation['stable'] != oracle(edge):
                            raise AssertionError('Observed fact contradicts fixed corpus')
                    ledger.mixture(formulas[ti].triple, True, f'position-{position}:successful formula')
                    snapshot = ledger.snapshot()
                    if Knowledge.restore(json.loads(json.dumps(snapshot))).snapshot() != snapshot:
                        raise AssertionError('Knowledge snapshot round trip changed facts')
                    if any(value != oracle(edge) for edge, value in ledger.priors().items()):
                        raise AssertionError('Durable fact changed across levels')
                    spent += replay['science']
                    counter['completedPositions'] += 1
                    counter['paidChecks'] += replay['tests']
                    counter['zeroNewPairChecks'] += replay['tests'] == 0
                    counter['negativeObservationsEarned'] += sum(not h['stable'] for h in history)
                    mixed_mean = selected['route'][0]['mean']
                    aggregate[density].append(dict(checks=replay['tests'], mixedEstimate=mixed_mean,
                                                  stableOnlyEstimate=control['mean']))
                    steps.append(dict(position=position, targetIndex=ti, packageIndex=ri, status='completed',
                                      initialPriors=[dict(edge=e, stable=v) for e, v in sorted(priors.items())],
                                      route=replay, mixedEstimate=mixed_mean, stableOnlyEstimate=control['mean'],
                                      spent=spent, knowledge=snapshot))
                    chosen.append(selected)
                if spent != sum(s['route']['science'] for s in steps if s['status'] == 'completed'):
                    raise AssertionError('Spending ledger double counted')
                traces.append(dict(startingDensity=density, orderIndex=oi, policy=policy,
                                   totalScience=spent, steps=steps))
        print(json.dumps(dict(stage='density finished', density=density, sequences=len(traces))), flush=True)
    capacity = two_slot_capacity(corpus_dir / 'ordinary-2.json', deadline)
    summaries = {}
    for density, rows in aggregate.items():
        checks = [r['checks'] for r in rows]
        summaries[str(density)] = dict(completed=len(rows), meanNewPairChecks=statistics.mean(checks),
                                      maxNewPairChecks=max(checks), zeroCheckFraction=checks.count(0)/len(checks),
                                      fixedPackageMixedMean=statistics.mean(r['mixedEstimate'] for r in rows),
                                      fixedPackageStableOnlyMean=statistics.mean(r['stableOnlyEstimate'] for r in rows),
                                      mixedEstimateBetter=sum(r['mixedEstimate'] < r['stableOnlyEstimate'] for r in rows),
                                      mixedEstimateWorse=sum(r['mixedEstimate'] > r['stableOnlyEstimate'] for r in rows))
    private_output.write_text(json.dumps(dict(traces=traces), ensure_ascii=False), encoding='utf-8')
    report = dict(complete=True, seconds=round(time.monotonic()-started, 3), sequences=len(traces),
                  orders=ORDERS, policies=['balanced', 'candidate_first'], startingDensities=[0, .2, .6],
                  verifiedPackages=sum(map(len, options)), servedTargets=sum(bool(r) for r in options),
                  totalTargets=len(options), counters=dict(counter), summaries=summaries,
                  twoSlotBoundedCapacity=capacity, legacyReplay=legacy,
                  inputHashes={label: hashlib.sha256(p.read_bytes()).hexdigest() for label, p in
                               {'renamedThree': corpus_dir/'ordinary-3.json',
                                'renamedTwo': corpus_dir/'ordinary-2.json', 'pool': pool_path,
                                'originalThree': original_corpus, 'legacyPool': original_pool}.items()},
                  sourceHashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                                (Path(__file__), Path(ranking.__file__),
                                 ROOT/'research/TagModelScreen/campaign_knowledge.py',
                                 ROOT/'research/TagModelScreen/science_route_comparison.py')},
                  privateTraceHash=hashlib.sha256(private_output.read_bytes()).hexdigest(),
                  caveats=['Fixed sampled pool, not exhaustive regeneration under every knowledge history.',
                           'Stress-test initial observations are explicit simulated facts, not real player histories.',
                           'Automated public-state policies do not measure human difficulty or interest.',
                           'Two-slot screen is the existing compact/composite capacity diagnostic, not a playable curriculum.',
                           'Incomplete sampled target coverage remains visible; no validity gates relaxed.'])
    public_output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('corpus_dir', 'pool_path', 'original_corpus', 'original_pool', 'private_output', 'public_output'):
        parser.add_argument(field, type=Path)
    args = parser.parse_args()
    run(args.corpus_dir, args.pool_path, args.original_corpus, args.original_pool,
        args.private_output, args.public_output)
