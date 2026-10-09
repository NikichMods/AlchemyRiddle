# Bounded rare-family search comparison — 2026-10-10

## Question and predeclared comparison

User accepts testing extra search attention for available rare condition families,
not a mandatory rare clue or final puzzle quota. Hypothesis: replacing a bounded
part of ordinary package proposals with rare-containing pairs recovers usable
reserve at the same attempt budget, without materially narrowing other families.
The preceding exact audit located shared-property loss in proposal search.

Comparison constants were set before running: 512 attempts per searchable field;
reserves 0, 64 and 128; 12 paired proposal seeds. Frozen fields are the accepted
152-field main sample over 19 ordinary three-slot targets; 65 fields meet the
unchanged minimum floor. Each arm consumes 399,360 attempts in total, including
duplicates and unsupported ordinary package sizes. This is equal attempt budget,
not measured equal wall time or equal predicate-evaluation count.

Previously frozen opportunity evidence defines rare roots by the same bounded
coverage prior used in the earlier rarity comparison: positive prior means
coverage below one quarter of targets in the training witnesses. Only `shared`
currently qualifies (2/19 training targets); this cutoff remains experimental.
The mechanism handles any set of rare roots, not a hard-coded shared-property
branch. Only two searchable frozen fields have shared available.

On those fields, the reserved draws choose an available rare root uniformly,
then a concrete predicate within it, then a uniformly sampled different predicate
as partner. Partners are sampled by concrete predicate, not root family; this
local bias is explicit and bounded by the reserve. These proposals contain two
clues; unchanged necessity, answer, interaction and ordinary-quality gates decide
whether they are usable. Other proposals remain family-first two/three-clue
draws. Missing rare roots fall back exactly to ordinary sampling.

Proposal and reservoir randomness are separate. The ordinary proposal stream is
consumed even on replaced attempts, so the remaining paired proposals are
identical. Reservoir remains uniform, capped at 12 candidates per target.
This is a controlled comparison, not exact replay of the old coupled RNG stream;
its baseline counts therefore differ from the preceding 504-package replay.

## Results

Aggregate evidence: `research/TagModelScreen/rare-search-2026-10-10-v1.json`.

| Reserved attempts / field | 0 | 64 | 128 |
| --- | ---: | ---: | ---: |
| Shared-containing eligible packages, total over 12 runs | 14 | 25 | 35 |
| Mean distinct shared predicate-mask packages per run | 1.17 | 1.67 | 2.00 |
| Shared-containing retained candidates, total | 7 | 16 | 20 |
| Runs retaining at least one shared candidate | 6/12 | 10/12 | 9/12 |
| Mean eligible packages of all kinds | 547.83 | 546.33 | 545.83 |
| Mean retained candidates of all kinds | 200.42 | 200.50 | 200.50 |

Other-family eligible incidence across all runs, baseline -> reserve 64:
literal 1969->1963; count 2369->2357; XOR 3610->3595; positive implication
1616->1604; negative implication 1200->1194; mixed count 2450->2453.
Family counts overlap, since a package can contain multiple families.
Every other family's eligible target coverage is identical in every paired run.
Total served-target counts are also identical: 17 or 18 of 19 depending on seed.
No quality gate was relaxed. This does not prove unchanged retained target
coverage per family, route suitability or final-player sequence diversity.

Reserve 64 replaces only 1,536 of 399,360 attempts across these runs because
rare availability is narrow. It reduces mean eligible package count by about
0.27%, while increasing retained rare opportunity availability. Reserve 128
finds more rare candidates, but uniform retention still loses all of them in
three runs; the smaller reserve does so in two. These are paired observations
on a small fixed field sample, not confidence estimates or universal optima.

Independent frozen-spec replay checks all 74 rare witness occurrences (12 unique
packages), reproducing predicate masks, unique complete-model targets and
necessity of each clue. Exact witnesses remain outside Git. Aggregate replay:
`research/TagModelScreen/rare-search-replay-2026-10-10-v1.json`.
All 36 research tests pass, including equal-budget/unchanged-tail, exact fallback,
multiple-rare-root attention and invalid-budget tests.

## Interpretation and next decision

The limited hypothesis is supported: focused search can recover rare candidates
without a larger attempt budget or excluding other condition types. Recommend
reserve 64 as the next experimental candidate rather than increasing the reserve
or final bonus. The accepted main generator remains unchanged; no default search
policy or weights are adopted by this comparison.

The recovered packages still come from one target/field and the same four
tag-survivor masks established by exhaustive audit. Twelve packages are not
twelve demonstrated different player experiences. Multiple rare roots have a
synthetic mechanics test, but only one rare root has real-corpus comparative
evidence here. Broader field/corpus transfer and BepInEx readiness remain open.

Next useful check: send the reserve-64 retained pool through the unchanged
sequence selector and independently seeded route validation. Hypothesis: the
additional reserve survives actual selection without concentrating one motif
or lengthening investigation routes. If supported, consider adopting the small
search reserve; if not, inspect retention/selection before raising search effort.
No new player fixture, network-playtest change or production behavior. Solved
case 20 is preserved. Production remains BLOCKED.
