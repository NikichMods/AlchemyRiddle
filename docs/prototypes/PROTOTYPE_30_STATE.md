# Prototype 30 — Two-slot known-recipe differential

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base:
- repo: `NikichMods/AlchemyRiddle`
- base main: `a4546accfbf958b7eff50ad7d003bc6423300be2`
- branch: `research/prototype-30-two-slot-known-recipe-differential`
- production remains **BLOCKED**

## Research question

Can a two-slot investigation built around already-known recipes produce a short,
player-owned deduction in which choosing **which reference to compare** is
meaningful, rather than repeating Prototype 11's nearly linear sequence?

This is the B candidate in the accepted A/B/C comparison plan.

The prototype intentionally uses a 3x2 ingredient field and exactly four live
unknown formula hypotheses after prior recipe knowledge is applied.

## Comparison controls

- fictional names; no semantic tag clues;
- 3 Powder candidates x 2 Liquid candidates;
- two field pairs are already known formulas for other products and therefore
  are excluded before play;
- four live unknown pairs remain;
- known recipes are always shown in full;
- only the comparison rule below can generate new research evidence;
- no STABLE/INCOMPATIBLE relation layer;
- no tag/property clues;
- no aggregate free-form hypothesis assay;
- no hidden progression/economy optimization.

The information budget is deliberately small: a good path should normally solve
the four live hypotheses in two paid comparisons.

## Player-facing target

**Тихий раствор**

The target name is fictional and carries no formula hint.

## Candidate field

### Powders
- P1 **Белый пепел**
- P2 **Костяная пыль**
- P3 **Янтарный порошок**

### Liquids
- L1 **Роса**
- L2 **Рассол**

Names are fictional and carry no hidden semantic properties.

## Prior recipe knowledge inside the field

The player already knows:

- P1 + L1 -> **Бледная смесь**
- P2 + L2 -> **Сухая настойка**

Because an exact two-slot formula at this station already produces another known
product, those two pairs cannot be the unknown target formula.

Therefore the four live target hypotheses at the start are:

- H1 = P1 + L2
- H2 = P2 + L1
- H3 = P3 + L1
- H4 = P3 + L2

## Additional known recipe library

The player also legitimately knows these complete recipes:

- C — **Янтарный раствор** = P3 + L3 **Спирт**
- D — **Меловой отвар** = P4 **Меловая пыль** + L1
- E — **Солёный спирт** = P4 **Меловая пыль** + L2

P4 and L3 are known reagents from prior alchemy but are **not** candidates for
the current target. They exist only inside known reference recipes.

The complete reference library visible to the player is therefore:

- A — Бледная смесь = P1 + L1
- B — Сухая настойка = P2 + L2
- C — Янтарный раствор = P3 + L3
- D — Меловой отвар = P4 + L1
- E — Солёный спирт = P4 + L2

## Hidden answer

Unique target formula:

- **H1 = P1 Белый пепел + L2 Рассол**

Do not change this after play begins.

## Player-known comparison rule

A **сравнительная перегонка** compares one target sample with one already-known
product A-E.

It reports only the number of **exact reagents shared in the same role**:

- 0 / 2 shared;
- 1 / 2 shared;
- 2 / 2 shared.

It does **not** identify which role matched.

There are:
- no near matches;
- no hidden properties;
- no stochastic results;
- no exceptions.

The player cannot invent an arbitrary comparison formula. Comparative
distillation only works against an already-known product from the visible
library.

## Deterministic outcomes for the hidden target H1

- target vs A (P1 + L1) -> **1 / 2**
- target vs B (P2 + L2) -> **1 / 2**
- target vs C (P3 + L3) -> **0 / 2**
- target vs D (P4 + L1) -> **0 / 2**
- target vs E (P4 + L2) -> **1 / 2**

Do not expose an outcome before the player selects that comparison.

## Why the library is not Prototype 11's linear setup

Across the four live hypotheses:

### Reference A
- H1 -> 1
- H2 -> 1
- H3 -> 1
- H4 -> 0
Partition: 3 / 1.

### Reference B
- H1 -> 1
- H2 -> 1
- H3 -> 0
- H4 -> 1
Partition: 3 / 1.

### Reference C
- H1 -> 0
- H2 -> 0
- H3 -> 1
- H4 -> 1
Partition: 2 / 2.

### Reference D
- H1 -> 0
- H2 -> 1
- H3 -> 1
- H4 -> 0
Partition: 2 / 2.

### Reference E
- H1 -> 1
- H2 -> 0
- H3 -> 0
- H4 -> 1
Partition: 2 / 2.

Thus the player can inspect the displayed formulas and identify references that
cross-cut the current hypothesis set more evenly than A/B.

For the hidden H1:
- C -> 0 leaves H1/H2; D then distinguishes them;
- D -> 0 leaves H1/H4; C or E then distinguishes them;
- E -> 1 leaves H1/H4; C or D then distinguishes them.

No balanced first comparison uniquely reveals H1. A good path therefore contains
at least one intermediate inference and normally two paid comparisons.

## Resources / economy

Start:
- **3 target-sample portions**.

Each comparative distillation:
- costs 1 target-sample portion;
- known reference product is treated as already available / cheaply reproducible
  for this paper prototype.

Target sample is replenishable at moderate burden. There is no irreversible fail
state.

The resource count is visible before every action.

## Real synthesis

The player may attempt any complete Powder + Liquid pair at any time.

- hidden target H1 -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- any other live pair -> **ИСКОМЫЙ ЭФФЕКТ НЕ ПОЛУЧЕН**;
- known A/B pairs still produce their already-known products and therefore are
  visibly not the target.

A failed synthesis gives no extra comparison score.

If deduction leaves one target pair, the investigation may resolve without a
ceremonial craft.

## Legal actions

At every decision point the player may:

1. run comparative distillation against any known product A-E;
2. attempt a real synthesis using any Powder + Liquid pair;
3. inspect the known recipe library and journal;
4. reacquire target sample if all three portions are spent.

No other experiment exists.

## Player-facing state requirements

Every turn show:

- target;
- 3x2 candidate field;
- the two already-known/non-target field pairs;
- all four live hypotheses, either explicitly as pair cells or visually enough
  that the player can reconstruct them without chat scrollback;
- known reference library A-E with complete formulas;
- comparison rule;
- remaining target-sample portions;
- comparison journal;
- established eliminations / live hypotheses;
- legal actions.

Do not perform new deductions for the player. Present raw outcomes and facts the
player has already stated or that follow from pre-existing knowledge such as
"known recipe A is not the target."

## Evaluation focus

Record:

- whether the first meaningful reference choice is clear;
- whether the player can explain why one reference is more informative than
  another before seeing its result;
- whether reference selection feels like alchemical analogy or abstract
  information-partition optimization;
- whether prior known formulas feel like useful accumulated expertise;
- whether the loop still degenerates into coordinate membership tests;
- whether the second action is meaningfully chosen or effectively forced;
- working-memory burden;
- strength of the "I worked out this recipe" feeling;
- whether the player wants another puzzle of this type;
- whether B feels stronger, weaker, or merely different from the expected A/C
  experiences.

## Stop / repair rule

End when:
- the player identifies the unique target;
- the player successfully synthesizes it;
- or the loop is clearly uninteresting/confusing enough to evaluate.

Per the accepted comparison plan:
- at most one narrow repair is allowed if an obvious prototype defect, rather
  than the candidate family itself, invalidates the comparison;
- otherwise record the result and move on to C;
- do not run a corpus-wide B optimization before the A/B/C player-experience
  checkpoint.

## Starting checkpoint

- active prototype: **30**
- target samples: **3 / 3**
- known non-target field pairs:
  - P1 + L1
  - P2 + L2
- live hypotheses: H1 / H2 / H3 / H4
- no comparative distillations performed
- awaiting player's first action
