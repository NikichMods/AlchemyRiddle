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


## Live checkpoint 4 — Investigation I

Player inference:
- rejected the P1 start after the observed compatibility results;
- chose microtest P2 + L1.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **4 / 8**.

Journal now contains:
- P1 + L1 -> STABLE;
- L1 + E1 -> INCOMPATIBLE;
- P1 + L2 -> INCOMPATIBLE;
- P2 + L1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 5 — Investigation I

Player action:
- microtest L1 + E2.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **3 / 8**.

Journal now contains:
- P1 + L1 -> STABLE;
- L1 + E1 -> INCOMPATIBLE;
- P1 + L2 -> INCOMPATIBLE;
- P2 + L1 -> STABLE;
- L1 + E2 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 6 — Investigation I

Player action:
- full synthesis P2 + L1 + E2.

Deterministic outcome:
- **TARGET EFFECT OBTAINED**.

Investigation I is solved.

Resources:
- Research Charges used: 5 / 8;
- Research Charges remaining: **3 / 8**;
- full synthesis attempts: 1;
- successful target syntheses: 1.

Observed reasoning path before success:
1. Apply the single-Mineral target fact.
2. Test P1+L1 -> STABLE.
3. Test L1+E1 -> INCOMPATIBLE.
4. Test P1+L2 -> INCOMPATIBLE.
5. Reject P1 as the starting Powder.
6. Test P2+L1 -> STABLE.
7. Test L1+E2 -> STABLE.
8. Synthesize P2+L1+E2 -> TARGET.

Do not solicit comparative evaluation yet; start Investigation II next.


## Investigation II activated

Investigation I is complete. Per the precommitted matched protocol, comparative evaluation is deferred until both cases are solved.

Active matched case: **Investigation II**.

Resources reset:
- Research Charges: **8 / 8**;
- no transferred relation knowledge;
- no synthesis exclusions.

Awaiting the player's first action in Investigation II.


## Live checkpoint 7 — Investigation II

Player inference:
- noticed the second matched case uses a 2x3x2 field rather than 2x2x2;
- applied the two-Mineral target fact and chose microtest P1 + L3.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Investigation II journal now contains:
- P1 + L3 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 8 — Investigation II

Player action:
- microtest L3 + E2.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **6 / 8**.

Investigation II journal now contains:
- P1 + L3 -> STABLE;
- L3 + E2 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 9 — Investigation II

Player action:
- microtest L3 + E1.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **5 / 8**.

Investigation II journal now contains:
- P1 + L3 -> STABLE;
- L3 + E2 -> INCOMPATIBLE;
- L3 + E1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 10 — Investigation II

Player action:
- microtest P2 + L3.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **4 / 8**.

Investigation II journal now contains:
- P1 + L3 -> STABLE;
- L3 + E2 -> INCOMPATIBLE;
- L3 + E1 -> STABLE;
- P2 + L3 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 11 — Investigation II

Player action:
- full synthesis P2 + L3 + E1.

Deterministic outcome:
- both adjacent links remain **STABLE**;
- **TARGET EFFECT ABSENT**.

Journal retains:
- P2 + L3 -> STABLE;
- L3 + E1 -> STABLE.

Triple-level exclusion added:
- P2 + L3 + E1 -> NOT the recipe for the current target.

Resources:
- Research Charges remaining: **4 / 8**;
- full synthesis attempts in Investigation II: 1;
- compatible non-target syntheses: 1.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 12 — Investigation II

Player action:
- full synthesis P2 + L2 + E2.

Deterministic outcome:
- **TARGET EFFECT ABSENT; FULL STABLE CHAIN NOT CONFIRMED**.

This synthesis does not add pairwise relation records that were not independently established.

Triple-level exclusion added:
- P2 + L2 + E2 -> NOT the recipe for the current target.

Resources:
- Research Charges remaining: **4 / 8**;
- full synthesis attempts in Investigation II: 2;
- compatible non-target syntheses: 1.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 13 — Investigation II

Player reasoning/confusion checkpoint:
- player correctly recognized that exactly two Mineral-bearing components yields three positional patterns;
- player noticed P1+L3+E2 as the remaining pattern without Powder Mineral, then rejected it because L3+E2 is already known INCOMPATIBLE;
- P2+L3+E1 has already been synthesized as compatible non-target;
- P2+L2+E2 has already been synthesized as non-target with no full stable chain;
- therefore only one target-fact-consistent triple remains unexcluded: P2+L1+E2.

UX evidence:
- despite having logically reduced the state to a single remaining hypothesis, the player reported confusion and felt as though there might be no options left;
- this suggests the journal/state presentation does not sufficiently surface elimination coverage or the fact that a unique hypothesis has been reached.

No new experimental result occurred in this checkpoint.


## Live checkpoint 14 — Presentation confound

Player UX clarification:
- the confusion at the unique-hypothesis state was materially caused by the chat presentation layout, not just by the puzzle logic;
- presenting all reagents as a single vertical table made slot membership harder to scan visually;
- the player reports that the earlier three-column presentation (Powders / Liquids / Essences as distinct spatial columns) made candidate relationships much easier to perceive at a glance;
- the player still acknowledges a momentary reasoning lapse, but explicitly identifies layout as a significant contributor.

Research interpretation:
- do **not** count checkpoint 13 confusion as clean evidence that 2x3x2 is cognitively too complex or that the deduction itself failed;
- it is confounded by facilitator/UI presentation;
- future paper prototypes comparing field sizes should preserve a slot-column layout so the tested variable is field size / reasoning, not visual parsing cost;
- candidate slot grouping is now a concrete UX requirement to evaluate for production presentation.

No new experimental result occurred in this checkpoint.


## Live completion — Investigation II

Player action:
- full synthesis P2 + L1 + E2.

Deterministic outcome:
- **TARGET EFFECT OBTAINED**.

Investigation II is solved.

Resources:
- Research Charges used: 4 / 8;
- Research Charges remaining: **4 / 8**;
- full synthesis attempts: 3;
- compatible non-target syntheses: 1;
- unsuccessful non-compatible syntheses: 1;
- successful target syntheses: 1.

Observed reasoning path:
1. Apply the two-Mineral target fact.
2. Test P1+L3 -> STABLE.
3. Test L3+E2 -> INCOMPATIBLE.
4. Test L3+E1 -> STABLE.
5. Test P2+L3 -> STABLE.
6. Synthesize P2+L3+E1 -> compatible non-target.
7. Synthesize P2+L2+E2 -> non-target; full stable chain not confirmed.
8. Reconstruct the three positional ways to place exactly two Mineral-bearing components.
9. Notice P1+L3+E2 is already invalid because L3+E2 is INCOMPATIBLE.
10. Conclude P2+L1+E2 is the only remaining target-consistent unexcluded triple.
11. Synthesize P2+L1+E2 -> TARGET.

Matched pair is now complete. Proceed to comparative player evaluation per the precommitted protocol.


## Final player evaluation

Disposition: **REJECT CURRENT SPARSE-START FLOOR GRAMMAR**.

Player comparative evaluation:
- Investigation I (2x2x2) was clearly boring;
- the experience felt like mechanically checking possibilities until the answer remained, closer to something to get through than a satisfying discovery;
- the single target fact "Mineral appears exactly once" was too simple and too weak as an opening structure;
- Investigation II (2x3x2) was somewhat more engaging, but only modestly so;
- the fact "Mineral appears exactly twice" still left the player feeling that the puzzle began from an almost blank search space;
- the earlier vertical-table presentation worsened Investigation II and is a confound, but correcting layout would not solve the deeper engagement problem.

Primary design insight:
- field size is **not** the main unresolved variable;
- the important issue is the **amount and shape of structure present at the start**;
- the player does not want to begin from a nearly unworked possibility block and repeatedly carve away options;
- the preferred experience is analogous to receiving a sculpture that is already partly formed, then making the final meaningful deductions that complete it;
- therefore the opening state should already contain several mutually useful constraints / known relations / target facts that form recognizable structure before the first experiment.

Interpretation:
- 2x2x2 should **not** be accepted as a normal production-quality floor under the tested sparse-start grammar;
- 2x3x2 is not validated merely because it was slightly better;
- increasing field size alone does not address the core problem;
- the next design work should focus on richer prestructured starting states, not on simply enlarging the candidate grid.

Relation to prior evidence:
- this is consistent with Prototype 23's stronger experience, where prior stable/incompatible relations plus a target fact created a partially solved landscape and the player investigated a few justified hypotheses;
- Prototype 23's seven surfaced old relations were visually too many, while one target fact alone felt sparse;
- the next target is therefore a **middle-information opening**: enough pre-existing structure to make the candidate space feel partially carved, but not so much journal clutter that the player is scanning a wall of facts.

New research question:
> What minimum opening information package makes the player feel they are completing a meaningful deduction rather than reducing a blank combinatorial space?

Candidate families to compare next:
- 2 target-specific facts + a small number of neutral prior relations;
- 1 target-specific fact + 2-4 carefully surfaced neutral prior relations;
- a compact derived structural clue plus 1-2 prior relations;
- equivalent-information presentations that differ in whether the structure is target-centric or relation-centric.

Do not assume one family is accepted architecture yet. Compare them before implementation.

Production implementation remains **BLOCKED**.
