# Puzzle Lab V0 — case 04 player checkpoint

Status: completed; explicitly accepted by the player as a satisfying richer puzzle.
Model: `research/PuzzleLab/fixtures/ink-04.json`.
Facilitator spoilers: `research/PuzzleLab/fixtures/INK_04_FACILITATOR.md`.

Target: Чернильный щит; one Powder + one Fluid. All clues hold simultaneously;
tags exhaustive; names add no rules. Shared property means the same tag on both
cards. Generic conditional explanation is visible before play: its consequent
is required when its antecedent holds, without requiring that antecedent.

Powders:
- p1 Пыль живого коралла — Минеральное, Животное;
- p2 Пыль ночного тростника — Растительное, Тёмное;
- p3 Пыль сердца сумеречного зверя — Животное, Тёмное, Орган.

Fluids:
- f1 Вода чёрного камня — Минеральное, Водное, Тёмное;
- f2 Берёзовый настой — Растительное, Водное;
- f3 Слизь лесного моллюска — Животное, Слизь.

Clues:
1. Selected Powder and Fluid have at least one shared property.
2. Exactly one selected card is Mineral.
3. Animal Powder requires Water Fluid.
4. Plant Powder and Dark Fluid cannot be together in this formula.

Science 1, submission costs 1, no replenishment; binary verdict only. All marks,
choices, notes and exports free. Initial selection/marks/notes/history empty;
submit disabled until both slots selected. No player-facing difficulty label.
The preceding initial state remains the precommitted baseline, not current state.

## Completed play — 2026-10-07

User narration and subsequent browser observation agree: selected p3 + f1,
one successful paid submission, Science 0, status solved. All six marks are off;
notes empty. Browser history contains only that successful submission. No model
or clue changes occurred during play. A technical mark/restore check after
completion restored the original unmarked state and is not player evidence.

Narrated reasoning: begin with Animal -> Water. Try p1+f1, reject two Mineral
cards; p1+f2 fails overlap. Try p3+f2, also no overlap. Briefly overgeneralize that
Animal powders have no viable branch before checking p3+f1. For p2: f2 fails
Mineral count, f1 fails the forbidden Plant/Dark conjunction, f3 fails overlap.
Return to p3+f1, verify all four clues, then submit once. This is player-led
branch reasoning followed by bounded verification, not blind paid enumeration.
Selection chronology is reported speech, not a recorded action trace; the final
result is independently browser-observed.

Acceptance: the player calls this an excellent puzzle, enjoyed sustained thought
and independently computing the answer. Rich tags/conditions looked inviting
rather than boring. Colors helped spot relevant conditions. Subjective difficulty
was estimated as medium or above; this is not a calibrated band and does not
authorize difficulty labels in the UI.

Friction: the player forgot which Fluid had been tried with p3. Preserve this as
working-memory evidence, not grounds for automatic deductions. Annotation was
attempted but cursor behavior was unclear; cause remains unknown. The player
instead gave verbal UI feedback: excessive nested rectangles and a large
exclusion button. After play, presentation-only changes replace that button with
a red bottom-right cross (restore arrow when excluded), remove full slot frames,
keep the divider and round the colored tags. Browser mark/restore and visual
checks passed; selections, history and solved result retained.

Next: retain case 04 alongside case 03 as a positive exemplar. Current browser
stays on the completed case for reviewing the lighter layout; prepare a distinct
inference case when advancing play. Mature/boss and three-slot quality remain
open; this success does not accept an entire generator family.
