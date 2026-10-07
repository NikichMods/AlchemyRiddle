# Same-package Science route comparison — 2026-10-07

## Predeclared scope

Authorized follow-up to the bounded diagnostic and user's Science clarification.
Use only the retained rich three-slot package 1 whose previous zero-answer-edge
traces were 3, 11, 11. Keep field, clues, stable priors and hidden corpus fixed.
Do not expand the target sample, alter tags or implement production behavior.

Compare two public-state policies:
- existing balanced-edge rule: maximize split score, then known-edge support;
- candidate-first: prefer a live triple with the most known stable edges, keep
  investigating it until refuted/certified; within it prefer the missing edge
  shared by most live triples. Resolve equal public choices uniformly.

Replay the original three seeds and exhaust all tied policy decisions using
memoized states. Cap each policy at 200,000 states and the run at 300 seconds;
report incompleteness explicitly. Selection may use clues and earned outcomes
only; hidden truth supplies outcomes after choice, not tie-breaking or ranking.
Stop at certification even if alternative hypotheses remain.

Measure initial live triples/unknown edges/sharing/anchor support, route-length
range, mechanical uniform-tie distribution, 3/5-check coverage, and Science
cost at 2 per pair plus one 5-Science final check. These are not human success
probabilities or a shortest-path guarantee. Original traces stay frozen.

For direct submissions, use success/failure only, retain failed triple identity,
and do not infer which edge failed. Report range and average under a uniformly
random ordering of the same live triples, explicitly a comparison baseline,
not an estimate of player beliefs. Compare costs also after observed pair routes.
Exact components, tag paths and route certificates remain private outside Git.

## Results

Primary bounded execution complete: both policies have identical uniform-tie
distributions, 3–13 checks, mean 7.25. Seventeen initially unknown relevant edges
each support only one of nine live triples. Costs are 11–31 Science, mean 19.5;
uniformly ordered direct submissions average 25. Results are not human rates.

Before a second, bounded finishing sensitivity: primary replay exposes states
with a single surviving public hypothesis where certification still buys missing
edges. PRODUCT_REQUIREMENTS already permits deduction without ceremonial research.
Repeat the same two policies allowing a singleton public survivor as a reasoned
submission-ready stop. Keep primary results and distinguish deduced from chemically
certified stops. No new field, clues or outcome feedback. This tests measurement
overhead rather than relaxing the generation or product contract.

### Structural cause

Clues leave 9 of the field's 27 triples. All 18 edges on these triples are
distinct; one is a known stable prior on a wrong candidate, leaving 17 unknown
edges with sharing multiplicity exactly 1. A negative check removes one triple;
a positive check certifies part of one triple without narrowing other branches.
The two policies both finish a supported candidate, so their different seeded
paths have exactly the same uniform-tie distribution. This package supports
candidate-by-candidate chemistry rather than reusable cross-branch experiments.
The result diagnoses this package/field, not the whole tag taxonomy or real corpus.

### Costs and finishing boundary

| Stop criterion, both policies | Pair range | Uniform-tie mean | Science range including final check | Mean Science |
| --- | ---: | ---: | ---: | ---: |
| Both answer edges observed stable | 3–13 | 7.25 | 11–31 | 19.5 |
| Also stop on a unique public survivor | 3–12 | 7 | 11–29 | 19 |

In both comparisons 12.5% of mechanical tie weight resolves within 3 checks,
32.59% within 5. These are **not player success probabilities**. Primary seeded
balanced routes reproduce 3/11/11, candidate-first seeds give 8/7/6. Singleton
stopping changes the balanced seeds to 3/9/11. Thus part of the previously stated
11-check cost was avoidable certification after deduction; correcting it does
not remove the package's long-route tail or establish the user's 3–5 target.

Direct whole-triple checking costs 5–45 Science across the nine possible answer
positions. Uniformly random ordering averages 25. This baseline favors pair
research on average (19 versus 25), so 2/5 is not inherently worse than guessing
in this particular case. It does not establish balance across other packages,
player priors or Science availability.

Continuation costs can reverse that preference. For example, after six checks
on one primary route, four live triples remain: continuing that pair policy
averages another 13 Science, whereas uniformly ordered direct checking averages
12.5. At one public survivor, direct checking costs 5; buying two missing pair
observations and then submitting costs 9 and is unnecessary for deduction.
Aggregate checkpoints record costs already spent separately from future costs.
Do not enforce chemical certification when public deduction already identifies
the answer. A hybrid decision can be economically reasonable; that alone is
not blind brute force or grounds to penalize the player.

### Judgment and next step

This retained package fails to support a robust ordinary 3–5-check claim under
the tested public strategies. The long routes persist after removing ceremonial
certification and changing policy. Prefer investigating clue/field structure
before increasing Science fees or altering canonical tags. Formal interaction,
uniqueness and one short witness are insufficient generation-quality checks.

Proposed next bounded step: compare alternative clue packages already retained
on this same field for residual branch count, edge sharing and affordable public
routes. Determine whether package choice can repair the problem before changing
the candidate field or establishing a generator rejection rule. This step is
proposed, **not executed**. No new human test or production implementation.

Reproducible tooling: `research/TagModelScreen/science_route_comparison.py`.
Frozen aggregates: `research/TagModelScreen/science-routes-2026-10-07.json`, with
source/input SHA-256 identities. Exact routes remain in the private certificate
directory outside Git. Both exhaustive passes complete below the predeclared
caps; five synthetic tests cover oracle isolation, exact tie accounting, locked
candidate behavior, negative reuse and nonceremonial singleton deduction.
