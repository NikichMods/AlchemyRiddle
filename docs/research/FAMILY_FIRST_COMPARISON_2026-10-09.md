# Family-first sampling comparison — 2026-10-09

User selects a trial of family-first random sampling, not quotas for final
puzzles or mandatory one-of-each. Existing ranking/recency weights, gates,
curriculum and production boundary remain unchanged.

Reuse `condition_variety_comparison.py` with `--family-first`: same accepted
19-target corpus, same 152 seeded 3x3x3 fields, 512 attempts per arm per field.
Three arms: old flat pool, expanded flat pool, expanded family-first. For each
predicate draw choose uniformly among available root families, then uniformly
among unused predicates in that family. Directions share their implication
root. Family repetitions are permitted; only reuse of the identical predicate
within one package is excluded. Absent/exhausted families are unavailable.
Equal family probability is a trial baseline, not calibrated product weights.

Predeclare three draw-offset passes: 0, 100000, 200000. Fields remain identical
between passes; only package draws vary. Three-minute cap per pass; exact
witnesses private, aggregate artifacts immutable. Primary offset zero must
reproduce the preceding baseline/expanded counters. Report eligible packages,
coverage, new-family representation and duplication; no route replay or human
interest claim. This uses existing corpus/gates and extends the bounded helper,
without a new research framework or production sampling-policy installation.

## Results

All three passes complete in 9.218 / 9.250 / 9.297 seconds. Each arm receives
77,824 attempts per pass on the same 152 fields. Offset-zero baseline and expanded
results exactly reproduce the preceding comparison's arm counters and coverage.

| Measure over three passes | Old flat | Expanded flat | Expanded family-first |
|---|---:|---:|---:|
| Eligible packages by pass | 618 / 633 / 628 | 378 / 351 / 359 | 576 / 608 / 598 |
| Mean eligible packages | 626.3 | 362.7 | 594.0 |
| Covered targets each pass | 18/19 | 18/19 | 18/19 |
| Covered fields by pass | 59 / 61 / 60 | 58 / 59 / 60 | 61 / 62 / 62 |
| Packages containing mixed count, pooled | 0 | 989/1088 (90.9%) | 688/1782 (38.6%) |
| Packages containing shared property, pooled | 0 | 0 | 31/1782 (1.7%) |

Family-first raises sampled eligible yield by 63.8% against expanded flat at
equal attempt count, while remaining about 5.2% below old-flat yield. Thus it
recovers most of the loss introduced by the expanded flat enumeration, exposes
both new forms, and reduces mixed-count concentration without banning repeated
families. It does not improve target coverage. Counts are sampled index packages,
not independent human puzzles or player probabilities; pooled passes can rediscover
the same package and share identical fields. This is draw-seed robustness, not
independent field/corpus validation or a statistical significance claim.

Independent verification: replay all 1,782 family-first records from frozen
specifications; every individual mask, unique complete-model target and clue
necessity agrees. After conversion, actual Lab JavaScript `satisfies` agrees on
all 3,824 condition masks across those records. All 27 research tests pass,
including four sampler checks: family-size bias removed, repeated families
permitted, implication directions grouped, predicate reuse excluded, insufficient
pool rejected and seeded draws reproducible.

Artifacts: `research/TagModelScreen/family-first-2026-10-09-{0,100000,200000}.json`.
Exact witnesses/replay data remain private. Generic helper metadata still names
the unused targeted-arm budget/caveat; no targeted arm runs in these passes.

## Decision implication

Recommend family-first as the next research sampling baseline: simple grouping
and two draws per predicate, no new operator, quota, decay or dependency.
Equal family chances here are deliberately untuned. A later curriculum can
change available motifs/chances while preserving this mechanism. Do not infer
that selected final puzzles must have equal family frequencies.

Current implementation is an opt-in bounded-comparison arm, not a silent switch
of `generator_route_ranking` or production code. Before wider adoption, record
the user's choice and assess resulting packages/routes; human readability,
interest and difficulty remain unproved. Existing ranking, quality gates,
curriculum semantics and solved case 20 are preserved.

## Accepted and applied to main research builders

User accepts family-first as the algorithm's baseline. Clarification: this is
not stricter filtering; the unchanged gates receive differently sampled proposals.
Compared with the old narrow pool the measured mean yield is about 5% lower,
with broader represented families; compared with expanded flat it is higher.
Adequacy is bounded to this research envelope, not guaranteed for every save/target.

Shared implementation now lives in `reasoning_diversity_screen.py` and is used
by its `build_options` and `generator_route_ranking.py`. The comparison arm uses
the same helper. Existing frozen evidence and specialized historical/control
searches are not rewritten. Main ranking/recency weights, clue predicates and
acceptance thresholds are unchanged. No quotas or smooth decay introduced.

Integration verification: all 27 research tests pass. Full main-ranking run on
the verified corpus completes in 13.36 seconds: 152 fields, 33,280 package
attempts after the existing field-floor skip, 504 eligible packages and a
199-candidate reservoir covering 18/19 targets. Selection-policy replays 19,104;
independent-seed validation replays 38,208. This run uses the main tool's historical
field/draw setup and reservoir; its counts are not directly paired with the trial
table above. Artifact: `family-first-ranking-adopted-2026-10-09.json`; exact
pool/witnesses remain private. This proves pipeline execution, not a new tuning
decision from its multi-weight experiment arms or player interest acceptance.

Current state: family-first is the accepted main research sampling baseline.
Production remains BLOCKED and no player fixture has been opened or changed.

## Follow-up: reserve counts versus final selection

User asks what package counts mean for game deployment and whether rare families
remain represented. The 362.7/594.0 means count accepted sampled packages across
all 19 targets and 152 fields per complete pass, not game puzzle inventory, an
exhaustive combinatorial count, per-target reserve or unique player experiences.
Multiple packages can serve the same target/field, be logically equivalent or
recur between draw passes. Future availability/knowledge/curriculum constraints
remain outside this full-availability screen. The unserved nineteenth target is
an unresolved bounded-search gap, not proof of impossibility.

Inspected actual final selections in the adopted ranking integration artifact:
fresh knowledge context, preferred route 3, accepted weak strength 0.25, three
target orders: 54 selections, not 54 distinct puzzles. Family presence counts:
literal 16, homogeneous count 18, XOR 23, positive implication 15, mixed count 19,
negative implication/forbidden combination 12, shared property 2. Every major
family appears in this sampled selection cohort; frequencies are unequal and
shared property remains rare (only one of the 199 reservoir packages contains
it). No general guarantee for every sequence/save/target or finer submotif.

Uniform chance applies only to available root families at proposal draw time.
Predicate availability, quality/necessity filters, reservoir retention and final
ranking/curriculum can change the resulting frequencies. Rare-family presence
must therefore be audited after selection, not inferred from proposal symmetry.
This finding introduces no frequency quota or override of quality requirements.
