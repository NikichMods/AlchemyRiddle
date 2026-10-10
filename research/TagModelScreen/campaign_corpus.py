# SPDX-License-Identifier: MPL-2.0
"""Privately rename accepted data without changing its structural identity."""
import argparse
import hashlib
import itertools
import json
import random
from pathlib import Path

from campaign_names import VERSION, reagent_names, target_names
import progression_variable_field_screen as three
import two_slot_tag_constraint_screen as two

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261010
SLOTS = ('powder', 'fluid', 'essence')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_inputs(datasets):
    ingredients = {}
    for data in datasets.values():
        local = set()
        for row in data['ingredients']:
            name = row['name']
            if name in local:
                raise ValueError('Duplicate ingredient identity')
            local.add(name)
            value = (row['type'], frozenset(row['tags']))
            if name in ingredients and ingredients[name] != value:
                raise ValueError('Cross-corpus property/type conflict')
            ingredients[name] = value
        for formula in data['formulas']:
            if any(formula[s] not in local for s in SLOTS if s in formula):
                raise ValueError('Formula references missing identity')
    return ingredients


def build(datasets, seed=SEED):
    ingredients = validate_inputs(datasets)
    identities = sorted(ingredients)
    random.Random(seed).shuffle(identities)
    ingredient_ids = {name: f'r{i+1:03}' for i, name in enumerate(identities)}
    outputs = sorted({f['output'] for d in datasets.values() for f in d['formulas']})
    random.Random(seed + 1).shuffle(outputs)
    output_ids = {name: f't{i+1:03}' for i, name in enumerate(outputs)}
    records = [dict(id=ingredient_ids[name], type=kind, tags=sorted(tags))
               for name, (kind, tags) in ingredients.items()]
    names = reagent_names(records, seed + 2)
    titles = target_names(output_ids.values(), seed + 3)
    for row in records:
        row['name'] = names[row['id']]
    transformed = {}
    formula_records = []
    for kind, data in datasets.items():
        formulas = []
        for f in data['formulas']:
            renamed = {'output': output_ids[f['output']]}
            renamed.update({s: ingredient_ids[f[s]] for s in SLOTS if s in f})
            formulas.append(renamed)
            if kind != 'core-2':
                formula_records.append(dict(arity=len(renamed)-1, **renamed))
        transformed[kind] = dict(ingredients=[dict(name=r['id'], type=r['type'], tags=r['tags'])
                                            for r in sorted(records, key=lambda r: r['id'])],
                                 formulas=formulas)
    core = {tuple(f[s] for s in ('output', 'powder', 'fluid'))
            for f in transformed['core-2']['formulas']}
    ordinary = {tuple(f[s] for s in ('output', 'powder', 'fluid'))
                for f in transformed['ordinary-2']['formulas']}
    if not core <= ordinary:
        raise ValueError('Core formulas are not a subset of ordinary two-slot data')
    pf = {(f['powder'], f['fluid']) for f in transformed['ordinary-3']['formulas']}
    fe = {(f['fluid'], f['essence']) for f in transformed['ordinary-3']['formulas']}
    manifest = dict(version=1, namingVersion=VERSION, seed=seed,
                    ingredients=sorted(records, key=lambda r: r['id']),
                    targets=[dict(id=i, name=titles[i]) for i in sorted(titles)],
                    formulas=sorted(formula_records, key=lambda f: (f['arity'], f['output'], f['powder'], f['fluid'], f.get('essence', ''))),
                    coreTwoSlot=[list(f) for f in sorted(core)],
                    optionalTwoSlot=[list(f) for f in sorted(ordinary-core)],
                    stablePF=[list(e) for e in sorted(pf)], stableFE=[list(e) for e in sorted(fe)])
    mapping = dict(ingredients=ingredient_ids, outputs=output_ids)
    verify(datasets, transformed, mapping, manifest)
    return manifest, transformed, mapping


def verify(datasets, transformed, mapping, manifest):
    for kind, source in datasets.items():
        got = transformed[kind]
        expected = sorted((mapping['outputs'][f['output']],
                           *(mapping['ingredients'][f[s]] for s in SLOTS if s in f))
                          for f in source['formulas'])
        actual = sorted((f['output'], *(f[s] for s in SLOTS if s in f)) for f in got['formulas'])
        if expected != actual:
            raise ValueError('Formula structure changed')
        a = {mapping['ingredients'][r['name']]: (r['type'], sorted(r['tags'])) for r in source['ingredients']}
        b = {r['name']: (r['type'], sorted(r['tags'])) for r in got['ingredients']}
        if a != b:
            raise ValueError('Ingredient semantics changed')
    if len(set(mapping['ingredients'].values())) != len(mapping['ingredients']):
        raise ValueError('Ingredient mapping is not injective')
    if len(set(mapping['outputs'].values())) != len(mapping['outputs']):
        raise ValueError('Output mapping is not injective')
    names = [r['name'] for r in manifest['ingredients']] + [r['name'] for r in manifest['targets']]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate display name')
    three_rows = transformed['ordinary-3']['formulas']
    for key, a, b in (('stablePF', 'powder', 'fluid'), ('stableFE', 'fluid', 'essence')):
        if {tuple(e) for e in manifest[key]} != {(f[a], f[b]) for f in three_rows}:
            raise ValueError('Relation graph changed')


def run(source_root, private_dir, public_path):
    if private_dir.resolve().is_relative_to(ROOT) or private_dir.exists() or public_path.exists():
        raise ValueError('Private output outside Git; evidence must not be overwritten')
    paths = {k: source_root / (k + '.json') for k in ('ordinary-2', 'core-2', 'ordinary-3')}
    data = {k: json.loads(p.read_text(encoding='utf-8')) for k, p in paths.items()}
    two.assert_baseline(data['ordinary-2'])
    three.assert_accepted_baseline(three.load_model(paths['ordinary-3']))
    if len(data['core-2']['formulas']) != 16:
        raise ValueError('Unexpected core two-slot baseline')
    manifest, renamed, mapping = build(data)
    private_dir.mkdir(parents=True)
    for k, d in renamed.items():
        (private_dir / (k + '.json')).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
    for k, d in (('manifest', manifest), ('reverse-mapping', mapping)):
        (private_dir / (k + '.json')).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
    model = three.load_model(private_dir / 'ordinary-3.json')
    three.assert_accepted_baseline(model)
    chains = sum((p, f) in model.stable_pf and (f, e) in model.stable_fe
                 for p, f, e in itertools.product(model.powders, model.fluids, model.essences))
    report = dict(complete=True, exactStructureVerified=True, namingVersion=VERSION,
                  ingredients=len(manifest['ingredients']), targets=len(manifest['targets']),
                  formulas=len(manifest['formulas']), coreTwoSlot=len(manifest['coreTwoSlot']),
                  optionalTwoSlot=len(manifest['optionalTwoSlot']), threeSlot=len(model.formulas),
                  stablePF=len(model.stable_pf), stableFE=len(model.stable_fe), compatibleChains=chains,
                  sourceHashes={k: sha(p) for k, p in paths.items()},
                  artifactHashes={p.name: sha(p) for p in sorted(private_dir.glob('*.json'))},
                  caveat='Private renamed real corpus, not perfect anti-recognition protection or a playable campaign.')
    public_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ('source_root', 'private_dir', 'public_path'):
        parser.add_argument(field, type=Path)
    args = parser.parse_args()
    run(args.source_root, args.private_dir, args.public_path)
