# Prototype 32 — Two-slot tag constraints

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base:
- repo: `NikichMods/AlchemyRiddle`
- base main: `7a8a857eb1ec4c83375bb865c9dee05a27c68b26`
- branch: `research/prototype-32-two-slot-tag-constraints`
- production remains **BLOCKED**

## Research question

Can Candidate A's fixed-reagent-property + logical-constraint grammar produce a
more satisfying two-slot deduction than the rejected B/C interaction loops?

This is the final blind candidate in the accepted A/B/C comparison.

## Fair-comparison controls

- 3 Powder candidates x 2 Liquid candidates;
- six complete candidate pairs;
- fictional reagent names;
- all reagent properties are visible and stable;
- no known-recipe library;
- no aggregate resonance;
- no pair-compatibility oracle;
- no paid probing required;
- exactly three target-specific constraints;
- each constraint is individually partial;
- the three constraints together identify exactly one pair.

The point is player-facing deduction quality, not corpus capacity; corpus capacity
for Candidate A has already been established separately.

## Player-facing target

**Сумеречная настойка**

The target name is fictional and carries no formula hint.

## Candidate reagents and visible fixed properties

### Powders
- P1 **Серый пепел** — {Растение}
- P2 **Костяная пыль** — {Труп}
- P3 **Янтарная пудра** — {Растение, Насекомое}

### Liquids
- L1 **Роса** — {Минерал}
- L2 **Рассол** — {Труп, Насекомое}

These properties are part of the player's stable reagent knowledge. They are not
secret target clues.

## Hidden answer

Unique target formula:
- **P3 Янтарная пудра + L1 Роса**

Do not change this after play begins.

## Target-specific research constraints

All three are visible from the start:

1. **Растение встречается ровно в одном из двух компонентов.**
2. **Ровно одно из двух утверждений верно:**
   - порошок имеет признак «Насекомое»;
   - жидкость имеет признак «Труп».
3. **Если порошок имеет признак «Растение», жидкость имеет признак «Минерал».**

Rule semantics are literal:
- "ровно в одном" / "ровно одно" means XOR / exactly one;
- implication means any candidate with Plant Powder requires Mineral Liquid;
- if the Powder does not have Plant, constraint 3 imposes no additional
  requirement.

No hidden properties, exceptions or unstated rules exist.

## Capacity of each clue

Across all six Powder+Liquid pairs:

Constraint 1 alone leaves:
- P1+L1
- P1+L2
- P3+L1
- P3+L2
(4 / 6)

Constraint 2 alone leaves:
- P1+L2
- P2+L2
- P3+L1
(3 / 6)

Constraint 3 alone leaves:
- P1+L1
- P2+L1
- P2+L2
- P3+L1
(4 / 6)

All three together leave only:
- **P3+L1**

Useful interaction:
- constraints 1+2 leave exactly two candidates: P1+L2 and P3+L1;
- constraint 3 distinguishes them.

Thus no single clue identifies the answer, and the final result requires
cross-constraint interaction.

## Player actions

The player may:
1. reason over the visible property lists and constraints;
2. manually state/eliminate candidate pairs;
3. attempt synthesis of any Powder+Liquid pair at any time.

No research probe is available or required in this prototype.

Synthesis:
- hidden target -> success;
- any other pair -> ordinary failure with no new clue.

If the player derives the unique answer, no ceremonial synthesis is required.

## Player-facing state requirements

Show:
- target;
- two explicit columns/lists: Powder | Liquid;
- visible properties attached to each reagent;
- all three target constraints;
- player-stated eliminations/conclusions if any;
- synthesis as optional action.

Do not automatically enumerate all six pairs unless the player asks for a matrix.
Do not perform a fresh deduction before the player states it.

## Evaluation focus

Record:
- whether the initial state is easier or harder to parse than B/C;
- whether the clue language feels like understandable alchemical evidence or an
  abstract logic worksheet;
- whether multiple individually weak facts produce a genuine "aha" when
  intersected;
- whether the player reasons by properties rather than mechanically enumerating
  all six pairs;
- working-memory burden;
- strength of "I worked out this recipe";
- interest rating / 5;
- whether the player wants another puzzle of this type;
- direct preference among A, B and C.

## Stop / repair rule

End when:
- the player identifies the unique target;
- the player synthesizes it;
- or the mechanic is sufficiently evaluated.

Per the accepted comparison plan:
- at most one narrow repair if an obvious presentation defect invalidates the
  comparison;
- otherwise close A and run the A/B/C decision checkpoint;
- no additional Candidate A optimization before that checkpoint.

## Starting checkpoint

- active prototype: **32**
- no actions yet
- all three constraints visible
- awaiting player's deduction
