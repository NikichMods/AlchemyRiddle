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
