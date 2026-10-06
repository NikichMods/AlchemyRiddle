#!/usr/bin/env python3
"""Progression-core property/sequence diversity screen for AlchemyRiddle.

Research-only helper. Exact vanilla formula rows stay in private/ephemeral JSON.

Usage:
  python property_sequence_diversity_screen.py TWO.json THREE.json OPTIONAL.json

TWO/THREE use the existing TagModelScreen schemas. OPTIONAL is a JSON array of
output IDs excluded from the mandatory progression core.

The screen:
- asserts the accepted two-/three-slot structural baselines;
- removes optional targets from the core sequence;
- builds late-style good-surface banks:
  * two-slot: 3x3, strict weak-clue composite unique;
  * three-slot: 3x3x3, accepted strong progression criterion;
- measures whether good fields prefer richer reagents after opportunity
  normalization;
- compares random surface selection with a simple anti-repetition selector over
  randomized within-arity formula-variant sequences.

Outputs aggregate metrics only.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import two_slot_tag_constraint_screen as two
import progression_variable_field_screen as three


DEFAULT_SEED = 20261006


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def signature(tags, item):
    return tuple(sorted(tags[item]))


def flatten(surface):
    return set(itertools.chain.from_iterable(surface))


def sample_bank(values, size, rng):
    values = list(values)
    if len(values) <= size:
        return values
    return rng.sample(values, size)


def build_two_bank(model, formula, bank_size, rng):
    target = (formula["powder"], formula["fluid"])
    masks = two.clue_masks(model, target, "composite")
    good = []
    for ps in two.surfaces(model.powders, target[0], 3):
        for fs in two.surfaces(model.fluids, target[1], 3):
            category = two.classify(
                model,
                target,
                model.surface_mask(ps, fs),
                masks,
                "strict",
            )
            if category in ("unique_2", "unique_3"):
                good.append((tuple(sorted(ps)), tuple(sorted(fs))))
    if not good:
        raise RuntimeError("No strict unique two-slot 3x3 surface")
    return sample_bank(good, bank_size, rng), len(good)


def build_three_bank(model, formula, bank_size, rng):
    target = formula.triple
    good = []
    seen = set()
    attempts = 0
    max_attempts = max(20000, bank_size * 50)
    while attempts < max_attempts and len(good) < bank_size:
        attempts += 1
        surface = three.random_surface(model, target, (3, 3, 3), rng)
        if surface in seen:
            continue
        seen.add(surface)
        if three.surface_passes(model, target, surface, 4):
            good.append(surface)
    if len(good) < bank_size:
        raise RuntimeError(
            "Could not sample requested strong three-slot surface bank: "
            f"{len(good)}/{bank_size}"
        )
    return good


def opportunity_rates(records, banks, role_universes, tag_map):
    occurrence = Counter()
    opportunity = Counter()

    for key, target in records:
        bank = banks[key]
        for role_index, universe in enumerate(role_universes):
            for item in universe:
                if item != target[role_index]:
                    opportunity[item] += len(bank)
        target_set = set(target)
        for surface in bank:
            for item in flatten(surface) - target_set:
                occurrence[item] += 1

    by_depth = defaultdict(list)
    for item, possible in opportunity.items():
        if possible:
            by_depth[len(tag_map[item])].append(occurrence[item] / possible)

    return {
        str(depth): {
            "items": len(values),
            "mean_inclusion_probability": statistics.mean(values),
            "median_inclusion_probability": statistics.median(values),
            "minimum": min(values),
            "maximum": max(values),
        }
        for depth, values in sorted(by_depth.items())
    }


def run_sequence(records, banks, tag_map, seed, window, mode):
    rng = random.Random(seed)
    order = list(records)
    rng.shuffle(order)

    recent_items = []
    recent_signatures = []
    visible_use = Counter()
    distractor_use = Counter()

    chosen_surfaces = []
    chosen_identity_overlap = []
    chosen_signature_overlap = []
    minimum_identity_overlap = []
    zero_reserve_steps = 0

    for key, target in order:
        bank = banks[key]
        target_set = set(target)
        recent = set().union(*recent_items[-window:]) if recent_items else set()
        recent_sig = (
            set().union(*recent_signatures[-window:])
            if recent_signatures else set()
        )

        candidates = []
        zeros = 0
        for surface in bank:
            distractors = flatten(surface) - target_set
            identity_overlap = len(distractors & recent)
            if identity_overlap == 0:
                zeros += 1
            signature_overlap = sum(
                signature(tag_map, item) in recent_sig for item in distractors
            )
            cumulative = sum(distractor_use[item] for item in distractors)
            max_use = max(
                (distractor_use[item] for item in distractors),
                default=0,
            )
            candidates.append(
                (
                    identity_overlap,
                    signature_overlap,
                    cumulative,
                    max_use,
                    surface,
                )
            )

        minimum_identity_overlap.append(min(x[0] for x in candidates))
        zero_reserve_steps += int(zeros == 0)

        if mode == "random":
            chosen = rng.choice(candidates)
        else:
            score = min(x[:4] for x in candidates)
            chosen = rng.choice([x for x in candidates if x[:4] == score])

        identity_overlap, signature_overlap, _, _, surface = chosen
        chosen_identity_overlap.append(identity_overlap)
        chosen_signature_overlap.append(signature_overlap)

        visible = flatten(surface)
        distractors = visible - target_set
        for item in visible:
            visible_use[item] += 1
        for item in distractors:
            distractor_use[item] += 1

        recent_items.append(visible)
        recent_signatures.append({signature(tag_map, x) for x in visible})
        chosen_surfaces.append(surface)

    total_visible = sum(len(flatten(x)) for x in chosen_surfaces)
    total_distractors = sum(
        len(flatten(surface) - set(target))
        for (_, target), surface in zip(order, chosen_surfaces)
    )
    jaccards = []
    for a, b in zip(chosen_surfaces, chosen_surfaces[1:]):
        aa, bb = flatten(a), flatten(b)
        jaccards.append(len(aa & bb) / len(aa | bb))

    return {
        "mean_minimum_recent_identity_overlap": statistics.mean(
            minimum_identity_overlap
        ),
        "maximum_minimum_recent_identity_overlap": max(
            minimum_identity_overlap
        ),
        "mean_chosen_recent_identity_overlap": statistics.mean(
            chosen_identity_overlap
        ),
        "maximum_chosen_recent_identity_overlap": max(
            chosen_identity_overlap
        ),
        "mean_chosen_recent_signature_overlap": statistics.mean(
            chosen_signature_overlap
        ),
        "steps_with_no_zero_identity_overlap_surface": zero_reserve_steps,
        "top5_visible_identity_share": (
            sum(x for _, x in visible_use.most_common(5)) / total_visible
        ),
        "top5_distractor_identity_share": (
            sum(x for _, x in distractor_use.most_common(5))
            / total_distractors
        ),
        "maximum_visible_identity_uses": max(visible_use.values()),
        "maximum_distractor_identity_uses": max(distractor_use.values()),
        "mean_consecutive_surface_jaccard": (
            statistics.mean(jaccards) if jaccards else 0.0
        ),
    }


def summarize_runs(rows):
    result = {}
    for key in rows[0]:
        values = [row[key] for row in rows]
        result[key] = {
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "minimum": min(values),
            "maximum": max(values),
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("two_json", type=Path)
    parser.add_argument("three_json", type=Path)
    parser.add_argument("optional_outputs_json", type=Path)
    parser.add_argument("--bank-size", type=int, default=512)
    parser.add_argument("--sequences", type=int, default=200)
    parser.add_argument("--recent-window", type=int, default=2)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()

    two_raw = load_json(args.two_json)
    optional_outputs = set(load_json(args.optional_outputs_json))

    two.assert_baseline(two_raw)
    two_model = two.Model(two_raw)
    three_model = three.load_model(args.three_json)
    three.assert_accepted_baseline(three_model)

    all_outputs = {x["output"] for x in two_raw["formulas"]} | {
        x.output for x in three_model.formulas
    }
    unknown_optional = optional_outputs - all_outputs
    if unknown_optional:
        raise ValueError(
            "Optional output IDs absent from formula corpus: "
            + ", ".join(sorted(unknown_optional))
        )
    if len(optional_outputs) != 8:
        raise ValueError(
            f"Expected 8 optional progression outputs, got {len(optional_outputs)}"
        )

    core_two = [
        row for row in two_raw["formulas"]
        if row["output"] not in optional_outputs
    ]
    core_three = [
        row for row in three_model.formulas
        if row.output not in optional_outputs
    ]

    rng = random.Random(args.seed)

    two_banks = {}
    two_full_counts = {}
    for index, row in enumerate(core_two):
        key = ("two", index)
        bank, full_count = build_two_bank(
            two_model, row, args.bank_size, rng
        )
        two_banks[key] = bank
        two_full_counts[key] = full_count

    three_banks = {}
    for index, row in enumerate(core_three):
        key = ("three", index)
        three_banks[key] = build_three_bank(
            three_model, row, args.bank_size, rng
        )

    two_records = [
        (("two", index), (row["powder"], row["fluid"]))
        for index, row in enumerate(core_two)
    ]
    three_records = [
        (("three", index), row.triple)
        for index, row in enumerate(core_three)
    ]

    richness = {
        "two_slot": opportunity_rates(
            two_records,
            two_banks,
            [two_model.powders, two_model.fluids],
            two_model.tags,
        ),
        "three_slot": opportunity_rates(
            three_records,
            three_banks,
            [
                three_model.powders,
                three_model.fluids,
                three_model.essences,
            ],
            three_model.tags,
        ),
    }

    sequence_results = {}
    for label, records, banks, tag_map in (
        ("two_slot", two_records, two_banks, two_model.tags),
        ("three_slot", three_records, three_banks, three_model.tags),
    ):
        sequence_results[label] = {}
        for mode in ("random", "anti_repeat"):
            rows = [
                run_sequence(
                    records,
                    banks,
                    tag_map,
                    args.seed + i * 17,
                    args.recent_window,
                    mode,
                )
                for i in range(args.sequences)
            ]
            sequence_results[label][mode] = summarize_runs(rows)

    report = {
        "screen": "property-depth-sequence-diversity-control",
        "method": {
            "two_slot_surface": "3x3 strict composite unique",
            "three_slot_surface": (
                "3x3x3 accepted strong progression criterion; sampled bank"
            ),
            "bank_size": args.bank_size,
            "randomized_sequences": args.sequences,
            "recent_window": args.recent_window,
            "anti_repeat_priority": (
                "avoidable distractor identity overlap, then signature overlap, "
                "then cumulative distractor reuse"
            ),
            "important_limit": (
                "Formula variants are sequence tasks. This is a structural "
                "control screen, not a canonical story chronology."
            ),
        },
        "baseline": {
            "two_slot_variants": len(two_raw["formulas"]),
            "two_slot_outputs": len({x["output"] for x in two_raw["formulas"]}),
            "three_slot_variants": len(three_model.formulas),
            "three_slot_outputs": len({x.output for x in three_model.formulas}),
            "optional_outputs_excluded_from_progression_core": len(optional_outputs),
            "core_two_slot_variants": len(core_two),
            "core_two_slot_outputs": len({x["output"] for x in core_two}),
            "core_three_slot_variants": len(core_three),
            "core_three_slot_outputs": len({x.output for x in core_three}),
        },
        "good_surface_bank": {
            "two_slot_full_good_surface_count": {
                "minimum": min(two_full_counts.values()),
                "median": statistics.median(two_full_counts.values()),
                "maximum": max(two_full_counts.values()),
            },
            "three_slot_sampled_good_surfaces_per_variant": args.bank_size,
        },
        "richness_opportunity_normalized": richness,
        "sequence": sequence_results,
    }

    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
