# Prototype 20 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test the main remaining core-UX uncertainty after Prototype 19 and the real-corpus adaptive information-budget screen:

**Can a 3x3x3 target-relevant field remain approachable when the player has no pre-known stable compatibility anchor, provided target facts already reduce the actionable first-stage space to three meaningful Powder+Liquid branches?**

This is a controlled no-anchor scaling test. It does not test production candidate-surface generation.

## Research-method checkpoint

Exact unknown:
- whether a no-anchor state with a calibrated three-branch first stage still produces hypothesis-driven microtests rather than matrix completion or external-note pressure.

Existing evidence path:
- Prototypes 17-19 already establish the adjacent-compatibility grammar, happy-path behavior, negative-result behavior, and anchored 3x3x3 scaling;
- the accepted real-corpus screen shows that 2-4 first-stage branches are achievable for ordinary targets with bounded shaping.

Why a new blind paper test is justified:
- the remaining uncertainty is player cognition, not host/runtime behavior;
- no new runtime probe or production code can answer it more directly;
- a single precommitted blind paper run is the lowest-complexity evidence path.

## Spoiler boundary

All reagent names, target facts, compatibility outcomes and the hidden answer are fictional.

## Universal player-visible law

A valid three-component formula is prepared in two stages:
1. Powder + Liquid must be **STABLE**.
2. Liquid + Essence must be **STABLE**.

A microtest checks one concrete adjacent pair and returns:
- **STABLE**; or
- **INCOMPATIBLE / SEPARATES**.

Compatibility is reusable empirical knowledge about the pair, independent of the current target.

Powder-Essence is never tested.

## Candidate pool

Powders:
- P1 Bark Powder — {Plant}
- P2 Chitin Powder — {Insect}
- P3 Chalk Powder — {Mineral}

Liquids:
- L1 Amber Solution — {Plant, Insect}
- L2 Rust Solution — {Insect, Mineral}
- L3 Mourning Solution — {Plant, Corpse}

Essences:
- E1 Carrion Essence — {Insect, Corpse}
- E2 Fossil Essence — {Mineral, Corpse}
- E3 Crystal Essence — {Plant, Mineral}

## Initial target research

The target contains:
- Plant in exactly **one** component;
- Corpse in exactly **one** component.

Applying only these facts leaves six target-compatible triples distributed across exactly three Powder+Liquid first-stage branches.

Do not enumerate those branches or triples automatically for the player.

## Prior empirical knowledge

None.

The journal contains **no known compatibility result for any candidate pair**.

This is the defining condition of Prototype 20.

## Hidden compatibility table

Powder-Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE
- P2 + L3 -> INCOMPATIBLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

Liquid-Essence:
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden valid answer

P2 Chitin Powder
+ L1 Amber Solution
+ E2 Fossil Essence

## Intended logical structure

The Plant x1 / Corpse x1 target facts leave three meaningful first-stage branches:
- P1 + L2;
- P2 + L1;
- P3 + L1.

Do not enumerate these automatically for the player.

Among those three:
- P1 + L2 -> INCOMPATIBLE;
- P2 + L1 -> STABLE;
- P3 + L1 -> INCOMPATIBLE.

Thus direct first-stage testing can establish the viable branch without scanning the 3x3 Powder-Liquid matrix.

For the viable P2 + L1 branch, the target facts allow two Essence continuations:
- E1;
- E2.

Their second-stage outcomes are:
- L1 + E1 -> INCOMPATIBLE;
- L1 + E2 -> STABLE.

The target can therefore be solved in two new microtests on the shortest route, and in three on a normal negative-first route.

If two of the three target-compatible first-stage branches have been experimentally eliminated, the remaining branch may be treated as logically forced because the prototype guarantees that the hidden answer is within the displayed candidate field.

## Alternative legal routes

All adjacent pair tests are legal.

Tests outside the target-compatible branch structure may be weak or irrelevant. Record whether the player feels a need to scan them anyway.

Positive tests are not by themselves target proof; they are reusable compatibility observations. Target facts still determine whether the pair can belong to this target.

## Resources

Start with **4 Research Charges**.

Each microtest costs 1 Research Charge.
Full synthesis consumes the selected reagents but no Research Charge.

No recharge occurs within this prototype.

Four charges intentionally provide one unit of slack beyond the expected 2-3-test solve so that the test measures cognitive approach rather than punishing one imperfect experiment.

## Player-facing journal

Show:
- all 3 candidates per slot and their provenance marks;
- target facts Plant x1 / Corpse x1;
- explicitly state that no pair compatibilities are known initially;
- each new raw pair outcome;
- remaining Research Charges.

Do not:
- enumerate the six target-compatible triples;
- enumerate the three first-stage branches;
- show a compatibility matrix/checklist;
- recommend a pair;
- infer eliminations before the player does.

## Evaluation targets

Record:
- whether the player can derive a small actionable branch set from the target facts without external notes;
- whether the first microtest is hypothesis-driven or effectively random;
- whether an initial INCOMPATIBLE result improves orientation or creates search pressure;
- whether a first STABLE result becomes a useful anchor quickly enough;
- whether the player begins filling a compatibility matrix;
- whether 3x3x3 still feels too heavy despite only three meaningful first-stage branches;
- number of microtests before final synthesis;
- whether 4 Research Charges feel like fair slack or encourage brute force;
- subjective rating relative to Prototype 19;
- whether the working 2-4 branch envelope should be tightened for no-anchor states.

## Integrity rule

All target facts, candidate properties, hidden formula, compatibility outcomes and resource limits are immutable for the blind run.


## Live activation checkpoint

Status: **active blind play; awaiting the player's first microtest choice**.

Exact current player-facing state:
- target: one unknown three-component product using Powder + Liquid + Essence;
- visible candidates: the full precommitted 3×3×3 candidate pool above;
- known target facts: Plant occurs in exactly one component; Corpse occurs in exactly one component;
- known compatibility observations: **none**;
- Research Charges: **4 / 4**;
- completed actions: none;
- journal: empty apart from the target facts and universal two-stage compatibility law;
- legal next action: choose any one adjacent Powder+Liquid or Liquid+Essence pair for a microtest, costing 1 Research Charge; full synthesis is also legal if the player chooses to commit.

No facilitator inference has been supplied. Hidden answer, properties, compatibility table, costs and resource limits remain unchanged from the precommit.


## Aborted presentation run

The initial player-facing activation is **ABORTED BEFORE ANY PLAYER ACTION**.

Reason:
- the facilitator presented the interface in Russian but left reagent display names in English;
- this is a presentation/readability defect that could affect the intended cognitive-load evidence.

No microtest, synthesis, inference, resource expenditure, or hidden-state change occurred.

Per the paper-prototype integrity rule, do not silently mutate the already-presented run. Restart the same logical test as a new precommitted Russian-localized presentation variant with unchanged hidden compatibility structure and evaluation purpose.
