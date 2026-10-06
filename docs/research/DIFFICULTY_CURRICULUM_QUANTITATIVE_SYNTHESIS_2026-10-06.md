# Difficulty Curriculum Quantitative Synthesis — 2026-10-06

Status: **accepted-evidence synthesis for curriculum realizability; no new formula-level calculation; production remains BLOCKED.**

Purpose: test the working difficulty envelopes in
`DIFFICULTY_CURRICULUM_ENVELOPES_2026-10-06.md` against the already accepted
reproducible corpus screens and blind prototype evidence before commissioning a
new expensive quantitative pass.

This pass deliberately reuses accepted evidence instead of re-running the same
private corpus under a differently named wrapper. No exact vanilla recipe rows
are persisted.

## 1. Evidence reused

Two-slot:
- `TWO_SLOT_TAG_CONSTRAINT_SCREEN_2026-10-06.md`
- helper: `research/TagModelScreen/two_slot_tag_constraint_screen.py`
- accepted baseline: 24 variants / 18 outputs / 15 first-slot participants /
  9 second-slot participants / 23 of 24 variants with a Hamming-1 neighbor.

Three-slot:
- `PROGRESSION_VARIABLE_FIELD_SCREEN_2026-10-05.md`
- `ADAPTIVE_ARCHITECTURE_SCREEN_2026-10-05.md`
- helpers:
  `research/TagModelScreen/progression_variable_field_screen.py` and
  `research/TagModelScreen/adaptive_architecture_screen.py`
- accepted baseline: 19 ordinary variants / 16 outputs / 10 x 9 x 9 /
  19 Powder-Liquid stable edges / 18 Liquid-Essence stable edges /
  47 two-edge-compatible chains.

Blind calibration already relevant to the envelopes:
- Prototype 24: sparse-start 2x2x2 versus 2x3x2;
- Prototype 25: target-rich versus relation-rich opening;
- Prototype 26: sparse-history tag compensation versus relation-rich opening;
- Prototypes 27-29: direct, mirrored, mixed and residual three-slot topologies;
- Prototype 32: successful two-slot fixed-properties + constraints core;
- Prototype 33: small 2x2 does not guarantee tutorial difficulty when composite
  clue interaction remains dense.

## 2. Two-slot envelope audit

### Tutorial

Working envelope:
- preferred 2x2;
- simple slot-local / exact-count facts;
- no need for XOR or implication;
- unique solution preferred.

Accepted corpus evidence:
- 2x2 simple grammar, compact weakness policy:
  - **91.1%** of all target-containing field instances reach a unique answer;
  - **24 / 24** concrete formula variants have at least one uniquely solvable
    2x2 field;
  - worst per-variant unique-field rate is **75.0%**.

Conclusion:
- **structurally proven across the full ordinary two-slot variant corpus**;
- the remaining uncertainty is tutorial presentation/cognitive load, not corpus
  coverage.

Prototype-33 consequence:
- the next tutorial must actually use the simple grammar; a 2x2 field with
  several composite clues is not evidence against the 2x2 tutorial envelope.

### Early

Working envelope:
- 2x2 / 2x3 / 3x2;
- simple clues remain normal;
- XOR may be introduced under reduced surrounding load.

Accepted corpus evidence:
- compact composite unique-field rates:
  - 2x3: **88.0%**;
  - 3x2: **83.1%**;
- all **24 / 24** variants have at least one uniquely solvable field at both
  sizes;
- under the stricter weak-clue stress test, all **24 / 24** variants still have
  at least one unique 2x3 and one unique 3x2 field.

Conclusion:
- **structurally robust**.

### Medium

Working envelope:
- primarily 2x3 / 3x2, with 3x3 available;
- familiar XOR and positive implication;
- interaction among individually partial clues.

Accepted corpus evidence:
- 3x3 composite compact unique-field rate: **79.5%**;
- every **24 / 24** variant has at least one uniquely solvable 3x3 field;
- strict weak-clue unique-field rate: **36.6%**, still with at least one unique
  field for **24 / 24** variants.

Conclusion:
- **structurally robust**;
- richer composite grammar has real capacity value rather than cosmetic wording
  value.

### Late / Boss

Working envelope:
- mainly 3x3;
- full accepted composite vocabulary;
- higher difficulty from interaction among familiar clues rather than larger
  fields.

Accepted evidence proves:
- every variant can support a strict weak-clue unique 3x3 solution using the
  full composite grammar;
- Prototype 32 already gives positive blind evidence for interacting
  implication/XOR/count reasoning.

Not yet separately quantified:
- a formal split between “late” and “boss”;
- frequency of packages that require exactly three mutually necessary clues
  while no two-clue subset already solves the field;
- exact cost of reverse-direction wording.

Conclusion:
- **upper-end capacity is proven; the late-versus-boss threshold remains a
  calibration problem, not a corpus-coverage blocker.**

Do not launch a new corpus-wide calculation solely to manufacture a boss label
before onboarding is calibrated.

## 3. Three-slot envelope audit

### Tutorial candidate

Working envelope:
- preferred 2x2x2;
- familiar property logic kept simple;
- the primary new concept is one adjacent STABLE/INCOMPATIBLE relation;
- a useful microtest is pedagogically desirable but not a permanent mandatory
  test count.

Accepted quantitative evidence:
- exact exhaustive representable 2x2x2 state service rate under the compact
  adaptive grammar: **95.815%**;
- exact worst recipe-variant service rate: **89.931%**;
- therefore 2x2x2 is not an unconditional generator guarantee.

Graceful richer fallback evidence:
- sampled 2x3x2 service: approximately **99.4%**;
- sampled 3x2x2 service: approximately **99.8%**;
- 3x3x2 and 3x3x3: **100%** in the accepted sample.

However Prototype 24 is decisive player evidence:
- a sparse-start 2x2x2 with only one weak target fact was **boring** and felt
  like checking possibilities;
- 2x3x2 was only modestly better;
- field size alone was not the missing ingredient.

Prototypes 25-26 further show:
- pre-existing relation structure is highly valuable because it behaves as an
  unfinished bridge;
- target-property facts are useful complements but do not fully substitute for
  relational structure across the whole puzzle arc.

Curriculum consequence:
- **2x2x2 remains a viable size, but not with the old sparse-start grammar**;
- the first relation tutorial must be deliberately prestructured by familiar
  property deductions so that the one new relation action has an obvious
  purpose;
- if a good 2x2x2 state does not exist, use the accepted 2x3x2 / 3x2x2 fallback
  rather than gating research or adding arbitrary clues.

This is the largest remaining onboarding uncertainty.

### Early

Working envelope:
- 2x2x2 through compact asymmetric 2x3x2 / 3x2x2 shapes;
- roughly 2-4 meaningful branches;
- one orientation at a time preferred;
- usually one or two useful new relation tests.

Accepted evidence:
- 2x3x2 and 3x2x2 are already near-universal compact service shapes;
- Prototype 25 validates a relation-rich middle-information opening;
- Prototype 26 validates relations as the primary scaffold with properties as
  complementary constraints.

Conclusion:
- **structurally and experientially supported**, subject to the first-teaching
  transition being calibrated.

### Medium

Working envelope:
- 3x3x3 becomes normal;
- multiple familiar clue forms;
- direct/mirrored/mixed relation orientations;
- variable zero-to-few new tests depending on prior knowledge.

Accepted adaptive screen at 0% prior relation knowledge:
- **16 / 16** targets have a fresh bounded 3x3x3 puzzle;
- the best fresh package uses two weak target-property facts for every target;
- intended target chain begins with both adjacent relations unknown.

Accepted blind prototypes:
- direct, mirrored and mixed anchor directions all produced viable deduction;
- composite clue forms are playable after the base grammar is learned.

Conclusion:
- **strongly supported**.

### Late

Working envelope:
- 3x3x3;
- richer prior relation graph;
- mixed orientation, reverse clue direction and residual-answer topology;
- clue-led, experiment-led and expertise-shortened cases all legitimate.

Accepted adaptive screen:
- at every sampled relation density and history family,
  **expertise-covered = 100%**;
- fresh-puzzle frequency decreases as knowledge rises, but every lost fresh
  puzzle is explained by the player already knowing both adjacent stable edges
  of at least one valid target formula;
- there are **zero** sampled no-fresh states where a target-chain edge is still
  unknown.

Accepted blind evidence:
- residual/off-starting-bridge answer shapes and mixed orientations have already
  been exercised successfully.

Conclusion:
- **strongly supported**;
- do not hide earned relation knowledge merely to force nominal difficulty.

### Boss

Working envelope:
- 3x3x3 remains the size ceiling;
- hardest fair combinations of already mastered concepts;
- short multi-stage proof rather than larger enumeration.

Existing evidence proves the component mechanisms separately:
- composite/reverse clue cost;
- mixed orientation;
- residual-answer topology;
- accumulated relation history;
- expertise-shortened cases.

Not yet proved:
- one specific production “boss” density/topology threshold.

Conclusion:
- **no architecture gap**;
- defer exact boss calibration until tutorial/early progression is stable.
  Building a corpus-wide boss classifier now would optimize the least urgent
  part of the curve.

## 4. Overall verdict

The working difficulty curriculum is **broadly realizable on the accepted
ordinary corpus**.

No evidence requires reopening either selected core grammar:
- two-slot fixed properties + logical constraints;
- three-slot Adaptive Knowledge-Aware properties + adjacent relations.

The main quantitative caveat is narrow and useful:
- preferred three-slot 2x2x2 onboarding is not universally serviceable
  (**95.815%**, not 100%);
- richer compact fallbacks already cover almost all/all tested states.

The main experiential caveat is even more important:
- sparse-start compact puzzles can feel like enumeration even when the
  mathematics says they are well bounded.

Therefore the next evidence need is **not another broad corpus screen**.

## 5. Smallest next blind calibration set

Run exactly two onboarding-focused blind prototypes before further generator
formalization.

### Prototype 34 — two-slot true tutorial

Purpose:
- test the curriculum claim that the first 2x2 should teach only
  property-intersection reasoning.

Precommit:
- 2x2;
- simple property facts only;
- no XOR;
- no implication;
- two or at most three facts;
- every fact partial;
- answer unique from intersection;
- no new theoretical decoy identities unless unavoidable.

Primary question:
> Does this finally feel like a genuine tutorial rather than Prototype 33's
> small-but-dense logic puzzle?

### Prototype 35 — three-slot relation-introduction tutorial

Purpose:
- test the cross-arity transfer claim.

Precommit:
- prefer 2x2x2; allow 2x3x2 / 3x2x2 only if the precommitted case cannot be
  shaped honestly;
- property reasoning uses only already-familiar simple forms;
- one genuinely new concept: adjacent STABLE/INCOMPATIBLE relation;
- starting property information must already create an obvious reason to test a
  particular adjacent pair or a very small choice among useful pairs;
- avoid the Prototype-24 sparse-start “blank block”;
- no mixed orientation, residual topology or composite-clue novelty;
- aim for one meaningful relation test, but do not force a ritual test if the
  precommitted knowledge state makes it unnecessary.

Primary question:
> Does the player understand why the new relation test is useful, and does the
> resulting step feel like extending familiar two-slot reasoning rather than
> starting an unrelated minigame?

Stop after these two prototypes and compare:
- clarity of first move;
- working-memory burden;
- “I worked it out” feeling;
- whether the relation layer feels like a natural escalation;
- whether 2x2x2 is acceptable for the first relation tutorial or should normally
  fall back to 2x3x2 / 3x2x2.

No installed-runtime test is required.
