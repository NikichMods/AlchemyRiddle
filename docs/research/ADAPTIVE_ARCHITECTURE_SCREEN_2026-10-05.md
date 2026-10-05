# Adaptive knowledge-aware architecture screen — 2026-10-05

**Status: quantitative research. Exact vanilla formula rows remain private.**

## Question

Compare the current robust three-slot baseline:

`bounded 3x3x3 -> dosed invariant target properties -> new compatibility tests`

against the adaptive candidate:

`bounded 3x3x3 -> dosed target properties + all previously learned adjacent
relations internal to the surface -> only missing tests`.

The key uncertainty is whether accumulated compatibility knowledge makes puzzle
generation fragile, heavily answer-curated, under-structured, or routinely
pre-solved.

## Research-method checkpoint

No new runtime probe is required.

The accepted private 1.407 three-slot corpus, fixed final-reagent property model,
and `research/TagModelScreen` already contain the evidence needed for this
question. The least-assumption method is therefore to extend the existing
reproducible corpus screen rather than create another harness or ask for a new
installed-runtime capture.

Tool:
- `research/TagModelScreen/adaptive_architecture_screen.py`
- private formula input is not committed;
- accepted baseline assertion remains 19 formulas / 16 outputs / 10 x 9 x 9 /
  19 Powder-Fluid stable edges / 18 Fluid-Essence stable edges / 47 compatible
  chains.

## Screen model

The learnable adjacent-relation universe contains **171** relations:
- 10 x 9 = 90 Powder-Fluid pairs;
- 9 x 9 = 81 Fluid-Essence pairs.

A learned relation carries its actual corpus outcome, STABLE or INCOMPATIBLE.

Two deterministic history families were sampled:
1. **uniform** — arbitrary learned relations, used as a topology stress test;
2. **recipe-seeded** — previously discovered non-target formulas first
   contribute their stable adjacent edges, then the remaining knowledge budget
   is filled by other learned relations.

Knowledge densities: **0%, 20%, 40%, 60%, 80%**.

For every non-zero density, the primary run used **64 histories per target**,
or **1,024 target/history states per density**. A second history seed was also
checked as a sensitivity pass.

Candidate-surface handling:
- every surface is 3x3x3 and preserves every valid vanilla formula for the
  target;
- all multi-formula target surfaces are enumerated exhaustively;
- single-formula targets use a deterministic sample of 1,024 admissible
  surfaces each for the state cross-product;
- target facts are exact property counts invariant across the full valid-answer
  set;
- one to three facts may be used;
- every individual fact is weak on the raw field, leaving 6-8 of 9 first-stage
  branches;
- a retained fact/surface configuration must leave at most two fully compatible
  chains once the complete real compatibility graph is applied.

The adaptive UI rule under test is neutral: **all already-known adjacent
relations internal to the selected surface are surfaced**. No old relation is
selected because it is secretly useful to the target.

## Fresh versus expertise-resolved

A state counts as a **fresh puzzle** when some retained surface/fact package:
- remains unresolved after applying already-known relations;
- leaves 1-4 live Powder-Fluid branches;
- contains more than two unresolved full triples;
- does not already expose one or two fully known stable chains including a
  valid target formula.

One first-stage branch is allowed in the adaptive screen because accumulated
knowledge may legitimately earn that narrowing while several Essence
continuations remain.

A state is **expertise-covered** when either a fresh puzzle exists or the
player's accumulated knowledge already supplies a justified near-solved state.

The screen is structural, not a player-choice simulator. The number of missing
target edges is a lower bound along a correct hypothesis branch; it does not
claim that a blind player will select that branch optimally. That behavioral
question belongs in blind comparison after this screen.

## Baseline result: 0% prior compatibility knowledge

All **16 / 16** targets have a fresh bounded puzzle.

For every target:
- the best fresh package uses **two** weak invariant property facts;
- both adjacent relations of the eventual target chain are still unknown;
- therefore the intended branch contains two new compatibility facts to learn.

Across targets, the median fraction of sampled/admissible candidate surfaces
that can support a fresh closure-capable package is **67.9%**.

The worst target is a known difficult multi-formula class: **3.4%** of its
admissible surfaces work under this stricter combined property+compatibility
screen. This still corresponds to dozens of admissible surfaces, but confirms
that multi-formula targets require materially more deliberate curation than
ordinary single-formula targets.

## Adaptive result

### Uniform arbitrary-relation histories

| Known relations | Fresh states | Expertise-covered | One weak target fact among fresh states | One target edge still missing among fresh states |
| ---: | ---: | ---: | ---: | ---: |
| 0% | 100.0% | 100% | 0% | 0% |
| 20% | 94.7% | 100% | 97.6% | 38.4% |
| 40% | 81.5% | 100% | 100% | 60.7% |
| 60% | 58.8% | 100% | 100% | 76.2% |
| 80% | 29.7% | 100% | 100% | 89.8% |

### Recipe-seeded histories

| Known relations | Fresh states | Expertise-covered | One weak target fact among fresh states | One target edge still missing among fresh states |
| ---: | ---: | ---: | ---: | ---: |
| 0% | 100.0% | 100% | 0% | 0% |
| 20% | 96.8% | 100% | 96.4% | 32.5% |
| 40% | 85.9% | 100% | 99.8% | 58.2% |
| 60% | 66.5% | 100% | 100% | 75.6% |
| 80% | 36.7% | 100% | 100% | 89.6% |

The second deterministic history seed changed fresh-state rates by at most
approximately **2.2 percentage points** and did not change any qualitative
conclusion below.

## The decisive result: every lost fresh puzzle is earned expertise

Across **both history families, every tested density and every sampled
target/history state**:

> If no fresh puzzle could be formed, the player already knew **both adjacent
> stable relations of at least one valid target formula**.

There were **zero** sampled no-fresh states where one or both target-chain edges
were still unknown.

This changes the interpretation of the declining fresh-state percentages at
high knowledge density.

The adaptive generator is not becoming under-structured or failing to find a
workable field. Instead, the neutral rule "show all known relations inside the
field" makes a fresh puzzle impossible exactly when the player's prior
laboratory history has already established the complete compatibility chain of
the answer.

Hiding one of those relations merely to manufacture a new puzzle would make the
journal stop behaving as honest external memory.

## Information-budget payoff

The adaptive architecture reduces target-specific clue pressure very quickly.

At 0% knowledge, all targets need the baseline two weak target facts.

At 20% knowledge:
- 97.6% of fresh uniform-history states;
- 96.4% of fresh recipe-seeded states

can use **one** individually weak target-property fact.

At 40% and above, effectively every fresh state in the primary sample uses one
weak fact (two recipe-seeded 40% states still need two).

Likewise, accumulated compatibility reduces missing experimental work:
- no-knowledge baseline: two target-chain relations remain unknown;
- at 40% knowledge, roughly 58-61% of fresh states already know one of those
  relations;
- at 80%, roughly 90% of the remaining fresh states know one and need only the
  other.

This is the intended adaptive-budget behavior: old laboratory knowledge can
replace some target-specific clue/test burden without the system secretly
selecting only answer-helpful old facts.

## Candidate-surface curation pressure

For states where a fresh puzzle exists, the median fraction of all sampled
admissible surfaces supporting at least one fresh package remains broad:

- uniform histories: about **74% / 81% / 80% / 54%** at 20/40/60/80%;
- recipe-seeded histories: about **73% / 80% / 81% / 61%**.

The minimum observed fresh-surface fraction is still governed by difficult
multi-formula classes:
- **3.4%** at 0-20% knowledge;
- it rises rather than collapses in the higher-density samples.

Therefore the adaptive system does **not** show evidence of needing more hidden
surface cherry-picking than the baseline. The known multi-formula curation
problem remains, but accumulated knowledge does not create a new curation
failure mode in this screen.

## Architecture comparison

### Baseline tag-centric system

Still the simpler deterministic baseline:
- always supplies a fresh authored micro-puzzle;
- two weak target facts are sufficient across the corpus;
- puzzle shape is independent of discovery history;
- accumulated compatibility expertise has little formal effect on later puzzle
  generation.

### Adaptive knowledge-aware system

Passes this quantitative robustness screen:
- when the target chain is not already fully known, every sampled state has a
  fresh surface/fact package;
- target-specific clue count usually drops from two to one after modest prior
  knowledge;
- missing new compatibility work falls naturally with expertise;
- surface curation does not become more fragile;
- discovery order changes puzzle length for an intelligible reason: the player
  genuinely knows different chemistry.

Its only observed fresh-puzzle loss is the intended edge case where the player
already knows the complete target compatibility chain.

## Decision checkpoint

The adaptive architecture therefore **passes the quantitative comparison and
should be retained for blind comparison against the baseline**.

This is not yet a production-architecture selection.

The next player-facing comparison should test whether the mathematical benefit
actually feels better:
- baseline: two or more weak target constraints create the structure, with no
  old compatibility required;
- adaptive: a comparable target uses fewer target-specific clues because
  neutral previously learned relations carry part of the reasoning.

A separate expertise-saturated case should later test whether a fully pre-known
target chain feels like satisfying mastery or like the puzzle disappearing too
often. The quantitative screen says that preserving a fresh puzzle in that
state would require hiding legitimate prior knowledge or adding artificial
noise.

## Limits

This screen does not settle:
- the final production rule for selecting the 3x3x3 surface;
- exact player strategy / worst-case number of tests after choosing a wrong
  branch;
- final property wording or UI salience;
- progression-specific relation densities;
- two-slot grammar;
- experiment economy/persistence;
- the picker-incompatible exceptional success definition.

Production architecture remains **BLOCKED**.
