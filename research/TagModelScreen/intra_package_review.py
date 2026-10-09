"""Static review of frozen packages; no recipe identities in public output."""
import argparse
import collections
import hashlib
import itertools
import json
import random
import statistics
import time
from pathlib import Path

import generator_route_ranking as ranking
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from field_feasibility import supports_necessary_clues


def terms(spec):
    kind = spec[0]
    if kind == 'literal':
        return [(('P', 'F', 'E').index(spec[1]), spec[2])]
    if kind == 'count':
        return [(i, spec[1]) for i in range(3)]
    if kind == 'count_mixed':
        return list(enumerate(spec[1]))
    if kind == 'shared':
        # No fixed named-property assertions; effective scope comes from masks.
        return []
    return [(spec[1], spec[2]), (spec[3], spec[4])]


def holds(spec, triple, tags):
    kind = spec[0]
    if kind == 'shared':
        return bool(set.intersection(*(set(tags[item]) for item in triple)))
    values = [tag in tags[triple[slot]] for slot, tag in terms(spec)]
    if kind == 'literal':
        return values[0] == spec[3]
    if kind in ('count', 'count_mixed'):
        return sum(values) == spec[2]
    if kind == 'xor':
        return values[0] != values[1]
    if kind.startswith('imp_pos'):
        return not values[0] or values[1]
    if kind.startswith('imp_neg'):
        return not values[0] or not values[1]
    raise ValueError('Unknown frozen clue kind')


def describe(row, target, model, gap=False):
    all_triples = list(itertools.product(*row['surface']))
    masks = [{t for t in all_triples if holds(c, t, model.tags)} for c in row['clues']]
    live = set.intersection(*masks)
    assert live == set(map(tuple, row['triples']))
    compatible = {t for t in all_triples if all(reasoning.stable_relation(model, e)
                  for e in ranking.bounded.edges(t))}
    assert live & compatible == {tuple(target)}
    assert supports_necessary_clues(len(compatible), len(masks))
    forgotten = [set.intersection(*(m for j, m in enumerate(masks) if i != j))
                 for i in range(len(masks))]
    assert all(len(m & compatible) > 1 for m in forgotten)
    roots = [reasoning.family_root(c[0]) for c in row['clues']]
    repeated = sum(n*(n-1)//2 for n in collections.Counter(roots).values())
    same_tag = sum(len(terms(c)) == 2 and terms(c)[0][1] == terms(c)[1][1]
                   for c in row['clues'])
    atoms = [set(terms(c)) for c in row['clues']]
    shared_atoms = sum(len(a & b) for a, b in itertools.combinations(atoms, 2))
    dead_branches = max_width = 0
    for slot, cards in enumerate(row['surface']):
        for card in cards:
            valid_count = sum(t[slot] == card for t in live)
            max_width = max(max_width, valid_count)
            if not valid_count and all(any(t[slot] == card for t in m) for m in masks):
                dead_branches += 1
    held = row['route'][1] if gap else row['validation'][0]
    return dict(clues=len(masks), distinctOperators=len(set(roots)),
                doubleSymmetricXor=(len(row['clues']) == 2 and all(
                    c[0] == 'xor' and c[2] == c[4] for c in row['clues'])),
                repeatedOperatorPairs=repeated, sameTagBinaryClauses=same_tag,
                sharedPredicateOccurrences=shared_atoms, tagValid=len(live),
                maxBranchWidth=max_width, crossClueDeadBranches=dead_branches,
                maxForgottenClueExtra=max(len(m-live) for m in forgotten),
                meanForgottenClueExtra=statistics.mean(len(m-live) for m in forgotten),
                selectionMean=row['route'][0]['mean'], heldOutMean=held['mean'])


def summarize(rows):
    fields = ('heldOutMean', 'tagValid', 'maxBranchWidth', 'crossClueDeadBranches',
              'maxForgottenClueExtra', 'meanForgottenClueExtra')
    return dict(count=len(rows), means={k: round(statistics.mean(r[k] for r in rows), 4)
                                      for k in fields} if rows else {})


def run(corpus, original, gap, output):
    started = time.monotonic()
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    source = json.loads(original.read_text(encoding='utf-8'))
    extension = json.loads(gap.read_text(encoding='utf-8'))
    assert sum(map(len, source['pool'])) + len(extension['candidates']) <= 240
    groups = []
    for target, rows in zip(source['targets'], source['pool']):
        groups.append([describe(r, target, model) for r in rows])
    gap_descriptions = [describe(r, extension['target'], model, True)
                        for r in extension['candidates']]
    groups.append(gap_descriptions)
    all_rows = [r for group in groups for r in group]
    assert time.monotonic() - started < 60
    scores = [ranking.baseline_score(r, [], 0) + .25*ranking.length_penalty(r['route'][0]['mean'], 3)
              for r in extension['candidates']]
    chosen = random.Random(20301013).choice([i for i, v in enumerate(scores) if v == min(scores)])
    reference = gap_descriptions[chosen]
    def near(r, ref):
        return 2 <= r['heldOutMean'] <= 5 and abs(r['heldOutMean']-ref['heldOutMean']) <= 1
    varied = [i for i, r in enumerate(gap_descriptions)
              if r['distinctOperators'] >= 2 and near(r, reference)]
    same_field = [i for i in varied if extension['candidates'][i]['surface']
                  == extension['candidates'][chosen]['surface']]
    two_varied = [i for i in varied if gap_descriptions[i]['clues'] == 2]
    examples = sorted(varied, key=lambda i: (gap_descriptions[i]['clues'],
        gap_descriptions[i]['repeatedOperatorPairs'],
        abs(gap_descriptions[i]['heldOutMean']-reference['heldOutMean'])))[:6]
    paired = []
    for group in groups:
        pairs = [(a,b) for a in group for b in group
                 if a['clues'] == b['clues'] and a['distinctOperators'] == 1
                 and b['distinctOperators'] >= 2 and near(b,a)]
        if pairs:
            paired.append(min(pairs, key=lambda p: abs(p[0]['heldOutMean']-p[1]['heldOutMean'])))
    report = dict(complete=True, scope='frozen eligible pool, static descriptors only',
        records=len(all_rows), targetGroupsWithCandidates=sum(bool(g) for g in groups),
        validatedGates='cached tag hypotheses, unique full answer, all omission witnesses, field floor',
        cohorts={f'{k}clues_{name}': summarize([r for r in all_rows if r['clues']==k and pred(r)])
            for k in (2,3) for name,pred in (
                ('singleOperator',lambda r:r['distinctOperators']==1),
                ('mixedOperators',lambda r:r['distinctOperators']>=2))},
        case11=dict(reference=reference, nearVaried=len(varied), nearVariedTwoClues=len(two_varied),
                    nearVariedSameField=len(same_field),
                    comparisons=[dict(sameField=i in same_field, descriptors=gap_descriptions[i]) for i in examples]),
        doubleSymmetricXor=summarize([r for r in all_rows if r['doubleSymmetricXor']]),
        matchedTargetSameClueCount=dict(groups=len(paired), repeated=summarize([a for a,b in paired]),
                                       varied=summarize([b for a,b in paired])),
        inputHashes={p.name:ranking.sha(p) for p in (corpus,original,gap)},
        sourceHash=ranking.sha(Path(__file__)), seconds=round(time.monotonic()-started,3),
        caveat='Static burden descriptors are uncalibrated; no human probability or new ranking weight.')
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus','original','gap','output'):
        parser.add_argument(name,type=Path)
    args = parser.parse_args()
    run(args.corpus,args.original,args.gap,args.output)
