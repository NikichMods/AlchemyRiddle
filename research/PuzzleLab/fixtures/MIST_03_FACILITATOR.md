# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

Precommitted model: `mist-03.json`, lab-v0-03, 2026-10-07.
Synthetic target Сумеречный покров. Two slots, three candidates per slot,
nine possible pairs. Answer p3 + f3. All properties are exhaustive, names add no
rules; no real game recipe is represented. No difficulty labels.

Three visible constraints, simultaneously true:
- sharedTag: intersection of the selected cards' tag sets is nonempty;
- exactly one Dark card;
- notTogether: NOT(Powder Plant AND Fluid Dark). This forbids only that
  conjunction; it does not require either property or forbid either separately.
  This is a target-specific logical clue, not a learned chemistry relation or
  a new two-slot STABLE/INCOMPATIBLE experiment layer.

Intended reasoning: shared-property + Dark-count leave p1+f1 and p3+f3.
The target-specific forbidden combination rejects p1+f1. All three clues are
necessary; each alone is partial. Their forms/roles are distinct: intersecting
property sets, counting one property, excluding a conjunction. Shared-property
is a deliberately bounded new fixture predicate, clearly defined at entry.
Interest remains a hypothesis until player feedback, not guaranteed by syntax.

Economy/actions: same as case 02 — Science 1, submit costs 1, no replenishment,
free selection/marks/notes/export; incomplete/invalid submissions cost nothing;
binary success/failure with no partial-match information. Success ends solved;
failure ends exhausted. No game inventory, acquisition burden or physical costs.
No hidden experiments, later clues, solver projection, automatic exclusions or
unsubmitted answer reveal. Marks are personal annotations, not rules.

Initial player state: title/description including shared-tag definition, both
groups/six cards, all three clues, generic count reference, Science 1, empty
selection/marks/notes/history; submit disabled until complete selection.
No planned facilitator inference before player reasoning. Do not change the
answer, card pool or clue semantics during play. Current durable player state
and exact next point: `docs/prototypes/PUZZLE_LAB_V0_03_STATE.md`.
