"""Bounded paired corpus screen; public aggregates, private exact witnesses."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import random
import time
from pathlib import Path

import bounded_quality_diagnostic as quality
from field_feasibility import supports_necessary_clues
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning

ROOT = Path(__file__).resolve().parents[2]
NEW = {'shared', 'count_mixed'}
SEED = 20261009
CORPUS_SHA256 = '92e140826b6b8c857bb994df71b5db83d3da2ed15a9cc4665db474ea8876ea20'


def admissible(model, raw, combo, triples, target_index, compatible):
    full = (1 << len(triples)) - 1
    if not supports_necessary_clues(compatible.bit_count(), len(combo)):
        return None, 'fieldFloor'
    masks = [raw[i][3] for i in combo]
    live = quality.intersects(masks, full)
    if live & compatible != 1 << target_index:
        return None, 'completeAnswer'
    if any((quality.intersects([m for j, m in enumerate(masks) if j != drop], full)
            & compatible).bit_count() <= 1 for drop in range(len(combo))):
        return None, 'necessity'
    row = reasoning.option_from_combo(model, raw, combo, triples, target_index)
    if row is None:
        return None, 'existingOptionGates'
    structure = quality.summarize_package([(c[0], c[2], c[3]) for c in raw],
                                          combo, triples, model.tags)
    if structure['controlProxy'] or structure['immediatelyHandedAntecedents']:
        return None, 'ordinaryQuality'
    return dict(families=row['families'], clues=[raw[i][2] for i in combo],
                masks=masks, structure=structure), 'eligible'


def family_groups(clues):
    groups = defaultdict(list)
    for i, clue in enumerate(clues):
        groups[reasoning.family_root(clue[0])].append(i)
    return dict(sorted(groups.items()))


def draw_family_first(groups, k, rng):
    """Uniform available root family, then uniform unused predicate; repeats allowed."""
    chosen = []
    for _ in range(k):
        available = [(family, [i for i in ids if i not in chosen])
                     for family, ids in groups.items()]
        available = [(family, ids) for family, ids in available if ids]
        if not available:
            raise ValueError('Not enough distinct predicates')
        _, ids = rng.choice(available)
        chosen.append(rng.choice(ids))
    return tuple(sorted(chosen))


def run(corpus, private, public, family_first=False, draw_offset=0):
    if private.resolve().is_relative_to(ROOT) or private.exists() or public.exists():
        raise ValueError('Private identities must remain outside Git; never overwrite a pass')
    started = time.monotonic()
    if hashlib.sha256(corpus.read_bytes()).hexdigest() != CORPUS_SHA256:
        raise ValueError('Input does not match the accepted corpus identity')
    model = three.load_model(corpus)
    three.assert_accepted_baseline(model)
    arms = ('baseline', 'expanded', 'family_first') if family_first else (
        'baseline', 'expanded', 'targeted_shared', 'targeted_count_mixed')
    counters = {arm: Counter() for arm in arms}
    targets = {arm: set() for arm in counters}
    fields_hit = {arm: set() for arm in counters}
    family_packages = {arm: Counter() for arm in counters}
    records = []
    clue_fields = Counter()
    clue_counts = Counter()
    for ti, formula in enumerate(sorted(model.formulas, key=lambda f: (f.output, f.triple))):
        surfaces = reasoning.sampled_surfaces(model, formula.triple, 8, random.Random(SEED + ti))
        for fi, surface in enumerate(surfaces):
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, formula.triple, surface)
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in quality.edges(t)))
            for family in NEW:
                amount = sum(c[0] == family for c in raw)
                clue_counts[family] += amount
                clue_fields[family] += bool(amount)
            pools = {'baseline': [c for c in raw if c[0] not in NEW], 'expanded': raw,
                     'targeted_shared': raw, 'targeted_count_mixed': raw}
            if family_first:
                pools = {'baseline': pools['baseline'], 'expanded': raw, 'family_first': raw}
            for arm, clues in pools.items():
                rng = random.Random(SEED + ti * 100 + fi + draw_offset)
                budget = 256 if arm.startswith('targeted_') else 512
                groups = family_groups(clues) if arm == 'family_first' else None
                anchor = arm.removeprefix('targeted_') if arm.startswith('targeted_') else None
                anchors = [i for i, c in enumerate(clues) if c[0] == anchor] if anchor else []
                if anchor and not anchors:
                    continue
                seen = set()
                for _ in range(budget):
                    if time.monotonic() - started > 180:
                        raise RuntimeError('Three-minute cap exceeded; no complete result')
                    counters[arm]['attempts'] += 1
                    k = rng.choice((2, 3))
                    if len(clues) < k:
                        counters[arm]['insufficientClues'] += 1
                        continue
                    if groups is not None:
                        combo = draw_family_first(groups, k, rng)
                    elif anchor:
                        a = rng.choice(anchors)
                        combo = tuple(sorted([a] + rng.sample([i for i in range(len(clues)) if i != a], k - 1)))
                    else:
                        combo = tuple(sorted(rng.sample(range(len(clues)), k)))
                    if combo in seen:
                        counters[arm]['duplicateDraw'] += 1
                        continue
                    seen.add(combo)
                    row, verdict = admissible(model, clues, combo, triples, target_index, compatible)
                    counters[arm][verdict] += 1
                    if row is None:
                        continue
                    targets[arm].add(ti)
                    fields_hit[arm].add((ti, fi))
                    family_packages[arm].update(set(reasoning.family_root(f) for f in row['families']))
                    records.append(dict(arm=arm, target=ti, field=fi, surface=surface, **row))
    report = dict(complete=True, seed=SEED, drawOffset=draw_offset, familyFirstComparison=family_first,
                  targets=len(model.formulas), fields=len(model.formulas) * 8,
                  seconds=round(time.monotonic() - started, 3),
                  inputSha256=hashlib.sha256(corpus.read_bytes()).hexdigest(),
                  sourceSha256={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in
                                (Path(__file__), Path(reasoning.__file__), Path(quality.__file__))},
                  budgets=dict(pairedPerFieldPerArm=512, targetedPerAvailableFamilyField=256, seconds=180),
                  availableNewClues=dict(clue_counts), fieldsWithNewClues=dict(clue_fields),
                  arms={arm: dict(counters=dict(counters[arm]), coveredTargets=len(targets[arm]),
                                 coveredFields=len(fields_hit[arm]), familyPackages=dict(family_packages[arm]))
                        for arm in counters},
                  baselinePlusNewCoveredTargets=len(set.union(*targets.values())),
                  caveat='Paired arms have equal attempts, not identical packages. Targeted arms have extra effort; '
                         'they prove sampled reserve, not equal-effort improvement or human interest.')
    private.write_text(json.dumps(dict(report=report, witnesses=records), indent=2), encoding='utf-8')
    public.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('corpus', 'private', 'public'):
        parser.add_argument(name, type=Path)
    parser.add_argument('--family-first', action='store_true')
    parser.add_argument('--draw-offset', type=int, default=0)
    args = parser.parse_args()
    run(args.corpus, args.private, args.public, args.family_first, args.draw_offset)
