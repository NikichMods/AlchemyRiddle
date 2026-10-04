# Prototype 12 — Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: active blind prototype.

## Purpose

Test the shortlisted target-bound vanilla-goo hybrid as the least-replacement control:
- ordinary alchemy attempts remain the experiment;
- semantic goo families remain the observation substrate;
- add only a target-specific research anchor / binding so goo can be relevant to the selected unknown product.

Do not name the family to the player until evaluation.

## Fictional candidate system

Target product: **Сдерживающий эликсир**.

Recipe arity: 3 ordered slots:
1. powder;
2. liquid;
3. essence.

There are four publicly known goo families. Each family has exactly one candidate reagent in each slot.

Death family (D):
- powder: Костяной порошок
- liquid: Мрачный раствор
- essence: Эссенция смерти

Order family (O):
- powder: Белый пепел
- liquid: Чистая вода
- essence: Эссенция порядка

Life family (L):
- powder: Зелёный порошок
- liquid: Растительный сок
- essence: Эссенция жизни

Chaos family (C):
- powder: Чёрный мел
- liquid: Спирт
- essence: Эссенция хаоса

Family membership is player-visible and represents already-learned vanilla-style goo semantics.

## Hidden target

Unique valid formula:
- powder: Костяной порошок (D)
- liquid: Чистая вода (O)
- essence: Эссенция жизни (L)

Do not change after play begins.

## Target-specific initial clue

Preliminary examination of the target sample establishes:

- the target uses three **different** goo families;
- exactly one of those three families is **Death**.

No slot is identified.
The other two families are unknown among Order, Life and Chaos.

This clue is fictional target-specific research, not vanilla evidence. Its purpose is to supply the missing target anchor while leaving goo to do the main experimental work.

## Target-bound goo rule

The player performs normal complete alchemy attempts.

1. If the exact hidden target formula is used, synthesis succeeds.
2. If the formula is wrong but shares at least one **exact reagent in the correct slot** with the hidden target:
   - target binding causes the failure path to use the researched target as the relevant nearby formula;
   - one matching slot acts as the anchor;
   - the failure produces goo families corresponding to the **other two target slots**;
   - the two goo families are shown as an **unordered pair**;
   - the UI marks this as a **target trace detected**.
3. If the wrong formula shares zero exact positional reagents with the target:
   - no target trace is detected;
   - the resulting unrelated sludge carries no target-useful family information in this prototype.

If a failed attempt has multiple exact positional matches, choose the anchor deterministically by slot priority:
Powder > Liquid > Essence.
This priority is facilitator-internal; the player is not told which slot was used as anchor.
The unordered goo pair is still computed from the two non-anchor target slots.

No stochastic adaptation is allowed.

## Deterministic outcome function

Target T = [D, O, L] by family/slot.

For any attempted [p,l,e]:
- exact [D,O,L] -> success.
- otherwise compute exact positional matches to [D,O,L].
- if none -> "no target trace", no informative goo pair.
- if one or more:
  - anchor = first matching position in Powder > Liquid > Essence priority;
  - output unordered family pair of the other two target positions.

Examples:
- [D,D,D] -> powder anchor -> target trace; goo {O,L}.
- [D,L,O] -> powder anchor -> target trace; goo {O,L}. (informationally redundant after the all-D test)
- [O,D,L] -> essence anchor -> target trace; goo {D,O}.
- [O,L,D] -> zero matches -> no target trace.
- [D,O,C] -> powder anchor due priority despite also liquid matching -> target trace; goo {O,L}.
- [D,O,L] -> synthesis success.

These examples must not be surfaced unless actually attempted.

## Resources/economy

Experiments are ordinary alchemy attempts:
- consume the three chosen ordinary reagents;
- no separate target-sample portion is consumed after the preliminary examination;
- ordinary reagents are considered replaceable at moderate but noticeable cost;
- no irreversible fail state.

The target sample remains as a journal/research anchor and is not consumed by each attempt.

## Legal actions

At every turn:
1. choose any complete powder + liquid + essence mixture and perform ordinary synthesis;
2. inspect the persistent candidate/family table and journal.

There is no separate resonance meter, comparison apparatus, or paid clue button.

## Player-facing UI requirements

Every turn show:
- target and 3-slot recipe shape;
- all candidate reagents grouped by slot, with goo-family label;
- initial target clue;
- target-bound goo rule in player-understandable form;
- full experiment journal;
- current justified facts/hypotheses;
- available action and resource cost.

Do not rely on scrollback.

## Evaluation

End when:
- exact synthesis succeeds;
- logic uniquely determines the formula and player accepts resolution;
- or the player considers the loop sufficiently evaluated.

Record:
- whether the target clue feels like arbitrary disclosure or a reasonable research anchor;
- whether goo feels meaningfully reused rather than decorative;
- whether experiment choice is meaningful;
- whether target-bound goo is too revealing once any anchor is hit;
- whether unordered family output creates useful deduction or confusion;
- reagent/context-switch burden;
- "I worked that out" feeling;
- retain/revise/reject/fallback judgment.

Hidden-state integrity is valid only because this file is committed before the player's first action.
