# SPDX-License-Identifier: MPL-2.0
"""Bounded coverage follow-up using existing sampler and unchanged quality gates."""
import argparse
import collections
import copy
import hashlib
import json
import random
import time
from pathlib import Path

import bounded_quality_diagnostic as bounded
from condition_variety_comparison import admissible
from field_feasibility import supports_necessary_clues
import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from rare_search_selection import verify_row

FIELDS = 32
SEED = 20261010


def run(corpus, original_pool, private_output, public_output):
    if private_output.resolve().is_relative_to(ranking.ROOT) or private_output.exists() or public_output.exists():
        raise ValueError('Private identities outside Git; immutable completed evidence')
    started = time.monotonic()
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    original = json.loads(original_pool.read_text())
    result = copy.deepcopy(original)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    if original['targets'] != [list(f.triple) for f in formulas]:
        raise ValueError('Unexpected target alignment')
    missing = [i for i, rows in enumerate(original['pool']) if not rows]
    reports = []
    for ti in missing:
        counts = collections.Counter()
        target = formulas[ti].triple
        retained = []
        rng = random.Random(SEED + 40000 + ti)
        retention_rng = random.Random(SEED + 80000 + ti)
        for fi, surface in enumerate(reasoning.sampled_surfaces(model, target, FIELDS, rng)):
            if time.monotonic() - started > 120:
                raise RuntimeError('Predeclared two-minute follow-up cap exceeded')
            counts['fields'] += 1
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, target, surface)
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in bounded.edges(t)))
            if not supports_necessary_clues(compatible.bit_count(), 2):
                counts['fieldFloor'] += 1
                continue
            groups = reasoning.family_groups(raw)
            seen = set()
            for combo in reasoning.rare_package_proposals(groups, compatible.bit_count(), SEED + ti*100 + fi):
                counts['attempts'] += 1
                if combo is None or combo in seen:
                    continue
                seen.add(combo)
                small, verdict = admissible(model, raw, combo, triples, target_index, compatible)
                counts[verdict] += 1
                if small is None:
                    continue
                row = reasoning.option_from_combo(model, raw, combo, triples, target_index)
                live = bounded.intersects(small['masks'], (1 << len(triples))-1)
                row.update(surface=surface, triples=[t for i, t in enumerate(triples) if live >> i & 1],
                           clues=small['clues'], structure=small['structure'])
                verify_row(model, row, target)
                if len(retained) < 12:
                    retained.append(row)
                else:
                    slot = retention_rng.randrange(counts['eligible'])
                    if slot < 12:
                        retained[slot] = row
        result['pool'][ti] = retained
        reports.append(dict(counters=dict(counts), retained=len(retained)))
    if any(result['pool'][i] != original['pool'][i] for i in range(len(formulas)) if i not in missing):
        raise AssertionError('Previously retained package pool changed')
    private_output.write_text(json.dumps(result), encoding='utf-8')
    report = dict(complete=True, formerlyMissing=len(missing), recovered=sum(bool(result['pool'][i]) for i in missing),
                  totalTargets=len(formulas), servedTargets=sum(bool(r) for r in result['pool']),
                  retained=sum(map(len, result['pool'])), perMissingTarget=reports,
                  declaredLimit=dict(fieldsPerMissingTarget=FIELDS, attemptsPerSearchableField=512,
                                     rareReserve=64, retainedPerTarget=12, seconds=120),
                  seconds=round(time.monotonic()-started, 3),
                  inputHashes=dict(corpus=ranking.sha(corpus), originalPool=ranking.sha(original_pool)),
                  privatePoolHash=ranking.sha(private_output),
                  sourceHashes={p.name: ranking.sha(p) for p in
                                (Path(__file__), Path(reasoning.__file__), Path(ranking.__file__))},
                  caveat='Supplementary research search; default budget, weights and gates unchanged. Not exhaustive capacity proof.')
    public_output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('corpus', 'original_pool', 'private_output', 'public_output'):
        parser.add_argument(field, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.original_pool, args.private_output, args.public_output)
