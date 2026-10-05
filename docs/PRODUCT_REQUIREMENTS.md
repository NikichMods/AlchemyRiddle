# Product Requirements and Acceptance Envelope

## Problem

Vanilla Graveyard Keeper teaches enough of farming/fertilizer progression for the player to encounter a need for a specific alchemical product, but it does not provide a sufficiently legible route from:

`I need product X -> what should I investigate -> what experiment should I run -> what did that result teach me -> why should the next experiment move me toward X?`

Failed alchemy experiments and slime-like outputs may encode useful information, but three gaps must be distinguished:

1. **interpretation gap** — the player is not adequately taught what a failed result means as information;
2. **targeting gap** — even after understanding failed-result semantics, the player may lack a reasoned way to investigate one particular required unknown product;
3. **continuity gap** — Graveyard Keeper naturally interrupts alchemy with energy, day/NPC schedules, corpse handling, farming, production and other systems, while vanilla does not preserve enough investigation context for the player to resume a multi-step deduction without reconstructing it from memory.

The project exists to close those gaps without replacing discovery with recipe disclosure.

## Durable product goal

**Make vanilla alchemy independently solvable as a deductive puzzle, without wiki lookup, brute-force enumeration, or advance revelation of formulas.**

Core principle:

**Do not make alchemy easier by giving the answer; make it explainable and solvable.**

Desired player conclusion after success:

> I worked out this recipe.

## Acceptance envelope

For an unknown vanilla product within the supported scope, the final design should make it possible to demonstrate, without revealing the formula in advance, that:

- the player has a comprehensible reason to begin investigating that specific product;
- the player understands the rules needed to interpret experimental outcomes;
- each meaningful experiment can reduce uncertainty or establish a useful constraint;
- controlled changes in an experiment produce feedback that is locally interpretable enough to support controlled reasoning;
- the information gained from an experiment is reasonable relative to its material cost and the gameplay interruption required to replace consumed reagents;
- the player can leave alchemy, engage with normal Graveyard Keeper systems, and later recover the established facts/open hypotheses without reconstructing the investigation from human memory alone;
- the next experiment can be chosen for a reason the player can articulate;
- blind full enumeration is not required;
- a wiki or external recipe list is not required;
- for the target deductive architecture, the system does not simply drip-feed a hidden recipe one ingredient at a time;
- successful discovery should preferably culminate in the real alchemy interaction, but this is **not a hard requirement**: if the research/minigame has logically exhausted all alternatives and uniquely determined the formula, it may explicitly resolve/reveal that formula rather than forcing a ceremonial final craft;
- after success, the player can explain why the decisive experiments were informative.

A good solution should normally converge in a small number of **meaningful** experiments after a useful initial clue. The exact target count is intentionally not fixed before the real search space is measured.

The cognitive and record-keeping burden should also fit Graveyard Keeper's broader, interruption-heavy game loop. The design must not assume the uninterrupted concentration or manual note-taking expected from a dedicated hardcore logic-puzzle game.



### Accepted target experience and investigation entry point

The intended alchemy interaction is a **short micro-deduction**, not a standalone hardcore puzzle. As a working UX target, an ordinary investigation should often fit roughly **1–3 minutes** of focused reasoning: enough friction for the player to feel briefly clever and competent, but not enough to become exhausting or dominate Graveyard Keeper's wider loop. This is a design target, not a rigid timer.

The preferred investigation entry point is the first **visible vanilla need for a specific unknown alchemical product X**. The intended flow is:

`visible need for X -> journal records X as an unknown research topic -> player chooses X -> first meaningful research step`

The notification for a newly recorded unknown product should be neutral, e.g. that a new journal entry was added. It should not itself explain the formula or direct the player toward a specific answer path.

Before creating an investigation topic, check whether vanilla has already legitimately revealed/unlocked the formula. Already-known formulas bypass the research loop rather than becoming fake mysteries.

The journal is part of the product, not merely convenience UI. It must function as external memory for experiments, observations, established/excluded facts, live hypotheses and the reason the investigation exists, so returning after normal gameplay interruption is easier than resorting to an external wiki.

## Design quality ladder and fallback policy

The project target remains a genuine deductive puzzle, but design quality is not binary. Use this ladder when comparing candidates:

1. **Opaque / vanilla-like** — information may exist internally, but the player is not taught enough to use it and has no reliable route toward a requested product.
2. **Guided disclosure** — the system deliberately narrows or reveals bounded parts of the hidden formula (for example, reducing one slot to a small explicit candidate set). This is not the target architecture, but it is a legitimate **fallback quality floor** because it can still remove wiki dependence and blind enumeration.
3. **Deductive narrowing** — the system gives facts or experiment outcomes and the player performs the inference that narrows the formula.
4. **Experimental deduction** — the player can choose informative experiments, interpret their consequences, form the next hypothesis, and ultimately verify a formula through real alchemy.

Levels 3–4 satisfy the intended product direction much better than level 2. Level 2 must not be rejected merely because it is staged disclosure; instead, retain it as a fallback if stronger designs prove disproportionate, incoherent across the real corpus, or mechanically worse.

Choosing a level-2 production architecture instead of the deductive target requires an explicit product decision after the solution-space trade study.

## Preserved invariants by default

Until evidence and an explicit product decision justify otherwise:

- keep vanilla recipe formulas unchanged;
- keep vanilla recipe success/failure semantics unchanged;
- keep progression, economy and save behavior unchanged;
- do not auto-unlock unknown recipes;
- do not expose exact unknown formulas **by default**; however, this anti-spoiler constraint is subordinate to finding the best player experience during design research. If hiding real formulas materially constrains solution-space analysis, the constraint may be relaxed explicitly rather than allowing spoiler protection to distort the design;
- do not require a parallel external encyclopedia;
- do not make arbitrary lore/flavor text carry mechanical meaning unless the rule is taught consistently.

## Candidate directions, not decisions

The following are research families only:

- better teaching/visualization of existing failed-experiment information;
- explicit investigation of a selected unknown product;
- product/reagent properties or signatures that support deduction;
- a deduction journal recording established/excluded constraints;
- hybrid systems combining the above.

None is accepted architecture at bootstrap.

## Design quality tests

A candidate fails the **target deductive standard** if it:

- works only when the player already knows roughly what the answer is;
- reduces random search but still leaves no route toward a requested product;
- encodes the answer behind a fixed sequence of clicks rather than inference; this may still be retained and evaluated as a level-2 fallback rather than discarded outright;
- requires dozens of low-information experiments in ordinary cases;
- consumes significant reagents or forces substantial reacquisition/context switching for low-information checks;
- depends on the player remembering prior attempts, inferred constraints or pending hypotheses across normal gameplay interruptions;
- teaches special-case exceptions instead of a coherent rule system;
- solves only a few hand-picked recipes while failing structurally on the rest of the corpus;
- relies on exact formula disclosure to explain why it works.

## Anti-spoiler requirement

Technical research may inspect the real recipe corpus privately as test data. Reports to the user and public-facing design discussion should default to aggregate evidence: recipe counts, candidate-space sizes, ambiguity classes, information gain, exceptional-case counts and path lengths.

Do not reveal exact ingredients or effectively reconstruct an unknown formula unless the user explicitly asks for that recipe.


## Clarifications accepted 2026-10-04

### Final craft is a preference, not a hard gate

The strongest experience is still expected to be one in which the player gathers enough direct and indirect evidence to form a justified hypothesis and then confirms it through ordinary alchemy.

However, the project must not artificially preserve uncertainty merely to force one more vanilla craft. If the investigation has legitimately eliminated every alternative and the formula is already uniquely determined, the research/minigame may acknowledge the solved recipe directly. A forced craft at that point would be ceremonial rather than deductive.

### Anti-spoiler policy is subordinate to product quality during research

Avoiding unnecessary recipe spoilers remains the default reporting discipline. It must not become a design constraint that prevents rigorous analysis of the real corpus or narrows the solution space.

If exact-formula inspection or explicit discussion becomes necessary to evaluate a candidate design properly, prefer the stronger research/design result. Relax the spoiler constraint explicitly and minimally rather than preserving it at the cost of a worse game.


## Progression-sensitive puzzle scaling and recipe variants

Accepted product intent:
- when the player's growing reagent knowledge naturally permits it, early
  investigations should tend to be smaller/easier and later investigations may
  become richer/more complex;
- this progression is desirable rather than something the generator should
  flatten away;
- fixed 3x3x3 fields are not required in production; smaller bounded fields are
  acceptable when they still produce a meaningful deductive interaction;
- a merely non-unique field is not sufficient: very small/trivial candidate
  spaces may fall below the intended puzzle-quality floor and require a different
  treatment.

For products with multiple vanilla formulas:
- unknown formula variants remain independently researchable;
- discovering one valid recipe must not erase the player's opportunity to
  discover other vanilla variants;
- a selected recipe-variant investigation may be generated around that specific
  hidden variant rather than requiring one puzzle to preserve every formula for
  the product at once;
- exact UI labeling and presentation of unknown variants remain open.

Readiness principle:
- if the selected hidden variant is fully representable from the player's
  legitimate reagent knowledge, prefer a suitably simplified puzzle over a hard
  block caused only by missing distractors;
- do not require discovery of irrelevant reagents solely to decorate or pad the
  puzzle;
- if a true component is still unknown, a hard readiness gate may be legitimate,
  but the eventual guidance must not simply reveal that missing component.


### Recipe-variant visibility

For products with multiple vanilla formulas, it is acceptable for the UI to
reveal **how many recipe variants exist**. This count is not considered a
meaningful recipe spoiler.

Unknown variants may remain individually researchable until each is discovered.
Exact labels and presentation remain open.
