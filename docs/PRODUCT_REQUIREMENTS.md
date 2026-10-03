# Product Requirements and Acceptance Envelope

## Problem

Vanilla Graveyard Keeper teaches enough of farming/fertilizer progression for the player to encounter a need for a specific alchemical product, but it does not provide a sufficiently legible route from:

`I need product X -> what should I investigate -> what experiment should I run -> what did that result teach me -> why should the next experiment move me toward X?`

Failed alchemy experiments and slime-like outputs may encode useful information, but two gaps must be distinguished:

1. **interpretation gap** — the player is not adequately taught what a failed result means as information;
2. **targeting gap** — even after understanding failed-result semantics, the player may lack a reasoned way to investigate one particular required unknown product.

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
- the next experiment can be chosen for a reason the player can articulate;
- blind full enumeration is not required;
- a wiki or external recipe list is not required;
- the system does not simply drip-feed a hidden recipe one ingredient at a time;
- successful discovery still occurs through the real alchemy interaction;
- after success, the player can explain why the decisive experiments were informative.

A good solution should normally converge in a small number of **meaningful** experiments after a useful initial clue. The exact target count is intentionally not fixed before the real search space is measured.

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

Reject or redesign a candidate if it:

- works only when the player already knows roughly what the answer is;
- reduces random search but still leaves no route toward a requested product;
- encodes the answer behind a fixed sequence of clicks rather than inference;
- requires dozens of low-information experiments in ordinary cases;
- teaches special-case exceptions instead of a coherent rule system;
- solves only a few hand-picked recipes while failing structurally on the rest of the corpus;
- relies on exact formula disclosure to explain why it works.

## Anti-spoiler requirement

Technical research may inspect the real recipe corpus privately as test data. Reports to the user and public-facing design discussion should default to aggregate evidence: recipe counts, candidate-space sizes, ambiguity classes, information gain, exceptional-case counts and path lengths.

Do not reveal exact ingredients or effectively reconstruct an unknown formula unless the user explicitly asks for that recipe.
