"""Independent frozen-spec replay of rare-search witnesses, without builder masks."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import bounded_quality_diagnostic as quality
from intra_package_review import holds
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning


def run(corpus, private, public):
    if public.exists():
        raise ValueError('Completed evidence is immutable')
    model = three.load_model(corpus)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    records = json.loads(private.read_text())['witnesses']
    identities = set()
    for row in records:
        triples = list(itertools.product(*row['surface']))
        masks = [{t for t in triples if holds(c, t, model.tags)} for c in row['clues']]
        integers = [sum(1 << i for i, t in enumerate(triples) if t in mask) for mask in masks]
        assert integers == row['masks']
        live = set.intersection(*masks)
        compatible = {t for t in triples if all(reasoning.stable_relation(model, e) for e in quality.edges(t))}
        assert live & compatible == {formulas[row['target']].triple}
        assert all(len(set.intersection(*(m for j, m in enumerate(masks) if j != i)) & compatible) > 1
                   for i in range(len(masks)))
        identities.add(json.dumps({k: row[k] for k in ('target', 'surface', 'clues')}, sort_keys=True))
    result = dict(complete=True, replayedRecords=len(records), distinctPackages=len(identities),
                  checks=['predicate masks', 'unique complete-model target', 'each clue necessary'],
                  hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (corpus, private, Path(__file__))})
    public.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'private', 'public'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.corpus, args.private, args.public)
