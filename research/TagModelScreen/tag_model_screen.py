#!/usr/bin/env python3
"""AlchemyRiddle tag-model screen.

Research-only helper. The repository intentionally does not contain the exact
vanilla recipe corpus. Supply a private JSON input at runtime.

Input shape:
{
  "ingredients": [
    {"name": "...", "type": "Powder|Fluid|Essence|Universal", "tags": ["..."]}
  ],
  "formulas": [
    {"output": "...", "powder": "...", "fluid": "...", "essence": "..."}
  ]
}

The helper reports:
- structural baseline counts;
- adjacent compatibility-chain count;
- fixed tag-signature collisions by ingredient type;
- for each output, common exact tag-count facts shared by all its formulas;
- best achievable Powder+Fluid branch count using any subset of those facts.

It never needs to print exact formula rows.
"""

import argparse
import itertools
import json
from collections import Counter, defaultdict


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def signature(tags):
    return tuple(sorted(tags))


def aggregate(names, tags_by_name, vocabulary):
    counts = Counter()
    for name in names:
        counts.update(tags_by_name[name])
    return {tag: counts[tag] for tag in vocabulary}


def choose_supersets(universe, required, size):
    required = set(required)
    if len(required) > size:
        return []
    extras = [x for x in universe if x not in required]
    return [
        tuple(sorted(required.union(extra)))
        for extra in itertools.combinations(extras, size - len(required))
    ]


def bounded_three_by_three_report(formulas, tags_by_name, vocabulary):
    powders = sorted({x["powder"] for x in formulas})
    fluids = sorted({x["fluid"] for x in formulas})
    essences = sorted({x["essence"] for x in formulas})
    essence_index = {name: i for i, name in enumerate(essences)}

    by_output = defaultdict(list)
    for row in formulas:
        by_output[row["output"]].append(row)

    triple_counts = {}
    for p in powders:
        for f in fluids:
            for e in essences:
                triple_counts[(p, f, e)] = aggregate(
                    (p, f, e), tags_by_name, vocabulary
                )

    output_report = {}
    aggregate_counts = Counter()

    for output, rows in sorted(by_output.items()):
        true_triples = {
            (r["powder"], r["fluid"], r["essence"])
            for r in rows
        }

        required_p = {x[0] for x in true_triples}
        required_f = {x[1] for x in true_triples}
        required_e = {x[2] for x in true_triples}

        p_surfaces = choose_supersets(powders, required_p, 3)
        f_surfaces = choose_supersets(fluids, required_f, 3)
        e_surfaces = choose_supersets(essences, required_e, 3)

        if not p_surfaces or not f_surfaces or not e_surfaces:
            output_report[output] = {
                "formula_count": len(rows),
                "surface_count": 0,
                "reason": "valid-answer set does not fit a 3x3x3 surface",
            }
            continue

        true_count_vectors = [
            triple_counts[x]
            for x in sorted(true_triples)
        ]
        invariant_facts = {
            tag: true_count_vectors[0][tag]
            for tag in vocabulary
            if all(v[tag] == true_count_vectors[0][tag]
                   for v in true_count_vectors)
        }

        fact_items = sorted(invariant_facts.items())
        fact_subsets = []
        matching_masks = {}

        for k in range(1, len(fact_items) + 1):
            for subset in itertools.combinations(fact_items, k):
                fact_subsets.append(subset)
                pair_masks = {}
                for p in powders:
                    for f in fluids:
                        mask = 0
                        for e in essences:
                            counts = triple_counts[(p, f, e)]
                            if all(
                                counts[tag] == value
                                for tag, value in subset
                            ):
                                mask |= 1 << essence_index[e]
                        pair_masks[(p, f)] = mask
                matching_masks[subset] = pair_masks

        full_subset = tuple(fact_items)
        if full_subset:
            full_masks = matching_masks[full_subset]
        else:
            all_essences_mask = (1 << len(essences)) - 1
            full_masks = {
                (p, f): all_essences_mask
                for p in powders
                for f in fluids
            }

        surface_count = 0
        minimum_fact_histogram = Counter()
        one_fact_surfaces = 0
        positive_one_fact_surfaces = 0
        at_most_two_fact_surfaces = 0
        any_envelope_surfaces = 0
        exact_answer_surfaces = 0
        best_full = None

        for p_surface in p_surfaces:
            for f_surface in f_surfaces:
                pl_pairs = [
                    (p, f)
                    for p in p_surface
                    for f in f_surface
                ]
                for e_surface in e_surfaces:
                    surface_count += 1
                    e_mask = sum(
                        1 << essence_index[e]
                        for e in e_surface
                    )

                    minimum = None
                    has_one = False
                    has_positive_one = False

                    for subset in fact_subsets:
                        if minimum is not None and len(subset) > minimum:
                            break

                        pair_masks = matching_masks[subset]
                        branches = sum(
                            1
                            for pair in pl_pairs
                            if pair_masks[pair] & e_mask
                        )

                        if 2 <= branches <= 4:
                            if minimum is None:
                                minimum = len(subset)
                            if len(subset) == 1:
                                has_one = True
                                if subset[0][1] > 0:
                                    has_positive_one = True

                    if minimum is None:
                        minimum_fact_histogram["none"] += 1
                    else:
                        minimum_fact_histogram[str(minimum)] += 1
                        any_envelope_surfaces += 1
                        if minimum <= 2:
                            at_most_two_fact_surfaces += 1

                    if has_one:
                        one_fact_surfaces += 1
                    if has_positive_one:
                        positive_one_fact_surfaces += 1

                    full_survivors = set()
                    full_branches = 0
                    for p, f in pl_pairs:
                        mask = full_masks[(p, f)] & e_mask
                        if mask:
                            full_branches += 1
                        for e in essences:
                            if mask & (1 << essence_index[e]):
                                full_survivors.add((p, f, e))

                    full_metric = (full_branches, len(full_survivors))
                    if best_full is None or full_metric < best_full:
                        best_full = full_metric

                    if full_survivors == true_triples:
                        exact_answer_surfaces += 1

        result = {
            "formula_count": len(rows),
            "invariant_exact_tag_facts": len(invariant_facts),
            "surface_count": surface_count,
            "minimum_fact_histogram": dict(
                sorted(minimum_fact_histogram.items())
            ),
            "one_fact_surfaces": one_fact_surfaces,
            "positive_one_fact_surfaces": positive_one_fact_surfaces,
            "at_most_two_fact_surfaces": at_most_two_fact_surfaces,
            "any_envelope_surfaces": any_envelope_surfaces,
            "exact_answer_surfaces": exact_answer_surfaces,
            "best_full_fact_branches": None if best_full is None else best_full[0],
            "best_full_fact_triples": None if best_full is None else best_full[1],
        }
        output_report[output] = result

        aggregate_counts["outputs"] += 1
        if one_fact_surfaces:
            aggregate_counts["outputs_with_one_fact_surface"] += 1
        if positive_one_fact_surfaces:
            aggregate_counts["outputs_with_positive_one_fact_surface"] += 1
        if at_most_two_fact_surfaces:
            aggregate_counts["outputs_with_at_most_two_fact_surface"] += 1
        if exact_answer_surfaces:
            aggregate_counts["outputs_with_exact_answer_surface"] += 1
        aggregate_counts["surfaces"] += surface_count
        aggregate_counts["one_fact_surfaces"] += one_fact_surfaces
        aggregate_counts["positive_one_fact_surfaces"] += positive_one_fact_surfaces
        aggregate_counts["at_most_two_fact_surfaces"] += at_most_two_fact_surfaces
        aggregate_counts["any_envelope_surfaces"] += any_envelope_surfaces
        aggregate_counts["exact_answer_surfaces"] += exact_answer_surfaces

    return {
        "surface_shape": "3x3x3",
        "branch_envelope": [2, 4],
        "aggregate": dict(aggregate_counts),
        "targets": output_report,
    }



def dosed_three_by_three_report(formulas, tags_by_name, vocabulary):
    """Screen whether clue strength can be distributed across weak facts.

    Two-fact criterion:
    - each individual fact leaves 6-8 Powder+Fluid branches out of 9;
    - their conjunction leaves 3-4 branches.

    Three-fact criterion:
    - each individual fact leaves 6-8 branches;
    - every two-fact conjunction leaves 3-6 branches;
    - all three facts leave 2-4 branches;
    - each fact is necessary: removing it increases branch count.

    Positive-only variants reject zero-count facts.
    """
    powders = sorted({x["powder"] for x in formulas})
    fluids = sorted({x["fluid"] for x in formulas})
    essences = sorted({x["essence"] for x in formulas})
    essence_index = {name: i for i, name in enumerate(essences)}

    by_output = defaultdict(list)
    for row in formulas:
        by_output[row["output"]].append(row)

    triple_counts = {}
    for p in powders:
        for f in fluids:
            for e in essences:
                triple_counts[(p, f, e)] = aggregate(
                    (p, f, e), tags_by_name, vocabulary
                )

    output_report = {}
    aggregate_counts = Counter()

    for output, rows in sorted(by_output.items()):
        true_triples = {
            (r["powder"], r["fluid"], r["essence"])
            for r in rows
        }
        required_p = {x[0] for x in true_triples}
        required_f = {x[1] for x in true_triples}
        required_e = {x[2] for x in true_triples}

        p_surfaces = choose_supersets(powders, required_p, 3)
        f_surfaces = choose_supersets(fluids, required_f, 3)
        e_surfaces = choose_supersets(essences, required_e, 3)

        true_count_vectors = [triple_counts[x] for x in sorted(true_triples)]
        invariant_facts = {
            tag: true_count_vectors[0][tag]
            for tag in vocabulary
            if all(v[tag] == true_count_vectors[0][tag]
                   for v in true_count_vectors)
        }
        facts = list(sorted(invariant_facts.items()))

        fact_masks = {}
        for fact in facts:
            tag, value = fact
            pair_masks = {}
            for p in powders:
                for f in fluids:
                    mask = 0
                    for e in essences:
                        if triple_counts[(p, f, e)][tag] == value:
                            mask |= 1 << essence_index[e]
                    pair_masks[(p, f)] = mask
            fact_masks[fact] = pair_masks

        surface_count = 0
        two_fact_surfaces = 0
        two_positive_surfaces = 0
        three_fact_surfaces = 0
        three_positive_surfaces = 0
        max_two_fact_surviving_triples = 0
        max_two_positive_surviving_triples = 0

        for p_surface in p_surfaces:
            for f_surface in f_surfaces:
                pl_pairs = [
                    (p, f)
                    for p in p_surface
                    for f in f_surface
                ]
                for e_surface in e_surfaces:
                    surface_count += 1
                    e_mask = sum(
                        1 << essence_index[e]
                        for e in e_surface
                    )

                    single = {
                        fact: sum(
                            1
                            for pair in pl_pairs
                            if fact_masks[fact][pair] & e_mask
                        )
                        for fact in facts
                    }

                    weak_facts = [
                        fact for fact in facts
                        if 6 <= single[fact] <= 8
                    ]

                    pair_counts = {}
                    has_two = False
                    has_two_positive = False
                    for a, b in itertools.combinations(weak_facts, 2):
                        surviving_masks = [
                            fact_masks[a][pair]
                            & fact_masks[b][pair]
                            & e_mask
                            for pair in pl_pairs
                        ]
                        count = sum(bool(mask) for mask in surviving_masks)
                        pair_counts[(a, b)] = count
                        if 3 <= count <= 4:
                            surviving_triples = sum(
                                mask.bit_count()
                                for mask in surviving_masks
                            )
                            has_two = True
                            max_two_fact_surviving_triples = max(
                                max_two_fact_surviving_triples,
                                surviving_triples,
                            )
                            if a[1] > 0 and b[1] > 0:
                                has_two_positive = True
                                max_two_positive_surviving_triples = max(
                                    max_two_positive_surviving_triples,
                                    surviving_triples,
                                )

                    if has_two:
                        two_fact_surfaces += 1
                    if has_two_positive:
                        two_positive_surfaces += 1

                    has_three = False
                    has_three_positive = False
                    for combo in itertools.combinations(weak_facts, 3):
                        pair_values = []
                        for a, b in itertools.combinations(combo, 2):
                            key = (a, b) if (a, b) in pair_counts else (b, a)
                            if key in pair_counts:
                                pair_value = pair_counts[key]
                            else:
                                pair_value = sum(
                                    1
                                    for pair in pl_pairs
                                    if (
                                        fact_masks[a][pair]
                                        & fact_masks[b][pair]
                                        & e_mask
                                    )
                                )
                                pair_counts[(a, b)] = pair_value
                            pair_values.append(pair_value)

                        if not all(3 <= x <= 6 for x in pair_values):
                            continue

                        full = sum(
                            1
                            for pair in pl_pairs
                            if (
                                fact_masks[combo[0]][pair]
                                & fact_masks[combo[1]][pair]
                                & fact_masks[combo[2]][pair]
                                & e_mask
                            )
                        )
                        if not 2 <= full <= 4:
                            continue
                        if not all(x > full for x in pair_values):
                            continue

                        has_three = True
                        if all(fact[1] > 0 for fact in combo):
                            has_three_positive = True

                    if has_three:
                        three_fact_surfaces += 1
                    if has_three_positive:
                        three_positive_surfaces += 1

        result = {
            "formula_count": len(rows),
            "invariant_fact_count": len(facts),
            "surface_count": surface_count,
            "two_fact_surfaces": two_fact_surfaces,
            "two_positive_surfaces": two_positive_surfaces,
            "three_fact_surfaces": three_fact_surfaces,
            "three_positive_surfaces": three_positive_surfaces,
            "max_two_fact_surviving_triples": max_two_fact_surviving_triples,
            "max_two_positive_surviving_triples": (
                max_two_positive_surviving_triples
            ),
        }
        output_report[output] = result

        aggregate_counts["outputs"] += 1
        aggregate_counts["surfaces"] += surface_count
        aggregate_counts["two_fact_surfaces"] += two_fact_surfaces
        aggregate_counts["two_positive_surfaces"] += two_positive_surfaces
        aggregate_counts["three_fact_surfaces"] += three_fact_surfaces
        aggregate_counts["three_positive_surfaces"] += three_positive_surfaces

        if two_fact_surfaces:
            aggregate_counts["outputs_with_two_fact_surface"] += 1
        if two_positive_surfaces:
            aggregate_counts["outputs_with_two_positive_surface"] += 1
        if three_fact_surfaces:
            aggregate_counts["outputs_with_three_fact_surface"] += 1
        if three_positive_surfaces:
            aggregate_counts["outputs_with_three_positive_surface"] += 1

    return {
        "surface_shape": "3x3x3",
        "two_fact_criterion": {
            "single_branch_range": [6, 8],
            "combined_branch_range": [3, 4],
        },
        "three_fact_criterion": {
            "single_branch_range": [6, 8],
            "pair_branch_range": [3, 6],
            "combined_branch_range": [2, 4],
            "each_fact_required": True,
        },
        "aggregate": dict(aggregate_counts),
        "targets": output_report,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json")
    ap.add_argument(
        "--assert-three-slot-baseline",
        action="store_true",
        help="Assert the accepted ordinary 1.407 three-slot structural baseline.",
    )
    ap.add_argument(
        "--bounded-3x3",
        action="store_true",
        help=(
            "Enumerate every 3x3x3 candidate surface containing all valid "
            "formula ingredients for each output and screen invariant tag facts."
        ),
    )
    ap.add_argument(
        "--dosing-screen",
        action="store_true",
        help=(
            "Screen 3x3x3 surfaces for balanced two- and three-fact clue sets "
            "whose individual facts remain weak."
        ),
    )
    args = ap.parse_args()

    data = load(args.input_json)
    ingredients = data["ingredients"]
    formulas = data["formulas"]

    tags_by_name = {x["name"]: set(x["tags"]) for x in ingredients}
    type_by_name = {x["name"]: x["type"] for x in ingredients}
    vocabulary = sorted({t for x in ingredients for t in x["tags"]})

    powders = sorted({x["powder"] for x in formulas})
    fluids = sorted({x["fluid"] for x in formulas})
    essences = sorted({x["essence"] for x in formulas})
    outputs = sorted({x["output"] for x in formulas})

    pl_edges = {(x["powder"], x["fluid"]) for x in formulas}
    le_edges = {(x["fluid"], x["essence"]) for x in formulas}
    compatible_chains = [
        (p, f, e)
        for p in powders
        for f in fluids
        for e in essences
        if (p, f) in pl_edges and (f, e) in le_edges
    ]

    structural = {
        "formulas": len(formulas),
        "outputs": len(outputs),
        "powders": len(powders),
        "fluids": len(fluids),
        "essences": len(essences),
        "cartesian_triples": len(powders) * len(fluids) * len(essences),
        "powder_fluid_edges": len(pl_edges),
        "fluid_essence_edges": len(le_edges),
        "compatible_chains": len(compatible_chains),
    }

    if args.assert_three_slot_baseline:
        expected = {
            "formulas": 19,
            "outputs": 16,
            "powders": 10,
            "fluids": 9,
            "essences": 9,
            "cartesian_triples": 810,
            "powder_fluid_edges": 19,
            "fluid_essence_edges": 18,
            "compatible_chains": 47,
        }
        if structural != expected:
            raise SystemExit(
                "Baseline mismatch:\n"
                + json.dumps({"expected": expected, "actual": structural},
                             ensure_ascii=False, indent=2)
            )

    signature_report = {}
    for ingredient_type in ("Powder", "Fluid", "Essence", "Universal"):
        groups = defaultdict(list)
        for name, typ in type_by_name.items():
            if typ == ingredient_type:
                groups[signature(tags_by_name[name])].append(name)
        signature_report[ingredient_type] = {
            "ingredients": sum(len(v) for v in groups.values()),
            "unique_signatures": len(groups),
            "singleton_signatures": sum(1 for v in groups.values() if len(v) == 1),
            "collision_sizes": sorted(
                [len(v) for v in groups.values() if len(v) > 1], reverse=True
            ),
        }

    all_triples = []
    for p in powders:
        for f in fluids:
            for e in essences:
                all_triples.append(
                    (p, f, e, aggregate((p, f, e), tags_by_name, vocabulary))
                )

    by_output = defaultdict(list)
    for row in formulas:
        by_output[row["output"]].append(row)

    target_report = {}
    for output, rows in by_output.items():
        formula_counts = [
            aggregate(
                (r["powder"], r["fluid"], r["essence"]),
                tags_by_name,
                vocabulary,
            )
            for r in rows
        ]
        common = {
            tag: formula_counts[0][tag]
            for tag in vocabulary
            if all(c[tag] == formula_counts[0][tag] for c in formula_counts)
        }

        best = None
        keys = sorted(common)
        for k in range(len(keys) + 1):
            best_this_k = None
            for subset in itertools.combinations(keys, k):
                candidates = [
                    row
                    for row in all_triples
                    if all(row[3][tag] == common[tag] for tag in subset)
                ]
                branches = len({(row[0], row[1]) for row in candidates})
                metric = (branches, len(candidates), subset)
                if best_this_k is None or metric < best_this_k:
                    best_this_k = metric
            if best_this_k is not None and best_this_k[0] <= 4:
                best = {
                    "facts": k,
                    "branches": best_this_k[0],
                    "triples": best_this_k[1],
                }
                break

        candidates_full = [
            row
            for row in all_triples
            if all(row[3][tag] == value for tag, value in common.items())
        ]
        target_report[output] = {
            "formula_count": len(rows),
            "common_exact_tag_facts": len(common),
            "minimum_facts_to_at_most_4_branches": best,
            "all_common_facts_branches": len(
                {(row[0], row[1]) for row in candidates_full}
            ),
            "all_common_facts_triples": len(candidates_full),
        }

    summary = {
        "structural": structural,
        "tag_vocabulary": vocabulary,
        "signature_report": signature_report,
        "outputs_reaching_at_most_4_branches": sum(
            1
            for x in target_report.values()
            if x["minimum_facts_to_at_most_4_branches"] is not None
        ),
        "outputs_total": len(target_report),
        "targets": target_report,
        "bounded_3x3": (
            bounded_three_by_three_report(formulas, tags_by_name, vocabulary)
            if args.bounded_3x3
            else None
        ),
        "dosing_screen": (
            dosed_three_by_three_report(formulas, tags_by_name, vocabulary)
            if args.dosing_screen
            else None
        ),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
