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
