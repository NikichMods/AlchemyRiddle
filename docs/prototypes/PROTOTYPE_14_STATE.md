# Prototype 14 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before the player's first Prototype 14 action.

## Purpose

Test a spoiler-safe progression slice based on the accepted Life Powder -> Heal Potion -> Glue anchors without revealing any real vanilla formula.

The core under test is a minimal hybrid of:
- world-grounded provenance/property evidence;
- cross-slot relational deduction;
- comparison against already-known mixtures as an analytical reference.

The prototype must answer whether the player feels they are choosing and interpreting an experiment, rather than purchasing another clue or scanning one slot.

## Spoiler boundary

All reagent names and hidden formulas below are fictional/isomorphic test data. They are deliberately not the real formulas for Heal Potion or Glue.

The player may be told that the test is spoiler-safe and structurally represents the accepted 2-slot / 3-slot progression states. Do not expose this file or the hidden answers during blind play.

## Universal player-visible rule

1. Every known reagent has one or more **origin marks** recorded in the substance compendium:
   - Plant
   - Insect
   - Mineral
   - Corpse
2. Two components are **related** if their origin-mark sets overlap by at least one mark.
3. A 2-component formula has one pair/relation.
4. A 3-component formula has three unordered pairs/relations:
   - Powder–Liquid
   - Liquid–Essence
   - Powder–Essence
5. A **comparison experiment** compares the unknown target with one already-known reference mixture and reports only how many pair-relations have the same related/unrelated state.
   - 2-slot result range: 0–1.
   - 3-slot result range: 0–3.
6. The comparison never reports which pair matched and never reports exact ingredient correctness.
7. Initial target research may provide aggregate origin facts, including which origin marks occur somewhere in the formula and how many components carry a specified mark. It never assigns an origin mark to a slot unless explicitly stated.
8. The substance compendium is external memory: it may show reagent marks and known-reference relation diagrams, but it must not enumerate surviving formulas or perform the player's fresh deduction.

## Prototype economy

To isolate puzzle quality from reagent-burn friction:
- comparison experiment: costs 1 Research Charge;
- each stage starts with 3 Research Charges;
- a comparison does not consume the real candidate reagents;
- final synthesis consumes one selected reagent per slot;
- Research Charge production recipe/economy is outside this prototype and must not be inferred as accepted product design.

A failed final synthesis only proves that exact attempted formula is not valid for the target. No extra goo semantics are used in Prototype 14.

## Stage 0 — reagent-information onboarding

This is not a blind deduction puzzle.

Progression role:
- the early Life-Powder-like need introduces reverse, goal-first reagent research;
- completing that research populates/updates the substance compendium with legitimate source/origin information;
- the player is not expected to remember provenance from ordinary gameplay.

Prototype 14 assumes this onboarding has already happened and the four origin marks are understood.

## Stage 1 — two-slot tutorial analogue

Represents the accepted Heal-Potion progression shape without using the real formula.

### Candidate pool

Powders:
- P-A **Growth Powder** — {Plant}
- P-B **Swarm Powder** — {Insect}
- P-C **Slate Powder** — {Mineral}

Liquids:
- L-A **Root Solution** — {Plant, Corpse}
- L-B **Swarm Solution** — {Insect}
- L-C **Stone Solution** — {Mineral, Corpse}

### Initial target profile

The unknown target:
- contains the Plant mark somewhere;
- contains no Mineral mark;
- contains exactly two distinct origin marks across the whole formula.

### Known reference

Reference R-2:
- relation state: RELATED (its two ingredients share at least one origin mark).

### Hidden valid answer

- P-A + L-B.
- Its relation state is UNRELATED.

### Deterministic comparison outcome

Compare target to R-2:
- 0 / 1 relation states match.

### Resolution

Under the visible candidate pool + initial target profile:
- before comparison, exactly two formulas satisfy the aggregate profile;
- their single relation states differ;
- after the comparison result, exactly one formula remains logically possible.

The facilitator must not state this deduction before the player does.

If the player explicitly derives the unique formula, the stage may resolve without a ceremonial craft. If the player chooses to craft, the hidden answer succeeds and all other pairs fail.

## Stage 2 — three-slot main test analogue

Represents the accepted Glue progression shape without using the real formula.

### Candidate pool

Powders:
- P1 **Sprout Powder** — {Plant}
- P2 **Carapace Powder** — {Insect}
- P3 **Slate Powder** — {Mineral}

Liquids:
- L1 **Cocoon Solution** — {Insect, Plant}
- L2 **Root-Mineral Solution** — {Mineral, Plant}
- L3 **Shell Solution** — {Insect, Mineral}

Essences:
- E1 **Shell Essence** — {Insect, Mineral}
- E2 **Pollen Essence** — {Insect, Plant}
- E3 **Gravebloom Essence** — {Corpse, Plant}

### Initial target profile

The unknown target:
- contains exactly these origin marks somewhere in its three components: Plant, Insect, Mineral;
- contains no Corpse mark;
- the Mineral mark occurs in exactly one of the three components.

These facts are aggregate and do not identify a slot.

### Hidden valid answer

- P1 + L1 + E1.

Hidden relation triangle:
- Powder–Liquid: RELATED;
- Liquid–Essence: RELATED;
- Powder–Essence: UNRELATED.
Signature: 110.

### Candidate-state invariant

Applying only the initial target profile to the complete 3x3x3 pool leaves seven valid formula hypotheses.

Their relation signatures are:
- 110: 1 formula (the hidden answer);
- 111: 3 formulas;
- 011: 2 formulas;
- 010: 1 formula.

Do not show this enumeration or signature-count table to the player unless they independently derive equivalent hypotheses.

### Known references

Reference R-A **Ash Elixir**
- relation signature: 000
- player UI may show this as three UNRELATED pair-lines.

Reference R-B **Root Elixir**
- relation signature: 100
- player UI may show Powder–Liquid RELATED, the other two pairs UNRELATED.

These are known references; their relation diagrams are player-visible external-memory facts.

### Deterministic comparison outcomes for the hidden target

Against R-A (000):
- 1 / 3 relation states match.

Against R-B (100):
- 2 / 3 relation states match.

### Why reference choice is non-equivalent

Given the initial-profile-valid hypothesis set:

R-A partitions formula hypotheses by returned score into groups of sizes:
- score 0: 3
- score 1: 3
- score 2: 1

R-B partitions them into:
- score 0: 2
- score 1: 4
- score 2: 1

Neither reference is a universally dominant button:
- R-A has the better worst-case partition;
- R-B isolates a different structural hypothesis and, for the actual hidden target, yields the unique 110 signature immediately.

If the player uses R-A first, the actual result leaves the target relation signature ambiguous between 110 and 011; R-B then distinguishes them.
If the player uses R-B first, the actual result identifies signature 110 among the initial-profile-valid hypotheses.

The facilitator must not state these deductions before the player does.

### Resolution

Because signature 110 occurs only once among formulas satisfying the initial target profile, once the player has legitimately established 110, the formula is logically unique and the stage may resolve immediately without requiring a ceremonial synthesis.

If the player attempts synthesis earlier:
- P1 + L1 + E1 succeeds;
- every other combination fails and consumes the selected reagents.

## Player-facing state requirements

At every decision:
- show target arity;
- show all candidate reagents by slot and their origin marks;
- show initial target-profile facts;
- show known reference mixtures and their relation diagrams;
- show remaining Research Charges;
- show comparison history/results;
- distinguish established facts from the player's stated hypotheses;
- list legal actions:
  - compare against a known reference (1 Research Charge);
  - attempt final synthesis with selected candidates.

Do not list surviving formulas automatically.

## Evaluation questions after Stage 2

Record:
- whether the relation rule was understandable without repeated rereading;
- whether the reference choice had a reason the player could articulate;
- whether a comparison felt like an experiment or like buying a clue;
- whether known formulas felt meaningfully useful;
- whether combining aggregate origin facts with relation evidence felt like deduction;
- whether the triangle of three pair relations was too much working memory;
- whether final resolution avoided the Prototype 13 slot-scan failure;
- desired resource cost / number of comparisons;
- overall subjective rating and comparison with Prototype 13 / Prototype 10.

## Integrity rule

The hidden answers, profiles, reference signatures, outcomes and resource model above are immutable for this blind run. If any missing rule materially affects reasoning, stop and start a new prototype rather than improvising.


## Live blind-play checkpoint — Stage 1, after first player action

Player feedback before acting:
- the term **related / родственные** was not immediately legible; the player reread the rule and struggled to form a mental model;
- “the reference elixir's two components are related” was initially ambiguous: the player wondered whether they were related to each other or to the unknown target;
- “matching relation state” also felt abstract/heavy;
- the player correctly reconstructed the intended semantics only after effort;
- action choice felt nearly forced: compare against the only reference or synthesize essentially at random.

Clarification given by facilitator:
- “related” means two ingredients **within the same formula** share at least one origin mark;
- the known reference's two ingredients are related to each other;
- comparison checks whether the unknown formula's pair has the same yes/no relation state as the reference.
This is a rephrasing of the precommitted rule, not a new mechanic.

Player action:
- compare the unknown 2-slot target against reference R-2 for 1 Research Charge.

Deterministic raw outcome:
- **0 / 1 relation states match**.

Resource state:
- Research Charges remaining: 2 / 3.

Journal:
1. Compare target vs R-2 (reference pair RELATED) -> 0/1 relation states match.

No fresh deduction has been performed by the facilitator. Await the player's interpretation.


## Live blind-play checkpoint — Stage 1, first synthesis attempt

Player interpretation / UX feedback before synthesis:
- player initially experienced the 0/1 comparison result as almost no information;
- player explicitly questioned why the composition of the already-known reference elixir was not shown in the interface;
- this exposes a presentation flaw: if known-formula comparison is supposed to make accumulated knowledge useful, the interface should show the known reference formula / visible reagent marks and let the player see why its relation state follows, rather than presenting only a precomputed “RELATED” label;
- player began enumerating candidate pairs from the aggregate target profile and described the intended next action as going through the possibility matrix in order;
- player proposed Growth Powder + Root Solution as the first synthesis candidate.

Facilitator correction before resolving the action:
- Growth Powder {Plant} and Root Solution {Plant, Corpse} share Plant, so their pair relation is RELATED;
- the prior raw comparison result was 0/1 against a RELATED reference, so this proposed pair already conflicts with the established comparison observation.
This correction uses only pre-existing rules/observations after the player stated their inference; it does not add a new clue.

Player action still treated as the explicitly selected synthesis:
- Growth Powder + Root Solution.

Deterministic raw outcome:
- **failure**.

Resources/state:
- Research Charges remain 2 / 3;
- selected synthesis reagents are consumed for this prototype attempt.

Journal:
1. Compare target vs R-2 (reference pair RELATED) -> 0/1 relation states match.
2. Synthesis Growth Powder + Root Solution -> failure.

Do not identify the remaining unique formula for the player. Await their interpretation.


## Live blind-play checkpoint — Stage 1 completion

Player clarified their interpretation of the comparison rule:
- they understood the reference as carrying a **specific shared origin identity** (for example Corpse+Corpse);
- they therefore interpreted 0/1 as excluding that specific shared-origin pattern only, while still allowing some different shared-origin pattern such as Plant+Plant;
- this differs materially from the precommitted rule, where comparison checks only the boolean relation state RELATED vs UNRELATED, independent of *which* origin mark creates the overlap.

This is strong evidence that the abstraction “same relation state” is not naturally legible from the current wording / mental model. The player constructed a more specific and arguably more intuitive semantic than the intended one.

Player next action:
- synthesize Growth Powder {Plant} + Swarm Solution {Insect}.

Deterministic raw outcome:
- **exact success**.

Stage 1 resolution:
- fictional 2-slot target obtained;
- meaningful actions: 1 comparison, 2 synthesis attempts;
- Research Charges remaining: 2 / 3.

Observed Stage 1 design findings:
- the reference comparison was initially experienced as nearly information-free because the player interpreted it as matching a specific shared property rather than generic overlap state;
- showing only a precomputed reference relation label hid the known formula knowledge that was supposed to make the reference meaningful;
- the player naturally drifted toward candidate-pair enumeration;
- after clarification, the intended boolean relation rule can eliminate a class of pairs, but the representation is not yet intuitive enough to trust as a tutorial grammar.

Do not yet assign final Prototype 14 disposition; Stage 2 remains the main 3-slot test.
