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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json")
    ap.add_argument(
        "--assert-three-slot-baseline",
        action="store_true",
        help="Assert the accepted ordinary 1.407 three-slot structural baseline.",
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
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
