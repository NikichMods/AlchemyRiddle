# Prototype 17 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test **information dosing** for direct adjacent compatibility.

Prototype 16 established that STABLE / INCOMPATIBLE pair behavior feels simple and promising, but two pre-seeded stable edges accidentally formed a complete recipe path.

Prototype 17 therefore tests:
- only one useful old compatibility fact;
- two plausible Powder+Liquid branches after target research;
- cheap pair microtests as hypothesis checks;
- no complete compatibility table;
- no recipe-reference comparisons;
- no Powder–Essence relation.

Primary question:
**Does choosing a concrete pair to test feel like natural experiment design rather than matrix completion?**

## Spoiler boundary

All reagent names, provenance marks, compatibility outcomes and the hidden formula are fictional.

## Universal player-visible law

A valid three-component formula is prepared in two stages:

1. Powder + Liquid must form a **stable base**.
2. The selected Liquid + Essence combination must remain **stable** when the essence is incorporated.

A microtest can test one actual adjacent pair:
- Powder + Liquid; or
- Liquid + Essence.

Raw result:
- **STABLE**; or
- **INCOMPATIBLE / SEPARATES**.

Compatibility is a reusable empirical property of the pair, independent of the current target.

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

The target contains:
- the Plant mark in exactly **one** component;
- the Corpse mark in exactly **one** component.

This leaves exactly four target hypotheses:
- P1 + L2 + E1
- P1 + L2 + E2
- P2 + L1 + E1
- P2 + L1 + E2

Do not enumerate these automatically for the player.

## Prior empirical knowledge

The journal contains exactly one useful old observation:

- P2 Hive Powder + L1 Nectar Solution -> **STABLE**

No Liquid+Essence compatibility is known.
No compatibility result involving P1+L2 is known.

This prior fact deliberately establishes only that the P2/L1 branch is physically viable. It does not identify the target and does not create a complete path.

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

## Hidden valid answer

P2 Hive Powder
+ L1 Nectar Solution
+ E1 Carrion Essence

## Intended hypothesis-driven path

The initial target facts create two Powder+Liquid branches:
- P1/L2;
- P2/L1.

Because P2/L1 is already known stable, the most direct falsification test for the rival branch is:
- P1 + L2 -> INCOMPATIBLE.

After the player legitimately infers P2/L1, two Essence candidates remain.
A direct discriminating test is:
- L1 + E2 -> INCOMPATIBLE.
This leaves E1.

The facilitator must not recommend these tests unless the player first states the relevant hypothesis/reasoning.

## Alternative tests

All pair choices are legal and use the hidden table.

Some choices are weak or redundant:
- retesting P2+L1 returns STABLE and wastes a charge;
- P1+L1 or P2+L2 may return STABLE but do not directly discriminate the two target-compatible Powder+Liquid branches;
- after P2/L1 is established, testing L1+E1 returns STABLE and can also support E1, but because E2 remains untested the player must reason using the rule that the selected pair must be stable; both a stable E1 test and an incompatible E2 test can justify selecting E1 if only one final Essence is to be committed, but the journal must not auto-eliminate E2 solely because E1 is stable.

## Resources

Start:
- 2 Research Charges.
- each microtest costs 1;
- full synthesis consumes one real candidate reagent per slot.

The resource limit is intentionally enough for the clean hypothesis-testing path, but not enough to fill the pair matrix.

## Player-facing journal

Show:
- candidate reagents and provenance marks;
- target Plant x1 / Corpse x1 facts;
- old empirical observation P2+L1 -> STABLE;
- each new pair result;
- remaining Research Charges.

Do not:
- display all possible pairs as a checklist;
- enumerate surviving formulas;
- recommend a pair;
- infer a branch before the player does.

## Legal actions

- name any Powder + Liquid pair for a microtest;
- name any Liquid + Essence pair for a microtest;
- attempt a final three-reagent synthesis.

## Evaluation targets

Record:
- whether one pre-known stable edge feels like useful experience without becoming a recipe hint;
- whether the player naturally identifies the rival Powder+Liquid branch and chooses to test it;
- whether testing an actual pair feels materially more natural than Prototype 15's assay questions;
- whether two charges feel like enough room for reasoning rather than a trap;
- whether the second-stage Essence decision feels like deduction or devolves into a last-slot scan;
- whether the final solve approaches the Prototype-15 “facts intersect into one answer” quality;
- whether compatibility should be a core grammar, one tool among several, or only a supporting fact.

## Integrity rule

The hidden formula, candidate facts, prior observation, compatibility table and resource model are immutable for this blind run.


## Live checkpoint after first microtest

Player reasoning:
- correctly noticed the Corpse x1 fact is non-discriminating in this candidate pool because both Essence candidates carry Corpse;
- used Plant x1 to understand how Powder/Liquid choices constrain one another;
- treated the pre-known Hive Powder + Nectar Solution stable pair as a promising first-stage branch;
- chose to test whether that branch can continue through Carrion Essence, i.e. Nectar Solution + Carrion Essence.

This is the intended kind of hypothesis-driven compatibility test: extend a promising partial chain rather than fill the pair matrix.

Player action:
- microtest Nectar Solution + Carrion Essence.

Raw outcome: **STABLE**.

Resources: 1 / 2 Research Charges remain.

Journal:
1. Prior: Hive Powder + Nectar Solution -> STABLE.
2. New: Nectar Solution + Carrion Essence -> STABLE.

No fresh deduction by facilitator; await player inference.


## Live blind-play completion

After the first microtest returned STABLE, the player chose immediate final synthesis:
- Hive Powder + Nectar Solution + Carrion Essence.

Player explicitly identified an important semantic limitation before committing:
- two stable adjacent pairs prove that the triple is physically/structurally viable under the compatibility rule;
- they do **not by themselves** prove that the resulting viable elixir is the specific target being investigated;
- the player therefore treated final synthesis as a hypothesis check rather than claiming complete logical identification in advance.

This distinction is correct and materially important for architecture evaluation.

Deterministic synthesis outcome: **SUCCESS — target product obtained**.

Resources:
- Research Charges used: 1 / 2;
- one microtest performed;
- no failed synthesis attempts.

Observed solve character:
- the player selected a natural continuation test from an already-known stable first-stage pair;
- one positive result produced a complete stable chain;
- instead of spending the final charge to eliminate the remaining theoretical target-compatible continuation, the player rationally used vanilla synthesis as bounded verification;
- this fits the accepted product rule that final craft may remain a hypothesis test when uncertainty is small, but it also proves adjacent compatibility alone is **not target identity evidence**.

Subjective evaluation pending.
