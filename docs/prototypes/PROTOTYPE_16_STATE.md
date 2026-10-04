# Prototype 16 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test the simplest natural-evidence version of the accepted Prototype-15 deduction direction:
- no recipe-to-recipe comparison;
- no positive/negative controls;
- no abstract relation labels;
- direct empirical pair compatibility only;
- prior successful work contributes remembered pair behavior as accumulated experience.

This prototype deliberately uses a small fictional 3-slot state. Its primary question is whether **fact acquisition** feels natural and lightweight, not whether it is the final universal architecture.

## Spoiler boundary

All reagent names, marks and hidden formula are fictional.

## Universal player-visible law

For this prototype, every successful 3-component formula must pass two ordinary preparation stages:

1. **Powder + Liquid** must form a stable base.
2. The selected **Liquid + Essence** combination must also be stable when the essence is incorporated.

The non-adjacent Powder–Essence pair is not tested and has no rule.

Pair stability is an empirical property of those two substances, not a statement that they belong to the current target.

A small research microtest can mix any candidate adjacent pair and report only:
- **STABLE**; or
- **SEPARATES / INCOMPATIBLE**.

The journal remembers pair results permanently. Successful recipes from earlier play may therefore seed pair results automatically.

## Candidate pool

Powders:
- P1 Bloom Powder — {Plant}
- P2 Hive Powder — {Insect}

Liquids:
- L1 Nectar Solution — {Plant, Insect}
- L2 Shell Solution — {Insect, Mineral}

Essences:
- E1 Carrion Essence — {Insect, Corpse}
- E2 Stonebone Essence — {Mineral, Corpse}

## Initial target research

The unknown target:
- contains the Plant mark in exactly **one** component;
- contains the Corpse mark in exactly **one** component.

This leaves four target hypotheses:
- P1 + L2 + E1
- P1 + L2 + E2
- P2 + L1 + E1
- P2 + L1 + E2

Do not enumerate these automatically for the player.

## Already-known compatibility from prior experience

The journal already contains:
- P2 Hive Powder + L1 Nectar Solution -> **STABLE**
- L1 Nectar Solution + E1 Carrion Essence -> **STABLE**

These facts are presented as old empirical observations, not as properties of a named reference recipe.

No other candidate-pair stability is initially known.

## Hidden compatibility table

Powder–Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE

Liquid–Essence:
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE

Only the two prior observations above are initially visible.

## Hidden valid answer

P2 Hive Powder
+ L1 Nectar Solution
+ E1 Carrion Essence

## Intended informative tests

Given the initial target facts:
- testing P1 + L2 directly discriminates whether the rival P1/L2 branch can be valid;
- if it is incompatible, P2/L1 becomes forced by the target constraints;
- testing L1 + E2 then discriminates the remaining essence alternative;
- if it is incompatible, E1 becomes forced.

Deterministic results:
- P1 + L2 -> INCOMPATIBLE
- L1 + E2 -> INCOMPATIBLE

The player is free to test any adjacent pair instead. All outcomes use the hidden table above.

## Resources

Start with 2 Research Charges.
Each microtest costs 1.
Final synthesis costs the selected real reagents but no Research Charge.

The two charges are sufficient for the intended discriminating path but do not prevent a suboptimal choice from leaving ambiguity. This is deliberate evidence about experiment selection.

## Legal actions

At every step:
- microtest any one Powder + Liquid pair;
- microtest any one Liquid + Essence pair;
- attempt final synthesis.

Do not offer a menu of abstract questions. The player names the actual two reagents to test.

## Journal / inference boundary

Show:
- initial target facts;
- the four candidate substances by slot and their provenance marks;
- prior empirical pair observations;
- new raw pair outcomes;
- remaining Research Charges.

Do not:
- enumerate surviving formulas;
- recommend the best pair;
- state what a result implies until the player does.

## Evaluation targets

After play record:
- whether direct pair testing feels substantially more natural than Prototype 15 controls;
- whether old pair observations feel like useful accumulated alchemical experience;
- whether choosing which two substances to test feels like experiment design or matrix completion;
- whether the simple STABLE/INCOMPATIBLE language is intuitive;
- whether the final deduction still feels satisfying enough;
- whether two charges create useful pressure or merely punish a non-optimal first test;
- whether this primitive should become a common tool, an optional tool, or be rejected.

## Integrity rule

All candidate marks, prior observations, hidden compatibility outcomes, hidden formula and resource limits are immutable for this blind run.


## Live blind-play completion

Player reasoning before any new microtest:
- player initially explored whether the provenance-count facts alone fixed slot roles, then correctly noticed multiple branches remain;
- direct STABLE/INCOMPATIBLE pair testing felt immediately simpler and more natural than Prototype 15's control/assay wrapper;
- player correctly understood compatibility as a universal empirical fact about a reagent pair that can carry forward to future investigations;
- however, the two already-known stable observations formed a complete adjacent path: Hive Powder + Nectar Solution and Nectar Solution + Carrion Essence;
- because the initial Plant/Corpse count facts are also satisfied by that path, the player saw no compelling reason to spend a Research Charge on an exclusion test;
- instead of designing a discriminating experiment, the player chose the already-known fully compatible chain for immediate final synthesis.

Player action:
- synthesize Hive Powder + Nectar Solution + Carrion Essence.

Deterministic outcome: **SUCCESS**.

Resources:
- Research Charges used: 0 / 2;
- no microtests were performed;
- no failed synthesis attempts occurred.

Observed design finding:
- the empirical compatibility primitive itself was experienced as simple, pleasant and potentially attractive;
- but seeding both adjacent compatibilities from prior experience can collapse the target directly into a candidate recipe path, turning accumulated knowledge into near-answer disclosure rather than a reason to investigate;
- Prototype 16 therefore does not yet test whether choosing a compatibility microtest is satisfying, because the player rationally bypassed the experiment layer.

Subjective evaluation pending.
