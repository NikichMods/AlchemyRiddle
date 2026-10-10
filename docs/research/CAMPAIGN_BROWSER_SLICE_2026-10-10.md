# Browser campaign slice — 2026-10-10

Status: implemented and locally verified research candidate; human learning and
difficulty acceptance pending. Production mod remains BLOCKED. Owning accepted
scope: `../PRODUCT_REQUIREMENTS.md`; prior recovery:
`CAMPAIGN_BROWSER_HANDOFF_2026-10-10.md`.

## Scenario and knowledge contract

This is an authored laboratory demand route after the relevant capabilities are
available, not a typical or mandatory vanilla walkthrough. It does not simulate
station construction, inventory acquisition, travel, time or Science acquisition.
Titles describe illustrative preparations and purposes; their assignment is
independent of hidden ingredients. They do not establish new vanilla item effects.
The private correspondence records exact unchanged corpus identities.

| Scenario | Need / displayed product | Field and instructional purpose | Starting knowledge |
|---|---|---|---|
| Two-slot 1 | Help a visitor: «Микстура для затяжного недомогания» | 2×2; complete properties, simultaneous conditions, submission | Fresh profile; no invented experiments or known formulas |
| Two-slot 2 | A traveller needs «Бальзам от дорожных ушибов» | 2×2; independent application of presence/exclusion/count | Actual first-step history and Science; two-slot success adds no pair fact |
| Three-slot 1 | After advanced laboratory capability, prepare «Препарат для сохранения тканей» | 3×3×3; two simple composition clauses, adjacent pair experiments and journal | Actual profile; first exposure to pair research |
| Three-slot 2 | Workshop request: «Раствор для восстановительных работ» | 3×3×3; simple clauses and chemistry together | Every actual earned positive/negative pair and successful-formula edge from preceding play |
| Separate mature scenario | «Эликсир спокойного сна» | 3×3×3, three interacting clauses; intended mature band | Separate sandbox with 34 explicitly seeded observations, zero invented completions/spending |

Early labels are «Лёгкая»; the separate mature scenario is «Максимальная».
These are intended labels, not measured human bands or a certified boss. First
three-slot packages still estimate around 3–5 pair checks from fresh knowledge;
compact grammar/field is not proof of easy learning. The first three-slot step
explains the experiment model; it contains no scripted paid demonstration or
free deduction of the answer. Human play must determine whether this is enough.

Developer UI displays both proposed full ladders (16/19), marks unfilled rungs
as proposals and offers only the four prepared steps plus the explicit mature
scenario. Sandbox switches create explicitly fresh/seeded profiles, not fictional
earlier play. Reload resumes the selected frozen sandbox. Main player statistics
are in separate storage/cookies and never inherit sandbox experiments.

## Bank feasibility before integration

Original 205-package pool uses 3×3×3 fields. Selecting simple literal/count
two-clause packages initially provided only one candidate for each chosen early
three-slot product. This was too narrow for knowledge-aware variation, so offline
preparation added 12 for each with unchanged gates: at most 32 sampled fields and
512 simple two-clause combinations per field/variant, retain at most 12. Existing
weakness, answer, omission, field-witness, option and structural-rubric checks
remain. No ranking weight, ordinary search budget or runtime generation changed.

The resulting private bank v2 has **421 packages: 192 two-slot / 229 three-slot**.
All 16 core two-slot variants have at least one compact unique/necessary package.
The two-slot preparation exhausts small 2×2 fields with the accepted compact
weakness floor and two necessary presence/absence/count clauses, retaining 12
per variant. This is a slice bank, not complete all-difficulty coverage.

Prepared alternatives per scenario: **24 / 12 / 13 / 13 / 4**. Three-slot estimates
were checked with fresh, explicitly seeded mixed (34 observations) and all-known
(171 observations) states. Full knowledge legitimately reduces new pair checks
to zero. Knowledge is never hidden to enforce a lower experiment count.
Aggregate report: `../../research/TagModelScreen/campaign-browser-feasibility-2026-10-10-v2.json`.

Bank SHA-256:
`6ce6e0e04bf79fdd49e6e5e2895ea1dbf8a829e56aefc18a7e6824a258f57371`.
World identity:
`world-a87492b34fffdfc6f836b5fc01288633410edfe790018a4b641be95da3a60f1b`.
Original manifest and 205-package pool hashes remain as recorded in the handoff.
The served five target titles have a new naming identity (2), with explicit
correspondence in the new private manifest. Frozen naming-v1 files are untouched.
Other world titles are not presented as an editorially accepted full campaign.

## Implementation ownership and readiness

Before source changes, the browser gate was READY: server request/action/persist
owns commits; rules own costs/results; UI renders only `publicView`; immutable
profile fixture owns answer/clauses/band after start. Blast radius is this isolated
research instance; existing single-fixture mode is retained and tested. Production
game behavior remains out of scope/BLOCKED.

Reuse source: committed online PuzzleLab subtree at `cb69e45`; integration base
`7a9aa8b`. The sibling advances independently (later observed `9c51595` with local
app/index/style changes); none of those files, processes, sessions or launchers
were modified in that checkout. This integration does not claim to include its
newer trial or uncommitted work.

- `campaign_bank.py` prepares privately and selects at start. Three-slot selection
  invokes the existing Python route estimator and ranking with actual mixed
  knowledge and recent packages. Two-slot selection is uniform within its prepared
  envelope; no invented two-slot score weights. Known formula variants bypass
  research; an empty suitable pool reports a blocker and preserves active state.
- `campaign.mjs` owns the profile, one active frozen investigation, ledger with
  provenance, per-arity completions, per-investigation/total spending, refills,
  completed frozen fixtures and explicit developer checkpoints. Global ingredient
  IDs are independent of role-local card IDs/order.
- Existing `server.mjs` remains the HTTP/origin/persistence owner. Per-profile
  mutation queues, puzzle/revision checks and action receipts prevent concurrent
  or replayed requests from paying twice. Rejected actions do not commit costs.
  Durable campaign cookies have separate player/sandbox/storage identities and
  a 30-day lifetime. Bank mismatch refuses restore without overwriting the old
  profile; migration is not silently inferred.
- Existing telemetry/admin files are reused. Private campaign events identify
  world, puzzle, step, band, mode, knowledge count and total cost. Individual early
  completion does not prematurely end campaign visible-time measurement. Private
  snapshots include campaign provenance and completions; ordinary API/assets
  exclude the bank, formulas, answers, ranking and reverse map.
- UI keeps accepted role typography and neutral failed-experiment feedback.
  Science refill remains subordinate. Existing authored clue templates are frozen
  at investigation start; already started fixtures are not rewritten on reload.

## Verification and boundaries

- **55 Node tests** pass, including legacy economy/wording/support, origin/tunnel,
  telemetry and campaign contracts. New campaign tests cover immediate negative
  facts, solved edges, no failed-mixture inference, free known-pair reuse, reordered
  local IDs, profile isolation, restart, denied actions, duplicate/stale/two-tab
  actions, known-target bypass, empty-pool preservation and sandbox isolation.
- **49 Python tests** pass. Existing research gates/weights remain unchanged.
- Private cross-language QA validates all **421 fixtures**, compares **14,766
  clause truth values** against source predicates and checks each omission still
  leaves more than one complete-model answer. No raw formulas are printed.
- Actual Python selector + HTTP + durable files completes all four player steps;
  a deliberately negative paid pair and four successful mixtures total **22
  Science**, one refill, four stable and one incompatible earned pair. Restart
  restores exactly the same public state. This deliberately guided QA trace is
  technical evidence, not blind play or a typical cost estimate.
- Separate mature profile starts with 34 seeded observations and zero completions
  or spending. Browser inspection verifies the board, costs, private scenario
  control and explicit knowledge origin. Player profile used for preview remains
  unplayed; technical traces use separate QA storage.

No online campaign deployment or live friends replacement occurred. Human
learning, interest, intended bands, boss depth, arbitrary-state coverage and full
35-position completion remain open. Next: blind local slice play; evaluate the
first-three-slot teaching burden and whether accumulated knowledge changes the
second investigation usefully. Extend/correct a specific envelope only from that
evidence; do not infer calibrated difficulty from successful automated routes.

Local paths, launch commands, private QA records and live instance identities are
in the private companion locator for this chat, outside Git.

## Frozen source and hosted checks

Implementation candidate: `2dae2eac8a9507577fbe6c64335d254e35fa1329`,
branch `research/rare-opportunity-screen`. Both hosted runs completed successfully:
[Puzzle Lab checks 38064692641](https://github.com/NikichMods/AlchemyRiddle/actions/runs/38064692641)
and [Research Python 38064692513](https://github.com/NikichMods/AlchemyRiddle/actions/runs/38064692513).
These checks cover public-input-free contracts; private corpus QA remains local
as described above. Subsequent documentation recording does not change the
candidate's browser source or frozen bank identity.
