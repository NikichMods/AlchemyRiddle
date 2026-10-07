"""Bounded expanded search for the previous empty target, with gate counters."""
import argparse
import collections
import hashlib
import json
import random
import statistics
import time
from pathlib import Path

import bounded_quality_diagnostic as bounded
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from science_route_comparison import Investigation


def legacy_rejection(model, raw, combo, triples, target_index):
    full = (1 << len(triples))-1
    masks = [raw[i][3] for i in combo]
    live = bounded.intersects(masks, full)
    if not 4 <= live.bit_count() <= 12:
        return 'residualRange'
    if any(bounded.intersects([m for j, m in enumerate(masks) if j != drop], full).bit_count()
           <= live.bit_count() for drop in range(len(masks))):
        return 'publicClueRedundancy'
    pf, fe = reasoning.branch_counts(triples, live)
    if not (2 <= pf <= 4 or 2 <= fe <= 4):
        return 'branchRange'
    answers = reasoning.compatible_indices(model, triples, live)
    if target_index not in answers or not 1 <= len(answers) <= 2:
        return 'compatibleAnswerRange'
    if reasoning.relation_elimination_profile(model, triples[target_index], triples, live)[0] is None:
        return 'authorEliminationWitness'
    raise AssertionError('legacy rejection breakdown disagrees with reused gate')


def run(corpus, original_pool, private_output, public_output):
    assert not private_output.resolve().is_relative_to(ranking.ROOT)
    started = time.monotonic()
    deadline = started+120
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    original = json.loads(original_pool.read_text(encoding='utf-8'))
    missing = [i for i, rows in enumerate(original['pool']) if not rows]
    assert len(missing) == 1
    index = missing[0]
    target = tuple(original['targets'][index])
    assert target in [f.triple for f in model.formulas]
    old_rng = random.Random(ranking.SEED+5000+index)
    relations = sorted([('PF', a, b) for a, b in model.stable_pf]
                       + [('FE', a, b) for a, b in model.stable_fe])
    assert tuple(old_rng.sample(relations, 4)) == tuple(tuple(e) for e in original['knowledge'][index][2])
    old_fields = reasoning.sampled_surfaces(model, target, 8, old_rng)
    old_counts = [sum(all(reasoning.stable_relation(model, e) for e in bounded.edges(t))
                      for t in reasoning.surface_triples(f)) for f in old_fields]
    seed = ranking.SEED+40000+index
    rng = random.Random(seed)
    counters = collections.Counter()
    fields = []
    candidates = []
    for surface in reasoning.sampled_surfaces(model, target, 32, rng):
        before = counters.copy()
        raw, triples, ti = reasoning.generate_true_weak_clues(model, model.tags, target, surface)
        full = (1 << len(triples))-1
        compatible = sum(1 << i for i, t in enumerate(triples)
                         if all(reasoning.stable_relation(model, e) for e in bounded.edges(t)))
        seen = set()
        for _ in range(2048):
            if time.monotonic() > deadline:
                raise RuntimeError('predeclared search cap exceeded')
            counters['attempts'] += 1
            k = rng.choice((2, 3))
            if len(raw) < k:
                counters['insufficientClues'] += 1
                continue
            combo = tuple(sorted(rng.sample(range(len(raw)), k)))
            if combo in seen:
                counters['duplicateCombo'] += 1
                continue
            seen.add(combo)
            counters['distinctPackages'] += 1
            masks = [raw[i][3] for i in combo]
            live = bounded.intersects(masks, full)
            if live & compatible != 1 << ti:
                counters['rejectCompleteAnswer'] += 1
                continue
            counters['uniqueAnswer'] += 1
            if any((bounded.intersects([m for j, m in enumerate(masks) if j != drop], full)
                    & compatible).bit_count() <= 1 for drop in range(k)):
                counters['rejectFullModelRedundancy'] += 1
                continue
            counters['necessaryFullModelClues'] += 1
            row = reasoning.option_from_combo(model, raw, combo, triples, ti)
            if row is None:
                counters['rejectLegacy_'+legacy_rejection(model, raw, combo, triples, ti)] += 1
                continue
            counters['legacyOptionAccepted'] += 1
            structure = bounded.summarize_package([(c[0], c[2], c[3]) for c in raw], combo, triples, model.tags)
            if structure['controlProxy']:
                counters['rejectFlatControl'] += 1
                continue
            if structure['immediatelyHandedAntecedents']:
                counters['rejectHandedAntecedent'] += 1
                continue
            counters['eligible'] += 1
            row.update(surface=surface, triples=[t for i, t in enumerate(triples) if live >> i & 1],
                       clues=[raw[i][2] for i in combo], structure=structure, route=[])
            if len(candidates) < 12:
                candidates.append(row)
            else:
                slot = rng.randrange(counters['eligible'])
                if slot < 12:
                    candidates[slot] = row
        fields.append(dict(weakClues=len(raw), compatibleTriplesBeforeClues=compatible.bit_count(),
                           counters={k: counters[k]-before[k] for k in counters
                                                       if counters[k] != before[k]}))
    search_seconds = time.monotonic()-started
    for row in candidates:
        for base, seeds in ((ranking.SEED+20000, 16), (ranking.SEED+90000, 32)):
            values = []
            for policy in ('balanced', 'candidate_first'):
                investigation = Investigation(row['triples'], (), lambda e: reasoning.stable_relation(model, e),
                                              policy, stop_unique=True)
                values.extend(investigation.replay(base+s)['tests'] for s in range(seeds))
                counters['replays'] += seeds
            row['route'].append(dict(mean=statistics.mean(values), min=min(values), max=max(values),
                                     observedStablePriors=0, initialCertified=False))
    selected = []
    if candidates:
        for preferred in (3, 5):
            scores = [ranking.baseline_score(r, [], 0)+0.25*ranking.length_penalty(r['route'][0]['mean'], preferred)
                      for r in candidates]
            best = random.Random(seed).choice([i for i, x in enumerate(scores) if x == min(scores)])
            row = candidates[best]
            selected.append(dict(preferred=preferred, strength=0.25,
                                 estimate=row['route'][0], heldOut=row['route'][1], structure=row['structure']))
    source_paths = [Path(__file__), Path(ranking.__file__), Path(reasoning.__file__), Path(three.__file__),
                    Path(bounded.__file__), ranking.ROOT/'research/TagModelScreen/science_route_comparison.py']
    report = dict(scope='one formerly empty variant, expanded unchanged 3x3x3 search', complete=True,
                  seed=seed, fields=len(fields), counters=dict(counters), perField=fields,
                  originalFieldCompatibleTriplesCounts=old_counts,
                  retained=len(candidates), selected=selected, searchSeconds=round(search_seconds, 3),
                  totalSeconds=round(time.monotonic()-started, 3),
                  limits=dict(fields=32, attempts=65536, retained=12, replays=1152, searchSeconds=120),
                  sourceHashes={p.name: ranking.sha(p) for p in source_paths},
                  inputHashes=dict(corpus=ranking.sha(corpus), originalPool=ranking.sha(original_pool)))
    private_output.write_text(json.dumps(dict(target=target, candidates=candidates), indent=2), encoding='utf-8')
    public_output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('complete', 'fields', 'counters', 'retained',
                                            'selected', 'searchSeconds', 'totalSeconds')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'original_pool', 'private_output', 'public_output'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.original_pool, args.private_output, args.public_output)
