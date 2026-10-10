# SPDX-License-Identifier: MPL-2.0
"""Prepare a private, bounded browser slice; select with actual earned knowledge.

No proprietary input or frozen bank belongs in Git. Curriculum filters are
declared below; the existing validity gates and three-slot weights are reused.
"""
import argparse
import copy
import hashlib
import itertools
import json
import random
import sys
import time
from pathlib import Path

import two_slot_tag_constraint_screen as two
import curriculum_serviceability_screen as curriculum
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
import generator_route_ranking as ranking
import bounded_quality_diagnostic as bounded
from rare_search_selection import verify_row
from campaign_sequence_screen import estimate, freeze_json
from prepare_corpus_contrast import convert, SLOTS
from prepare_real_case import TAGS


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def two_convert(c):
    if c[0] == 'literal':
        return dict(kind='exactly', count=int(c[3]), terms=[dict(slot=SLOTS['PF'.index(c[1])], tag=TAGS[c[2]])])
    if c[0] == 'count':
        return dict(kind='exactly', count=c[2], terms=[dict(slot=s, tag=TAGS[c[1]]) for s in SLOTS[:2]])
    raise ValueError('Slice two-slot grammar is presence/absence/count only')


def fixture(manifest, formula, row, arity):
    records = {r['id']: r for r in manifest['ingredients']}
    cards = []
    mapping = {}
    for slot, label, surface in zip(SLOTS, ('Порошок', 'Жидкость', 'Эссенция'), row['surface']):
        order = list(surface)
        random.Random(int(digest([slot, row['surface']])[:12], 16)).shuffle(order)
        entries = []
        for item in order:
            identifier = slot + '-' + item
            mapping[(slot, item)] = identifier
            entries.append(dict(id=identifier, globalId=item, name=records[item]['name'], tags=[TAGS[t] for t in records[item]['tags']]))
        cards.append(dict(id=slot, name=label, cards=entries))
    f = dict(title='', description='', slots=cards, propertyVocabulary=list(TAGS.values()),
             clues=[two_convert(c) if arity == 2 else convert(c) for c in row['clues']],
             science=20, submissionCost=5, economy=dict(mode='sharedScience', refillAmount=10),
             researchSupport=dict(version=1), answer={s: mapping[(s, formula[s])] for s in SLOTS[:arity]})
    if arity == 3:
        stable = []
        for i, key in enumerate(('stablePF', 'stableFE')):
            for a, b in manifest[key]:
                if (SLOTS[i], a) in mapping and (SLOTS[i+1], b) in mapping:
                    stable.append(mapping[(SLOTS[i], a)] + ':' + mapping[(SLOTS[i+1], b)])
        f.update(pairTestCost=2, knownRelations=[], compatibility=dict(stablePairs=sorted(stable)))
    return f


def prepare(corpus_dir, pool_path, output, report_path):
    root = Path(__file__).resolve().parents[2]
    if output.exists() or report_path.exists() or output.resolve().is_relative_to(root):
        raise ValueError('Private immutable bank must be new and outside Git')
    manifest = json.loads((corpus_dir/'manifest.json').read_text(encoding='utf-8'))
    m2 = two.Model(json.loads((corpus_dir/'core-2.json').read_text()))
    m3 = three.load_model(corpus_dir/'ordinary-3.json')
    data = json.loads(pool_path.read_text())
    formulas3 = sorted(m3.formulas, key=lambda f: (f.output, f.triple))
    bank = []
    counts = {}
    for formula in sorted(m2.formulas, key=lambda f: (f['output'], f['powder'], f['fluid'])):
        target = (formula['powder'], formula['fluid'])
        rows = []
        # Exhaustive small 2x2 fields; no generator threshold changes.
        for p in m2.powders:
            for g in m2.fluids:
                if p == target[0] or g == target[1]:
                    continue
                surface = ((target[0], p), (target[1], g))
                mask = m2.surface_mask(*surface)
                valid = [v for v in curriculum.two_valid_clues(m2, target, mask) if v[0][0] in ('literal', 'count')]
                for combo in itertools.combinations(valid, 2):
                    if curriculum.unique_and_necessary([v[1] for v in combo], 4):
                        row = dict(surface=surface, clues=[v[0] for v in combo])
                        rows.append(row)
        random.Random(20261010 + len(bank)).shuffle(rows)
        # Keep several fields/semantic packages rather than one assigned puzzle.
        for row in rows[:12]:
            f = fixture(manifest, formula, row, 2)
            bank.append(dict(id='pkg-'+digest(f)[:20], arity=2, output=formula['output'],
                             targetKey=digest(formula), fixture=f, row=row, envelope='compact'))
        counts[digest(formula)] = len(rows[:12])
    for ti, rows in enumerate(data['pool']):
        formula = dict(output=formulas3[ti].output, **dict(zip(SLOTS, formulas3[ti].triple)))
        for raw in rows:
            row = copy.deepcopy(raw)
            row['triples'] = list(map(tuple, row['triples']))
            verify_row(m3, row, formulas3[ti].triple)
            f = fixture(manifest, formula, row, 3)
            roots = {reasoning.family_root(v) for v in row['families']}
            compact = len(row['clues']) == 2 and roots <= {'literal', 'count'}
            bank.append(dict(id='pkg-'+digest(f)[:20], arity=3, output=formula['output'],
                             targetKey=digest(formula), fixture=f, row=row,
                             envelope='compact' if compact else 'mature'))
    compact_outputs2 = sorted({b['output'] for b in bank if b['arity'] == 2})
    compact_outputs3 = sorted({b['output'] for b in bank if b['arity'] == 3 and b['envelope'] == 'compact'})
    if len(compact_outputs2) < 2 or len(compact_outputs3) < 2:
        raise ValueError('Insufficient early targets: do not relax gates')
    # Existing 3x3x3 bank has only one simple package for some early outputs.
    # Offline extension: at most 32 fields and 512 proposals per field/variant,
    # retaining at most 12 extra packages with exactly the same option gates.
    for fi, original in enumerate(formulas3):
        if original.output not in compact_outputs3[:2]:
            continue
        retained = 0
        for si, surface in enumerate(reasoning.sampled_surfaces(m3, original.triple, 32, random.Random(20261011+fi))):
            raw, triples, target_index = reasoning.generate_true_weak_clues(m3, m3.tags, original.triple, surface)
            simple = [i for i,c in enumerate(raw) if c[0] in ('literal','count')]
            full = (1 << len(triples))-1
            compatible = sum(1<<i for i,t in enumerate(triples) if all(reasoning.stable_relation(m3,e) for e in bounded.edges(t)))
            for combo in list(itertools.combinations(simple, 2))[:512]:
                if compatible.bit_count() < 3:
                    break
                masks = [raw[i][3] for i in combo]
                live = bounded.intersects(masks, full)
                if live & compatible != 1<<target_index or any((m & compatible).bit_count()<=1 for m in masks):
                    continue
                row = reasoning.option_from_combo(m3, raw, combo, triples, target_index)
                if row is None:
                    continue
                structure = bounded.summarize_package([(c[0],c[2],c[3]) for c in raw], combo, triples, m3.tags)
                if structure['controlProxy'] or structure['immediatelyHandedAntecedents']:
                    continue
                row.update(surface=surface, triples=[t for i,t in enumerate(triples) if live>>i&1], clues=[raw[i][2] for i in combo], structure=structure)
                verify_row(m3, row, original.triple)
                formula = dict(output=original.output, **dict(zip(SLOTS,original.triple)))
                f = fixture(manifest, formula, row, 3)
                pid = 'pkg-'+digest(f)[:20]
                if any(b['id']==pid for b in bank):
                    continue
                bank.append(dict(id=pid, arity=3, output=formula['output'], targetKey=digest(formula), fixture=f, row=row, envelope='compact'))
                retained += 1
                if retained == 12:
                    break
            if retained == 12:
                break
    # An authored demand route, not an asserted typical vanilla chronology.
    titles = ('Микстура для затяжного недомогания', 'Бальзам от дорожных ушибов',
              'Препарат для сохранения тканей', 'Раствор для восстановительных работ',
              'Эликсир спокойного сна')
    outputs = [*compact_outputs2[:2], *compact_outputs3[:2]]
    late_options = [b for b in bank if b['arity'] == 3 and b['output'] not in outputs and len(b['row']['clues']) == 3 and len(set(map(reasoning.family_root, b['row']['families']))) >= 2]
    if not late_options:
        raise ValueError('No mature three-clause target')
    outputs.append(sorted({b['output'] for b in late_options})[0])
    stages = []
    purposes = ('Первое исследование: свойства перечислены полностью; все условия действуют вместе.',
                'Нужен новый состав. Примените сведения о свойствах самостоятельно.',
                'После открытия трёхслотовой лаборатории: исследуйте соседние пары. Неудачный опыт тоже даёт знание.',
                'Новая задача мастерской. Совместимые пары необходимы, но смесь должна подходить и под сведения о составе.',
                'Отдельный зрелый сценарий: исходные сведения заданы явно, а не заработаны вашим профилем.')
    for i, (out, title, purpose) in enumerate(zip(outputs, titles, purposes)):
        stages.append(dict(id=f'slice-{i+1}', arity=2 if i < 2 else 3, rung=i+1 if i < 2 else i-1 if i < 4 else 7,
                           output=out, title=title, purpose=purpose, band='Лёгкая' if i < 4 else 'Максимальная',
                           envelope='compact' if i < 4 else 'mature', separate=i == 4))
    # New editorial identity; frozen v1 naming assignments are untouched.
    revised = copy.deepcopy(manifest)
    revised['namingVersion'] = 2
    for stage in stages:
        next(t for t in revised['targets'] if t['id'] == stage['output'])['name'] = stage['title']
    all_edges = sorted([('PF', p, g) for p, g in itertools.product(m3.powders, m3.fluids)] +
                       [('FE', g, e) for g, e in itertools.product(m3.fluids, m3.essences)])
    seeded = random.Random(20261010).sample(all_edges, 34)
    checkpoint = [dict(edge=e, stable=reasoning.stable_relation(m3, e), source='seeded:mature-v1') for e in seeded]
    world_id = 'world-'+digest(revised)
    payload = dict(version=1, id='campaign-browser-slice-v1', worldId=world_id,
                   namingVersion=2, sourceManifestHash=ranking.sha(corpus_dir/'manifest.json'),
                   manifest=revised, packages=bank, stages=stages, checkpoint=checkpoint)
    # Bounded feasibility through fresh/mixed/all-known states, including shortcuts.
    checks = []
    deadline = time.monotonic()+180
    for stage in stages:
        eligible = [b for b in bank if b['arity'] == stage['arity'] and b['output'] == stage['output'] and
                    (b['envelope'] == 'compact' if stage['envelope'] == 'compact' else len(b['row']['clues']) == 3)]
        if not eligible:
            raise ValueError('Empty curriculum pool')
        routes = []
        if stage['arity'] == 3:
            for density in (0, 34, len(all_edges)):
                priors = {e: reasoning.stable_relation(m3, e) for e in seeded[:density]} if density < len(all_edges) else {e: reasoning.stable_relation(m3, e) for e in all_edges}
                means = [estimate(b['row'], priors, lambda e: reasoning.stable_relation(m3, e), deadline)['mean'] for b in eligible]
                routes.append(dict(observations=len(priors), minimum=min(means), maximum=max(means)))
        checks.append(dict(stage=stage['id'], arity=stage['arity'], packages=len(eligible), routes=routes))
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    report = dict(version=1, bankHash=ranking.sha(output), worldId=world_id,
                  sourceManifestHash=payload['sourceManifestHash'], sourcePoolHash=ranking.sha(pool_path),
                  twoSlotPackages=sum(b['arity']==2 for b in bank), threeSlotPackages=sum(b['arity']==3 for b in bank),
                  twoSlotVariantsServed=sum(n>0 for n in counts.values()), twoSlotUnserved=sum(n==0 for n in counts.values()),
                  checks=checks, gates='Unchanged two-slot compact weakness + unique/necessary; imported three-slot rows independently verified.',
                  limits='Authored lab demand; human learning/bands unmeasured; no arbitrary-state completeness claim.')
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


def select(bank_path, request):
    data = json.loads(bank_path.read_text(encoding='utf-8'))
    stage = next(s for s in data['stages'] if s['id'] == request['stage'])
    solved = set(request.get('solved', []))
    rows = [b for b in data['packages'] if b['arity']==stage['arity'] and b['output']==stage['output'] and b['targetKey'] not in solved and
            (b['envelope']=='compact' if stage['envelope']=='compact' else len(b['row']['clues'])==3)]
    if not rows:
        return dict(status='known_target' if any(b['output']==stage['output'] and b['targetKey'] in solved for b in data['packages']) else 'empty_suitable_pool')
    rng = random.Random(request['seed'])
    recent = request.get('recent', [])
    if stage['arity']==2:
        # No new two-slot ranking weights: uniform within prepared envelope.
        available = [b for b in rows if b['id'] not in recent[-2:]] or rows
        chosen = rng.choice(available)
        route = None
    else:
        priors = {}
        for fact in request.get('knowledge', []):
            if type(fact['stable']) is not bool:
                raise ValueError('Nonboolean knowledge')
            edge = tuple(fact['edge'])
            if edge in priors and priors[edge] != fact['stable']:
                raise ValueError('Contradictory knowledge')
            priors[edge] = fact['stable']
        pf, fe = set(map(tuple, data['manifest']['stablePF'])), set(map(tuple, data['manifest']['stableFE']))
        oracle = lambda e: (e[1], e[2]) in (pf if e[0]=='PF' else fe)
        if any(oracle(e)!=v for e,v in priors.items()):
            raise ValueError('Knowledge/world conflict')
        prior_rows = [copy.deepcopy(b['row']) for pid in recent for b in data['packages'] if b['id']==pid and b['arity']==3]
        for row in prior_rows:
            row['semantics'] = freeze_json(row['semantics'])
        candidates = []
        deadline = time.monotonic()+30
        for b in rows:
            row = copy.deepcopy(b['row'])
            row['triples'] = list(map(tuple,row['triples']))
            row['semantics'] = freeze_json(row['semantics'])
            relevant = {e for t in row['triples'] for e in bounded.edges(t)}
            route = estimate(row, {e:v for e,v in priors.items() if e in relevant}, oracle, deadline)
            row['route'] = [route]
            score = ranking.selection_score(row, prior_rows, len(prior_rows), .25, 3, 0)
            candidates.append((score, b, route))
        best = min(c[0] for c in candidates)
        _, chosen, route = rng.choice([c for c in candidates if abs(c[0]-best)<1e-10])
    f = copy.deepcopy(chosen['fixture'])
    f.update(id=f"{stage['id']}:{chosen['id']}:{request['seed']}", title=stage['title'], description=stage['purpose'])
    return dict(status='selected', fixture=f, packageId=chosen['id'], targetKey=chosen['targetKey'], route=route)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('prepare','select'))
    parser.add_argument('paths', nargs='+', type=Path)
    args = parser.parse_args()
    if args.mode=='prepare':
        prepare(*args.paths)
    else:
        print(json.dumps(select(args.paths[0], json.load(sys.stdin)), ensure_ascii=False))
