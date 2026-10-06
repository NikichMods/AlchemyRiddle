# Prototype 35 — Three-slot relation-introduction tutorial

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base main: `03dfda96686ba1031b438d9470b024df5ad80baa`.

Purpose: test the cross-arity curriculum claim that three-slot onboarding should
reuse already-familiar simple property reasoning and introduce exactly one new
reasoning concept: an empirical adjacent STABLE / INCOMPATIBLE relation.

Production remains **BLOCKED**.

## Research question

> After familiar two-slot-style property reasoning has already carved the
> candidate field down to one Powder + one Liquid and two possible Essences,
> does one purposeful adjacent relation test feel like a natural escalation
> rather than a new unrelated minigame?

## Curriculum contract under test

- arity: Powder + Liquid + Essence;
- field: 2x2x2;
- reagent cards deliberately show one property each;
- familiar logical language only:
  - one slot-local requirement;
  - one exact-count fact;
- exactly one new concept family:
  adjacent Powder-Liquid / Liquid-Essence relations can be tested and return
  **СТАБИЛЬНО** or **НЕСОВМЕСТИМО**;
- no XOR;
- no implication;
- no reverse-direction clue;
- no mixed relation orientation;
- no prior relation-history graph;
- no residual/off-bridge topology;
- no theoretical-new-identity issue;
- no resource scarcity.

## Player-visible target

**Настой ясности**

## Candidate field

### Powders
- P1 **Пыльцевой порошок** — {Растение}
- P2 **Меловой порошок** — {Минерал}

### Liquids
- L1 **Травяной раствор** — {Растение}
- L2 **Мрачный раствор** — {Труп}

### Essences
- E1 **Летучая эссенция** — {Насекомое}
- E2 **Сухая эссенция** — {Труп}

## Familiar target facts

1. **Порошок имеет признак Минерал.**
2. **Растение встречается ровно в одном из трёх компонентов.**

Literal semantics. No hidden properties.

Applying only the familiar property facts:
- Powder is fixed to P2;
- because P2 is not Plant and neither Essence is Plant, Liquid is fixed to L1;
- both E1 and E2 remain possible.

Thus the pre-relation live hypotheses are exactly:
- P2 + L1 + E1;
- P2 + L1 + E2.

Do not enumerate this pair to the player unless the player derives it.

## New tutorial rule

Only adjacent pairs can be tested:
- Powder + Liquid;
- Liquid + Essence.

Powder + Essence cannot be tested directly.

A tested adjacent pair returns:
- **СТАБИЛЬНО**, or
- **НЕСОВМЕСТИМО**.

A formula cannot contain an **НЕСОВМЕСТИМО** adjacent pair.

A STABLE pair is chemically viable but, in general, does not by itself prove
that the target formula uses it.

For this tutorial, after the player has derived P2 + L1 and two Essence
candidates remain, both L1+E1 and L1+E2 are legal useful tests.

## Hidden relation outcomes

- P2 + L1 -> STABLE
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE

Other relations are irrelevant to the intended tutorial and need not be
surfaced unless the player explicitly tests them. If an unexpected legal test
is requested, use this complete table:

Powder-Liquid:
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> INCOMPATIBLE

Liquid-Essence:
- L1 + E1 -> INCOMPATIBLE
- L1 + E2 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> INCOMPATIBLE

## Hidden answer

**P2 Меловой порошок + L1 Травяной раствор + E2 Сухая эссенция**.

## Intended-but-not-forced tutorial path

1. familiar facts identify P2 and L1;
2. E1/E2 remain;
3. the player sees why testing an L1+Essence adjacent pair is useful;
4. if L1+E1 is tested, INCOMPATIBLE eliminates E1 and leaves E2;
5. if L1+E2 is tested first, STABLE makes E2 the leading viable continuation
   but does not establish a general meta-rule that every STABLE pair is the
   target; in this deliberately bounded tutorial, the player may then submit the
   remaining formula hypothesis.

The primary evidence is not which Essence is tested first. It is whether the
player understands **why** the relation test is informative before using it.

## Resource handling

No Science/charge cost in this paper tutorial.
The economy is out of scope and must not influence first-use comprehension.

## Evaluation

Observe:
- whether the two familiar facts are immediately readable after Prototype 34;
- whether the player independently identifies P2 + L1 before relation testing;
- whether the purpose of testing L1 with an Essence is obvious;
- whether the new relation concept feels like a natural extension of the same
  investigation;
- whether 2x2x2 feels acceptably small when the opening is already structured;
- whether one new concept is enough cognitive novelty.

After resolution ask:
- did this feel like a natural next lesson after the two-slot tutorial;
- was the new STABLE/INCOMPATIBLE rule clear;
- was the case too trivial, tutorial-appropriate, or confusing;
- did the relation test feel purposeful rather than like trying combinations;
- would the player accept this as the first three-slot puzzle.

Stop after evaluation. Do not add another prototype in the same blind sequence.


## Live checkpoint 1

Player-facing comprehension before acting:
- the three-slot rules still read as clear, clean and understandable despite the
  player having seen earlier three-slot prototypes;
- the player explicitly contrasted ordinary property/XOR/implication logic with
  the adjacent STABLE/INCOMPATIBLE layer and judged the latter as comparatively
  fresh and authorial rather than a generic assembled logic-puzzle vocabulary;
- this is positive subjective design evidence, but not general-user usability
  evidence; broader onboarding legibility remains to be validated beyond the
  current experienced tester.

Player deduction before any relation test:
- fact 1 fixes Powder to **P2 Меловой порошок**;
- fact 2 then fixes Liquid to **L1 Травяной раствор**, because Plant must occur
  exactly once and neither Essence carries Plant;
- only the Essence remains unresolved.

Player independently chose **L1 + E1** as the first relation test.
This is exactly the intended purposeful-test shape: the test targets the sole
remaining uncertainty rather than scanning arbitrary pairs.

Precommitted result:
**L1 + E1 -> INCOMPATIBLE**.

No rules or hidden state changed.


## Live checkpoint 2

After receiving the precommitted result
**L1 Травяной раствор + E1 Летучая эссенция -> НЕСОВМЕСТИМО**,
the player immediately concluded:

**P2 Меловой порошок + L1 Травяной раствор + E2 Сухая эссенция**.

This matches the precommitted hidden answer.

Observed reasoning trajectory:
1. familiar property facts fixed P2;
2. the same familiar property logic fixed L1;
3. one purposeful adjacent relation test eliminated E1;
4. E2 became the unique remaining continuation.

No brute-force scanning, arbitrary pair testing, or clarification of the new
relation semantics was required.

The tutorial has now reached deterministic resolution. A final subjective
evaluation is still required before disposition is recorded.


## Final player evaluation

Disposition: **PASS — ACCEPT AS FIRST THREE-SLOT TUTORIAL SHAPE.**

Player judgement:
- the transition from the two-slot tutorial felt natural after reflection;
- the adjacent STABLE / INCOMPATIBLE rule was clear on first presentation;
- the single L1 + E1 test felt like a purposeful experiment rather than random
  trial among candidates;
- difficulty felt **right for the first three-slot puzzle**;
- the player would accept this general case as the first three-component
  AlchemyRiddle investigation.

Important UX constraint:
- the future interface must make the currently available action space explicit;
- in particular, the player should not have to remember from an earlier tutorial
  that adjacent-pair compatibility tests exist;
- when a useful adjacent test is available, the UI should make that interaction
  discoverable without auto-solving or recommending the answer;
- this is a future presentation/interaction requirement, not evidence for a
  specific production UI architecture.

Curriculum conclusion:
- two-slot onboarding can teach simple property intersection first;
- the first three-slot investigation can then reuse that exact reasoning language
  and add one new layer: adjacent empirical compatibility;
- one purposeful relation test is enough to make the escalation feel new without
  making it feel like a separate minigame.

Prototype 35 is complete.
