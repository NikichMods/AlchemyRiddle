# Puzzle Lab local research tool — working plan

Status: **V0 implemented on research/puzzle-lab-v0; cases 03, 04 and 05 accepted as positive two-slot exemplars; case 06 accepted after three-slot play; case 07 precommitted and ready for blind play with stable-only starting bridges. Not production UI architecture; no Graveyard Keeper runtime behavior is changed**.

## Current execution checkpoint — 2026-10-07

Implementation and run instructions: `research/PuzzleLab/README.md`.
Local command: `node research/PuzzleLab/server.mjs`; player URL:
`http://127.0.0.1:4173`.

The minimal stack is Node.js 24 built-ins plus HTML/CSS/browser modules, without
package dependencies. Fixture data, rules/evaluation, server projection and
presentation are separate. Five synthetic two-slot fixtures and one three-slot fixture preserve their precommitted models;
subjective findings are recorded separately for each case.

Implemented: card selection, personal exclusions, notes, paid binary submission,
player journal export, optional facilitator truth-table/session view, and live
browser reload for presentation/fixture edits. Answer and evaluator stay on the
server; debug routes require explicit `--debug`. One Science/one submission is
this fixture's bounded calibration budget, not accepted production balance.

Verified locally on Node 24.19.0: fifteen deterministic/HTTP tests pass, including
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

Current active fixture: `lab-v0-07`, synthetic target Фонарь переправы, with
three slots, three varied target clues, prior adjacent-pair observations and paid pair research.
Completed checkpoint/next point:
`docs/prototypes/PUZZLE_LAB_V0_07_STATE.md`. No player-facing
difficulty labels or progression indicators are added; progression presentation
is a separate open product decision. The user found the colored tags attractive
and the revised layout somewhat better; finer UI polish is deferred.

Run the current case:
`node research/PuzzleLab/server.mjs --fixture=research/PuzzleLab/fixtures/harbor-06.json`.
The original `fixture.json` is retained as historical negative onboarding
evidence. Fifteen deterministic/HTTP tests now pass, including the fourth case's
uniqueness, per-clue necessity and overlap/forbidden-conjunction semantics.

Case 02 feedback: the player independently articulated the correct answer,
liked rich multi-tag cards, and rejected the three parallel exact-one clues as
boring ordinary-play content. Formal submission is not yet observed. Current
state and narrated reasoning are preserved in the case-02 player checkpoint.

The user requested the next example after case 02 reasoning; no formal case-02
submission result is asserted. Case 03's model is precommitted before play.
Shared-property is a narrow fixture predicate, defined in the visible rules;
forbidden conjunction is a target-specific logical constraint, not a change to
the selected two-slot architecture or a chemistry experiment relation.

Case 03 completed successfully in one paid submission. The player liked lively
but precise wording and chose a plausible Fluid first, inferred the Powder's
required property and checked overlap without exhaustively inspecting all cards.
Exact final state/reasoning are in the case-03 checkpoint. Retain as a positive
wording/short-hypothesis case; do not claim the intended deeper elimination path
was actually used or that mature inference quality is calibrated.

The user subsequently accepted the whole case 03 as a pleasant initial puzzle
and requested next play. Preserve it as a positive initial exemplar. Case 04
is precommitted to test richer card interaction and an active conditional;
generic conditional semantics are visible before play.

Case 04 completed with one successful submission. The player explicitly enjoyed
richer interacting constraints and independent branch reasoning, estimating
medium or greater difficulty. Retain as a second positive exemplar, without
turning the subjective estimate into a calibrated band. A forgotten tested pair
is evidence for future memory support, not automatic deduction.

After play, exclusion buttons became small red bottom-right crosses with restore
arrows. Full slot frames were removed, the divider retained and colored tags
rounded. Browser toggle/restore and visual checks passed, with solved state kept.
Case 05 completed with one successful submission and explicit acceptance as
pleasant, interesting and subjectively medium. Actual reasoning was systematic
pair rejection, with inactive conditionals understood correctly; the compressed
author chain was not explicitly stated. Preserve the positive experience without
claiming increased abstract proof depth. Exact final state and narration are in
the case-05 checkpoint. UI watch item for the next pass: red cross resembles a
close/remove action; use a different manual-exclusion marker, keeping cards
visible and restoration available. The icon feedback was initially deferred; the next harness UI pass implements it without changing marking semantics.
Case 06 was precommitted before play and is now completed. The bounded harness extension supports three
slots, prior stable/incompatible observations and unknown adjacent-pair tests.
Science 1 funds one formula check; four separate Research Charges fund pair tests
at cost 1. No refill; spent research charges do not block remaining synthesis.
All prior observations on the surface are shown without relevance labels, and
no survivor set or deductions are calculated for the player. This is one frozen
knowledge state of the accepted three-slot core, not a generator or game mod.
The marker now uses a slashed circle instead of a close-like red cross.
Next: review the compact workspace with the preserved completed case, then precommit a stable-start example,
then continue calibration
toward mature/boss and three-slot calibration. Technical
smoke tests and successful deduction are not blanket acceptance of puzzle quality.

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

## Three-slot Lab extension checkpoint — 2026-10-07

Case 06 uses the selected three-slot grammar in one frozen synthetic knowledge
state. Automated checks cover 27 triples, every clue's necessity, initial partial
anchors, no initial known complete target-compatible chain, adjacent-only tests,
independent budgets, free invalid/repeated requests, final synthesis and public
projection/session continuity. All 14 tests pass. Isolated browser checks on
port 4174 verified both research buttons, raw observations, charge spending,
three selections, exclusion/restore and the three-column layout. This technical
session is separate from the untouched blind-play state on port 4173.

The browser check caught an incomplete-pair display incorrectly matching a
different prior relation. Lookup now checks both relation slot identities and
both selected cards. Conditions are placed immediately below cards, before
research controls, to avoid burying them beneath the observation journal.

Collaboration preference is canonical in AGENTS.md: execute obvious agreed next
steps autonomously; check before major unaccepted direction/mechanics/scope
decisions. Do not ask for permission merely to carry out an already accepted step.

## Compact workspace checkpoint — 2026-10-07

Case 06 completed successfully: three pair investigations, no failed synthesis,
one successful complete formula; Science 0, Research Charges 1. Explicit positive
acceptance, subjective medium / medium-high. Detailed exact history/narration:
`docs/prototypes/PUZZLE_LAB_V0_06_STATE.md`.

Requested workspace changes are implemented: three candidate columns with
repeat-click selection/deselection; pair actions and formula action immediately
below them; observed pair statuses beside each action; target clues and relation
journal alongside candidates. Stable/incompatible entries differ by color and
symbol; initial/current-investigation observations and pair types are separated;
matching selected pairs highlighted. General rules consolidated under a single
reference disclosure, notes/history under another. No automatic tag reasoning.

Tests: all 15 pass, including server toggle semantics, invalid incomplete synthesis
and unchanged pair/Science budgets. Isolated browser verification confirmed
repeat-click deselection, unknown/known-incompatible states, new observation
classification and matching highlight. At actual 1600x900 viewport the core fit
without scrolling; other sizes are not claimed from that check. A requested
1280x800 viewport override reported 1600x1000 in the page, so it is not evidence
for the nominal size; override reset. Small screens use a stacked layout.

The server must restart for new action semantics. Preserve the completed case
by reconstructing its previously recorded three pair actions and successful
submission, then verify the resulting state matches the saved checkpoint. This
technical restoration is not a second human playtest.

New accepted initial presentation: only STABLE pair observations at entry; once
research begins, keep and display all new outcomes. Do not retrofit case 06's
frozen mixed-polarity model. This supersedes the previous all-polarities initial
surface for new fixtures. Cross-investigation negative-history reuse remains
unspecified; do not delete durable history. Next: review layout, then precommit a
new three-slot example under the stable-start policy; mature/boss quality open.
Completed-state restoration was browser-verified against the pre-restart record:
three pair outcomes in the same order, one synthesis success, selected p2/f2/e2,
Science 0, one Research Charge, eight observations (three personally tested),
empty notes and all marks off. The current visible viewport measured 1151x1065
and the core ended at y~781. Two-slot browser regression also passed.

QA session note: localhost ports on the same hostname share the browser cookie;
a secondary-port browser session can replace the primary Lab cookie. Run all
secondary UI checks before final primary-session restoration, or use a separate
hostname/profile. Final primary restoration was rechecked through page reload
only after temporary servers/tabs were closed; budgets, journal and selection
still matched the completed player record.

## Stable-start example and identity scanning — 2026-10-07

Case 07 (Фонарь переправы) precommitted with three stable initial observations,
three interacting tag clues, exhaustive deterministic adjacent outcomes and a
unique target. Research budget 8 / Science 1 are synthetic calibration quantities,
not production balance. All 16 tests pass, including absence of an initially
known complete target chain, clue necessity, retention of negative discoveries
and branch-first exhaustive rejection within budget. Shortest route may be much
shorter; no subjective difficulty claim is made before human play.

Remove exclusion controls from candidates, while retaining historical API/data.
Card codes П1/Ж1/Э1 are repeated in journal entries; hover or keyboard focus on
an observation highlights its two candidate cards without changing selection or
adding deductions. Full synthesis has a separate Финальный ответ accent.
Browser verification on actual 1151x1065 viewport: no exclusion controls, exactly
two highlighted candidates on journal focus, core ends at y~774. Fresh player
state has Science 1 / Research 8, three stable initial observations and no actions.
The primary server now runs lantern-07.json; current user tab is retained as a
deliverable. Checkpoint: docs/prototypes/PUZZLE_LAB_V0_07_STATE.md.
Next: human blind play and feedback on the identity scanning aid, then debrief.
