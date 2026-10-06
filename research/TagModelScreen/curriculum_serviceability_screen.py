#!/usr/bin/env python3
"""Curriculum serviceability screen for AlchemyRiddle.

Research-only. Exact vanilla formula rows stay in private/ephemeral JSON.

The screen asks whether a player-selected formula variant can still serve the
desired curriculum beat without the scheduler choosing a different target.

Inputs are already-filtered progression-core models using the current accepted
property assignment (including Dark + Organ):
  TWO.json   - 16 mandatory two-slot formula variants
  THREE.json - 19 ordinary three-slot formula variants

Only aggregate results are printed.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import statistics
from collections import Counter
from pathlib import Path

import progression_variable_field_screen as three
import reasoning_diversity_screen as reasoning
import two_slot_tag_constraint_screen as two


TWO_FOCAL_SPECS = {
    "xor": {
        "family": "xor",
        "direction": None,
        "support": {"literal", "count"},
    },
    "imp_pos": {
        "family": "imp_pos",
        "direction": "fwd",
        "support": {"literal", "count", "xor"},
    },
    "imp_neg": {
        "family": "imp_neg",
        "direction": "fwd",
        "support": {"literal", "count", "xor", "imp_pos"},
    },
    "reverse_implication": {
        "family": None,
        "direction": "rev",
        "support": {"literal", "count", "xor", "imp_pos", "imp_neg"},
    },
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(values):
    return {
        "minimum": min(values),
        "median": statistics.median(values),
        "mean": statistics.mean(values),
        "maximum": max(values),
    }


def two_family(clue):
    kind = clue[0]
    if kind in ("literal", "count", "xor"):
        return kind
    if kind in ("imp_pf", "imp_fp"):
        return "imp_pos" if clue[-1] else "imp_neg"
    raise ValueError("unknown clue: " + repr(clue))


def two_direction(clue):
    if clue[0] == "imp_pf":
        return "fwd"
    if clue[0] == "imp_fp":
        return "rev"
    return None


def two_clue_mask(model, clue):
    mask = 0
    for index, pair in enumerate(model.pairs):
        if two.eval_clue(model, clue, pair):
            mask |= 1 << index
    return mask


def two_valid_clues(model, target, surface, exact_half=False):
    volume = surface.bit_count()
    target_bit = 1 << model.index[target]
    floor = max(2, math.ceil(volume / 2))

    result = []
    seen = set()
    for clue in two.target_clues(model, target, "composite"):
        mask = two_clue_mask(model, clue)
        survivors = surface & mask
        count = survivors.bit_count()

        if exact_half:
            if count * 2 != volume:
                continue
        elif not (floor <= count <= volume - 1):
            continue

        if not survivors & target_bit:
            continue

        eliminated = surface & ~mask
        key = (two_family(clue), two_direction(clue), eliminated)
        if eliminated and key not in seen:
            seen.add(key)
            result.append((clue, eliminated))

    return result


def unique_and_necessary(eliminations, volume):
    union = 0
    for eliminated in eliminations:
        union |= eliminated

    if volume - union.bit_count() != 1:
        return False

    for index, eliminated in enumerate(eliminations):
        others = 0
        for other_index, other in enumerate(eliminations):
            if index != other_index:
                others |= other
        if not eliminated & ~others:
            return False

    return True


def is_focal(clue, focal):
    spec = TWO_FOCAL_SPECS[focal]
    family = two_family(clue)
    direction = two_direction(clue)

    if focal == "reverse_implication":
        return family in ("imp_pos", "imp_neg") and direction == "rev"

    return (
        family == spec["family"]
        and (
            spec["direction"] is None
            or direction == spec["direction"]
        )
    )


def valid_support(clue, focal):
    spec = TWO_FOCAL_SPECS[focal]

    if is_focal(clue, focal):
        return False

    family = two_family(clue)
    if family not in spec["support"]:
        return False

    # Reverse implication wording is itself a later concept. Before that concept
    # is introduced, implication support must remain forward-direction.
    if family in ("imp_pos", "imp_neg") and two_direction(clue) != "fwd":
        return False

    return True


def two_surface_has_intro(model, target, surface, focal, exact_half=False):
    valid = two_valid_clues(model, target, surface, exact_half=exact_half)
    focal_rows = [row for row in valid if is_focal(row[0], focal)]
    support_rows = [row for row in valid if valid_support(row[0], focal)]

    for focal_row in focal_rows:
        for support in support_rows:
            if unique_and_necessary(
                [focal_row[1], support[1]],
                surface.bit_count(),
            ):
                return True

        for first, second in itertools.combinations(support_rows, 2):
            if unique_and_necessary(
                [focal_row[1], first[1], second[1]],
                surface.bit_count(),
            ):
                return True

    return False


def two_surface_has_breathe(model, target, surface, exact_half=False):
    valid = [
        row
        for row in two_valid_clues(
            model,
            target,
            surface,
            exact_half=exact_half,
        )
        if two_family(row[0]) in ("literal", "count")
    ]

    for count in (2, 3):
        for combo in itertools.combinations(valid, count):
            if unique_and_necessary(
                [row[1] for row in combo],
                surface.bit_count(),
            ):
                return True

    return False


def screen_two(data):
    model = two.Model(data)

    outputs = {row["output"] for row in model.formulas}
    if len(model.formulas) != 16 or len(outputs) != 10:
        raise ValueError(
            "Expected filtered mandatory two-slot core: "
            "16 variants / 10 outputs."
        )

    metrics = ["breathe"] + list(TWO_FOCAL_SPECS)
    normal_rates = {metric: [] for metric in metrics}
    half_rates = {metric: [] for metric in metrics}

    for row in model.formulas:
        target = (row["powder"], row["fluid"])
        total = 0
        normal_hits = Counter()
        half_hits = Counter()

        for powders in two.surfaces(model.powders, target[0], 2):
            for fluids in two.surfaces(model.fluids, target[1], 2):
                total += 1
                surface = model.surface_mask(powders, fluids)

                if two_surface_has_breathe(model, target, surface):
                    normal_hits["breathe"] += 1
                if two_surface_has_breathe(
                    model,
                    target,
                    surface,
                    exact_half=True,
                ):
                    half_hits["breathe"] += 1

                for focal in TWO_FOCAL_SPECS:
                    if two_surface_has_intro(
                        model,
                        target,
                        surface,
                        focal,
                    ):
                        normal_hits[focal] += 1
                    if two_surface_has_intro(
                        model,
                        target,
                        surface,
                        focal,
                        exact_half=True,
                    ):
                        half_hits[focal] += 1

        for metric in metrics:
            normal_rates[metric].append(normal_hits[metric] / total)
            half_rates[metric].append(half_hits[metric] / total)

    def aggregate(rows):
        return {
            metric: {
                "variants_serviceable": sum(value > 0 for value in values),
                "rate": summarize(values),
            }
            for metric, values in rows.items()
        }

    return {
        "scope": {
            "formula_variants": len(model.formulas),
            "outputs": len(outputs),
            "first_role_candidate_identities": len(model.powders),
            "second_role_candidate_identities": len(model.fluids),
            "surface": "2x2",
            "important_limit": (
                "Candidate identities are intentionally limited to identities "
                "present in the mandatory core input, making this a conservative "
                "serviceability lower-bound relative to the larger ordinary pool."
            ),
        },
        "accepted_compact_envelope": aggregate(normal_rates),
        "sensitivity_exact_2_of_4_per_clue": aggregate(half_rates),
    }


def simple_three_clues(model, target, surface):
    triples = tuple(itertools.product(*surface))
    target_index = triples.index(target)
    result = {}

    for slot_index, slot in enumerate(("P", "F", "E")):
        for tag in model.vocabulary:
            expected = tag in model.tags[target[slot_index]]
            mask = 0
            for index, triple in enumerate(triples):
                if (tag in model.tags[triple[slot_index]]) == expected:
                    mask |= 1 << index
            if mask >> target_index & 1:
                result.setdefault(mask, ("literal", slot, tag, expected))

    for tag in model.vocabulary:
        expected = sum(tag in model.tags[item] for item in target)
        mask = 0
        for index, triple in enumerate(triples):
            if sum(tag in model.tags[item] for item in triple) == expected:
                mask |= 1 << index
        if mask >> target_index & 1:
            result.setdefault(mask, ("count", tag, expected))

    return [
        (clue, mask)
        for mask, clue in result.items()
        if 3 <= mask.bit_count() <= 7
    ], triples


def purposeful_relation_resolution(model, target, triples, mask):
    live = [
        triple
        for index, triple in enumerate(triples)
        if mask >> index & 1
    ]
    if len(live) != 2 or target not in live:
        return None

    other = live[0] if live[1] == target else live[1]
    differing = [
        index
        for index in range(3)
        if other[index] != target[index]
    ]

    if differing == [0]:
        if (
            (target[0], target[1]) in model.stable_pf
            and (other[0], other[1]) not in model.stable_pf
        ):
            return "PF"

    if differing == [2]:
        if (
            (target[1], target[2]) in model.stable_fe
            and (other[1], other[2]) not in model.stable_fe
        ):
            return "FE"

    return None


def three_surface_relation_tutorial(model, target, surface):
    clues, triples = simple_three_clues(model, target, surface)

    for first, second in itertools.combinations(clues, 2):
        live = first[1] & second[1]
        if live.bit_count() != 2:
            continue

        orientation = purposeful_relation_resolution(
            model,
            target,
            triples,
            live,
        )
        if orientation is not None:
            return orientation

    return None


def screen_three_relation_tutorial(model):
    rates = []
    orientation_variants = Counter()
    orientation_surface_hits = Counter()

    for formula in model.formulas:
        target = formula.triple
        total = 0
        hits = 0
        local_orientations = Counter()

        for powder in (
            item for item in model.powders if item != target[0]
        ):
            for fluid in (
                item for item in model.fluids if item != target[1]
            ):
                for essence in (
                    item for item in model.essences if item != target[2]
                ):
                    surface = (
                        tuple(sorted((target[0], powder))),
                        tuple(sorted((target[1], fluid))),
                        tuple(sorted((target[2], essence))),
                    )
                    total += 1

                    orientation = three_surface_relation_tutorial(
                        model,
                        target,
                        surface,
                    )
                    if orientation is not None:
                        hits += 1
                        local_orientations[orientation] += 1
                        orientation_surface_hits[orientation] += 1

        rates.append(hits / total)
        for orientation in ("PF", "FE"):
            if local_orientations[orientation]:
                orientation_variants[orientation] += 1

    return {
        "variants_serviceable": sum(value > 0 for value in rates),
        "serviceable_surface_rate": summarize(rates),
        "orientation_variants_serviceable": dict(orientation_variants),
        "orientation_surface_hits": dict(orientation_surface_hits),
        "contract": (
            "2x2x2; exactly two familiar literal/count clues; each clue alone "
            "leaves 3-7 triples; together they leave exactly two hypotheses "
            "differing only in Powder or Essence; one adjacent relation test "
            "can eliminate the non-target continuation."
        ),
    }


def screen_three_reasoning(model, surfaces, packages, seed):
    options = reasoning.build_options(
        model,
        model.tags,
        surfaces,
        packages,
        seed,
    )

    roots = ("literal", "count", "xor", "imp_pos", "imp_neg")
    result = {}

    for root in roots:
        counts = []
        for rows in options:
            counts.append(
                sum(
                    root in {
                        reasoning.family_root(family)
                        for family in row["families"]
                    }
                    for row in rows
                )
            )

        result[root] = {
            "variants_serviceable": sum(count > 0 for count in counts),
            "retained_option_count": summarize(counts),
        }

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("two_json", type=Path)
    parser.add_argument("three_json", type=Path)
    parser.add_argument("--reasoning-surfaces", type=int, default=70)
    parser.add_argument("--reasoning-packages", type=int, default=450)
    parser.add_argument("--seed", type=int, default=20261011)
    args = parser.parse_args()

    two_data = load_json(args.two_json)
    three_model = three.load_model(args.three_json)
    three.assert_accepted_baseline(three_model)

    vocabulary = set(
        tag
        for values in three_model.tags.values()
        for tag in values
    )
    if not {"Dark", "Organ"} <= vocabulary:
        raise ValueError(
            "Current accepted Dark + Organ property model is required."
        )

    report = {
        "screen": "curriculum-serviceability",
        "question": (
            "Can a player-selected target variant serve the desired curriculum "
            "beat without forcing the scheduler to choose another recipe?"
        ),
        "two_slot": screen_two(two_data),
        "three_slot": {
            "relation_introduction": screen_three_relation_tutorial(
                three_model
            ),
            "later_reasoning_family_capacity": screen_three_reasoning(
                three_model,
                args.reasoning_surfaces,
                args.reasoning_packages,
                args.seed,
            ),
        },
        "important_limits": [
            "This is structural serviceability, not a player-choice simulator.",
            "It does not model progression-limited identity knowledge.",
            "It does not model accumulated learned-relation history.",
            "Later bridge/residual relation-topology introductions are not "
            "classified as separate curriculum concepts in this screen.",
        ],
    }

    print(json.dumps(
        report,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()
