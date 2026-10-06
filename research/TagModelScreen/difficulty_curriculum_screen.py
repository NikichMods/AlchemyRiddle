#!/usr/bin/env python3
"""AlchemyRiddle difficulty-curriculum structural screen.

Research-only helper. Exact vanilla formula rows are supplied as private JSON
inputs and are never embedded or printed by this script.

Purpose:
- reproduce the accepted 2-slot / 3-slot structural baselines;
- split the 2-slot logical grammar into pedagogical introduction tiers;
- test compact 3-slot tutorial/early fields using only already-familiar simple
  property clues plus the adjacent-relation layer;
- report only aggregate coverage.

This is an existence / structure screen, not a final player model. In particular,
it does not know which reagent identities a specific save has already exposed,
and it does not assign a final Science price to formula submission.
"""

import argparse
import itertools
import json
import math
from collections import Counter, defaultdict


TWO_SHAPES = ((2, 2), (2, 3), (3, 2), (3, 3))
THREE_COMPACT_SHAPES = ((2, 2, 2), (2, 3, 2), (3, 2, 2))


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def choose_supersets(universe, required, size):
    required = set(required)
    if len(required) > size:
        return []
    extras = [x for x in universe if x not in required]
    return [
        tuple(sorted(required.union(extra)))
        for extra in itertools.combinations(extras, size - len(required))
    ]


def assert_two_baseline(data):
    formulas = data["formulas"]
    outputs = Counter(row["output"] for row in formulas)
    powders = {row["powder"] for row in formulas}
    fluids = {row["fluid"] for row in formulas}
    pairs = [(row["powder"], row["fluid"]) for row in formulas]
    neighbor_count = sum(
        any(
            i != j
            and sum(a != b for a, b in zip(pair, other)) == 1
            for j, other in enumerate(pairs)
        )
        for i, pair in enumerate(pairs)
    )
    actual = (
        len(formulas),
        len(outputs),
        sum(v > 1 for v in outputs.values()),
        max(outputs.values()),
        len(powders),
        len(fluids),
        neighbor_count,
    )
    expected = (24, 18, 4, 3, 15, 9, 23)
    if actual != expected:
        raise AssertionError("2-slot baseline mismatch: {} != {}".format(actual, expected))


def assert_three_baseline(data):
    formulas = data["formulas"]
    powders = sorted({row["powder"] for row in formulas})
    fluids = sorted({row["fluid"] for row in formulas})
    essences = sorted({row["essence"] for row in formulas})
    outputs = {row["output"] for row in formulas}
    stable_pf = {(row["powder"], row["fluid"]) for row in formulas}
    stable_fe = {(row["fluid"], row["essence"]) for row in formulas}
    chains = sum(
        (p, f) in stable_pf and (f, e) in stable_fe
        for p in powders
        for f in fluids
        for e in essences
    )
    actual = (
        len(formulas),
        len(outputs),
        len(powders),
        len(fluids),
        len(essences),
        len(powders) * len(fluids) * len(essences),
        len(stable_pf),
        len(stable_fe),
        chains,
    )
    expected = (19, 16, 10, 9, 9, 810, 19, 18, 47)
    if actual != expected:
        raise AssertionError("3-slot baseline mismatch: {} != {}".format(actual, expected))


def tag_model(data):
    tags = {row["name"]: set(row["tags"]) for row in data["ingredients"]}
    vocabulary = sorted({tag for values in tags.values() for tag in values})
    return tags, vocabulary


def has(tags, item, tag):
    return tag in tags[item]


# ---------------------------------------------------------------------------
# Two-slot grammar tiers
# ---------------------------------------------------------------------------

TWO_TIERS = (
    "simple",
    "xor",
    "forward_positive_implication",
    "forward_all_implication",
    "full",
)


def two_target_clues(tags, vocabulary, target, tier):
    powder, fluid = target
    clues = []

    for tag in vocabulary:
        clues.append(("literal", "P", tag, has(tags, powder, tag)))
        clues.append(("literal", "F", tag, has(tags, fluid, tag)))
        clues.append(
            (
                "count",
                tag,
                int(has(tags, powder, tag)) + int(has(tags, fluid, tag)),
            )
        )

    if tier == "simple":
        return clues

    for ptag in vocabulary:
        for ftag in vocabulary:
            if has(tags, powder, ptag) != has(tags, fluid, ftag):
                clues.append(("xor", ptag, ftag))

    if tier == "xor":
        return clues

    for ptag in vocabulary:
        if not has(tags, powder, ptag):
            continue
        for ftag in vocabulary:
            expected = has(tags, fluid, ftag)
            if expected:
                clues.append(("imp_pf", ptag, ftag, True))
            elif tier in ("forward_all_implication", "full"):
                clues.append(("imp_pf", ptag, ftag, False))

    if tier == "forward_positive_implication":
        return clues
    if tier == "forward_all_implication":
        return clues

    if tier != "full":
        raise ValueError("unknown 2-slot tier: " + tier)

    for ftag in vocabulary:
        if not has(tags, fluid, ftag):
            continue
        for ptag in vocabulary:
            clues.append(("imp_fp", ftag, ptag, has(tags, powder, ptag)))

    return clues


def eval_two_clue(tags, clue, pair):
    powder, fluid = pair
    kind = clue[0]

    if kind == "literal":
        _, slot, tag, expected = clue
        item = powder if slot == "P" else fluid
        return has(tags, item, tag) == expected
    if kind == "count":
        _, tag, expected = clue
        return int(has(tags, powder, tag)) + int(has(tags, fluid, tag)) == expected
    if kind == "xor":
        _, ptag, ftag = clue
        return has(tags, powder, ptag) != has(tags, fluid, ftag)
    if kind == "imp_pf":
        _, ptag, ftag, expected = clue
        return (not has(tags, powder, ptag)) or has(tags, fluid, ftag) == expected
    if kind == "imp_fp":
        _, ftag, ptag, expected = clue
        return (not has(tags, fluid, ftag)) or has(tags, powder, ptag) == expected
    raise ValueError("unknown clue: " + repr(clue))


def weak_floor(volume, policy):
    if policy == "strict":
        return math.ceil(2 * volume / 3)
    if policy == "compact":
        return max(2, math.ceil(volume / 2))
    raise ValueError("unknown policy: " + policy)


def nonredundant_masks(masks):
    masks = tuple(masks)
    for i, mask in enumerate(masks):
        others = 0
        for j, other in enumerate(masks):
            if i != j:
                others |= other
        if not (mask & ~others):
            return False
    return True


def classify_two_surface(tags, vocabulary, target, surface, tier, policy):
    pairs = [(p, f) for p in surface[0] for f in surface[1]]
    target_index = pairs.index(target)
    target_bit = 1 << target_index
    volume = len(pairs)
    floor = weak_floor(volume, policy)

    eliminations = set()
    for clue in two_target_clues(tags, vocabulary, target, tier):
        survivors = 0
        for i, pair in enumerate(pairs):
            if eval_two_clue(tags, clue, pair):
                survivors |= 1 << i
        count = survivors.bit_count()
        if not survivors & target_bit:
            raise AssertionError("generated target-false 2-slot clue")
        if floor <= count <= volume - 1:
            eliminated = ((1 << volume) - 1) & ~survivors
            if eliminated:
                eliminations.add(eliminated)

    unique = False
    residual_two = False
    unique_clues = None

    elims = list(eliminations)
    for k in (2, 3):
        for combo in itertools.combinations(elims, k):
            if not nonredundant_masks(combo):
                continue
            removed = 0
            for x in combo:
                removed |= x
            remaining = volume - removed.bit_count()
            if remaining == 1:
                unique = True
                unique_clues = k
                return unique, residual_two, unique_clues
            if remaining == 2:
                residual_two = True

    return unique, residual_two, unique_clues


def two_slot_report(data):
    assert_two_baseline(data)
    tags, vocabulary = tag_model(data)
    formulas = data["formulas"]
    powders = sorted({row["powder"] for row in formulas})
    fluids = sorted({row["fluid"] for row in formulas})

    report = {}
    for shape in TWO_SHAPES:
        psize, fsize = shape
        shape_key = "{}x{}".format(psize, fsize)
        report[shape_key] = {}

        for policy in ("compact", "strict"):
            tier_rows = {}
            for tier in TWO_TIERS:
                covered_unique = 0
                covered_two = 0
                two_clue_unique = 0
                for row in formulas:
                    target = (row["powder"], row["fluid"])
                    target_unique = False
                    target_two = False
                    target_two_clue = False
                    for ps in choose_supersets(powders, [target[0]], psize):
                        if target_unique and target_two_clue:
                            break
                        for fs in choose_supersets(fluids, [target[1]], fsize):
                            unique, residual_two, clue_count = classify_two_surface(
                                tags, vocabulary, target, (ps, fs), tier, policy
                            )
                            target_unique |= unique
                            target_two |= unique or residual_two
                            target_two_clue |= unique and clue_count == 2
                            if target_unique and target_two and target_two_clue:
                                break
                    covered_unique += int(target_unique)
                    covered_two += int(target_two)
                    two_clue_unique += int(target_two_clue)

                tier_rows[tier] = {
                    "unique_variants": covered_unique,
                    "le2_variants": covered_two,
                    "unique_in_2_clues_variants": two_clue_unique,
                }
            report[shape_key][policy] = tier_rows
    return report


# ---------------------------------------------------------------------------
# Three-slot compact tutorial/early screen
# ---------------------------------------------------------------------------


def three_simple_clues(tags, vocabulary, target):
    p, f, e = target
    clues = []
    for tag in vocabulary:
        clues.append(("literal", "P", tag, has(tags, p, tag)))
        clues.append(("literal", "F", tag, has(tags, f, tag)))
        clues.append(("literal", "E", tag, has(tags, e, tag)))
        clues.append(
            (
                "count",
                tag,
                int(has(tags, p, tag))
                + int(has(tags, f, tag))
                + int(has(tags, e, tag)),
            )
        )
    return clues


def eval_three_simple(tags, clue, triple):
    p, f, e = triple
    kind = clue[0]
    if kind == "literal":
        _, slot, tag, expected = clue
        item = {"P": p, "F": f, "E": e}[slot]
        return has(tags, item, tag) == expected
    if kind == "count":
        _, tag, expected = clue
        return (
            int(has(tags, p, tag))
            + int(has(tags, f, tag))
            + int(has(tags, e, tag))
            == expected
        )
    raise ValueError("unknown 3-slot clue: " + repr(clue))


def branch_count(triples, survivor_mask):
    return len(
        {
            (p, f)
            for i, (p, f, _e) in enumerate(triples)
            if (survivor_mask >> i) & 1
        }
    )


def useful_relation_metrics(triples, survivor_mask, stable_pf, stable_fe, target):
    surviving = [
        triple
        for i, triple in enumerate(triples)
        if (survivor_mask >> i) & 1
    ]
    if not surviving:
        return {
            "narrowing_incompatible_test": False,
            "target_anchor_max_continuations": None,
            "min_incompatible_tests_to_le2": None,
        }

    pvals = sorted({p for p, _, _ in triples})
    fvals = sorted({f for _, f, _ in triples})
    evals = sorted({e for _, _, e in triples})

    narrowing = False
    incompatible_elims = []

    for p in pvals:
        for f in fvals:
            if (p, f) in stable_pf:
                continue
            removes = {
                i for i, (pp, ff, _ee) in enumerate(surviving)
                if pp == p and ff == f
            }
            if removes and len(removes) < len(surviving):
                narrowing = True
                incompatible_elims.append(removes)

    for f in fvals:
        for e in evals:
            if (f, e) in stable_fe:
                continue
            removes = {
                i for i, (_pp, ff, ee) in enumerate(surviving)
                if ff == f and ee == e
            }
            if removes and len(removes) < len(surviving):
                narrowing = True
                incompatible_elims.append(removes)

    min_tests = None
    if len(surviving) <= 2:
        min_tests = 0
    else:
        for k in (1, 2, 3):
            found = False
            for combo in itertools.combinations(incompatible_elims, k):
                removed = set().union(*combo)
                if len(surviving) - len(removed) <= 2:
                    min_tests = k
                    found = True
                    break
            if found:
                break

    tp, tf, te = target
    pf_cont = len({e for p, f, e in surviving if p == tp and f == tf})
    fe_cont = len({p for p, f, e in surviving if f == tf and e == te})
    anchor_max = max(pf_cont, fe_cont)

    return {
        "narrowing_incompatible_test": narrowing,
        "target_anchor_max_continuations": anchor_max,
        "min_incompatible_tests_to_le2": min_tests,
    }


def compact_three_surface_candidates(
    tags,
    vocabulary,
    target,
    surface,
    stable_pf,
    stable_fe,
    branch_min,
    branch_max,
    max_clues,
    policy,
):
    triples = [
        (p, f, e)
        for p in surface[0]
        for f in surface[1]
        for e in surface[2]
    ]
    target_index = triples.index(target)
    target_bit = 1 << target_index
    raw_branches = len(surface[0]) * len(surface[1])
    floor = (
        max(2, math.ceil(raw_branches / 2))
        if policy == "compact"
        else math.ceil(2 * raw_branches / 3)
    )

    clue_masks = set()
    for clue in three_simple_clues(tags, vocabulary, target):
        mask = 0
        for i, triple in enumerate(triples):
            if eval_three_simple(tags, clue, triple):
                mask |= 1 << i
        if not mask & target_bit:
            raise AssertionError("generated target-false 3-slot clue")
        b = branch_count(triples, mask)
        if floor <= b <= raw_branches - 1:
            clue_masks.add(mask)

    all_mask = (1 << len(triples)) - 1
    candidates = []
    # 0 clues is kept only for diagnostics / expertise-like simple starts.
    for k in range(0, max_clues + 1):
        source = [()] if k == 0 else itertools.combinations(clue_masks, k)
        for combo in source:
            survivor = all_mask
            for mask in combo:
                survivor &= mask
            if not survivor & target_bit:
                continue
            branches = branch_count(triples, survivor)
            if not (branch_min <= branches <= branch_max):
                continue
            if k > 1:
                # Every clue must change the result relative to the others.
                ok = True
                for i in range(k):
                    without = all_mask
                    for j, mask in enumerate(combo):
                        if i != j:
                            without &= mask
                    if without == survivor:
                        ok = False
                        break
                if not ok:
                    continue

            relation = useful_relation_metrics(
                triples, survivor, stable_pf, stable_fe, target
            )
            candidates.append(
                {
                    "clues": k,
                    "branches": branches,
                    "triples": survivor.bit_count(),
                    **relation,
                }
            )
    return candidates


def three_slot_compact_report(data):
    assert_three_baseline(data)
    tags, vocabulary = tag_model(data)
    formulas = data["formulas"]
    powders = sorted({row["powder"] for row in formulas})
    fluids = sorted({row["fluid"] for row in formulas})
    essences = sorted({row["essence"] for row in formulas})
    stable_pf = {(row["powder"], row["fluid"]) for row in formulas}
    stable_fe = {(row["fluid"], row["essence"]) for row in formulas}

    scenarios = {
        "tutorial": {
            "branch_min": 2,
            "branch_max": 3,
            "max_clues": 2,
            "policy": "compact",
        },
        "early": {
            "branch_min": 2,
            "branch_max": 4,
            "max_clues": 2,
            "policy": "compact",
        },
    }

    report = {}
    for shape in THREE_COMPACT_SHAPES:
        psize, fsize, esize = shape
        shape_key = "{}x{}x{}".format(psize, fsize, esize)
        report[shape_key] = {}

        for scenario_name, spec in scenarios.items():
            covered = 0
            covered_narrowing = 0
            covered_anchor_le3 = 0
            min_test_hist = Counter()
            min_clue_hist = Counter()

            for row in formulas:
                target = (row["powder"], row["fluid"], row["essence"])
                found = []
                for ps in choose_supersets(powders, [target[0]], psize):
                    for fs in choose_supersets(fluids, [target[1]], fsize):
                        for es in choose_supersets(essences, [target[2]], esize):
                            found.extend(
                                compact_three_surface_candidates(
                                    tags,
                                    vocabulary,
                                    target,
                                    (ps, fs, es),
                                    stable_pf,
                                    stable_fe,
                                    **spec
                                )
                            )

                if not found:
                    continue

                covered += 1
                min_clues = min(x["clues"] for x in found)
                min_clue_hist[str(min_clues)] += 1

                if any(x["narrowing_incompatible_test"] for x in found):
                    covered_narrowing += 1
                if any(
                    x["target_anchor_max_continuations"] is not None
                    and x["target_anchor_max_continuations"] <= 3
                    for x in found
                ):
                    covered_anchor_le3 += 1

                tests = [
                    x["min_incompatible_tests_to_le2"]
                    for x in found
                    if x["min_incompatible_tests_to_le2"] is not None
                ]
                if tests:
                    min_test_hist[str(min(tests))] += 1
                else:
                    min_test_hist["gt3_or_none"] += 1

            report[shape_key][scenario_name] = {
                "covered_variants": covered,
                "variants_with_narrowing_incompatible_test": covered_narrowing,
                "variants_with_target_anchor_le3_continuations": covered_anchor_le3,
                "minimum_clue_count_histogram": dict(sorted(min_clue_hist.items())),
                "optimistic_min_incompatible_tests_to_le2_histogram": dict(
                    sorted(min_test_hist.items())
                ),
            }

    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--two-slot", required=True)
    parser.add_argument("--three-slot", required=True)
    args = parser.parse_args()

    two = load(args.two_slot)
    three = load(args.three_slot)

    output = {
        "baseline": {
            "two_slot": "accepted-1.407-baseline-reproduced",
            "three_slot": "accepted-1.407-baseline-reproduced",
        },
        "two_slot_grammar_tiers": two_slot_report(two),
        "three_slot_compact": three_slot_compact_report(three),
        "limits": [
            "identity exposure requires a save/progression knowledge state",
            "Science economy / paid-submission brute-force pressure is not modeled",
            "3-slot incompatible-test count is an optimistic structural lower bound, not a player strategy prediction",
            "medium/late 3-slot 3x3x3 capacity remains covered by earlier accepted dosing/adaptive screens",
        ],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
