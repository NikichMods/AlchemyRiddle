# Prototype 22 — Blind architecture A/B facilitator state

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first choice**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `53f63173129c2cf7fe0bf1c42be01f106c5378bf`;
- active research branch: `research/prototype-22-blind-ab`;
- production architecture remains **BLOCKED**.

## Purpose

Blind player-facing comparison of the two surviving three-slot architectures:

- fixed tag-centric baseline;
- adaptive knowledge-aware candidate.

The question is experiential rather than structural:

> Does replacing part of the target-specific clue burden with honest reusable
> prior compatibility knowledge feel like accumulated alchemical expertise, or
> like authorial/meta guidance?

The quantitative adaptive screen already established structural robustness.
This prototype does not re-test corpus coverage.

## Research-method checkpoint

Exact uncertainty:
- player ownership of the deduction;
- whether old compatibility observations feel like accumulated knowledge rather
  than breadcrumbs;
- whether the next experiment is chosen for an articulated reason;
- whether the adaptive reduction in new work feels good rather than suspicious.

Existing path:
- accepted quantitative screen closes the structural question;
- Prototypes 20R/21 establish the no-anchor and structured-start experiential
  baselines.

Method:
- a blind paper A/B is the lowest-assumption test because the remaining
  uncertainty is cognitive/player-facing;
- no new runtime probe, host research, production code or CI artifact is needed.

## Matching / control design

The two cases are deliberately **structurally isomorphic**:
- same 3x3x3 size;
- same abstract ingredient-property incidence under a permutation of labels;
- same hidden compatibility graph under a permutation of reagent identities;
- same answer position in the abstract graph, but different displayed reagent
  positions;
- same microtest/synthesis rules;
- same resource budget;
- different fictional display names to prevent direct answer carryover.

Only the intended architecture-level starting-information difference changes.

This is synthetic/anonymized player-experience evidence grounded in the accepted
real-corpus structural envelope. It is not new corpus-coverage evidence.

## Hidden A/B order

Order is fixed mechanically from the base-main SHA rather than facilitator
preference.

Rule:
- parse the first byte of the base SHA;
- even -> fixed first;
- odd -> adaptive first.

For `53...`, `0x53 = 83`, which is odd.

Therefore:
- **Investigation I = adaptive knowledge-aware**;
- **Investigation II = fixed tag-centric baseline**.

Do not reveal this mapping until both investigations reach their evaluation
point.

## Universal player-visible law

A valid three-component formula is prepared in two adjacent stages:

1. Powder + Liquid must be **STABLE**.
2. Liquid + Essence must be **STABLE**.

A microtest checks one concrete adjacent pair and returns:
- **СТАБИЛЬНО**;
- **НЕСОВМЕСТИМО**.

Compatibility is reusable empirical knowledge about that pair.

Powder + Essence is never tested directly.

Both stable adjacent relations are necessary for a formula, but compatibility
alone is not sufficient to prove that a compatible triple is the target recipe.

## Common resources and action rules

For both investigations:
- start with **4 Research Charges**;
- each microtest costs **1 Research Charge**;
- full synthesis costs **0 Research Charges**;
- synthesis may be attempted at any time;
- no replenishment occurs inside the paper prototype;
- candidate material quantities are otherwise not modeled.

Synthesis outcome:
- exact hidden formula -> **SUCCESS**;
- any other triple -> **FAILURE**.

A failed synthesis does not retroactively reveal untested pair outcomes.

## Common facilitator rules

At every decision point:
- show all 3 candidates per slot with their displayed properties;
- show target facts;
- show all old compatibility observations that the case legitimately contains;
- show all new raw observations;
- show remaining Research Charges;
- show legal actions.

Do not:
- enumerate target-compatible triples;
- enumerate first-stage branches;
- show a compatibility matrix;
- recommend a pair;
- identify which old relation is useful;
- derive a fresh player deduction before the player states it;
- reveal the A/B architecture mapping before debrief.

---

# Abstract master structure

This section exists only to prove matching.

## Master ingredient properties

- P1 = {Plant, Corpse}
- P2 = {Insect}
- P3 = {Insect, Corpse}
- L1 = {Plant, Insect}
- L2 = {Mineral, Corpse}
- L3 = {Plant, Mineral}
- E1 = {Mineral, Corpse}
- E2 = {Corpse}
- E3 = {Insect}

Master hidden answer:
- P1 + L1 + E2

Master target facts used by the fixed baseline:
- Insect = 1;
- Corpse = 2.

Structural checks:
- Insect=1 alone -> 7 Powder-Liquid branches / 12 triples;
- Corpse=2 alone -> 7 Powder-Liquid branches / 12 triples;
- both facts -> 4 Powder-Liquid branches / 7 triples.

Thus both fixed clues are individually weak and become useful through
intersection.

## Master compatibility table

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
- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> INCOMPATIBLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> STABLE

Under both fixed target facts, complete compatibility leaves exactly two
compatible target-fact-consistent chains:
- the hidden answer;
- one stable decoy chain.

This intentionally permits the accepted final 1-2 justified-hypothesis state
rather than making compatibility identical to the recipe table.

---

# Investigation I — hidden adaptive case

**Do not label as adaptive to the player.**

## Display permutation

Master reagent identity -> displayed identity:
- P1 -> P2
- P2 -> P3
- P3 -> P1
- L1 -> L3
- L2 -> L1
- L3 -> L2
- E1 -> E2
- E2 -> E1
- E3 -> E3

Master property -> displayed property:
- Plant -> Минерал
- Insect -> Растение
- Mineral -> Труп
- Corpse -> Насекомое

## Candidate pool

Powders:
- P1 Серебристый порошок — {Растение, Насекомое}
- P2 Тусклый порошок — {Минерал, Насекомое}
- P3 Алый порошок — {Растение}

Liquids:
- L1 Мутный раствор — {Труп, Насекомое}
- L2 Янтарный раствор — {Минерал, Труп}
- L3 Тёплый раствор — {Минерал, Растение}

Essences:
- E1 Тихая эссенция — {Насекомое}
- E2 Холодная эссенция — {Труп, Насекомое}
- E3 Искристая эссенция — {Растение}

## Target-specific research

Player-visible:
- **Растение appears in exactly 1 component.**

Do not reveal the matched second master fact in this case.

This one fact is individually weak:
- 7 first-stage Powder-Liquid branches;
- 12 complete triples.

## Prior empirical knowledge

The complete set of already-known adjacent relations internal to this field is:

- P2 Тусклый порошок + L3 Тёплый раствор -> **СТАБИЛЬНО**
- P1 Серебристый порошок + L2 Янтарный раствор -> **СТАБИЛЬНО**
- P3 Алый порошок + L2 Янтарный раствор -> **НЕСОВМЕСТИМО**
- L1 Мутный раствор + E1 Тихая эссенция -> **НЕСОВМЕСТИМО**

These four records are the whole internal prior-knowledge set for the selected
surface. Do not hide or add a relation based on answer usefulness.

Interpretation:
- exactly one hidden-answer edge is already known stable;
- a second live stable Powder-Liquid relation is a decoy/alternative anchor;
- two known incompatibilities provide honest pruning;
- no complete adjacent chain is pre-known.

After applying the known incompatibilities to the one-fact field:
- 6 Powder-Liquid branches / 8 triples remain structurally live.

Under the complete hidden compatibility graph, the one-fact field contains
three compatible chains, so the displayed old stable anchors are not the only
structurally viable compatibility routes.

## Hidden compatibility table

Powder-Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> STABLE
- P2 + L3 -> STABLE
- P3 + L1 -> STABLE
- P3 + L2 -> INCOMPATIBLE
- P3 + L3 -> STABLE

Liquid-Essence:
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> STABLE

## Hidden valid answer

- P2 Тусклый порошок
- L3 Тёплый раствор
- E1 Тихая эссенция

Exact synthesis:
- P2 + L3 + E1 -> SUCCESS
- every other triple -> FAILURE

## Starting resources

- Research Charges: 4 / 4
- completed new actions: none

---

# Investigation II — hidden fixed-baseline case

**Do not label as fixed/baseline to the player.**

## Display permutation

Master reagent identity -> displayed identity:
- P1 -> P3
- P2 -> P1
- P3 -> P2
- L1 -> L2
- L2 -> L3
- L3 -> L1
- E1 -> E3
- E2 -> E2
- E3 -> E1

Master property -> displayed property:
- Plant -> Растение
- Insect -> Минерал
- Mineral -> Насекомое
- Corpse -> Труп

## Candidate pool

Powders:
- P1 Серый порошок — {Минерал}
- P2 Медный порошок — {Минерал, Труп}
- P3 Лунный порошок — {Растение, Труп}

Liquids:
- L1 Смоляной раствор — {Растение, Насекомое}
- L2 Золотистый раствор — {Растение, Минерал}
- L3 Молочный раствор — {Насекомое, Труп}

Essences:
- E1 Звонкая эссенция — {Минерал}
- E2 Тёмная эссенция — {Труп}
- E3 Стеклянная эссенция — {Насекомое, Труп}

## Target-specific research

Player-visible:
- **Минерал appears in exactly 1 component.**
- **Труп appears in exactly 2 components.**

Structural checks:
- Минерал=1 alone -> 7 Powder-Liquid branches / 12 triples;
- Труп=2 alone -> 7 Powder-Liquid branches / 12 triples;
- both -> 4 Powder-Liquid branches / 7 triples.

## Prior empirical knowledge

No previously learned adjacent relation inside this working field.

The player may know chemistry elsewhere, but none of those old relations has
both ingredients present on this selected surface.

## Hidden compatibility table

Powder-Liquid:
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> STABLE
- P3 + L1 -> STABLE
- P3 + L2 -> STABLE
- P3 + L3 -> INCOMPATIBLE

Liquid-Essence:
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> STABLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> INCOMPATIBLE

## Hidden valid answer

- P3 Лунный порошок
- L2 Золотистый раствор
- E2 Тёмная эссенция

Exact synthesis:
- P3 + L2 + E2 -> SUCCESS
- every other triple -> FAILURE

## Starting resources

- Research Charges: 4 / 4
- completed new actions: none

---

# Pre-play leak / confound audit

Passed before activation:

1. **Same resource signal**
   - both cases start at 4 Research Charges;
   - synthesis cost is identical.

2. **Same interface/action grammar**
   - same 3x3x3 candidate presentation;
   - same property notation;
   - same microtest legality;
   - same journal semantics.

3. **No answer in naming**
   - fictional names are atmospheric labels only;
   - no name is intended to encode compatibility or target membership.

4. **No target-position pattern**
   - displayed hidden answers occupy different P/L/E indices.

5. **No exact answer carryover**
   - reagent identities and property labels are permuted between cases.

6. **Intrinsic topology controlled**
   - both cases are isomorphic copies of the same hidden property and
     compatibility model.

7. **Intentional architecture difference only**
   - fixed case gets two weak target facts and no internal old relations;
   - adaptive case gets one weak target fact plus every old relation internal to
     the field.

8. **Adaptive neutrality**
   - all four internal old relations are shown;
   - there is no answer-helpful subset selection;
   - known stable relations include both target and non-target structure;
   - no full target chain is known at start.

9. **Facilitator inference boundary**
   - after a new test, show raw result and state only;
   - wait for the player's inference before updating earned conclusions.

10. **Order bias containment**
    - case order was fixed mechanically from the base SHA;
    - if the subjective result is close/contradictory, do not over-interpret one
      pair; run a second matched pair in reverse order.

## Primary comparison questions after both cases

Before revealing architecture labels, ask the player to compare:

- what reasoning they considered genuinely their own in each case;
- whether prior relations felt like accumulated laboratory knowledge or like
  authored hints;
- whether the next experiment was chosen for an articulable reason;
- whether either case encouraged matrix completion / sequential checking;
- which case produced the stronger "I worked it out" feeling;
- whether either case was too easy, too directed, noisy, or cognitively heavy.

Mechanical observations:
- microtests used;
- failed syntheses;
- chosen branch sequence;
- whether a wrong branch was pursued;
- whether the player attempted broad matrix completion;
- whether the player explicitly relied on assumed authorial friendliness.

## Live checkpoint

Current active investigation:
- **Investigation I**;
- player-facing state activated in the current chat;
- Research Charges: 4 / 4;
- completed actions: none;
- legal next action: any adjacent microtest or any full synthesis.

Exact current interaction point:
- Investigation I panel has been presented;
- architecture identity remains hidden;
- awaiting the player's first action.



## Investigation I — live checkpoint 1

Player reasoning before the first microtest:
- explicitly noticed the 4-charge budget as potential meta-information only because
  of prior prototype experience, and judged it likely irrelevant to a first-time
  player;
- started from the known STABLE pair P2 Тусклый порошок + L3 Тёплый раствор;
- applied the target fact Растение ×1;
- observed that P2 contributes no Растение while L3 contributes one, so E3
  Искристая эссенция would add a second Растение and was rejected as a
  continuation;
- identified E1 Тихая эссенция and E2 Холодная эссенция as the two plausible
  continuations of that stable pair;
- chose to test L3 + E1 first.

Player action:
- microtest L3 Тёплый раствор + E1 Тихая эссенция.

Raw outcome:
- **СТАБИЛЬНО**.

Resources:
- Research Charges remaining: **3 / 4**.

Facilitator supplied no deduction from the fresh observation.

Current interaction point:
- awaiting the player's inference / next action.



## Investigation I — live completion

Player inference after the first microtest:
- recognized that P2 + L3 was already known STABLE and L3 + E1 had now tested
  STABLE;
- treated the resulting two-edge stable chain as sufficient confidence to
  attempt the full formula immediately;
- did not spend a second microtest on L3 + E2.

Player action:
- synthesize P2 Тусклый порошок + L3 Тёплый раствор + E1 Тихая эссенция.

Deterministic outcome:
- **SUCCESS / УСПЕХ**.

Resources:
- Research Charges used: **1 / 4**;
- Research Charges remaining: **3 / 4**;
- microtests: **1**;
- failed synthesis attempts: **0**.

Observed blind-play path:
1. Start from a pre-known stable P2 + L3 relation.
2. Apply the target fact Растение ×1 to reject E3 as a continuation.
3. Test L3 + E1 -> STABLE.
4. Immediately synthesize P2 + L3 + E1 -> SUCCESS.

Facilitator supplied no new deduction before the player's synthesis choice.

Investigation I is complete.
Architecture identity remains hidden pending completion/evaluation of Investigation II.

Production architecture remains **BLOCKED**.
