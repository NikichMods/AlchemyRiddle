# Prototype 25 — Middle-information opening structure

**FACILITATOR SPOILERS — DO NOT SURFACE DURING LIVE PLAY**

Status: **precommitted before the player's first action**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `e8737eebe7e2eef4035f138425f3a9284fb0bef4`;
- research branch: `research/prototype-25-opening-structure`;
- accepted three-slot core: Adaptive Knowledge-Aware;
- production implementation remains **BLOCKED**.

## Research question

Prototype 24 showed that field size alone is not the main engagement variable.
The player prefers to begin from a partially formed deduction state rather than
a nearly blank combinatorial field.

Question:

> Which kind of middle-information opening better creates the feeling of
> "finishing a partially formed sculpture": more target-specific constraints,
> or fewer target constraints plus a small reusable relation history?

## Solution-space checkpoint

Goal:
- preserve a short atomic investigation;
- give the player visible starting structure before the first experiment;
- avoid both sparse-start blankness and Prototype 23's seven-relation clutter;
- keep deduction player-owned rather than disclosing the formula.

Useful families:
1. **Target-rich hybrid** — two target-specific constraints + one prior relation.
2. **Relation-rich hybrid** — one target-specific constraint + three prior relations.
3. **New derived structural clue** — a new clue type that summarizes structure more directly.
4. **More/larger candidate fields** — increase search space without increasing starting structure.

Choice for Prototype 25:
- compare families 1 and 2 first;
- hold field size at 3x3x3;
- defer family 3 because it introduces a new semantic mechanism before simpler
  existing ingredients have been compared;
- reject family 4 as the immediate next step because Prototype 24 already showed
  that field size alone does not solve the engagement problem.

## Research-method checkpoint

Exact uncertainty is experiential: whether the opening feels partially solved
and gives immediate reasoning hooks.

Existing corpus statistics cannot answer this.
No new game/runtime probe is required.
A matched synthetic paper-prototype pair is the least-complex adequate method.

## Presentation contract

At every player decision point, candidates must be shown in a **three-column
slot layout**:

| Powders | Liquids | Essences |
| --- | --- | --- |
| P1 ... | L1 ... | E1 ... |
| P2 ... | L2 ... | E2 ... |
| P3 ... | L3 ... | E3 ... |

Do not replace this with one vertical mixed list.

Known relations must be shown separately in the journal.

## Universal player-visible rules

Recipe arity:
- Powder + Liquid + Essence.

Legal adjacent microtests:
- Powder + Liquid -> **СТАБИЛЬНО / НЕСОВМЕСТИМО**;
- Liquid + Essence -> **СТАБИЛЬНО / НЕСОВМЕСТИМО**;
- Powder + Essence cannot be tested directly.

Meaning:
- both adjacent stable relations are necessary for a viable staged mixture;
- they are not sufficient to prove target identity;
- compatible non-target synthesis excludes only that exact triple;
- established pair relations remain true after synthesis.

Full synthesis outcomes:
- exact target formula -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- non-target triple with both adjacent relations stable ->
  **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**;
- other non-target triple ->
  **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; ПОЛНАЯ УСТОЙЧИВАЯ ЦЕПОЧКА НЕ ПОДТВЕРЖДЕНА.**

A full synthesis does not silently add pair records that were not already
established by microtest/history.

## Resource model

Each investigation independently:
- Research Charges: **8 / 8**;
- adjacent microtest: **1**;
- full synthesis: **0**;
- candidate quantities are not modeled;
- resources reset between investigations;
- no relation knowledge transfers between investigations.

## Order / blindness caveat

Precommitted order:
1. Investigation I — target-rich hybrid;
2. Investigation II — relation-rich hybrid.

The player is not told the family labels until the matched pair is complete.
Visible facts/history necessarily expose their surface differences, so this is
not architecture-blind.

Hidden formula, compatibility graph, decoy identity and intended reasoning path
remain blind.

# Investigation I — target-rich hybrid

Player-facing target: **Реагент равновесия**.

## Candidate field

### Powders
- P1 **Пыльцевой порошок** — {Растение}
- P2 **Пепельный порошок** — {Труп}
- P3 **Каменный порошок** — {Минерал}

### Liquids
- L1 **Зелёный раствор** — {Растение}
- L2 **Мутный раствор** — {Труп}
- L3 **Кристальный раствор** — {Минерал}

### Essences
- E1 **Светлая эссенция** — {Растение}
- E2 **Сухая эссенция** — {Труп}
- E3 **Каменная эссенция** — {Минерал}

## Target-specific facts

Player-visible:
1. **Минерал встречается ровно в одном из трёх компонентов.**
2. **Признак Труп встречается ровно в одном из трёх компонентов.**

## Prior laboratory knowledge

This is the complete prior-relation set internal to this field:
- P2 Пепельный порошок + L3 Кристальный раствор -> **СТАБИЛЬНО**.

No other pair relation is known at start.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> STABLE
- P2 + L3 -> STABLE
- P3 + L1 -> STABLE
- P3 + L2 -> INCOMPATIBLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> STABLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> INCOMPATIBLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> STABLE

## Hidden target formula

**P3 Каменный порошок + L1 Зелёный раствор + E2 Сухая эссенция**

## Designed compatible non-target chain

**P2 Пепельный порошок + L3 Кристальный раствор + E1 Светлая эссенция**

Facts:
- P2 + L3 is pre-known STABLE;
- L3 + E1 is hidden STABLE;
- the triple satisfies both target-specific facts;
- full synthesis is compatible but non-target.

## Target-fact-consistent triples

Facilitator-only:
- P1 + L2 + E3;
- P1 + L3 + E2;
- P2 + L1 + E3;
- P2 + L3 + E1 — compatible non-target;
- P3 + L1 + E2 — TARGET;
- P3 + L2 + E1.

Do not enumerate this set to the player.

Complete compatibility leaves exactly the designed decoy and target among these
six.

## Expected-but-not-forced shape

The two target facts carve the raw 27-triple field to six target-consistent
triples before any new experiment.

The one old stable relation gives one immediate visible anchor. Applying both
target facts to that anchor identifies E1 as its only target-consistent
continuation.

The player may follow that anchor, choose another branch, or synthesize directly.
Do not recommend a path.

# Investigation II — relation-rich hybrid

Player-facing target: **Реагент сосредоточения**.

## Candidate field

### Powders
- P1 **Волокнистый порошок** — {Растение}
- P2 **Тёмный порошок** — {Труп}
- P3 **Кристаллический порошок** — {Минерал}

### Liquids
- L1 **Травяной раствор** — {Растение}
- L2 **Серебристый раствор** — {Минерал}
- L3 **Бледный раствор** — {Насекомое}

### Essences
- E1 **Сухая эссенция** — {Растение}
- E2 **Тёмная эссенция** — {Труп}
- E3 **Кристальная эссенция** — {Минерал}

## Target-specific fact

Player-visible:
- **Минерал встречается ровно в одном из трёх компонентов.**

## Prior laboratory knowledge

This is the complete prior-relation set internal to this field:
- P1 Волокнистый порошок + L2 Серебристый раствор -> **СТАБИЛЬНО**;
- P3 Кристаллический порошок + L3 Бледный раствор -> **СТАБИЛЬНО**;
- L2 Серебристый раствор + E1 Сухая эссенция -> **НЕСОВМЕСТИМО**.

No other pair relation is known at start.

## Complete hidden compatibility table

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

## Hidden target formula

**P3 Кристаллический порошок + L3 Бледный раствор + E1 Сухая эссенция**

## Designed compatible non-target chain

**P1 Волокнистый порошок + L2 Серебристый раствор + E2 Тёмная эссенция**

Facts:
- P1 + L2 is pre-known STABLE;
- L2 + E1 is pre-known INCOMPATIBLE;
- E3 would add a second Mineral and violate the target fact;
- therefore E2 is the only target-consistent continuation of the P1+L2 anchor;
- L2 + E2 is hidden STABLE;
- full synthesis is compatible but non-target.

## Second visible stable anchor

P3 + L3 is pre-known STABLE.

Because P3 already carries the single allowed Mineral:
- E3 is target-inconsistent;
- E1 and E2 remain target-consistent;
- L3 + E1 is hidden STABLE (TARGET);
- L3 + E2 is hidden INCOMPATIBLE.

## Target-fact-consistent full compatible chains

Facilitator-only:
- P1 + L2 + E2 — compatible non-target;
- P3 + L3 + E1 — TARGET.

Do not enumerate them to the player.

## Expected-but-not-forced shape

The opening presents two visible stable anchors rather than requiring the player
to discover structure from scratch.

One anchor is almost completed by the combination of target fact + one known
incompatibility; the other remains a two-way continuation.

The player may follow either anchor or ignore them. Do not recommend a path.

# Evaluation protocol

Do not ask for comparative evaluation until both investigations are complete.

During each investigation record:
- whether the player can articulate a promising line before the first new test;
- meaningful microtest count;
- full synthesis count;
- whether the player feels they are extending existing structure versus
  cleaning up a search space;
- journal scan burden;
- any point where a clue feels like bookkeeping rather than reasoning;
- any point where the starting state feels over-solved.

After both cases ask:
- which opening felt more like a partially completed sculpture;
- which gave better immediate "hooks";
- whether two target facts felt richer or merely like more filtering;
- whether three prior relation records felt useful or cluttered;
- whether either package was too close to revealing the answer;
- approximate 1-5 rating for each;
- preferred direction for the next iteration.

Possible dispositions:
- **TARGET-RICH RETAIN**;
- **RELATION-RICH RETAIN**;
- **BOTH RETAIN / MIX**;
- **BOTH INSUFFICIENT** -> reopen new structural-clue family.

# Starting checkpoint

- active prototype: **25**;
- matched case: **Investigation I**;
- Research Charges: **8 / 8**;
- prior journal contains exactly one relation: P2 + L3 -> STABLE;
- no new actions;
- no synthesis exclusions;
- awaiting the player's first action.


## Live checkpoint 1 — Investigation I

Player action:
- microtest L3 + E1.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Journal now contains:
- prior: P2 + L3 -> STABLE;
- new: L3 + E1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 2 — Investigation I

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
- Research Charges remaining: **7 / 8**;
- full synthesis attempts in Investigation I: 1;
- compatible non-target syntheses: 1.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 3 — Investigation I

Player attempted microtest:
- P2 + L3.

Protocol handling:
- this relation is already present in the prior journal as **STABLE**;
- no duplicate experiment is performed;
- no Research Charge is consumed.

Resources remain:
- Research Charges: **7 / 8**.

Journal remains unchanged.

UX evidence:
- repeat-test interception remains relevant; already-known relation should be surfaced explicitly at selection time.

Current interaction point:
- awaiting player's next action.


## Live checkpoint 4 — Investigation I

Player action:
- microtest P1 + L2. (User utterance transcribed as “B1 L2”; interpreted as P1 L2 from current slot notation.)

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **6 / 8**.

Journal now contains:
- P2 + L3 -> STABLE;
- L3 + E1 -> STABLE;
- P2 + L3 + E1 -> NOT the current target;
- P1 + L2 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 5 — Investigation I

Player action:
- microtest P1 + L3.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **5 / 8**.

Journal now contains:
- P2 + L3 -> STABLE;
- L3 + E1 -> STABLE;
- P2 + L3 + E1 -> NOT the current target;
- P1 + L2 -> INCOMPATIBLE;
- P1 + L3 -> INCOMPATIBLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 6 — Investigation I

Player action:
- microtest P3 + L1.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **4 / 8**.

Journal now contains:
- P2 + L3 -> STABLE;
- L3 + E1 -> STABLE;
- P2 + L3 + E1 -> NOT the current target;
- P1 + L2 -> INCOMPATIBLE;
- P1 + L3 -> INCOMPATIBLE;
- P3 + L1 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live completion — Investigation I

Player action:
- full synthesis P3 + L1 + E2.

Deterministic outcome:
- **TARGET EFFECT OBTAINED**.

Investigation I is solved.

Resources:
- Research Charges used: 4 / 8;
- Research Charges remaining: **4 / 8**;
- full synthesis attempts: 2;
- compatible non-target syntheses: 1;
- successful target syntheses: 1.

Observed path:
1. Start with two target facts plus prior P2+L3 STABLE.
2. L3+E1 -> STABLE.
3. P2+L3+E1 -> compatible non-target.
4. Attempted repeat P2+L3 -> intercepted, no charge.
5. P1+L2 -> INCOMPATIBLE.
6. P1+L3 -> INCOMPATIBLE.
7. P3+L1 -> STABLE.
8. P3+L1+E2 -> TARGET.

Matched-pair transition:
- activate Investigation II;
- reset Research Charges to **8 / 8**;
- do not transfer relation knowledge from Investigation I;
- Investigation II starts with exactly its precommitted three prior relations and one target-specific fact.

No comparative evaluation yet.


## Live checkpoint 7 — Investigation II

Player action:
- microtest L2 + E2.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Investigation II journal now contains:
- prior: P1 + L2 -> STABLE;
- prior: P3 + L3 -> STABLE;
- prior: L2 + E1 -> INCOMPATIBLE;
- new: L2 + E2 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 8 — Investigation II

Player action:
- full synthesis P1 + L2 + E2.

Deterministic outcome:
- both adjacent links are **STABLE**;
- **TARGET EFFECT ABSENT**.

Journal retains:
- P1 + L2 -> STABLE;
- L2 + E2 -> STABLE.

Triple-level exclusion added:
- P1 + L2 + E2 -> NOT the recipe for the current target.

Resources:
- Research Charges remaining: **7 / 8**;
- full synthesis attempts in Investigation II: 1;
- compatible non-target syntheses: 1.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.
