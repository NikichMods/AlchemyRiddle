# Property Depth and Sequence Diversity Screen Plan — 2026-10-06

Status: **accepted research plan; no tag-model change accepted; production remains BLOCKED.**

## Research question

The current fixed-property model has 35 ordinary reagent identities with this
property-count distribution:

- 16 one-property reagents;
- 14 two-property reagents;
- 5 three-property reagents.

The immediate question is not merely whether this vocabulary can solve
individual puzzles. Existing screens already show strong local solvability.

The new question is:

> Does the current property-depth distribution produce enough **late-game
> puzzle diversity across a sequence of investigations**, or does the generator
> repeatedly depend on the same small set of richer reagents / tag profiles?

This is a sequence-level design question as well as a per-puzzle information
question.

## User hypothesis to test

The current distribution may be too shallow:
- one-property reagents can be useful as simple anchors;
- however, if mid/late puzzles disproportionately require the small set of
  two-/three-property reagents, the same identities may recur too often;
- repeated use of the same rich reagents or the same tag-signature shapes may
  make the overall puzzle campaign feel repetitive even if each individual
  puzzle is formally valid.

The user's intuitive prior is that a more balanced spread of one-, two- and
three-property reagents might produce healthier variety. This is **not** an
accepted target ratio and must not be hard-coded before measurement.

No four-property tier is currently proposed as a default. Three properties
remains the plausible practical ceiling unless evidence shows otherwise.

## Screen structure

Run three stages.

### Stage A — Current-model local quality

Using the accepted hidden ordinary corpus and current eight-property assignment,
measure for mid/late two-slot and three-slot candidate surfaces:

- count of valid high-quality clue packages;
- proportion requiring genuine clue interaction;
- proportion where all selected clues are necessary;
- clue-family diversity;
- number of distinct good surfaces available per target;
- dependence on one-property vs two-/three-property reagents.

This establishes whether one-property-heavy fields are locally weaker.

### Stage B — Sequence-level diversity

This stage is mandatory.

Simulate many legal mid/late investigation sequences rather than selecting each
puzzle independently.

For each generated sequence record:

1. **Reagent reuse concentration**
   - usage count per reagent identity;
   - fraction of puzzle slots occupied by the most-used 5 and 10 reagents;
   - maximum repeated appearance streak where relevant.

2. **Tag-signature reuse**
   - frequency of repeated exact property signatures;
   - concentration of puzzles around the same small set of signatures.

3. **Surface overlap**
   - Jaccard overlap between consecutive candidate fields;
   - repeated candidate-pair / candidate-triple neighborhoods.

4. **Puzzle-logic variety**
   - clue-family mix across the sequence;
   - repeated information trajectories;
   - repeated reliance on the same “rich” reagent as the decisive discriminator.

5. **Target coverage fairness**
   - whether every target can receive a good mid/late puzzle without repeatedly
     importing the same few distractor identities;
   - how often the generator must fall back to easier structure because diverse
     high-quality surfaces are unavailable.

6. **Choice reserve**
   - number of materially distinct high-quality candidate puzzles available at
     each step after penalizing recent reagent/signature reuse.

The key metric is not merely average solvability. It is whether the generator
retains a healthy **reserve of different good choices** after recent-history
anti-repetition constraints are applied.

### Stage C — Counterfactual enrichment upper bound

Only if Stage A/B shows a meaningful diversity bottleneck, create artificial
research-only enrichments.

Do not invent lore-facing production tags yet.

Counterfactual variants should include:
- modest enrichment: selected one-property reagents receive one additional
  synthetic property;
- stronger enrichment: move the distribution toward a roughly balanced
  one-/two-/three-property spread;
- an optimistic upper-bound assignment chosen to maximize useful information
  diversity.

Compare against current model on both:
- local puzzle quality;
- sequence-level diversity metrics.

This answers:
> If we had ideal additional properties available, how much would they actually
> improve the campaign?

If the improvement is small, do not complicate the property model.
If the improvement is large and systematic, only then research world-grounded
additional properties.

## Important controls

Do not reward enrichment merely for producing more formal clue combinations.

A “better” enriched model must improve at least one meaningful player-facing
property:
- materially larger reserve of good late puzzles;
- lower reagent/signature repetition across sequences;
- stronger clue interaction without longer clue walls;
- fewer forced repeats of the same rich identities;
- better target coverage under anti-repetition constraints.

Also track costs:
- average visible properties per card;
- number of distinct property labels the player must learn;
- frequency of three-property cards;
- risk that cards become visually dense or taxonomy-heavy.

The benefit must exceed the cognitive/presentation cost.

## Possible outcomes

### A. Current model is sufficient
Late sequences retain broad choice and acceptable identity/signature diversity.

Action:
- keep the eight-property assignment unchanged.

### B. Local model is sufficient, sequence diversity is the issue
Individual puzzles are strong, but repeated rich reagents become overused.

Action:
- first try generator-level anti-repetition / field-diversity constraints;
- do not add properties unless those constraints materially damage puzzle
  quality or target coverage.

### C. Structural property-depth ceiling
Even with reasonable generator diversity constraints, current tags force heavy
reuse and sharply reduce the reserve of good late puzzles; counterfactual
enrichment fixes this substantially.

Action:
- research additional world-grounded property sources;
- then evaluate candidate real properties rather than adopting the synthetic
  research tags directly.

## Decision principle

Do not optimize toward an aesthetically balanced 1/2/3-property histogram for
its own sake.

A more balanced distribution is valuable only if it measurably improves:
- sequence diversity;
- quality reserve;
- anti-repetition robustness;
- or late-puzzle interaction depth.

The campaign-level sequence is therefore the primary new criterion added by this
research plan.

No runtime test is required.


## Preflight: property-depth bottleneck is slot-asymmetric

Before any sequence simulation, the accepted 35-reagent property assignment was
recounted by native reagent form.

| Form | Reagents | 1 property | 2 properties | 3 properties | Distinct exact signatures |
| --- | ---: | ---: | ---: | ---: | ---: |
| Powder | 15 | **9** | 5 | 1 | **9** |
| Fluid | 8 | **1** | 4 | 3 | **7** |
| Essence | 8 | **3** | 4 | 1 | **5** |
| Universal | 4 | **3** | 1 | 0 | **4** |

Exact-signature repetition is also uneven:
- Powder has repeated signatures at multiplicities 3, 3, 2 and 2;
- Fluid has only one duplicated signature, with multiplicity 2;
- Essence has one signature repeated 3 times and another repeated 2 times;
- Universal identities all have distinct signatures.

Interpretation:
- the potential expressive-depth problem is **not** simply “16 of 35 reagents
  are one-property”;
- Powder is the clearest shallow/repetitive form;
- Fluid is already information-rich under the current model;
- Essence has moderate depth but significant signature duplication;
- a future enrichment, if justified, should be selective rather than
  mechanically adding properties to every one-property reagent.

This preflight does not prove that any enrichment is needed. It narrows the
sequence screen to test whether Powder/Essence signature concentration actually
forces repeated identities or weak late-puzzle fields.
