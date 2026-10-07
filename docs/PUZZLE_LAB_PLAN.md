# Puzzle Lab local research tool — working plan

Status: **V0 implemented on research/puzzle-lab-v0; cases 03, 04 and 05 accepted as positive two-slot exemplars; cases 06 and 07 accepted after three-slot play. Case 08 ended with a UI-confounded failed synthesis; layout revised and three final checks accepted for future models. Not production UI architecture; no Graveyard Keeper runtime behavior is changed**.

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

Current active fixture: `lab-v0-08`, synthetic target Печать прилива, with
three slots, three varied target clues, prior adjacent-pair observations and paid pair research.
Completed checkpoint/next point:
`docs/prototypes/PUZZLE_LAB_V0_08_STATE.md`. No player-facing
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

## Attention hierarchy and case-07 outcome — 2026-10-07

Case 07 completed: f2e1 incompatible, f2e3 incompatible, p2f3 stable, final
p2f3e2 success. Science 0, Research 5, six observations, no notes/marks.
User accepted the pleasant relaxed puzzle and highly legible known/unknown pair
states; perceived reduced UI burden is not a controlled before/after experiment.
Unique conditional terms offered an author-intent shortcut, not logical proof
that a premise must be true. See the exact checkpoint for narrated reasoning.

Visual priorities: candidates and composition/empirical information first;
research actions second, final submission a distinct compact action rather than
a large contrasting region. Reduced action fills/borders/size, stronger primary
headings/card text/clues. Actions remain below candidates on desktop; narrow
layout and DOM order are candidates -> evidence -> actions. Guidance consulted:
https://www.nngroup.com/articles/visual-hierarchy-ux-definition/ and
https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/.
These inform presentation choices; human hierarchy acceptance remains open.

Click/Enter/Space on any journal observation atomically selects exactly its two
components, clears the third slot, costs nothing and adds no history. Server
accepts only observations already known in that session; budgets/notes/marks/
terminal status unchanged. Both positive and personally learned negative entries
are selectable. A compact final-answer chain shows observed stable/incompatible/
unknown edges only; never evaluates tags or signals that the formula is correct.

All 17 tests pass, including pair-selection validation and state preservation.
Browser confirmed mouse and keyboard pair selection, clear-third semantics,
unknown/incompatible/all-stable final summaries, and no errors. Actual viewport
1917x1065: main core ends at y~757; no nominal smaller-size claim is made.
Server restarted for new action, then the original three tests and successful
synthesis were restored mechanically and verified against the recorded history,
selected p2/f3/e2, budgets 0/5 and six relations. This is technical restoration,
not another human playtest. No reset button added from tentative speculation.
Next: user reviews hierarchy revision on completed case 07, then a fresh stronger
logical-interaction example; generator acceptance and mature/boss remain open.

## Legibility refinement and case 08 — 2026-10-07

User found the quieter hierarchy too small and caption-heavy. Retain the hierarchy
but increase reading text/statuses: 16px core facts and formula message, 15px card
names/chosen formula tiles, 14px action buttons/costs. Journal names 13px, codes and
tags 12px. Remove repeated selected names from pair controls; show identity codes
beside actions. Replace the tiny final chain with three full-name selected tiles
and one contextual observed-state message once all slots are selected. No automatic
tag checking, synthesis blocking by inferred validity, or changes to paid actions.
Hide duplicate incomplete-formula instructions; placeholders already show missing
slots. Move the card click instruction into the existing disclosure.

New lab-v0-08, Печать прилива, tide-08.json: four necessary interacting clues,
three stable initial bridges, five Research Charges and one Science. Complete
model and author hypotheses frozen in TIDE_08_FACILITATOR.md before play. Eighteen
tests pass including uniqueness, clause necessity, no initially complete known
target chain, linked conditionals and a five-test branch-first route. This is a
new blind model; do not retrofit case 07. Subjective depth awaits human evidence.

Browser QA on completed case 07 confirmed selected full-name tiles and large
stable-message display. Binding old tab 17 timed out on focus emulation; a fresh
visible tab 19 loaded immediately. Exact cause is unknown, not diagnosed as a
server fault. Primary server restarted with tide-08.json; new tab verified title,
four clauses, three priors, no selection/history, Science 1 / Research 5, no errors.
Actual 1600x900 viewport: core ends at y~778. This initial state remains untouched
by pair investigations or synthesis. Tab retained as deliverable for human play.
Current exact checkpoint: docs/prototypes/PUZZLE_LAB_V0_08_STATE.md.
Next: fresh blind play with reasoning/UI feedback before debrief.

## Case 08 outcome, information-first scan and future economy — 2026-10-07

Attempt ended with p1f3e1 failure, no pair microtests, Science 0 / Research 5.
Player correctly used Plant -> Animal -> Water and mineral count; all four tag
conditions fit the attempt. The other empirical edge was unknown. Do not expose
its hidden outcome or the answer during debrief. This is useful linked-clue and
UI evidence, not an accepted difficulty band. Exact state/history is in case-08
checkpoint; no model change, reset or new observation added from synthesis.

User accepted THREE final checks for future examples, cost 1 Science each.
Keep case 08 frozen/exhausted; production Science acquisition/refill is still open.
All 19 tests pass, including failure -> continued research -> third-check success
under a three-Science model using the existing evaluator. Presentation now shows
remaining/original final-check counts and price, with a nonterminal failure message
when resources remain. Unknown pairs are a risk, not a prerequisite enforced by
UI; remove the imperative that conflicted with the enabled synthesis button.

New scan layout: candidates top-left; two equally important information blocks
below (composition and compatibility), actions at right. Compatibility block
states the short two-stable-pair requirement; whole-target tag requirement remains
visible. Hide incomplete pair panels rather than showing technical dashes; show
selected formula as plain output, not empty bordered pseudo-inputs. Hide known-pair
buttons, accent the unknown-pair research action. Journal selection stays optional.
Browser verified actual 1151x1065 completed/exhausted state with correct area order,
unchanged p1f3e1, sole failed submission, three prior observations and budgets 0/5.
No errors, resources or hidden model changed during UI revision.

User requests lexical variation in future synthetic powder/essence names, without
names conveying extra properties. Follow the existing slot headers/exhaustive tags
for semantics; do not rename a frozen live fixture.

Research sequence remains puzzle-first: next fresh richer three-slot example with
three checks, then mature/boss contrast; capture reasoning and subjective findings,
distill inference-quality acceptance criteria, then bounded real-corpus screen.
UI adjustments support this sequence rather than replacing it. Counts: eight
presented human calibration cases, separate from nineteen automated checks; case
08 failure is not evidence that the user failed tag reasoning or the selected core.

## Fresh case 09 handoff — 2026-10-07

The prior UI revision did not switch fixtures: the exhausted case 08 remained
visible, including persisted selections and terminal failure text. User perceived
this as a fresh puzzle already failed without submitting. Selection does not
invoke synthesis; persistence itself is intentional. Correct the handoff rather
than erase previous research on every reload.

Case lab-v0-09, Свет под водой, precommitted in lantern-09.json; varied powder and
essence nouns, richer tags, four necessary clauses, unique full answer. Stable-only
priors; 6 research charges, 3 final checks costing 1 Science each, no refill.
Fresh initial state is empty and playing. Checkpoint: prototypes/PUZZLE_LAB_V0_09_STATE.md.
Twenty automated tests cover validity, clue necessity, bounded investigative route,
fresh state and three-check continued play. Next: user blind play and reasoning,
then mature/boss contrast and inference-quality criteria; no difficulty labels.

## Case 09 accepted; compact identity journal — 2026-10-07

Five paid pair tests, one successful synthesis; remaining Research 1 / Science 2.
Player rejected tag/empirical branches and all initial bridges, then constructed
and verified a new chain. Strong positive report of independent research feeling;
count-two welcomed. Exact state and action order in case-09 checkpoint.

Presentation follow-up retains codes alongside different silhouettes rather than
ambiguous icons alone. Powder mound, fluid flask, essence faceted outline are
synthetic slot identities, not new properties. Pair rows omit full names but keep
hover titles, accessible names, linked-card highlighting and atomic selection.
Prior observations use neutral text/no success check; personal stable/incompatible
outcomes remain explicit in words and symbols. Background fills removed. Property
tags vertically centered with inline flex. Local research rule distinguishes one
pair experiment from full synthesis; unknown summary states uncertainty without
contradictory imperative/availability text. No evaluator or resource change.

Design references: NN/g Icon Usability (https://www.nngroup.com/articles/icon-usability/)
for labels with unfamiliar icons; W3C Use of Color
(https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) for redundant symbols/text.
The implementation is an experimental application, not a claim of WCAG certification.
Next research step: mature/boss contrast before quality criteria and corpus screen.

## Case 10 precommit and consistent visual vocabulary — 2026-10-07

User accepted compact journal but requested consistent green check/text for stable
prior and earned pairs. Source headings distinguish origin; large green fills stay
removed. Remove selection dot because selected-card outline already carries the
signal; preserve aria-pressed and repeat-click deselection. Codes optically centered
in usable silhouette interior, rather than a uniform canvas center. Powder shape
now broad rounded mound/scattered grains, unlike flask neck or faceted essence.

Fresh contrast case lab-v0-10, Сердце глубины: 4 candidates per slot, 5 necessary
constraints, 3 final checks, 9 research charges, stable-only priors. Complete hidden
model precommitted in depth-10.json and DEPTH_10_FACILITATOR.md before play. Model
has one full answer and a bounded seven-investigation feasibility witness; this
is facilitator evidence, not a player hint. Checkpoint prototypes/PUZZLE_LAB_V0_10_STATE.md.
Acceptance/difficulty pending. Next: human contrast play, quality criteria synthesis.
Potential further UI simplifications should first be described, not silently
implemented: repeated whole-formula rule, repeated selected names vs card codes,
and explanatory copy only when relevant. Do not sacrifice return-from-pause clarity.
Browser handoff verified in tab 20: title Сердце глубины, all selections empty,
3/3 final checks, no result text/history. Tab 19 timed out during reload/close;
fresh tab loads normally, root cause unknown. Twenty-one tests pass. Larger pool
uses slightly tighter card padding while preserving font sizes. No player action
or research performed in handed-off session.

## Case 10 accepted and help simplified — 2026-10-07

Actual route: p1f2 negative, p1f3 stable, f3e1 negative, f3e3 negative, p1f4 stable,
f4e1 stable, then successful full synthesis. Six research charges spent, one
Science; remain Research 3 / Science 2. Player followed a single branch, occasionally
experimented before checking every clause, then explicitly validated final tags.
Positive acceptance of substantial investigation and structured larger interface.
Not a calibrated boss/hard classification. Exact outcome in case-10 checkpoint.

Remove bottom notes/history/download controls and duplicated whole-formula rule.
Retain compatibility observations (essential puzzle memory) and server-side action
history for reproducible research. Rewrite disclosure as goal -> choose -> learn
pairs -> check all clues -> final synthesis; small reference for counts/conditionals,
free choices, finite costs, hover/click linkage and refresh continuity. No evaluator,
resource or prior knowledge change. Final action Смешать и проверить with subtle
alchemy styling; no animation, hidden information or misleading readiness signal.

Row-color suggestion remains a proposal: shared hue across slot positions could
be read as a matching/compatible set, while property tags already use colors.
Retain slot silhouettes/codes and the current restrained palette for now.
Next: distill quality acceptance criteria from cases, then bounded corpus screen;
no need to produce another example merely to extend the count.
