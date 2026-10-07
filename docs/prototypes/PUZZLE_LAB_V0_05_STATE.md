# Puzzle Lab V0 — case 05 player checkpoint

Status: completed; explicitly accepted as an interesting, pleasant puzzle.
Model: `research/PuzzleLab/fixtures/dew-05.json`.
Facilitator spoilers: `research/PuzzleLab/fixtures/DEW_05_FACILITATOR.md`.

Target: Печать росы. Choose one Powder and one Fluid. All four clues hold
simultaneously. Tags exhaustive; names add no rules. Shared property means the
same tag on both cards. Visible generic implication explanation: consequent is
required when antecedent holds, without requiring the antecedent itself.

Powders:
- p1 Пыль окаменевшего папоротника — Минеральное, Растительное;
- p2 Пыль сумеречного мха — Растительное, Тёмное;
- p3 Пыль речного камня — Минеральное, Водное, Тёмное.

Fluids:
- f1 Чернила речного спрута — Животное, Водное, Тёмное;
- f2 Сок звероцвета — Животное, Растительное;
- f3 Росный настой — Растительное, Водное.

Clues:
1. Если порошок имеет свойство «Минеральное», то жидкость имеет свойство «Животное».
2. Среди компонентов формулы ровно один имеет свойство «Водное».
3. Если жидкость имеет свойство «Животное», то порошок имеет свойство «Водное».
4. У выбранных порошка и жидкости есть хотя бы одно общее свойство.

Science 1, submission costs 1, no replenishment. Binary verdict only. Choices,
personal exclusion/restore marks, notes and exports free. Initial selection,
marks, notes and history empty; status playing. Submit disabled until both slots
selected. No difficulty labels or progression indicator. Lighter case-04 layout
retained: slot divider, colored rounded tags, red exclusion crosses/restore arrows.

The preceding initial state remains the precommitted baseline, not current state.

## Completed play — 2026-10-07

User report and independent browser observation agree: p2 + f3 selected, one
successful submission, Science 0, status solved. All six marks off, notes empty;
history contains only that successful submission. No model changes during play.
No facilitator deductions/hints supplied before the player narrated the result.

Narrated route (speech, not a recorded selection trace): start with the first
conditional because it forms plausible pairs. p1+f1 passes the first two clues
but fails Fluid Animal -> Powder Water; p1+f2 has no Water. For p3, f1 gives
two Water components; f2 passes the first three clues but lacks overlap. Then
try p2: the first conditional is inactive; both Animal fluids fail the third
clue. f3 gives one Water component and shared Plant; verify and submit once.
Informal reagent-name slips are normalized to the fixture identifiers using
their stated properties; no alternate candidate set is inferred from speech.

The player independently rejects hypothetical pairs and treats false conditional
antecedents correctly as imposing no consequent requirement. This is systematic
branch reasoning followed by one paid verification, not paid blind enumeration.
The author-planned compressed chain was not explicitly articulated: do not claim
case 05 proved longer abstract inference or felt harder than case 04. The actual
path and positive subjective experience are separate from that open hypothesis.

Acceptance: tags felt medium-to-high richness; conditions did not look boring.
Reasoning was called pleasant, fun and interesting; subjective difficulty medium.
Retain as a third positive two-slot exemplar alongside cases 03/04. No calibrated
band, difficulty-label policy or generator-wide acceptance follows from this.
Two similar conditional sentence forms were not rejected here; their interacting
roles remain distinct from case 02's repetitive parallel counts.

UI follow-up, explicitly deferred by the player: red cross suggests closing or
making the card disappear. At the next UI pass, choose a different exclusion
marker that communicates annotation and keeps the card visible; retain restore,
accessible labels and manual-only semantics. No presentation changes this turn.

Next: current browser remains on the completed case. Extend calibration toward
representative three-slot play; V0 currently validates two slots only, so that
extension requires a bounded research-harness change and a precommitted model.
Mature/boss proof depth remains open. Preserve this actual state before switching.
