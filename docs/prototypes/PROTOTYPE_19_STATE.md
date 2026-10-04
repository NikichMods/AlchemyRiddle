# Prototype 19 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test the comfortable scaling envelope of the leading adjacent-compatibility core.

This is diagnostic, not a requirement for unbounded scaling. If the 3x3x3 field becomes bookkeeping-heavy, the accepted fallback is to expose a smaller target-relevant candidate set rather than reject compatibility.

Primary question:
**With three candidates per slot, can the player still reason from hypotheses and choose a small number of meaningful pair tests, or do they drift into pair-matrix completion?**

## Universal player-visible law

A valid three-component formula is prepared in two stages:
1. Powder + Liquid must be STABLE.
2. Liquid + Essence must be STABLE.

A microtest checks one concrete adjacent pair and returns:
- STABLE; or
- INCOMPATIBLE / SEPARATES.

Compatibility is reusable empirical knowledge about the pair, independent of the current target.

Powder–Essence is never tested.

## Candidate pool

Powders:
- P1 Bloom Powder — {Plant}
- P2 Hive Powder — {Insect}
- P3 Slate Powder — {Mineral}

Liquids:
- L1 Nectar Solution — {Plant, Insect}
- L2 Shell Solution — {Insect, Mineral}
- L3 Grave Solution — {Plant, Corpse}

Essences:
- E1 Carrion Essence — {Insect, Corpse}
- E2 Stonebone Essence — {Mineral, Corpse}
- E3 Pollen Essence — {Plant, Mineral}

## Initial target research

The target contains:
- Plant in exactly **one** component;
- Corpse in exactly **one** component.

Applying only these facts leaves six target hypotheses:
- P1 + L2 + E1
- P1 + L2 + E2
- P2 + L1 + E1
- P2 + L1 + E2
- P3 + L1 + E1
- P3 + L1 + E2

Do not enumerate them automatically for the player.

## Prior empirical knowledge

The journal already contains:
- P2 Hive Powder + L1 Nectar Solution -> **STABLE**
- P1 Bloom Powder + L2 Shell Solution -> **INCOMPATIBLE**

These are old pair observations, not target-specific clues.

No other candidate pair has known compatibility.

## Hidden compatibility table

Powder–Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE
- P2 + L3 -> INCOMPATIBLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

Liquid–Essence:
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden valid answer

P2 Hive Powder
+ L1 Nectar Solution
+ E1 Carrion Essence

## Intended discriminating route

Initial target facts + old incompatibility eliminate the P1/L2 branch when the player notices it.

Remaining meaningful Powder+Liquid branches:
- P2/L1 — already known STABLE;
- P3/L1 — unknown.

A direct falsification test:
- P3 + L1 -> INCOMPATIBLE
eliminates the rival Powder branch.

Then E1/E2 remain as target-compatible Essences with L1.
A direct falsification test:
- L1 + E2 -> INCOMPATIBLE
leaves E1.

This solves in two new microtests.

## Alternative routes

All adjacent pair tests are legal.

Potentially suboptimal examples:
- L1+E1 -> STABLE is positive evidence for E1 but does not by itself eliminate E2.
- testing pairs involving L3 or E3 can be irrelevant after target-count reasoning.
- retesting old observations wastes a charge.

The player has enough slack to recover from one weak experiment.

## Resources

Start with **3 Research Charges**.
Each microtest costs 1.
Full synthesis consumes the selected real reagents but no Research Charge.

## Player-facing journal

Show:
- all 3 candidates per slot and provenance marks;
- target facts Plant x1 / Corpse x1;
- two old empirical observations;
- new raw pair outcomes;
- remaining Research Charges.

Do not:
- enumerate the six hypotheses;
- show a compatibility matrix/checklist;
- recommend a pair;
- infer eliminations before the player does.

## Evaluation targets

Record:
- whether 3x3x3 feels materially heavier than 2x2x2;
- whether the player first uses target facts to ignore irrelevant candidates;
- whether old pair observations feel like useful experience or too much pre-solving;
- whether experiment choice remains hypothesis-driven;
- whether the player starts mentally or explicitly filling a matrix;
- number of microtests before final synthesis;
- whether 3 Research Charges feel like useful slack or invite brute force;
- overall rating relative to Prototypes 17/18;
- if scaling degrades, estimate the preferred bounded candidate envelope.

## Integrity rule

All target facts, prior observations, compatibility results, resource limits and hidden formula are immutable for the blind run.


## Live checkpoint after first microtest

Player reasoning:
- used Plant x1 / Corpse x1 to see that the known stable Hive Powder + Nectar Solution branch can be continued only by an Essence carrying Corpse;
- chose Carrion Essence as the first concrete continuation to test;
- selection was hypothesis-driven from an already-known viable first stage, not matrix filling.

Player action:
- microtest Nectar Solution + Carrion Essence.

Raw outcome: **STABLE**.

Resources: 2 / 3 Research Charges remain.

No facilitator deduction; await player inference.


## Live completion

After the first new microtest returned STABLE, the player rechecked the target facts and chose immediate final synthesis rather than spending more charges.

Final synthesis: Hive Powder + Nectar Solution + Carrion Essence.

Deterministic outcome: **SUCCESS**.

Research Charges used: 1 / 3.

Observed scaling note: even with a visible 3x3x3 candidate field, the player followed one known stable branch and one continuation test, then committed to synthesis without matrix completion. Subjective evaluation pending.


## Player subjective evaluation

The 3x3x3 field felt materially heavier than 2x2x2. The player could still solve the happy path, but reported that a worse branch structure would likely exceed comfortable working memory and might require external notes.

Key observation:
- the run remained manageable mainly because one useful stable Powder+Liquid pair was already known;
- that fact let the player mentally discard the other Powder/Liquid candidates and focus only on continuing one branch;
- without such a stable anchor, the player expects the 3x3x3 field to feel difficult to approach.

Core rating remains approximately **4+ / 5**: still strong, but lower than the 4++ small-field unhappy-path result because broader fields increase working-memory load.

Player design hypothesis:
- starting information should be calibrated to the amount of uncertainty left in the current candidate space;
- one known stable pair may allow fewer target-specific clues;
- with no known stable pair, more target-specific information may be required;
- sufficiency should ideally be computed from how much each fact reduces the actionable hypothesis space rather than from a fixed clue count.
