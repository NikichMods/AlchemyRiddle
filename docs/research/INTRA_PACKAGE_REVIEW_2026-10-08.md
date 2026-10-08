# Within-puzzle repetition and branch tracking — bounded review

Predeclared scope (2026-10-08): inspect only the frozen route-ranking pool and
the twelve retained coverage-gap packages used to select corpus case 11. No new
fields, clue search, simulation runs, UI changes or blind trial. At most 228+12
records, 60 seconds, six aggregate comparison examples. Preserve all old gates,
weak route correction and field floor. Exact source identities stay private.

Human evidence: before making an error the player already found the two symmetric
exactly-one conditions sparse and dull. After the error, the impression was that
the clues were insufficient, rather than that an assumption had been lost.
Repeated operators and same-property endpoints may impair quick scanning; this
is a hypothesis, not an established cause. Desire for a third clue is recorded,
not an accepted mechanics change.

Questions: can existing eligible packages offer different operators with similar
estimated pacing, for the same target and preferably the same field? Does a third
necessary clue inherently improve the observable burden? Do not infer that it does.

Static descriptors: repeated operator pairs; same-tag endpoints inside binary
clauses; number of slot/tag predicates shared across clauses; maximum valid
continuations after choosing one card; branches individually possible under each
clue but impossible jointly; extra tag-valid triples when one clue is forgotten.
The latter are exact structural quantities, not a human-error probability or a
validated cognitive score. Compare packages with two clues separately from three.
Reuse cached fresh/held-out route estimates; simulated policies maintain all clues.

Acceptance boundary: report availability and tradeoffs. Do not introduce a penalty,
add clues, auto-highlight violated clues or change the source model without a
subsequent owning decision. This review can suggest a soft selection preference,
but cannot calibrate its weight or establish human benefit.

## Completed result

Reviewed all 209 frozen eligible records across 19 covered targets, including the
12 extension candidates. Recomputed public tag-valid tuples, unique full-model
answer, every omission witness and field floor; all agree with cached evidence.
No fresh fields or route simulations. Source/input hashes and aggregate output:
`research/TagModelScreen/intra-package-review-2026-10-08.json`. Reproduction: run
`intra_package_review.py` with private ordinary-3.json,
generator-route-ranking-private.json, coverage-gap-private.json and public output.

Two-clue packages: 103 mixed-operator versus 92 single-operator. Three-clue reserve:
10 mixed and 4 single-operator. Only two retained records have exactly two XOR
clauses each comparing the same tag across its endpoints (the played pattern).
This is a reservoir inventory, not occurrence probability or universal badness.

For each of 19 targets, a same-clue-count repeated/mixed pair has held-out means
in 2–5 differing by at most one. Deterministically select the closest-mean pair;
aggregate means are 3.820 versus 3.861. Fields may differ. Variety is available at
close simulated pacing; this is not a controlled human difficulty comparison.

For the played target two varied alternatives meet that envelope, both with two
necessary clues on different fields. No varied alternative in the retained pool
shares the exact played field. That does not prove no such package exists:
the reservoir holds only twelve of the previously eligible packages.

| Structural descriptor | Played | Alternative A | Alternative B |
| --- | ---: | ---: | ---: |
| Necessary clues / operator kinds | 2 / 1 | 2 / 2 | 2 / 2 |
| Binary clauses with same-tag endpoints | 2 | 0 | 0 |
| Cached held-out mean pair checks | 2.969 | 3.594 | 3.609 |
| Tag-valid triples | 5 | 6 | 6 |
| Maximum continuations after fixing one card | 3 | 6 | 6 |
| Card branches individually possible per clue, impossible jointly | 0 | 2 | 2 |
| Maximum extra hypotheses if one clue is omitted | 7 | 12 | 12 |

Alternatives are more varied, but several branch-maintenance descriptors are
larger. Variety is not a proxy for easier reasoning or lower error probability.
The played package has small descriptors yet felt sparse/confusing; static
quantities miss human scanning/interpretation and cannot prevent recurrence.

Three-clue records have fewer extra hypotheses per omitted clue on average, but
differ in target/field and leave more clauses to maintain. Only 14 records; this
does not establish adding a third necessary clue repairs the played case.
A redundant clue would require an explicit teaching/scaffolding exception.

## Recommendation and next decision

Preserve hard gates and weak pacing term. Propose a separate soft preference
against the narrow double-symmetric-XOR pattern when a suitable diverse package
exists, plus explicit within-package variety review. Do not ban all repeated
operators: interacting same-family clauses have prior positive evidence.
No numeric penalty or new generator behavior accepted/implemented here.

Separate richer clue experience (direct pre-error reaction) from mistake
visibility/recovery (failed submission). Diversity alone does not solve the
second. Future contrast should test the first without claiming to fix the second.
Do not silently add a third clue, auto-checking or new feedback. Next interaction
is discussing this recommendation, not starting another blind trial by assumption.

Estimation boundary: cached ranking stops on either a certified chain or a unique
unrefuted public survivor, unlike the case-11 exact certification-only policy
distributions. Neither model includes lost constraints or misreading.

## Accepted soft preference — 2026-10-08

User accepts avoiding repeated structure within a puzzle as a soft preference,
explicitly preserving fallback when alternatives are unsuitable. Implemented in
research selection only; no production or Lab model change.

Penalty units: 0.25 for each pair of clauses sharing an operator family, plus 0.75
for each pair of symmetric XOR clauses (same tag across each clause's endpoints).
Selection adds 0.25 times those units to the existing score. A double symmetric
XOR therefore costs 0.25; other repeated-operator pairs cost 0.0625. Direction
variants of implication share a family. These are provisional implementation
weights, not human-calibrated difficulty values. No infinite penalty, exclusion,
mandatory extra clue or family ban. Existing hard gates and route strength 0.25
remain intact. Historical case-11 builder explicitly retains zero new penalty
for reproduction; played artifact is frozen.

Fixed-pool check: 209 packages, 19 targets, three orders, preferred 3 and 5,
114 selections per arm, existing cached fresh-state/held-out routes only.
Preferred-3 changes 11/57 selections: held-out mean 3.698 -> 3.755, mean repetition
units 0.180 -> 0.154; means above five 3 -> 5. Preferred-5 changes 22/57: mean
3.938 -> 3.988, repetition 0.180 -> 0.123; above-five 7 -> 7. Double symmetric
XOR selections 0 -> 0 and 1 -> 0 respectively. This is a bounded tradeoff, not
a claim every pacing/diversity metric improves. No target coverage is removed.

Same isolated case-11 target counterfactual selects a two-clue, zero-repetition
package instead of double symmetric XOR; held-out estimate 2.969 -> 3.594.
Neither a replacement blind trial nor a change to the completed trial.
Artifact: research/TagModelScreen/repetition-selection-2026-10-08.json.
Sixteen Python checks pass, including single-option fallback, preference at equal
pace, and retaining a repeated package over a much worse-paced diverse one.
Human acceptance and mistake visibility remain open; no new blind case launched.
