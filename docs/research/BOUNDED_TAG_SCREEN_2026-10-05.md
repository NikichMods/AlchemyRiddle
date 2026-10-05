# Bounded 3x3x3 fixed-tag screen — 2026-10-05

**Research result; spoiler-sensitive formula rows are not persisted.**

## Question

Given the already accepted fixed final-reagent property model, does a bounded
3x3x3 candidate surface provide enough information diversity for the ordinary
three-slot Graveyard Keeper 1.407 corpus?

The desired initial envelope is **2-4 Powder+Fluid branches** after target
property information. Every candidate surface must preserve **all** valid
vanilla formulas for its output.

## Method

The screen uses the accepted private ordinary three-slot corpus and first
re-validates the structural baseline:

- 19 formulas;
- 16 outputs;
- 10 first-slot candidates;
- 9 second-slot candidates;
- 9 third-slot candidates;
- 810 unrestricted positional triples;
- 19 Powder-Fluid stable edges;
- 18 Fluid-third stable edges;
- 47 two-edge-compatible chains.

For every output, the screen exhaustively enumerates every 3x3x3 surface whose
three slot sets contain the ingredients required by **every** valid formula for
that output.

Target property facts are limited to exact counts that are invariant across the
output's complete valid-formula set. Zero-count exclusions are allowed, but are
reported separately from positive counts.

For every surface, the screen measures:
- the minimum number of invariant property facts whose surviving triples occupy
  2-4 distinct Powder+Fluid branches;
- whether a single **positive** property-count fact can do so;
- what remains after applying all invariant property facts;
- whether all invariant facts isolate exactly the valid vanilla formula set.

The exact formula rows remain private/ephemeral.

## Exhaustive surface population

The ordinary three-slot corpus contains:
- 13 outputs with one valid formula;
- 3 outputs with two valid formulas.

A single-formula output has **28,224** admissible 3x3x3 surfaces in the current
10x9x9 structural universe.

The three multi-formula output classes have 1,568 / 1,764 / 1,764 admissible
surfaces depending on how their alternative formulas share slot ingredients.

Total enumerated surfaces across the 16 outputs: **372,008**.

## Primary result

**All 16 / 16 outputs have at least one valid 3x3x3 surface where a single
invariant property-count fact leaves 2-4 Powder+Fluid branches.**

This upgrades the earlier full-field result:

- unrestricted 10x9x9 field: only **11 / 16** outputs can reach <=4
  Powder+Fluid branches using the fixed natural property vocabulary alone;
- bounded 3x3x3 field: **16 / 16** can enter the intended 2-4 branch envelope
  with **one** invariant fact, for at least one admissible surface.

For **15 / 16** outputs, that one-fact result can use a positive count such as
"property X appears N times."

The remaining output is a multi-formula class where the sole useful one-fact
route requires a zero-count / absence statement. Its available positive
invariant by itself does not reach the 2-4 branch envelope in any admissible
3x3x3 surface.

## Robustness: single-formula outputs

For the 13 single-formula outputs, this is not a fragile cherry-picked
existence result.

The fraction of all admissible 3x3x3 surfaces where **one** invariant property
fact reaches the 2-4 branch envelope ranges from:

- minimum: **61.6%**;
- median: **92.7%**;
- maximum: **100%**.

For every one of the 13 single-formula outputs, at least one surface plus one
fact can leave exactly:
- 3 Powder+Fluid branches;
- 3 surviving full triples.

Therefore the fixed property layer is broadly strong enough to shape ordinary
single-formula three-slot puzzles without requiring a uniquely engineered
distractor set.

## Robustness: multi-formula outputs

The three two-formula output classes are materially more sensitive to candidate
selection.

The fraction of admissible surfaces where one invariant fact reaches the 2-4
branch envelope is:

- **1.8%** for the weakest class;
- **27.8%** for another;
- **44.0%** for the strongest.

Allowing up to two invariant facts raises those respective reachable-surface
fractions to:

- **44.6%**;
- **35.7%**;
- **86.5%**.

Thus all three multi-formula outputs have many workable surfaces, but candidate
curation is much more important than for single-formula outputs.

This is a useful design distinction rather than a failure of the property
model.

## Residual ambiguity after all invariant property facts

All 13 single-formula outputs have at least one 3x3x3 surface where the complete
invariant property set isolates exactly the one valid vanilla formula.

Among the three multi-formula outputs:
- one class has a surface where all invariant properties isolate exactly its
  two valid formulas: **2 branches / 2 triples**;
- one class can do no better than **2 branches / 3 triples**;
- one class can do no better than **4 branches / 4 triples**.

Therefore **14 / 16** outputs can, in principle, be made property-complete
inside some 3x3x3 surface, but **2 / 16** retain unavoidable false candidates
under the current invariant property vocabulary.

Those two residual ambiguity classes are particularly strong evidence for the
second relational layer: compatibility can resolve ambiguity that should not be
papered over by inventing finer, less-natural properties.

## Aggregate sanity check

Across all 372,008 admissible surfaces, weighting every surface equally:
- **86.2%** reach the 2-4 branch envelope with one invariant fact;
- **99.1%** do so with at most two facts;
- **99.36%** do so with some subset of the invariant facts.

This weighted aggregate is dominated by the 13 single-formula outputs and
should not replace the per-output robustness analysis above.

## Design consequence

The fixed type-level natural property model **passes the bounded-field
information-sufficiency test**.

This is deliberately narrower than saying the resulting puzzle is already
well-shaped. The screen minimizes clue count, so it rewards strong one-fact
reductions. It does not test whether the preferred player experience instead
uses several individually weak constraints whose conjunction creates the
deduction path. Candidate-surface selection itself is also an information
source.

Current evidence supports this shape:

1. a deliberately bounded 3x3x3 field provides the coarse search-space limit;
2. one small invariant target-property clue is normally enough to shape that
   field into 2-4 meaningful first-stage branches;
3. compatibility provides the relational/experimental layer that resolves
   remaining ambiguity and creates the interesting deduction;
4. there is no current evidence-based need to make the property taxonomy finer
   merely to manufacture more unique signatures.

Do not expose the complete property vector by default merely because it can
solve many single-formula targets. The desired clue budget remains adaptive and
partial.

## What remains open

This screen does not decide:
- the production rule for selecting one admissible 3x3x3 surface;
- how much answer-aware curation is acceptable;
- the exact final player-facing wording/boundaries of the property vocabulary;
- two-slot puzzle grammar;
- progression-specific availability;
- how prior compatibility observations are selected/presented.

The next separate foundation question can now move to the ordinary two-slot
corpus using the same fixed type-level property model.

Production architecture remains **BLOCKED**.
