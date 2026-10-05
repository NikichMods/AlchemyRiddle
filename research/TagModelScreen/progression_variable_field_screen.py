#!/usr/bin/env python3
"""Progression-aware variable-field screen for AlchemyRiddle.

Consumes the same private JSON shape as the TagModelScreen tools. Exact vanilla
formula rows stay outside the repository; output is aggregate by default.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Set, Tuple

Triple = Tuple[str, str, str]
Surface = Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[str, ...]]
Relation = Tuple[str, str, str]


@dataclass(frozen=True)
class Formula:
    output: str
    powder: str
    fluid: str
    essence: str

    @property
    def triple(self) -> Triple:
        return self.powder, self.fluid, self.essence


@dataclass(frozen=True)
class Config:
    orientation: str
    fact_count: int
    survivors: FrozenSet[Triple]


@dataclass
class Model:
    formulas: List[Formula]
    tags: Dict[str, FrozenSet[str]]
    powders: Tuple[str, ...]
    fluids: Tuple[str, ...]
    essences: Tuple[str, ...]
    vocabulary: Tuple[str, ...]
    stable_pf: FrozenSet[Tuple[str, str]]
    stable_fe: FrozenSet[Tuple[str, str]]
    counts: Dict[Triple, Tuple[int, ...]]


def load_model(path: Path) -> Model:
    raw = json.loads(path.read_text(encoding="utf-8"))
    tags = {x["name"]: frozenset(x.get("tags", [])) for x in raw["ingredients"]}
    formulas = [Formula(**x) for x in raw["formulas"]]
    powders = tuple(sorted({x.powder for x in formulas}))
    fluids = tuple(sorted({x.fluid for x in formulas}))
    essences = tuple(sorted({x.essence for x in formulas}))
    vocabulary = tuple(sorted(set().union(*(tags[x] for x in tags))))
    missing = sorted({y for x in formulas for y in x.triple if y not in tags})
    if missing:
        raise ValueError(f"Missing tag records for formula ingredients: {missing}")
    stable_pf = frozenset((x.powder, x.fluid) for x in formulas)
    stable_fe = frozenset((x.fluid, x.essence) for x in formulas)
    counts = {}
    for triple in itertools.product(powders, fluids, essences):
        counts[triple] = tuple(
            sum(tag in tags[item] for item in triple) for tag in vocabulary
        )
    return Model(
        formulas,
        tags,
        powders,
        fluids,
        essences,
        vocabulary,
        stable_pf,
        stable_fe,
        counts,
    )


def assert_accepted_baseline(m: Model) -> None:
    outputs = {x.output for x in m.formulas}
    compatible = sum(
        (p, f) in m.stable_pf and (f, e) in m.stable_fe
        for p, f, e in itertools.product(m.powders, m.fluids, m.essences)
    )
    got = (
        len(m.formulas),
        len(outputs),
        len(m.powders),
        len(m.fluids),
        len(m.essences),
        len(m.stable_pf),
        len(m.stable_fe),
        compatible,
    )
    expected = (19, 16, 10, 9, 9, 19, 18, 47)
    if got != expected:
        raise ValueError(
            "Private input does not match accepted 3-slot baseline: "
            f"got={got}, expected={expected}"
        )


def surface_iter(
    m: Model, target: Triple, shape: Tuple[int, int, int]
) -> Iterable[Surface]:
    p0, f0, e0 = target
    a, b, c = shape
    for pe in itertools.combinations(
        [x for x in m.powders if x != p0], a - 1
    ):
        ps = tuple(sorted((p0,) + pe))
        for fe in itertools.combinations(
            [x for x in m.fluids if x != f0], b - 1
        ):
            fs = tuple(sorted((f0,) + fe))
            for ee in itertools.combinations(
                [x for x in m.essences if x != e0], c - 1
            ):
                es = tuple(sorted((e0,) + ee))
                yield ps, fs, es


def fact_survivors(
    m: Model,
    target: Triple,
    surface: Surface,
    positive_only: bool,
) -> List[Tuple[int, int, FrozenSet[Triple]]]:
    triples = tuple(itertools.product(*surface))
    target_counts = m.counts[target]
    out = []
    for index, value in enumerate(target_counts):
        if positive_only and value <= 0:
            continue
        survivors = frozenset(
            x for x in triples if m.counts[x][index] == value
        )
        out.append((index, value, survivors))
    return out


def configs_for_orientation(
    m: Model,
    target: Triple,
    surface: Surface,
    orientation: str,
    min_live_triples: int,
    positive_only: bool = False,
) -> List[Config]:
    ps, fs, es = surface
    triples = tuple(itertools.product(ps, fs, es))
    if orientation == "PF":
        raw_branches = len(ps) * len(fs)
        branch = lambda x: (x[0], x[1])
    elif orientation == "FE":
        raw_branches = len(fs) * len(es)
        branch = lambda x: (x[1], x[2])
    else:
        raise ValueError(orientation)

    weak_min = math.ceil(2 * raw_branches / 3)
    weak = []
    for index, value, survivors in fact_survivors(
        m, target, surface, positive_only
    ):
        branch_count = len({branch(x) for x in survivors})
        if weak_min <= branch_count <= raw_branches - 1:
            weak.append((index, value, survivors))

    retained: List[Config] = []
    for fact_count in range(1, min(3, len(weak)) + 1):
        for combo in itertools.combinations(weak, fact_count):
            survivors: Set[Triple] = set(triples)
            for _, _, mask in combo:
                survivors.intersection_update(mask)

            branch_count = len({branch(x) for x in survivors})
            if not (
                2 <= branch_count <= 4
                and len(survivors) >= min_live_triples
            ):
                continue

            full_chains = sum(
                (p, f) in m.stable_pf and (f, e) in m.stable_fe
                for p, f, e in survivors
            )
            if full_chains > 2:
                continue

            if fact_count > 1:
                redundant = False
                for dropped in combo:
                    without: Set[Triple] = set(triples)
                    for fact in combo:
                        if fact is not dropped:
                            without.intersection_update(fact[2])
                    if len(without) == len(survivors):
                        redundant = True
                        break
                if redundant:
                    continue

            retained.append(
                Config(orientation, fact_count, frozenset(survivors))
            )
    return retained


def configs(
    m: Model,
    target: Triple,
    surface: Surface,
    min_live_triples: int,
    positive_only: bool = False,
) -> List[Config]:
    return (
        configs_for_orientation(
            m, target, surface, "PF", min_live_triples, positive_only
        )
        + configs_for_orientation(
            m, target, surface, "FE", min_live_triples, positive_only
        )
    )


def surface_passes(
    m: Model,
    target: Triple,
    surface: Surface,
    min_live_triples: int,
    positive_only: bool = False,
) -> bool:
    return bool(
        configs(
            m,
            target,
            surface,
            min_live_triples,
            positive_only,
        )
    )


def shape_stats(
    m: Model,
    shape: Tuple[int, int, int],
    min_live_triples: int,
    positive_only: bool = False,
) -> Dict[str, float]:
    rates = []
    existence = 0
    for formula in m.formulas:
        total = good = 0
        for surface in surface_iter(m, formula.triple, shape):
            total += 1
            good += surface_passes(
                m,
                formula.triple,
                surface,
                min_live_triples,
                positive_only,
            )
        rate = good / total
        rates.append(rate)
        existence += good > 0

    return {
        "variants_with_any": existence,
        "mean_surface_fraction": statistics.mean(rates),
        "median_surface_fraction": statistics.median(rates),
        "minimum_surface_fraction": min(rates),
        "maximum_surface_fraction": max(rates),
    }


def random_surface(
    m: Model,
    target: Triple,
    shape: Tuple[int, int, int],
    rng: random.Random,
) -> Surface:
    p, f, e = target
    a, b, c = shape
    ps = tuple(
        sorted(
            [p]
            + rng.sample(
                [x for x in m.powders if x != p],
                a - 1,
            )
        )
    )
    fs = tuple(
        sorted(
            [f]
            + rng.sample(
                [x for x in m.fluids if x != f],
                b - 1,
            )
        )
    )
    es = tuple(
        sorted(
            [e]
            + rng.sample(
                [x for x in m.essences if x != e],
                c - 1,
            )
        )
    )
    return ps, fs, es


def random_good_surface(
    m: Model,
    target: Triple,
    shape: Tuple[int, int, int],
    rng: random.Random,
) -> Surface:
    for _ in range(20000):
        candidate = random_surface(m, target, shape, rng)
        if surface_passes(m, target, candidate, 4):
            return candidate
    raise RuntimeError(
        f"No strong surface sampled for shape {shape}; "
        "run the existence screen first"
    )


def classify_known_relations(
    m: Model,
    target: Triple,
    surface: Surface,
    known: Set[Relation],
) -> Tuple[str, int | None]:
    stable_known: Set[Relation] = set()
    for rel in known:
        kind, a, b = rel
        if (a, b) in (
            m.stable_pf if kind == "PF" else m.stable_fe
        ):
            stable_known.add(rel)

    any_strong = any_thin = any_resolved = False
    missing = []

    for config in configs(m, target, surface, 4):
        live = set(config.survivors)
        for kind, a, b in known:
            if (kind, a, b) in stable_known:
                continue
            if kind == "PF":
                live = {
                    x for x in live
                    if (x[0], x[1]) != (a, b)
                }
            else:
                live = {
                    x for x in live
                    if (x[1], x[2]) != (a, b)
                }

        if config.orientation == "PF":
            branch_count = len({(x[0], x[1]) for x in live})
        else:
            branch_count = len({(x[1], x[2]) for x in live})

        complete_known = [
            x
            for x in live
            if ("PF", x[0], x[1]) in stable_known
            and ("FE", x[1], x[2]) in stable_known
        ]
        resolved = (
            len(live) <= 2
            or (
                target in complete_known
                and len(complete_known) <= 2
            )
        )
        if resolved:
            any_resolved = True
            continue

        target_missing = int(
            ("PF", target[0], target[1]) not in stable_known
        ) + int(
            ("FE", target[1], target[2]) not in stable_known
        )

        if 2 <= branch_count <= 4 and len(live) >= 4:
            any_strong = True
            missing.append(target_missing)
        elif 1 <= branch_count <= 4 and len(live) >= 3:
            any_thin = True
            missing.append(target_missing)

    if any_strong:
        return "strong", min(missing)
    if any_thin:
        return "thin", min(missing)
    if any_resolved:
        return "expertise", 0
    return "gap", None


def relation_screen(
    m: Model,
    shape: Tuple[int, int, int],
    histories: int,
    seed: int,
) -> Dict[str, object]:
    rng = random.Random(
        seed + shape[0] * 100 + shape[1] * 10 + shape[2]
    )
    banks = {
        formula: [
            random_good_surface(
                m,
                formula.triple,
                shape,
                rng,
            )
            for _ in range(histories)
        ]
        for formula in m.formulas
    }

    result = {}
    for density in (0.0, 0.25, 0.5, 0.75, 1.0):
        categories = Counter()
        missing = []

        for formula in m.formulas:
            for surface in banks[formula]:
                ps, fs, es = surface
                relations = [
                    ("PF", p, f)
                    for p in ps
                    for f in fs
                ] + [
                    ("FE", f, e)
                    for f in fs
                    for e in es
                ]
                known_count = round(density * len(relations))
                known = (
                    set(rng.sample(relations, known_count))
                    if known_count
                    else set()
                )

                category, target_missing = classify_known_relations(
                    m,
                    formula.triple,
                    surface,
                    known,
                )
                categories[category] += 1
                if (
                    category in ("strong", "thin")
                    and target_missing is not None
                ):
                    missing.append(target_missing)

        total = sum(categories.values())
        result[str(density)] = {
            "category_rates": {
                key: value / total
                for key, value in sorted(categories.items())
            },
            "mean_missing_target_edges_if_fresh": (
                statistics.mean(missing) if missing else None
            ),
        }

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument(
        "--mode",
        choices=("shapes", "relations"),
        default="shapes",
    )
    parser.add_argument("--histories", type=int, default=64)
    parser.add_argument("--seed", type=int, default=20261005)
    args = parser.parse_args()

    model = load_model(args.input)
    assert_accepted_baseline(model)

    print(
        json.dumps(
            {
                "baseline": {
                    "variants": len(model.formulas),
                    "outputs": len(
                        {x.output for x in model.formulas}
                    ),
                    "dimensions": [
                        len(model.powders),
                        len(model.fluids),
                        len(model.essences),
                    ],
                    "stable_pf": len(model.stable_pf),
                    "stable_fe": len(model.stable_fe),
                    "compatible_chains": sum(
                        (p, f) in model.stable_pf
                        and (f, e) in model.stable_fe
                        for p, f, e in itertools.product(
                            model.powders,
                            model.fluids,
                            model.essences,
                        )
                    ),
                }
            },
            indent=2,
            sort_keys=True,
        )
    )

    if args.mode == "shapes":
        shapes = [
            (2, 2, 2),
            (2, 2, 3),
            (2, 3, 2),
            (3, 2, 2),
            (3, 3, 3),
        ]
        result = {}
        for shape in shapes:
            result[str(shape)] = {
                "strong": shape_stats(
                    model,
                    shape,
                    4,
                ),
                "thin_or_better": shape_stats(
                    model,
                    shape,
                    3,
                ),
                "strong_positive_only": shape_stats(
                    model,
                    shape,
                    4,
                    True,
                ),
            }
        print(
            json.dumps(
                {"shape_screen": result},
                indent=2,
                sort_keys=True,
            )
        )
    else:
        result = {
            str(shape): relation_screen(
                model,
                shape,
                args.histories,
                args.seed,
            )
            for shape in (
                (2, 2, 3),
                (2, 3, 2),
                (3, 2, 2),
                (3, 3, 3),
            )
        }
        print(
            json.dumps(
                {"relation_screen": result},
                indent=2,
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
