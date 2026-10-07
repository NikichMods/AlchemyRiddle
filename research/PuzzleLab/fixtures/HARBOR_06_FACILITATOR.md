# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

Precommitted 2026-10-07: lab-v0-06, `harbor-06.json`, synthetic Тихая гавань.
Three slots, three cards each, 27 triples. Answer p2+f2+e2. No real recipe.
Complete pool, exhaustive tags, target conditions, prior knowledge and stable
edges are frozen in the fixture. All other adjacent edges are INCOMPATIBLE,
which fully defines the deterministic 18-pair table. No non-adjacent tests.
Names convey no extra rules. No hidden observations or mid-play adaptation.

Research-method checkpoint: representative three-slot play needs the selected
adaptive knowledge-aware grammar, not merely a third column of static tags.
The existing Lab lacked adjacent tests/known observations. A narrow extension
adds those interactions and a three-slot layout, reusing the same server/session,
clue rendering, notes, manual marks and binary formula verification. This frozen
prior-knowledge state represents one case, not a production adaptive generator.
Production architecture/gates and real-game integration remain untouched.

Visible rules: all three target clues simultaneously true; each adjacent pair
Powder+Fluid and Fluid+Essence must be stable for a valid formula. Stability alone
does not imply a valid target. Tags neither predict compatibility nor require
overlap. Microtest a selected adjacent pair: stable/incompatible, no partial
target score. All five previously learned pair observations on this surface are
shown neutrally, with no answer-relevance label. Some stable anchors are dead ends.

Author's hypothesis, not player-earned facts: target clues leave 9 triples across
4 Powder/Fluid branches. Initial incompatibilities remove p3+f1 and f1+e2,
leaving four hypotheses: p1f3e2, p2f1e1, p2f2e1, p2f2e2. Two competing branches
have a stable first edge; the answer has a stable second edge but an unknown
first edge. No target-compatible full stable chain is known initially.
Unknown edges distinguishing these hypotheses: p2f2, f2e1, f1e1, f3e2.
Actual table outcomes: stable, incompatible, incompatible, incompatible.
A short route tests p2f2 and f2e1, using known f2e2 to finish; alternate branch
falsification routes are equally legitimate. No automatic surviving-set display.
Every target clue is necessary against the full hidden table. Removing count,
implication, prohibition restores, respectively, p2f1e3, p1f1e3, p3f2e2.

Resources: Science 1 for one full-formula check, cost 1, no refill. Research
Charges 4, each previously unknown adjacent-pair test costs 1, no refill. This
covers all four relevant unknown edges, with no need for failed full synthesis.
Repeated known-pair requests cost nothing and add no duplicate history; UI disables
them. Invalid/incomplete/non-adjacent requests cost nothing. Selection, marking,
notes and export free. Success -> solved; failed full formula -> exhausted;
no further research after either terminal result. Exhausting Research Charges
does not prevent a remaining Science-funded synthesis. No acquisition costs.

Initial state: all selections/marks/notes/action history empty; Science 1,
Research Charges 4, five initial observations. Formula check disabled until all
three slots selected; pair buttons disabled until their two slots selected.
Exclusion icon is a slashed circle with restore arrow, never removes cards.
Previous case 05 is completed and persisted before restart.
Player checkpoint: `docs/prototypes/PUZZLE_LAB_V0_06_STATE.md`.
Next: blind human play. Capture reasoning and subjective response before
explaining the intended path; do not treat this as mature/boss acceptance.

## Human outcome — 2026-10-07

Completed with three pair investigations and one successful synthesis; explicit
positive acceptance. Actual route: f3e2 incompatible, f1e1 incompatible, p2f2
stable, then p2f2e2 success. Final state/narration and UI findings are canonical
in the case-06 player checkpoint. No model changes during play. Subsequent user
clarification selects stable-only initial bridges for future fixtures; preserve
this mixed starting-knowledge case as historical evidence.
