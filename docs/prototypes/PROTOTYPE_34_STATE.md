# Prototype 34 — True two-slot tutorial

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base main: `905ee6e43b829e8f8feb7765e77e61de83844ee4`.

Purpose: calibrate the accepted difficulty-curriculum claim that the first
two-slot tutorial should teach only fixed-property intersection under low
surrounding load.

This prototype does **not** retest:
- the full end-to-end theoretical-reagent/source flow;
- formula-confirmation economy;
- final UI layout;
- composite clue wording;
- three-slot relations.

Production remains **BLOCKED**.

## Research question

Prototype 33 used a 2x2 field but still felt closer to medium difficulty because
two of its three clues were compound.

Question:

> If the same 2x2 geometry uses only two simple partial property facts, does it
> finally behave like a real tutorial while retaining the “I worked it out”
> feeling?

## Curriculum contract under test

- arity: Powder + Liquid;
- field: 2x2;
- one new reasoning concept only: **intersect partial facts over stable reagent
  properties**;
- no XOR;
- no implication;
- no reverse-direction wording;
- no relation/compatibility layer;
- no unknown theoretical decoy identity;
- exactly two target facts;
- each fact alone must leave two of four candidate pairs;
- the conjunction must identify one unique pair.

## Player-visible candidate field

Target product: **Тихая настойка**.

### Powders
- P1 **Белёсый порошок** — {Труп, Минерал}
- P2 **Пыльцевой порошок** — {Растение, Насекомое}

### Liquids
- L1 **Травяной раствор** — {Растение, Слизь}
- L2 **Мрачный раствор** — {Труп, Слизь}

All four reagent identities and their shown properties are already familiar for
this synthetic tutorial. Practical acquisition is out of scope.

## Player-visible target facts

1. **Минерал встречается ровно в одном из двух компонентов.**
2. **Растение встречается ровно в одном из двух компонентов.**

Literal semantics. No hidden properties or exceptions.

## Hidden answer

**P1 Белёсый порошок + L1 Травяной раствор**.

Verification:
- P1+L1: Mineral=1, Plant=1 -> passes both.
- P1+L2: Mineral=1, Plant=0 -> fails fact 2.
- P2+L1: Mineral=0, Plant=2 -> fails both.
- P2+L2: Mineral=0, Plant=1 -> fails fact 1.

Individual-fact partitions:
- fact 1 leaves P1+L1 and P1+L2;
- fact 2 leaves P1+L1 and P2+L2.

Therefore neither fact identifies the answer alone; their intersection is
unique.

## Confirmation handling

The prototype is testing reasoning clarity, not economy.

Ask the player to name the pair they believe is the formula and, if useful,
explain the deduction.

Do not encourage trial submissions.

If the player submits:
- hidden pair -> report **ФОРМУЛА ПОДТВЕРЖДЕНА**;
- any other pair -> report only **ФОРМУЛА НЕ ПОДТВЕРЖДЕНА** and record the
  unexpected wrong submission before deciding whether the tutorial failed.

Do not add or change clues mid-test.

## Evaluation

After resolution ask briefly:
- was the first useful deduction obvious;
- did both facts have a clear role;
- did the task feel trivial, tutorial-appropriate, or already like a puzzle;
- did it still produce any “I worked it out” feeling;
- would this be comfortable as the player's first formal AlchemyRiddle
  deduction.

Primary success condition:
- player independently identifies the unique pair without confusion and judges
  the reasoning load appropriate for first onboarding.

Important interpretation:
- “easy” is not a failure here;
- the tutorial is meant to establish the reasoning language, not challenge an
  experienced tester.

Stop after evaluation and record the result before starting Prototype 35.


## Live checkpoint 1

Player independently selected **P1 + L1**, matching the precommitted hidden answer.

Observed reasoning:
- fact 1 made P1 the only Powder candidate carrying the required Mineral;
- with P1 selected, fact 2 required the Plant property to come from the Liquid;
- L1 is the only Liquid carrying Plant;
- therefore P1 + L1 is unique.

The player did not enumerate all four pairs and did not require clarification of
the clue semantics.

Immediate side observation raised by the player:
- reagents with only one fixed property/tag may be comparatively weak as
  participants in later high-interaction puzzles;
- consider whether some reagents should receive an additional AlchemyRiddle
  property, or whether a new world-grounded property family could be derived
  cheaply from existing game evidence;
- this is an **open design hypothesis only**, not an accepted tag-model change;
- explicitly evaluate the benefit against costs: artificial taxonomy,
  learnability, presentation density, consistency, and risk of making the
  property system feel mod-invented rather than discovered from the world.

Prototype 34 still needs the player's subjective tutorial evaluation before
disposition is recorded.


## Final player evaluation

Disposition: **PASS AS FIRST-TUTORIAL SHAPE, WITH PRESENTATION SIMPLIFICATION.**

Player judgement:
- the case was **very easy**, but acceptable specifically as the first
  two-slot tutorial;
- it still produced a small but real feeling of “I derived the answer myself”;
- the player would accept this general shape as the first formal AlchemyRiddle
  puzzle;
- some of the perceived triviality was accidental: the hidden answer happened
  to be the first Powder and first Liquid in the visible lists, so the player
  barely needed to inspect the later entries.

Important onboarding refinement:
- the first tutorial does not need rich multi-tag reagent cards;
- one visible property per reagent may be preferable for the very first case,
  because the pedagogical goal is to teach **candidate columns + stable
  properties + intersecting target facts**, not to demonstrate the full later
  property density;
- richer one/two/three-property reagent cards should appear after the basic
  reading model is established.

Do not infer that the first tutorial needs a larger field merely because 2x2 is
easy. A 3x3 field could remain mechanically trivial while adding visual search
load.

Preferred next iteration for production/tutorial design:
- keep the first tutorial deliberately simple;
- avoid placing the intended answer in the first row/first row position;
- use only the minimum visible properties needed to teach the rule;
- let the following early puzzle, not the tutorial itself, introduce richer
  cards or a larger field.

The exact choice between a 2x2 and a slightly larger demonstration field remains
a presentation calibration detail, not an architecture question.

Separate open hypothesis retained:
- later-puzzle expressive depth may benefit from reviewing the current
  distribution of one-, two- and three-property reagents;
- do not alter the accepted fixed-property model until a dedicated information-
  gain screen shows that extra properties materially improve later puzzle
  quality.

Prototype 34 is complete.
