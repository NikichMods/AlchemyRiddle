# Prototype 27 — Bridge topology and clue variety

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `ce1d9b40d5ff1932b46f13e2166523113298ba10`;
- research branch: `research/prototype-27-bridge-topology`;
- accepted three-slot core: Adaptive Knowledge-Aware;
- current cognitive model: prior STABLE relations provide constructive scaffold; target/reagent properties constrain continuations; newly discovered INCOMPATIBLE relations close active branches;
- production implementation remains **BLOCKED**.

## Research question

Prototype 26 retained stable prior relations as the primary scaffold but exposed a construction bias: most blind cases began from a Powder+Liquid anchor and searched forward for an Essence.

Question:

> Does the "unfinished bridge" model remain legible and enjoyable when bridge orientation and topology vary, while keeping information density approximately constant?

Secondary question:
> Can more varied weak target-property statements (absence + exact count + non-oracular slot-local constraint) enrich the tag layer without increasing cognitive burden materially?

## Solution-space checkpoint

Goal:
- preserve the low-working-memory constructive scaffold;
- avoid turning every investigation into the same `P+L -> find E` routine;
- keep target clues complementary rather than dominant;
- do not pre-solve the target at the opening.

Useful topology families considered:

1. **Mirrored anchors** — known Liquid+Essence relations; player searches backward for Powder.
2. **Mixed orientation** — one known Powder+Liquid anchor and one known Liquid+Essence anchor coexist.
3. **Pre-completed chain** — both adjacent stable relations of a complete chain are already known at start.
4. **Larger fork/star graph** — several anchors share one node or form a denser network.

Choice:
- compare (1) and (2) first;
- reject (3) for this test because it is too close to presenting a finished hypothesis rather than an unfinished bridge;
- defer (4) until the simpler orientation question is proved, because it adds topology density and presentation burden simultaneously.

## Research-method checkpoint

Exact uncertainty:
- player experience, orientation symmetry, interruption-resilience, and topology repetition risk.

Existing path:
- no missing Graveyard Keeper host/runtime fact is involved;
- accepted real-corpus tag/compatibility work already proves the underlying information sources are available;
- Prototype 25/26 already establish the relevant interaction semantics and presentation envelope.

Method:
- matched synthetic blind paper prototype is the least-complex adequate test;
- no new runtime probe, quantitative harness, or production source mutation is justified.

## Shared controls

Both investigations:
- 3x3x3 candidate field;
- three target-property constraints;
- exactly two prior **STABLE** adjacent relations;
- zero prior INCOMPATIBLE relations;
- multi-property reagent cards where useful;
- 8 Research Charges;
- adjacent microtest costs 1;
- full synthesis costs 0;
- no knowledge transfer between investigations;
- same three-column presentation and prior/new journal distinction.

The player is not told topology-family labels until matched evaluation.

## Universal rules

Recipe:
- Powder + Liquid + Essence.

Legal microtests:
- Powder + Liquid;
- Liquid + Essence;
- Powder + Essence cannot be directly tested.

Microtest outcome:
- **СТАБИЛЬНО** or **НЕСОВМЕСТИМО**.

A viable complete chain requires both adjacent relations to be stable, but that does not prove the target.

Full synthesis outcomes:
- target -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- compatible non-target -> **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**;
- other non-target -> **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; ПОЛНАЯ УСТОЙЧИВАЯ ЦЕПОЧКА НЕ ПОДТВЕРЖДЕНА.**

Synthesis excludes only the exact triple and does not silently add unknown pair records.

# Investigation I — mirrored bridges

Player-facing target: **Реагент отражения**.

## Candidate field

### Powders
- P1 **Зелёный порошок** — {Растение}
- P2 **Белёсый порошок** — {Труп, Минерал}
- P3 **Искристый порошок** — {Минерал, Насекомое}

### Liquids
- L1 **Вязкий раствор** — {Растение, Слизь}
- L2 **Каменный раствор** — {Минерал}
- L3 **Мрачный раствор** — {Труп}

### Essences
- E1 **Светлая эссенция** — {Растение}
- E2 **Сухая эссенция** — {Труп}
- E3 **Летучая эссенция** — {Насекомое}

## Target-property constraints

Player-visible:
1. **Слизь не встречается ни в одном компоненте.**
2. **Труп встречается ровно в одном компоненте.**
3. **Порошок не относится к Трупу.**

These are intentionally different clue forms:
- global absence;
- exact total count;
- slot-local absence.

Combined target-consistent triples (facilitator only):
- P1 + L2 + E2;
- P1 + L3 + E1;
- P1 + L3 + E3;
- P3 + L2 + E2;
- P3 + L3 + E1;
- P3 + L3 + E3.

Do not enumerate this set to the player.

## Prior laboratory knowledge

Exactly two prior STABLE relations, both mirrored orientation:
- L2 + E2 -> **STABLE**;
- L3 + E1 -> **STABLE**.

No prior incompatibilities.

For each visible bridge, target constraints leave two plausible Powder continuations:
- L2+E2 -> P1 or P3;
- L3+E1 -> P1 or P3.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE
- P2 + L3 -> STABLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> INCOMPATIBLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> STABLE
- L3 + E3 -> INCOMPATIBLE

## Hidden target

**P3 + L3 + E1**

## Designed compatible non-target

**P1 + L2 + E2**

Among target-consistent triples:
- P1+L2+E2 -> compatible non-target;
- P1+L3+E1 -> blocked by P1+L3;
- P1+L3+E3 -> blocked by P1+L3 and L3+E3;
- P3+L2+E2 -> blocked by P3+L2;
- P3+L3+E1 -> TARGET;
- P3+L3+E3 -> blocked by L3+E3.

## Intended-but-not-forced shape

Both starting bridges are Liquid+Essence.
The player must reason "backward" toward Powder rather than always extending Powder+Liquid toward Essence.

Neither bridge has a unique Powder continuation from tags alone:
- both P1 and P3 remain plausible until compatibility is tested.

This deliberately avoids turning reversed orientation into a trivial slot lookup.

# Investigation II — mixed bridge orientations

Player-facing target: **Реагент сопряжения**.

## Candidate field

### Powders
- P1 **Пепельный порошок** — {Труп, Насекомое}
- P2 **Липкий порошок** — {Слизь}
- P3 **Каменный порошок** — {Минерал}

### Liquids
- L1 **Мрачный раствор** — {Труп}
- L2 **Вязкий раствор** — {Насекомое, Слизь}
- L3 **Кристальный раствор** — {Минерал}

### Essences
- E1 **Густая эссенция** — {Слизь}
- E2 **Тягучая эссенция** — {Слизь}
- E3 **Зелёная эссенция** — {Растение}

## Target-property constraints

Player-visible:
1. **Минерал встречается ровно в одном компоненте.**
2. **Растение не встречается ни в одном компоненте.**
3. **Раствор не относится к Трупу.**

Again the clue forms are:
- exact total count;
- global absence;
- slot-local absence.

Combined target-consistent triples (facilitator only):
- P1 + L3 + E1;
- P1 + L3 + E2;
- P2 + L3 + E1;
- P2 + L3 + E2;
- P3 + L2 + E1;
- P3 + L2 + E2.

Do not enumerate this set to the player.

## Prior laboratory knowledge

Exactly two prior STABLE relations with mixed orientation:
- P3 + L2 -> **STABLE**;
- L3 + E1 -> **STABLE**.

No prior incompatibilities.

Target constraints leave two continuations on each bridge:
- P3+L2 -> E1 or E2;
- L3+E1 -> P1 or P2.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> STABLE
- P2 + L3 -> STABLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> INCOMPATIBLE

## Hidden target

**P2 + L3 + E1**

## Designed compatible non-target

**P3 + L2 + E2**

Among target-consistent triples:
- P1+L3+E1 -> blocked by P1+L3;
- P1+L3+E2 -> blocked by P1+L3 and L3+E2;
- P2+L3+E1 -> TARGET;
- P2+L3+E2 -> blocked by L3+E2;
- P3+L2+E1 -> blocked by L2+E1;
- P3+L2+E2 -> compatible non-target.

## Intended-but-not-forced shape

The opening contains:
- one Powder+Liquid bridge that invites forward continuation to Essence;
- one Liquid+Essence bridge that invites backward continuation to Powder.

Both have two target-consistent continuation candidates.
The goal is to test whether mixed orientation feels richer and less procedural while remaining as easy to parse as the mirrored case.

# Evaluation protocol

Do not ask comparative evaluation until both investigations are complete.

During play record:
- which bridge the player notices first and why;
- whether backward completion from L+E feels as natural as forward completion from P+L;
- whether two same-orientation bridges feel repetitive or coherent;
- whether mixed orientation feels richer or merely less tidy;
- whether the three varied target constraints are easy to use;
- whether the slot-local negative clue is useful, forgettable, or too direct;
- whether the player can resume from the journal after digressions;
- microtests and syntheses;
- any transition into enumeration.

After both ask:
- did mirrored L+E bridges validate orientation symmetry;
- which topology was more enjoyable/readable: mirrored or mixed;
- did mixed orientation reduce repetition without raising working-memory cost;
- did varied clue forms improve the tag layer;
- did three constraints still feel comfortable;
- should future topology work proceed to denser fork/star networks, or is simple mixed orientation already enough;
- approximate rating / preferred direction.

Possible dispositions:
- **ORIENTATION SYMMETRY CONFIRMED; MIXED RETAIN**
- **ORIENTATION SYMMETRY CONFIRMED; MIRRORED CLEANER**
- **REVERSE ORIENTATION WEAK**
- **MIXED TOO MESSY**
- **BOTH GOOD; TEST DENSER NETWORK**
- **CLUE-VARIETY REVISE**

# Starting checkpoint

- active prototype: **27**;
- active case: **Investigation I**;
- Research Charges: **8 / 8**;
- prior journal:
  - L2 + E2 -> STABLE;
  - L3 + E1 -> STABLE;
- no prior incompatibilities;
- no new actions;
- no synthesis exclusions;
- awaiting first player action.


## Live checkpoint 1 — Investigation I

Player UX observations before acting:
- the varied target-property clue set immediately feels substantially more engaging than repeated exact-count clues;
- the player naturally begins from the incomplete stable bridges and uses tags to filter continuations;
- this starts reasoning quickly without unacceptable working-memory load;
- the slot-local negative clue is mechanically clear and immediately useful, but its literal wording (“Powder does not belong to Corpse”) feels awkward and should later be rephrased more naturally without changing semantics;
- the player explicitly reports strong positive affect before any experiment is made.

Player reasoning:
- starts from known L2+E2 STABLE;
- observes L2 supplies Mineral and E2 supplies Corpse;
- notes the target already satisfies the one-Corpse condition through E2;
- therefore Powder must not be Corpse, matching the slot-local constraint;
- chooses P1+L2 as a plausible backward completion.

Player action:
- microtest P1 + L2.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Journal now contains:
- prior: L2 + E2 -> STABLE;
- prior: L3 + E1 -> STABLE;
- new: P1 + L2 -> STABLE.

No facilitator deduction supplied beyond confirming the player-stated reasoning.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 2 — Investigation I

Player action:
- full synthesis P1 + L2 + E2. (Player's spoken reference to “P2+L2 stable” is treated as a slip; the established new relation is P1+L2 STABLE and the requested triple is explicit.)

Deterministic outcome:
- both adjacent links are **STABLE**;
- **TARGET EFFECT ABSENT**.

Triple exclusion:
- P1 + L2 + E2 is not the current target recipe.

Resources:
- Research Charges remaining: **7 / 8**;
- full synthesis attempts in Investigation I: 1;
- compatible non-target syntheses: 1.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 3 — Investigation I

Player design observation before acting:
- the player notes a possible meta-pattern: the first obvious well-formed hypothesis can start to feel predictably wrong if prototypes repeatedly use it as a decoy;
- future cases should avoid making “first elegant hypothesis = designed false branch” into a learnable facilitator pattern.

Player reasoning:
- P2 is excluded for the current L2+E2 bridge because E2 already supplies the one allowed Corpse and P2 also has Corpse;
- after P1+L2+E2 proved to be a compatible non-target, the player tests the remaining plausible Powder continuation P3+L2.

Player action:
- microtest P3 + L2.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **6 / 8**.

Journal now contains:
- prior: L2 + E2 -> STABLE;
- prior: L3 + E1 -> STABLE;
- new: P1 + L2 -> STABLE;
- P1 + L2 + E2 -> NOT the current target;
- new: P3 + L2 -> INCOMPATIBLE.

No facilitator deduction supplied beyond confirming the player-stated branch logic.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 4 — Investigation I

Player reasoning:
- moves from the exhausted L2+E2 bridge to the second prior stable bridge L3+E1;
- L3 supplies Corpse and E1 supplies Plant;
- Slime can be ignored for Powder selection because no Powder candidate carries Slime;
- P2 is excluded because the target allows Corpse exactly once and L3 already supplies it;
- chooses P1+L3 as the first backward-completion test.

Player action:
- microtest P1 + L3.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **5 / 8**.

Journal now contains:
- prior: L2 + E2 -> STABLE;
- prior: L3 + E1 -> STABLE;
- new: P1 + L2 -> STABLE;
- P1 + L2 + E2 -> NOT the current target;
- new: P3 + L2 -> INCOMPATIBLE;
- new: P1 + L3 -> INCOMPATIBLE.

No facilitator deduction supplied beyond confirming the player-stated tag filtering.

Current interaction point:
- awaiting player's inference / next action.


## Live checkpoint 5 — Investigation I

Player action:
- microtest P3 + L3.

Raw outcome:
- **STABLE**.

Resources:
- Research Charges remaining: **4 / 8**.

Journal now contains:
- prior: L2 + E2 -> STABLE;
- prior: L3 + E1 -> STABLE;
- new: P1 + L2 -> STABLE;
- P1 + L2 + E2 -> NOT the current target;
- new: P3 + L2 -> INCOMPATIBLE;
- new: P1 + L3 -> INCOMPATIBLE;
- new: P3 + L3 -> STABLE.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.


## Live completion — Investigation I

Player action:
- full synthesis P3 + L3 + E1.

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
1. Start with two prior L+E stable bridges and three varied target constraints.
2. P1+L2 -> STABLE.
3. P1+L2+E2 -> compatible non-target.
4. P3+L2 -> INCOMPATIBLE, closing the first bridge.
5. Move to second bridge L3+E1.
6. P1+L3 -> INCOMPATIBLE.
7. P3+L3 -> STABLE.
8. P3+L3+E1 -> TARGET.

Experiential signal:
- reverse-orientation bridge completion was used naturally; player repeatedly treated L+E pairs as unfinished structures to be completed backward with a Powder.
- varied clue forms were positively received before any action and used directly during branch filtering.

Matched-pair transition:
- activate Investigation II;
- reset Research Charges to **8 / 8**;
- do not transfer relation knowledge from Investigation I;
- Investigation II starts with exactly its two precommitted stable anchors and three target-property constraints.

No comparative evaluation yet.


## Live checkpoint 6 — Investigation II

Player design observations before acting:
- a target-property clue that never affects any branch feels like dead decorative information; weak clues are acceptable, but ideally each surfaced clue should matter at least once during the intended reasoning path;
- strong stable bridges need not always contain the target. For medium/high difficulty, a promising topology is: several visible bridges are exhausted logically, and that process leaves one small non-bridge residual branch as the answer, avoiding both “all answers come from bridges” meta-learning and post-bridge brute force;
- simple slot-exclusion clues can become dull if they only erase one candidate; they may be more useful in larger fields or when combined with richer logic;
- conditional/composite target clues are promising, e.g. constraints of the form “property X is forbidden in slot Y if property Z is present elsewhere”; exact syntax is not accepted, but the general class is strongly interesting;
- diversity should come from different logical roles, not arbitrary noise: global counts/absence, slot-local constraints, conditional dependencies, bridge topology, and residual deduction can be mixed carefully;
- the player reports that the underlying grammar now feels stable enough that ideation has shifted from “how do we make this work?” to “how do we make this richer?”, a positive maturity signal;
- future external validation idea: a standalone web demo/puzzle could collect anonymized path statistics from multiple players to see whether “follow visible stable bridges first” is a general strategy or player-specific.

Player reasoning in Investigation II:
- target constraints immediately exclude L1 because the Liquid must not have Corpse;
- from prior P3+L2 STABLE, P3 supplies the one allowed Mineral;
- E3 is excluded because Plant is forbidden;
- player intends to test the bridge continuation with E1.

Protocol correction:
- player verbally said “P2, E1”, but Powder+Essence cannot be directly tested and the stated reasoning clearly refers to continuing P3+L2 with E1;
- interpret intended legal microtest as **L2 + E1**.

Player action:
- microtest L2 + E1.

Raw outcome:
- **INCOMPATIBLE**.

Resources:
- Research Charges remaining: **7 / 8**.

Journal now contains:
- prior: P3 + L2 -> STABLE;
- prior: L3 + E1 -> STABLE;
- new: L2 + E1 -> INCOMPATIBLE.

No facilitator deduction supplied beyond clarifying the legal adjacent pair implied by the player's reasoning.

Current interaction point:
- awaiting player's inference / next action.
