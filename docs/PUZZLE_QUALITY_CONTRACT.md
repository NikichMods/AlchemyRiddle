# Puzzle quality — Lab calibration synthesis

2026-10-07. Status: **completed evidence synthesis; working evaluation rubric**.
Owning product direction: [PRODUCT_REQUIREMENTS.md](PRODUCT_REQUIREMENTS.md).
This operationalizes accepted principles; it does not accept production balance,
numeric difficulty bands, a universal interest score, or a new generator architecture.

The user explicitly accepts the current Lab interface as sufficient for this
research phase. Freeze discretionary UI iteration while evaluating puzzle quality.
Production implementation remains BLOCKED. No installed-runtime test is needed
for this synthesis.

## Scope and evidence strength

Ten sequential synthetic cases, one player familiar with the design discussion.
The interface, teaching, resources and authoring strategy changed between cases.
This is formative evidence, not a controlled experiment or population estimate.
Narration mixes choices, inference, UI feedback and speech-to-text name errors;
paid-action histories establish experiments, not an exact log of silent reasoning.
No reliable solve-time measurements exist. The 1–3-minute product target remains
unverified; do not time narration or development intervals as solving time.

The selected cores also have earlier paper-prototype evidence. In particular,
the post-Prototype-29 checkpoint in DESIGN_RESEARCH already accepts mixed bridge
orientations, residual answers and occasional zero-experiment reasoned solutions.
These ten Lab cases supplement that evidence; they do not restart architecture selection.

### Human outcomes

| Case | Observed route/outcome | What it supports |
| --- | --- | --- |
| [01](prototypes/PUZZLE_LAB_V0_EASY_01_RESULT.md) | Failed submission; repeated Plant wording and implication misunderstood | Revise onboarding; formal validity does not establish comprehensibility |
| [02](prototypes/PUZZLE_LAB_V0_02_STATE.md) | Correct pair independently narrated; no observed submission; rejected three parallel exact-one conditions | Repetitive cognitive work can remain boring despite necessity and successful deduction |
| [03](prototypes/PUZZLE_LAB_V0_03_STATE.md) | Tentative Fluid, derive Powder property, check overlap; one success | Accepted pleasant initial hypothesis-and-check puzzle; exhaustive elimination is unnecessary |
| [04](prototypes/PUZZLE_LAB_V0_04_STATE.md) | Independent branch rejection, revisit a prematurely dismissed branch; one success | Rich interacting tags felt inviting; remembering earlier checks imposed avoidable load |
| [05](prototypes/PUZZLE_LAB_V0_05_STATE.md) | Pair-by-pair rejection; inactive implications correctly handled; one success | Two conditional forms can be interesting when roles interact; intended compressed proof was not observed |
| [06](prototypes/PUZZLE_LAB_V0_06_STATE.md) | Three pair tests, one success | Stable anchors plus tag-guided completion/rejection accepted; historical negative priors superseded for future starts |
| [07](prototypes/PUZZLE_LAB_V0_07_STATE.md) | Three pair tests, one success; author-intent conditional shortcut | Clear observation display appreciated; shortcut is not a logically forced antecedent |
| [08](prototypes/PUZZLE_LAB_V0_08_STATE.md) | Correct tag-linked triple, no pair tests, failed synthesis and exhaustion | UI/economy-confounded failure; does not refute tag reasoning or selected puzzle core |
| [09](prototypes/PUZZLE_LAB_V0_09_STATE.md) | Five pair tests, one success; reject starting bridges and construct a new chain | Strong independent-research response; count-two welcomed |
| [10](prototypes/PUZZLE_LAB_V0_10_STATE.md) | Six pair tests, one success; explore one Powder branch, then check final clues | Larger structured surface accepted; exploratory detours tolerated; no measured boss classification |

Seven cases received explicit positive puzzle acceptance (03–07, 09–10).
There are nine observed submissions: seven successes, two failures; case 02 has
no observed submission. Three-slot successes total seventeen paid pair tests.
These are descriptive counts, not a success rate for new players.

## Reproducible structural audit

Run from the repository root:

```sh
node research/PuzzleLab/audit-calibration.mjs --write
```

[Aggregate output](../research/PuzzleLab/calibration-audit.json) records source
hashes, enumeration and historical pair-trace replay. It contains no answer tuples
and never runs in the player UI. It is not a general human solver or an interest score.

Research question: which formal properties distinguish accepted and rejected
examples, and did recorded experiments narrow target hypotheses or certify a
proposed solution? Existing frozen fixtures and rule functions answer this directly.
A small offline enumerator removes manual counting errors across ten models;
no new runtime probe, generator or reconstructed game mechanics is needed.

All ten fixtures have one valid full answer. Omitting any one clue increases the
full-model answer count in every case, including rejected 01 and 02. Thus uniqueness
and clue necessity are hygiene checks, not sufficient quality criteria.

For three-slot cases distinguish:
- **unrefuted hypothesis:** satisfies all visible tag clues and no observed negative edge;
- **certified formula:** additionally has both edges observed stable;
- **full-model answer:** satisfies clues and the hidden complete compatibility model.

| Case | Tuples in field | Tag-compatible triples | Initially unrefuted | Paid pair tests | Tests on no then-unrefuted target hypothesis | Unrefuted after pair trace | Certified after pair trace |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 06 | 27 | 7 | 4 | 3 | 0 | 2 | 1 |
| 07 | 27 | 9 | 9 | 3 | 0 | 7 | 1 |
| 08 | 27 | 5 | 5 | 0 | 0 | 5 | 0 |
| 09 | 27 | 4 | 4 | 5 | 0 | 1 | 1 |
| 10 | 64 | 7 | 7 | 6 | 3 | 6 | 1 |

Counts stop before full synthesis; failed-synthesis exclusions are not included.
Zero recorded probes in 08 is its actual failed route, not a zero-probe solution.
Positive pair results need not remove other hypotheses to be useful: they can
certify the player's candidate. Requiring the public survivor set to reach one
would incorrectly reject the accepted routes in 06, 07 and 10.

In 10, three paid pair tests lay on no triple satisfying all tag clues. They still
revealed chemical facts, but could have been avoided for this target. The observed
route ended in explicit checking of all final conditions and positive acceptance.
Do not turn this into mandatory waste, punish nonoptimal play, or label every
paid click a necessary inference. Actual spare budget allowed exploratory recovery.

In 09, every Fluid is Water. Its exact-two-Water clause therefore has one constant
term and constrains the Powder/Essence combination. The player liked the count-two
wording, but its surface arity does not prove three-variable reasoning depth.
Inspect fixed terms and semantic simplifications when evaluating future packages.

## Evaluation contract

### 1. Formal and epistemic gates

- Precommit the field, complete outcomes, clues, initial knowledge, costs and stop
  conditions. Freeze them through play. Check wording against rule semantics.
- Verify that the intended answer/valid-answer set is correct. Lab fixtures require
  uniqueness; production must respect unchanged vanilla formulas and its accepted
  target/variant scope, rather than imposing synthetic uniqueness by alteration.
- Establish each ordinary clue's contribution with an omission/branch witness.
  Redundant teaching scaffolds require an explicit pedagogical reason. A clue
  becoming unnecessary after earned observations is normal, not an authoring defect.
- Keep author-level full-graph proofs separate from what current player knowledge
  permits. UI displays earned facts; it does not perform new tag deductions.
- Record at least one legal, resource-feasible route using only public knowledge
  and observations. One successful route proves existence, not robustness across
  plausible choices; record which claim was actually checked.
- At fresh starts show stable observations only; retain every personally learned
  outcome. Cross-investigation treatment of stored negative knowledge stays open.

### 2. Positive vocabulary of useful reasoning

These are overlapping motifs, not mandatory stages or a score awarded per operator.

| Motif | Observable work | Supporting cases |
| --- | --- | --- |
| Hypothesis then consequence | A tentative component changes what another slot must contain; verify the resulting candidate | 03, 04 |
| Interacting branch rejection | A candidate passes one clue but another condition closes its continuation; reuse that conclusion | 04, 05 |
| Anchor completion | Use an observed stable edge, tag constraints and a missing-edge test to construct or reject a triple | 06, 07 |
| Reuse of negative evidence | A known failed edge closes a later proposal without paying again | 06, 09 |
| Residual construction | Starting bridges are resolved, leaving a reasoned route to an unseeded chain | 09; earlier Prototype 29 |
| Exploration then certification | Investigate a local branch, build a known stable chain and explicitly verify all target conditions | 10 |

A pleasant initial case may use a short hypothesis and one verification. Ordinary
richer cases should make facts interact or make learned outcomes change the next
useful move. A deeper mature/boss claim still needs a visible multi-stage dependency
or equivalent hard reasoning; larger fields and more paid tests cannot establish it.
Case 10 is accepted substantial exploratory play, not proof of a boss ceiling.

### 3. Repetition and author-pattern review

- Evaluate repeated **work**, not repeated words alone. Three parallel exact-one
  filters were rejected in 02; interacting implications were accepted in 05.
- Rich tags and lively exact wording support engagement but cannot repair a flat
  logical package by themselves.
- Simplify constraints under the actual field before judging depth. Record constant
  terms, immediate literals and uniquely identifiable implication endpoints.
- Review sequences for author tells: always using the antecedent, always keeping
  the answer on a starting bridge, or always making starting bridges dead ends.
  Cases 06/07 have one answer edge in initial observations; 09/10 have none.
  Both forms are supported; neither should become a promised clue to the answer.
- A starting bridge may be ruled out by tags. It must have a clear role in the
  investigation; do not fill the journal with unrelated decoration to simulate richness.

### 4. Cost and freedom of approach

Current product clarification (2026-10-07): production checks use replenishable
Science, with provisional prices of 2 per pair and 5 per whole triple, without a
per-puzzle attempt cap. Latest clarification: evaluate generator selection with
soft 3–5 pair-check preferences (about 3 lower/middle, about 5 higher intended
difficulty); two can be valid. More than about 7 is particularly undesirable,
about 10 a warning. Prefer a progressive ranking penalty, not an automatic cap.
Tutorials are separate; earned knowledge and deduction may shorten valid routes.
These are not measured guarantees, calibrated difficulty labels or mandatory minima.
Assess reasoning depth separately from check count and compare selected-package
distributions across declared targets/knowledge states before and after proposed
ranking. One fixture diagnoses a failure mode, not generator prevalence. The
route estimator, penalty weights and treatment of plausible detours remain open.
This is an additive criterion: retain existing reasoning/interest/diversity and
knowledge-aware selection. Use estimated mean **new** paid pair checks as the
primary length measure, counting both outcomes and excluding known edges. Mean
is over predeclared public policies/ties, not shortest/worst luck and not a claim
of measured player average. Compare selection on the same candidate pool before
and after the new soft term; do not replace established gates with route count.
Compare research plus final-check cost against direct guessing; distinguish
policy detours from clue/field ambiguity. See PRODUCT_REQUIREMENTS.md for ownership.
Historical Lab pools and the completed screen's 6/9 thresholds are evidence only.

- Accept a justified solution even if alternatives were not exhausted or the author
  intended another route. Do not impose a minimum experiment count for ceremony.
- Useful experiments can eliminate a live branch **or certify an uncertain edge**
  of a live candidate. Survivor-count reduction alone is not a complete metric.
- Track both an efficient feasible route and observed/plausible detours. Evaluate
  paid investigation and recovery costs; do not fit them only to an omniscient
  shortest path or treat a diagnostic threshold as an enforced attempt cap.
- Three final checks are accepted for later synthetic Lab examples. Cases 09/10
  each succeeded on the first, so they do not establish wrong-answer recovery
  quality or production economy. Pair charges and Science are separate Lab pools.
- Compare brute-force attractiveness separately. When clues leave four triples and
  three final checks are available (09), most of that residual set can be submitted
  without pair research. The user chose research; that does not prove guessing is
  unattractive in a production economy. No new fee/limit is selected by this finding.

### 5. Legibility and evidence collection

- Current Lab UI is accepted as sufficient. Stop routine polish; fix only defects
  that threaten test validity or newly authorized changes.
- Preserve the distinction between tag constraints, observed compatibility and
  final synthesis. Known pair display supports memory without certifying tag logic.
- Bottom notes/history/export removal is accepted for the Lab, not a cancellation
  of the production persistence requirement. Keep facilitator action evidence.
- Record actual decisions, skipped/misread conditions, reused evidence, useful and
  target-irrelevant probes, resource pressure and subjective satisfaction separately.
- Do not declare a calibrated difficulty band from a single subjective adjective.
  Future comparisons should hold UI, knowledge and economy fixed when possible.

## Current conclusions and remaining questions

Established for this player: the core supports pleasant short deduction and richer
empirical investigation; varied interacting conditions outperform repetitive filters;
earned pair visibility supports independent reasoning; the Lab interface is now
sufficient. Formal validity is necessary but does not predict enjoyment.

Still open: generalization to unfamiliar players, actual duration/interruption
recovery, an upper difficulty ceiling, robust budgets under multiple policies,
anti-bruteforce balance and transfer of these motifs to the fixed real corpus.
The manually authored/screened synthetic matrices and property combinations are
not evidence that the real corpus can provide the same quality on demand.

## Next bounded screen — execution specification

Execution checkpoint: [bounded diagnostic plan](research/BOUNDED_QUALITY_DIAGNOSTIC_2026-10-07.md).
Recovery, property/core input validation and the bounded pass are complete:
six real variants, 192 fields, 46,801 sampled packages and 18 reviewed certificates.
Matched flat/compound alternatives exist for this sample. Public route costs vary
substantially with starting knowledge and query choices; formal interaction alone
does not establish resource robustness. The linked report owns evidence, limits
and the completed same-package policy comparison, now recorded in
[Science route comparison](research/SCIENCE_ROUTE_COMPARISON_2026-10-07.md).
That package leaves nine triples without shared pair edges; both tested policies
retain a long-route tail after removing unnecessary certification of a singleton.
Review remaining branch structure and reusable experimental effects alongside
formal gates; do not silently accept a numeric generator rejection threshold.
No new difficulty/balance acceptance.

The latest user direction is generator-level evaluation, using soft route-length
preferences owned by PRODUCT_REQUIREMENTS.md. The single-package comparison is
diagnostic evidence only. Before another screen, declare the sampled generation
and selection process, starting knowledge, route estimator and comparison
baseline; measure selection quality/frequency rather than continue improving
one handpicked fixture. No new screen is executed by this clarification.

Reuse TagModelScreen and the accepted private corpus/property inputs; do not build
a new production generator or repeat the completed architecture/curriculum survey.
The first pass is a small diagnostic sample, not a corpus-wide coverage claim:

1. Freeze input identity, selected model and random seeds. Use the accepted core
   scope (16 two-slot / 19 three-slot variants), not all runtime outputs by assumption.
2. Choose a predeclared small sample covering simple true components, rich candidate
   fields, common/rare tags and contrasting bridge support. Report selection bias.
3. For each target, retain several contrasting valid packages where available,
   including a formally valid flat baseline. Compare with the same field/knowledge
   when isolating clue-package effects; do not rename the desired target to make it fit.
4. Emit aggregate formal gates, clause simplifications, plausible branches, initial
   knowledge, answer-edge support, feasible public-knowledge routes, budget slack
   and residual-submission attractiveness. Do not publish real recipe paths.
5. Apply this rubric to compact route certificates before commissioning more play.
   Automate rejection of proved formal failures; treat interest proxies as ranking
   evidence requiring review, not an autonomous quality oracle.
6. Stop after the declared sample/budget. Report which motifs transferred, failed,
   or remain untested, with bounded next actions. Missing private inputs are an
   explicit blocker to that screen, not permission to fabricate a synthetic corpus.

Do not launch an eleventh synthetic puzzle merely to increase the count. A new
human test should resolve a named remaining uncertainty, such as matched depth,
novice onboarding or recovery after a mistaken full synthesis.
