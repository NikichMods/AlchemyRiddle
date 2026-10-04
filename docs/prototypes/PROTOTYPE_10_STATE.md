# Prototype 10 — Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: active blind prototype.

## Purpose

Test the next shortlisted mechanism family after prototype 9. Player-facing evaluation is about whether whole-mixture comparison creates a short, meaningful deduction rather than rote slot enumeration.

Do not name or explain the design family to the player until the prototype reaches a natural evaluation point.

## Fictional target and candidate space

Target product: **Тихий катализатор**.

Recipe arity: 3 ordered/category slots:
1. powder;
2. liquid;
3. essence.

Candidate reagents:

Powders:
- Белый пепел (P1)
- Чёрный мел (P2)
- Кристальная пыль (P3)

Liquids:
- Роса (L1)
- Рассол (L2)
- Спирт (L3)

Essences:
- Эхо (E1)
- Искра (E2)
- Тень (E3)

All names are fictional and carry no hidden semantic properties.

## Hidden answer

The unique valid formula is:

- P1 Белый пепел
- L2 Рассол
- E3 Тень

Do not change this after play begins.

## Player-known comparison rule

A resonance test compares one complete three-reagent test mixture with the target sample.

The result is an integer score from 0 to 3.

Each point means exactly one recipe slot contains the exact same reagent as the target formula:
- powder match contributes 1;
- liquid match contributes 1;
- essence match contributes 1.

The assay reports only the total. It never identifies which slot(s) matched.

There are no near-matches, cross-slot matches, hidden traits, secondary rules, stochastic effects or exceptions.

For any test mixture Q and hidden target T:

score(Q,T) = count of positions i where Q[i] == T[i].

## Initial clue

Before the player's first choice, the journal contains one calibration comparison performed as part of opening the investigation:

Reference mixture:
- P1 Белый пепел
- L1 Роса
- E1 Эхо

Observed resonance: **1 / 3**.

This is a factual starting clue, not a player-paid experiment.

Given the stated rule, exactly one ingredient of the reference mixture is present in the same slot in the target formula.

Initial compatible formula count is 12 of 27. Do not list those formulas unless the player derives/asks to enumerate them as part of play.

## Resources / economy

At prototype start, after the calibration observation, the player has:
- 3 research portions of target sample available for paid resonance tests.
- ordinary candidate reagents are easy to replenish relative to target sample and are not inventory-limited inside this paper prototype.

Each resonance test:
- consumes 1 target-sample portion;
- consumes one unit of each chosen test reagent;
- returns exactly the aggregate 0–3 score defined above.

Target sample is replenishable. Acquiring another sample is moderately more burdensome than replacing ordinary reagents, but there is no irreversible fail state.

The intended ordinary solve should be possible within the 3 available paid resonance tests under a good strategy. A poor strategy may require reacquiring target sample; that is allowed and should be recorded as UX evidence rather than prevented.

## Real synthesis

The player may attempt a real formula at any time.

A synthesis attempt:
- consumes the chosen three ordinary reagents;
- succeeds if and only if the exact hidden answer is used;
- otherwise fails with an ordinary non-informative failed result for this prototype.
- A failed synthesis does not consume target sample and does not return a resonance score.

If the journal constraints logically leave exactly one valid formula, the investigation may mark the recipe as solved without requiring a ceremonial final synthesis. The player may still choose to synthesize it.

## Legal actions

At every decision point the player may:

1. Run a resonance test on any complete powder + liquid + essence mixture, if at least one target-sample portion remains.
2. Attempt a real synthesis with any complete powder + liquid + essence formula.
3. If target-sample portions are exhausted, reacquire another sample batch before further resonance testing.

No other experiment type exists in prototype 10.

## Deterministic outcome examples / integrity

All outcomes are generated only by the score rule above. Examples:

- P1 + L1 + E1 -> 1
- P1 + L2 + E3 -> 3
- P2 + L2 + E3 -> 2
- P1 + L3 + E2 -> 1
- P3 + L1 + E2 -> 0

Do not use these examples player-facing unless the player actually performs the corresponding action.

## Player-facing state requirements

Every turn must show:
- target and 3-slot recipe shape;
- all candidates by slot;
- remaining target-sample portions and replenishment note;
- the resonance rule;
- complete research journal/history;
- established constraints without silently doing unearned deductions;
- current legal actions and costs.

Do not rely on chat scrollback.

## Stopping/evaluation

End the blind interaction when:
- the player successfully synthesizes the target; or
- the formula becomes logically unique and the player recognizes/accepts the deduction; or
- the player decides the interaction is already clearly uninteresting/confusing enough to evaluate.

Afterward record:
- meaningful experiment count;
- whether choices felt strategic or like slot enumeration;
- whether aggregate feedback was understandable;
- whether the player felt “I worked that out”;
- whether 1–3 minute / low-working-memory target was plausible;
- retain/revise/reject/fallback judgment.

Hidden-state integrity is valid only if this file predates the player's first prototype-10 action.
