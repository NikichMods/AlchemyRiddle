"""Additive route ranking over a frozen pool; exact game identities stay private."""
import argparse
import collections
import hashlib
import itertools
import json
import math
import random
import statistics
import time
from pathlib import Path

import bounded_quality_diagnostic as bounded
import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
from science_route_comparison import Investigation
from field_feasibility import supports_necessary_clues

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261007
REPETITION_STRENGTH = 0.25


def length_penalty(mean, preferred, earned=False):
    return (max(0, mean-preferred)**2 + max(0, mean-5)**2
            + 2*max(0, mean-7)**2 + (0 if earned else max(0, 2-mean)**2))


def baseline_score(row, chosen, step):
    """Same formula as reasoning.anti_clump_sequence; no route input."""
    families = reasoning.option_family_set(row)
    recent = chosen[-2:]
    family_counts = collections.Counter(f for r in chosen for f in reasoning.option_family_set(r))
    relation_counts = collections.Counter(r['relation_mode'] for r in chosen)
    third = sum(8.0 for f in families if len(recent) == 2
                and all(f in reasoning.option_family_set(r) for r in recent))
    immediate = sum(1.2 for f in families if recent and f in reasoning.option_family_set(recent[-1]))
    balance = sum(family_counts[f] for f in families)*0.12 + relation_counts[row['relation_mode']]*0.08
    semantic = 1.8*reasoning.jaccard(reasoning.option_semantic_atoms(row),
                                    reasoning.option_semantic_atoms(recent[-1])) if recent else 0
    score = third + immediate + balance + semantic
    if step % 4 == 3:
        score += 0.5*(len(row['families'])-2)
    elif step % 4 == 2:
        score += 0.5*(3-len(row['families']))
    return score


def structural_repetition(row):
    """Finite cost, never a gate; identical symmetric XORs receive extra emphasis."""
    families = [reasoning.family_root(f) for f in row['families']]
    repeated = sum(n*(n-1)//2 for n in collections.Counter(families).values())
    symmetric_xors = sum(c[0] == 'xor' and c[2] == c[4] for c in row.get('clues', []))
    return .25*repeated + .75*symmetric_xors*(symmetric_xors-1)/2


def selection_score(row, chosen, step, strength, preferred, context,
                    repetition_strength=REPETITION_STRENGTH):
    return (baseline_score(row, chosen, step) + strength*length_penalty(
        row['route'][context]['mean'], preferred,
        (row['route'][context]['observedStablePriors'] > 0
         or row['route'][context].get('observedIncompatiblePriors', 0) > 0))
        + repetition_strength*structural_repetition(row))


def select_sequence(options, order, seed, strength, preferred, context,
                    repetition_strength=REPETITION_STRENGTH):
    rng = random.Random(seed)
    chosen = []
    records = []
    for target in order:
        candidates = options[target]
        if not candidates:
            continue
        scores = [selection_score(r, chosen, len(chosen), strength, preferred, context,
                                  repetition_strength) for r in candidates]
        best = min(scores)
        index = rng.choice([i for i, s in enumerate(scores) if abs(s-best) < 1e-10])
        selected = candidates[index]
        records.append(dict(target=target, index=index,
                            oldScore=baseline_score(selected, chosen, len(chosen))))
        chosen.append(selected)
    return records


def summarize(options, records, context, route_key='route'):
    rows = [options[r['target']][r['index']] for r in records]
    if not rows:
        return dict(selected=0)
    means = [r[route_key][context]['mean'] for r in rows]
    overlaps = [reasoning.jaccard(reasoning.option_family_set(a), reasoning.option_family_set(b))
                for a, b in zip(rows, rows[1:])]
    return dict(selected=len(rows), meanPairChecks=statistics.mean(means),
                meanScience=2*statistics.mean(means)+5,
                selectedMean2To5=sum(2 <= m <= 5 for m in means)/len(means),
                selectedMeanAbove5=sum(m > 5 for m in means)/len(means),
                selectedMeanAbove7=sum(m > 7 for m in means)/len(means),
                meanLegacySelectionScore=statistics.mean(r['oldScore'] for r in records),
                meanAdjacentFamilyOverlap=statistics.mean(overlaps) if overlaps else 0,
                meanCrossSlotClauses=statistics.mean(r['structure']['crossSlotClauses'] for r in rows),
                meanDerivedAntecedents=statistics.mean(r['structure']['derivedAntecedents'] for r in rows),
                meanConstantCountTerms=statistics.mean(r['structure']['constantCountTerms'] for r in rows),
                meanUniqueConditionalEndpoints=statistics.mean(r['structure']['uniqueConditionalEndpoints'] for r in rows),
                sampledRouteAbove7=sum(r[route_key][context]['above7'] for r in rows)/len(rows),
                sampledMaximum=max(r[route_key][context]['max'] for r in rows),
                researchNotCheaperThanRandomSubmission=sum(
                    2*r[route_key][context]['mean']+5 >= (5 if r[route_key][context]['initialCertified']
                    else 5*(len(r['triples'])+1)/2) for r in rows)/len(rows))


def average_summaries(summaries):
    return {k: statistics.mean(s[k] for s in summaries) for k in summaries[0]}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(input_path, private_path, public_path):
    assert not private_path.resolve().is_relative_to(ROOT)
    if private_path.exists() or public_path.exists():
        raise ValueError('Completed research artifacts are immutable')
    start = time.monotonic()
    deadline = start + 360
    model = three.load_model(input_path)
    three.assert_accepted_baseline(model)
    formulas = sorted(model.formulas, key=lambda f: (f.output, f.triple))
    all_relations = sorted([('PF', a, b) for a, b in model.stable_pf]
                           + [('FE', a, b) for a, b in model.stable_fe])
    counters = collections.Counter()
    options = []
    knowledge = []
    def check_cap():
        if time.monotonic() > deadline:
            raise RuntimeError('predeclared six-minute cap exceeded; do not report a complete pass')
    for ti, formula in enumerate(formulas):
        rng = random.Random(SEED + 5000 + ti)
        known_four = tuple(rng.sample(all_relations, 4))
        contexts = ((), known_four[:1], known_four)
        knowledge.append(contexts)
        surfaces = reasoning.sampled_surfaces(model, formula.triple, 8, rng)
        reservoir = []
        accepted = 0
        retention_rng = random.Random(SEED + 800000 + ti)
        for fi, surface in enumerate(surfaces):
            counters['fields'] += 1
            raw, triples, target_index = reasoning.generate_true_weak_clues(model, model.tags, formula.triple, surface)
            groups = reasoning.family_groups(raw)
            full = (1 << len(triples))-1
            compatible = sum(1 << i for i, t in enumerate(triples)
                             if all(reasoning.stable_relation(model, e) for e in bounded.edges(t)))
            if not supports_necessary_clues(compatible.bit_count(), 2):
                counters['rejectFieldWitnessFloor'] += 1
                continue
            seen = set()
            if any(groups.get(f) for f in reasoning.RESEARCH_RARE_FAMILIES):
                counters['rareSearchableFields'] += 1
                counters['focusedPackageAttempts'] += reasoning.RARE_SEARCH_RESERVE
            for combo in reasoning.rare_package_proposals(groups, compatible.bit_count(),
                    SEED + ti * 100 + fi):
                check_cap()
                counters['packageAttempts'] += 1
                if combo is None:
                    counters['rejectPackageWitnessFloor'] += 1
                    continue
                k = len(combo)
                if combo in seen:
                    continue
                seen.add(combo)
                masks = [raw[i][3] for i in combo]
                live = bounded.intersects(masks, full)
                if live & compatible != 1 << target_index:
                    counters['rejectCompleteAnswer'] += 1
                    continue
                if any((bounded.intersects([m for j, m in enumerate(masks) if j != drop], full)
                        & compatible).bit_count() <= 1 for drop in range(k)):
                    counters['rejectFullModelRedundancy'] += 1
                    continue
                row = reasoning.option_from_combo(model, raw, combo, triples, target_index)
                if row is None:
                    counters['rejectExistingOptionGates'] += 1
                    continue
                converted = [(c[0], c[2], c[3]) for c in raw]
                structure = bounded.summarize_package(converted, combo, triples, model.tags)
                if structure['controlProxy'] or structure['immediatelyHandedAntecedents']:
                    counters['rejectOrdinaryRubricProxy'] += 1
                    continue
                accepted += 1
                counters['eligible'] += 1
                row.update(surface=surface, triples=[t for i, t in enumerate(triples) if live >> i & 1],
                           clues=[raw[i][2] for i in combo], structure=structure, route=[])
                if len(reservoir) < 12:
                    reservoir.append(row)
                else:
                    slot = retention_rng.randrange(accepted)
                    if slot < 12:
                        reservoir[slot] = row
        options.append(reservoir)
    print(json.dumps(dict(stage='pool frozen', candidates=[len(x) for x in options], counters=dict(counters))), flush=True)
    for ti, rows in enumerate(options):
        for row in rows:
            for contexts in knowledge[ti]:
                relevant_edges = {e for t in row['triples'] for e in bounded.edges(t)}
                priors = tuple(e for e in contexts if e in relevant_edges)
                counts = []
                for policy in ('balanced', 'candidate_first'):
                    investigator = Investigation(row['triples'], priors,
                        lambda e: reasoning.stable_relation(model, e), policy, deadline, stop_unique=True)
                    for seed in range(16):
                        check_cap()
                        replay = investigator.replay(SEED + 20000 + seed)
                        counts.append(replay['tests'])
                        counters['replays'] += 1
                row['route'].append(dict(mean=statistics.mean(counts), min=min(counts), max=max(counts),
                    above7=sum(n > 7 for n in counts)/len(counts), observedStablePriors=len(priors),
                    initialCertified=all(e in priors for e in bounded.edges(formulas[ti].triple))))
    # Held-out seeds evaluate fixed choices; they never enter candidate ranking.
    validation_deadline = time.monotonic() + 360
    for ti, rows in enumerate(options):
        for row in rows:
            row['validation'] = []
            for contexts in knowledge[ti]:
                relevant_edges = {e for t in row['triples'] for e in bounded.edges(t)}
                priors = tuple(e for e in contexts if e in relevant_edges)
                counts = []
                for policy in ('balanced', 'candidate_first'):
                    investigator = Investigation(row['triples'], priors,
                        lambda e: reasoning.stable_relation(model, e), policy, validation_deadline, stop_unique=True)
                    for seed in range(32):
                        if time.monotonic() > validation_deadline:
                            raise RuntimeError('held-out validation cap exceeded')
                        counts.append(investigator.replay(SEED+90000+seed)['tests'])
                        counters['validationReplays'] += 1
                row['validation'].append(dict(mean=statistics.mean(counts), min=min(counts), max=max(counts),
                    above7=sum(n > 7 for n in counts)/len(counts), observedStablePriors=len(priors),
                    initialCertified=all(e in priors for e in bounded.edges(formulas[ti].triple))))
    comparisons = []
    examples = []
    records_private = []
    for context in range(3):
        for preferred in (3, 5):
            baseline_records = []
            for variant in range(3):
                order = list(range(len(formulas)))
                random.Random(SEED+30000+variant).shuffle(order)
                baseline_records.append((order, select_sequence(options, order, SEED+variant, 0, preferred, context)))
            baseline = average_summaries([summarize(options, records, context) for _, records in baseline_records])
            baseline_validation = average_summaries([summarize(options, records, context, 'validation')
                                                      for _, records in baseline_records])
            for strength in (0.25, 0.5, 1, 2):
                new_records = [select_sequence(options, order, SEED+v, strength, preferred, context)
                               for v, (order, _) in enumerate(baseline_records)]
                updated = average_summaries([summarize(options, records, context) for records in new_records])
                updated_validation = average_summaries([summarize(options, records, context, 'validation')
                                                        for records in new_records])
                changed = sum(a['index'] != b['index'] for (_, old), new in zip(baseline_records, new_records)
                              for a, b in zip(old, new))
                comparisons.append(dict(knownGlobalStableRelations=(0, 1, 4)[context], preferred=preferred,
                                        strength=strength, baseline=baseline, additive=updated,
                                        heldOutBaseline=baseline_validation, heldOutAdditive=updated_validation,
                                        changedSelections=changed, selectionsCompared=sum(len(r) for r in new_records)))
                records_private.append(dict(context=context, preferred=preferred, strength=strength,
                                            baseline=[r for _, r in baseline_records], additive=new_records))
                if context == 0 and strength == 0.5:
                    for (_, old), new in zip(baseline_records, new_records):
                        for a, b in zip(old, new):
                            if a['index'] != b['index'] and len(examples) < 6:
                                x, y = options[a['target']][a['index']], options[b['target']][b['index']]
                                examples.append(dict(preferred=preferred, before=x['route'][context], after=y['route'][context],
                                                     beforeStructure=x['structure'], afterStructure=y['structure'],
                                                     oldScoreBefore=a['oldScore'], oldScoreAfter=b['oldScore']))
    public = dict(scope='19 ordinary three-slot variants; full ingredient availability; sampled fixed candidate pool',
                  complete=True, repetitionStrength=REPETITION_STRENGTH,
                  search=dict(policy='bounded rare-family pairs plus family-first',
                              budget=reasoning.PACKAGE_SEARCH_BUDGET, reserve=reasoning.RARE_SEARCH_RESERVE,
                              rareFamilies=sorted(reasoning.RESEARCH_RARE_FAMILIES)),
                  counters=dict(counters), coveredTargets=sum(bool(x) for x in options),
                  targets=len(formulas), candidatesPerTarget=[len(x) for x in options],
                  comparisons=comparisons, reviewedStructuralChanges=examples,
                  estimator=dict(policies=['balanced', 'candidate_first'], seedsPerPolicy=16,
                                 heldOutSeedsPerPolicy=32, sampled=True, stop='certified or unique public survivor'),
                  inputSha256=sha(input_path),
                  sourceHashes={p.name: sha(p) for p in (Path(__file__), Path(bounded.__file__),
                                      Path(three.__file__), Path(reasoning.__file__),
                                      ROOT/'research/TagModelScreen/field_feasibility.py',
                                      ROOT/'research/TagModelScreen/science_route_comparison.py')},
                  limits=dict(targets=19, fields=152, packageAttempts=77824, candidates=228,
                              replays=21888, validationReplays=43776, secondsPerPass=360, reviewedChanges=6),
                  seconds=round(time.monotonic()-start, 3),
                  caveat='Existing automated proxies preserved; human interest and exact player averages unverified.')
    private_path.write_text(json.dumps(dict(targets=[f.triple for f in formulas], knowledge=knowledge,
                            pool=options, selection=records_private), indent=2), encoding='utf-8')
    public_path.write_text(json.dumps(public, indent=2), encoding='utf-8')
    print(json.dumps(dict(covered=public['coveredTargets'], candidates=sum(map(len, options)),
                         counters=dict(counters), seconds=public['seconds']), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'private_output', 'public_output'):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    run(args.input, args.private_output, args.public_output)
