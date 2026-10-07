# Puzzle Lab V0 — case 06 player checkpoint

Status: precommitted initial state; first three-slot Lab play pending.
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
No difficulty labels/progression UI. No player-earned deductions yet.
Next: play, report reasoning/interest and memory friction; preserve actual state
at material checkpoints. No new model decisions are awaiting permission.
