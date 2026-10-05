#!/usr/bin/env python3
"""AlchemyRiddle two-slot tag-constraint capacity screen.

Research-only helper. Exact vanilla formulas stay in private/ephemeral JSON.
The helper emits structural and aggregate metrics only.

Input:
{
  "ingredients": [{"name": "...", "tags": ["..."]}],
  "formulas": [{"output": "...", "powder": "...", "fluid": "..."}]
}

The role names powder/fluid mean the first/second tier-I alchemy slots; vanilla
Universal reagents may legitimately occupy either role.

Grammars:
- simple: slot-local target-true presence/absence + exact pair tag counts;
- composite: simple + cross-slot XOR + active cross-slot implications whose
  antecedent is true on the hidden target. Vacuous target implications are
  deliberately excluded.

Weakness policies:
- strict: each clue alone leaves ceil(2V/3)..V-1 candidates;
- compact: each clue alone leaves max(2, ceil(V/2))..V-1 candidates.

A 2- or 3-clue set is retained only if every clue is necessary. Unique
resolution is preferred; exactly-two survivors are the bounded fallback.
"""

import argparse
import itertools
import json
import math
import statistics
from collections import Counter


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def assert_baseline(data):
    formulas = data["formulas"]
    outputs = Counter(row["output"] for row in formulas)
    powders = {row["powder"] for row in formulas}
    fluids = {row["fluid"] for row in formulas}

    checks = {
        "formula variants": (len(formulas), 24),
        "outputs": (len(outputs), 18),
        "multi-formula outputs": (sum(v > 1 for v in outputs.values()), 4),
        "max formulas/output": (max(outputs.values()), 3),
        "first-slot participants": (len(powders), 15),
        "second-slot participants": (len(fluids), 9),
    }
    for label, (actual, expected) in checks.items():
        if actual != expected:
            raise AssertionError(
                "{}: expected {}, got {}".format(label, expected, actual)
            )

    pairs = [(row["powder"], row["fluid"]) for row in formulas]
    neighbor_count = sum(
        any(
            i != j
            and sum(a != b for a, b in zip(pair, other)) == 1
            for j, other in enumerate(pairs)
        )
        for i, pair in enumerate(pairs)
    )
    if neighbor_count != 23:
        raise AssertionError(
            "expected 23/24 Hamming-1-neighbor variants, got {}/24".format(
                neighbor_count
            )
        )


class Model:
    def __init__(self, data):
        self.formulas = list(data["formulas"])
        self.tags = {
            row["name"]: set(row["tags"])
            for row in data["ingredients"]
        }
        self.powders = sorted({row["powder"] for row in self.formulas})
        self.fluids = sorted({row["fluid"] for row in self.formulas})
        participants = set(self.powders) | set(self.fluids)
        missing = sorted(participants - set(self.tags))
        if missing:
            raise ValueError("missing tag rows: " + ", ".join(missing))

        self.vocabulary = sorted(
            {tag for name in participants for tag in self.tags[name]}
        )
        self.pairs = [
            (powder, fluid)
            for powder in self.powders
            for fluid in self.fluids
        ]
        self.index = {pair: i for i, pair in enumerate(self.pairs)}

    def has(self, item, tag):
        return tag in self.tags[item]

    def surface_mask(self, powders, fluids):
        mask = 0
        for powder in powders:
            for fluid in fluids:
                mask |= 1 << self.index[(powder, fluid)]
        return mask


def target_clues(model, target, grammar):
    powder, fluid = target
    clues = []

    for tag in model.vocabulary:
        clues.append(("literal", "P", tag, model.has(powder, tag)))
        clues.append(("literal", "F", tag, model.has(fluid, tag)))
        clues.append(
            (
                "count",
                tag,
                int(model.has(powder, tag)) + int(model.has(fluid, tag)),
            )
        )

    if grammar == "simple":
        return clues
    if grammar != "composite":
        raise ValueError("unknown grammar: " + grammar)

    for ptag in model.vocabulary:
        for ftag in model.vocabulary:
            if model.has(powder, ptag) != model.has(fluid, ftag):
                clues.append(("xor", ptag, ftag))

    for ptag in model.vocabulary:
        if model.has(powder, ptag):
            for ftag in model.vocabulary:
                clues.append(
                    ("imp_pf", ptag, ftag, model.has(fluid, ftag))
                )

    for ftag in model.vocabulary:
        if model.has(fluid, ftag):
            for ptag in model.vocabulary:
                clues.append(
                    ("imp_fp", ftag, ptag, model.has(powder, ptag))
                )

    return clues


def eval_clue(model, clue, pair):
    powder, fluid = pair
    kind = clue[0]

    if kind == "literal":
        _, slot, tag, expected = clue
        item = powder if slot == "P" else fluid
        return model.has(item, tag) == expected

    if kind == "count":
        _, tag, expected = clue
        return (
            int(model.has(powder, tag)) + int(model.has(fluid, tag))
            == expected
        )

    if kind == "xor":
        _, ptag, ftag = clue
        return model.has(powder, ptag) != model.has(fluid, ftag)

    if kind == "imp_pf":
        _, ptag, ftag, expected = clue
        return (
            not model.has(powder, ptag)
            or model.has(fluid, ftag) == expected
        )

    if kind == "imp_fp":
        _, ftag, ptag, expected = clue
        return (
            not model.has(fluid, ftag)
            or model.has(powder, ptag) == expected
        )

    raise ValueError("unknown clue: " + repr(clue))


def clue_masks(model, target, grammar):
    target_bit = 1 << model.index[target]
    masks = set()

    for clue in target_clues(model, target, grammar):
        mask = 0
        for i, pair in enumerate(model.pairs):
            if eval_clue(model, clue, pair):
                mask |= 1 << i
        if not mask & target_bit:
            raise AssertionError("target-false clue generated")
        masks.add(mask)

    return list(masks)


def weak_floor(volume, policy):
    if policy == "strict":
        return math.ceil(2 * volume / 3)
    if policy == "compact":
        return max(2, math.ceil(volume / 2))
    raise ValueError("unknown policy: " + policy)


def classify(model, target, surface, masks, policy):
    volume = surface.bit_count()
    target_bit = 1 << model.index[target]
    floor = weak_floor(volume, policy)

    eliminations = set()
    for clue_mask in masks:
        survivors = surface & clue_mask
        count = survivors.bit_count()
        if floor <= count <= volume - 1 and survivors & target_bit:
            eliminated = surface & ~clue_mask
            if eliminated:
                eliminations.add(eliminated)

    eliminations = list(eliminations)
    residual_two_with_two = False

    for i, first in enumerate(eliminations):
        for second in eliminations[i + 1 :]:
            if not (first & ~second) or not (second & ~first):
                continue
            remaining = volume - (first | second).bit_count()
            if remaining == 1:
                return "unique_2"
            if remaining == 2:
                residual_two_with_two = True

    residual_two_with_three = False
    for i in range(len(eliminations)):
        first = eliminations[i]
        for j in range(i + 1, len(eliminations)):
            second = eliminations[j]
            for k in range(j + 1, len(eliminations)):
                third = eliminations[k]
                union = first | second | third
                remaining = volume - union.bit_count()
                if remaining not in (1, 2):
                    continue

                # Every clue must eliminate at least one candidate that the
                # other two would leave alive.
                if not (first & ~(second | third)):
                    continue
                if not (second & ~(first | third)):
                    continue
                if not (third & ~(first | second)):
                    continue

                if remaining == 1:
                    return "unique_3"
                residual_two_with_three = True

    if residual_two_with_two:
        return "residual2_2"
    if residual_two_with_three:
        return "residual2_3"
    return "none"


def surfaces(universe, required, size):
    extras = [item for item in universe if item != required]
    for chosen in itertools.combinations(extras, size - 1):
        yield (required,) + chosen


def rates(values):
    return {
        "minimum": min(values) if values else 0.0,
        "median": statistics.median(values) if values else 0.0,
        "maximum": max(values) if values else 0.0,
    }


def screen_shape(model, shape, grammar, policy):
    pcount, fcount = shape
    aggregate = Counter()
    unique_rates = []
    bounded_rates = []

    for row in model.formulas:
        target = (row["powder"], row["fluid"])
        masks = clue_masks(model, target, grammar)
        local = Counter()
        count = 0

        for ps in surfaces(model.powders, target[0], pcount):
            for fs in surfaces(model.fluids, target[1], fcount):
                count += 1
                category = classify(
                    model,
                    target,
                    model.surface_mask(ps, fs),
                    masks,
                    policy,
                )
                local[category] += 1

        aggregate.update(local)
        unique = local["unique_2"] + local["unique_3"]
        bounded = (
            unique + local["residual2_2"] + local["residual2_3"]
        )
        unique_rates.append(unique / count)
        bounded_rates.append(bounded / count)

    total = sum(aggregate.values())
    unique = aggregate["unique_2"] + aggregate["unique_3"]
    bounded = (
        unique + aggregate["residual2_2"] + aggregate["residual2_3"]
    )

    return {
        "shape": "{}x{}".format(pcount, fcount),
        "surface_instances": total,
        "category_counts": dict(sorted(aggregate.items())),
        "unique_surface_rate": unique / total,
        "bounded_at_most_two_surface_rate": bounded / total,
        "variants_with_any_unique_surface": sum(x > 0 for x in unique_rates),
        "variants_with_any_bounded_surface": sum(x > 0 for x in bounded_rates),
        "per_variant_unique_surface_rate": rates(unique_rates),
        "per_variant_bounded_surface_rate": rates(bounded_rates),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--assert-two-slot-baseline", action="store_true")
    parser.add_argument("--grammars", default="simple,composite")
    parser.add_argument("--policies", default="strict,compact")
    parser.add_argument("--shapes", default="2x2,2x3,3x2,3x3")
    args = parser.parse_args()

    data = load(args.input)
    if args.assert_two_slot_baseline:
        assert_baseline(data)

    model = Model(data)
    grammars = [x.strip() for x in args.grammars.split(",") if x.strip()]
    policies = [x.strip() for x in args.policies.split(",") if x.strip()]
    shapes = [
        tuple(int(v) for v in raw.lower().split("x", 1))
        for raw in args.shapes.split(",")
    ]

    outputs = Counter(row["output"] for row in model.formulas)
    report = {
        "baseline": {
            "formula_variants": len(model.formulas),
            "outputs": len(outputs),
            "multi_formula_outputs": sum(v > 1 for v in outputs.values()),
            "max_formulas_per_output": max(outputs.values()),
            "first_slot_participants": len(model.powders),
            "second_slot_participants": len(model.fluids),
            "tag_vocabulary_size": len(model.vocabulary),
        },
        "grammar": {
            "simple": [
                "slot-local target-true presence/absence",
                "exact pair tag count",
            ],
            "composite_additions": [
                "cross-slot XOR / exact-one-of-two",
                "active cross-slot implication with signed consequent",
            ],
            "vacuous_target_implications": "excluded",
        },
        "policy": {
            "strict": "each clue alone leaves ceil(2V/3)..V-1",
            "compact": "each clue alone leaves max(2,ceil(V/2))..V-1",
        },
        "screens": {},
    }

    for policy in policies:
        report["screens"][policy] = {}
        for grammar in grammars:
            report["screens"][policy][grammar] = [
                screen_shape(model, shape, grammar, policy)
                for shape in shapes
            ]

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
