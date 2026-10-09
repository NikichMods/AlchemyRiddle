"""Exact replay of the accepted main pool builder, instrumented before retention."""
import argparse
import collections
import hashlib
import itertools
import json
import random
import time
from pathlib import Path

import bounded_quality_diagnostic as quality
from condition_variety_comparison import admissible, CORPUS_SHA256
from field_feasibility import supports_necessary_clues
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning


def identity(row):
    return json.dumps(dict(surface=row['surface'], clues=row['clues']), sort_keys=True)


def run(corpus, retained_path, private_path, public_path):
    root = Path(__file__).resolve().parents[2]
    if private_path.resolve().is_relative_to(root) or private_path.exists() or public_path.exists():
        raise ValueError('Private exact witnesses outside Git; never overwrite a completed pass')
    if hashlib.sha256(corpus.read_bytes()).hexdigest() != CORPUS_SHA256:
        raise ValueError('Unexpected corpus identity')
    started = time.monotonic()
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    old = json.loads(retained_path.read_text())
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    assert [list(f.triple) for f in formulas] == old['targets']
    relations = sorted([('PF', a, b) for a, b in model.stable_pf]
                       + [('FE', a, b) for a, b in model.stable_fe])
    raw_fields = collections.Counter()
    attempted = collections.Counter()
    accepted = collections.Counter()
    retained = collections.Counter()
    gate_counts = collections.defaultdict(collections.Counter)
    accepted_targets = collections.defaultdict(set)
    retained_targets = collections.defaultdict(set)
    field_floor = collections.Counter()
    rare_records = []
    shared_fields = []
    counters = collections.Counter()
    for ti, formula in enumerate(formulas):
        rng = random.Random(ranking.SEED + 5000 + ti)
        known = tuple(rng.sample(relations, 4))
        assert [list(e) for e in known] == old['knowledge'][ti][2]
        surfaces = reasoning.sampled_surfaces(model, formula.triple, 8, rng)
        reservoir = []
        eligible = 0
        for surface in surfaces:
            counters['fields'] += 1
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, formula.triple, surface)
            families = set(c[0] for c in raw)
            raw_fields.update({reasoning.family_root(f) for f in families})
            groups = reasoning.family_groups(raw)
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in quality.edges(t)))
            if not supports_necessary_clues(compatible.bit_count(), 2):
                counters['fieldFloor'] += 1
                field_floor.update({reasoning.family_root(f) for f in families})
                continue
            if 'shared' in families:
                shared_fields.append((ti, surface, raw, triples, target_index, compatible))
            seen = set()
            for _ in range(512):
                if time.monotonic() - started > 180:
                    raise RuntimeError('Three-minute audit cap exceeded')
                counters['attempts'] += 1
                k = rng.choice((2, 3))
                if not supports_necessary_clues(compatible.bit_count(), k):
                    counters['packageFloor'] += 1
                    continue
                if len(raw) < k:
                    continue
                combo = reasoning.draw_family_first(groups, k, rng)
                if combo in seen:
                    continue
                seen.add(combo)
                roots = {reasoning.family_root(raw[i][0]) for i in combo}
                attempted.update(roots)
                _, verdict = admissible(model, raw, combo, triples, target_index, compatible)
                for family in roots:
                    gate_counts[family][verdict] += 1
                if verdict != 'eligible':
                    continue
                eligible += 1
                counters['eligible'] += 1
                accepted.update(roots)
                for family in roots:
                    accepted_targets[family].add(ti)
                row = dict(surface=surface, clues=[raw[i][2] for i in combo], families=tuple(roots))
                if 'shared' in roots:
                    rare_records.append(dict(target=ti, masks=[raw[i][3] for i in combo], **row))
                if len(reservoir) < 12:
                    reservoir.append(row)
                else:
                    slot = rng.randrange(eligible)
                    if slot < 12:
                        reservoir[slot] = row
        assert [identity(r) for r in reservoir] == [identity(r) for r in old['pool'][ti]], 'Pool replay mismatch'
        for row in reservoir:
            retained.update(row['families'])
            for family in row['families']:
                retained_targets[family].add(ti)
    kept = {identity(row) for rows in old['pool'] for row in rows}
    rare_kept = [r for r in rare_records if identity(r) in kept]
    rare_masks = {tuple(sorted(r['masks'])) for r in rare_records}
    # Additional exhaustive diagnostic on only the two replay fields that admit shared.
    # No RNG calls or modification of the original reservoir above.
    exhaustive = collections.Counter()
    exhaustive_records = []
    for ti, surface, raw, triples, target_index, compatible in shared_fields:
        anchor = next(i for i, c in enumerate(raw) if c[0] == 'shared')
        others = [i for i in range(len(raw)) if i != anchor]
        for k in (2, 3):
            if not supports_necessary_clues(compatible.bit_count(), k):
                continue
            for remaining in itertools.combinations(others, k - 1):
                if time.monotonic() - started > 180:
                    raise RuntimeError('Three-minute audit cap exceeded')
                combo = tuple(sorted((anchor,) + remaining))
                row, verdict = admissible(model, raw, combo, triples, target_index, compatible)
                exhaustive[verdict] += 1
                if row is not None:
                    exhaustive_records.append(dict(target=ti, surface=surface, **row))
    report = dict(complete=True, exactReservoirReplay=True, seconds=round(time.monotonic() - started, 3),
                  counters=dict(counters), poolCandidates=sum(len(rows) for rows in old['pool']),
                  families={f: dict(rawFields=raw_fields[f], fieldFloorRejected=field_floor[f],
                                    uniqueDrawnPackages=attempted[f], eligiblePackages=accepted[f],
                                    retainedPackages=retained[f], eligibleTargets=len(accepted_targets[f]),
                                    retainedTargets=len(retained_targets[f]), rejections=dict(gate_counts[f]))
                            for f in reasoning.FAMILY_ORDER},
                  sharedDistinctMaskPackages=len(rare_masks), sharedRetainedRecords=len(rare_kept),
                  exhaustiveSharedFields=len(shared_fields), exhaustiveSharedCounters=dict(exhaustive),
                  exhaustiveSharedDistinctMasks=len({(r['target'], json.dumps(r['surface']), tuple(sorted(r['masks'])))
                                                     for r in exhaustive_records}),
                  sampledMissedSharedPackages=sum(identity(r) not in {identity(x) for x in rare_records}
                                                  for r in exhaustive_records),
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          (corpus, retained_path, Path(__file__), Path(ranking.__file__), Path(reasoning.__file__))},
                  caveat='Exact replay of one frozen main run, not exhaustive rare-condition capacity. '
                         'Family presence counts overlap; raw eligibility is not proof of a valid package.')
    private_path.write_text(json.dumps(dict(rareRecords=rare_records, exhaustiveRecords=exhaustive_records), indent=2), encoding='utf-8')
    public_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'retained', 'private', 'public'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.retained, args.private, args.public)
