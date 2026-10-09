"""Main-path identity check against the already tested reserve-64 pool."""
import argparse
import hashlib
import json
from pathlib import Path
from unittest.mock import patch

import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from rare_search_selection import verify_row


def identity(row):
    return json.dumps({k: row[k] for k in ('surface', 'clues')}, sort_keys=True)


def run(corpus, reference, adopted, public):
    if public.exists():
        raise ValueError('Completed evidence is immutable')
    previous = json.loads(reference.read_text())
    current = json.loads(adopted.read_text())
    expected = next(r['pool'] for r in previous['pools'] if r['repeat'] == 0 and r['reserve'] == 64)
    assert [[identity(r) for r in rows] for rows in current['pool']] == [[identity(r) for r in rows] for rows in expected]
    assert current['knowledge'] == previous['knowledge']
    model = three.load_model(corpus)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    verified = 0
    for ti, rows in enumerate(current['pool']):
        for row, old in zip(rows, expected[ti]):
            row['triples'] = list(map(tuple, row['triples']))
            verify_row(model, row, formulas[ti].triple)
            assert row['route'] == old['route']
            assert row['validation'] == old['validation']
            verified += 1
    selections = {(r['context'], r['preferred'], r['order']): r['records']
                  for r in previous['selections'] if r['repeat'] == 0 and r['reserve'] == 64}
    compared = 0
    for result in current['selection']:
        if result['strength'] != .25:
            continue
        for order, records in enumerate(result['additive']):
            assert records == selections[result['context'], result['preferred'], order]
            compared += 1
    # Exercise the other main caller with real corpus inputs, recording budgets
    # rather than adding a synthetic substitute for its unchanged option gates.
    with patch.object(reasoning, 'rare_package_proposals', wraps=reasoning.rare_package_proposals) as probe:
        options = reasoning.build_options(model, model.tags, 2, 512, 20261007)
    assert probe.call_count > 0
    assert all(call.kwargs['reserve'] == 64 and call.kwargs['budget'] == 512
               and call.args[1] is None for call in probe.call_args_list)
    report = dict(complete=True, exactOrderedPoolMatch=True, exactKnowledgeMatch=True,
                  exactRouteAndHeldOutMatch=True, verifiedPackages=verified,
                  exactDefaultSelectionSequences=compared,
                  capacityBuilder=dict(fieldsInvoked=probe.call_count, budget=512, reserve=64,
                                       optionCount=sum(map(len, options))),
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                          (corpus, reference, adopted, Path(__file__))},
                  caveat='Exact match to tested repeat 0, not a promise of rare retention in every random run.')
    public.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'reference', 'adopted', 'public'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.reference, args.adopted, args.public)
