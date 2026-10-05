# Tag clue-power dosing screen — 2026-10-05

**Status: quantitative research. Exact vanilla formula rows remain private.**

## Question

Can the already accepted fixed final-reagent property model be **power-dosed**
inside a bounded 3x3x3 candidate surface?

The desired shape is not "one strong fact nearly solves the puzzle." Instead,
several simple facts should each be weak in isolation and become useful mainly
through conjunction.

The screen therefore tests clue interaction rather than minimum clue count.

## Corpus / baseline

The private ordinary three-slot corpus reproduces the accepted structural
baseline:

- 19 formulas;
- 16 outputs;
- 10 first-slot candidates;
- 9 second-slot candidates;
- 9 third-slot candidates;
- 810 unrestricted triples;
- 19 Powder-Fluid stable edges;
- 18 Fluid-third stable edges;
- 47 two-edge-compatible chains.

Every enumerated 3x3x3 surface preserves all valid vanilla formulas for its
target. The same **372,008** admissible surfaces from the bounded-property
screen are evaluated.

Target facts remain restricted to exact property counts that are invariant
across the complete valid-formula set for that output.

## Screen A — balanced two-fact start

Criterion:

- each property fact alone leaves **6-8** of the 9 Powder+Fluid branches;
- the conjunction of the two facts leaves **3-4** branches.

This means neither clue may eliminate more than one third of the first-stage
branch space by itself.

### Result

**16 / 16 outputs pass.**

Across all admissible surfaces:
- **245,562 / 372,008 = 66.0%** support at least one such two-fact clue set;
- per-output surface coverage ranges from **7.94%** to **81.03%**;
- median per-output coverage is **69.03%**.

Thus balanced clue power is not merely possible through one exceptional
hand-picked surface. For most outputs it is available across a large fraction
of legal 3x3x3 fields.

### Positive-count-only variant

If both facts must have positive counts, such as "Plant x1" rather than
"Mineral x0":

- **14 / 16** outputs pass;
- the two failures are both multi-formula output classes.

The two remaining classes pass the ordinary two-fact criterion when one
absence/zero-count fact is allowed.

This is compatible with the already-discussed clue language, which explicitly
allows statements such as "no Mineral."

## Residual full-triple space

The balanced two-fact criterion does not have to over-solve the third slot.

For **all 16 / 16 outputs**, there is an admissible surface and balanced
two-fact clue set that leaves:

- **4 Powder+Fluid branches**;
- **12 complete triples**.

Therefore the property layer can be tuned to structure the first-stage search
while deliberately leaving the Essence/continuation layer almost entirely for
compatibility and later experiments.

This is strong evidence that property clues and compatibility can carry
different parts of the deduction rather than redundantly revealing the same
answer.

## Screen B — progressive three-fact start

A stricter screen tests whether three property facts can form a genuinely
progressive conjunction.

Criterion:

- each individual fact leaves **6-8** branches;
- every two-fact conjunction leaves **3-6** branches;
- all three facts leave **2-4** branches;
- every fact is necessary: removing any one fact must increase the branch
  count.

### Result

**14 / 16 outputs pass.**

Across all admissible surfaces:
- **135,042 / 372,008 = 36.3%** satisfy the strict three-fact criterion;
- among the 14 covered outputs, per-output coverage ranges from **9.36%** to
  **51.40%**;
- median coverage among covered outputs is **39.00%**.

The two failures are the same difficult multi-formula classes. Under the
current simple invariant vocabulary they have too little independent invariant
structure to support a strict three-property chain without redundancy or an
over-strong intermediate clue.

That is not evidence that they need finer artificial properties. Both already
pass the balanced two-fact screen and can receive their next deduction step
from compatibility.

### Positive-count-only three-fact variant

With zero-count facts disallowed, **11 / 16** outputs pass the strict
three-fact screen.

This reinforces that absence facts are not merely cosmetic; they contribute
real orthogonal information in the current natural vocabulary.

## Example shape from the real corpus

Without identifying the target or its formula, one real admissible field has
three positive invariant facts with this branch trajectory:

- start: **9** Powder+Fluid branches;
- fact A alone: **7**;
- fact B alone: **6**;
- fact C alone: **6**;
- pair intersections: **5 / 4 / 4**;
- all three facts together: **3**.

The facts in that hidden example are ordinary natural properties, not synthetic
solver labels.

This is the desired qualitative pattern: no clue is close to an answer, but
their overlap creates a compact hypothesis set.

## Interpretation

The answer to the research question is **yes**.

The fixed natural property vocabulary is not merely powerful enough; its power
can be **distributed**:

1. candidate-surface selection establishes a bounded working field;
2. two or three individually weak target facts can cross-constrain that field;
3. the property conjunction can be stopped deliberately at 3-4 first-stage
   branches and a much larger set of complete triples;
4. compatibility can then provide the relational deduction step instead of
   serving as cleanup after the tags already solved everything.

The two-fact result is universal across the ordinary three-slot corpus under
the tested 3x3x3 convention. The richer three-fact pattern is available for
14/16 outputs and should be treated as an optional richer shape rather than a
mandatory template.

## Design consequence

Do **not** optimize future puzzle generation for minimum clue count.

A more appropriate target is a controlled information trajectory, for example:

- starting first-stage branches: 9;
- each individual property clue: about 6-8;
- property conjunction: about 3-4;
- compatibility / microtests: further discriminate those branches;
- full intended research may eventually reach a unique valid formula.

The exact numeric thresholds are not yet production balance constants. They are
evidence that the natural tag system has enough headroom to create the richer
cross-constraint experience requested by the product.

## Still open

This screen does not decide:

- the final candidate-surface selection policy;
- whether a specific puzzle should use two or three starting property facts;
- final wording / visual presentation of absence facts;
- how many compatibility observations should be pre-known vs discovered;
- two-slot puzzle grammar;
- progression-specific availability.

Production architecture remains **BLOCKED**.
