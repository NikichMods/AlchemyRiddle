# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

Precommitted 2026-10-07: lab-v0-05, `dew-05.json`, synthetic Печать росы.
Two slots, three cards each, nine pairs; answer p2 + f3. No real recipe.
Candidate pool and exhaustive tags are frozen in the fixture and player checkpoint.
Names imply no extra rules. Four clues visible simultaneously at entry:
Powder Mineral -> Fluid Animal; exactly one Water component;
Fluid Animal -> Powder Water; nonempty tag intersection.
Generic implication meaning is visible before play. No difficulty/progression UI.

Research question: can a linked pair of implications make another condition useful
in a new way, with the same six-card field and four-clue count as case 04?
Existing evaluator/harness suffice; no new predicate, solver or game hook needed.
The two implications repeat grammar but have dependent, opposite-slot roles;
this is an intentional test of interaction, not cosmetic sentence variation.
Repetitiveness and intellectual interest remain subject to player judgment.

Author's reasoning hypothesis, not player-earned facts:
Mineral Powder entails Animal Fluid, which entails Water Powder. This rules out
p1. For p3, exactly-one Water forces the non-Water Fluid f2; it lacks overlap
with p3. Thus Mineral Powder is impossible. Remaining p2 lacks Water; the count
forces Water Fluid, and Animal Fluid would require Water Powder. Hence f3.
An alternative player path can start from Fluid Animal and derive the same
contradiction/branch exclusions. Enumerating nine pairs is still possible;
do not assert deeper thinking was used merely because this path exists.
No clue directly supplies an implication's antecedent. Both implications are
vacuously true in the final answer but matter in excluding plausible branches.
Each clue is independently partial and necessary: removing clues 1/2/3/4 adds,
respectively, p1+f3 / p3+f1 / p2+f1 / p3+f2. All alternate valid routes allowed.

Science 1; one complete submission costs 1; no replenishment. Selection,
personal marks, notes and journal export free. Marks neither solve nor constrain
selection. Binary verdict only: exact answer -> solved, otherwise exhausted;
no partial result or answer reveal. Incomplete/invalid submission free.
Marks/notes/export remain available after completion. No hidden experiments,
inventory/acquisition costs, automatic deduction or unsubmitted answer reveal.

Initial state: empty selection, marks, notes, history; status playing; Science 1;
submission disabled until both slots selected. Preserve previous completed case
before switching servers. Never revise this model during blind play.
Player checkpoint: `docs/prototypes/PUZZLE_LAB_V0_05_STATE.md`.
Next: human play and unprompted reasoning report; no hints about the chain.
