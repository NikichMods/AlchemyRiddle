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


## Progression-aware variable-field screen

Run `progression_variable_field_screen.py` against the same private three-slot
JSON corpus after the adaptive architecture has been selected for further
research.

Examples:

```
python progression_variable_field_screen.py private.json --mode shapes
python progression_variable_field_screen.py private.json --mode relations --histories 64 --seed 20261005
```

This screen changes two assumptions from the earlier 3x3x3 work:

- each concrete vanilla recipe variant is an independent hidden research target;
- the candidate field may use 2 or 3 candidates per slot rather than always
  using 3x3x3.

The branch metric is orientation-neutral. A puzzle may begin from either adjacent
pair (Powder-Fluid or Fluid-Essence); this avoids treating a permutation such as
2x2x3 as intrinsically weaker merely because an earlier research metric always
started from Powder-Fluid.

The single-fact weakness rule scales the accepted 3x3x3 threshold rather than
inventing a new one: on a raw first-stage branch count B, a fact is weak only
when it leaves from ceil(2B/3) through B-1 branches. For 3x3 this reproduces the
accepted 6-8-of-9 rule exactly.

Two research tiers are reported:

- **strong** — after one to three individually weak, non-redundant target facts,
  2-4 first-stage branches and at least four full triples remain, while complete
  compatibility knowledge leaves at most two chains;
- **thin-or-better** — the same screen with a three-triple floor, used to expose
  the boundary where a mathematically ambiguous field may already feel like
  short branch checking.

These are screening tiers, not a selected production balance contract. In
particular, a thin result still requires blind player testing before it can be
called an acceptable puzzle.

`--mode relations` samples neutral previously learned adjacent relations
internal to prevalidated strong fields. It reports whether the same field remains
strong, becomes thin, or becomes legitimately near-resolved by prior expertise.
Exact formula rows remain private.


### Progression-limited known-pool mode

The variable-field helper also has a \`pools\` mode. Unlike the surface-only
existence screen, this conditions each recipe variant on a concrete set of
currently known Powder / Fluid / Essence reagents and asks whether the generator
can construct a usable contained field.

Examples:

\`\`\`
python progression_variable_field_screen.py private.json \
  --mode pools \
  --pool-criterion compact \
  --pool-counts "2,2,2;2,3,2;3,2,2;3,3,2;3,3,3" \
  --pool-samples 128 \
  --relation-density 0

python progression_variable_field_screen.py private.json \
  --mode pools \
  --pool-criterion compact \
  --pool-counts "2,2,2;2,3,2;3,3,3" \
  --pool-samples 64 \
  --relation-density 0.5
\`\`\`

Every known-pool state is conditioned on the selected hidden recipe variant
being fully representable: all three true components are included in the known
pool. A \`gap\` result therefore means the current puzzle grammar could not form
an acceptable field from available distractors; it is **not** evidence that the
target should be hard-gated.

Two clue criteria are available:

- \`legacy\` mechanically scales the old 3x3x3 weak-fact ratio
  (\`ceil(2B/3)..B-1\`);
- \`compact\` allows the coarser granularity of small fields while still
  requiring each single target fact to leave at least two first-stage branches
  and more than two full triples.

The compact criterion is a research candidate, not a production balance
contract. Its current aggregate results and limitations are documented in
\`docs/research/PROGRESSION_VARIABLE_FIELD_SCREEN_2026-10-05.md\`.


## Two-slot tag-constraint screen

Run `two_slot_tag_constraint_screen.py` against a private two-slot corpus to
measure whether the accepted fixed reagent properties can support the proposed
early-game tag-constraint grammar without committing vanilla formula rows.

Example:

```
python two_slot_tag_constraint_screen.py private-two-slot.json \
  --assert-two-slot-baseline
```

The private input contains only ingredient tag sets and exact two-slot formula
rows. The baseline assertion reproduces the accepted ordinary tier-I structure:

- 24 formula variants;
- 18 outputs;
- 4 multi-formula outputs;
- at most 3 formulas for one output;
- 15 first-slot participants;
- 9 second-slot participants;
- 23 / 24 formula variants have another ordinary formula at Hamming distance 1.

The helper exhaustively screens 2x2, 2x3, 3x2 and 3x3 candidate fields that
contain the selected hidden formula variant.

Two clue grammars are compared:

- **simple** — slot-local target-true presence/absence plus exact pair tag
  counts;
- **composite** — the simple grammar plus cross-slot XOR/exact-one-of-two and
  active cross-slot implications with positive or negative consequents.

Implications whose antecedent is false on the hidden target are deliberately
excluded, so a target never satisfies an implication only vacuously.

Two clue-strength policies are reported:

- **strict** — every clue alone leaves `ceil(2V/3)..V-1` candidates, preserving
  the earlier three-slot weak-clue ratio;
- **compact** — every clue alone leaves `max(2, ceil(V/2))..V-1` candidates,
  allowing the coarser granularity of small onboarding fields.

A retained 2- or 3-clue set must be non-redundant: every clue has to eliminate
at least one candidate that the other selected clues would leave alive.
Resolution categories distinguish:
- unique answer in two clues;
- unique answer in three clues;
- exactly two residual candidates after two or three clues;
- no bounded result.

Exact formula rows remain private and are never printed.


## Curriculum serviceability screen

Run `curriculum_serviceability_screen.py` after the current property model and
progression core have been selected.

The private inputs are deliberately filtered to:
- 16 mandatory two-slot formula variants / 10 outputs;
- 19 ordinary three-slot formula variants / 16 outputs;
- the accepted Dark + Organ property assignment.

Example:

```
python curriculum_serviceability_screen.py TWO_CORE.json THREE_CORE.json
```

The screen asks whether **a player-selected target formula** can still serve the
desired curriculum beat. It does not let the scheduler choose another target.

Two-slot:
- exhaustively checks 2x2 fields;
- tests BREATHE/simple packages plus low-load introductions of XOR, forward
  positive implication, forward negative-consequent implication and reverse
  implication direction;
- includes a deliberately over-strict exact-2-of-4 clue-split sensitivity
  control to expose failures caused by unnecessary generator constraints.

Three-slot:
- exhaustively checks Prototype-35-like 2x2x2 first-relation tutorial surfaces;
- reuses the accepted reasoning-diversity option generator to measure later
  major-family capacity per target.

Only aggregates are emitted. Exact formula rows remain private.

Important limits:
- this is formula-identity serviceability, not a complete save-state simulator;
- progression-limited known identities and accumulated learned relations can
  still force runtime generation fallback;
- later bridge/residual relation-topology concepts remain a separate question.

## Bounded quality diagnostic and input recovery

`recover_private_inputs.py` reconstructs private screen inputs from the exact
accepted local asset hash and probe-0.2.0 capture. It uses UnityPy 1.25.4 for the
asset container, verifies narrow candidate joins against complete runtime rows,
and checks properties against the canonical assignment. Derived inputs must be
written outside the repository. It is not a complete GameBalance parser.

`bounded_quality_diagnostic.py TWO_CORE.json THREE.json PRIVATE_CERTIFICATES.json
AGGREGATES.json` runs the declared six-variant/192-field diagnostic using existing
clue predicates. Exact selections/certificates stay private; public output contains
only hashes, structural measures and policy-route summaries. Query policies see
public hypotheses and observations; outcomes are consulted only after selection.

Specification/results: `docs/research/BOUNDED_QUALITY_DIAGNOSTIC_2026-10-07.md`.
Frozen aggregate artifact: `bounded-quality-2026-10-07.json`. These results are not
an autonomous interest score, a production economy or corpus-wide quality coverage.
Run focused route-policy checks with:

```
python -m unittest discover -s research/TagModelScreen -p test_bounded_quality_diagnostic.py
```

`science_route_comparison.py THREE.json PRIVATE_CERTIFICATES.json
PRIVATE_ROUTES.json AGGREGATES.json` compares the two public policies on one
frozen package, exhaustively accounting for tied choices with memoized states.
It also compares singleton-deduction stopping and 2/5 Science costs. Exact
certificates/output stay outside Git. No new corpus sample or production behavior.
Plan/results: `docs/research/SCIENCE_ROUTE_COMPARISON_2026-10-07.md`;
aggregates: `science-routes-2026-10-07.json`. Uniform mechanical tie/order weights
are not human probabilities. Tests: `test_science_route_comparison.py`.
