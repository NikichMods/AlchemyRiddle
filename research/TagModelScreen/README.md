# Tag Model Screen

Research-only reproducibility helper for the secondary AlchemyRiddle design branch.

The exact vanilla formula table is intentionally **not committed**. The helper
accepts a private JSON corpus at runtime and emits only structural/aggregate
metrics.

Before using results from a new tag model, run with
`--assert-three-slot-baseline`. The private ordinary 1.407 three-slot corpus
must reproduce the accepted baseline:

- 19 formulas;
- 16 outputs;
- 10 Powder candidates;
- 9 Fluid candidates;
- 9 Essence candidates;
- 810 Cartesian triples;
- 19 Powder-Fluid stable edges;
- 18 Fluid-Essence stable edges;
- 47 two-edge-compatible chains.

This converts the previous one-off calculation into a repeatable method while
preserving the project's anti-spoiler rule.

The helper does not choose product architecture. It screens whether a proposed
fixed reagent-tag vocabulary has enough information to be worth prototyping.


## Bounded 3x3x3 screen

Pass `--bounded-3x3` to enumerate every 3x3x3 candidate surface that
contains every valid formula ingredient for each output.

The bounded screen:
- preserves every valid vanilla formula for the target;
- derives only exact tag-count facts invariant across all of those formulas;
- measures whether some subset of those facts leaves 2-4 Powder+Fluid branches;
- separately tracks one-fact and positive-one-fact surfaces;
- records whether the complete invariant fact set can isolate exactly the
  target's valid formula set.

The candidate universe comes from the slot populations present in the supplied
private formula corpus. Exact formula rows remain outside the repository.
