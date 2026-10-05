# Two-slot tag-constraint capacity screen — 2026-10-06

**Status: accepted quantitative research for Candidate A; production remains BLOCKED. Exact vanilla formula rows remain private.**

## Question

Can the already accepted fixed final-reagent property vocabulary support a
two-slot puzzle in which the player combines several partial tag constraints to
infer a Powder/Fluid pair, rather than receiving the answer through a
compatibility oracle?

The screen tests **information capacity and clue interaction**, not final wording
or player enjoyment.

## Evidence / corpus controls

Private input was reconstructed from the accepted Graveyard Keeper 1.407
AlchemyRiddle runtime corpus evidence and the accepted fixed-tag assignment.

The two-slot corpus reproduces all accepted structural controls:

- 24 ordinary two-slot formula variants;
- 18 outputs;
- 4 multi-formula outputs;
- maximum 3 formulas for one output;
- 15 distinct first-slot participants;
- 9 distinct second-slot participants;
- 23 / 24 formula variants have another ordinary formula at Hamming distance 1.

The exact named tier-I formula table was cross-checked against the accepted
anonymized runtime formula graph. The graphs are isomorphic with the same
multiplicity/neighbor structure; exact formula rows are not persisted here.

The tag vocabulary is the accepted fixed eight-property model documented in
`docs/DESIGN_RESEARCH.md`.

## Screened candidate fields

For every concrete vanilla two-slot recipe variant, the helper exhaustively
enumerates every target-containing field of these shapes:

- 2x2;
- 2x3;
- 3x2;
- 3x3.

A formula variant is treated as the selected hidden research target, consistent
with the accepted recipe-variant policy.

The reported `surface_instances` are target-variant/field instances, not a
claim that production should select fields uniformly at random.

## Clue grammars

### Simple

- slot-local target-true presence / absence;
- exact total count of one tag across the pair.

### Composite

Includes the simple grammar plus:

- cross-slot XOR / exact-one-of-two;
- active cross-slot implication with a positive or negative consequent.

Implication antecedents must be true on the hidden target. A clue is never
counted merely because the target satisfies it vacuously.

These are logical predicates for capacity screening, not accepted final
player-facing sentences.

## Information-shape rules

Only 2- or 3-clue sets are retained.

Every selected clue must be:
- true of the hidden target;
- individually partial under the current weakness policy;
- non-redundant: it must eliminate at least one candidate that the other
  selected clues would leave alive.

Resolution categories:

- `unique_2` — unique pair after two clues;
- `unique_3` — unique pair after three clues;
- `residual2_2` / `residual2_3` — exactly two clue-consistent pairs remain;
- `none` — no qualifying bounded result.

Unique resolution is preferred over the two-candidate residual fallback.

Two clue-strength policies are reported:

- **strict** — each clue alone leaves `ceil(2V/3)..V-1` candidates, preserving
  the earlier three-slot weak-clue ratio;
- **compact** — each clue alone leaves `max(2, ceil(V/2))..V-1`, allowing the
  coarser information granularity of small onboarding fields.

Neither is yet a production balance constant.

## Compact-policy result

### Simple grammar only

| Field | Surface instances | Unique | At most 2 survivors | Variants with any unique field | Worst per-variant unique-field rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2x2 | 2,688 | **91.1%** | **91.1%** | **24/24** | **75.0%** |
| 2x3 | 9,408 | **65.2%** | **95.3%** | **24/24** | **44.4%** |
| 3x2 | 17,472 | **59.2%** | **95.5%** | **24/24** | **41.2%** |
| 3x3 | 61,152 | **7.5%** | **76.5%** | **21/24** | **0.0%** |

Interpretation:
- very small two-slot fields already have substantial deductive capacity using
  only simple fixed-tag constraints;
- 2x2 is especially strong as an onboarding shape: composite logic adds no
  capacity under this criterion because simple clues already solve the useful
  information partitions;
- 2x3 and 3x2 remain broadly serviceable with simple clues;
- 3x3 exposes a real ceiling: simple clues often narrow well but rarely isolate
  the exact pair.

### Composite grammar

| Field | Surface instances | Unique | At most 2 survivors | Variants with any unique field | Worst per-variant unique-field rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2x2 | 2,688 | **91.1%** | **91.1%** | **24/24** | **75.0%** |
| 2x3 | 9,408 | **88.0%** | **96.7%** | **24/24** | **64.3%** |
| 3x2 | 17,472 | **83.1%** | **98.6%** | **24/24** | **63.5%** |
| 3x3 | 61,152 | **79.5%** | **96.6%** | **24/24** | **53.8%** |

The composite vocabulary therefore provides **real additional information
capacity**, not just wording variety:

- 2x3 unique coverage rises from 65.2% to 88.0%;
- 3x2 rises from 59.2% to 83.1%;
- 3x3 rises from 7.5% to 79.5%;
- all 24 formula variants have at least one uniquely solvable field at every
  screened shape under the composite grammar.

The 3x3 result is especially important: compound logical relations appear to
be a plausible later-two-slot difficulty layer rather than something needed to
make the first tutorial work at all.

## Strict weak-clue stress test

The strict policy deliberately refuses any clue that removes more than one
third of the field by itself.

### Simple grammar

No field shape reaches a unique answer with 2-3 qualifying simple clues.

However, simple clues can still reach exactly two survivors on:
- 57.4% of 2x3 field instances;
- 47.2% of 3x2;
- 72.4% of 3x3.

This is useful negative evidence: under a deliberately weak-clue budget, simple
facts alone tend to narrow rather than finish.

### Composite grammar

| Field | Unique | At most 2 survivors | Variants with any unique field |
| --- | ---: | ---: | ---: |
| 2x2 | **0.0%** | **64.3%** | 0/24 |
| 2x3 | **74.9%** | **91.9%** | **24/24** |
| 3x2 | **61.8%** | **87.5%** | **24/24** |
| 3x3 | **36.6%** | **75.4%** | **24/24** |

Thus the composite result is not an artifact of allowing very strong compact
clues. Even when every individual clue is constrained to be weak, 2x3, 3x2 and
3x3 all support unique 2-3-clue solutions for every formula variant on at least
one candidate field.

The 2x2 failure under the strict policy is expected geometry: demanding that
each clue leave at least 3 of 4 candidates gives almost no room for a short
unique deduction. The compact 4 -> about 2 -> 1 shape is a more plausible
tutorial criterion and must be tested perceptually rather than rejected on
formal purity.

## Main conclusion

**Candidate A passes the quantitative capacity screen strongly.**

The existing natural fixed-tag vocabulary does not need artificial tag
inflation to make ordinary two-slot recipes support short deduction.

The evidence suggests a particularly coherent progression:

1. **early 2x2:** simple tag conditions are sufficient;
2. **2x3 / 3x2:** simple conditions still work, while composite conditions add
   substantial variety and robustness;
3. **later 3x3:** composite XOR/implication-style clues become genuinely useful
   for reaching a unique answer rather than merely adding linguistic flavour;
4. **two-survivor fallback:** remains broadly available, but should stay a
   secondary resolution shape rather than the ordinary goal.

This is unusually well aligned with the desired two-slot -> three-slot
pedagogy: the player can first learn tag intersection on small fields, then
learn richer logical relations, and only later add STABLE/INCOMPATIBLE
compatibility bridges in three-slot alchemy.

## What this does not prove

The screen does not establish:

- that the clue sentences feel natural in blind play;
- that the answer-aware candidate-field selection is acceptable in every
  progression state;
- which exact clue families belong in the tutorial;
- final UI wording or visualization;
- whether 2x2, 2x3 or 3x2 should be the ordinary early field size;
- progression-specific reagent availability;
- that Candidate A should be selected before the remaining two-slot
  solution-space families are compared.

Production remains **BLOCKED**.

## Reproducibility

Helper:
`research/TagModelScreen/two_slot_tag_constraint_screen.py`

Research branch:
`research/two-slot-tag-constraint-screen`

Exact vanilla formula rows remain private/ephemeral input. The helper's
`--assert-two-slot-baseline` gate verifies the accepted structural fingerprint
before reporting results.
