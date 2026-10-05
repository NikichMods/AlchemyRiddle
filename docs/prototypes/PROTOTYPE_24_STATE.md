# Prototype 24 — Variable-field minimum floor matched pair

**FACILITATOR SPOILERS — DO NOT SURFACE DURING LIVE PLAY**

Status: **precommitted before the player's first action**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `0d586ac6d8060064f53a36527d13c171169bb327`;
- research branch: `research/prototype-24-variable-field-floor`;
- accepted three-slot core: Adaptive Knowledge-Aware;
- production implementation remains **BLOCKED**.

## Research question

The quantitative progression-limited screen promoted 2x2x2 to the minimum-floor
blind-test candidate and showed 2x3x2 / 3x2x2 as very robust slightly richer
compact shapes.

The remaining question is experiential:

> Does a well-formed 2x2x2 adaptive investigation still feel like a real
> deduction the player worked out, or does it collapse into short enumeration
> compared with a matched 2x3x2 case?

## Research-method checkpoint

Existing corpus statistics cannot answer subjective puzzle quality.

No new host/runtime probe is required.

The least-complex adequate method is a matched synthetic paper-prototype pair
using the already accepted target-property + adjacent-compatibility grammar.

The pair deliberately removes resource scarcity and progression acquisition
from the tested variable.

## Blindness / order caveat

The user knows from the preceding design discussion that compact field size is
the current research topic. The visible candidate counts also make field size
observable.

Therefore this is blind with respect to:
- hidden target formula;
- hidden compatibility graph;
- designed compatible decoy;
- intended reasoning path.

It is **not** blind with respect to the fact that the two cases differ in field
size.

Order is precommitted:
1. Investigation I — 2x2x2;
2. Investigation II — 2x3x2.

Do not reveal the size labels during live play until the matched pair is
complete.

## Universal player-visible rules

Every investigation has:
- Powder + Liquid + Essence;
- a bounded candidate field;
- one target-property fact;
- pairwise compatibility microtests;
- full synthesis.

Legal adjacent microtests:
- Powder + Liquid -> **СТАБИЛЬНО / НЕСОВМЕСТИМО**;
- Liquid + Essence -> **СТАБИЛЬНО / НЕСОВМЕСТИМО**;
- Powder + Essence cannot be tested directly.

Meaning:
- both adjacent links being stable is necessary for a fully compatible chain;
- a fully compatible chain is not guaranteed to be the requested target;
- a compatible non-target synthesis excludes only that exact triple;
- pairwise results remain true after synthesis.

Full synthesis outcomes:
- exact hidden formula -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- non-target with both adjacent links stable ->
  **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**;
- other non-target ->
  **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; ПОЛНАЯ УСТОЙЧИВАЯ ЦЕПОЧКА НЕ ПОДТВЕРЖДЕНА.**

A full synthesis does not silently add pair results that were not independently
known.

## Resource model

For each investigation independently:
- Research Charges: **8 / 8**;
- one adjacent microtest costs **1**;
- full synthesis costs **0**;
- candidate reagent quantities are not modeled;
- charges are intentionally ample so scarcity does not drive the comparison.

There is no prior compatibility knowledge in either investigation.

This intentionally represents an early / low-expertise state.

# Investigation I — hidden facilitator model

Player-facing target: **Реагент тишины**.

## Candidate field

### Powders
- P1 **Пепельный порошок** — {Труп}
- P2 **Серебристый порошок** — {Минерал}

### Liquids
- L1 **Тихий раствор** — {Растение}
- L2 **Густой раствор** — {Насекомое}

### Essences
- E1 **Каменная эссенция** — {Минерал}
- E2 **Сухая эссенция** — {Растение}

## Target-specific fact

Player-visible:

**Минерал встречается ровно в одном из трёх компонентов.**

No other target-property fact is available at start.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE

### Liquid-Essence
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE

## Hidden target formula

**P2 Серебристый порошок + L1 Тихий раствор + E2 Сухая эссенция**

## Compatible non-target chain

**P2 Серебристый порошок + L2 Густой раствор + E2 Сухая эссенция**

Both adjacent links are stable and the target-property fact is satisfied, but
full synthesis returns the compatible-non-target outcome.

## Target-fact-consistent hidden candidates

Facilitator-only:
- P1 + L1 + E1;
- P1 + L2 + E1;
- P2 + L1 + E2 — TARGET;
- P2 + L2 + E2 — compatible non-target.

Do not enumerate this set to the player.

## Intended quality shape

The one target fact leaves four exact candidate triples across all four
Powder-Liquid branches.

Complete compatibility removes the two P1 hypotheses and leaves exactly:
- the target;
- one compatible non-target.

The player must still use compatibility and possibly synthesis to distinguish
identity.

No path is forced.

# Investigation II — hidden facilitator model

Player-facing target: **Реагент ясности**.

## Candidate field

### Powders
- P1 **Тёмный порошок** — {Труп}
- P2 **Кристаллический порошок** — {Минерал}

### Liquids
- L1 **Бледный раствор** — {Растение}
- L2 **Густой раствор** — {Труп}
- L3 **Каменный раствор** — {Минерал}

### Essences
- E1 **Сухая эссенция** — {Растение}
- E2 **Кристальная эссенция** — {Минерал}

## Target-specific fact

Player-visible:

**Минерал встречается ровно в двух из трёх компонентов.**

No other target-property fact is available at start.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE

## Hidden target formula

**P2 Кристаллический порошок + L1 Бледный раствор + E2 Кристальная эссенция**

## Compatible non-target chain

**P2 Кристаллический порошок + L3 Каменный раствор + E1 Сухая эссенция**

Both adjacent links are stable and the target-property fact is satisfied, but
full synthesis returns the compatible-non-target outcome.

## Target-fact-consistent hidden candidates

Facilitator-only:
- P1 + L3 + E2;
- P2 + L1 + E2 — TARGET;
- P2 + L2 + E2;
- P2 + L3 + E1 — compatible non-target.

Do not enumerate this set to the player.

## Intended quality shape

The one target fact leaves four exact candidate triples across four
Powder-Liquid branches even though the visible raw field is larger than
Investigation I.

Complete compatibility removes two hypotheses and leaves exactly:
- the target;
- one compatible non-target.

This intentionally holds the post-property hypothesis count roughly constant
while increasing the visible candidate-field richness.

# Matched evaluation protocol

Do not ask for comparative evaluation until both investigations are complete.

After Investigation I:
- ask only for the player's next action until solved;
- record meaningful microtests, syntheses, self-generated deductions, confusion,
  and whether actions felt like justified hypothesis tests;
- do not tell the player whether this was the smaller or larger test condition.

Then start Investigation II with fresh resources and no transferred relation
knowledge.

After Investigation II, ask for:
- which investigation felt better and why;
- whether Investigation I felt like genuine deduction or merely checking four
  options;
- whether Investigation II added useful reasoning or only visual/working-memory
  burden;
- preferred minimum field size;
- approximate 1-5 rating for each;
- whether either case felt too long for an atomic Graveyard Keeper interaction.

Primary acceptance question:

> Is 2x2x2 acceptable as the normal minimum production-quality field?

Possible dispositions:
- **ACCEPT FLOOR** — 2x2x2 is satisfying enough for early progression;
- **FALLBACK ONLY** — usable, but normal floor should require at least one
  three-candidate slot;
- **REJECT** — compact field feels enumerative/trivial and needs a different
  early-game grammar.

# Starting checkpoint

- active prototype: **24**;
- matched case: **Investigation I**;
- Research Charges: **8 / 8**;
- no relation records;
- no synthesis exclusions;
- awaiting the player's first action.


## Live checkpoint 1 — Investigation I

Player inference:
- the single-Mineral target fact was applied to the visible candidate properties;
- player chose microtest P1 Пепельный порошок + L1 Тихий раствор.

Raw outcome:
- **СТАБИЛЬНО**.

Resources:
- Research Charges remaining: **7 / 8**.

Journal now contains:
- P1 + L1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 2 — Investigation I

Player action:
- microtest L1 + E1.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **6 / 8**.

Journal now contains:
- P1 + L1 -> STABLE;
- L1 + E1 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 3 — Investigation I

Player action:
- microtest P1 + L2.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **5 / 8**.

Journal now contains:
- P1 + L1 -> STABLE;
- L1 + E1 -> INCOMPATIBLE;
- P1 + L2 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.
