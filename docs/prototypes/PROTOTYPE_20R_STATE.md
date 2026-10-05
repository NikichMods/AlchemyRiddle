# Prototype 20R Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Russian-localized restart of Prototype 20 after the original activation was aborted before any player action because English reagent display names leaked into an otherwise Russian player-facing interface.

The logical test is unchanged:

**Can a 3×3×3 target-relevant field remain approachable when the player has no pre-known stable compatibility anchor, provided target facts already reduce the actionable first-stage space to three meaningful Powder+Liquid branches?**

## Universal player-visible law

A valid three-component formula is prepared in two stages:
1. Порошок + Жидкость must be STABLE.
2. Жидкость + Эссенция must be STABLE.

A microtest checks one concrete adjacent pair and returns:
- STABLE;
- INCOMPATIBLE / SEPARATES.

Compatibility is reusable empirical knowledge about the pair.

Порошок + Эссенция is never tested directly.

## Candidate pool — Russian display names

Порошки:
- P1 Порошок коры — {Растение}
- P2 Хитиновый порошок — {Насекомое}
- P3 Меловой порошок — {Минерал}

Жидкости:
- L1 Янтарный раствор — {Растение, Насекомое}
- L2 Ржавый раствор — {Насекомое, Минерал}
- L3 Траурный раствор — {Растение, Труп}

Эссенции:
- E1 Падальная эссенция — {Насекомое, Труп}
- E2 Ископаемая эссенция — {Минерал, Труп}
- E3 Кристальная эссенция — {Растение, Минерал}

## Initial target research

The target contains:
- Растение in exactly one component;
- Труп in exactly one component.

Applying only these facts leaves six target-compatible triples distributed across exactly three Powder+Liquid first-stage branches.

Do not enumerate those branches or triples automatically for the player.

## Prior empirical knowledge

None.

The journal contains no known compatibility result for any candidate pair.

## Hidden compatibility table

Powder-Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE
- P2 + L3 -> INCOMPATIBLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

Liquid-Essence:
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden valid answer

P2 + L1 + E2

## Resources

Start with 4 Research Charges.
Each microtest costs 1.
Full synthesis costs no Research Charge.

## Player-facing journal

Show:
- all 3 candidates per slot using the Russian display names above;
- target facts Растение ×1 / Труп ×1;
- no prior compatibility observations;
- each raw pair outcome;
- remaining charges.

Do not:
- enumerate target-compatible triples or first-stage branches;
- show a compatibility matrix;
- recommend a pair;
- infer new eliminations before the player does.

## Evaluation targets

Same as Prototype 20:
- can the player derive a small actionable branch set without notes;
- is the first microtest hypothesis-driven;
- does a negative result improve orientation;
- does a stable result become a useful anchor;
- does the player drift into matrix completion;
- is 3×3×3 still too heavy despite only three meaningful first-stage branches;
- microtests before synthesis;
- whether the 2–4 branch envelope should be tightened in no-anchor states.

## Integrity rule

All target facts, candidate properties, hidden formula, compatibility outcomes and resource limits are immutable for the blind run.

## Live activation checkpoint

Status: active blind play; awaiting the player's first microtest choice.

Current state:
- 3×3×3 candidate pool above;
- target facts: Растение ×1; Труп ×1;
- known compatibility observations: none;
- Research Charges: 4/4;
- completed actions: none;
- legal next action: any adjacent pair microtest or full synthesis.


## Live checkpoint 1

Player reasoning before the first microtest:
- noticed that P1 Порошок коры is the only Powder candidate carrying Растение;
- reasoned conditionally that if P1 belongs to the target, the Liquid cannot also carry Растение, so L2 Ржавый раствор is the target-compatible Liquid continuation;
- reasoned that the Essence would then need to supply Труп without adding another Растение, leaving E1 Падальная эссенция or E2 Ископаемая эссенция as conditional continuations;
- chose the concrete first-stage microtest P1 + L2.

Player action:
- microtest P1 Порошок коры + L2 Ржавый раствор.

Raw outcome: **INCOMPATIBLE / НЕСОВМЕСТИМО**.

Resources:
- Research Charges remaining: **3 / 4**.

Presentation note:
- the player's client rendered the Растение and Труп glyphs but not the previous Насекомое and Минерал glyphs;
- subsequent player-facing screens should use more broadly supported display glyphs (🐞 Насекомое, 💎 Минерал) without changing any prototype semantics.

No facilitator deduction from the fresh result. Await player inference / next action.


## Live checkpoint 2

Player inference after the first microtest:
- treated the P1 + L2 incompatibility as rejecting the conditional P1 target branch;
- decided not to spend more tests on P1;
- moved to P2 Хитиновый порошок;
- reasoned that with P2 + L1 Янтарный раствор, the target facts Растение ×1 / Труп ×1 allow either E1 Падальная эссенция or E2 Ископаемая эссенция as conditional continuations.

Player action:
- microtest P2 Хитиновый порошок + L1 Янтарный раствор.

Raw outcome: **STABLE / СТАБИЛЬНО**.

Resources:
- Research Charges remaining: **2 / 4**.

No facilitator deduction from the fresh result. Await player inference / next action.


## Live checkpoint 3

Player inference before the third microtest:
- accepted P2 + L1 as a stable first-stage branch;
- chose to test one of its two target-compatible Essence continuations directly.

Player action:
- microtest L1 Янтарный раствор + E1 Падальная эссенция.

Raw outcome: **INCOMPATIBLE / НЕСОВМЕСТИМО**.

Resources:
- Research Charges remaining: **1 / 4**.

No facilitator deduction from the fresh result. Await player inference / next action.


## Live completion

Clarification:
- the player briefly misspoke `P1 + L1 + E2`, immediately corrected it before any synthesis result was resolved;
- no action was taken for the misspoken formula and no state/resource change occurred.

Player final action:
- synthesize P2 Хитиновый порошок + L1 Янтарный раствор + E2 Ископаемая эссенция.

Deterministic outcome: **SUCCESS / УСПЕХ**.

Resources:
- Research Charges used: **3 / 4**;
- Research Charges remaining: **1 / 4**;
- microtests: 3;
- failed synthesis attempts: 0.

Observed blind-play path:
1. P1 + L2 -> INCOMPATIBLE, eliminating the player's first conditional branch.
2. P2 + L1 -> STABLE, establishing a viable first-stage anchor.
3. L1 + E1 -> INCOMPATIBLE, falsifying one of the two target-compatible continuations.
4. Player synthesized P2 + L1 + E2 and succeeded.

Facilitator did not supply the player's new deductions after fresh observations.

Subjective evaluation pending.


## Player subjective evaluation

The run was manageable and did not feel like blind brute force. The player used target properties to discard impossible combinations, then tested only plausible branches.

However, the starting state felt under-structured. With only two target properties and no prior relational information, the early interaction still felt too much like sequentially checking admissible pairs.

Accepted player-experience finding:
- do not increase difficulty merely by increasing cognitive load;
- lower working-memory burden is acceptable and may be preferable;
- the preferred improvement is richer legitimate starting structure: constraints or pair relationships that intersect, reinforce, or rule one another out;
- the interesting part should be reasoning inside an already-shaped space, not building the whole useful structure by pair testing.

Disposition:
- calibrated no-anchor 3x3x3 is viable;
- it is not the preferred ordinary presentation when richer starting knowledge can be supplied legitimately;
- the next prototype should test a similarly bounded field with richer starting relational structure without pre-solving the target.
