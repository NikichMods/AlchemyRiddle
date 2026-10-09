# Bounded rare-family search adopted — 2026-10-10

## Owning decision and implementation

User accepts the reserve-64 search policy after search-only and downstream
selection/held-out route comparisons. Change candidate search, preserve ordinary
selection, and introduce no rarity bonus or content quota. Production remains
BLOCKED; this is the working research generator, not shipped mod behavior.

The tested pair sampler and proposal stream moved into
`reasoning_diversity_screen.py`. `rare_search_comparison.py` re-exports the
same functions instead of maintaining another implementation. Main
`generator_route_ranking.py` and `reasoning.build_options` use that shared helper.
Other callers of `build_options` (curriculum and Dark-organ diagnostic screens)
therefore receive the same search policy; historical flat/family-first control
probes and the exact old audit remain explicit historical paths.

The main budget remains 512 attempts per searchable field, duplicates included.
When an empirically rare root is available, 64 attempts draw a rare root, a
predicate within it and one different predicate as partner. Attention is uniform
across available rare roots; partner sampling is uniform over concrete predicates
as in the accepted trial. All proposals face the unchanged main acceptance gates.
Without a rare root all 512 proposals are ordinary family-first. Uniform retention
still has a cap of 12 per target. No selection, recurrence, route or structural
weight changes; no required rare final puzzle.

The current small research profile contains `shared`, supported by the frozen
opportunity comparison. It is explicit and reusable for several roots, but is not
a permanent production rarity fact or automatically recalculated feedback weight.
No new history store, decay model or generator quota system is introduced.

Ordinary proposal, focused proposal and retention streams are separate, using
the seeds of tested repeat 0. Field/knowledge sampling matches the previous main
field sample. Historical coupled-RNG draws need not match. Auxiliary capacity
builders preserve their existing budgets and gates; reserve is one eighth of
their budget capped at 64 (e.g. 56 of default 450). They pass no complete-model
floor to the helper, since those capacity diagnostics did not previously apply
the main ordinary-package floor. Do not mistake their larger capacity totals
for main-pipeline eligible ordinary puzzles. Their random draws change under
the adopted sampler; previous frozen comparisons retain their original identity.

Completed main ranking artifacts now reject overwrite. Frozen old outputs are
preserved; new outputs have separate dated identities.

## Full-path verification

Aggregate main result:
`research/TagModelScreen/rare-search-adopted-ranking-2026-10-10-v1.json`.

- 152 sampled fields; 87 rejected by the unchanged field floor.
- 33,280 total package attempts over 65 searchable fields; 128 focused attempts
  across the two fields with rare availability, included in that total.
- 564 eligible packages; 200 retained candidates; 17/19 targets served.
- 19,200 selection-estimation and 38,400 held-out route replays; full pass 12.969s.

`verify_rare_search_adoption.py` checks against the privately frozen downstream
comparison's repeat-0/reserve-64 pool. All 200 ordered surface/clue identities,
starting knowledge, route and held-out summaries match exactly. The 18 main
default-strength selection sequences (six settings x three orders) also match.
Independent frozen-spec evaluation verifies all 200 packages' tag-valid triples,
unique complete-model answer and necessity of each clue.

The second main caller is exercised on two fields for each of 19 targets: all
38 calls use the shared helper with the declared 512/64 budget and preserved
capacity semantics. Aggregate proof:
`research/TagModelScreen/rare-search-adoption-replay-2026-10-10-v1.json`.
All 38 research unit tests pass, including the moved helper's existing paired
budget/tail, unavailable-root fallback and multiple-root tests, plus default
integration and insufficient-predicate/floor handling.

This particular main run retains no shared package. The matching ordinary
control also serves 17 targets; the earlier coupled-RNG main pool served 18.
The new run is not a claimed improvement over that unmatched historical seed
stream. Adoption relies on the 12 paired search runs and downstream comparison,
not cherry-picking a new seed with a rare candidate. Nothing in this policy
guarantees rare retention or final selection in every run.

## Remaining boundaries

The accepted change makes bounded rare exploration the research baseline.
Human interest, repeated rare-motif exposure in a campaign, broader fields and
actual availability/knowledge states remain open. Current evidence tests only
one empirically rare root, although the helper supports multiple roots.
Main gate/scoring code and the current solved Lab fixture are preserved; no
browser UI, network-playtest preparation, vanilla recipe, economy or save change.
Continue from this accepted baseline rather than reopening the completed
baseline-versus-reserve decision without new evidence.
