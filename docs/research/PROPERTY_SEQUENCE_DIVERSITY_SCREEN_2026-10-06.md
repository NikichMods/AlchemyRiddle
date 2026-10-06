# Property / sequence diversity screen — 2026-10-06

Status: **accepted bounded quantitative research; current tag model unchanged; production remains BLOCKED.**

Method:
- helper: `research/TagModelScreen/property_sequence_diversity_screen.py`;
- accepted private 1.407 formula/tag corpus; exact formulas remain private;
- two-slot late-style surface: 3x3, strict weak composite clues, unique result;
- three-slot late-style surface: 3x3x3, accepted strong progression criterion;
- 200 randomized formula-variant orders per arity;
- anti-repeat window: previous 2 investigations;
- optional decorative colour variants excluded from the mandatory progression core.

## Progression-core correction

The eight optional decorative/remodelling colour targets do **not** reserve late
difficulty and do not belong in the mandatory campaign denominator.

White and black paint remain core because they also participate in ordinary
gameplay production.

Core used by this screen:
- two-slot: **10 outputs / 16 independently researchable formula variants**;
- three-slot: **16 outputs / 19 variants**;
- total: **26 outputs / 35 variants**.

The core alone is long enough to reach late/boss difficulty in both independent
arity ladders. Optional paint research may exist as side content but must not be
required to reach the top of the curve.

## Good-surface reserve

Two-slot core, exhaustive 3x3 strict-composite good fields per variant:
- minimum **585**;
- median **844.5**;
- mean **1,008.1**;
- maximum **2,207**.

Three-slot:
- every one of the 19 variants filled a deterministic bank of **512** strong
  3x3x3 surfaces;
- the worst sampled variant needed 1,664 unique candidate surfaces to find 512
  good ones.

There is already a large structural choice reserve before anti-repetition.

## Rich-reagent bias

Distractor inclusion was normalized by how often each reagent was actually
eligible.

Average good-surface inclusion probability by property count:

| Arity | 1 property | 2 properties | 3 properties |
| --- | ---: | ---: | ---: |
| two-slot | **18.1%** | **18.8%** | **18.5%** |
| three-slot | **23.8%** | **24.3%** | **23.8%** |

Result:
**good late puzzles do not systematically depend on richer 2-3-property
reagents.**

The feared mechanism “the same rich substances must keep coming back” is not
supported.

## Sequence anti-repetition

The selector penalized only **avoidable distractor** repetition; true target
ingredients were not treated as a generator mistake.

### Two-slot — 16 core variants

Random good-surface selection:
- repeated distractor identities vs previous two puzzles: **1.76 / 4**;
- top-five distractor share: **41.7%**;
- mean consecutive surface overlap: **16.7%**;
- repeated distractor signatures: **2.55 / 4**.

Anti-repeat selection:
- repeated distractor identities: **0.071 / 4**;
- top-five distractor share: **34.0%**;
- mean consecutive surface overlap: **5.1%**;
- repeated distractor signatures: **0.60 / 4**.

### Three-slot — 19 core variants

Random:
- repeated distractor identities: **3.03 / 6**;
- top-five distractor share: **29.7%**;
- consecutive surface overlap: **19.6%**;
- repeated distractor signatures: **4.60 / 6**.

Anti-repeat:
- repeated distractor identities: **0.44 / 6**;
- top-five distractor share: **23.1%**;
- consecutive surface overlap: **6.9%**;
- repeated distractor signatures: **3.31 / 6**.

Conclusion:
- identity/material repetition is largely controllable by generator policy;
- exact **property-signature** repetition remains noticeably higher in
  three-slot play.

## Optimistic enrichment upper bound

A deliberately semantically-invalid research control modified ten shallow /
duplicate Powder-Essence identities:
- no new property labels;
- at most one extra property per modified identity;
- no identity exceeds three properties;
- goal: make repeated signatures as distinct as practical, not propose lore.

Effects:

Two-slot good-field reserve:
- minimum **585 -> 860**;
- median **844.5 -> 1,097**;
- mean **1,008.1 -> 1,226.1**.

Anti-repeat identity diversity changes very little:
- two-slot repeated distractor identities **0.071 -> 0.065**;
- three-slot **0.44 -> 0.43**;
- consecutive field overlap is effectively unchanged.

Signature repetition changes substantially:
- two-slot **0.60 -> 0.28**;
- three-slot **3.31 -> 1.77**.

## Decision

Split the original hypothesis:

1. **“Too few rich reagents force the same substances to repeat.”**
   - **Not supported.**
   - Do not add tags for this reason.

2. **“Too few distinct property signatures may make the reasoning texture
   repeat.”**
   - **Plausible and quantitatively supported enough to remain open.**
   - Enrichment nearly halves signature repetition and raises two-slot late
     surface reserve.

Do not search for real new tags yet.

## Smallest next question

Before changing the property taxonomy, test whether signature duplication
actually reduces **reasoning-path diversity**:

- distinct useful clue-family combinations;
- repeated elimination trajectories;
- repeated reliance on the same signature as decisive discriminator;
- current model versus the same optimistic enrichment upper bound.

Only if that produces a material gain should the project research real,
world-grounded extra properties and then blind-test a small matched pair.

No runtime test is required.
