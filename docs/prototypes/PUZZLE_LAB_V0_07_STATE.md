# Puzzle Lab V0 case 07 — player checkpoint

2026-10-07. Completed blind play, explicitly positive user feedback.
Synthetic target: Фонарь переправы. Three slots, three candidates each.
Canonical pool, exhaustive visible tags and rendered clues: lantern-07.json
under research/PuzzleLab/fixtures. Facilitator model is separately frozen in
LANTERN_07_FACILITATOR.md; do not surface its contents during blind play.

Initial visible pair knowledge, all stable:
- Пыль окаменевшего вереска + Сок болотного плюща.
- Пыль лунного папоротника + Раствор серебристой соли.
- Чернила ночного спрута + Эссенция жемчужной раковины.

Exact initial state: Science 1, Research Charges 8; costs 1 each for full
formula / previously unknown adjacent pair. Status playing; selection, marks,
notes and action history empty. Three initial observations, no personal tests.
All later outcomes are retained, including incompatible results. No refill.

UI revision requested after case 06: remove personal exclusion controls;
link journal observations to cards with compact П/Ж/Э + row codes and hover/focus
highlight; emphasize full formula as final answer. Pair-status and journal-origin
layout received positive user feedback; revised identity scanning remains to be
evaluated. Do not count mechanical UI QA as human puzzle play.

## Completed play — 2026-10-07

Browser observation and narration agree: p2/f3/e2 selected, status solved,
Science 0, Research Charges 5, notes empty, marks empty (controls absent).
Exact action history: f2e1 incompatible; f2e3 incompatible; p2f3 stable;
complete formula success. Known relations: three initial stable observations
plus these three personally tested observations. No failed synthesis. Frozen
fixture/outcomes unchanged during play; no facilitator deduction supplied.

Narration: follow p1f2 bridge, use mineral count to reject e2, test both remaining
continuations e1/e3 and reject this bridge. Briefly inspect p3f1, then notice
the implication's uniquely identifiable Water Powder / Animal Essence terms.
Switch to p2/e2, scan fluids by visible pair knowledge, recognize known f3e2,
test missing p2f3 stable, submit successfully. The player treated the authored
conditional as a promising lead because conditions usually do useful work.
This is an author-intent heuristic, not a logically forced affirmative premise:
the implication does not require Water Powder, and tags never imply stability.
Do not count this shortcut as proof of deeper cross-clue deduction.

User response: pleasant, fairly relaxed puzzle solving; strongly positive to
pair-state visibility and incompatible-result readability. Clearer UI appeared
to make the puzzle easier in a welcome way by reducing remembering/cross-checking
work. This is subjective feedback from one case, not a controlled UI comparison
or calibrated difficulty threshold. Higher logical challenge now appears worth
testing, without expanding candidate count or claiming a mature/boss contract.

Requested refinement: candidates, composition clues and observations should
dominate attention; large research/final blocks should recede without moving
actions far from candidates. Clicking any journal observation should clear the
old selection and select only its two components. Show the observed two-edge
chain near the final formula; stable edges must not imply target validity.
An all-clear/reset control was merely uncertain speculation, not an accepted need.

Next: review the refined workspace on this completed case, then test a fresh
example with stronger logical interaction after recording the exact new model.
