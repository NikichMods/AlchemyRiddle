# Prototype 15 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test whether explicit **positive/negative known-formula controls** make a cross-slot relation query feel like a designed experiment rather than purchased information.

This is a bounded fictional 3-slot mid-progression test. It does not claim that the required known controls are guaranteed at the real Glue progression point.

## Spoiler boundary

All target/control formulas and reagent names are fictional. Do not expose the hidden answer or facilitator candidate table during blind play.

## Player-visible substance rule

Every candidate reagent has inspectable provenance marks:
- Plant
- Insect
- Mineral
- Corpse

A reagent may have more than one mark.

There is no abstract RELATED/UNRELATED state.

## Experimental rule

A control assay asks one explicit named question about **two target slots**, for example:

“Do the target Liquid and Essence both have the Insect mark?”

The player is shown two already-known formulas:
- a **positive control** in which the selected pair visibly satisfies the question;
- a **negative control** in which the selected pair visibly does not.

The analyzer is calibrated from those known mixtures, then tests the unknown target residue under the same condition.

Raw result:
- MATCHES POSITIVE CONTROL; or
- MATCHES NEGATIVE CONTROL.

The known control formulas and their reagent marks are always visible. The player never has to trust a hidden relation label.

Each assay costs 1 Research Charge. Candidate reagents are not consumed by an assay.
A synthesis attempt consumes its selected candidate reagents.

## Candidate pool

Powders:
- P1 Bloom Powder — {Plant}
- P2 Hive Powder — {Insect}
- P3 Slate Powder — {Mineral}

Liquids:
- L1 Nectar Solution — {Plant, Insect}
- L2 Grave Solution — {Plant, Corpse}
- L3 Shell Solution — {Insect, Mineral}

Essences:
- E1 Sprout Essence — {Plant}
- E2 Carrion Essence — {Insect, Corpse}
- E3 Stonebone Essence — {Mineral, Corpse}

## Initial target research

The unknown target:
- contains the Plant mark in exactly **one** of its three components;
- contains the Corpse mark in exactly **one** of its three components.

No slot is identified by either fact.

Applying only these facts leaves six legal hypotheses. Do not enumerate them for the player.

## Available assay A — Insect bridge, Liquid–Essence

Question:
**Do the target Liquid and Essence both have the Insect mark?**

Positive control: Buzzing Tonic
- Powder: Chalk Powder — {Mineral}
- Liquid: Meadow Solution — {Plant, Insect}
- Essence: Carrion Essence C — {Insect, Corpse}
- therefore the tested Liquid–Essence pair visibly answers YES.

Negative control: Garden Draught
- Powder: Bark Powder — {Plant}
- Liquid: Gravewater — {Plant, Corpse}
- Essence: Crystal Essence — {Mineral}
- therefore the tested Liquid–Essence pair visibly answers NO.

Among the six hidden hypotheses this assay partitions 3 / 3.

## Available assay B — Insect bridge, Powder–Liquid

Question:
**Do the target Powder and Liquid both have the Insect mark?**

Positive control: Carapace Elixir
- Powder: Moth Powder — {Insect}
- Liquid: Meadow Solution B — {Plant, Insect}
- Essence: Crystal Essence B — {Mineral}
- therefore the tested Powder–Liquid pair visibly answers YES.

Negative control: Stone Draught
- Powder: Chalk Powder B — {Mineral}
- Liquid: Gravewater B — {Plant, Corpse}
- Essence: Carrion Essence D — {Insect, Corpse}
- therefore the tested Powder–Liquid pair visibly answers NO.

Among the six hidden hypotheses this assay partitions 2 / 4.

The A and B partitions cross-cut; neither result can be inferred from the other before testing.

## Hidden answer

P2 Hive Powder {Insect}
+ L1 Nectar Solution {Plant, Insect}
+ E2 Carrion Essence {Insect, Corpse}

It satisfies:
- Plant count = 1 (L1 only)
- Corpse count = 1 (E2 only)

Deterministic outcomes:
- Assay A: MATCHES POSITIVE CONTROL.
- Assay B: MATCHES POSITIVE CONTROL.

After both positive outcomes, the hidden answer is the unique surviving hypothesis.

If A is run first, three hypotheses remain.
If B is run first, two hypotheses remain.
The second assay then makes the formula unique.

The facilitator must not announce candidate counts or deductions unless the player derives them.

## Resources

Start:
- 2 Research Charges.
- both assays cost 1.
- no automatic recharge during the prototype.

This deliberately allows both available control experiments but not arbitrary repeated querying.

## Legal actions

At each decision:
- run Assay A if not already used and a Research Charge remains;
- run Assay B if not already used and a Research Charge remains;
- attempt synthesis with one Powder + one Liquid + one Essence.

## Journal / inference boundary

After an assay show only:
- chosen assay/question;
- both visible controls;
- raw positive/negative match;
- remaining charges;
- prior established target facts.

Do not say what candidates are excluded until the player states their inference.

## Evaluation targets

After completion ask:
- Was the explicit assay question immediately understandable?
- Did positive/negative controls make the known recipes feel useful, or merely decorate a yes/no clue?
- Could the player articulate why they chose A vs B?
- Did choosing an assay feel like experimental design or like selecting a query from a menu?
- Did cross-slot information actually feel different from testing one ingredient at a time?
- Was two-charge bounded research appropriate?
- Did showing full known-control compositions help or overload?
- Does this mechanism deserve another iteration, optional-tool status, fallback status, or rejection?

## Integrity rule

All candidate marks, target facts, control formulas, hidden answer, assay partitions and outcomes are immutable for this blind run.


## Live checkpoint after first assay

Player feedback: information load felt high; the paired-control construction felt artificial/high-level; it was unclear why one named mark relation is selected while other visible marks are ignored; the negative control had no intuitive role; the mechanic did not feel suitable for onboarding. The player nevertheless reconstructed Assay B correctly as testing whether Powder and Liquid both carry Insect, and chose it mainly because it covers slots 1+2 first rather than because of a discriminating hypothesis.

Player action: run Assay B.

Raw outcome: **MATCHES POSITIVE CONTROL**.

Resources: 1 / 2 Research Charges remain.

No fresh deduction by facilitator; await player inference.


## Live checkpoint after second assay

Player inference after Assay B: Powder and Liquid both carry Insect. This was correctly derived by the player and may now be treated as established.

Player briefly explored whether Essence could also carry Insect, corrected their own confusion about the candidate Essences, and chose the remaining Assay A. The player also noted that the presentation/interface made it harder than necessary to keep straight which slots each assay tests.

Player action: run Assay A (Liquid + Essence both Insect).

Raw outcome: **MATCHES POSITIVE CONTROL**.

Resources: 0 / 2 Research Charges remain.

Journal:
1. Initial: Plant occurs in exactly one component.
2. Initial: Corpse occurs in exactly one component.
3. Assay B: Powder + Liquid both Insect -> positive.
4. Assay A: Liquid + Essence both Insect -> positive.

No fresh deduction by facilitator; await player inference.


## Live blind-play completion

Player final deduction:
- Assay B established Powder and Liquid both carry Insect.
- Assay A established Liquid and Essence both carry Insect.
- Therefore all three selected ingredients must carry Insect.
- This fixes Powder to Hive Powder and Essence to Carrion Essence.
- Liquid is then resolved by the initial target facts: Plant must occur exactly once and Corpse exactly once.
- The player first momentarily considered Shell Solution, then self-corrected after checking the Plant-count constraint.
- Final answer: Hive Powder + Nectar Solution + Carrion Essence.

Deterministic synthesis outcome: **SUCCESS**.

Prototype 15 completion state:
- 2 / 2 Research Charges used;
- no synthesis failures before the final answer;
- final formula was deduced rather than enumerated through trial synthesis;
- the player did perform a genuine cross-slot inference chain from both assay results plus initial aggregate facts.

Observed usability findings during play:
- raw information load was high;
- paired-control framing felt artificial/high-level;
- the negative control had no intuitive value to the player;
- assay choice was driven mainly by slot order, not by an explicit discriminating hypothesis;
- keeping track of which slots each assay applied to was harder than necessary;
- despite those UX problems, the two assay results combined cleanly into a non-enumerative final deduction.

Explicit subjective evaluation is still pending before assigning final disposition.


## Player subjective evaluation

Overall rating: **~3/5**.

Strong positive:
- the final deduction was described as **exemplary / exactly the desired shape**;
- the player explicitly enjoyed the moment where two independently obtained cross-slot facts combined with the initial constraints and collapsed to one exact answer;
- the artificial way those facts had been obtained did **not** invalidate the satisfaction of the final reasoning itself;
- the player strongly likes situations where properties interact, constrain one another and produce a unique resolution.

Strong negative:
- the route to those facts felt artificial, high-level and non-native;
- paired-control machinery and compound property questions were too constructed and cognitively heavy;
- the player wants the same quality of final deduction but with facts acquired through a more natural, native, lightweight investigative interaction.

Known-recipe comparison remains attractive only as an optional/simple source of evidence. It should not be forced into a layered meta-comparison system merely because accumulated recipe knowledge is thematically appealing.

Final disposition: **REVISE, retain the deduction shape; reject the current fact-acquisition wrapper as core.**
