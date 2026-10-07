# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

## Precommitted lab-v0-02 — 2026-10-07

Model owner: `amber-02.json`. Synthetic only. Authoring complete before player
choices; player independently reasoned to the correct pair, but rejected the
repetitive clue package as ordinary-play content. Submission not observed.
Current state/evidence: `docs/prototypes/PUZZLE_LAB_V0_02_STATE.md`.
Same two-slot property-count grammar,
no conditional lesson in this case. No player-facing difficulty label.

Answer: p2 + f1. Complete field: 3 Powder / 3 Fluid, 9 tuples. All card properties
are exhaustive. Names carry no additional semantics. All three exact-one facts
are visible together at entry and apply simultaneously. Each fact counts cards
with its specified property, not the total number of tags on a card. A card may
count toward different facts. No extra hidden constraints or subsequent clues.

Intended reasoning: Plant + Mineral counts preserve p1+f3, p2+f1, p3+f1.
Dark count rejects zero-Dark p1+f3 and double-Dark p3+f1. Equivalently, reasoning
may begin from either other pair of facts; no single prescribed solution order.
Every clue is necessary. This is a proposed intersecting-count structure;
mathematical non-redundancy is not proof of interesting play.

Legal actions, observations and economy: choose one card per slot; freely toggle
personal exclusions and write notes; export journal; submit a complete pair for
1 Science. Initial Science 1, no replenishment. Binary success/failure only;
no partial-match feedback. Invalid requests cost nothing. Success completes;
failure exhausts and blocks further submissions. Notes/marks/export remain
available. No game inventory, acquisition burden or physical resource cost is
modeled. No automatic deduction or answer revelation before successful submission.

Initial UI state: title/description, six cards in two labeled groups, three
colored count clues, always-visible short count explanation, no selection,
marks, notes or history, Science 1, submit disabled until both slots selected.
Count explanation uses generic wording and contains no recipe-specific inference.
Further implication explanation remains in the expandable grammar reference;
it is unused by this fixture. No reset action or difficulty/progression label.

Next interaction: human reads/reasons, optionally marks or records notes, and
submits. Facilitator does not supply a deductive path during play. Record the
human's reasoning before discussing intended inference. If confused, capture
the symptom without defending the puzzle. No changes to model during play.

Continuity owner: server memory; durable initial state and next point are also
recorded in `docs/prototypes/PUZZLE_LAB_V0_02_STATE.md`. At a material action or
chat migration, persist actual player state there; do not infer it from this
precommit or an old technical test. New authoring/restart is a new session.
