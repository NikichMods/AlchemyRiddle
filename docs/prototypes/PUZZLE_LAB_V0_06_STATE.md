# Puzzle Lab V0 — case 06 player checkpoint

Status: completed; explicitly accepted as a good, enjoyable three-slot puzzle.
Model: `research/PuzzleLab/fixtures/harbor-06.json`.
Facilitator spoilers: `research/PuzzleLab/fixtures/HARBOR_06_FACILITATOR.md`.
Target: Тихая гавань. One Powder + one Fluid + one Essence.

Powders:
- p1 Пыль каменного вереска — Растительное, Минеральное;
- p2 Пыль сумеречного мотылька — Животное, Тёмное;
- p3 Пыль ночного плюща — Растительное, Тёмное.
Fluids:
- f1 Раствор речной соли — Водное, Минеральное;
- f2 Сок вязкой лианы — Растительное, Слизь;
- f3 Вода сумеречного ключа — Водное, Тёмное.
Essences:
- e1 Эссенция сердца цветка — Растительное, Орган;
- e2 Эссенция лесного моллюска — Животное, Слизь;
- e3 Эссенция чёрного кристалла — Минеральное, Тёмное.

Clues:
1. Exactly one of the three components is Dark.
2. Mineral Powder requires Animal Essence.
3. Plant Powder cannot coexist with Slime Fluid in this formula.

All clues simultaneously true, tags exhaustive, names add no rules. Implication
does not require its antecedent. A valid formula also requires both adjacent
pairs stable. Tags do not determine compatibility. Stable pairs alone do not
guarantee the target formula; no Powder+Essence test is offered.

All prior pair observations on this surface:
- p1+f3 STABLE;
- f1+e2 INCOMPATIBLE;
- p3+f1 INCOMPATIBLE;
- p2+f1 STABLE;
- f2+e2 STABLE.
These are reusable pair knowledge, not declarations of relevance to this target.

Science 1; full formula check costs 1. Research Charges 4; each unknown adjacent
pair test costs 1. No replenishment. Selection/marks/notes/export free; repeated
known-pair requests free. Binary pair outcome only; formula verdict success/failure
without partial disclosure. No derived facts or automatically excluded candidates.
On formula success or exhausted Science the experience ends; exhausting pair
charges alone leaves formula checking available. State stays in server memory.

Initial selection/marks/notes/action history empty; status playing. Formula check
disabled until all three selected; pair tests require only their two slots.
Three separated columns, colored tags, slashed-circle exclusion with restore.
No difficulty labels/progression UI. The preceding initial state remains the
precommitted baseline, not current state.

## Completed play — 2026-10-07

User narration and independent browser observation agree: selected p2+f2+e2,
status solved, Science 0, Research Charges 1. No marks, notes empty. Exact action
history: f3+e2 INCOMPATIBLE; f1+e1 INCOMPATIBLE; p2+f2 STABLE; full formula success.
Three new pair investigations, one synthesis, no failed synthesis. Known relations
are the five initial observations plus those three new observations. Model stayed
unchanged; no facilitator hints supplied during play. Speech-derived name slips
are normalized against the fixed cards and stated properties, not new candidates.

Narrated route: start with known p1+f3; count fixes no further Dark component and
Mineral Powder implies Animal Essence, selecting e2. Test missing f3+e2 edge:
incompatible, reject branch. Next known p2+f1: reject Dark e3, test f1+e1 and find
incompatible; consult prior f1+e2 incompatibility, reject this pair branch rather
than all of p2. Finally start from known f2+e2: Plant Powder is forbidden with
Slime Fluid, choose p2 to supply the one Dark component; test p2+f2, stable, then
verify the complete formula. The player briefly conflated satisfying tags with
pair stability, corrected themselves before the paid test. Preserve this as
evidence for separate visible tag constraints and observed pair state.

Acceptance: good puzzle, substantial but simple sequential thinking, very positive
response. Subjective medium / medium-high estimate, not a calibrated band. The
player explicitly anticipates clearer UI improving the experience. Limited natural
recipe demand means ordinary later puzzles should not feel disposable; onboarding
should teach meaningful reasoning, with only the first example possibly very simple.
Do not convert approximate spoken demand counts into new corpus facts.

UI requests: candidates, pair/formula actions, tag clues and pair observations
visible together on a normal desktop viewport. Repeat-click deselect; clearly
show selected adjacent pairs as stable/incompatible/unknown using only observed
knowledge. Differentiate results by polarity, pair type and initial vs personally
tested origin; highlight observations matching current selection. Compact task
at top; consolidate general logic/economy into one expandable reference.

Product question: user prefers only stable authored starting bridges and tag-based
initial exclusions. This conflicts with the existing all-relevant-known-relations
policy if applied to accumulated negative knowledge. Clarified by the user: at start show stable pairs only; after research show all outcomes. This supersedes the old initial presentation policy for future cases. Preserve case 06 as historical evidence rather than rewriting its initial knowledge.

Next: review the implemented workspace on this completed state, then precommit a new stable-start example. Starting-knowledge policy is reconciled; subjective layout acceptance remains with the player. Further mature/boss calibration remains open.

Workspace verification after server restart: the saved three research actions
and successful submission were restored mechanically, then checked against the
original browser record. Same selected p2/f2/e2, eight observations, exactly three
new observations, Science 0, Research Charges 1, empty notes and all marks off.
This restoration is not a second human trial. Desktop check on actual 1151x1065
viewport showed the core ending around y=781, fully visible. Two-slot browser
regression confirmed deselection and hidden pair controls/journal with no error.
