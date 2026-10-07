# Puzzle Lab local research tool — working plan

Status: **V0 implemented on research/puzzle-lab-v0; mechanical checks passed; first player feedback requires revising onboarding. Not production UI architecture; no Graveyard Keeper runtime behavior is changed**.

## Current execution checkpoint — 2026-10-07

Implementation and run instructions: `research/PuzzleLab/README.md`.
Local command: `node research/PuzzleLab/server.mjs`; player URL:
`http://127.0.0.1:4173`.

The minimal stack is Node.js 24 built-ins plus HTML/CSS/browser modules, without
package dependencies. Fixture data, rules/evaluation, server projection and
presentation are separate. One synthetic easy two-slot fixture is precommitted;
its subjective inference quality is unaccepted until blind play.

Implemented: card selection, personal exclusions, notes, paid binary submission,
player journal export, optional facilitator truth-table/session view, and live
browser reload for presentation/fixture edits. Answer and evaluator stay on the
server; debug routes require explicit `--debug`. One Science/one submission is
this fixture's bounded calibration budget, not accepted production balance.

Verified locally on Node 24.19.0: seven deterministic/HTTP tests pass, including
clue truth tables, uniqueness, budget exhaustion, invalid requests, session
continuity and player/debug separation. Browser checks prove initial rendering,
selection, notes, personal marking, failed submission and exhausted-budget UI.
An HTML edit triggered automatic reload while retaining notes and selections.
The normal test runner was blocked by local child-process permissions; the same
tests passed with `--test-isolation=none`. CI runs the normal isolated command.

First player feedback: `docs/prototypes/PUZZLE_LAB_V0_EASY_01_RESULT.md`.
The easy fixture is formally valid but requires revised onboarding: repetitive
single-property wording and conditional interpretation caused rejection/confusion.
It is now in debrief; repeating it cannot count as a fresh blind attempt.
Colored property badges and explicit slot frames have been implemented and
visually verified in a new browser tab. The old tab remained unresponsive while
HTTP page/state requests returned 200 promptly. Permanent EventSource reload
was replaced with short finite polling; new-tab reload reaches document state
`complete`. Exact player state was recovered and persisted in the result record.
The server/fixture were not reset. The precise cause of the old-tab CDP timeout
remains unproved; do not present the stream change as proof of that root cause.

Current active fixture: `lab-v0-02`, synthetic target Янтарный оберег, with a
precommitted interacting-count model. Initial player checkpoint and next
interaction: `docs/prototypes/PUZZLE_LAB_V0_02_STATE.md`. No player-facing
difficulty labels or progression indicators are added; progression presentation
is a separate open product decision. The user found the colored tags attractive
and the revised layout somewhat better; finer UI polish is deferred.

Run the current case:
`node research/PuzzleLab/server.mjs --fixture=research/PuzzleLab/fixtures/amber-02.json`.
The original `fixture.json` is retained as historical negative onboarding
evidence. Eight deterministic/HTTP tests now pass, including the second case's
uniqueness, per-clue necessity and compact count wording.

Case 02 feedback: the player independently articulated the correct answer,
liked rich multi-tag cards, and rejected the three parallel exact-one clues as
boring ordinary-play content. Formal submission is not yet observed. Current
state and narrated reasoning are preserved in the case-02 player checkpoint.

Next: allow the player to submit/finish the current case, then author a new
precommitted positive case with distinct interacting clue roles. Do not fix
repetition merely by paraphrasing the same constraints. Capture subjective
interest before expanding to mature and three-slot fixtures. Technical smoke
tests and successful deduction are not player acceptance of puzzle quality.

State lives only in server memory. A restart or valid fixture replacement clears
it. Preserve a player journal before stopping during live calibration.

## Why this exists

AlchemyRiddle has moved from broad architecture discovery into repeated puzzle
calibration. Text-only paper prototypes remain valid evidence, but they are now
slow for the expected volume of blind iteration and make it harder to evaluate
interaction flow, notation, candidate marking and future UI ideas.

The local **Puzzle Lab** should shorten that loop.

Its immediate purpose is:

`define fixture -> play it quickly in a browser -> capture player reasoning / friction -> revise fixture or generator rule`.

A later standalone showcase version is a useful possible descendant, but it is
**not** the current requirement and must not distort the research tool.

## Current environment state

As of 2026-10-07:
- ChatGPT Desktop / Codex is working stably for the user;
- the local AlchemyRiddle repository is open in Codex;
- local localhost and presentation live-reload development were verified during
  V0 bootstrap; server/rules changes require a restart;
- repository/canonical docs, not chat history, remain the recovery source.

Local Codex must first inspect its checkout/worktree, branch, HEAD and local
changes under `DevRules/CODEX_WORKFLOW.md` before synchronizing with remote work.

## Product question the first Lab must serve

The highest-leverage open design question is **inference quality / intellectual
interest**, separate from numerical difficulty.

The first Lab-backed calibration should test whether short puzzles contain
genuine cross-clue inference rather than flat filtering.

Accepted negative examples include:
- several same-slot unary exclusions that merely eliminate candidates one by
  one;
- an implication paired with another clue that directly states its antecedent,
  collapsing the conditional into a disguised literal.

Positive cases should make one fact change the usefulness or interpretation of
another fact, ideally creating a compact player-articulable "aha" step.

The immediate calibration set remains:
1. a simple/easy two-slot positive case;
2. a RICH two-slot case;
3. a mature MAX/BOSS two-slot case;
4. one representative three-slot case.

Do not build a corpus-wide generator before these positive structures are
player-calibrated.

## V0 acceptance envelope

The smallest useful local tool should:

1. run locally in a normal browser on localhost with a short repeatable dev
   command and fast reload;
2. load a **synthetic puzzle fixture** without embedding its logic directly into
   presentation components;
3. show the candidate reagents/cards, their visible properties and surfaced
   clues needed by the fixture;
4. let the player perform the currently needed puzzle interactions directly in
   the UI instead of describing every move in chat;
5. support lightweight player-owned candidate marking/exclusion if it is cheap
   enough to add without inventing final production semantics;
6. preserve a clean **player mode** that does not expose the hidden answer or
   facilitator-only state;
7. provide a separate **debug/facilitator view** sufficient to verify the hidden
   answer, live candidate set and clue semantics while authoring fixtures;
8. make it cheap to replace one fixture with the next calibration case.

For the first V0, a static/local fixture file is sufficient. Persistence across
browser restarts, a database, accounts and cloud storage are not required.

## Architecture preference, not production commitment

Prefer a thin separation:

`puzzle fixture/model -> puzzle rules/evaluation -> web presentation`

The reason is research ergonomics:
- the same fixture can be rendered differently without rewriting its semantics;
- hidden facilitator state can stay separate from player presentation;
- puzzle logic can later receive automated tests;
- a future standalone web showcase can reuse the research model if that remains
  advantageous.

This is **not** a decision that the Graveyard Keeper mod must use the same web
technology or source code. The eventual production mod remains a BepInEx/C#
runtime integration and will need separate evidence gates.

Do not generalize the engine beyond current fixture needs merely for elegance.

## Explicit non-goals for V0

Do not spend time yet on:
- public deployment or hosting;
- accounts/login;
- multiplayer or remote sessions;
- polished standalone-game branding;
- final Graveyard Keeper visual imitation;
- production journal layout;
- localization framework beyond what is necessary for test readability;
- analytics backend;
- save migration;
- exact in-game persistence ownership;
- generalized authoring tools;
- full real-corpus recipe import;
- production mod hooks.

If a feature does not materially shorten or improve the next blind calibration,
defer it.

## Evidence boundary

Puzzle Lab is a **research harness**.

It may provide:
- exact deterministic fixture state;
- interaction ergonomics;
- repeatable blind presentation;
- action/session trace if cheap;
- faster visual iteration.

It does not prove:
- real Graveyard Keeper UI ownership/lifecycle;
- production save persistence;
- in-game pause behavior;
- BepInEx integration;
- actual resource/economy balance;
- subjective puzzle quality without the player's blind test.

The user remains the player for perceptual/subjective calibration. The tool
must not silently solve deductions on the player's behalf.

## First execution checkpoint

Before creating substantial new harness code, answer:

**Question:** Can a minimal local web surface materially accelerate the next
inference-quality blind prototypes?

**Existing path:** text paper prototypes work but require repeated manual
state presentation and slow interaction.

**Justification for the Lab:** the upcoming work expects repeated matched
fixtures and interaction/UI iteration; a tiny local browser harness removes
mechanical presentation overhead while preserving the existing blind-prototype
semantics.

Therefore a minimal local Puzzle Lab is justified. Keep it narrower than a
standalone game until evidence requires more.

## First local sequence

1. Inspect local checkout/worktree and synchronize safely with current remote
   canonical state.
2. Verify a minimal localhost/hot-reload cycle.
3. Select the smallest web stack already practical in the local environment;
   do not choose a framework for hypothetical future deployment.
4. Implement one synthetic two-slot fixture with strict player/debug separation.
5. Use that fixture to rebuild the next **positive** inference-quality prototype.
6. Blind-test it with the user.
7. Only after the interaction loop is useful, extend the Lab to the remaining
   calibration fixtures and then to the representative three-slot case.

No installed Graveyard Keeper runtime test is required for this research-tool
bootstrap.
