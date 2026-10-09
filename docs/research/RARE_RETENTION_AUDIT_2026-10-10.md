# Rare-candidate retention audit — 2026-10-10

User authorizes checking where usable rare packages disappear before final
selection. Exact replay of the adopted main family-first run: same corpus hash,
19 targets, 152 fields, RNG seeds/draw consumption, field/package floors and gates,
512 attempts per eligible field, twelve-slot uniform reservoir per target.
Instrument before reservoir only; do not rerun routes or change retention policy.

The existing frozen 199-candidate pool can prove final availability, but cannot
recover discarded records. A bounded replay reuses the existing `admissible`
gates and sampler to record family counts before/after retention. It must exactly
reproduce every retained surface/clue specification in order, all 504 eligible
packages and 199 retained candidates. Three-minute cap; fail rather than report
complete if identity/replay differs. Exact rare witnesses remain private.

Question: are rare alternatives absent because of field/gate feasibility,
proposal search, or uniform reservoir eviction? Report all family counts and
target coverage, preserving failures. This is one exact historical run, not
exhaustive corpus capacity. No new blind example, production code or weights.

Bounded follow-up declared after replay: exhaustively enumerate every two/three
clue package containing shared property on the replay's two eligible shared
fields. Same gates and existing clues, no random sampling or field changes;
retain the three-minute total cap. This distinguishes local package-sampling
misses from absence of further valid shared packages in these exact fields.

## Results

Exact replay complete: all 504 eligible packages, 199 retained records and their
per-target order/surface/clue specifications match the frozen main run. No
route replay or sampling-policy change. Replay plus bounded exhaustive follow-up
completes in 6.015 seconds. Canonical aggregate:
`research/TagModelScreen/rare-retention-2026-10-10-v2.json`.

Shared-property pipeline in this run:
- individually eligible shared predicate on 8/152 fields;
- six fail the existing minimum complete-model alternatives needed for an ordinary
  two-necessary-clue puzzle; two fields enter package search;
- 198 unique sampled packages containing shared: 152 fail full-model necessity,
  41 fail unique complete-model answer, four fail existing option gates;
- one eligible package, and that same package is retained. No shared-property
  reservoir eviction occurred.

Full follow-up examines 325,889 two/three-clue combinations containing shared
on those same two fields, excluding unsupported package sizes under the unchanged
floor. It finds 12 eligible packages, all two-clue, on one field for one target.
Their complete sets of tag-valid triples have four distinct masks; these are not
12 established distinct player experiences. Original random search missed 11
of the 12 packages. The second eligible field yields none. Independent frozen-spec
replay verifies all 12 masks, unique complete-model targets and necessity.

Other family retention: literal 157->62, count 190->69, XOR 282->105, positive
implication 114->41, negative implication 89->43, mixed count 183->73. Most
families preserve target coverage; negative implication drops from 16 to 15
targets. Thus uniform reservoir sampling can remove local opportunities in
general, but it is not the observed cause of scarce shared-property reserve.
Do not use these aggregate ratios as calibrated production survival probabilities.

32 existing research tests pass; exact reservoir replay acts as the integration
check for this instrumentation. The intermediate v1 audit double-counted
implication directions in raw field totals; it was corrected before publication
and kept privately, not used as canonical evidence. Valid-package replay itself
was unaffected. Public evidence contains only counts and hashes; exact witnesses
remain private.

## Next decision

The observed loss is primarily proposal search: many variants exist in a field,
but a fixed random package budget reaches few of the necessary combinations.
Rare condition availability itself is also narrow in this sample. Neither a
stronger final-selection bonus nor a larger uniform reservoir can restore
packages never proposed.

Recommend a bounded extra exploration step when a rare family is actually
available, starting with two-clue combinations and preserving all gates. This
could recover reserve without compulsory rare clues or exhaustive three-clue
search in every field. Compare equal total effort against current sampling,
keep costs visible, and test retention of found alternatives. This is a proposed
next trial, not an installed quota, generator change or relaxed acceptance rule.
No unseen fields, full-corpus exhaustiveness or human variety are proved.
