# Reasoning-diversity screen — 2026-10-06

Status: **accepted bounded quantitative research; no production tag change; production remains BLOCKED.**

## Question

The previous sequence screen established two different facts:

1. reagent-identity repetition is easy to suppress by field selection;
2. exact property-signature repetition remains noticeable, especially in
   three-slot puzzles, and an optimistic synthetic enrichment reduces it.

The remaining question was more important:

> Do extra properties create meaningfully more **ways to reason**, or do they
> merely repaint the same logical puzzle?

A second campaign-level concern was also tested:

> Can the current corpus avoid accidental runs such as five XOR-heavy puzzles in
> a row without exhausting good puzzle choices?

## Corpus and method

Primary scope: the complete ordinary picker-compatible **three-slot** corpus.

The reconstructed research input revalidated the accepted baseline:
- 19 formula variants;
- 16 outputs;
- 10 Powder-role participants;
- 9 Fluid-role participants;
- 9 Essence-role participants;
- 19 stable Powder-Fluid edges;
- 18 stable Fluid-Essence edges;
- 47 chemically compatible chains.

The known exceptional three-slot success outside the ordinary picker is excluded.

Helper:
`research/TagModelScreen/reasoning_diversity_screen.py`.

Sampling:
- 70 distinct 3x3x3 candidate surfaces per formula variant;
- 450 candidate 2-3-clue packages sampled per surface;
- deterministic seed;
- 200 randomized formula-variant sequence orders for the anti-clumping stress
  test.

Clue families:
- slot-local property literal / exclusion;
- exact total property count;
- XOR;
- positive implication;
- negative-consequent implication;
- implication direction (forward/reverse) remains part of the richer internal
  fingerprint.

A retained package:
- uses individually weak clues;
- requires every selected clue;
- leaves 4-12 live triples;
- leaves a bounded PF and/or FE first-stage branch surface;
- contains the true chain;
- leaves at most two fully compatible chains after the real relation graph is
  applied.

Relation-test depth in this screen is only a structural lower-bound proxy based
on eliminating candidates through known-incompatible adjacent edges. It is **not**
a claim about how many experiments a blind player will perform.

## Comparison models

### Current model
The accepted fixed-property assignment.

### Optimistic enrichment upper bound
A deterministic research-only control:
- up to ten shallow/duplicate Powder/Essence-role identities receive one extra
  existing property;
- no identity exceeds three properties;
- assignment is optimized for signature separation;
- semantics are deliberately ignored.

This is not a proposed taxonomy. It asks only how much headroom ideal extra
properties could provide.

## Result 1 — logical-family diversity is already abundant

Distinct major clue-family multisets available per formula variant:

Current:
- minimum **48**;
- median **49**;
- mean **49.32**;
- maximum **50**.

Optimistic enrichment:
- minimum **48**;
- median **49**;
- mean **49.05**;
- maximum **50**.

There is effectively **no gain**.

Interpretation:
- extra tags do not create new reasoning operators;
- XOR / count / literal / positive implication / negative implication variety is
  already structurally available in the current model;
- a run such as five XOR-heavy puzzles is therefore a **generator scheduling
  failure**, not a corpus/tag-capacity failure.

## Result 2 — extra properties do increase reasoning texture

A slot-abstracted semantic fingerprint treats cases such as “Plant in Powder”
and “Plant in Fluid” as substantially the same property idea when the logical
operation is otherwise the same. This deliberately matches the player's stated
concern that merely moving the same tag to another column should not count as a
fully new puzzle.

Distinct slot-abstracted semantic packages per formula:

Current:
- minimum **3,706**;
- median **6,116**;
- mean **5,909.7**;
- maximum **6,967**.

Optimistic enrichment:
- minimum **5,652**;
- median **6,418**;
- mean **6,460.0**;
- maximum **7,088**.

Mean gain: **+9.3%**.

Distinct structural elimination / branching / relation trajectories:

Current:
- minimum **2,269**;
- median **2,862**;
- mean **2,909.6**;
- maximum **3,373**.

Optimistic enrichment:
- minimum **2,518**;
- median **3,267**;
- mean **3,208.6**;
- maximum **3,684**.

Mean gain: **+10.3%**; median gain: **+14.2%**.

Interpretation:
- enrichment does not broaden the *alphabet* of logical operations;
- it does broaden the number of materially different ways those operations can
  carve the field and interact with the relation layer;
- combined with the previous large reduction in exact-signature repetition,
  this is a real secondary benefit rather than merely cosmetic renaming.

## Result 3 — accidental logic clumping is not forced

A deliberately aggressive anti-clumping selector was run as a capacity stress
test.

It penalized:
- using a clue family present in the immediately previous puzzle;
- using a family for a third consecutive puzzle even more strongly;
- recent slot-abstracted semantic overlap;
- imbalance in PF / FE / mixed relation orientation.

It also used a minimal 4-beat proxy only to avoid optimizing every puzzle toward
the same clue count. This is **not** the production curriculum.

Across 200 randomized 19-variant orders, the current tag model had enough choice
reserve to drive:
- mean adjacent major-family overlap to **0**;
- mean adjacent slot-abstracted semantic overlap to **0**.

The enriched model can do the same.

This is intentionally stronger anti-repetition than the desired player
curriculum. The significance is only:

> the corpus does not force immediate logical repetition.

Production should intentionally allow repetition where learning needs it.

## Generator consequence

Do **not** target perfect equality or absolute non-repetition.

Use separate recency costs for at least:
1. reagent identity;
2. exact property signature;
3. major logical family / reasoning motif;
4. richer reasoning fingerprint where practical (for example clue-family
   combination + relation orientation + rough experiment/branching shape).

Then modulate those costs by the curriculum beat:

- **INTRODUCE** — permit one genuinely new motif and keep surrounding load low;
- **PRACTICE** — deliberately reuse the focus motif; reduce or invert its
  recency penalty, while varying surrounding tags/identities when possible;
- **COMBINE** — combine mastered motifs, strongly penalizing an exact recent
  reasoning fingerprint;
- **BREATHE** — prefer a simpler mastered path and avoid the recently dominant
  motif where feasible.

Thus:
- XOR -> XOR can be intentional practice;
- XOR -> XOR -> XOR -> XOR -> XOR should not happen accidentally.

## Decision on additional properties

The evidence now separates necessity from value.

### Not necessary for
- avoiding repeated reagent identities;
- providing all major logical operation families;
- preventing accidental five-in-a-row motif clumping.

The current model already has ample capacity for these.

### Potentially valuable for
- making property cards less functionally repetitive;
- reducing repeated exact signatures;
- increasing semantic clue-package variety;
- increasing distinct structural reasoning trajectories by about 10% in the
  optimistic upper bound.

The user explicitly values this kind of visible/logical differentiation.

Therefore a **small search for real world-grounded property candidates is now
justified**, but only as a candidate search:
- do not adopt a new tag merely to match the synthetic upper bound;
- prefer properties already legible from item source/world data;
- target shallow/duplicate Powder and Essence signatures first;
- keep three visible properties per reagent as the current practical ceiling;
- rerun the same screens before accepting any real property.

No installed-runtime test is required for this research result.
