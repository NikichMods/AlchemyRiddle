# Product Requirements and Acceptance Envelope

## Problem

Vanilla Graveyard Keeper teaches enough of farming/fertilizer progression for the player to encounter a need for a specific alchemical product, but it does not provide a sufficiently legible route from:

`I need product X -> what should I investigate -> what experiment should I run -> what did that result teach me -> why should the next experiment move me toward X?`

Failed alchemy experiments and slime-like outputs may encode useful information, but three gaps must be distinguished:

1. **interpretation gap** — the player is not adequately taught what a failed result means as information;
2. **targeting gap** — even after understanding failed-result semantics, the player may lack a reasoned way to investigate one particular required unknown product;
3. **continuity gap** — Graveyard Keeper naturally interrupts alchemy with energy, day/NPC schedules, corpse handling, farming, production and other systems, while vanilla does not preserve enough investigation context for the player to resume a multi-step deduction without reconstructing it from memory.

The project exists to close those gaps without replacing discovery with recipe disclosure.

## Durable product goal

**Make vanilla alchemy independently solvable as a deductive puzzle, without wiki lookup, brute-force enumeration, or advance revelation of formulas.**

Core principle:

**Do not make alchemy easier by giving the answer; make it explainable and solvable.**

Desired player conclusion after success:

> I worked out this recipe.

## Acceptance envelope

For an unknown vanilla product within the supported scope, the final design should make it possible to demonstrate, without revealing the formula in advance, that:

- the player has a comprehensible reason to begin investigating that specific product;
- the player understands the rules needed to interpret experimental outcomes;
- each meaningful experiment can reduce uncertainty or establish a useful constraint;
- controlled changes in an experiment produce feedback that is locally interpretable enough to support controlled reasoning;
- the information gained from an experiment is reasonable relative to its material cost and the gameplay interruption required to replace consumed reagents;
- the player can leave alchemy, engage with normal Graveyard Keeper systems, and later recover the established facts/open hypotheses without reconstructing the investigation from human memory alone;
- the next experiment can be chosen for a reason the player can articulate;
- blind full enumeration is not required;
- a wiki or external recipe list is not required;
- for the target deductive architecture, the system does not simply drip-feed a hidden recipe one ingredient at a time;
- successful discovery should preferably culminate in the real alchemy interaction, but this is **not a hard requirement**: if the research/minigame has logically exhausted all alternatives and uniquely determined the formula, it may explicitly resolve/reveal that formula rather than forcing a ceremonial final craft;
- after success, the player can explain why the decisive experiments were informative.

A good solution should normally converge in a small number of **meaningful** experiments after a useful initial clue. The exact target count is intentionally not fixed before the real search space is measured.

The cognitive and record-keeping burden should also fit Graveyard Keeper's broader, interruption-heavy game loop. The design must not assume the uninterrupted concentration or manual note-taking expected from a dedicated hardcore logic-puzzle game.



### Accepted target experience and investigation entry point

The intended alchemy interaction is a **short micro-deduction**, not a standalone hardcore puzzle. As a working UX target, an ordinary investigation should often fit roughly **1–3 minutes** of focused reasoning: enough friction for the player to feel briefly clever and competent, but not enough to become exhausting or dominate Graveyard Keeper's wider loop. This is a design target, not a rigid timer.

The preferred investigation entry point is the first **visible vanilla need for a specific unknown alchemical product X**. The intended flow is:

`visible need for X -> journal records X as an unknown research topic -> player chooses X -> first meaningful research step`

The notification for a newly recorded unknown product should be neutral, e.g. that a new journal entry was added. It should not itself explain the formula or direct the player toward a specific answer path.

Before creating an investigation topic, check whether vanilla has already legitimately revealed/unlocked the formula. Already-known formulas bypass the research loop rather than becoming fake mysteries.

The journal is part of the product, not merely convenience UI. It must function as external memory for experiments, observations, established/excluded facts, live hypotheses and the reason the investigation exists, so returning after normal gameplay interruption is easier than resorting to an external wiki.

## Design quality ladder and fallback policy

The project target remains a genuine deductive puzzle, but design quality is not binary. Use this ladder when comparing candidates:

1. **Opaque / vanilla-like** — information may exist internally, but the player is not taught enough to use it and has no reliable route toward a requested product.
2. **Guided disclosure** — the system deliberately narrows or reveals bounded parts of the hidden formula (for example, reducing one slot to a small explicit candidate set). This is not the target architecture, but it is a legitimate **fallback quality floor** because it can still remove wiki dependence and blind enumeration.
3. **Deductive narrowing** — the system gives facts or experiment outcomes and the player performs the inference that narrows the formula.
4. **Experimental deduction** — the player can choose informative experiments, interpret their consequences, form the next hypothesis, and ultimately verify a formula through real alchemy.

Levels 3–4 satisfy the intended product direction much better than level 2. Level 2 must not be rejected merely because it is staged disclosure; instead, retain it as a fallback if stronger designs prove disproportionate, incoherent across the real corpus, or mechanically worse.

Choosing a level-2 production architecture instead of the deductive target requires an explicit product decision after the solution-space trade study.

## Preserved invariants by default

Until evidence and an explicit product decision justify otherwise:

- keep vanilla recipe formulas unchanged;
- keep vanilla recipe success/failure semantics unchanged;
- keep progression, economy and save behavior unchanged;
- do not auto-unlock unknown recipes;
- do not expose exact unknown formulas **by default**; however, this anti-spoiler constraint is subordinate to finding the best player experience during design research. If hiding real formulas materially constrains solution-space analysis, the constraint may be relaxed explicitly rather than allowing spoiler protection to distort the design;
- do not require a parallel external encyclopedia;
- do not make arbitrary lore/flavor text carry mechanical meaning unless the rule is taught consistently.

## Candidate directions, not decisions

The following are research families only:

- better teaching/visualization of existing failed-experiment information;
- explicit investigation of a selected unknown product;
- product/reagent properties or signatures that support deduction;
- a deduction journal recording established/excluded constraints;
- hybrid systems combining the above.

None is accepted architecture at bootstrap.

## Design quality tests

A candidate fails the **target deductive standard** if it:

- works only when the player already knows roughly what the answer is;
- reduces random search but still leaves no route toward a requested product;
- encodes the answer behind a fixed sequence of clicks rather than inference; this may still be retained and evaluated as a level-2 fallback rather than discarded outright;
- requires dozens of low-information experiments in ordinary cases;
- consumes significant reagents or forces substantial reacquisition/context switching for low-information checks;
- depends on the player remembering prior attempts, inferred constraints or pending hypotheses across normal gameplay interruptions;
- teaches special-case exceptions instead of a coherent rule system;
- solves only a few hand-picked recipes while failing structurally on the rest of the corpus;
- relies on exact formula disclosure to explain why it works.

## Anti-spoiler requirement

Technical research may inspect the real recipe corpus privately as test data. Reports to the user and public-facing design discussion should default to aggregate evidence: recipe counts, candidate-space sizes, ambiguity classes, information gain, exceptional-case counts and path lengths.

Do not reveal exact ingredients or effectively reconstruct an unknown formula unless the user explicitly asks for that recipe.


## Clarifications accepted 2026-10-04

### Final craft is a preference, not a hard gate

The strongest experience is still expected to be one in which the player gathers enough direct and indirect evidence to form a justified hypothesis and then confirms it through ordinary alchemy.

However, the project must not artificially preserve uncertainty merely to force one more vanilla craft. If the investigation has legitimately eliminated every alternative and the formula is already uniquely determined, the research/minigame may acknowledge the solved recipe directly. A forced craft at that point would be ceremonial rather than deductive.

### Anti-spoiler policy is subordinate to product quality during research

Avoiding unnecessary recipe spoilers remains the default reporting discipline. It must not become a design constraint that prevents rigorous analysis of the real corpus or narrows the solution space.

If exact-formula inspection or explicit discussion becomes necessary to evaluate a candidate design properly, prefer the stronger research/design result. Relax the spoiler constraint explicitly and minimally rather than preserving it at the cost of a worse game.


## Progression-sensitive puzzle scaling and recipe variants

Accepted product intent:
- when the player's growing reagent knowledge naturally permits it, early
  investigations should tend to be smaller/easier and later investigations may
  become richer/more complex;
- this progression is desirable rather than something the generator should
  flatten away;
- fixed 3x3x3 fields are not required in production; smaller bounded fields are
  acceptable when they still produce a meaningful deductive interaction;
- a merely non-unique field is not sufficient: very small/trivial candidate
  spaces may fall below the intended puzzle-quality floor and require a different
  treatment.

For products with multiple vanilla formulas:
- unknown formula variants remain independently researchable;
- discovering one valid recipe must not erase the player's opportunity to
  discover other vanilla variants;
- a selected recipe-variant investigation may be generated around that specific
  hidden variant rather than requiring one puzzle to preserve every formula for
  the product at once;
- exact UI labeling and presentation of unknown variants remain open.

Readiness principle:
- if the selected hidden variant is fully representable from the player's
  legitimate reagent knowledge, prefer a suitably simplified puzzle over a hard
  block caused only by missing distractors;
- do not require discovery of irrelevant reagents solely to decorate or pad the
  puzzle;
- if a true component is still unknown, a hard readiness gate may be legitimate,
  but the eventual guidance must not simply reveal that missing component.


### Recipe-variant visibility

For products with multiple vanilla formulas, it is acceptable for the UI to
reveal **how many recipe variants exist**. This count is not considered a
meaningful recipe spoiler.

Unknown variants may remain individually researchable until each is discovered.
Exact labels and presentation remain open.


### Independent difficulty ladders by recipe arity

Accepted product direction:
- difficulty progression is **not one global chronological ladder** from all
  two-slot alchemy into all three-slot alchemy;
- two-slot and three-slot investigations have **independent difficulty ladders**,
  because actual Graveyard Keeper target needs can interleave after the relevant
  workstation/technology capabilities are available;
- the first investigation the player actually undertakes in each arity should be
  eligible for an onboarding/tutorial-grade puzzle even if the other arity has
  already been used several times;
- later investigations within the same arity should generally grow richer and
  harder, up to occasional late "boss"-grade cases, subject to real
  progression/knowledge and corpus feasibility rather than a rigid fixed curve;
- shared concepts should transfer across arities (stable reagent properties,
  basic count/exclusion logic, later compound logical forms), while three-slot
  alchemy remains a richer but partly independent grammar because it adds
  adjacent STABLE/INCOMPATIBLE relation knowledge;
- difficulty should be generated from the player's **within-arity investigation
  history / current knowledge state**, not from a fixed assumption that every
  two-slot target is encountered before every three-slot target.

Formula-variant advancement is resolved below under **Formula-variant completion
advances arity experience**: every independently completed variant counts as
genuine within-arity practice. Exact numeric rank increments remain a generator
implementation detail.



### Optional decorative targets do not reserve difficulty

Accepted product direction:
- optional decorative/remodelling alchemy targets are **side content**, not the
  denominator of either arity's mandatory difficulty curve;
- do not reserve late/boss difficulty for targets that a normal player may never
  choose to pursue;
- do not proactively populate the journal with every decorative target merely
  because its formula exists;
- create/surface such a lead when the player has a concrete visible decorative
  or remodelling need;
- if the player voluntarily starts one, generate it from the player's current
  two-slot difficulty state rather than assigning a permanent "late paint"
  difficulty;
- whether optional completions advance the arity experience counter remains a
  balance detail, but they must never be required to reach the top difficulty
  bands.

For the current ordinary corpus classification, eight decorative colour variants
are in this optional group. White and black paint are not: they also have
ordinary gameplay production uses.



### Reasoning-motif diversity is curriculum-aware

Accepted generator requirement:
- avoid accidental campaign-level repetition not only of reagent identities, but
  also of exact property signatures and recently used reasoning motifs;
- track recency/cost separately for at least:
  - reagent identity;
  - exact property signature;
  - major logical family (property literal/exclusion, exact count, XOR,
    positive implication, negative-consequent implication);
  - richer reasoning fingerprint where practical, including relation
    orientation / bridge shape and rough branching/experiment structure;
- do **not** optimize for mathematically equal frequencies of every clue family;
  the curriculum owns when repetition is pedagogically useful.

The recency policy must respect the accepted wave-shaped curriculum:
- INTRODUCE may add one genuinely new motif under reduced surrounding load;
- PRACTICE may deliberately repeat the focus motif and should reduce or invert
  its normal recency penalty;
- COMBINE should mix already mastered motifs while penalizing an exact recent
  reasoning fingerprint;
- BREATHE should prefer a simpler mastered route and avoid the recently dominant
  motif where feasible.

A short deliberate repetition such as XOR -> XOR can therefore be correct
practice. A long run such as five XOR-heavy puzzles must not happen merely
because the generator failed to account for recent reasoning history.

### Goal-first research coexists with vanilla experimentation

The preferred mod flow remains:
`visible need for unknown product -> journal target -> selected investigation`.

This is additive to vanilla alchemy rather than a reason to prohibit free
vanilla experimentation. Preserve the player's ability to try mixtures directly
unless later evidence establishes a concrete conflict. The mod should make a
targeted deductive route available; it does not need to close the existing
vanilla route merely because that route is opaque.


### Recipe-variant difficulty is assigned at investigation start

Accepted refinement:
- an alternative formula variant does **not** inherit the difficulty that another
  formula for the same output had when that earlier formula was researched;
- every unresolved formula variant is an independent research puzzle;
- when the player actually starts investigating that variant, its puzzle should
  be generated from the **current within-arity difficulty state** and current
  legitimate reagent knowledge;
- therefore two valid formulas for the same product may legitimately be
  encountered as easy and later/harder investigations. This is not considered a
  product inconsistency: the difficulty belongs to the research puzzle and the
  player's current expertise, not to an intrinsic fixed difficulty of the output;
- once an investigation has started, its generated puzzle state should remain
  stable rather than silently changing difficulty while the player postpones it.

Exact counter advancement semantics remain to be finalized together with the
difficulty generator. The leading hypothesis is that completing any genuinely
independent formula-variant investigation should count as alchemical practice,
rather than special-casing alternative formulas solely because they share an
output.


### Formula-variant completion advances arity experience

Accepted refinement:
- completing an independently researched formula variant counts as genuine
  practice for that recipe arity, even when another formula for the same output
  was researched earlier;
- therefore a later alternative formula normally participates in the same
  within-arity difficulty progression as any other completed investigation;
- exact numeric rank increments remain generator implementation detail, but do
  not special-case an alternative formula as "not real progression" merely
  because its output is already known.

### Investigation state must survive interruption

Accepted continuity requirement:
- entering a deduction puzzle must not trap the player in that screen until
  completion;
- the player may leave normal research UI and return to Graveyard Keeper
  activities at any time;
- an investigation's generated puzzle state is frozen once that investigation
  starts: difficulty budget, candidate field, surfaced clues, experiments,
  exclusions/marks and other earned evidence must resume exactly rather than be
  regenerated from the player's later progression state;
- the journal remains the external-memory owner for this continuity.

The later **One active deduction and visible progress** decision supersedes the
earlier multi-investigation option: only one unsolved deduction may be active at
a time. Other discovered targets remain visible in the journal, and the active
puzzle resumes unchanged after interruption.

### Separate theoretical deduction from practical acquisition

Accepted product model:
- a target investigation may reason about a bounded set of **theoretical reagent
  identities** even when the player has not yet learned the practical
  source/decomposition route for every reagent shown;
- the puzzle may establish a unique theoretical formula before every component is
  practically obtainable;
- theoretical exposure must not silently grant decomposition knowledge,
  inventory, or practical source mastery;
- once deduction uniquely determines a concrete vanilla formula variant, that
  formula becomes known recipe knowledge immediately;
- if a required reagent is not yet practically mastered, the solved formula
  creates a separate reagent-acquisition/source-research lead.

The accepted two-layer flow is:
`deduce/unlock formula knowledge -> learn missing reagent route(s) if needed -> synthesize when practical`.

The later **Deduction unlocks recipe knowledge before first synthesis** section is
the canonical recipe-knowledge boundary.


### One active deduction and visible progress

Accepted product behavior:
- only **one unsolved deduction investigation** may be active at a time;
- the player may leave the research UI and return to normal gameplay freely;
- returning later resumes the exact persisted puzzle state;
- other discovered research targets remain visible in the journal but cannot start
  a second deduction until the active one is theoretically solved;
- once the deduction reaches a unique formula, the active deduction slot is
  freed immediately even if practical reagent acquisition or final synthesis
  remains outstanding;
- the relevant two-slot or three-slot difficulty progression advances when the
  deduction is completed, not when the target is eventually synthesized.

Visible progression is desirable:
- when feasible, expose the player's real progression through each arity's
  difficulty ladder rather than hiding it entirely;
- difficulty labels/bands, progress indicators, completed milestones or similar
  UI may reinforce competence and long-term mastery;
- presentation must reflect real system state rather than inventing fake
  progression.

Current presentation scope, clarified 2026-10-07: Puzzle Lab does not yet expose
labels such as tutorial/easy/medium/hard or a difficulty/progression bar.
Showing meaningful player progression remains desirable, but its final metric
and UI are open; increasing difficulty alone must not silently be treated as
equivalent to player progression. Existing within-arity progression design is
retained. Research fixture identities/band hypotheses are internal metadata.

### Theoretical reagent identities are valid puzzle candidates

Accepted product decision:
- a target puzzle may show the **real in-game reagent identity/name** and the
  real AlchemyRiddle property tags for a reagent even if the player has never
  physically produced that reagent before;
- this is an intentional abstraction cost accepted in exchange for a much more
  world-grounded puzzle than arbitrary symbolic placeholders;
- the player is allowed to learn that such a reagent exists through target
  research itself;
- exposing the reagent identity/property card does **not** automatically teach
  its source/preparation route or grant the vanilla decomposition unlock.

Reagent property tags should also be available from ordinary item/tooltips once
the relevant reagent identity is known, so the puzzle does not depend on hidden
journal-only metadata or external memory.

### Deduction unlocks recipe knowledge before first synthesis

Accepted product decision, superseding the earlier default that unknown recipes
must not be auto-unlocked:
- when an investigation uniquely determines a concrete vanilla formula variant,
  that formula becomes **known recipe knowledge immediately**;
- the vanilla alchemy recipe-selection/known-recipe presentation should then
  recognize that formula in the same semantic sense as a vanilla scripted recipe
  discovery;
- the player does not need to perform a ceremonial first synthesis merely to
  make the already-deduced formula appear in the known-recipe list;
- actual possession/production of each reagent remains separate, so a known
  formula may be temporarily uncraftable because one or more reagent source
  routes are still unknown or unavailable.

This is an explicit product-level exception to the bootstrap invariant
`do not auto-unlock unknown recipes`. Formula contents and vanilla success
semantics remain unchanged.

### Goal-first reagent-source research

Accepted direction:
- when a known/theoretically exposed reagent lacks a practical source route,
  the journal may list it as an unresolved substance/source problem;
- the player may spend **Science** on a concrete research action to learn new
  acquisition/preparation information for that reagent;
- every Science expenditure in this subsystem should produce a concrete new
  observation, relation or source/preparation fact rather than function as a
  generic entry fee;
- the default safe behavior is informational/hybrid: research teaches a valid
  source/preparation route, while ordinary vanilla Study/decomposition/physical
  acquisition remains required unless a later explicit decision changes it.

Exact Science costs and whether some actions also require Faith remain open.

### Pause while using the research interface

Accepted UX preference:
- normal world time should be paused while the dedicated alchemy research/journal
  interface is open, not only while a logical puzzle sub-screen is open;
- this lets the player read known formulas, reagent/property references,
  unresolved-substance entries and deduction state without NPC/day/corpse timers
  pressuring them;
- the UI should communicate clearly that time is paused.

The technical pause mechanism remains BLOCKED pending exact host ownership and
lifecycle evidence.

### Paid formula submission prevents brute-force confirmation

Accepted direction:
- if the player may submit an arbitrary candidate formula and receive a
  success/failure verdict, that action is an information-producing oracle rather
  than a ceremonial confirmation;
- a free unlimited confirmation action would let the player brute-force candidate
  pairs/triples instead of reasoning;
- such formula submission should therefore have a non-zero research cost, with
  **Science** as the leading native resource;
- a working prototype value is **1 Science per submitted formula**, but exact
  production cost remains a balance decision;
- a logically unique answer may still be submitted through the same interaction
  for consistency, but the reason for the cost is anti-bruteforce pressure, not
  forcing uncertainty after deduction;
- if the final interaction can avoid exposing a reusable free success/failure
  oracle by some other clean mechanism, that may also satisfy the requirement;
  the invariant is **no free brute-force confirmation**, not necessarily a fixed
  fee of exactly 1 Science.

Exact wrong-answer feedback must not reveal more information than the agreed
success/failure semantics unless that information is deliberately part of the
puzzle design.

### Deduction success is acknowledged before practical blockers

Accepted UX sequence when a submitted formula succeeds:
1. explicitly acknowledge success;
2. show the now-known target formula and its components;
3. record/unlock that formula as known recipe knowledge;
4. only then evaluate whether each required reagent is practically mastered;
5. for any missing practical route, surface a separate new lead such as
   **"Source research available: <reagent>"**;
6. the player is free to start another deduction or pursue the reagent-source
   lead.

Do not merge "you solved the formula" and "you still cannot obtain one reagent"
into one ambiguous failure-like message. The deduction should feel complete
before the next practical problem is introduced.


### Reagent compendium preserves paid research knowledge

Accepted product direction:
- source/preparation knowledge must be durable reference data, not a transient
  notification or research-history entry;
- maintain a unified compendium/database for **all known reagent identities**,
  not only reagents that were once missing from a target formula;
- for each known reagent, the player should be able to inspect:
  - its identity/name;
  - its accepted AlchemyRiddle property tags;
  - whether a practical source/preparation route is known;
  - the known route when it has been learned;
- when the route is unknown, the compendium may expose the corresponding
  source-research action;
- do not require the player to search old journal chronology to recover
  information they previously paid Science to learn.

Exact layout, status wording and navigation remain UI-design questions. Avoid
unnecessary bureaucratic states such as a permanent "practical mastery still
ahead" label when the durable route knowledge itself communicates what matters.


### Unknown decoy reagents may appear, but source research remains goal-first

Accepted product direction:
- a deduction puzzle may include real in-game reagent identities that the player
  has not yet practically mastered, **including decoy candidates** that are not
  part of the hidden formula;
- the generator should prefer already-known/mastered reagent identities where
  practical, but it is not constrained to them when a richer field is needed;
- exposing an unmastered decoy identity/name/properties inside the puzzle is an
  accepted small future-content spoiler cost in exchange for preserving
  difficulty progression and a world-grounded candidate field.

However, merely appearing as a candidate does **not** automatically create a
source-research task.

Goal-first rule:
- source/preparation research becomes actionable when the reagent is established
  as **actually needed by a known/deduced formula or another concrete visible
  gameplay need**;
- decoy reagents that merely appeared in a puzzle do not populate an
  "investigate everything you saw" task queue;
- therefore the journal may maintain a focused section such as
  **unknown substances required by known formulas**, rather than treating every
  exposed candidate as an acquisition objective.

This prevents the mod from turning bounded puzzle distractors into arbitrary
completionist busywork.


## Difficulty curriculum: novelty and wave-shaped progression

Accepted product direction after the 2026-10-06 external validation:

- puzzle difficulty is **multidimensional**; field size or clue count alone must
  not define the difficulty rank;
- treat **concept novelty relative to the player's prior investigations** as an
  explicit difficulty cost;
- when a reasoning concept is first introduced, introduce at most one genuinely
  new concept family in that investigation and deliberately reduce surrounding
  load rather than making every difficulty dimension rise at once;
- after a concept has been introduced, later investigations may practice it and
  then combine it with other already-familiar concepts;
- local progression should therefore be **wave-shaped**, not strictly monotonic:
  introduce under reduced load -> practice -> combine -> occasional breather ->
  next conceptual escalation;
- late/boss difficulty should come primarily from richer interaction among
  already-mastered ideas, not from maximizing field size, clue count, relation
  density, unfamiliar reagent identities and experiment count simultaneously;
- concepts learned in two-slot alchemy transfer into three-slot alchemy and
  reduce their novelty cost there; the adjacent STABLE/INCOMPATIBLE relation
  layer remains genuinely new and deserves its own low-load onboarding;
- accumulated knowledge may legitimately shorten later puzzles. Do not hide
  correct prior knowledge merely to preserve a nominal difficulty curve.

Theoretical reagent-identity exposure remains a separate soft generation cost:
prefer familiar identities when an equally good puzzle exists, especially
during onboarding, but do not turn that preference into a hard readiness gate.

Brute-force attractiveness is also a separate product criterion. A puzzle is
not acceptable merely because its logical difficulty is well calibrated if
blind sequential formula submission is strategically easier than reasoning.
The working Science cost for submission is not by itself proof that brute force
is adequately controlled.

Exact numeric band thresholds, concept-familiarity counters, submission economy
and curriculum beat frequency remain generator/balance questions.



### Curriculum pacing: teach early, play richly for the majority of each ladder

Accepted product direction:
- the independent two-slot and three-slot ladders are short enough that the
  curriculum should be **hand-authored at the step-role level** rather than
  driven by a general-purpose curriculum state machine unless a later concrete
  need proves one necessary;
- INTRODUCE / PRACTICE / COMBINE / BREATHE remain useful descriptions of a
  step's pedagogical role, but they are **not a mandatory four-step cycle** after
  every newly introduced concept;
- onboarding should be deliberately front-loaded: teach the puzzle language
  quickly, then spend the majority of the remaining investigations on richer
  puzzles that combine already-known mechanics;
- explicit teaching is front-loaded and compact; the current semantic target is
  roughly the first **four** investigations of each arity carrying most genuine
  concept introduction, followed by rich/hard play;
- the mature/MAX envelope should become available roughly around the **sixth or
  seventh** investigation of an arity rather than being reserved for the tail;
- the full 16 two-slot / 19 three-slot variant sets are completionist capacity,
  not assumed campaign lengths; after MAX is reached, the remaining content
  forms a mature plateau with rich, hard, breathe and selected boss peaks;
- late richness should come from interaction depth, clue weakness, field shape,
  relation topology and combinations of familiar operators rather than from
  continuing to introduce new rules;
- BREATHE steps should be occasional deliberate load releases, not a metronomic
  every-fourth-step requirement;
- reverse/reference-direction wording is the same implication mechanic read
  from the opposite slot direction and does not receive a dedicated teaching
  rung by default.

Exact numbered placement inside the mature plateau remains tuning. The accepted
semantic order is: basic language -> compact concept introductions -> rich
combination -> hard -> early MAX -> mature plateau -> selected boss peaks.

### Accepted property-density refinement: Dark and rare four-tag cards

Accepted product direction:
- **Dark** is accepted as a real AlchemyRiddle reagent property for the
  Health / Death / Acceleration dark-family reagent identities across their
  Powder / Fluid / Essence forms;
- do not block Dark on a requirement for a separate visual-identification test;
  the combined vanilla naming/family/color semantics are sufficient for this
  design decision;
- the former practical ceiling of exactly three visible properties per reagent
  is relaxed;
- **rare four-property cards are allowed** when the fourth property follows from
  a strong, globally coherent world-grounded rule;
- four-property cards are desirable candidates for later/higher-density puzzles,
  but difficulty is still multidimensional: a four-property card does not by
  itself define a late puzzle;
- do not create four-property cards merely to make the histogram richer.

Warm/heat-colour grouping is rejected as a current tag direction.

Organ remains the leading next systemic candidate. If a consistent Organ rule
creates a small number of four-property cards, that is no longer a reason to
discard it.


### Difficulty ceiling should arrive early enough for partial-play players

Accepted product refinement:
- do not assume a player will complete every independently researchable formula
  variant in either arity;
- the difficulty curve should therefore expose the **full mature grammar and
  maximum difficulty band early enough** that a player who researches only a
  modest subset of available alchemy targets can still experience the complete
  progression from tutorial to hard play;
- reaching the maximum band does **not** mean every later puzzle must be a boss
  puzzle: after the ceiling is unlocked, continue with a mature plateau that may
  alternate normal hard puzzles, occasional lower-load breathers and explicit
  boss/peak puzzles;
- reserve several late investigations as guaranteed boss-grade peaks for
  completion-oriented players, but do not reserve first exposure to the maximum
  difficulty band for the very end of the 16-step / 19-step ladders;
- simple exact-count clues are part of the basic shared grammar and do not need a
  dedicated repeat/teaching step after the initial onboarding;
- reverse slot-direction implication wording is the same implication mechanic
  read from the opposite slot direction, not a separate logical rule that
  automatically deserves its own lesson.

Rationale from accepted progression evidence:
- the two-slot core contains 10 distinct outputs / 16 formula variants, but only
  8 of those outputs have strong downstream or direct story/system demand while
  2 are player-driven direct-use consumables;
- the three-slot core contains 16 distinct outputs / 19 variants, with 10 strong
  downstream-use outputs and 6 player-driven direct-use consumables;
- alternate formula variants remain independently researchable but are not a
  safe assumption for ordinary natural-demand progression.

Exact first-max-band and boss-step indices remain tuning work.


### Mature and boss difficulty: richer cards plus deeper interaction

Accepted product refinement:
- visible reagent-property richness should generally increase with difficulty: onboarding should prefer simpler one-property cards when an equally good surface exists; early play may mix one- and two-property cards; mature/MAX and boss play should increasingly prefer two-, three- and naturally occurring four-property cards;
- this is a **soft field-level preference**, not a requirement that every true late-game formula component itself have many properties. Vanilla formulas remain fixed, so a valid late target with simple components must remain serviceable;
- mature difficulty should also increase through weaker individual clues, higher interaction depth, denser plausible near-misses and, in three-slot play, richer relation topology;
- boss puzzles should primarily combine a small number of these high-cost dimensions rather than introduce a wholly new mechanic at the end;
- higher-order clue forms are allowed when they are understandable extensions of already learned grammar (for example a broader exact-one/exact-count condition or a compound conditional), but a genuinely new logical operator must not first appear only in a boss puzzle;
- the defining boss property is a short multi-stage proof in which several individually partial facts are mutually necessary and become decisive only through their interaction;
- do not equate boss difficulty with more clicks, more clues, larger-than-screened fields or compatibility-matrix filling.

Exact mature/boss clue grammar and thresholds remain design/prototype work.


### Mature clue packages must avoid pseudo-complexity

Accepted product refinement:
- do not manufacture difficulty by stacking several near-identical unary filters on the same slot (for example, several separate clues that each merely exclude one Fluid property/candidate);
- a mature clue package should create **cross-clue deductions**, not just a checklist of independent eliminations;
- an implication should not be paired with another clue that directly fixes its antecedent true, because that collapses the implication into a disguised direct consequent;
- conditional clues are strongest when the antecedent becomes relevant only after combining other partial facts, so the player must derive when/how the condition applies;
- repeated clue families are acceptable only when they participate in materially different branches or interactions, not when wording changes while logical work stays the same;
- HARD / MAX / BOSS candidates should therefore be scored not only for necessity/non-redundancy, but also for **interaction quality**: whether one clue changes how another clue can be used.

This sharpens the existing rule that late difficulty comes from interaction among mastered ideas rather than from more text or more exclusions.


### Intellectual interest is a separate quality axis from difficulty

Accepted product refinement:
- do not equate puzzle difficulty with puzzle quality;
- evaluate **intellectual interest** separately from cognitive load or nominal difficulty;
- a good investigation should preferably create at least one meaningful deduction where information changes the interpretation or usefulness of other information, producing an understandable "aha" step;
- a puzzle may be easy yet intellectually satisfying if it contains a clean non-obvious inference;
- a puzzle may be hard yet poor if it consists mainly of repetitive elimination, bookkeeping, many similar filters, or long candidate scanning;
- this criterion applies to **all** investigations, not only HARD / MAX / BOSS cases;
- later difficulty may increase interaction depth, but early/tutorial puzzles should also avoid mechanically flat clue packages when an equally clear inferential structure is available;
- generator acceptance should therefore distinguish at least:
  - difficulty / cognitive load;
  - logical validity and uniqueness;
  - brute-force attractiveness;
  - intellectual-interest / inference quality.

Exact automated scoring for intellectual interest remains open; do not collapse it into clue count or survivor count.

Clue wording preference, accepted from case-03 feedback on 2026-10-07: use lively,
natural wording while remaining crystal-clear, understandable and unambiguous.
Visible tags, counts, slot scope and logical conditions retain their exact
meaning. Liveliness must not add unstated mechanics or replace precise property
names with ambiguous flavor/metaphor. Case 03's target-specific forbidden pairing
and varied sentence roles received positive feedback; this does not by itself
prove deep inference quality.

Player calibration refinement, 2026-10-07: outside a deliberately bounded
tutorial, reject clue packages made of parallel repetitions of the same logical
form (case 02: three exact-one property counts). Rich cards, mathematical clue
necessity and a valid deductive path do not by themselves compensate for felt
repetition. Prefer conditions with distinct cognitive roles that interact;
cosmetic rewording is insufficient. This does not impose a blanket ban on any
repeated tag/operator, nor select a player-facing difficulty-label policy.
