# Difficulty Curriculum Generator Envelopes — 2026-10-06

Status: **working generator model for quantitative screening; conceptual curriculum rules accepted, exact numeric thresholds remain provisional; production remains BLOCKED.**

This document converts the accepted post-Prototype-33 difficulty direction and the external validation in `DIFFICULTY_CURRICULUM_EXTERNAL_VALIDATION_2026-10-06.md` into testable generator envelopes.

It does **not** define final UI labels, exact Science prices, production save fields, or runtime implementation.

## 1. Core model

Difficulty is not one scalar and is not defined by field size alone.

For each generated investigation evaluate at least:

- **candidate field** — visible candidates per slot;
- **live hypothesis trajectory** — how many plausible formula branches survive at meaningful points;
- **clue grammar** — simple facts versus XOR / implication / negative consequent / reverse-direction forms;
- **interaction depth** — how many partial facts must be combined before a useful deduction appears;
- **relation load** (three-slot only) — amount, polarity and topology of known/new STABLE or INCOMPATIBLE adjacent relations;
- **meaningful action demand** — useful microtests and, separately, formula submissions;
- **concept novelty** — reasoning concepts the player has not yet encountered in a completed investigation;
- **identity exposure** — newly exposed theoretical reagent identities;
- **brute-force attractiveness** — whether sequential submission/testing is easier than reasoning.

The generator should not collapse these dimensions into a single additive score at this stage. Use bounded envelopes plus rejection rules.

## 2. Curriculum beats: introduce -> practice -> combine -> breathe

The five broad difficulty bands are not a strictly monotonic sequence in every dimension.

Within either arity, use four pedagogical beat types:

### INTRODUCE
Purpose: teach one genuinely new reasoning concept.

Rules:
- at most **one new reasoning concept family** in the investigation;
- all other load dimensions should be below the normal ceiling of the current band;
- avoid simultaneously introducing several new reagent identities;
- the new concept must have a clear useful role, not decorative presence.

### PRACTICE
Purpose: reuse recently learned concepts under ordinary load.

Rules:
- no new reasoning concept family;
- modest increase in field size, clue interaction or relation work is allowed;
- prefer clear repetition with a different logical shape rather than exact repetition.

### COMBINE
Purpose: create the stronger “I worked this out” challenge.

Rules:
- no new reasoning concept family;
- difficulty comes from interaction among already familiar concepts;
- several individually partial pieces may become decisive only together;
- later/boss investigations should derive most of their difficulty from this beat.

### BREATHE
Purpose: prevent a permanently rising cognitive wall and allow earned expertise to feel valuable.

Rules:
- no new concept;
- one or more load dimensions intentionally below the current band norm;
- knowledge-resolved or clue-led zero-microtest cases are valid;
- do not manufacture extra work merely to keep the puzzle “busy”.

This beat model is the accepted wave-shaped curriculum consequence of the external validation.

## 3. Concept families and transfer

### Shared logical language

Concept families that can be learned in two-slot and transfer into three-slot:

1. stable reagent properties/tags;
2. slot-local requirement or exclusion;
3. total presence / absence / exact-count facts;
4. exact-one-of-two / XOR;
5. positive implication;
6. implication with negative consequent;
7. clue direction / reverse reference as a higher cognitive cost.

A concept already encountered successfully in two-slot should not count as newly introduced merely because it appears in a three-slot puzzle.

### Three-slot-specific relation language

Additional concept families:

1. an adjacent pair can be empirically **STABLE** or **INCOMPATIBLE**;
2. a known stable pair is a useful chemical anchor, not proof that the target formula uses it;
3. either adjacent orientation may be investigated (Powder-Liquid or Liquid-Essence);
4. several known relations may form a bridge/topology;
5. a valid target may remain as a residual answer outside the starting bridges.

The first three-slot investigation should primarily introduce the first relation concept. Do not introduce the complete bridge/topology vocabulary simultaneously.

## 4. Two-slot generator envelopes

The selected core remains fixed reagent properties + logical constraints.

### Tutorial / onboarding

Target experience:
> “Two ingredients have stable properties. Several simple partial facts intersect to identify the pair.”

Field:
- preferred: **2x2**;
- do not increase field merely to make the tutorial appear substantial.

Clues:
- **2-3 simple clues**;
- allowed: slot-local presence/absence and simple exact-count facts;
- XOR and implication are **not** tutorial requirements and should normally be absent;
- no individual clue may identify the answer by itself;
- compact small-field strength is acceptable: an individual clue may reduce four pairs to two or three.

Interaction:
- require at least one real intersection of facts;
- unique answer is preferred;
- do not use the residual-two fallback for the first tutorial unless a later blind test proves it pedagogically superior.

Novelty:
- one new reasoning idea: property-constraint intersection;
- theoretical identity exposure target: **0 new decoys**;
- at most one new reagent identity is acceptable if it is an unavoidable true component of the selected target and the puzzle remains otherwise simple.

Formula submission:
- intended state before confirmation: unique answer;
- anti-bruteforce economics remain separate and unresolved.

### Early

Field:
- **2x2**, **2x3** or **3x2**.

Clues:
- 2-3 clues;
- simple grammar remains normal;
- one composite family (prefer XOR before implication) may be introduced on an INTRODUCE beat;
- when a composite family is introduced, keep the field and other clues easier than the band maximum.

Interaction:
- unique answer remains ordinary target;
- exactly two survivors may occur as occasional bounded verification, not the dominant pattern.

Novelty/exposure:
- at most one new reasoning family in an INTRODUCE case;
- normally no more than one newly exposed reagent identity when an equivalent known-heavy field exists.

### Medium

Field:
- primarily **2x3 / 3x2**;
- **3x3** allowed, especially on a simple-grammar or BREATHE case.

Clues:
- XOR and positive implication may now be familiar normal tools;
- negative-consequent implication may be introduced under reduced surrounding load;
- 2-3 individually partial clues;
- prefer packages where at least two clues must interact materially.

Interaction:
- avoid one dominant clue doing nearly all the work;
- unique answer preferred;
- rare two-survivor residual verification remains valid.

Novelty/exposure:
- no more than one new reasoning family per INTRODUCE beat;
- 0-2 newly exposed identities are acceptable as a soft range, but minimize unknown decoys among equivalent fields.

### Late

Field:
- primarily **3x3**;
- smaller fields remain valid when their information structure is genuinely demanding.

Clues:
- full accepted composite vocabulary;
- reverse-direction formulations may appear;
- prefer weak clues whose conjunction creates the decisive reduction;
- all selected clues should be non-redundant.

Interaction:
- three-way clue interaction is desirable;
- difficulty comes from combining mastered ideas, not from adding a fourth/fifth clue by default;
- exact-two residual endings may be used as variety but should remain bounded.

Novelty/exposure:
- normally zero new reasoning families;
- theoretical identity exposure remains minimized rather than deliberately maximized.

### Boss / peak challenge

Field:
- normally **3x3**; do not exceed the currently screened field merely to make a boss puzzle larger.

Clues:
- 2-3 demanding, individually partial clues using familiar grammar;
- high interaction depth;
- may combine reverse direction with composite logic, but avoid maximizing every difficulty axis simultaneously.

Interaction:
- the intended challenge is a compact proof, not candidate enumeration;
- all clues should matter;
- at least one non-obvious cross-constraint step should be required;
- if brute-force pair submission becomes the simpler strategy, reject/regenerate the puzzle.

A boss is therefore “denser reasoning with known tools,” not “more candidates and more clicks.”

## 5. Three-slot generator envelopes

The selected core remains Adaptive Knowledge-Aware properties + adjacent STABLE/INCOMPATIBLE relations.

All prior learned relations internal to the chosen field remain honest external memory. Do not hide earned knowledge merely to manufacture a fresh puzzle.

### Tutorial / onboarding

Target experience:
> “The property logic is familiar. The new idea is that adjacent reagents have an empirical chemical relation that can be tested and remembered.”

Field:
- preferred: **2x2x2**;
- graceful fallback: **2x3x2** or symmetric **3x2x2** when the compact field cannot support a good tutorial.

Target clues:
- 1-2 simple familiar property facts;
- no stack of composite clues;
- if a shared logical concept is already familiar from two-slot, it may be reused without novelty cost.

Relations:
- introduce the STABLE/INCOMPATIBLE adjacent-relation concept only;
- keep topology direct and local;
- avoid mixed orientation, residual-answer topology and reverse-direction relation reasoning in the same tutorial.

Meaningful experiments:
- design candidate: normally **one clearly useful adjacent microtest** should teach the relation action;
- this is pedagogical, not a permanent minimum experiment rule;
- if existing knowledge already makes that test meaningless, choose another tutorial field rather than requiring a ritual test.

Live branches:
- aim for about **2-3 meaningful branches** after starting property information.

Novelty/exposure:
- one new reasoning concept: adjacent empirical relation;
- prefer 0 new decoy identities;
- allow at most one newly exposed true reagent identity where necessary.

### Early

Field:
- **2x2x2**, **2x3x2 / 3x2x2**, occasionally another compact permutation.

Target clues:
- simple familiar properties;
- a previously learned composite clue may appear sparsely;
- do not introduce a new logical clue family on the same investigation that introduces a new relation/topology concept.

Relations:
- one useful prior relation or one first-stage relation hypothesis is typical;
- one orientation at a time is preferred;
- clear distinction between “STABLE” and “relevant to this target”.

Meaningful experiments:
- usually **1-2** useful microtests;
- zero is valid on a BREATHE/expertise case when the answer is genuinely justified.

Live branches:
- roughly **2-4**, consistent with the accepted adaptive information-budget evidence.

### Medium

Field:
- compact asymmetric fields remain valid;
- **3x3x3** becomes normal where it gives a better information trajectory.

Target clues:
- familiar composite clues may be ordinary;
- 2-3 partial facts;
- forward-direction clues preferred when the relation topology itself is demanding.

Relations:
- direct, mirrored and mixed orientations are all available;
- both STABLE and INCOMPATIBLE prior knowledge may participate;
- accumulated player history may legitimately replace some target-specific clue burden.

Meaningful experiments:
- 0-2 is a healthy ordinary range;
- a third test can be acceptable when each test corresponds to a distinct reasoned branch rather than scanning.

Topology:
- target on a starting bridge is still common;
- non-target compatible branches may produce useful negative target evidence.

### Late

Field:
- normally **3x3x3**, but field size is not itself a requirement.

Target clues:
- full familiar clue vocabulary;
- reverse-direction clues may contribute deliberate cost;
- composite clue packages can coexist with richer relation topology.

Relations/topology:
- mixed orientation;
- denser prior relation graph;
- off-bridge / residual-answer topology available;
- starting STABLE relations may be immediately target-ineligible if clues prove that clearly.

Meaningful experiments:
- variable; clue-led zero-test and experiment-led cases both remain legitimate;
- reject paths that require filling a compatibility matrix.

### Boss / peak challenge

Field:
- **3x3x3** is the current ceiling; do not seek larger fields for prestige.

Target clues and relations:
- use the hardest fair combinations of **already mastered** concepts;
- a peak case may combine two major high-cost features (for example residual topology + reverse/composite clues), but should not automatically stack every available difficulty feature;
- known relation density may be high because expertise is real, not because the generator injects noise.

Interaction:
- aim for a short multi-stage proof:
  property constraints -> relation/topology consequence -> residual or final formula;
- several plausible branches may exist, but the player should not need broad enumeration;
- if accumulated knowledge fully establishes a valid target chain, allow earned expertise to shorten or effectively solve the case rather than hiding knowledge.

## 6. Hypothesis-space and clue-strength rules

### Two-slot

Do not balance only by total pair count.

Track:
- raw visible pair count;
- survivors after each individual clue;
- survivors after clue intersections;
- whether every clue is necessary;
- final clue-consistent survivor count before formula submission.

Working targets:
- tutorial: 4 raw pairs -> partial reductions -> 1;
- early/medium: preserve several candidates after every individual clue, then converge through interaction;
- late/boss: prefer stricter weak-clue packages where feasible.

The accepted quantitative screen already proves that compact and strict weakness policies have different roles. Do not force the 2/3 weakness ratio onto 2x2.

### Three-slot

Retain the accepted actionable-branch model:
- roughly **2-4 meaningful first-stage branches** is the ordinary envelope;
- one branch can be legitimate when accumulated knowledge has earned it and several continuations remain;
- do not use raw full-triple count as the sole cognitive metric;
- do not require a minimum number of new experiments.

## 7. Identity-exposure budget

Theoretical reagent identities remain allowed, including decoys.

Treat exposure as a soft generation cost:

1. prefer fields using already known/mastered identities when puzzle quality is equivalent;
2. introduce a new true component when needed for the target flow;
3. introduce unknown decoys only when they materially improve the intended puzzle structure;
4. among equivalent surfaces choose the one with fewer unnecessary new identities.

Curriculum preference:
- tutorial: 0 new decoys; <=1 new identity total where practical;
- early: normally <=1 new identity;
- medium: 0-2 is acceptable;
- late/boss: no fixed reward for higher exposure; allow more only when the puzzle needs it.

These are screening targets, not final production constants.

## 8. Brute-force attractiveness is a separate veto

Do not treat anti-bruteforce as just another difficulty point.

For every candidate puzzle later evaluate:
- clue-consistent candidates before submission;
- intended number of reasoned submissions;
- cost and information content of a wrong submission;
- how many blind submissions a resource-rich player could make;
- whether sequential guessing is strategically easier than the designed reasoning path.

A puzzle that is logically elegant but economically easier to brute-force fails the product goal.

The working “1 Science per formula submission” value remains unvalidated balance and must not be embedded in the curriculum constants.

## 9. Generator selection order

A future generator/scorer should conceptually search in this order:

1. determine arity-specific progression band;
2. determine curriculum beat (INTRODUCE / PRACTICE / COMBINE / BREATHE);
3. determine which concept families are already familiar;
4. build candidate fields that contain the hidden variant and respect the identity-exposure preference;
5. build clue/relation packages allowed by the band and beat;
6. evaluate hypothesis trajectory and meaningful experiment demand;
7. reject over-solved, under-structured, redundant or brute-force-attractive candidates;
8. among equivalent candidates prefer lower unnecessary novelty/exposure and simpler presentation.

Do not begin with a fixed field size and then pile clues onto it until uniqueness appears.

## 10. What is accepted versus provisional

Accepted:
- two independent arity ladders;
- multidimensional difficulty;
- field size is not sufficient as a difficulty measure;
- one new reasoning concept at a time on introduction beats;
- reduced surrounding load when introducing a new concept;
- later difficulty primarily combines familiar concepts;
- non-monotonic/wave-shaped local difficulty;
- persistent external memory and honest use of accumulated knowledge;
- theoretical identity exposure as a soft cost;
- brute-force attractiveness as a separate design criterion.

Provisional until quantitative/blind validation:
- exact band field distributions;
- exact clue-count and weakness thresholds per band;
- “normally one microtest” for the three-slot tutorial;
- numeric exposure ranges;
- exact frequency/order of INTRODUCE/PRACTICE/COMBINE/BREATHE beats;
- exact definition of when a concept becomes “familiar/mastered”.

## 11. Next evidence step

Do **not** start production implementation.

Next, screen these envelopes against the concealed ordinary corpus and accepted property/relation model.

The quantitative pass should answer, separately for two-slot and three-slot:
- coverage of each band;
- how often the preferred field shape exists;
- how often a fallback shape is needed;
- clue-family availability under the novelty rules;
- interaction-depth / redundancy distribution;
- expected relation-test demand for three-slot;
- theoretical identity exposure needed to satisfy each band;
- frequency of expertise-resolved starts;
- frequency of candidate states that are easier to brute-force than to reason through.

Only after those envelopes prove broadly realizable should we select the smallest set of blind paper prototypes needed to calibrate the provisional thresholds.
