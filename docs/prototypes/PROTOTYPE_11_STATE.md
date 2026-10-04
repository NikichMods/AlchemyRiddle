# Prototype 11 — Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: active blind prototype.

## Purpose

Test the shortlisted "known-recipe differential / analogy" family using comparisons against already-known formulas rather than freely constructed probe mixtures.

Do not name or explain the family to the player until the prototype reaches a natural evaluation point.

## Target and candidates

Target product: **Тихая настойка**.

Recipe arity: 3 ordered/category slots:
1. powder;
2. liquid;
3. essence.

Candidate reagents:

Powders:
- Белый пепел (P1)
- Чёрный мел (P2)
- Кристальная пыль (P3)
- Костяная соль (P4)

Liquids:
- Роса (L1)
- Рассол (L2)
- Спирт (L3)
- Масло (L4)

Essences:
- Эхо (E1)
- Искра (E2)
- Тень (E3)
- Порядок (E4)

Names are fictional and carry no hidden semantic hints.

## Hidden answer

Unique valid target formula:
- P1 Белый пепел
- L2 Рассол
- E3 Тень

Do not change this after play begins.

## Known recipe library

The player already legitimately knows these complete recipes:

A — Ясный раствор:
- P1 Белый пепел
- L1 Роса
- E1 Эхо

B — Сухой фиксатор:
- P1 Белый пепел
- L2 Рассол
- E2 Искра

C — Меловая настойка:
- P2 Чёрный мел
- L1 Роса
- E2 Искра

D — Тёмный экстракт:
- P3 Кристальная пыль
- L3 Спирт
- E3 Тень

The player may inspect these formulas at any time.

## Player-known comparison rule

A **comparative distillation** compares a target sample with one already-known product A/B/C/D.

Result is an integer 0–3:
- each point means the target recipe and that known recipe use the same exact reagent in the same slot;
- only the total is reported;
- the test never identifies which slot(s) matched;
- there are no near matches, hidden traits, stochastic effects or exceptions.

The player cannot invent an arbitrary comparison mixture for this assay; comparisons are only against the known recipe library.

## Initial clue

Opening the investigation includes one free comparative distillation against known recipe A:

Target vs A (Ясный раствор) -> **1/3 shared ingredients**.

This does not consume a target-sample portion.

Exactly one of A's three ingredients is therefore present in the target in the same slot.

## Resources / economy

Start after the free comparison with:
- 3 target-sample portions available for paid comparative distillations;
- known comparison products are considered already available / cheaply reproducible relative to the target sample for this paper prototype.

Each paid comparative distillation:
- consumes 1 target-sample portion;
- compares against one selected known product B/C/D (or A again, though repeating A is informationally useless);
- returns the deterministic 0–3 overlap score.

Target sample is replenishable at moderate burden; no irreversible fail state.

## Deterministic outcomes

With hidden target P1/L2/E3:

- target vs A (P1/L1/E1) = 1
- target vs B (P1/L2/E2) = 2
- target vs C (P2/L1/E2) = 0
- target vs D (P3/L3/E3) = 1

Do not expose outcomes before the corresponding comparison.

## Real synthesis

Player may attempt any complete candidate formula at any time.

- exact hidden formula succeeds;
- any other formula fails without extra comparison information;
- consumes ordinary reagents only, not target sample.

If constraints leave one valid formula, investigation may resolve it without ceremonial craft.

## Legal actions

At every decision point:
1. compare target against one known recipe A/B/C/D using comparative distillation (cost 1 target sample; A may be repeated but is redundant);
2. attempt a real synthesis using any complete formula;
3. if samples are exhausted, reacquire more target sample.

No other experiment type exists in prototype 11.

## Player-facing UI requirements

Every turn show:
- target and 3-slot shape;
- all candidate reagents;
- known recipe library with formulas;
- comparison rule;
- sample count/replenishment;
- research journal/history;
- justified established constraints;
- legal actions.

Do not rely on chat scrollback.

## Stopping/evaluation

End when:
- player successfully synthesizes;
- constraints become unique and player recognizes/accepts the solution;
- or player decides the loop is clearly uninteresting/confusing enough to evaluate.

Record:
- meaningful comparison count;
- whether choosing *which known recipe to compare* felt like meaningful experimental design or arbitrary button selection;
- whether reasoning from relationships among known formulas felt more naturally alchemical than arbitrary ingredient probing;
- whether the fixed recipe library reduced slot-by-slot enumeration or merely reframed aggregate scoring;
- clarity, working-memory burden and "I worked that out" feeling;
- retain/revise/reject/fallback judgment.

Hidden-state integrity is valid only because this file is committed before the player's first prototype-11 action.
