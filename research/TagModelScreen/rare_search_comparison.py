"""Paired bounded rare-pair exploration; leaves the accepted generator unchanged."""
import argparse
import collections
import hashlib
import json
import random
from pathlib import Path

import bounded_quality_diagnostic as quality
from condition_variety_comparison import admissible, CORPUS_SHA256
from field_feasibility import supports_necessary_clues
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from rare_opportunity_screen import opportunity_prior

BUDGET = 512
RESERVES = (0, 64, 128)
REPEATS = 12


def focused_pair(groups, rare, rng):
    """Share attention between available rare roots, then sample a partner."""
    available = sorted(f for f in rare if groups.get(f))
    if not available:
        return None
    anchor = rng.choice(groups[rng.choice(available)])
    partners = [i for values in groups.values() for i in values if i != anchor]
    if not partners:
        return None
    return tuple(sorted((anchor, rng.choice(partners))))


def proposals(groups, compatible_count, seed, reserve, rare):
    if not 0 <= reserve <= BUDGET:
        raise ValueError('Reserve must fit the unchanged total budget')
    normal_rng = random.Random(seed)
    focused_rng = random.Random(seed + 10000000)
    active = any(groups.get(f) for f in rare)
    for attempt in range(BUDGET):
        # Always consume the ordinary stream: identical remaining proposals in
        # each paired arm, independent of focused-search and reservoir draws.
        k = normal_rng.choice((2, 3))
        normal = (reasoning.draw_family_first(groups, k, normal_rng)
                  if supports_necessary_clues(compatible_count, k) else None)
        if active and attempt < reserve:
            focused = focused_pair(groups, rare, focused_rng)
            yield focused if focused is not None else normal
        else:
            yield normal


def run(corpus, private_root, private_path, public_path):
    root = Path(__file__).resolve().parents[2]
    if private_path.resolve().is_relative_to(root) or private_path.exists() or public_path.exists():
        raise ValueError('Private witnesses outside Git; immutable completed passes')
    if hashlib.sha256(corpus.read_bytes()).hexdigest() != CORPUS_SHA256:
        raise ValueError('Unexpected corpus identity')
    training_paths = [private_root / f'family-first-private-{n}.json' for n in (0, 100000, 200000)]
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    prior, coverage = opportunity_prior([json.loads(p.read_text()) for p in training_paths], len(formulas))
    rare = {f for f, value in prior.items() if value > 0}
    relations = sorted([('PF', a, b) for a, b in model.stable_pf]
                       + [('FE', a, b) for a, b in model.stable_fe])
    fields = []
    for ti, formula in enumerate(formulas):
        rng = random.Random(ranking.SEED + 5000 + ti)
        rng.sample(relations, 4)
        for fi, surface in enumerate(reasoning.sampled_surfaces(model, formula.triple, 8, rng)):
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, formula.triple, surface)
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in quality.edges(t)))
            if supports_necessary_clues(compatible.bit_count(), 2):
                fields.append((ti, fi, surface, raw, triples, target_index, compatible))
    # Fixed fields and separate proposal/retention streams permit paired budget
    # comparison; this intentionally is not an exact old-RNG reservoir replay.
    cache, witnesses, results = {}, [], []
    for repeat in range(REPEATS):
        for reserve in RESERVES:
            counters = collections.Counter()
            families = collections.Counter()
            target_sets = collections.defaultdict(set)
            rare_masks = set()
            pools = collections.defaultdict(list)
            accepted = collections.Counter()
            retention_rng = {ti: random.Random(ranking.SEED + 800000 + repeat * 100 + ti)
                             for ti in range(len(formulas))}
            for ti, fi, surface, raw, triples, target_index, compatible in fields:
                groups = reasoning.family_groups(raw)
                seen = set()
                seed = ranking.SEED + repeat * 10000 + ti * 100 + fi
                for combo in proposals(groups, compatible.bit_count(), seed, reserve, rare):
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
                        cache[key] = admissible(model, raw, combo, triples, target_index, compatible)
                    row, verdict = cache[key]
                    counters[verdict] += 1
                    if row is None:
                        continue
                    roots = {reasoning.family_root(raw[i][0]) for i in combo}
                    families.update(roots)
                    for f in roots:
                        target_sets[f].add(ti)
                    record = dict(target=ti, surface=surface, families=sorted(roots),
                                  clues=[raw[i][2] for i in combo], masks=[raw[i][3] for i in combo])
                    if roots & rare:
                        rare_masks.add((ti, fi, tuple(sorted(record['masks']))))
                        witnesses.append(dict(repeat=repeat, reserve=reserve, **record))
                    accepted[ti] += 1
                    if len(pools[ti]) < 12:
                        pools[ti].append(record)
                    else:
                        slot = retention_rng[ti].randrange(accepted[ti])
                        if slot < 12:
                            pools[ti][slot] = record
            retained = collections.Counter(f for rows in pools.values() for row in rows for f in row['families'])
            results.append(dict(repeat=repeat, reserve=reserve, counters=dict(counters),
                                families=dict(families), targetCoverage={f: len(v) for f, v in target_sets.items()},
                                retainedFamilies=dict(retained), retained=sum(map(len, pools.values())),
                                servedTargets=len(pools), rareMaskPackages=len(rare_masks),
                                retainedRareTargets=len({ti for ti, rows in pools.items()
                                                         if any(set(r['families']) & rare for r in rows)})))
    report = dict(complete=True, budgetPerSearchableField=BUDGET, reserves=RESERVES,
                  repeats=REPEATS, searchableFields=len(fields), rareFamilies=sorted(rare),
                  priorCoverage=coverage, results=results,
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          [corpus, Path(__file__), *training_paths]},
                  caveat='Same frozen fields; independent per-field proposal streams. Not exact old RNG replay. '
                         'Counts overlap. No final ranking, route cost or human-experience validation.')
    private_path.write_text(json.dumps(dict(witnesses=witnesses), indent=2), encoding='utf-8')
    public_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'results'}, indent=2))
    for reserve in RESERVES:
        rows = [r for r in results if r['reserve'] == reserve]
        print(json.dumps(dict(reserve=reserve, eligible=[r['counters'].get('eligible', 0) for r in rows],
                              shared=[r['families'].get('shared', 0) for r in rows],
                              retainedShared=[r['retainedFamilies'].get('shared', 0) for r in rows],
                              rareMasks=[r['rareMaskPackages'] for r in rows],
                              served=[r['servedTargets'] for r in rows])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'private_root', 'private', 'public'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.private_root, args.private, args.public)
