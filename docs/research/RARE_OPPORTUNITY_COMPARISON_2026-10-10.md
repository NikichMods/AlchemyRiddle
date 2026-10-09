# Rare-opportunity preference — bounded frozen-pool comparison

Predeclared question: can a small scarcity preference improve rare-opportunity
use without reducing sequence diversity or degrading suitable routes? Research
only; accepted weights/defaults and production remain unchanged.

Reuse the exact 199-package family-first ranking pool and stored independent-seed
route validation. Estimate scarcity from target coverage in the three earlier
family-first witness passes, not output frequency. No new corpus/field/puzzle.
Those passes share the corpus but use different fields from the ranking pool;
this is not independent-corpus validation.

For each observed family: prior = max(0, 1 - coveredTargets / (19/4)). Unknown
families get zero. This quarter-coverage cutoff is an experimental, not accepted
product value. Bonus strength 0/.25/.5/1/2 times the maximum applicable prior,
never summed across rare families. Disable a family's bonus if it appears in
either of the last two selected puzzles. Existing recurrence/quality/route scores
stay active. No quota and no force-selection gate; untested curriculum overrides
are not claimed implemented.

Use 12 fixed target orders: original three plus nine additional orders; fresh,
one and four globally known stable relations, preferred routes 3 and 5. Baseline
must exactly reproduce existing selector at strength zero. Report all arms;
do not choose weight from rare frequency alone. Inspect major-family presence,
entropy of family incidences, adjacent overlap, semantic-template repetitions,
and held-out route mean/tails. Entropy is an abstract distribution diagnostic,
not player enjoyment. One encounter per target/order cannot validate long-term
repeated-target play; focused synthetic checks cover recent-bonus suppression.

Tool: `rare_opportunity_screen.py`; reusing frozen estimates avoids new probes
and property/corpus extraction. Dedicated comparison code is needed only to
add the experimental score and sequence metrics. All output is aggregate;
no exact recipes/predicates are published. No blind example opened.

## Completed results and limits

All 360 sequence comparisons complete: six knowledge/pace settings, twelve
orders, five bonus strengths. Each sequence selects 18 packages; the same 199
candidate pool is used throughout. Observed target opportunity coverage:
literal/count/XOR/mixed count 18, positive/negative implication 17, shared property
2 of 19. Only shared property receives a positive experimental prior (11/19);
this estimate comes from finite searches, not exhaustive feasibility.

At strength .25 the actual maximum score discount is about .145. Compare shared
package selection counts per twelve sequences, each with one encounter per target:

| Global known stable relations | Preferred route | No bonus | Small bonus .25 |
|---|---:|---:|---:|
| 0 | 3 | 11 | 11 |
| 0 | 5 | 7 | 10 |
| 1 | 3 | 10 | 10 |
| 1 | 5 | 8 | 10 |
| 4 | 3 | 10 | 10 |
| 4 | 5 | 10 | 11 |

Across these settings: 56 to 62 shared selections out of 1296 total selections;
the same rare candidate is involved, not six newly discovered templates.
For the usual fresh preferred-3 setting the existing selector already uses
11 of 12 opportunities, and tested strengths up to 2 do not change that result.
Stronger bonus is therefore not justified as a remedy in that setting.

At .25 all setting-average family entropy values are unchanged or improve;
paired audits show no sequence increases its maximum abstract-semantic-template
repeat count, and no adjacent identical semantic template appears. Adjacent
family overlap slightly rises in one setting and falls in another; overlap of
families is not identity of complete templates. Seven families remain present
in pooled selections. These measures support a bounded diversity benefit,
not a claim about player enjoyment or universal campaign diversity.

Held-out mean pair checks are unchanged or slightly lower in every setting.
However fresh preferred-5 selected-mean-above-5 share rises from 20/216 (9.26%)
to 21/216 (9.72%): a downstream sequence tradeoff despite lower mean. One-known
preferred-5 share falls from 18/216 to 17/216. No selected mean above seven.
Do not hide this tail change behind a favorable average. These are sampled
mechanical routes, not measured human solve times or calibrated difficulty bands.

The .5/1 arms give 65 shared selections, strength 2 gives 70. All arms are
reported in `rare-opportunity-2026-10-10.json`; no default weight chosen from them.
Calibration is limited by a single rare package in the ranking reservoir and
only two opportunity-bearing targets in the supporting searches. It cannot
evaluate a rich variety of rare templates or repeated demand for one product.

## Verification

32 research tests pass, including five new checks for bounded/non-stacking bonus,
recent exposure suppression, target rather than package-frequency calibration,
unfavorable-route preservation and JSON semantic-key restoration. Strength-zero
replay matches the existing selector in all settings/orders; the original three
orders also exactly reproduce the retained historical selection records.
`rare-opportunity-audit-2026-10-10.json` records changed choices and paired
repeat/tail checks. The small bonus changes 50/1296 choices in total, including
downstream changes caused by sequence history, not just the six extra rare picks.

A preliminary commentary associated an existing semantic repeat with the bonus;
paired audit disproved that interpretation. No increased template repetition
was found. The actual observed tradeoff is the small route-tail change above.

## Recommendation

Keep the accepted principle, but do not install a fixed calibrated weight yet.
The experiment shows modest useful opportunity compensation while recurrence
guards stay active. In the normal fresh preferred-3 setting there is almost no
missed opportunity left for a bonus to repair. Improving the number of distinct
rare candidates is a more informative next question than increasing the bonus.
Proposed next bounded audit: determine whether rare eligible packages are lost
before final selection (field search/reservoir retention), preserving current
quality gates. Its result would distinguish search/retention work from ranking
tuning. This next audit is not already executed or an accepted retention policy.

Implementation is comparison-only in an isolated research worktree/branch.
Main selection weights, family-first sampler, fixtures, UI and network-playtest
work are untouched. Production remains BLOCKED.
