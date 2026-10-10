# Puzzle Lab V0

Local research harness, not a game mod or published website. Original source is
MPL-2.0. No third-party packages, game assets or real recipes are included.

For a separate temporary friends instance through Cloudflare Quick Tunnel, see
[`docs/research/PUZZLE_LAB_FRIENDS_PLAYTEST.md`](../../docs/research/PUZZLE_LAB_FRIENDS_PLAYTEST.md)
and `playtest.ps1`. Public mode uses a frozen private synthetic fixture and
separate durable sessions; it never enables facilitator/debug access. Five-task
progression and a guided tutorial remain separate unimplemented product work.

## Current research state

2026-10-09: synthetic upper interest/difficulty case 20 is solved on 4183,
with positive boss-like feedback and answer-order sensitivity. Frozen private fixture, facilitator proof,
public-policy witnesses and starting browser session are recorded in
`docs/prototypes/PUZZLE_LAB_V0_INTEREST_20_STATE.md`. Prior solved case 19 remains
preserved on 4182. No grammar or economy change; original player session preserved.
An isolated QA copy reproduced failure UX; it is not player evidence.

2026-10-09: accepted role presentation is now the default on every Lab URL.
Instructions, headings, clues and help share role shapes/colors/bold names;
ingredient names remain intact. The top task links to composition and pair
evidence; pair verdicts consistently use compatibility terminology. Subdued
refill and the alchemical synthesis button retain dynamic costs. No mechanics or
fixture change. Browser currently uses a separate fresh visual-review session; actual solved
case 19 remains durable and must not be confused with that preview. See
`docs/research/LAB_GUIDANCE_AND_HIERARCHY_2026-10-09.md`.

The dated entries below preserve historical research stages, not current UI defaults.

2026-10-09: explicit role-scanning presentation trial implemented. Append
`?roles=1` to a Lab URL for bold complete slot words plus small monochrome card
silhouettes in clues; omit it for the original rendering. Same model/session,
no wording or mechanics changes. Solved case 19 is shown with this variant on
4182; human review pending. All 42 tests pass. See
`docs/research/SLOT_ROLE_PRESENTATION_2026-10-09.md`.

2026-10-09: case 19 solved and positively accepted as a solid research puzzle;
four new pair checks, one success, Science 7. Subjective medium-high/high, not
maximum. Repeated slot-role scanning weakness recorded; visual treatment not
selected or implemented. No new trial. Start with current DESIGN_RESEARCH entry
and `docs/prototypes/PUZZLE_LAB_V0_INTEREST_19_STATE.md`; preserve solved session
on 4182. The precommit entry below is historical.

2026-10-09: user selected interest-ceiling research; synthetic case 19 is
precommitted for independent play on 4182. Start with
`docs/prototypes/PUZZLE_LAB_V0_INTEREST_19_STATE.md` and current DESIGN_RESEARCH
entry. Existing grammar and harness unchanged; four necessary clues, frozen
illustrative prior knowledge, verified public-policy routes. Difficulty/interest
await human evidence. Preserve all prior sessions. Production remains BLOCKED.

2026-10-08 chat closure: cases 16–18 are solved synthetic examples, preserved on
4179–4181. Case 18 did not establish boss difficulty. Current Lab suite: 42 passing
tests. Explicit tutorial, compound boss hypothesis, wording/role clarity and event
UI remain distinct next-step options; no next track selected. Start with
`docs/research/CHAT_HANDOFF_2026-10-08_NEXT_STEP_CHOICES.md` and DESIGN_RESEARCH.md.
The following dated case entries retain their historical evidence.

Completed coherent Keeper-voice trial: corpus case 15 on 4178, six new pair checks,
two submissions, one refill, Science 8. Read
`docs/prototypes/PUZZLE_LAB_V0_CORPUS_15_STATE.md` and the prototype protocol before
resuming. Final private model and exact text frozen; public initial snapshot tracked.
Do not replace or restart prior solved cases.
Future research support is opt-in; original case 15 remains binary-feedback only.
Current full suite has 41 tests.

Completed Keeper-wording trial: corpus case 14 on 4177, three paid pair checks,
one success, Science 9, no refill. Read
`docs/prototypes/PUZZLE_LAB_V0_CORPUS_14_STATE.md` and the prototype protocol before
resuming. Exact wording/one separate aside and hidden model precommitted privately;
public initial/completed snapshots tracked. Do not replace prior solved sessions.
Semicolon XOR rejected; future authoring uses new either/or template ID and thirteen context-gated
optional clue asides. Original played text preserved. Full suite now has 35 checks.

Completed trial: corpus case 13 on 4176, two new pair checks and one success.
It began with one prior stable pair and three necessary
clauses. Read docs/prototypes/PUZZLE_LAB_V0_CORPUS_13_STATE.md before resuming.
Hidden model/durable state private; solved prior cases below remain preserved.

Completed contrast: corpus case 12 on 4175, independently solved with five pair
checks and one success. Durable private state is solved. Read
`docs/prototypes/PUZZLE_LAB_V0_CORPUS_12_STATE.md` before resuming. Initial public
snapshot is tracked; full model stays private. Case-11 state below is historical,
and its solved session remains on 4174. The original wording integration passed
33 checks; subsequent case-14 refinement has 35.

Completed trial: anonymous real-corpus case 11, solved with 13 pair checks and
two submissions. Current browser state is solved; do not replace it by assumption. Checkpoint:
`docs/prototypes/PUZZLE_LAB_V0_CORPUS_11_STATE.md`. Hidden fixture stays private;
tracked public JSON is an initial snapshot, not a full fixture. Historical case-10
state below is the preceding completed trial.

Cases 01–10 are complete; the user accepts the interface as sufficient for the
laboratory. Current served case 10 (Сердце глубины) is solved, not fresh blind play.
Its recorded state is Science 2 / Research 3 after six pair tests and one success.
Checkpoint: `docs/prototypes/PUZZLE_LAB_V0_10_STATE.md`.
Consolidated findings/next step: `docs/PUZZLE_QUALITY_CONTRACT.md`.

## Run and verify

From the repository root, using Node.js 24 built-ins:

```sh
node research/PuzzleLab/server.mjs --fixture=research/PuzzleLab/fixtures/depth-10.json
node --test research/PuzzleLab/lab.test.mjs research/PuzzleLab/economy.test.mjs research/PuzzleLab/wording.test.mjs research/PuzzleLab/support.test.mjs
node research/PuzzleLab/audit-calibration.mjs --write
```

## Wording for future, unplayed cases

See `docs/KEEPER_CONTEXT_SCENARIOS.md` for the approved 13 clue-note
contexts and 9 stored (not yet displayed) event-response contexts. The example
`--aside=clue-has-organ-v1` below is eligible **only** if the chosen clue
at the specified zero-based index asserts that the essence has tag «Орган».
An ineligible note is rejected at authoring time; no default remark is added.



Prepare a new private case before precommit/handoff, then author its wording:

```sh
node research/PuzzleLab/author-wording.mjs PRIVATE_UNPLAYED_INPUT NEW_PRIVATE_OUTPUT
node research/PuzzleLab/author-wording.mjs PRIVATE_UNPLAYED_INPUT NEW_PRIVATE_OUTPUT --aside=clue-has-organ-v1 --aside-at=0
node research/PuzzleLab/author-wording.mjs PRIVATE_UNPLAYED_INPUT NEW_PRIVATE_OUTPUT --variant-offset=1
```

These are alternative commands; output must not already exist. Never use a played
case as the input for a replacement handoff. Keep real-corpus inputs/outputs private.
Use the authored output as the fixture for validation, hashing, precommit and serving.
Existing fixture preparers still emit a raw model; this authoring step is explicit.

`wording.version=1` and one entry per clue persist template ID and exact text, plus
optional aside ID/text. Plain/note alternatives rotate only for repeated eligible
families, using their order; selection never reads the answer or compatibility.
No aside by default; the author may attach one explicitly from thirteen context-eligible lines in
`keeper-asides.mjs`. Future XOR uses `xor-plain-v2`; `xor-plain-v1` remains valid for
frozen texts. Unsupported AST shapes or unfamiliar slot labels use
`plain-fallback-v2`; historical `plain-fallback-v1` remains readable. IDs are immutable: change
wording with a new version/ID. Validation rejects mismatched text, wrong scopes,
unknown IDs and more than one aside. Source and existing output cannot be overwritten.

The UI renders asides separately from conditions. Legacy fixtures without wording
retain their original rendering path; no solved case is reauthored or restarted.
See `docs/CLUE_TEMPLATE_SHEET.md`. This is research-only, not a production mod.

If child-process isolation is restricted, use
`node --test --test-isolation=none research/PuzzleLab/lab.test.mjs`.
There are 27 deterministic/HTTP tests (include `economy.test.mjs` in the test command). The offline audit validates all ten frozen
fixtures, replays recorded pair histories and emits aggregate structural evidence
with fixture hashes in `calibration-audit.json`; it does not score human interest.

Open http://127.0.0.1:4173. Stop with Ctrl+C. An alternative port uses `--port=4174`.
The server binds IPv4 loopback; `localhost` works when it resolves to IPv4.
The default `fixture.json` remains original negative onboarding case 01 for
reproduction. Select historical cases explicitly with `--fixture=path/to/file.json`.

## State and presentation

Future opted-in fixtures may contain `researchSupport: {version: 1}`. The builder
exposes `--research-support`; freeze it before player choice. Paid failed synthesis
stores a general compositionMismatch flag only after checking visible tag conditions;
no failed-clause list or correct component is disclosed, and no pre-submit validation
appears. Reminder is shown for a selected previously submitted invalid mixture.
Submitted mixtures/outcomes persist in the existing history and appear in a journal.
Selected repeats are labelled, remain allowed and cost Science. Disabled submit
explains incomplete selection, shortage or completion. Legacy fixtures retain the
old feedback/display envelope. UI module loads only for opted-in cases, so already
running legacy servers do not require a restart or a new asset route.

Asides have 13 user-approved context-gated clue notes in `authoringAsides`;
9 additional approved event replies are stored but are not yet shown by the UI.
Retired historical IDs remain valid only for frozen records. Each of the seven covered wording families
has four active variants (28 total). `--variant-offset=N` selects a deterministic alternate independent
of answer/chemistry, persisted as exact template ID/text. No per-play paraphrasing.

State is held in server memory, associated with an HttpOnly session cookie.
HTML/CSS/browser-JS changes reload presentation and preserve current state.
Finite polling every two seconds avoids permanent reload streams. Server/rules
changes require a restart. A valid changed fixture resets sessions; invalid
fixture edits preserve the last valid model. Do not change a live blind fixture.
A restart creates fresh sessions, not restoration of a historical human trial.
Preserve paid actions and current player state in the case checkpoint beforehand.

Player surface: candidate cards and labeled colored properties, composition clues,
observed adjacent compatibility, selected-pair experiments, final synthesis and
expandable instructions. Repeat-click deselects; observed-pair selection clears
other choices. Pair identities have slot silhouettes/codes and linked highlighting.
No automatic tag deductions, survivor list, difficulty/progression labels,
manual exclusion controls, notes, bottom action-history list or download button.
Historical mark/notes data and paid-action history remain in session/API evidence.

The rules module evaluates and renders the same structured clue objects. Two or
three slots, exact counts, implication, shared-property and forbidden-conjunction
clauses are supported. Startup validates a unique answer in each synthetic model.
The fixture owns candidates, exhaustive properties, clues, answer and budgets.
Cases 09/10 allow three final checks; older budgets remain frozen. Neither budget
nor synthetic outcome matrices establish production balance or corpus coverage.

Three-slot models require both adjacent edges stable and all composition clues.
`compatibility.stablePairs` defines the full hidden graph; every other legal
adjacent edge is incompatible. `knownRelations` contains only public priors.
New cases start with stable priors only; every personally researched result stays
visible. Pair research charges and synthesis Science are separate finite pools.
Known/invalid pair requests are free. Pair tests reveal only binary compatibility;
full synthesis reveals success/failure. Exhausting pair charges does not block a
remaining full synthesis. Success or exhausted Science ends the investigation.

## Facilitator and evidence boundary

Only public fields and earned observations are served in normal mode. Answer,
unobserved edges, audit and fixture source are not player routes. To inspect a
private authoring/debug session explicitly run `--debug` and open `/facilitator`.
That page warns about spoilers before linking to `/api/debug`, which includes the
full model and sessions. Both routes return 404 in ordinary mode.

This is accidental-spoiler separation, not an anti-cheat system: a local user can
read repository files or start a new session. Facilitator files contain fictional
spoilers and must not be surfaced during blind play. Exact played fixtures stay
frozen; dated outcomes belong in their checkpoints. See `docs/PAPER_PROTOTYPE_PROTOCOL.md`.

## Shared Science and durable corpus trial

Opt-in finite shared pool: `economy: {mode:'sharedScience',refillAmount:0}`.
Server denies refill; UI hides it. Pair tests and submissions use one pool.
When a paid action leaves less than the final-check cost, the no-refill trial
ends exhausted (success wins). Historical positive-refill behavior unchanged.
Recovery: `docs/prototypes/PUZZLE_LAB_FRIENDS_THREE_SLOT_01_STATE.md`.

Case 11 opts into sharedScience: pair 2, triple 5, initially 20 Science, unlimited
explicit free +10 Lab refill. Wrong submissions and zero Science do not end play.
Acquisition in the game is not simulated. Historical fixtures retain finite pools.

Use `--fixture=PRIVATE_FIXTURE --state-dir=PRIVATE_STATE_DIRECTORY --port=4174`.
Optional state directory atomically persists actions and restores the cookie's
session after restart when the fixture hash matches. Keep it outside Git. Without
this option the historical memory-only behavior above applies.

## Separate ngrok friends playtest

Use `ngrok-playtest.ps1 -Mode Start|Stop|Status -PrivateDirectory PRIVATE_DIR
-NodePath NODE_EXE` (default port 4184). Private directory must be outside Git,
with frozen synthetic `fixture.json`, `sessions/`, and `ngrok/ngrok.exe` plus
locally authenticated `ngrok/ngrok.yml`. Never commit tokens or player data.
Start discovers the actual HTTPS endpoint and explicitly approves only that
origin for the public server. Debug and reload are disabled; Host/Origin checks
and secure durable cookies remain required. Occupied ports and 4183 are rejected.
Stop terminates only recorded owned processes and preserves sessions. Status
checks the actual puzzle and full assets, not registration alone.

Visitors may see ngrok's Visit Site screen. Keep computer, network and both
processes running; sleep/reboot interrupts access. Account dev domain is normally
reused on restart, but availability and visitor access require separate checks.
The launcher verifies public responses from this computer; an independent
visitor network must still be tested. Retain the same browser cookies to resume.

## Private facilitator panel

`panel.ps1 -Mode Start|Stop|Status -PrivateDirectory PRIVATE_DIR -NodePath NODE_EXE`
starts a separate local panel at http://127.0.0.1:4185. Never expose that port with
a tunnel. It reads private saved sessions and offers fixed playtest Start/Stop/
Status controls, animal pseudonyms, owner/test categorization, summaries, action
timelines and local JSON export. Stopping the panel does not stop the playtest.

Durable sessions include private versioned telemetry: server-accepted/rejected
actions and earned results; page/help/visibility signals. No timeline or nickname
is exposed to players. Historical sessions have incomplete coverage and unknown
timing. Counts represent cookie sessions, not distinct people. Visible-tab time
is an estimate, not proof of attention. Default summaries exclude untouched
probes and marked owner/test sessions. Exports contain private trial evidence:
keep them outside Git. Tests include `telemetry.test.mjs`.

## Presentation ordering before a new playtest

After model/wording generation, run the authoring-only pass before freezing the
new fixture and facilitator precommit:

```text
node research/PuzzleLab/author-card-order.mjs PRIVATE_INPUT.json PRIVATE_NEW_OUTPUT.json NEW-CASE-ID SEED
```

Keep both output and adjacent `.order-audit.json` outside public Git. It reorders
cards only; identity must be new, source and existing output cannot be overwritten.
The default strength is 2 on its own 0..1 score, with at most 128 seeded sampled
orders (exhaustive below that size). Optional programmatic settings are exported
by `prepareCardOrder`; preserve the returned audit. Revalidate/precommit the exact
output before first play. This pass supplements the existing model-generation
criteria and does not run on requests, refreshes or already-started cases.
See `docs/research/PUZZLE_LAB_UI_HIERARCHY_2026-10-10.md` for scoring/limitations.
