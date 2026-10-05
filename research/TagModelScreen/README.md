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


## Adaptive architecture comparison

Run `adaptive_architecture_screen.py` against the same private three-slot JSON
corpus to compare the fixed tag-centric baseline with a knowledge-aware variant.

Example:

```
python adaptive_architecture_screen.py private.json \
  --assert-three-slot-baseline \
  --surface-samples 1024 \
  --history-samples 64
```

The screen models two deterministic knowledge-history families at 0/20/40/60/80%
of the 171 learnable adjacent Powder-Fluid / Fluid-Essence relations:

- **uniform** — arbitrary previously learned relations, used as a topology stress
  test;
- **recipe-seeded** — prior successful formulas contribute their stable adjacent
  edges first, then the remaining relation budget is filled by other learned
  relations.

For each target/history the candidate generator may use one to three invariant
target-property facts. Every individual fact is weak on the raw 3x3x3 surface
(6-8 first-stage branches). A configuration is retained only when full
compatibility knowledge would leave at most two compatible chains.

The screen reports whether a **fresh** puzzle can still be formed after known
incompatibilities are applied, how many target-property facts are needed, how
often accumulated expertise already resolves/over-directs the target, and how
large the usable candidate-surface set remains.

Important limits:

- this is a structural/existence screen, not a player-choice simulator;
- the reported number of missing target edges is a lower bound along a correct
  hypothesis branch, not a claim that a blind player selects that branch
  optimally;
- single-formula candidate surfaces are deterministically sampled by default;
  multi-formula surfaces remain exhaustive;
- exact formula rows stay in the private runtime input and are never committed.
