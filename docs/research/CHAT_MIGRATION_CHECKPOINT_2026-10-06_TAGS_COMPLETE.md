# Chat migration checkpoint — 2026-10-06 — property model complete

Status: **canonical recovery checkpoint for the next chat**.

This checkpoint resolves any ambiguity between older intermediate research notes
and later accepted decisions. Repository state and this checkpoint outrank chat
memory.

## Current phase

AlchemyRiddle remains in design/research. Production implementation is
**BLOCKED**. No runtime test is currently required.

The selected puzzle cores remain:
- two-slot: fixed reagent properties + logical constraints;
- three-slot: adaptive knowledge-aware properties + adjacent
  STABLE/INCOMPATIBLE relations + constraints.

The accepted wave-shaped curriculum remains:
INTRODUCE -> PRACTICE -> COMBINE -> BREATHE.

Generator anti-repeat must be curriculum-aware and separately consider:
- reagent identity;
- exact property signature;
- logical motif / clue family;
- richer reasoning fingerprint where practical.

Intentional repetition during PRACTICE is valid; accidental long runs of the
same motif are not.

## Accepted property model state

The original eight broad properties remain:
- Plant
- Corpse
- Mineral
- Insect
- Animal
- Fish
- Slime
- Water

Two additional properties are now accepted for continued design:

### Dark

Apply Dark to the Health / Death / Acceleration Powder, Fluid and Essence
families: nine reagent identities total.

Dark was accepted without requiring another visual-validation gate. Its combined
vanilla family/naming/colour semantics are sufficient for the product decision.

### Organ

Apply Organ when the reagent has a direct intestine / brain / heart source-family
route, including dark variants: six reagent identities total.

Organ is intentionally narrower than Body:
- bone does not qualify;
- blood does not qualify;
- fat does not qualify;
- wings do not qualify merely because they are body-derived.

The user accepted continuing with Organ after its quantitative PASS and static
sanity-check; treat Organ as part of the current working property model, not as
an unresolved candidate.

### Property-count policy

The previous strict three-property ceiling is superseded.

Rare four-property cards are allowed when they arise naturally from coherent
systemic properties. They may contribute useful later-game visual density, but
property count alone does not determine puzzle difficulty.

The earlier 25/50/25 one/two/three-property idea is only a soft aesthetic
preference and is no longer an optimization target.

Hierarchy/subtype semantics are rejected. Warm is rejected. Do not search for a
third broad property merely to improve the histogram.

## Quantitative state after Dark + Organ

Full 35-reagent property-count distribution:
- 1 property: 12
- 2 properties: 11
- 3 properties: 8
- 4 properties: 4

Distinct same-role signatures:
- Powder: 12 / 15
- Fluid: 8 / 8
- Essence: 6 / 8
- Universal: 4 / 4

Only 9 / 35 cards belong to an exact same-role duplicate group.

All three-property and all four-property cards are unique within their role.

Residual exact duplicate groups are local:
- two Powder clusters;
- two Essence clusters.

Do not treat close but non-identical subset/superset signatures as defects by
default; they can be useful deductive structure.

## Dark + Organ screen result

Compared with Dark alone, adding Organ:
- increased total distinct exact signatures from 20 / 35 to 22 / 35;
- made every Fluid signature unique;
- improved Powder signature diversity;
- did not materially change reagent-identity repetition;
- reduced recent exact-signature repetition in three-slot anti-repeat sequences
  by about 9.5%;
- increased slot-abstracted semantic clue-package reserve by about 6.1%;
- left major clue-family diversity and structural reasoning-trajectory count
  essentially unchanged;
- modestly improved strong 3x3x3 surface availability.

Interpretation:
- Dark is the large global density/signature improvement;
- Organ is a coherent second layer that improves card differentiation and
  semantic reasoning texture;
- Organ is not expected to create a new logical operator.

Visible properties and clue strength are separate concerns. A true property may
remain on the card even when its positive clue would be unusually strong; the
generator should price clue strength from actual candidate-field prevalence.

## Taxonomy stopping rule

The static heatmap found no broad remaining taxonomy deficiency.

Do not:
- run synthetic split tests on the four residual duplicate groups merely because
  they exist;
- search for Metal/Precious/Flower/etc. merely to remove local duplicates;
- reopen the tag vocabulary simply to create a prettier property-count
  distribution.

Reopen taxonomy only if:
1. blind play exposes a concrete stale/repetition problem;
2. progression sequencing cannot avoid a concrete problem without sacrificing
   puzzle quality; or
3. another independently compelling, short, broad, world-grounded property
   emerges for a separate reason.

Therefore the property-taxonomy research thread is **closed for now**.

## Other important still-accepted surrounding decisions

- optional decorative colour targets do not consume the mandatory late/boss
  difficulty curve;
- white and black paint remain core due ordinary gameplay uses;
- core progression corpus remains 16 two-slot formula-variant investigations
  plus 19 three-slot formula-variant investigations;
- theoretical reagent identities may appear as true candidates or decoys;
- decoy exposure alone does not create source-research work;
- a solved formula becomes known before first physical synthesis;
- missing practical reagent routes become separate Science-funded source
  research;
- one unsolved deduction may be active at a time and persists unchanged across
  interruption;
- formula submission remains an information oracle and must not become free
  brute-force confirmation;
- visible reagent-property richness is valuable, but difficulty remains
  multidimensional.

## Exact next step after migration

Do **not** continue taxonomy optimization.

Return to the puzzle generator / progression design using the accepted
Dark + Organ property model.

The next bounded design question should be whichever remaining generator issue is
highest leverage after recovery, with current leading area:
- translate the accepted curriculum + anti-repeat requirements into an actual
  campaign/sequence generation policy and identify the next unresolved generator
  parameter that needs evidence.

Before new implementation or deep mechanism-specific research, perform the normal
DevRules solution-space / evidence checkpoint.

No user runtime action is needed at migration.


## Post-migration continuation — curriculum serviceability closed

The next-step wording above has now been completed and is superseded by:

`docs/research/CURRICULUM_SERVICEABILITY_SCREEN_2026-10-06.md`.

Accepted continuation state:
- free player target choice is structurally compatible with the tested curriculum
  at formula-identity level;
- all 16 mandatory two-slot variants can carry the tested low-load BREATHE / XOR
  / forward implication / negative-consequent implication / reverse-direction
  beats under the accepted compact envelope;
- all 19 ordinary three-slot variants can carry the accepted first-relation
  tutorial shape;
- do not add a normal scheduler layer that reserves or selects target recipes for
  curriculum reasons;
- preserve adaptive fallback only for actual dynamic-state infeasibility;
- the next highest-leverage generator question is the smallest curriculum state
  machine: per-arity state, cross-arity concept transfer, mastery transition and
  non-metronomic INTRODUCE / PRACTICE / COMBINE / BREATHE selection.

Production remains BLOCKED. No runtime action is required.


## Post-migration continuation — curriculum pacing simplified

The "smallest curriculum state machine" next step is now superseded.

Accepted direction:
- keep the two-slot and three-slot difficulty ladders independent;
- hand-author their short progression at the **step role / load** level instead of
  introducing a general curriculum state machine;
- preserve free player target choice; the actual puzzle remains generated around
  the selected target;
- INTRODUCE / PRACTICE / COMBINE / BREATHE are descriptive roles, not a repeated
  mandatory four-step cycle;
- front-load most explicit teaching, then spend the majority of each ladder on
  richer puzzles using familiar mechanics;
- working pacing target: about 5-6 teaching-heavy steps then 10-11 rich steps in
  the 16-step two-slot ladder; about 4-5 relation/topology teaching steps then
  14-15 rich steps in the 19-step three-slot ladder;
- BREATHE is occasional load relief rather than metronomic scheduling;
- late/boss difficulty should primarily combine and deepen mastered mechanics;
- exact per-step assignments remain open, and the earlier rough tables are not
  canonical.

Immediate next step:
draft the compressed manual 16-step and 19-step ladders and inspect them as a
design artifact before creating any new quantitative screener.

Production remains BLOCKED. No runtime action is required.


## Post-migration continuation — reach mature difficulty early

Accepted refinement after reviewing the compressed ladder draft:
- do not assume players will research all 16 two-slot or all 19 three-slot
  formula variants;
- expose the mature / maximum difficulty band early enough that a partial-play
  player can experience the whole difficulty progression;
- once the ceiling is reached, keep playing inside that mature band with waves:
  ordinary hard puzzles, occasional breathers and selected boss peaks;
- several final investigations may still be guaranteed boss-grade, but first
  maximum-band exposure must occur earlier;
- exact-count facts do not need their own repeated lesson;
- reverse implication direction is not a separate rule and does not require a
  dedicated introduction by default;
- residual/off-bridge three-slot reasoning is an already-tested advanced use of
  known relation semantics, not a wholly new interaction mechanic.

The immediate next task is to draft:
1. revised compressed 16-step and 19-step ladders with an early max plateau;
2. one plausible mixed two-slot/three-slot player-experience sequence using the
   existing P1-P4 progression skeleton, clearly marked illustrative rather than
   canonical chronology.

Production remains BLOCKED. No runtime action is required.
