# Rare search through unchanged selection and held-out routes — 2026-10-10

## Question and method

User accepts the next check of reserve 64: does extra rare-candidate reserve
survive ordinary selection without concentrating motifs or lengthening routes?
The preceding search-only comparison established candidate recovery, not this
downstream effect. No extra rare-selection bonus is used here.

The existing search comparison did not persist complete retained pools. This
follow-up reconstructs its 12 paired baseline/reserve-64 pools using the same
shared proposal helper, unchanged gates and independent retention seeds. All
prior counters, family incidences, target coverage, mask counts and retention
aggregates match exactly in all 24 cases. This is stronger than matching only
mean candidate counts; it is not a byte comparison to previously absent pools.
Full reconstructed pools and selections are now frozen privately for continuation.

New code is only orchestration/recovery of that comparison. It reuses the accepted
`select_sequence`, `selection_score`, `Investigation`, frozen-spec evaluator and
metrics; no new selection/route model. Independent frozen-spec replay checks all
2,256 distinct retained packages for their tag-valid triples, unique compatible
answer and necessity of each clue. Package identity was also counted from
target/surface/clue specifications, independently of in-memory object identity.

Predeclared matrix: 12 search seeds x 12 target orders x starting knowledge of
0/1/4 globally stable pairs x preferred means 3/5 x search reserves 0/64.
Each arm contains 864 simulated sequences and 15,264 selected target steps.
Orders repeat the same 19 targets; these are dependent comparisons, not 864
independent corpora. Unchanged route and structural-repetition strengths are
0.25. Quality gates and recurrence preferences are unchanged.

Route estimation uses the existing two public-information policies with 16
seeds per policy for selection; independent 32 seeds per policy evaluate fixed
choices. Stops include unique public survivor, not mandatory certification of
both pairs. Cached results depend on public survivor triples and starting
knowledge, not condition wording. There are 3,282 public contexts and 315,072
route replays. Pool reconstruction and route estimation each have six-minute
caps. All 36 research unit tests pass; the full matrix completes.

Aggregate: `research/TagModelScreen/rare-search-selection-2026-10-10-v1.json`.
Exact target/ingredient identities and selected paths remain outside Git.

## Results

| Starting knowledge / preference | Shared selections, baseline -> 64 | Held-out mean pair checks, baseline -> 64 | Selected means above 5, baseline -> 64 |
| --- | ---: | ---: | ---: |
| None / 3 | 46 -> 76 | 3.552 -> 3.539 | 50 -> 50 |
| None / 5 | 28 -> 61 | 3.956 -> 3.961 | 213 -> 212 |
| One known pair / 3 | 47 -> 76 | 3.494 -> 3.477 | 46 -> 44 |
| One known pair / 5 | 31 -> 59 | 3.880 -> 3.880 | 196 -> 197 |
| Four known pairs / 3 | 51 -> 73 | 3.159 -> 3.150 | 35 -> 31 |
| Four known pairs / 5 | 36 -> 63 | 3.499 -> 3.487 | 171 -> 178 |

Each row has 2,544 selections per arm. Shared selections increase from 239 to
408 overall: 1.57% -> 2.67%. The selector does not select every available rare
opportunity: availability rises from 72 to 120 target steps per setting, while
actual selections remain 59..76 with reserve 64. This demonstrates reserve
benefit under the existing selector rather than compulsory rare content.

Mean family entropy improves in all six settings by 0.018..0.029 bits; mean
distinct family count per sequence also increases in all six. Individual paired
sequences can lose entropy. Adjacent exact abstract-semantic repeats remain zero
in both arms. Maximum same-template occurrence rises in six paired sequences
(all in four-known-pair settings) and falls in four; the maximum full semantic
occurrence anywhere is still two in both arms. Family overlap between neighbours
has mixed small changes, so recurrence is not universally improved.

Overall held-out mean is 3.590 -> 3.582 checks. Five settings improve; fresh
preferred-5 increases by 0.005 checks. No selected package has held-out mean
above 7 in either arm; individual simulated detours may still exceed 7. The
four-known/preferred-5 tail above mean 5 grows from 171 to 178 of 2,544 despite
lower overall mean (about 0.28 percentage-point increase). Individual sequence
mean changes range roughly -0.607 to +0.407 checks. Do not call these results
strict dominance or zero cost.

## Decision implication and limits

Recommend reserve 64 as the next working research search policy, with unchanged
ordinary selection and no added rarity bonus. Evidence supports a modest
candidate-search intervention; strengthening final weights is unnecessary for
the observed downstream gain. The small tail/repetition tradeoffs do not justify
another scoring mechanism on this evidence. Adoption is recommended, not silently
performed: accepted main builders and weights remain unchanged in this commit.

These are mechanical proxies, not measured human interest or human mean route
length. Rare packages still arise from one target/field and four survivor masks.
At most one rare target occurs per sequence, so repeated rare-motif campaign
clumping is not stress-tested. Multiple rare families have a synthetic helper
test, but comparative corpus evidence here concerns only shared property.
Opportunity prior cutoff and transfer to other fields/availability states remain
experimental; do not turn this sample into permanent production rarity weights.

The next user-owned decision is whether to adopt the small search reserve as
research baseline. If accepted, connect the tested helper to main research pool
generation and verify it through that path, retaining gates, selection weights,
bounded total budget and ordinary fallback. Broader field/campaign evidence and
human playtests remain required before production claims. No new puzzle fixture,
network-playtest edit or vanilla behavior change. Solved case 20 preserved;
production remains BLOCKED.
