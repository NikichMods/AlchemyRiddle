# Paper Prototype Protocol

This file is the execution contract for blind/player-facing AlchemyRiddle paper prototypes. Its purpose is to make prototype results reproducible across ChatGPT chat boundaries and to prevent facilitator improvisation from contaminating player-experience evidence.

## Before a blind prototype starts

Precommit the complete facilitator model before the player's first choice:

- hidden formula or valid-answer set;
- complete candidate pool and recipe arity;
- all rules the player is entitled to know;
- all hidden inference semantics that make observations relevant to the formula;
- experiment menu and legal parameter choices;
- deterministic or explicitly probabilistic outcome model for every offered experiment;
- resource costs, current quantities, replenishment rules and relevant acquisition burden;
- stopping/resolution conditions, including when logical exhaustion may resolve the formula without another physical craft;
- intended UI state shown to the player.

Do not choose or revise the hidden answer after observing player choices. Do not add a new rule after a choice merely to make an earlier observation useful. If the precommitted model is incomplete in a way that affects the player's reasoning, stop the blind test, record the defect, repair the prototype, and restart as a new prototype.

For cross-chat robustness, persist the facilitator state in repository evidence before play. A facilitator-state file may contain fictional prototype spoilers and must be clearly marked **FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**. The player-facing response must not link to or quote hidden-state contents until the prototype is over.

## Player-facing state panel

Every decision point must be self-contained. Do not rely on conversation scrollback.

Show, at minimum:

- current research target and recipe arity/station;
- candidate reagents, grouped by slot/category;
- current resources, experiment costs, and replenishment facts that can affect choice;
- known rules/research model required to interpret observations;
- research journal/history of completed actions and their results;
- established facts, supported hypotheses, and unresolved state, kept distinct;
- currently legal actions and their costs/required selections.

After every action, update and re-display this state before requesting the next choice.

The journal is external player memory, not a solver. It should preserve observations and justified conclusions without silently performing deductions that the player has not earned.

## Experiment-quality checks

Before exposing an action menu, check that offered investigative actions are not accidentally meaningless or strictly dominated under current player knowledge.

A known-outcome demonstration that cannot change the player's belief state must not masquerade as a research choice unless it has another explicit purpose.

A short residual synthesis search can be acceptable after meaningful target-specific narrowing. Evaluate separately:

1. whether the logic works;
2. whether the player had meaningful choices;
3. whether the sequence creates the intended "I worked that out" competence feeling;
4. whether working-memory burden remains low.

Logical solvability alone is not sufficient.

## During play

Treat the player only as the player. Do not explain which architecture/family is being tested until the interaction has reached a natural evaluation point.

Do not defend a prototype against player confusion. Confusion, forgotten state, dominated actions, arbitrary-feeling rules, and inability to justify the next move are evidence to record.

If the player asks what the interface shows, answer from the precommitted state and show the full current panel.

## Cross-chat checkpoint

An active prototype must be recoverable from repository state alone. Before a planned chat migration, and at any natural boundary where a chat cutoff would materially hurt continuity, persist:

- prototype identifier and family under test;
- facilitator-state file/path;
- exact current player-facing state;
- completed actions and observations;
- remaining resources;
- live hypotheses/unresolved state;
- latest player-experience findings;
- exact next interaction point.

Operational test semantics count as decision-bearing project state. Do not assume that a future chat will reconstruct them from general design prose.

On recovery in a new chat, read this protocol and the active prototype state before presenting or resolving another player choice.

## After a prototype

Record:

- whether it was logically valid;
- whether its blind-test integrity held;
- where the player found it interesting, obvious, confusing, arbitrary, or tedious;
- approximate meaningful experiment count;
- whether remaining formula search was deduction, bounded verification, or brute-force cleanup;
- retain / revise / reject / fallback-only judgment and why.

Do not generalize a family-wide conclusion from a prototype whose facilitator model was underspecified or changed during play.
