# Prototype 26 — Adaptive information budget

**FACILITATOR SPOILERS — DO NOT SURFACE DURING LIVE PLAY**

Status: **precommitted before the player's first action**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `0adce80bb9901922d1300bb5a6fe0bbee7aa2e08`;
- research branch: `research/prototype-26-adaptive-information-budget`;
- accepted three-slot core: Adaptive Knowledge-Aware;
- production implementation remains **BLOCKED**.

## Research question

Prototype 25 showed:
- relation-rich openings are preferred;
- two target-property constraints are acceptable;
- current three-column panel density is a strong UX reference;
- when relation history is sparse, the player hypothesizes that richer reagent
  property cards plus more target-property constraints may compensate.

Question:

> Can a sparse-history state with richer multi-property reagents and several
> weak target constraints feel comparably "partially formed" to a relation-rich
> state, without becoming a bookkeeping wall or over-solving the target?

## Existing evidence / method checkpoint

No new host/runtime probe or research harness is required before this blind test.

Accepted real-corpus evidence already establishes:
- the fixed 35-reagent property model contains 16 one-property, 14 two-property,
  and 5 three-property reagents;
- balanced two-fact starts exist for 16/16 ordinary three-slot outputs;
- progressive three-fact starts exist for 14/16;
- the adaptive architecture screen already shows target-fact demand falling as
  prior compatibility knowledge rises.

The residual uncertainty is experiential and presentation-oriented.
A matched synthetic blind paper-prototype pair is therefore the least-complex
adequate next method.

## Shared presentation contract

Both investigations use:
- a 3x3x3 candidate field;
- multi-property reagent cards;
- spatially distinct Powder / Liquid / Essence columns;
- the same universal compatibility and synthesis semantics;
- 8 Research Charges;
- 1 charge per adjacent microtest;
- 0 charge per full synthesis;
- no cross-investigation knowledge transfer.

Do not reveal the comparison labels during play.

## Universal player-visible rules

Recipe:
- Powder + Liquid + Essence.

Legal microtests:
- Powder + Liquid;
- Liquid + Essence;
- Powder + Essence is not directly testable.

Microtest result:
- **СТАБИЛЬНО** or **НЕСОВМЕСТИМО**.

A viable complete chain requires both adjacent relations to be stable.
That does not guarantee the target.

Full synthesis outcomes:
- exact target -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- compatible non-target -> **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**;
- other non-target -> **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; ПОЛНАЯ УСТОЙЧИВАЯ ЦЕПОЧКА НЕ ПОДТВЕРЖДЕНА.**

A synthesis does not silently add unknown pair records.

# Investigation I — sparse-history compensated opening

Player-facing target: **Реагент согласования**.

## Candidate field

### Powders
- P1 **Волокнистый порошок** — {Растение, Насекомое}
- P2 **Белёсый порошок** — {Труп, Минерал}
- P3 **Каменный порошок** — {Минерал}

### Liquids
- L1 **Зелёный раствор** — {Растение, Слизь}
- L2 **Живой раствор** — {Труп, Растение, Насекомое}
- L3 **Кристальный раствор** — {Минерал, Насекомое}

### Essences
- E1 **Светлая эссенция** — {Растение, Слизь}
- E2 **Тёмная эссенция** — {Труп, Слизь}
- E3 **Летучая эссенция** — {Насекомое}

## Target-specific facts

Player-visible:
1. **Минерал встречается ровно в одном из трёх компонентов.**
2. **Труп встречается ровно в одном из трёх компонентов.**
3. **Растение встречается ровно в одном из трёх компонентов.**

## Prior laboratory knowledge

Exactly one prior relation:
- P1 + L3 -> **СТАБИЛЬНО**.

No other pair relation is known at start.

## Target-fact-consistent triples

Facilitator-only:
- P1 + L3 + E2;
- P2 + L1 + E3;
- P3 + L1 + E2;
- P3 + L2 + E3.

Do not enumerate to the player.

The prior P1+L3 anchor plus all three target facts determines E2 as its only
target-consistent continuation.

## Hidden compatibility table

### Powder-Liquid
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE

- P2 + L1 -> STABLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> STABLE

- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> STABLE
- L1 + E3 -> INCOMPATIBLE

- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE

- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden target

**P3 + L2 + E3**

## Designed compatible non-target

**P1 + L3 + E2**

Both adjacent links are stable and the triple satisfies all target facts.

Among the four target-fact-consistent triples:
- P1+L3+E2 -> compatible non-target;
- P2+L1+E3 -> blocked by L1+E3;
- P3+L1+E2 -> blocked by P3+L1;
- P3+L2+E3 -> TARGET.

## Intended-but-not-forced reasoning shape

The opening should visibly contain:
- rich reagent signatures;
- three intersecting target facts;
- one old stable anchor.

The old anchor can be completed by target facts alone to a specific candidate
triple, creating an immediate hypothesis without requiring a new discovery
first. After that decoy is excluded, the remaining facts still leave several
branches and compatibility must finish the deduction.

Do not direct the player to the anchor.

# Investigation II — relation-rich reference opening

Player-facing target: **Реагент настройки**.

## Candidate field

### Powders
- P1 **Пыльцевой порошок** — {Растение, Насекомое}
- P2 **Тёмный порошок** — {Труп, Слизь}
- P3 **Кристаллический порошок** — {Минерал}

### Liquids
- L1 **Травяной раствор** — {Растение, Слизь}
- L2 **Серебристый раствор** — {Минерал, Насекомое}
- L3 **Мрачный раствор** — {Труп}

### Essences
- E1 **Сухая эссенция** — {Растение}
- E2 **Тёмная эссенция** — {Труп, Слизь}
- E3 **Кристальная эссенция** — {Минерал, Насекомое}

## Target-specific fact

Player-visible:
- **Минерал встречается ровно в одном из трёх компонентов.**

## Prior laboratory knowledge

Exactly three prior relations:
- P1 + L2 -> **СТАБИЛЬНО**;
- P3 + L3 -> **СТАБИЛЬНО**;
- L2 + E1 -> **НЕСОВМЕСТИМО**.

No other pair relation is known at start.

## Hidden compatibility table

### Powder-Liquid
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE

- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> INCOMPATIBLE

- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> STABLE
- L1 + E3 -> STABLE

- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE

- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> STABLE

## Hidden target

**P3 + L3 + E1**

## Designed compatible non-target

**P1 + L2 + E2**

Target-fact handling:
- P1+L2 already contains the single allowed Mineral at L2, so E3 is excluded
  by the target fact;
- E1 is pre-known incompatible with L2;
- E2 is therefore the only target-consistent continuation of that anchor;
- L2+E2 is hidden STABLE, producing the compatible decoy.

Second anchor:
- P3+L3 is pre-known STABLE and already contains the single allowed Mineral at
  P3;
- E1 and E2 are target-consistent;
- L3+E1 is hidden STABLE and is the TARGET;
- L3+E2 is hidden INCOMPATIBLE.

## Intended-but-not-forced reasoning shape

This is the relation-rich reference:
- one target fact;
- three old relations;
- rich reagent property cards;
- two visible stable anchors.

It should remain close to the information-density reference from Prototype 25.

# Evaluation protocol

Do not ask comparative questions until both investigations are complete.

During each case record:
- whether the player has an immediate justified hypothesis before a new test;
- whether multi-property reagent cards help or create scan burden;
- whether the target facts feel like interacting constraints or bookkeeping;
- whether the opening feels already partially formed;
- microtest and synthesis counts;
- whether any candidate state feels over-solved.

After both ask:
- which case felt more like a partially completed sculpture;
- did Investigation I successfully compensate for sparse relation history;
- did three target facts feel useful, neutral, or excessive;
- did multiple tags on reagents improve reasoning enough to justify their screen cost;
- did either case exceed the Prototype-25 ideal information density;
- approximate preference / rating;
- whether adaptive compensation should be retained, revised, or rejected.

Possible dispositions:
- **ADAPTIVE COMPENSATION RETAIN**;
- **RELATIONS STILL REQUIRED**;
- **TAG-RICH TOO DENSE**;
- **REVISE COMPENSATION**.

# Starting checkpoint

- active prototype: **26**;
- active case: **Investigation I**;
- Research Charges: **8 / 8**;
- prior journal: P1 + L3 -> STABLE;
- no new actions;
- no synthesis exclusions;
- awaiting player's first action.


## Live checkpoint 1 — Investigation I

Player design observations before acting:
- target-property clues need not all use the same exact-count wording; absence facts such as “tag X does not occur” may be interesting;
- slot-local tag clues may also be viable in some cases, e.g. a property is present/absent in a specific slot, provided they do not collapse to an exact ingredient too directly;
- controlled extra candidate noise may be acceptable when tag clues immediately eliminate some of it, but this is explicitly a hypothesis to test rather than an accepted rule;
- tag clues are viewed as less intrinsically interesting than accumulated stable-pair knowledge, so they may tolerate somewhat more variety/volume to keep reasoning from feeling repetitive;
- early-game investigations should not artificially avoid a first hypothesis that can succeed quickly if the player reached it through meaningful multi-step reasoning; a short “micro-wow” can be desirable for teaching and competence reinforcement.

Player reasoning:
- starts from prior P1+L3 STABLE;
- notes P1 contributes Plant and Insect while L3 contributes Mineral and Insect;
- under the three target facts, Corpse is still missing and E2 carries Corpse;
- chooses L3+E2 as the next microtest.

Player action:
- microtest L3 + E2.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE.

No facilitator deduction beyond confirming the player-stated reasoning.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 2 — Investigation I

Player action:
- full synthesis P2 + L3 + E2.

Outcome:
- adjacent links are stable;
- target effect absent.

Triple exclusion:
- P2 + L3 + E2 is not the target recipe.

No new pairwise journal fact is inferred from synthesis.

Resources:
- Research Charges: 7 / 8;
- full syntheses: 1;
- compatible non-target syntheses: 1.

Current interaction point:
- awaiting next player action.


## Live checkpoint 3 — Investigation I

Player design observations before acting:
- a compatible non-target synthesis should potentially grant a small consolation/research reward so the outcome acknowledges that the player reasoned correctly even though the hidden target was not hit;
- simplest candidate reward: restore some Research Charge(s); exact economy and presentation remain open;
- UI distinction between **starting/prior knowledge** and **newly learned facts** feels useful and should be preserved visually;
- after the first well-justified compatible decoy failed, the player felt the opening structure largely disappeared and explicitly described the next move as simple enumeration;
- this is evidence that rich target tags can create a strong first hook but may fail to sustain a second reasoning step when too few relation anchors remain.

Player reasoning:
- P1+L3 was the initial anchor and its E2 continuation was stable, but that line did not yield the target;
- the player no longer sees another comparably structured continuation and chooses the next unexplored Powder-Liquid pair by simple enumeration.

Player action:
- microtest P2 + L1.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **6 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE;
- P2 + L3 + E2 -> NOT the current target;
- new: P2 + L1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 4 — Investigation I

Player reasoning:
- P2+L1 is stable;
- P2 contributes Corpse + Mineral and L1 contributes Plant + Slime;
- under the target constraints, E3 is the natural continuation candidate;
- player chooses L1+E3.

Player action:
- microtest L1 + E3.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **5 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE;
- P2 + L3 + E2 -> NOT the current target;
- new: P2 + L1 -> STABLE;
- new: L1 + E3 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 5 — Investigation I

Player reasoning:
- explicitly closes the P2 branch from visible target constraints plus the failed L1+E3 continuation;
- identifies P3+L1 as the next plausible branch: Mineral + Plant leaves Corpse still required.

Player action:
- microtest P3 + L1.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **4 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE;
- P2 + L3 + E2 -> NOT the current target;
- new: P2 + L1 -> STABLE;
- new: L1 + E3 -> INCOMPATIBLE;
- new: P3 + L1 -> INCOMPATIBLE.

No facilitator deduction beyond confirming the player-stated P2 branch closure.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 6 — Investigation I

Player action:
- microtest P3 + L2.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **3 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE;
- P2 + L3 + E2 -> NOT the current target;
- new: P2 + L1 -> STABLE;
- new: L1 + E3 -> INCOMPATIBLE;
- new: P3 + L1 -> INCOMPATIBLE;
- new: P3 + L2 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 7 — Investigation I

Player action:
- microtest L2 + E3.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **2 / 8**.

Journal now contains:
- prior: P1 + L3 -> STABLE;
- new: L3 + E2 -> STABLE;
- P2 + L3 + E2 -> NOT the current target;
- new: P2 + L1 -> STABLE;
- new: L1 + E3 -> INCOMPATIBLE;
- new: P3 + L1 -> INCOMPATIBLE;
- new: P3 + L2 -> STABLE;
- new: L2 + E3 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.
