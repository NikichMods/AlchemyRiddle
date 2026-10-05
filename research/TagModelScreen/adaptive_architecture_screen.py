#!/usr/bin/env python3
"""Compare fixed tag-centric and adaptive knowledge-aware three-slot puzzle shapes.

Research-only helper. The exact vanilla formula corpus is supplied as a private
JSON input and is never embedded in this repository.

This screen is intentionally a structural/existence test, not a player model.
It asks whether a bounded 3x3x3 surface plus weak invariant property clues can
remain well-shaped after arbitrary previously learned adjacent compatibility
relations are applied.

A "fresh" state means:
- at least one weak-clue configuration leaves 1-4 live Powder+Fluid branches;
- more than two full triples remain;
- the target is not already represented by one or two fully known stable chains.

A no-fresh state can still be expertise-covered when the player's accumulated
knowledge already supplies a justified target chain / <=2 residual hypotheses.
"""

import argparse
import itertools
import json
import math
import random
import statistics
from collections import Counter, defaultdict


DEFAULT_DENSITIES = (0.0, 0.2, 0.4, 0.6, 0.8)
DEFAULT_SEED = 20261005


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


def build_model(data, surface_samples, seed):
    ingredients = data["ingredients"]
    formulas = data["formulas"]
    tags_by_name = {x["name"]: set(x["tags"]) for x in ingredients}
    vocabulary = sorted({tag for x in ingredients for tag in x["tags"]})

    powders = sorted({x["powder"] for x in formulas})
    fluids = sorted({x["fluid"] for x in formulas})
    essences = sorted({x["essence"] for x in formulas})
    outputs = sorted({x["output"] for x in formulas})

    by_output = defaultdict(list)
    for row in formulas:
        by_output[row["output"]].append(row)

    triples = [
        (p, f, e)
        for p in powders
        for f in fluids
        for e in essences
    ]
    triple_index = {triple: i for i, triple in enumerate(triples)}

    pf_pairs = [(p, f) for p in powders for f in fluids]
    pf_index = {pair: i for i, pair in enumerate(pf_pairs)}
    triple_pf_bits = [
        1 << pf_index[(p, f)]
        for p, f, _ in triples
    ]

    stable_pf = {(x["powder"], x["fluid"]) for x in formulas}
    stable_fe = {(x["fluid"], x["essence"]) for x in formulas}

    relations = (
        [("PF", p, f) for p in powders for f in fluids]
        + [("FE", f, e) for f in fluids for e in essences]
    )
    relation_index = {relation: i for i, relation in enumerate(relations)}
    stable_relations = (
        {("PF", p, f) for p, f in stable_pf}
        | {("FE", f, e) for f, e in stable_fe}
    )
    stable_relation_mask = sum(
        1 << relation_index[relation]
        for relation in stable_relations
    )
    all_relation_mask = (1 << len(relations)) - 1
    incompatible_relation_mask = all_relation_mask ^ stable_relation_mask

    triple_edges = []
    edge_triple_masks = [0] * len(relations)
    compatible_mask = 0
    for i, (p, f, e) in enumerate(triples):
        a = relation_index[("PF", p, f)]
        b = relation_index[("FE", f, e)]
        triple_edges.append((a, b))
        edge_triple_masks[a] |= 1 << i
        edge_triple_masks[b] |= 1 << i
        if (
            ((stable_relation_mask >> a) & 1)
            and ((stable_relation_mask >> b) & 1)
        ):
            compatible_mask |= 1 << i

    def aggregate(triple):
        counts = Counter()
        for name in triple:
            counts.update(tags_by_name[name])
        return {tag: counts[tag] for tag in vocabulary}

    triple_counts = {triple: aggregate(triple) for triple in triples}
    fact_masks = {}
    for tag in vocabulary:
        max_count = max(triple_counts[t][tag] for t in triples)
        for value in range(max_count + 1):
            mask = 0
            for i, triple in enumerate(triples):
                if triple_counts[triple][tag] == value:
                    mask |= 1 << i
            fact_masks[(tag, value)] = mask

    true_masks = {}
    invariant_facts = {}
    target_true_triples = {}
    for output, rows in by_output.items():
        true = [
            (r["powder"], r["fluid"], r["essence"])
            for r in rows
        ]
        target_true_triples[output] = true
        true_masks[output] = sum(1 << triple_index[t] for t in true)
        vectors = [triple_counts[t] for t in true]
        invariant_facts[output] = sorted(
            (tag, vectors[0][tag])
            for tag in vocabulary
            if all(v[tag] == vectors[0][tag] for v in vectors)
        )

    def branch_count(mask):
        branch_mask = 0
        value = mask
        while value:
            bit = value & -value
            i = bit.bit_length() - 1
            value -= bit
            branch_mask |= triple_pf_bits[i]
        return branch_mask.bit_count()

    def make_surface_mask(p_surface, f_surface, e_surface):
        mask = 0
        for p in p_surface:
            for f in f_surface:
                for e in e_surface:
                    mask |= 1 << triple_index[(p, f, e)]
        return mask

    surface_records = {}
    surface_population = {}

    for output_index, output in enumerate(outputs):
        true = set(target_true_triples[output])
        p_surfaces = choose_supersets(
            powders, {x[0] for x in true}, 3
        )
        f_surfaces = choose_supersets(
            fluids, {x[1] for x in true}, 3
        )
        e_surfaces = choose_supersets(
            essences, {x[2] for x in true}, 3
        )
        all_surfaces = [
            (ps, fs, es)
            for ps in p_surfaces
            for fs in f_surfaces
            for es in e_surfaces
        ]
        surface_population[output] = len(all_surfaces)

        # Multi-formula outputs are the fragile classes and remain exhaustive.
        # Single-formula classes use a deterministic surface sample for the
        # knowledge-state Monte Carlo to keep the cross-product tractable.
        if len(by_output[output]) > 1 or surface_samples <= 0:
            selected = all_surfaces
        else:
            sample_count = min(surface_samples, len(all_surfaces))
            rng = random.Random(seed + (output_index + 1) * 104729)
            selected_indices = sorted(
                rng.sample(range(len(all_surfaces)), sample_count)
            )
            selected = [all_surfaces[i] for i in selected_indices]

        records = []
        facts = invariant_facts[output]

        for p_surface, f_surface, e_surface in selected:
            surface_mask = make_surface_mask(
                p_surface, f_surface, e_surface
            )

            singles = {}
            weak_facts = []
            for fact in facts:
                mask = surface_mask & fact_masks[fact]
                branches = branch_count(mask)
                singles[fact] = (mask, branches)
                if 6 <= branches <= 8:
                    weak_facts.append(fact)

            configs = []

            # One weak fact is useful only in the adaptive architecture, where
            # old incompatibilities may provide the rest of the narrowing.
            for fact in weak_facts:
                mask, _ = singles[fact]
                if (mask & compatible_mask).bit_count() <= 2:
                    configs.append((1, (fact,), mask))

            # Two facts: individually weak, conjunction still leaves enough
            # structure for prior relations / new tests to matter.
            for a, b in itertools.combinations(weak_facts, 2):
                mask = surface_mask & fact_masks[a] & fact_masks[b]
                branches = branch_count(mask)
                if not 3 <= branches <= 6:
                    continue
                if singles[a][1] <= branches or singles[b][1] <= branches:
                    continue
                if (mask & compatible_mask).bit_count() <= 2:
                    configs.append((2, (a, b), mask))

            # Three facts: every pair remains intermediate and every fact is
            # non-redundant in the final conjunction.
            for combo in itertools.combinations(weak_facts, 3):
                pair_counts = []
                valid = True
                for a, b in itertools.combinations(combo, 2):
                    pair_mask = (
                        surface_mask
                        & fact_masks[a]
                        & fact_masks[b]
                    )
                    pair_branches = branch_count(pair_mask)
                    pair_counts.append(pair_branches)
                    if not 3 <= pair_branches <= 6:
                        valid = False
                        break
                if not valid:
                    continue

                mask = surface_mask
                for fact in combo:
                    mask &= fact_masks[fact]
                branches = branch_count(mask)
                if not 2 <= branches <= 6:
                    continue
                if not all(x > branches for x in pair_counts):
                    continue
                if (mask & compatible_mask).bit_count() <= 2:
                    configs.append((3, combo, mask))

            if not configs:
                continue

            # Different fact sets may produce the same candidate mask. Keep the
            # smallest clue count for that information state.
            dedup = {}
            for clue_count, clue_facts, mask in configs:
                previous = dedup.get(mask)
                if previous is None or clue_count < previous[0]:
                    dedup[mask] = (clue_count, clue_facts, mask)

            records.append({
                "configs": list(dedup.values()),
            })

        surface_records[output] = records

    formula_edge_sets = []
    for row in formulas:
        formula_edge_sets.append((
            row["output"],
            {
                relation_index[("PF", row["powder"], row["fluid"])],
                relation_index[("FE", row["fluid"], row["essence"])],
            },
        ))

    return {
        "formulas": formulas,
        "by_output": by_output,
        "outputs": outputs,
        "powders": powders,
        "fluids": fluids,
        "essences": essences,
        "relations": relations,
        "relation_index": relation_index,
        "stable_relation_mask": stable_relation_mask,
        "incompatible_relation_mask": incompatible_relation_mask,
        "triple_edges": triple_edges,
        "edge_triple_masks": edge_triple_masks,
        "compatible_mask": compatible_mask,
        "triple_pf_bits": triple_pf_bits,
        "true_masks": true_masks,
        "surface_records": surface_records,
        "surface_population": surface_population,
        "formula_edge_sets": formula_edge_sets,
        "branch_count": branch_count,
        "structural": {
            "formulas": len(formulas),
            "outputs": len(outputs),
            "powders": len(powders),
            "fluids": len(fluids),
            "essences": len(essences),
            "cartesian_triples": len(triples),
            "powder_fluid_edges": len(stable_pf),
            "fluid_essence_edges": len(stable_fe),
            "compatible_chains": compatible_mask.bit_count(),
            "learnable_adjacent_relations": len(relations),
        },
    }


def complete_known_mask(model, known_stable_mask):
    result = 0
    value = model["compatible_mask"]
    while value:
        bit = value & -value
        i = bit.bit_length() - 1
        value -= bit
        a, b = model["triple_edges"][i]
        if (
            ((known_stable_mask >> a) & 1)
            and ((known_stable_mask >> b) & 1)
        ):
            result |= bit
    return result


def removed_mask(model, known_mask):
    incompatible = known_mask & model["incompatible_relation_mask"]
    result = 0
    value = incompatible
    while value:
        bit = value & -value
        relation = bit.bit_length() - 1
        value -= bit
        result |= model["edge_triple_masks"][relation]
    return result


def scan_target_state(model, output, known_mask):
    known_stable = known_mask & model["stable_relation_mask"]
    known_complete = complete_known_mask(model, known_stable)
    remove = removed_mask(model, known_mask)
    true_mask = model["true_masks"][output]

    missing_target_edges = []
    value = true_mask
    while value:
        bit = value & -value
        i = bit.bit_length() - 1
        value -= bit
        a, b = model["triple_edges"][i]
        missing_target_edges.append(
            sum(
                1
                for edge in (a, b)
                if not ((known_mask >> edge) & 1)
            )
        )
    minimum_missing = min(missing_target_edges)

    counts = Counter()
    min_fresh_clues = None
    has_one_branch_fresh = False

    for record in model["surface_records"][output]:
        has_fresh = False
        has_resolved = False
        has_understructured = False
        has_narrow_fresh = False

        for clue_count, _, base_mask in record["configs"]:
            live = base_mask & ~remove
            branches = model["branch_count"](live)

            logical_resolution = live.bit_count() <= 2
            complete_live = known_complete & live
            complete_count = complete_live.bit_count()
            chain_resolution = (
                1 <= complete_count <= 2
                and bool(complete_live & true_mask)
            )

            if logical_resolution or chain_resolution:
                has_resolved = True
                continue

            # A single first-stage branch is not automatically solved: it can
            # still contain several third-slot continuations. It is retained as
            # a legitimate expertise-narrowed fresh puzzle.
            if 1 <= branches <= 4:
                has_fresh = True
                if branches == 1:
                    has_narrow_fresh = True
                    has_one_branch_fresh = True
                if (
                    min_fresh_clues is None
                    or clue_count < min_fresh_clues
                ):
                    min_fresh_clues = clue_count
            else:
                has_understructured = True

        if has_fresh:
            counts["fresh_surfaces"] += 1
        if has_narrow_fresh:
            counts["narrow_fresh_surfaces"] += 1
        if has_resolved:
            counts["resolved_surfaces"] += 1
        if has_understructured:
            counts["understructured_surfaces"] += 1
        if has_fresh or has_resolved:
            counts["usable_or_expertise_surfaces"] += 1
        if not has_fresh and has_resolved:
            counts["only_resolved_surfaces"] += 1
        if not has_fresh and not has_resolved:
            counts["no_usable_surfaces"] += 1

    pool = len(model["surface_records"][output])
    return {
        "sampled_closure_capable_surfaces": pool,
        **counts,
        "fresh": counts["fresh_surfaces"] > 0,
        "expertise_covered": (
            counts["fresh_surfaces"] > 0
            or counts["resolved_surfaces"] > 0
        ),
        "minimum_fresh_clues": min_fresh_clues,
        # This is an existence/lower-bound metric: along a correct target
        # branch, at most the two still-unknown stable adjacent edges need to be
        # established. It is not a claim that a blind player will choose that
        # branch optimally.
        "minimum_missing_target_edges": minimum_missing,
        "has_one_branch_fresh": has_one_branch_fresh,
    }


def uniform_histories(model, density, count, seed):
    relation_count = len(model["relations"])
    if density == 0:
        return [0]
    learned_count = round(density * relation_count)
    universe = list(range(relation_count))
    result = []
    for history in range(count):
        rng = random.Random(
            seed
            + round(density * 1000) * 10007
            + history * 7919
        )
        chosen = rng.sample(universe, learned_count)
        result.append(sum(1 << x for x in chosen))
    return result


def recipe_seeded_histories(
    model, output, output_index, density, count, seed
):
    relation_count = len(model["relations"])
    if density == 0:
        return [0]

    learned_count = round(density * relation_count)
    prior_formulas = [
        edges
        for owner, edges in model["formula_edge_sets"]
        if owner != output
    ]
    universe = list(range(relation_count))
    result = []

    for history in range(count):
        rng = random.Random(
            seed
            + 1234567
            + round(density * 1000) * 10007
            + history * 7919
            + (output_index + 1) * 101
        )
        formula_count = min(
            len(prior_formulas),
            round(density * len(prior_formulas)),
        )
        selected = (
            rng.sample(prior_formulas, formula_count)
            if formula_count
            else []
        )
        learned = set().union(*selected) if selected else set()

        if len(learned) > learned_count:
            learned = set(
                rng.sample(sorted(learned), learned_count)
            )
        if len(learned) < learned_count:
            remaining = [x for x in universe if x not in learned]
            learned.update(
                rng.sample(
                    remaining,
                    learned_count - len(learned),
                )
            )

        result.append(sum(1 << x for x in learned))

    return result


def summarize_states(rows, target_count):
    state_count = len(rows)
    fresh_rows = [x for x in rows if x["state"]["fresh"]]
    saturated_rows = [x for x in rows if not x["state"]["fresh"]]

    clue_counts = Counter(
        x["state"]["minimum_fresh_clues"]
        for x in fresh_rows
    )
    missing_edges = Counter(
        x["state"]["minimum_missing_target_edges"]
        for x in fresh_rows
    )

    fresh_surface_fractions = [
        (
            x["state"].get("fresh_surfaces", 0)
            / x["state"]["sampled_closure_capable_surfaces"]
        )
        for x in fresh_rows
        if x["state"]["sampled_closure_capable_surfaces"]
    ]

    by_target = defaultdict(list)
    for row in rows:
        by_target[row["target_index"]].append(row["state"])

    target_rates = []
    for states in by_target.values():
        target_rates.append(
            sum(x["fresh"] for x in states) / len(states)
        )

    saturated_with_missing_edges = Counter(
        x["state"]["minimum_missing_target_edges"]
        for x in saturated_rows
    )

    return {
        "state_count": state_count,
        "fresh_state_rate": (
            len(fresh_rows) / state_count if state_count else 0
        ),
        "expertise_covered_state_rate": (
            sum(x["state"]["expertise_covered"] for x in rows)
            / state_count
            if state_count
            else 0
        ),
        "saturated_state_count": len(saturated_rows),
        "saturated_missing_target_edge_distribution": dict(
            sorted(saturated_with_missing_edges.items())
        ),
        "saturated_not_explained_by_complete_known_target_chain": sum(
            1
            for x in saturated_rows
            if x["state"]["minimum_missing_target_edges"] != 0
        ),
        "fresh_minimum_clue_distribution": dict(
            sorted(clue_counts.items())
        ),
        "fresh_missing_target_edge_distribution": dict(
            sorted(missing_edges.items())
        ),
        "fresh_states_with_one_branch_option_rate": (
            sum(
                x["state"]["has_one_branch_fresh"]
                for x in fresh_rows
            )
            / len(fresh_rows)
            if fresh_rows
            else 0
        ),
        "fresh_surface_fraction_median": (
            statistics.median(fresh_surface_fractions)
            if fresh_surface_fractions
            else None
        ),
        "fresh_surface_fraction_minimum": (
            min(fresh_surface_fractions)
            if fresh_surface_fractions
            else None
        ),
        "targets_fresh_in_every_sampled_history": sum(
            1 for rate in target_rates if rate == 1
        ),
        "target_count": target_count,
        "worst_target_fresh_history_rate": (
            min(target_rates) if target_rates else None
        ),
    }


def run_family(
    model, family, density, history_samples, seed
):
    rows = []
    outputs = model["outputs"]

    if density == 0:
        for target_index, output in enumerate(outputs):
            rows.append({
                "target_index": target_index,
                "state": scan_target_state(model, output, 0),
            })
        return rows

    if family == "uniform":
        histories = uniform_histories(
            model, density, history_samples, seed
        )
        for target_index, output in enumerate(outputs):
            for known in histories:
                rows.append({
                    "target_index": target_index,
                    "state": scan_target_state(
                        model, output, known
                    ),
                })
        return rows

    if family == "recipe_seeded":
        for target_index, output in enumerate(outputs):
            histories = recipe_seeded_histories(
                model,
                output,
                target_index,
                density,
                history_samples,
                seed,
            )
            for known in histories:
                rows.append({
                    "target_index": target_index,
                    "state": scan_target_state(
                        model, output, known
                    ),
                })
        return rows

    raise ValueError("Unknown history family: " + family)


def parse_densities(raw):
    values = tuple(float(x.strip()) for x in raw.split(",") if x.strip())
    if not values:
        raise ValueError("At least one density is required")
    if any(x < 0 or x > 1 for x in values):
        raise ValueError("Densities must be in [0, 1]")
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument(
        "--surface-samples",
        type=int,
        default=1024,
        help=(
            "Deterministic sample per single-formula target; "
            "multi-formula targets remain exhaustive. Use 0 for exhaustive."
        ),
    )
    parser.add_argument(
        "--history-samples",
        type=int,
        default=64,
        help="Knowledge histories per non-zero density and target/family.",
    )
    parser.add_argument(
        "--densities",
        default="0,0.2,0.4,0.6,0.8",
        help="Comma-separated learned-relation fractions.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
    )
    parser.add_argument(
        "--assert-three-slot-baseline",
        action="store_true",
    )
    args = parser.parse_args()

    densities = parse_densities(args.densities)
    data = load(args.input_json)
    model = build_model(
        data,
        surface_samples=args.surface_samples,
        seed=args.seed,
    )

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
    if args.assert_three_slot_baseline:
        actual = {
            key: model["structural"][key]
            for key in expected
        }
        if actual != expected:
            raise SystemExit(
                "Baseline mismatch:\n"
                + json.dumps(
                    {"expected": expected, "actual": actual},
                    ensure_ascii=False,
                    indent=2,
                )
            )

    report = {
        "screen": "adaptive-architecture-comparison",
        "method": {
            "surface_shape": "3x3x3",
            "surface_samples_per_single_formula_target": (
                args.surface_samples
            ),
            "multi_formula_surfaces": "exhaustive",
            "history_samples_per_nonzero_density": (
                args.history_samples
            ),
            "densities": densities,
            "seed": args.seed,
            "fresh_branch_range": [1, 4],
            "weak_single_fact_branch_range": [6, 8],
            "eventual_compatible_chain_cap": 2,
            "important_limit": (
                "Structural/existence screen only; missing-target-edge counts "
                "are a lower bound along a correct hypothesis branch, not a "
                "blind-player policy."
            ),
        },
        "structural": model["structural"],
        "sampled_closure_capable_surfaces_by_target": {
            "minimum": min(
                len(model["surface_records"][x])
                for x in model["outputs"]
            ),
            "median": statistics.median(
                len(model["surface_records"][x])
                for x in model["outputs"]
            ),
            "maximum": max(
                len(model["surface_records"][x])
                for x in model["outputs"]
            ),
        },
        "families": {},
    }

    baseline_rows = run_family(
        model, "uniform", 0.0, args.history_samples, args.seed
    )
    baseline_summary = summarize_states(
        baseline_rows, len(model["outputs"])
    )

    for family in ("uniform", "recipe_seeded"):
        family_report = {}
        for density in densities:
            if density == 0:
                summary = baseline_summary
            else:
                rows = run_family(
                    model,
                    family,
                    density,
                    args.history_samples,
                    args.seed,
                )
                summary = summarize_states(
                    rows, len(model["outputs"])
                )
            family_report[str(density)] = summary
        report["families"][family] = family_report

    print(json.dumps(
        report,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()
