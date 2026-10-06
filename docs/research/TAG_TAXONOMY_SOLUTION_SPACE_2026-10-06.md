# Tag taxonomy solution-space scan — 2026-10-06

Status: **research framing; no taxonomy change accepted; production remains BLOCKED.**

## Why the question widened

The current accepted 35-reagent model has:
- 16 one-property cards;
- 14 two-property cards;
- 5 three-property cards.

The user values visible property density as part of perceived puzzle richness:
- one-property cards can read as deliberately simple / early;
- two-property cards are the natural visual core;
- three-property cards can support richer / later presentation;
- a rough 25/50/25 shape is a soft aesthetic target, not a quota.

The search must therefore optimize more than formal information gain.

## Separate two values of a property

A property can have:

1. **display value**
   - makes a reagent card feel richer and less interchangeable;
   - can be valuable even when rare;

2. **deductive value**
   - produces useful non-trivial partitions of candidate fields;
   - depends on prevalence, correlation and interaction with other tags.

Do not require every displayed property to be equally clue-active.

A globally true rare property may remain visible while the generator gives it a
high information-strength cost or excludes it from ordinary clue packages.

This is preferable to rejecting a good world-grounded property merely because a
positive clue using it would almost name one reagent.

## Source-research spoiler constraint

Properties are visible during theoretical deduction even when the practical
source/preparation route is not yet known.

Therefore distinguish:

### Low-spoiler material/source-nature properties
Examples:
- Organ;
- Metal / precious material;
- Flower;
- fungus;
- aquatic organism/material.

These characterize what the source *is* more than how the player obtains it.

### High-spoiler provenance/process properties
Examples:
- Cremated;
- cultivated/farmed;
- mined;
- hive-produced;
- vendor/source-location categories.

These can directly reveal the later source-research answer.

Treat high-spoiler provenance tags as disfavoured by default even when they are
mathematically useful.

## Broad solution families

### A. Additive intrinsic/material properties

Keep the current eight broad properties and add a small number of orthogonal,
world-grounded descriptors.

Pros:
- smallest rules change;
- preserves all accepted clue semantics;
- naturally increases visible 2/3-property density.

Cons:
- the strongest broad candidates (Organ, Flower) collide with cards that already
  have three properties;
- a strict three-property ceiling therefore filters the candidate set in a way
  that may favour narrower, less valuable tags.

Leading material candidates:
- Organ;
- Metal or the broader economic/material idea Precious;
- Flower;
- fungus;
- aquatic;
- dark-organ / dark anatomical material.

### B. Specific-over-general refinement

Split some broad source classes into more specific mutually exclusive classes,
for example:
- corpse-derived -> Organ versus other corpse material;
- plant-derived -> Flower / crop / other plant;
- mineral -> Metal / gem / other mineral.

Pros:
- can increase signature diversity without exceeding three visible tags;
- strong semantic candidates no longer create 4-tag cards.

Cons:
- a player may reasonably expect “Organ” also to satisfy “Corpse”;
- if it does not, the flat taxonomy can feel semantically arbitrary;
- if it *does*, the design has become hierarchical.

This family needs a clear player-facing ontology before it can be preferred.

### C. Hierarchical taxonomy

Allow subtype implications such as:
- Organ -> Corpse;
- Flower -> Plant;
- Metal -> Mineral.

Pros:
- semantically clean;
- preserves broad and specific reasoning;
- can produce genuinely richer deductions.

Cons:
- adds a new formal rule layer;
- raises tutorial/working-memory cost;
- can create 4+ visible logical properties unless UI collapses parents;
- risks becoming a taxonomy puzzle rather than a short alchemy deduction.

Keep as a higher-complexity fallback, not the default.

### D. Curated “up to three salient properties”

Maintain a larger truth set but display/use only three selected properties per
reagent.

Pros:
- easy to hit a desired visual-density distribution.

Cons:
- selection can become arbitrary;
- two reagents with the same real source trait may show it inconsistently;
- hidden salience rules are difficult for a player to trust.

Reject unless a deterministic, obvious salience rule is found.

### E. Acquisition/provenance taxonomy

Use tags such as cultivated, mined, cremated, hive-produced.

Pros:
- highly systematic and easy to derive from game data.

Cons:
- directly competes with the accepted goal-first Science-funded source-research
  layer by leaking acquisition information before that research is purchased.

Do not use as the default property vocabulary.

### F. Functional/effect-family tags

Use life/death/health/order/toxicity/etc.

Pros:
- extremely systematic.

Cons:
- largely restates reagent identity/effect family;
- risks behaving like disguised answer metadata rather than world-grounded
  evidence.

Reject for the current architecture.

## Candidate observations from the full 35-reagent source scan

### Organ
Strongest broad candidate found so far.
- applies across Powder, Fluid and Essence;
- differentiates multiple corpse-derived signatures;
- affects roughly six accepted reagent identities;
- useful deductive prevalence rather than being a singleton.

Naive additive use creates two four-property Life-family cards.

### Precious versus Metal

Metal is extremely clean but reaches only Gold and Silver Powder.

A broader **Precious material** interpretation can also include the emerald-based
Order Powder:
- still world-legible;
- reaches three cards;
- enriches two one-property cards and one two-property card;
- creates no >3-property collision.

This is worth screening alongside literal Metal rather than assuming Metal is
automatically superior.

### Flower
Systemic across several forms and materially differentiates plant-derived
signatures.

Naive addition collides with three already three-property cards.

### Cultivated crop
Systemic and improves several shallow plant cards, but it is partly provenance
rather than intrinsic material nature and can leak source information.
Also produces a 4-property collision under naive addition.

### Bee / hive family
Broad enough to be mathematically useful, but “hive-produced” is strongly
source-revealing. A purely biological “bee-derived” wording is less process-like
but still needs a clean rule for bee / honey / wax.

### Aquatic
A small but clean cross-family material/ecology candidate (for example eel- and
nori-derived material).
Low prevalence means high display value but likely high clue strength.

### Fungus
Extremely intuitive but currently very rare.
Treat primarily as display/signature texture unless later corpus work shows a
safe clue role.

### Dark anatomical material
A narrow but coherent cross-form family for the death-side anatomical sources.
It fits the three-property ceiling cleanly, but is less elegant/general than
Organ.

## Important non-goal: hit 25/50/25 at any cost

It is possible to assemble narrow additive candidates that happen to produce a
very attractive 1/2/3 histogram.

Do not select a taxonomy because its histogram is pretty.

A candidate set wins only if:
- its rules are globally coherent;
- the player can understand the words without a bespoke lore lecture;
- it does not leak source research materially;
- it improves signature/reasoning diversity;
- its visual-density gain is worth the extra vocabulary.

## New candidate generator policy

If a final taxonomy includes rare world-grounded properties:

- keep them visible on the reagent card;
- assign clue-strength / rarity cost from actual corpus prevalence;
- do not let a rare positive property become a cheap ordinary clue that nearly
  identifies a reagent;
- late/boss puzzles may deliberately exploit stronger rare properties when the
  total difficulty budget permits it.

Thus visual richness and clue difficulty can be tuned independently.

## Smallest next research step

Before testing exact formulas again, build **2-3 concrete taxonomy candidates**
from the solution families above:

1. conservative additive material traits;
2. a specificity/refinement candidate;
3. only if needed, a rare-four-property additive candidate using Organ as the
   stress case.

For each candidate report:
- vocabulary size;
- 1/2/3/4 property distribution;
- exact signature multiplicities;
- source-spoiler risk;
- rare-tag frequencies / clue-strength risk;
- previous sequence/reasoning-diversity metrics.

Then choose at most one or two for a matched player-facing test.

No runtime test is required.


## User refinement after broad scan

Accepted constraints/preferences:
- **do not pursue hierarchical tag semantics**;
- the desired next search is for broad cross-cutting vocabulary, not primarily
  one-off tags that repair one duplicated signature;
- a new **core** tag is much more attractive when it naturally applies to a
  material fraction of the 35 reagents (rough working preference: about 6-12
  identities, not 2-3);
- rare 1-3 identity tags are not forbidden, but they should be exceptions and
  should not be the main mechanism used to enrich the global 1/2/3-property
  distribution;
- tag labels should be **short**, with English UI length especially important
  because the expected audience is predominantly English-speaking;
- Russian research labels may remain explanatory during design, but candidate
  production vocabulary should be judged on concise English naming as well;
- continue to treat the user's desired 1/2/3 distribution as a soft visual
  target, not a quota.

This refinement weakens narrow candidates such as Metal/Precious as primary
taxonomy additions unless they participate in a broader coherent package.


## Direction update: Dark accepted, four-property exception allowed

The solution-space comparison is narrowed:
- Dark is no longer merely a candidate; it is accepted into the working model;
- Warm is rejected;
- hierarchy remains rejected;
- rare four-property cards are allowed;
- Organ should be evaluated additively and globally before considering
  refinement/replacement tricks.

The next comparison is therefore **current + Dark** versus
**current + Dark + global Organ**, not a broad hierarchy/taxonomy redesign.
