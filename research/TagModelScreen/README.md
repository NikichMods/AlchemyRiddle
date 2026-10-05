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


## Clue-power dosing screen

Pass `--dosing-screen` to test whether the information carried by invariant
target properties can be distributed across several individually weak facts.

Current accepted screening criteria:

**Balanced two-fact start**
- each fact alone leaves 6-8 of the 9 Powder+Fluid branches;
- both facts together leave 3-4 branches.

**Progressive three-fact start**
- each fact alone leaves 6-8 branches;
- every pair leaves 3-6 branches;
- all three leave 2-4 branches;
- every fact is necessary: removing it increases the branch count.

The report also distinguishes positive-count-only clue sets from sets that use
an absence / zero-count fact, and records how many full triples can remain
after a balanced two-fact start.

These thresholds are a research screen for clue interaction, not a production
balance contract.
