# Puzzle Lab local research tool — working plan

Status: **V0 calibration completed through case 10; interface accepted as sufficient
for the laboratory; inference-quality synthesis complete; production remains BLOCKED**.

## Current execution checkpoint — 2026-10-07

Completed trial: anonymous real-corpus case 11, recorded in
prototypes/PUZZLE_LAB_V0_CORPUS_11_STATE.md. Generator gates, weak route term and
field floor retained. Shared Science 20, pair 2, triple 5, unlimited +10 Lab refill.
Private fixture and durable session stay outside Git. Solved: 13 pair checks,
two submissions, seven pair checks outside tag-valid hypotheses. Human pacing
acceptance remains open; next proposed review is within-puzzle repetition and
branch-tracking burden.
This assesses human investigation, not acquisition balance.

Read [PUZZLE_QUALITY_CONTRACT.md](PUZZLE_QUALITY_CONTRACT.md) for the consolidated
results, evidence limits and working evaluation rubric. The ten individual
checkpoints remain the source for exact paid actions and narrated reasoning.

- Seven positive cases: 03–07, 09–10; negative 01/02; failed/UI-confounded 08.
- Five two-slot and five three-slot frozen fixtures; no active blind play.
- Served case 10 remains solved: Science 2, Research 3, p1/f4/e1 selected.
- Current UI: candidates and both information sources, nearby pair experiments,
  final synthesis, compact identity journal and expandable action-oriented help.
  Manual exclusions and bottom notes/history/download controls are removed.
- Observed pair results and server-side paid-action history remain available.
- Three final checks apply to 09/10; do not rewrite earlier one-check fixtures.
- 21 deterministic/HTTP tests pass. Node 24 built-ins, no package dependencies.
- Routine interface work is complete by explicit user acceptance. No difficulty
  labels/progression UI or production UI architecture is selected.

Current case reproduction (starts a fresh session if server is restarted):

```sh
node research/PuzzleLab/server.mjs --fixture=research/PuzzleLab/fixtures/depth-10.json
node --test --test-isolation=none research/PuzzleLab/lab.test.mjs
node research/PuzzleLab/audit-calibration.mjs --write
```

URL: http://127.0.0.1:4173. Keep the currently completed session during analysis.
Presentation reload preserves state; restart/fixture replacement clears process
sessions. Historical outcomes must be recovered from checkpoints, not recreated
as new human trials. Occasional old-tab timeouts remain of unknown cause; fresh
browser tabs have worked. Run details: `research/PuzzleLab/README.md`.

Next: the bounded corpus diagnostic in the quality contract. Reuse the existing
TagModelScreen tooling/accepted private models; do not repeat architecture choice
or commission an undefined automatic 'interest score'. Further human play should
address a specific remaining question. Dated sections below preserve the earlier
implementation and calibration sequence rather than current-state instructions.

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

## Within-package review completed — 2026-10-08

See research/INTRA_PACKAGE_REVIEW_2026-10-08.md: 209 retained packages, 19 target
groups, same-count varied alternatives at close cached pace. No new corpus search
or human trial. Next owning decision: proposed narrow within-package soft
preference, separate from mistake visibility/recovery. No new weight accepted.

## Active fresh human contrast — 2026-10-08

Case 12 is precommitted and opened on loopback 4175. Recovery:
prototypes/PUZZLE_LAB_V0_CORPUS_12_STATE.md and PAPER_PROTOTYPE_PROTOCOL.md.
Fresh target, two different displayed clause roles, no priors, shared 20 Science,
costs 2/5 and unlimited +10 refill. Player-facing start verified with no selections
or experiments. Keep prior solved case on 4174; restore private durable state
before resuming. No further test or automatic clue feedback authorized.

## Case 12 completed — 2026-10-08

Five target-relevant pair checks, one success, 15 Science spent, no refill, 5 remain.
Ordinary/normal acceptance; no reported confusion or lost condition. Full result:
prototypes/PUZZLE_LAB_V0_CORPUS_12_STATE.md. Preserve solved session. Do not claim
causal validation of repetition weight or mistake recovery; no further trial
launched. Human/save-state generalization remains open, production BLOCKED.
