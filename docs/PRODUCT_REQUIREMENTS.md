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
- successful discovery still occurs through the real alchemy interaction;
- after success, the player can explain why the decisive experiments were informative.

A good solution should normally converge in a small number of **meaningful** experiments after a useful initial clue. The exact target count is intentionally not fixed before the real search space is measured.

The cognitive and record-keeping burden should also fit Graveyard Keeper's broader, interruption-heavy game loop. The design must not assume the uninterrupted concentration or manual note-taking expected from a dedicated hardcore logic-puzzle game.

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
- do not expose exact unknown formulas;
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
