# Friends three-slot trial 04 — Elixir of vigor

2026-10-10. Current synthetic post-tutorial three-slot candidate. Human ease and
interest are unverified; production remains BLOCKED. No unknown vanilla recipes.

## Feedback and accepted presentation

User reports a playtest and requests restored card elimination marks and an
explicit statement of unique solution at the start. No specific player outcome,
completion time or difficulty verdict was supplied; do not invent one from this
feedback. These UI improvements apply to both supported arities.

Every card now has a free `Вычеркнуть` / `Вернуть` toggle. The existing server
`mark` action persists player-owned marks without changing selected components,
Science, rules or observations. Names are struck through; properties remain
readable, cards remain selectable, and a marked card can be restored. This is a
personal hypothesis, not automatic elimination by the system. Help states these
semantics. Above the board: `У загадки ровно одно решение.` The assertion rests on
server fixture validation of exactly one full-model answer, including compatibility
for the three-slot core; tag-only hypotheses may remain multiple.

## Frozen model and recovery

- ID `lab-friends-three-slot-04`, title `Эликсир бодрости`.
- Fixture SHA256 `3a6e0308704e97896fefde992488080a403cc968c07a2f16417d64f4f2ff8f76`.
- Private preparation `friends-three-slot-04/`: original bounded authoring script,
  complete spoiler-labelled precommit, frozen fixture, initial public state,
  aggregate audit, independent engine replay and browser screenshot. Full answer,
  graph and policy traces must not surface during blind play.
- Active private directory remains historical `starter-2x2/`, separate durable
  sessions outside Git. Player server 4184, local-only facilitator panel 4185;
  retained Start/Stop/Status wrappers and panel controls continue to work.
- Previous trial 03 archived before replacement in
  `starter-2x2/archives/easy-03-2026-10-10/`, including all sessions, QA, frozen
  model, precommit, aggregate, initial snapshot and statistics export. Manifest
  verifies 12 model/session/QA files byte-identical. Prior archives preserved.
  Original solved case-20 session hash remains unchanged.

## Preflight and intended experience

Use the accepted three-slot core with a smaller 3x3x3 field, two short necessary
composition conditions, and two prior stable pairs. Nine fresh fictional reagents
have coherent exhaustive properties. Illustrative budget remains 30 shared
Science; pair check costs 2, whole synthesis 5, no refill. Canonical generator
weights, puzzle semantics, production economy and accepted layout unchanged.

Full field 27; compatible before clues 6; tag-only hypotheses 6; unique full
answer 1. Omitting the respective clues leaves 4/3 full-model answers, so neither
condition is redundant. Initial tag hypotheses retain at least two candidates
per role. Known priors are target-relevant and do not certify the answer upfront.
Seven unknown hypothesis edges; even checking all seven plus synthesis costs 19.
All four tied highest-current-hypothesis-coverage routes take three informative
pair checks and final synthesis, cost 11. Worst witness replayed through the real
engine reaches solved. Policy routes are bounded strategy evidence, not measured
human actions or a promise that every play style takes three checks. This is an
intended post-tutorial candidate on the independent three-slot ladder, not an
implemented tutorial or campaign progression.

## Verification

Source `5284e627164919ca83294c127f4791bc7b2b6a22`: 51 local tests pass; CI success:
https://github.com/NikichMods/AlchemyRiddle/actions/runs/38064369707
No new runtime mechanics; restored UI consumes the existing validated mark path.
Browser visibly shows all nine toggles and the uniqueness sentence. Arbitrary
mark -> reload -> restore works, leaves choice empty and Science at 30. Final
browser preview restored to unmarked state; preview classified test in private
statistics, not a participant result.

Two fresh HTTPS cookie sessions verified: QA A's free mark persists, one unknown
pair costs 2, refresh preserves mark/history and 28 Science; QA B remains at 30
with no mark or paid history. QA identities kept private and classified test.
Refill POST returns 400. Public model/debug/facilitator/statistics export paths
return 404. Same assigned public ngrok URL serves the new fixture and source
assets; panel reads only the current trial. These are host/public-route and
in-app-browser observations, not independent-network or Yandex confirmation.

## Next interaction

First independent player choice. Show raw observations and preserve the journal;
do not derive the solution for the player. After natural completion, collect
whether marking and the unique-solution statement clarified the task, and whether
the smaller three-slot field fits the intended post-tutorial ease.

## Human feedback and presentation revision (2026-10-10)

User reports a returning playtester selected the first known stable pair, chose
the first essence satisfying the composition clues, and succeeded on the first
synthesis without pair research. The tester reports a sense of guessing rather
than competence, boring/non-thought-provoking clues, and a perceived advantage
for residual enumeration. This is reported human evidence, not a reconstructed
identity or measured duration. Do not replace it with the earlier policy witness
or treat the user's separate screenshot as the same session: its displayed
journal includes paid pair checks, unlike the narrated one-synthesis route.

A direct frozen-model audit confirms: the first prior has two composition-valid
extensions, one full answer, and the first extension in card order is the answer.
Worst-case direct residual synthesis enumeration costs 10 Science against a 30
pool. The other prior has one composition-valid extension and no full answer.
Do not reveal these branch details during independent play. Existing 3-check
policy witnesses are valid routes, not shortest-policy evidence or proof that
users benefit from choosing them. The candidate fails its intended subjective
post-tutorial deduction experience in this reported playtest; uniqueness and clue
necessity are insufficient. Retain this frozen candidate as diagnostic evidence,
not a positively accepted difficulty example. This does not reject the entire
three-slot core. Recommended next investigation: compare the cheapest residual
search after each prior with informative research and ask whether the clauses
create a useful inference; selection weights/gates remain unchanged pending
agreement, rather than raising prices or adding arbitrary checks.

User explicitly requests compact historic elimination controls, second-click
pair deselection and the supplied desktop block order. History `ccf3c34` confirms
`×` / `↶` icon controls and dashed excluded cards. Current restoration also dims
the marked card; properties remain legible, existing personal mark semantics stay.
Journal first click selects only that pair. When its two components are already
selected, clicking clears those two slots and retains an unrelated third choice.
No Science or journal outcomes change; observations remain visible. Regression
checks include known positive/earned negative pairs, retained third selection and
invalid/unearned relation rejection. Repeated pair choice is now a toggle, an
explicit user-authorized selection behavior change; formula semantics unchanged.

Desktop layout matches the supplied grouping: candidate board at upper left,
pair research and selected formula at upper right; below, final synthesis left,
composition clues middle, compatibility journal right. Narrow screens stack
board, clues, journal, chosen research/formula, synthesis, preserving accessible
controls and a reading order before paid verification. Original model, priors,
answer and fixture hash unchanged. Local source suite: 51 pass. Source
`63e771e71f88cf44a542e07ac8af4542d9c58e4b` CI success:
https://github.com/NikichMods/AlchemyRiddle/actions/runs/38065902583
A subsequent whitespace-only cleanup accompanies this record.

Owned player/tunnel restarted to activate server selection semantics; no session
files removed or model replacement. A live before/restart comparison checks 8
existing states, with 7 equal and 1 different during overlapping live access;
no before snapshot was retained to attribute that difference. Do not claim all
states byte-identical from that observation. Browser QA confirms pair select then
second-click deselect, free mark persistence after reload, icon return and empty
final choice at 30 Science. Preview remains classified test. Desktop screenshots
with marked/unmarked cards kept privately; no independent-network claim added.

## Subsequent user correction — 2026-10-10

The user rejects the implemented block layout, accepts mark/toggle behavior, and
requests a slashed-circle exclusion icon. It supersedes the cross iteration.
Repeated reported first-guess success raises a structural generator hypothesis;
see ../research/PUZZLE_LAB_UI_HIERARCHY_2026-10-10.md for the soft-penalty
direction and pending UI proposal. No live fixture, order, sessions or scoring
changed by this correction.

Icon-only verification: JavaScript syntax and whitespace checks pass; the actual
public page reload displays ⊘ for exclusion. A private viewport screenshot was
visually inspected. No process restart or session actions were necessary.

## Workbench activation — 2026-10-10

User selected the two-zone workbench, split liquid outline, centered exclusion
SVG and soft preparation-order pass. Implementation and verification are owned by
../research/PUZZLE_LAB_UI_HIERARCHY_2026-10-10.md. The pass was verified against a
separate private review copy; the live frozen fixture/order/hash remain unchanged.
Existing classified browser QA session spends 2 Science to verify an earned
negative right edge and persists marks/selection after reload. Human sessions
are not reset; no serving process restart. 55 local tests pass.
