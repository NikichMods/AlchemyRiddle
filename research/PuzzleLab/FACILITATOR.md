# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

## Precommitted model: lab-v0-easy-01

Status: authored and mechanically validated; blind player test NOT STARTED.
No real Graveyard Keeper recipe is represented.

`fixture.json` is the complete immutable-within-a-session model. Two slots,
two candidates each, four tuples. Answer: p1 + f1. All clues are visible at
entry; there are no hidden experiments or later clues. Property labels are
exhaustive for this fixture. Card names carry no additional semantics.

Clues: exactly one chosen component is Plant; Plant powder implies Plant fluid.
Intended inference: assuming Plant powder would force two Plant components,
contradicting exactly-one. Therefore powder is not Plant, and fluid is Plant.
Each clue alone leaves multiple candidates; together they uniquely determine
the answer. This is a hypothesis for an easy cross-clue inference, not proof
of intellectual interest or a mature difficulty exemplar.

Actions: choose one card in each slot, freely toggle personal exclusion marks,
write notes, export player journal, submit the selected pair. Selections and
marks reveal no new facts. Submission costs 1 Science; starting budget is 1;
there is no replenishment. No reagent inventory, acquisition burden or time
cost is modeled. Invalid/incomplete requests cost nothing. Valid submission
returns only success/failure; it never names a correct component on failure.
Success completes the experiment. Failure exhausts this session and blocks
further submissions. Notes/marks/export remain available after either ending.
No reset action exists in the player UI; a deliberate server restart/new
cookie is a new technical session and must not count as a fresh blind test.

Initial player state: target title/description, both slot groups, four property
cards, both clues, grammar help, no selections/marks/notes/history, Science 1.
Next human interaction: read the board, reason and optionally mark candidates,
record reasoning and submit. No facilitator deduction should be supplied.

Operational continuity: server memory retains actions until stop or fixture
change. Before chat migration with active play, export the journal and persist
the exact player state and next interaction point under docs/prototypes, per
PAPER_PROTOTYPE_PROTOCOL.md. Browser state alone is not a recovery artifact.
After play record validity, blindness, confusion/interest, meaningful action
count, deduction vs guessing, and retain/revise/reject judgment.
