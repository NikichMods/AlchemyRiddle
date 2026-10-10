# SPDX-License-Identifier: MPL-2.0
"""Post-hoc aggregate diversity/shortcut analysis; frozen choices never reranked."""
import argparse
import collections
import hashlib
import json
import statistics
from pathlib import Path

from campaign_sequence_screen import freeze_json
import reasoning_diversity_screen as reasoning


def run(pool_path, traces_path, output):
    if output.exists():
        raise ValueError('Completed evidence is immutable')
    pool = json.loads(pool_path.read_text())['pool']
    for rows in pool:
        for row in rows:
            row['semantics'] = freeze_json(row['semantics'])
    traces = json.loads(traces_path.read_text())['traces']
    summaries = []
    for density in (0, .2, .6):
        family_counts = collections.Counter()
        repeats, distinct, maximum_repeats, checked_steps, improvements, deteriorations = [], [], [], [], [], []
        zero_reasons = collections.Counter()
        for trace in (t for t in traces if t['startingDensity'] == density):
            steps = [s for s in trace['steps'] if s['status'] == 'completed']
            rows = [pool[s['targetIndex']][s['packageIndex']] for s in steps]
            signatures = [reasoning.abstract_semantics(r) for r in rows]
            families = {f for r in rows for f in reasoning.option_family_set(r)}
            distinct.append(len(families))
            family_counts.update(f for r in rows for f in reasoning.option_family_set(r))
            repeats.append(sum(a == b for a, b in zip(signatures, signatures[1:])))
            maximum_repeats.append(max(collections.Counter(map(repr, signatures)).values()))
            for step in steps:
                checked_steps.append(step['route']['tests'])
                delta = step['stableOnlyEstimate'] - step['mixedEstimate']
                if delta > 0:
                    improvements.append(delta)
                elif delta < 0:
                    deteriorations.append(-delta)
                if step['route']['tests'] == 0:
                    zero_reasons[step['route']['stopReason']] += 1
        summaries.append(dict(startingDensity=density, selected=len(checked_steps),
                              familyCounts=dict(family_counts), minFamiliesPerSequence=min(distinct),
                              maxFamiliesPerSequence=max(distinct),
                              adjacentExactSemanticRepeats=sum(repeats),
                              maxSameAbstractPackageInOneSequence=max(maximum_repeats),
                              zeroPairCheckReasons=dict(zero_reasons),
                              fixedPackageMeanGainWhenBetter=statistics.mean(improvements) if improvements else 0,
                              fixedPackageMaxLossWhenWorse=max(deteriorations, default=0)))
    report = dict(complete=True, summaries=summaries,
                  retainedFamilyCoverage=sorted({f for rs in pool for r in rs for f in reasoning.option_family_set(r)}),
                  hashes={label: hashlib.sha256(path.read_bytes()).hexdigest() for label, path in
                          {'pool': pool_path, 'traces': traces_path, 'analysis': Path(__file__)}.items()},
                  caveat='Post-hoc descriptive metrics. Greedy public-state policies and finite tie samples are not optimal solvers or human-interest measurements.')
    output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('pool', 'traces', 'output'):
        parser.add_argument(field, type=Path)
    args = parser.parse_args()
    run(args.pool, args.traces, args.output)
