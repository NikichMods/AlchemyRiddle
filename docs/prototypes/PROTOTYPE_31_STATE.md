# Prototype 31 — Two-slot controlled comparison / aggregate resonance

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base:
- repo: `NikichMods/AlchemyRiddle`
- base main: `a21108db980821ab52e3d38fa3e307852d5f24bf`
- branch: `research/prototype-31-two-slot-resonance`
- production remains **BLOCKED**

## Research question

Can a two-slot aggregate-resonance puzzle produce a short, legible,
player-owned controlled experiment without collapsing into slot-by-slot
enumeration?

This is Candidate C in the accepted A/B/C comparison plan.

## Fair-comparison controls

- 3 Powder candidates x 2 Liquid candidates;
- fictional names with no hidden semantic tags;
- no known-recipe library;
- no ingredient-property clues;
- no STABLE/INCOMPATIBLE relation layer;
- no external candidate matrix with products in its cells;
- all interaction happens through the two recipe roles: choose one Powder and
  one Liquid to make a test mixture;
- one free calibration observation is present before the first paid action so
  the first paid test can be hypothesis-driven rather than arbitrary.

## Player-facing target

**Лунный раствор**

The name is fictional and carries no formula hint.

## Candidate reagents

### Powder
- P1 **Серый пепел**
- P2 **Костяная пыль**
- P3 **Янтарная пудра**

### Liquid
- L1 **Роса**
- L2 **Рассол**

## Hidden answer

Unique target formula:

- **P3 Янтарная пудра + L1 Роса**

Do not change this after play begins.

## Player-known resonance rule

A research test mixes one candidate Powder with one candidate Liquid and compares
the resulting test reaction with the target sample.

The device reports aggregate resonance:

- **0 / 2** — neither selected component matches the target;
- **1 / 2** — exactly one selected component matches the target;
- **2 / 2** — both selected components match the target.

The device never says which component matched.

There are:
- no partial/near matches;
- no hidden traits;
- no cross-role matches;
- no stochastic outcomes;
- no exceptions.

Equivalent rule:
- correct Powder contributes 1;
- correct Liquid contributes 1;
- only the total is shown.

## Free calibration observation

Before the player's first paid choice, the journal already contains one
calibration test performed while setting up the target sample:

- P1 Серый пепел + L1 Роса -> **1 / 2 resonance**

This observation is free and does not consume the player's test budget.

Formal consequence:
- the hidden target is one of exactly three formulas:
  - P1 + L2
  - P2 + L1
  - P3 + L1

Do not surface this three-formula reduction until the player derives it or asks
for the direct logical consequences of the recorded result.

## Paid test budget

Start:
- **2 research tests** available.

Each paid resonance test:
- consumes one test charge;
- uses one Powder + one Liquid;
- returns 0/2, 1/2 or 2/2 according to the deterministic rule.

For this paper prototype, ordinary reagents are considered readily
replenishable. The test charge represents the limited target-analysis medium,
not irreversible target loss.

## Deterministic outcomes for hidden target P3 + L1

- P1 + L1 -> 1
- P1 + L2 -> 0
- P2 + L1 -> 1
- P2 + L2 -> 0
- P3 + L1 -> 2
- P3 + L2 -> 1

Do not reveal outcomes before the corresponding action.

## Intended discrimination structure

After the free P1+L1 -> 1 calibration, a controlled test P2+L1 is maximally
diagnostic across the three compatible hypotheses:

- if target P1+L2 -> result 0
- if target P2+L1 -> result 2
- if target P3+L1 -> result 1

Thus one deliberate one-factor change can distinguish all remaining hypotheses.

Other tests are legal and may be less informative. Do not steer the player
toward P2+L1 or explain this partition before play.

## Real synthesis

The player may attempt any complete Powder + Liquid formula at any time.

- exact hidden answer succeeds;
- any other pair fails without additional resonance information.

If the player logically establishes a unique answer, synthesis is not required
merely for ceremony.

## Legal actions

At every decision point:
1. run a resonance test on any Powder + Liquid pair if a test charge remains;
2. attempt real synthesis with any pair;
3. review the candidate lists and journal.

No other experiment exists.

## Player-facing state requirements

Every turn show:
- target;
- Powder column/list;
- Liquid column/list;
- resonance rule;
- remaining test charges;
- calibration and later journal entries;
- player-established eliminations/hypotheses only;
- legal actions.

Do not use a product-filled cross-table unless the player explicitly finds one
helpful. The default presentation should make the interaction concrete:
choose one Powder and one Liquid to prepare a test mixture.

Do not perform the player's new deduction for them.

## Evaluation focus

Record:
- whether the physical interaction is immediately clearer than Prototype 30;
- whether the free calibration makes the first paid action feel purposeful;
- whether the player independently uses controlled one-factor change;
- whether aggregate 1/2 feedback is easy to reason from;
- whether the solve feels like experiment design or merely coordinate search;
- whether a one-test solution feels elegant or trivial;
- working-memory burden;
- strength of "I worked out this recipe";
- whether the player wants another puzzle of this type.

## Stop / repair rule

End when:
- the player identifies the unique target;
- the target is synthesized;
- or the candidate is sufficiently evaluated.

Per the accepted comparison plan:
- at most one narrow repair is allowed for an obvious prototype defect;
- otherwise record the result and proceed to Candidate A;
- no corpus-wide C optimization before the A/B/C player-experience checkpoint.

## Starting checkpoint

- active prototype: **31**
- test charges: **2 / 2**
- journal:
  - [Calibration] P1 + L1 -> 1 / 2
- no paid actions yet
- awaiting player's first action


## Live checkpoint 1 — controlled liquid substitution

Pre-action player UX observations:
- the core rule was immediately described as clear, simple, and somewhat immersive;
- the player could readily imagine physically preparing a mixture and running it through an analyzer;
- unlike Prototype 30, no representation confusion appeared before the first action;
- from calibration P1+L1 -> 1/2, the player's first instinct was to hold P1 fixed and change only the liquid to L2;
- the player explicitly asked whether an immediate exact match would simply return the successful result, indicating that 2/2 is understood as a natural terminal observation rather than a separate hidden rule.

Player action:
- resonance test P1 Серый пепел + L2 Рассол.

Deterministic outcome:
- **0 / 2 resonance**.

Resources after action:
- test charges: **1 / 2**.

Protocol boundary:
- present the raw 0/2 observation and journal;
- do not infer the target formula or remaining candidates until the player states their own reasoning.


## Live checkpoint 2 — controlled powder substitution

Player inference from the first paid test:
- calibration P1+L1 -> 1/2;
- test P1+L2 -> 0/2;
- because P1 was held constant and only the liquid changed, the player correctly concluded:
  - L1 Роса is the correct liquid;
  - P1 Серый пепел is not the correct powder.

Player next action:
- hold L1 Роса fixed;
- change powder to P2 Костяная пыль;
- resonance test P2 + L1.

Deterministic outcome:
- **1 / 2 resonance**.

Resources after action:
- test charges: **0 / 2**.

Protocol boundary:
- present the raw 1/2 observation and current journal;
- do not infer the remaining unique powder until the player states their own reasoning.


## Live completion

Player deduction:
- from P1+L1 -> 1/2 and P1+L2 -> 0/2, the player established:
  - L1 is correct;
  - P1 is incorrect.
- P2+L1 -> 1/2 then shows that P2 is also incorrect, because L1 already accounts for the single resonance point.
- therefore the only remaining Powder is P3.

Player identifies the unique target as:
- **P3 Янтарная пудра + L1 Роса**

This matches the precommitted hidden answer.

No ceremonial synthesis is required because the formula is uniquely established.

Resources:
- paid tests used: **2 / 2**
- free calibration observations: **1**
- failed/guess synthesis attempts: **0**

## Immediate player-experience result

Positive:
- the rule was immediately understandable and easy to imagine as a physical alchemical test;
- the player naturally chose controlled one-variable changes without facilitator steering;
- each observation had a locally legible consequence;
- the final answer was deduced rather than guessed or synthesis-enumerated;
- working-memory burden was low.

Observed friction:
- the player briefly lost track of which reagent changed / which symbol referred to which role, but recovered immediately;
- this appears to be naming/state-tracking friction rather than rule opacity;
- the solving strategy still has a coordinate-isolation character: once one role is established, the remaining role is resolved by testing candidates one at a time.

Disposition pending explicit comparative evaluation against Candidate A:
**C SURVIVES PLAYER-EXPERIENCE SCREEN; retain as a serious finalist, with coordinate-search/routinization risk still open.**

Per the accepted plan, proceed to Candidate A rather than optimizing C further.
Production remains BLOCKED.
