#!/usr/bin/env python3
"""Compare accepted Dark model against Dark + Organ.

Research-only. Exact formula rows and tag-overlay membership stay in private /
ephemeral JSON. The committed helper prints aggregate metrics only.

Usage:
  python dark_organ_comparison_screen.py THREE.json OVERLAYS.json

OVERLAYS schema:
{
  "dark": ["ingredient-name", ...],
  "organ": ["ingredient-name", ...]
}
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import replace
from pathlib import Path

import progression_variable_field_screen as base
import property_sequence_diversity_screen as seq
import reasoning_diversity_screen as reasoning


def load_overlay(path: Path):
    raw = json.loads(path.read_text(encoding="utf-8"))
    return set(raw["dark"]), set(raw["organ"])


def apply_tags(model: base.Model, dark: set[str], organ: set[str]):
    tags = {name: set(values) for name, values in model.tags.items()}
    missing = (dark | organ) - set(tags)
    if missing:
        raise ValueError(
            "Overlay names absent from private model: "
            + ", ".join(sorted(missing))
        )
    for name in dark:
        tags[name].add("Dark")
    for name in organ:
        tags[name].add("Organ")
    frozen = {name: frozenset(values) for name, values in tags.items()}
    return replace(model, tags=frozen)


def sampled_pass_rates(model: base.Model, samples: int, seed: int):
    rng = random.Random(seed)
    rates = []
    for formula in model.formulas:
        seen = set()
        good = 0
        while len(seen) < samples:
            surface = seq.random_surface(
                model, formula.triple, (3, 3, 3), rng
            )
            if surface in seen:
                continue
            seen.add(surface)
            good += seq.surface_passes(
                model, formula.triple, surface, 4
            )
        rates.append(good / samples)
    return {
        "minimum": min(rates),
        "median": statistics.median(rates),
        "mean": statistics.mean(rates),
        "maximum": max(rates),
    }


def signature_stats(model: base.Model):
    counts = {}
    for values in model.tags.values():
        key = tuple(sorted(values))
        counts[key] = counts.get(key, 0) + 1
    return {
        "distinct_signatures": len(counts),
        "duplicate_multiplicities": sorted(
            (value for value in counts.values() if value > 1),
            reverse=True,
        ),
    }


def sequence_stats(model: base.Model, bank_size: int, runs: int, seed: int):
    rng = random.Random(seed)
    banks = {}
    for formula in model.formulas:
        good = []
        seen = set()
        while len(good) < bank_size:
            surface = base.random_surface(
                model, formula.triple, (3, 3, 3), rng
            )
            if surface in seen:
                continue
            seen.add(surface)
            if base.surface_passes(
                model, formula.triple, surface, 4
            ):
                good.append(surface)
        banks[formula] = good

    rows = []
    records = [(formula, formula.triple) for formula in model.formulas]
    for index in range(runs):
        rows.append(
            seq.run_sequence(
                records,
                banks,
                model.tags,
                seed + index * 17,
                2,
                "anti_repeat",
            )
        )
    return seq.summarize_runs(rows)


def reasoning_stats(
    model: base.Model,
    surfaces: int,
    packages: int,
    sequences: int,
    seed: int,
):
    options = reasoning.build_options(
        model, model.tags, surfaces, packages, seed
    )
    return {
        "option_diversity": reasoning.summarize_options(options),
        "anti_clump_sequence": reasoning.summarize_sequences(
            options, sequences, seed + 1
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("three_json", type=Path)
    parser.add_argument("overlays_json", type=Path)
    parser.add_argument("--surface-samples", type=int, default=1000)
    parser.add_argument("--bank-size", type=int, default=512)
    parser.add_argument("--sequence-runs", type=int, default=200)
    parser.add_argument("--reasoning-surfaces", type=int, default=70)
    parser.add_argument("--reasoning-packages", type=int, default=450)
    parser.add_argument("--seed", type=int, default=20261010)
    args = parser.parse_args()

    raw = base.load_model(args.three_json)
    base.assert_accepted_baseline(raw)
    dark, organ = load_overlay(args.overlays_json)

    model_a = apply_tags(raw, dark, set())
    model_b = apply_tags(raw, dark, organ)

    report = {}
    for label, model in (
        ("dark", model_a),
        ("dark_plus_organ", model_b),
    ):
        report[label] = {
            "signature_stats": signature_stats(model),
            "strong_surface_rate": sampled_pass_rates(
                model, args.surface_samples, args.seed
            ),
            "sequence": sequence_stats(
                model, args.bank_size, args.sequence_runs, args.seed
            ),
            "reasoning": reasoning_stats(
                model,
                args.reasoning_surfaces,
                args.reasoning_packages,
                args.sequence_runs,
                args.seed,
            ),
        }

    print(json.dumps(
        report, ensure_ascii=False, indent=2, sort_keys=True
    ))


if __name__ == "__main__":
    main()
