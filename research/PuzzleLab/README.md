# Puzzle Lab V0

Local research harness, not a game mod or published website. Original source is
MPL-2.0. No third-party packages, game assets or real recipes are included.

## Current research state

Active contrast: corpus case 12 on 4175 with durable private model/state. Read
`docs/prototypes/PUZZLE_LAB_V0_CORPUS_12_STATE.md` before resuming. Initial public
snapshot is tracked; full model stays private. Case-11 state below is historical,
and its solved session remains on 4174. Test suite now has 26 checks.

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
node --test research/PuzzleLab/lab.test.mjs
node research/PuzzleLab/audit-calibration.mjs --write
```

If child-process isolation is restricted, use
`node --test --test-isolation=none research/PuzzleLab/lab.test.mjs`.
There are 26 deterministic/HTTP tests (include `economy.test.mjs` in the test command). The offline audit validates all ten frozen
fixtures, replays recorded pair histories and emits aggregate structural evidence
with fixture hashes in `calibration-audit.json`; it does not score human interest.

Open http://127.0.0.1:4173. Stop with Ctrl+C. An alternative port uses `--port=4174`.
The server binds IPv4 loopback; `localhost` works when it resolves to IPv4.
The default `fixture.json` remains original negative onboarding case 01 for
reproduction. Select historical cases explicitly with `--fixture=path/to/file.json`.

## State and presentation

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

Case 11 opts into sharedScience: pair 2, triple 5, initially 20 Science, unlimited
explicit free +10 Lab refill. Wrong submissions and zero Science do not end play.
Acquisition in the game is not simulated. Historical fixtures retain finite pools.

Use `--fixture=PRIVATE_FIXTURE --state-dir=PRIVATE_STATE_DIRECTORY --port=4174`.
Optional state directory atomically persists actions and restores the cookie's
session after restart when the fixture hash matches. Keep it outside Git. Without
this option the historical memory-only behavior above applies.
