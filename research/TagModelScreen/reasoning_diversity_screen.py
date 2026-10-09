#!/usr/bin/env python3
"""Reasoning-path diversity screen for AlchemyRiddle.

Research-only. Exact formula rows stay in the private input JSON and are never
printed. Compares the accepted three-slot tag model with a deterministic,
semantically-invalid optimistic enrichment upper bound.

The screen measures:
- clue-family package reserve;
- slot-abstracted semantic clue-package reserve;
- survivor/branch/relation trajectory reserve;
- whether a recency-aware selector can avoid accidental logic-family clumping.

This is a structural capacity screen, not a player model and not a proposed
production generator.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import progression_variable_field_screen as base


FAMILY_ORDER = ("literal", "count", "xor", "imp_pos", "imp_neg", "shared", "count_mixed")


def clone_tags(model):
    return {name: set(values) for name, values in model.tags.items()}


def signature(tags, item):
    return tuple(sorted(tags[item]))


def slot_signature_objective(tags, items):
    sigs = [signature(tags, x) for x in items]
    counts = Counter(sigs)
    distances = [
        len(tags[a] ^ tags[b])
        for a, b in itertools.combinations(items, 2)
    ]
    return (
        len(counts),
        -max(counts.values()),
        statistics.mean(distances) if distances else 0.0,
    )


def enrichment_objective(tags, model):
    p = slot_signature_objective(tags, model.powders)
    e = slot_signature_objective(tags, model.essences)
    return (p[0] + e[0], p[1] + e[1], p[2] + e[2])


def optimistic_enrichment(model, modifications=10, max_properties=3):
    """Research-only upper bound; returns tags but never the chosen mapping."""
    tags = clone_tags(model)
    vocab = tuple(model.vocabulary)
    modified = set()

    for _ in range(modifications):
        candidates = []
        for item in tuple(model.powders) + tuple(model.essences):
            if item in modified or len(tags[item]) >= max_properties:
                continue
            for tag in vocab:
                if tag in tags[item]:
                    continue
                probe = {k: set(v) for k, v in tags.items()}
                probe[item].add(tag)
                candidates.append(
                    (enrichment_objective(probe, model), item, tag)
                )
        if not candidates:
            break
        _, item, tag = max(candidates)
        tags[item].add(tag)
        modified.add(item)

    return tags, len(modified)


def random_surface(model, target, rng):
    p, f, e = target
    return (
        tuple(sorted((p,) + tuple(rng.sample(
            [x for x in model.powders if x != p], 2
        )))),
        tuple(sorted((f,) + tuple(rng.sample(
            [x for x in model.fluids if x != f], 2
        )))),
        tuple(sorted((e,) + tuple(rng.sample(
            [x for x in model.essences if x != e], 2
        )))),
    )


def sampled_surfaces(model, target, count, rng):
    seen = set()
    out = []
    population = (
        math.comb(len(model.powders) - 1, 2)
        * math.comb(len(model.fluids) - 1, 2)
        * math.comb(len(model.essences) - 1, 2)
    )
    count = min(count, population)
    while len(out) < count:
        value = random_surface(model, target, rng)
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def surface_triples(surface):
    return tuple(itertools.product(*surface))


def generate_true_weak_clues(model, tags, target, surface):
    triples = surface_triples(surface)
    target_index = triples.index(target)
    vocab = tuple(model.vocabulary)
    clues = []

    def add(family, semantic, strict, predicate):
        mask = 0
        for index, triple in enumerate(triples):
            if predicate(triple):
                mask |= 1 << index
        if not ((mask >> target_index) & 1):
            return
        # Generic weak-clue envelope for a 27-cell 3x3x3 field.
        if 12 <= mask.bit_count() <= 26:
            clues.append((family, semantic, strict, mask))

    for slot_index, slot in enumerate(("P", "F", "E")):
        for tag in vocab:
            expected = tag in tags[target[slot_index]]
            add(
                "literal",
                ("literal", tag, expected),
                ("literal", slot, tag, expected),
                lambda triple, i=slot_index, t=tag, x=expected:
                    ((t in tags[triple[i]]) == x),
            )

    for tag in vocab:
        value = sum(tag in tags[item] for item in target)
        add(
            "count",
            ("count", tag, value),
            ("count", tag, value),
            lambda triple, t=tag, v=value:
                sum(t in tags[item] for item in triple) == v,
        )

    # Existing Lab semantics: one unnamed common property across all three roles.
    add(
        "shared", ("shared",), ("shared",),
        lambda triple: bool(set.intersection(*(set(tags[item]) for item in triple))),
    )

    # One distinct assertion per role; homogeneous counts already appear above.
    # Store only tag IDs and an integer count, with no compound-expression tree.
    for role_tags in itertools.product(vocab, repeat=3):
        if len(set(role_tags)) == 1:
            continue
        value = sum(tag in tags[item] for item, tag in zip(target, role_tags))
        add(
            "count_mixed",
            ("count_mixed", tuple(sorted(role_tags)), value),
            ("count_mixed", role_tags, value),
            lambda triple, ts=role_tags, v=value:
                sum(tag in tags[item] for item, tag in zip(triple, ts)) == v,
        )

    for a, b in itertools.combinations(range(3), 2):
        for ta in vocab:
            for tb in vocab:
                if (ta in tags[target[a]]) == (tb in tags[target[b]]):
                    continue
                add(
                    "xor",
                    ("xor", tuple(sorted((ta, tb)))),
                    ("xor", a, ta, b, tb),
                    lambda triple, aa=a, bb=b, xa=ta, xb=tb:
                        (xa in tags[triple[aa]]) != (xb in tags[triple[bb]]),
                )

    for a in range(3):
        for b in range(3):
            if a == b:
                continue
            direction = "fwd" if a < b else "rev"
            for antecedent in vocab:
                if antecedent not in tags[target[a]]:
                    continue
                for consequent in vocab:
                    expected = consequent in tags[target[b]]
                    root = "imp_pos" if expected else "imp_neg"
                    family = root + "_" + direction
                    add(
                        family,
                        (root, antecedent, consequent, direction),
                        (family, a, antecedent, b, consequent),
                        lambda triple, aa=a, bb=b, x=antecedent,
                               y=consequent, z=expected:
                            (x not in tags[triple[aa]])
                            or ((y in tags[triple[bb]]) == z),
                    )

    dedup = {}
    for clue in clues:
        dedup[(clue[0], clue[1], clue[3])] = clue
    return tuple(dedup.values()), triples, target_index


def stable_relation(model, relation):
    kind, a, b = relation
    return (
        (a, b) in model.stable_pf
        if kind == "PF"
        else (a, b) in model.stable_fe
    )


def compatible_indices(model, triples, mask):
    return [
        i for i, (p, f, e) in enumerate(triples)
        if ((mask >> i) & 1)
        and (p, f) in model.stable_pf
        and (f, e) in model.stable_fe
    ]


def branch_counts(triples, mask):
    live = [
        triple for i, triple in enumerate(triples)
        if (mask >> i) & 1
    ]
    return (
        len({(p, f) for p, f, _ in live}),
        len({(f, e) for _, f, e in live}),
    )


def relation_elimination_profile(model, target, triples, mask):
    target_index = triples.index(target)
    relation_masks = {}

    for i, (p, f, e) in enumerate(triples):
        if not ((mask >> i) & 1):
            continue
        for relation in (("PF", p, f), ("FE", f, e)):
            if stable_relation(model, relation):
                continue
            relation_masks[relation] = (
                relation_masks.get(relation, 0) | (1 << i)
            )

    relations = tuple(relation_masks)
    if mask.bit_count() <= 2:
        return 0, "none"

    for count in range(1, min(4, len(relations)) + 1):
        orientations = set()
        for combo in itertools.combinations(relations, count):
            removed = 0
            for relation in combo:
                removed |= relation_masks[relation]
            live = mask & ~removed
            if (
                ((live >> target_index) & 1)
                and live.bit_count() <= 2
            ):
                orientations.add(tuple(sorted({x[0] for x in combo})))
        if orientations:
            best = min(orientations, key=lambda x: (len(x), x))
            return count, "mixed" if len(best) > 1 else best[0]

    return None, None


def family_root(value):
    if value.startswith("imp_pos"):
        return "imp_pos"
    if value.startswith("imp_neg"):
        return "imp_neg"
    return value


def family_groups(clues):
    groups = defaultdict(list)
    for i, clue in enumerate(clues):
        groups[family_root(clue[0])].append(i)
    return dict(sorted(groups.items()))


def draw_family_first(groups, k, rng):
    """Uniform available root family, then uniform unused predicate; repeats allowed."""
    chosen = []
    for _ in range(k):
        available = [(family, [i for i in ids if i not in chosen])
                     for family, ids in groups.items()]
        available = [(family, ids) for family, ids in available if ids]
        if not available:
            raise ValueError('Not enough distinct predicates')
        _, ids = rng.choice(available)
        chosen.append(rng.choice(ids))
    return tuple(sorted(chosen))


def option_from_combo(model, clues, combo, triples, target_index):
    full = (1 << len(triples)) - 1
    mask = full
    for index in combo:
        mask &= clues[index][3]

    final_count = mask.bit_count()
    if not 4 <= final_count <= 12:
        return None

    for dropped in range(len(combo)):
        probe = full
        for i, index in enumerate(combo):
            if i != dropped:
                probe &= clues[index][3]
        if probe.bit_count() <= final_count:
            return None

    pf, fe = branch_counts(triples, mask)
    if not ((2 <= pf <= 4) or (2 <= fe <= 4)):
        return None

    compatible = compatible_indices(model, triples, mask)
    if (
        target_index not in compatible
        or not 1 <= len(compatible) <= 2
    ):
        return None

    tests, relation_mode = relation_elimination_profile(
        model, triples[target_index], triples, mask
    )
    if tests is None:
        return None

    families = tuple(sorted(clues[i][0] for i in combo))
    semantics = tuple(sorted(
        (clues[i][1] for i in combo), key=repr
    ))
    singles = tuple(sorted(
        (clues[i][3].bit_count() for i in combo),
        reverse=True,
    ))
    pairs = tuple(sorted(
        (
            (clues[a][3] & clues[b][3]).bit_count()
            for a, b in itertools.combinations(combo, 2)
        ),
        reverse=True,
    ))

    return {
        "families": families,
        "semantics": semantics,
        "trajectory": (
            singles, pairs, final_count, pf, fe,
            len(compatible), tests, relation_mode,
        ),
        "tests": tests,
        "relation_mode": relation_mode,
    }


def build_options(
    model, tags, surfaces_per_formula, packages_per_surface, seed
):
    rng = random.Random(seed)
    result = []

    for formula in model.formulas:
        target = formula.triple
        options = {}
        for surface in sampled_surfaces(
            model, target, surfaces_per_formula, rng
        ):
            clues, triples, target_index = generate_true_weak_clues(
                model, tags, target, surface
            )
            if len(clues) < 2:
                continue
            groups = family_groups(clues)
            seen = set()
            for _ in range(packages_per_surface):
                count = 2 if rng.random() < 0.5 else 3
                if len(clues) < count:
                    continue
                combo = draw_family_first(groups, count, rng)
                if combo in seen:
                    continue
                seen.add(combo)
                option = option_from_combo(
                    model, clues, combo, triples, target_index
                )
                if option is None:
                    continue
                key = (
                    option["families"],
                    option["semantics"],
                    option["trajectory"],
                )
                options[key] = option
        result.append(tuple(options.values()))

    return result


def abstract_semantics(option):
    result = []
    for value in option["semantics"]:
        if value[0] in ("imp_pos", "imp_neg"):
            result.append((value[0], value[1], value[2]))
        else:
            result.append(value)
    return tuple(sorted(result, key=repr))


def summarize_options(options):
    per_formula = []
    for rows in options:
        family_multisets = {
            tuple(sorted(family_root(x) for x in row["families"]))
            for row in rows
        }
        semantic = {abstract_semantics(row) for row in rows}
        trajectories = {row["trajectory"] for row in rows}
        per_formula.append({
            "family_multisets": len(family_multisets),
            "semantic_packages": len(semantic),
            "trajectories": len(trajectories),
        })

    result = {}
    for key in per_formula[0]:
        values = [row[key] for row in per_formula]
        result[key] = {
            "minimum": min(values),
            "median": statistics.median(values),
            "mean": statistics.mean(values),
            "maximum": max(values),
        }
    return result


def option_family_set(option):
    return {family_root(x) for x in option["families"]}


def option_semantic_atoms(option):
    return set(abstract_semantics(option))


def jaccard(a, b):
    return len(a & b) / len(a | b) if a or b else 0.0


def anti_clump_sequence(options, order, seed, sample=400):
    rng = random.Random(seed)
    chosen = []
    family_counts = Counter()
    relation_counts = Counter()

    for step, formula_index in enumerate(order):
        rows = options[formula_index]
        candidates = (
            rows if len(rows) <= sample
            else rng.sample(rows, sample)
        )
        best_score = None
        best = []

        for row in candidates:
            families = option_family_set(row)
            recent = chosen[-2:]

            third_repeat = sum(
                8.0
                for family in families
                if len(recent) == 2
                and all(
                    family in option_family_set(x)
                    for x in recent
                )
            )
            immediate = sum(
                1.2
                for family in families
                if recent
                and family in option_family_set(recent[-1])
            )
            balance = sum(
                family_counts[family] for family in families
            ) * 0.12
            balance += relation_counts[row["relation_mode"]] * 0.08

            semantic_repeat = (
                1.8 * jaccard(
                    option_semantic_atoms(row),
                    option_semantic_atoms(recent[-1]),
                )
                if recent else 0.0
            )

            score = third_repeat + immediate + balance + semantic_repeat

            # Cheap wave proxy: every fourth slot is a breather, the previous
            # one prefers a 3-clue combination. Production curriculum owns the
            # real INTRODUCE/PRACTICE/COMBINE/BREATHE semantics.
            if step % 4 == 3:
                score += 0.5 * (len(row["families"]) - 2)
            elif step % 4 == 2:
                score += 0.5 * (3 - len(row["families"]))

            if best_score is None or score < best_score:
                best_score = score
                best = [row]
            elif score == best_score:
                best.append(row)

        picked = rng.choice(best)
        chosen.append(picked)
        family_counts.update(option_family_set(picked))
        relation_counts[picked["relation_mode"]] += 1

    adjacent_family_overlap = [
        jaccard(option_family_set(a), option_family_set(b))
        for a, b in zip(chosen, chosen[1:])
    ]
    adjacent_semantic_overlap = [
        jaccard(option_semantic_atoms(a), option_semantic_atoms(b))
        for a, b in zip(chosen, chosen[1:])
    ]

    return {
        "mean_adjacent_family_overlap": statistics.mean(
            adjacent_family_overlap
        ),
        "mean_adjacent_semantic_overlap": statistics.mean(
            adjacent_semantic_overlap
        ),
        "family_counts": dict(family_counts),
        "relation_counts": dict(relation_counts),
    }


def summarize_sequences(options, count, seed):
    rng = random.Random(seed)
    rows = []
    for index in range(count):
        order = list(range(len(options)))
        rng.shuffle(order)
        rows.append(anti_clump_sequence(
            options, order, seed + index * 1009
        ))

    return {
        "mean_adjacent_family_overlap": statistics.mean(
            x["mean_adjacent_family_overlap"] for x in rows
        ),
        "mean_adjacent_semantic_overlap": statistics.mean(
            x["mean_adjacent_semantic_overlap"] for x in rows
        ),
        "mean_family_counts": {
            family: statistics.mean(
                x["family_counts"].get(family, 0) for x in rows
            )
            for family in FAMILY_ORDER
        },
        "mean_relation_counts": {
            mode: statistics.mean(
                x["relation_counts"].get(mode, 0) for x in rows
            )
            for mode in ("PF", "FE", "mixed")
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--surfaces", type=int, default=70)
    parser.add_argument("--packages-per-surface", type=int, default=450)
    parser.add_argument("--sequences", type=int, default=200)
    parser.add_argument("--seed", type=int, default=20261007)
    args = parser.parse_args()

    model = base.load_model(args.input_json)
    base.assert_accepted_baseline(model)

    current_tags = clone_tags(model)
    enriched_tags, modified = optimistic_enrichment(model)

    current = build_options(
        model, current_tags, args.surfaces,
        args.packages_per_surface, args.seed
    )
    enriched = build_options(
        model, enriched_tags, args.surfaces,
        args.packages_per_surface, args.seed
    )

    report = {
        "screen": "three-slot-reasoning-diversity",
        "method": {
            "surface": "3x3x3",
            "surfaces_per_formula": args.surfaces,
            "package_samples_per_surface": args.packages_per_surface,
            "sequence_samples": args.sequences,
            "seed": args.seed,
            "optimistic_enrichment_modified_identities": modified,
            "important_limit": (
                "Relation-test count is a structural lower-bound proxy based "
                "on incompatible-edge elimination, not a player experiment "
                "count."
            ),
        },
        "current": {
            "option_diversity": summarize_options(current),
            "anti_clump_sequence": summarize_sequences(
                current, args.sequences, args.seed + 1
            ),
        },
        "optimistic_enrichment": {
            "option_diversity": summarize_options(enriched),
            "anti_clump_sequence": summarize_sequences(
                enriched, args.sequences, args.seed + 2
            ),
        },
    }

    print(json.dumps(
        report, ensure_ascii=False, indent=2, sort_keys=True
    ))


if __name__ == "__main__":
    main()
