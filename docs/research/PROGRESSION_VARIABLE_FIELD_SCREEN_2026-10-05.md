# Progression-limited variable-field screen — 2026-10-05

**Status: quantitative research; recipe rows remain private; production implementation remains BLOCKED.**

## Question

The accepted three-slot architecture is Adaptive Knowledge-Aware. This screen does **not** reopen that choice.

It asks the next progression/readiness question:

> Once a selected vanilla recipe variant is fully representable from the player's legitimately known reagents, how small can the bounded field become while still supporting a real deduction puzzle rather than trivial branch checking?

The screen also checks whether accumulated neutral compatibility knowledge creates new readiness gaps or mostly converts fresh puzzles into earned expertise.

## Research-method checkpoint

No new installed-runtime probe is required.

The accepted Graveyard Keeper 1.407 ordinary three-slot oracle already exists:
- 19 picker-compatible formula variants;
- 16 outputs;
- 10 Powder candidates;
- 9 Fluid candidates;
- 9 Essence candidates;
- 19 stable Powder-Fluid edges;
- 18 stable Fluid-Essence edges;
- 47 two-edge-compatible chains.

The private input was reconstructed from accepted anonymized runtime evidence and passed that exact baseline assertion before use.

The repository helper is:
- `research/TagModelScreen/progression_variable_field_screen.py`.

Exact vanilla recipe rows remain outside Git.

## Recipe-variant target semantics

Each of the 19 concrete formula rows is treated as an independent hidden research target.

This follows the accepted product decision that alternative vanilla formulas for one product can be researched as separate unresolved variants. Target-property facts are therefore evaluated against the selected hidden variant rather than forced to be invariant across all formulas for the output.

## Progression-limited known pools

A knowledge state is represented by per-slot known reagent counts `P x F x E`.

Every sampled state is conditioned on the selected hidden variant already being **representable**:
- its true Powder is known;
- its true Fluid is known;
- its true Essence is known.

The remaining known reagents are neutral distractor availability, not answer-guided unlocks.

Therefore a failure in this screen means:

> the answer is already known enough to be representable, but the current property/compatibility grammar cannot form a puzzle that clears the tested quality bar from that particular known pool.

It is **not** permission to hard-gate the target. The accepted product contract still forbids blocking merely because irrelevant distractors are missing.

## Candidate-field floor used by the screen

The progression pool mode only considers candidate surfaces with at least **two candidates in every slot**.

This deliberately keeps `2x2x1` and other one-candidate-slot shapes outside the candidate production-quality envelope: such a surface directly gives away one exact component and was already identified as a likely triviality risk.

This is an operational research floor, not yet a final product balance decision.

The generator may choose any contained surface up to 3 candidates per slot:
- 2x2x2;
- 2x2x3 and permutations;
- 2x3x3 and permutations;
- 3x3x3.

Either adjacent orientation may carry the first-stage branching:
- Powder-Fluid; or
- Fluid-Essence.

This avoids making a shape look artificially weak merely because an earlier screen always measured Powder-Fluid first.

## Two clue-quality bars

### Legacy-scaled comparator

The earlier 3x3x3 rule required every individual target fact to leave 6-8 of 9 first-stage branches.

The mechanical variable-field translation is:

`ceil(2B/3) .. B-1`

for raw branch count `B`.

This is retained as a comparator because it preserves the old weakness ratio exactly.

### Compact candidate bar

Small fields have coarse branch granularity. On 2x2 first-stage branching, an informative fact often changes 4 branches directly to 2 or 3; requiring it to leave exactly 3 branches can reject otherwise coherent compact puzzles for a purely arithmetic reason.

The compact candidate bar therefore requires an individual target fact to:
- be informative;
- leave at least 2 first-stage branches;
- leave more than 2 full triples;
- not identify the target by itself.

Up to three non-redundant facts may be combined.

A retained package must:
- keep the true variant alive;
- leave a bounded hypothesis space;
- have at most two chains under complete real compatibility knowledge, so adjacent compatibility plus final synthesis can close the investigation;
- with no prior compatibility knowledge, leave 2-4 live first-stage branches and more than two full triples.

This bar is deliberately less restrictive about **how weak one clue must be**, not about whether deduction/compatibility work remains.

## Main result: 2x2x2 is a credible floor candidate, not a universal guarantee

The complete 2x2x2 knowledge-pool population is small enough to enumerate exhaustively.

Across all **10,944** representable `2x2x2` known-pool states:
- compact-bar service rate: **95.815%**;
- worst individual recipe-variant service rate: **89.931%**;
- every served 2x2x2 state uses the 2x2x2 surface itself;
- the successful compact packages are overwhelmingly one target-property fact followed by compatibility/identity reasoning.

This is a strong result, but not 100%.

Therefore:
- 2x2x2 is quantitatively plausible as the earliest normal three-slot puzzle size;
- it cannot yet be made the unconditional production minimum solely from this screen;
- the remaining approximately 4.2% of representable 2x2x2 states need a graceful fallback rather than an artificial readiness gate.

## One extra known candidate almost closes the remaining gap

Deterministic sampled known-pool runs used 64 states per recipe variant for the larger count classes, or 1,216 states per class.

Compact-bar observed service rates:

| Known pool | Served | Worst variant | Variants served in every sampled state |
| --- | ---: | ---: | ---: |
| 2x2x2 | ~95.8% | ~82.8% in this sample | 5 / 19 |
| 2x3x2 | ~99.4% | ~96.9% | 15 / 19 |
| 3x2x2 | ~99.8% | ~98.4% | 17 / 19 |
| 3x3x2 | 100% | 100% | 19 / 19 |
| 3x3x3 | 100% | 100% | 19 / 19 |

The sampled 2x2x2 row is consistent with the exact exhaustive 95.815% result; the exact worst-variant figure is the exhaustive 89.931%, not the smaller-sample value.

The selected field also naturally grows with available knowledge:
- at 2x2x2 knowledge, only 2x2x2 is available;
- at 2x3x2 / 3x2x2, the generator overwhelmingly retains the larger 12-triple shape;
- at 3x3x2, the 18-triple shape dominates;
- at 3x3x3, 3x3x3 dominates, with smaller fallbacks used only where they score better.

This is the desired progression-sensitive direction: early knowledge can produce a compact puzzle; broader knowledge permits a richer field instead of merely padding the same puzzle.

## Why the legacy ratio should not define the small-field floor

Using the mechanically scaled old weakness rule on the same pool model sharply reduces service:
- 2x2x2: roughly **30%** in the sampled comparator;
- 2x3x2: roughly **86%**;
- 3x3x3: roughly **99.5%**.

This does **not** show that early alchemy is intrinsically unsolvable.

It shows that the old 6-8-of-9 clue-dosing ratio was calibrated to a nine-branch field and does not transfer cleanly to four-branch fields. Small-field clue granularity is coarser.

Therefore the old ratio remains useful as a 3x3x3 reference/comparator, but should not silently become the production definition of an "interesting" early puzzle.

## Prior compatibility knowledge does not create a new readiness problem

A second sampled pass applied neutral previously learned adjacent relations internal to the known pool at 0%, 25%, 50% and 75% density.

Representative compact-bar results:

### 2x2x2

Coverage stayed approximately **96.6%** in the sampled bank across all densities.

The composition changed:
- 0% relations: ~96.6% fresh puzzles;
- 25%: ~77.0% fresh + ~19.6% expertise-resolved;
- 50%: ~26.2% fresh + ~70.4% expertise-resolved;
- 75%: ~2.6% fresh + ~93.9% expertise-resolved.

### 2x3x2

Coverage stayed approximately **99.2%**:
- 0%: ~99.2% fresh;
- 25%: ~92.6% fresh + ~6.6% expertise;
- 50%: ~61.8% fresh + ~37.3% expertise;
- 75%: ~9.2% fresh + ~90.0% expertise.

### 3x3x3

Coverage remained **100%** in the sampled bank:
- 0%: 100% fresh;
- 25%: ~96.9% fresh + ~3.1% expertise;
- 50%: 75.0% fresh + 25.0% expertise;
- 75%: ~29.1% fresh + ~70.9% expertise.

Interpretation:

> accumulated compatibility knowledge mostly changes **fresh puzzle -> earned expertise**, rather than **researchable -> blocked**.

This is consistent with the earlier accepted Adaptive Knowledge-Aware architecture result.

Important limit: these are neutral internal-relation samples, not a claim about one canonical Graveyard Keeper playthrough chronology.

## Hard-gate implication

This screen materially narrows the hard-readiness problem.

If a true recipe component is still unknown, the accepted hard gate remains legitimate.

If the selected recipe variant is already fully representable:
- 3x3x2 / 3x3x3 knowledge is structurally enough in the sampled compact screen;
- 2x3x2 / 3x2x2 is very nearly enough;
- 2x2x2 is usually enough but has a real minority of gaps.

Therefore the product should **not** use "insufficient alchemical knowledge" merely because one of those representable compact states fails the current scorer.

The remaining representable-gap fallback should be investigated among:
- a slightly stronger but still non-oracular target fact;
- a compact presentation that uses a different information orientation;
- another bounded target-specific evidence form.

Requiring an irrelevant reagent discovery remains rejected.

## Minimum interesting-puzzle checkpoint

Quantitative conclusion:

- **2x2x1 and other one-candidate-slot shapes:** keep below the current candidate quality floor.
- **2x2x2:** promote to **minimum-floor blind-test candidate**.
- **2x3x2 / 3x2x2:** strong compact shapes and likely safe fallback/richer early shapes.
- **3x3x2 / 3x3x3:** quantitatively robust under the current grammar.

The unresolved question is now experiential, not structural:

> Does a well-formed 2x2x2 adaptive puzzle still feel like "I worked this out", or does it feel too close to short enumeration compared with a matched 2x3x2 case?

That cannot be answered honestly by another corpus statistic alone.

## Exact next step

Run a blind matched paper-prototype pair using the accepted Adaptive Knowledge-Aware semantics:

1. one **2x2x2 compact** investigation;
2. one matched **2x3x2 (or symmetric 3x2x2)** investigation.

Keep target/property/compatibility semantics as comparable as practical and measure:
- whether 2x2x2 produces a real inference before testing;
- whether residual hypothesis checking feels justified rather than enumerative;
- meaningful new experiment count;
- working-memory burden;
- preference between the compact and slightly richer field;
- whether 2x2x2 should become the production minimum floor or remain fallback-only.

A separate later case should test a representable 2x2x2 state from the small quantitative gap and compare graceful fallback options.

No installed-runtime test is required from the user.

Production implementation remains **BLOCKED**.
