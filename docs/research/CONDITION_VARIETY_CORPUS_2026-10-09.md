# Condition-variety corpus comparison — 2026-10-09

## Predeclared question and method

User authorizes checking whether the two connected forms supply useful reserve
on the verified real corpus. Reuse the accepted 19 ordinary three-slot variants,
full ingredient availability, eight seeded 3x3x3 fields per target, unchanged
weak-clue, field-floor, unique-answer, necessity and ordinary-quality gates.
No production generator, weight change, clue-strength relaxation or blind play.

Existing route-ranking tool includes unnecessary route/selection experiments for
this question. A bounded helper reuses its exact gates and existing enumerator,
adds only paired-pool filtering, anchored draws and aggregate bookkeeping.

Two paired arms: old families versus expanded families, 512 attempts per field
per arm, identical fields and draw seeds. Larger pools can dilute sampling;
do not assume baseline packages are preserved by equal-effort random selection.
Separate diagnostic arms: 256 attempts anchored on each available new family
per field. These use additional effort and establish reserve, not a fair-budget
performance gain. Report available clues, eligible packages, target/field
coverage and rejection counts. No quota forcing new forms into selected puzzles.

Predeclared seed 20261009; three-minute cap. Stop with an explicit incomplete
result if cap reached. Store exact fields, predicates and witnesses privately;
public output contains aggregates and input/source hashes only. Historical
evidence stays unchanged. Player interest and mean experiment cost unmeasured.

## Completed results

Pass complete in 5.515 seconds, all 19 targets / 152 fields. Corpus SHA-256
matches the accepted input identity `92e140826b6b8c857bb994df71b5db83d3da2ed15a9cc4665db474ea8876ea20`.
Aggregates: `research/TagModelScreen/condition-variety-corpus-2026-10-09.json`;
independent replay summary: `condition-variety-corpus-audit-2026-10-09.json`.

| Arm | Attempts | Eligible packages | Targets covered | Fields covered |
|---|---:|---:|---:|---:|
| Old families, equal budget | 77,824 | 618 | 18/19 | 59/152 |
| Expanded families, equal budget | 77,824 | 378 | 18/19 | 58/152 |
| Extra diagnostic anchored on shared property | 1,792 | 24 | 2/19 | 2/152 |
| Extra diagnostic anchored on mixed counts | 38,912 | 104 | 15/19 | 47/152 |

These are distinct sampled index combinations within each field/arm, not
necessarily distinct truth functions or human puzzles. Across targeted arms a
package containing both new forms may appear twice. The baseline differs from
the historical 542-package pass because this comparison predeclares new field/
draw seeds; do not represent it as reproduction of that historical sample.

Shared property passes the individual weak-clue envelope in only 7/152 fields
(one unnamed intersection predicate per field). Mixed counts produce 76,904
individual candidate clues across all 152 fields. The expanded equal-budget
arm includes mixed counts in 346/378 packages, about 91.5%; shared property
appears in none of its eligible packages. Thus simply pooling every new
predicate and sampling uniformly is not an adequate diversity strategy. The
forms exist and work, but the much larger mixed-count enumeration dominates
that draw procedure. No smooth recency decay or ranking weight was involved.

New-form arms provide 413 distinct individual-predicate-mask packages; 339 are
absent from the 477 distinct sampled baseline mask packages. This establishes
additional sampled representations/condition combinations, not that equivalent
logic is impossible to express using old forms or absent from an exhaustive old
search. Target coverage after union with the baseline remains 18/19: no new
formula-serviceability claim.

## Independent verification

Replayed every one of the 1,124 accepted package records using frozen-spec
`holds`, rather than trusting the generator's stored masks. Verified all
predicate masks, unique chemically valid target and extra complete-model
survivors when each clue is dropped. Replayed all 128 diagnostic package records
after conversion with actual JavaScript Puzzle Lab `satisfies`: all 275
condition masks agree on their 27-cell fields. Existing 23 research tests pass.
Exact fields/witnesses and converted replay inputs remain private. No blind
player example opened or existing fixture modified.

## Implication for the next decision

Keep both forms: each contributes usable ordinary packages under unchanged
criteria. Shared property is naturally rare in this bounded corpus/field sample;
do not force it into every target or relax its strength gate. Mixed counts need
bounded opportunity, not opportunity proportional to the number of syntactic
variants. Uniform selection from the enlarged flat list reduced eligible yield
by about 39% at equal effort and heavily concentrated one family.

Recommended next comparison, not an adopted generator policy: choose a logical
family before a concrete predicate, or preserve the old search and allocate a
small additional exploration budget to new forms. Compare equal total effort
and retain all current quality gates; no fixed family-frequency quotas. The
first option is a simple candidate-sampling mechanism compatible with later
portable implementation; the second preserves the old sampled pool but costs
extra work. Do not silently install either choice from this diagnostic.

The pass establishes valid reserve and a sampling imbalance. It does not establish
greater human interest, boss quality, pacing, save-state availability coverage,
production runtime performance or calibrated family probabilities.
