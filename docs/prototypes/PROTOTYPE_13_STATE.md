# Prototype 13 — Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: completed blind prototype.

## Purpose

Test the post-0.3.0 leading hybrid:
**world-grounded property gating -> simple whole-mixture aggregate resonance**.

Specific questions:
- does an inspectable substance compendium remove memory/wiki burden without solving the puzzle;
- do one or two world-grounded observations make a realistically larger candidate set feel tractable;
- after gating, does aggregate exact-match scoring create controlled experiments rather than coordinate enumeration;
- does the combined loop feel like “I understood the material, designed an experiment, and worked it out”?

Do not expose the hidden answer or future resonance outcomes.

## Target / entry fiction

Target product: **Связующий эликсир**.

The player needs the unknown product for an already-visible downstream task.
The target itself is not owned.

A small residue from the downstream apparatus is available for non-destructive preliminary examination. This is the legitimate source of the two starting observations; do not imply the player already owns the finished target.

Recipe arity:
1. powder
2. liquid
3. essence

## Known-reagent compendium

All listed reagents are already known/studied by the player.
The compendium is external memory: properties may be inspected/filter-matched at any time.

### Powders
P1 Белый порошок — provenance: mineral — family: White — cost: low
P2 Порошок графита — provenance: mineral — family: Graphite — cost: low
P3 Соль — provenance: mineral — family: Salt — cost: low
P4 Порошок жизни — provenance: botanical/anatomical — family: Life — cost: standard
P5 Порошок смерти — provenance: anatomical — family: Death — cost: standard
P6 Порошок хаоса — provenance: creature/insect — family: Chaos — cost: standard

### Liquids
L1 Раствор жизни — provenance: botanical/anatomical — family: Life — cost: standard
L2 Раствор смерти — provenance: anatomical — family: Death — cost: standard
L3 Раствор порядка — provenance: botanical/creature — family: Order — cost: standard
L4 Алкоголь — provenance: processed botanical — family: Alcohol — cost: low
L5 Масло — provenance: processed botanical — family: Oil — cost: low
L6 Вода — provenance: inorganic — family: Water — cost: low

### Essences
E1 Экстракт жизни — provenance: botanical/anatomical — family: Life — cost: high
E2 Экстракт смерти — provenance: anatomical — family: Death — cost: high
E3 Экстракт порядка — provenance: botanical/creature — family: Order — cost: high
E4 Экстракт хаоса — provenance: creature/insect — family: Chaos — cost: high
E5 Экстракт ускорения — provenance: botanical/creature — family: Acceleration — cost: high
E6 Экстракт здоровья — provenance: botanical — family: Health — cost: high

These are fictionalized candidates shaped to resemble the measured 0.3.0 grouping power. Names/properties are player-visible and carry no hidden extra semantics beyond the table.

## Starting observations from residue

Observation A — mineral sediment:
“После выпаривания остаётся характерный минеральный осадок. Порошковая составляющая получена из минерального сырья.”

Formal meaning known to player:
- the correct powder has provenance tag mineral.

The compendium/filter may directly show matching known powders P1/P2/P3. This matching is reference lookup, not deduction.

Observation B — Life-family assay:
“Жизненный отклик возникает ровно один раз.”

Formal meaning known to player:
- exactly **one** of the three correct ingredients belongs to semantic family Life.
- no slot is identified.

The compendium may show which known reagents are Life-family, but must not infer which slot contains it.

Starting constraints therefore reduce the hidden structural space from 6*6*6 = 216 listed combinations to:
- powder in {P1,P2,P3};
- exactly one Life among the three;
- because P1/P2/P3 are non-Life, the valid constrained hypotheses are:
  * L1 + one non-Life essence, or
  * one non-Life liquid + E1.
Count = 3 * (1*5 + 5*1) = 30.
Do not surface this derived 30 or the liquid/essence XOR unless the player derives it.

## Universal experiment rule

The player may perform a complete synthesis attempt with any powder + liquid + essence.

If exact formula matches target: synthesis succeeds.

Otherwise an attached research indicator reports **aggregate resonance 0/3, 1/3 or 2/3**:
- one point for each exact correct ingredient in its correct slot;
- aggregate total only;
- no identity/slot attribution;
- no near matches;
- deterministic;
- no extra goo information in this prototype.

This rule is fully player-visible from the start.

## Hidden valid-answer set

Exactly one formula:
**P2 Порошок графита + L3 Раствор порядка + E1 Экстракт жизни.**

Do not change after first action.

## Deterministic outcome function

For any attempt [P,L,E], resonance is the number of exact positional matches against [P2,L3,E1].
Exact 3/3 means success.

## Resources

No target sample is consumed by synthesis attempts.

Each experiment consumes one unit of each selected reagent.
For paper play, all reagents are replenishable:
- low cost: negligible friction;
- standard: noticeable but acceptable;
- high: materially more expensive but still repeatable.

Every three-slot attempt necessarily consumes one high-cost essence, so cost does not create a hidden dominance among otherwise equivalent hypotheses; it exists to preserve normal alchemy stakes.

No irreversible fail state.

## Legal actions

At every turn:
1. inspect/filter the substance compendium by any visible property;
2. synthesize any complete powder + liquid + essence mixture;
3. review raw observations/results and previously established player conclusions.

The facilitator must never derive a fresh consequence before the player states it.

## UI/state requirements

Every decision screen must show:
- target and recipe arity;
- the two starting residue observations;
- compact compendium or an immediately available filtered view sufficient for current reasoning;
- experiment rule;
- full experiment journal;
- player-established facts/hypotheses only;
- resource rule/legal actions.

Do not rely on scrollback for critical state.

## Evaluation / stopping

End when:
- exact formula succeeds;
- the player independently establishes a unique formula and accepts logical resolution;
- or the player declares the loop sufficiently evaluated.

Record:
- whether the compendium feels like helpful external memory or like an embedded wiki;
- whether the starting observations feel world-grounded and understandable;
- whether property matching itself feels trivial/admin work or useful orientation;
- whether choosing a first resonance experiment feels meaningful;
- whether later play becomes one-slot coordinate search;
- meaningful experiment count;
- perceived mental load;
- “I worked it out” feeling;
- whether the two-layer design is better than Prototype 10 alone;
- retain/revise/reject/fallback.

Blind integrity requires this state to be committed before the player's first action.


## Completed play sequence

Player experiments:

1. Powder of Death + Solution of Death + Extract of Death -> resonance 0/3.
   - Player intentionally created a null reference so later single-variable changes would be attributable.
2. White Powder + Solution of Death + Extract of Death -> resonance 0/3.
3. Graphite Powder + Solution of Death + Extract of Death -> resonance 1/3.
4. Graphite Powder + Solution of Death + Extract of Life -> resonance 2/3.
5. Graphite Powder + Solution of Order + Extract of Life -> exact success.

Hidden formula integrity remained valid throughout.

## Observed play behavior

- The property layer gave the player an immediately understandable first objective: determine which of the three mineral powders was correct.
- The player independently designed a strong control experiment: a deliberately all-Death 0/3 baseline, then changed one variable at a time.
- This is genuine experiment design, not a facilitator-supplied path.
- After identifying the powder, the player used the “exactly one Life-family component” clue together with a controlled essence substitution to locate Life in the essence slot.
- Once powder and essence were established, the remaining liquid problem reduced to ordinary sequential candidate testing. The player explicitly noticed this and described the remaining step as brute-force search among the non-Life/non-Death liquid candidates.
- The player also spontaneously flagged the material cost / repetition issue: every test consumes three reagents, including one high-cost essence, so even logically clean controlled experiments can feel long and expensive.
- The compendium created no memory-recall obstacle during the paper test; properties were available directly and the reasoning operated on visible information.

Meaningful synthesis attempts: 5.

Disposition pending explicit player evaluation, but the observed structural result is:
- property gating materially improves orientation and supports a good first controlled experiment;
- aggregate resonance still tends to collapse into coordinate search once only one slot remains unresolved;
- experiment economy may become a major UX constraint for a production version.
