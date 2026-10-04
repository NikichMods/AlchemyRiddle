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
