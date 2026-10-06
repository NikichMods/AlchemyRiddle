# Two-slot matched difficulty examples — 2026-10-06

Status: **working design artifact for visual comparison; not yet an accepted final per-band grammar; production remains BLOCKED**.

Purpose:
hold candidate field and hidden answer constant while varying only clue structure,
so RICH / HARD / MAX / BOSS can be compared without confounding field size or
property density.

This is synthetic test material. It does not disclose any vanilla recipe.

## Shared synthetic field

Hidden target for all four examples:
- Powder B + Fluid B.

Cards:

| Card | Properties |
| --- | --- |
| Powder A | Corpse, Plant |
| Powder B | Dark |
| Powder C | Corpse, Dark, Organ, Plant |
| Fluid A | Corpse, Mineral, Water |
| Fluid B | Corpse, Plant |
| Fluid C | Corpse, Dark, Organ, Water |

There are nine visible formula candidates in all four examples.

Note:
property richness is intentionally frozen here. In production, later bands should
also increasingly prefer richer visible candidate cards where an equally good
surface exists.

## RICH

Clues:
1. Plant occurs exactly once across the pair.
2. Exactly one is true: Powder has Plant / Fluid has Corpse.

Individual clue survivor counts:
- clue 1: 5 / 9;
- clue 2: 3 / 9.

Together:
- 1 / 9, Powder B + Fluid B.

Intended feel:
two familiar nontrivial statements intersect cleanly. The route is short and
satisfying, but one clue still performs substantial narrowing.

## HARD

Clues:
1. Plant occurs exactly once across the pair.
2. Fluid does not have Mineral.
3. Fluid does not have Dark.

Individual survivor counts:
- 5 / 9;
- 6 / 9;
- 6 / 9.

Sequential intersection in the listed order:
- 9 -> 5 -> 3 -> 1.

All three clues are necessary.

Intended feel:
no single statement is decisive. The player must carry a small live candidate
set through several partial eliminations.

## MAX

Clues:
1. Plant occurs exactly once across the pair.
2. Powder has Dark.
3. If Powder has Dark, then Fluid has Plant.

Individual survivor counts:
- 5 / 9;
- 6 / 9;
- 5 / 9.

Sequential intersection:
- 9 -> 5 -> 3 -> 1.

All three clues are necessary.

Intended feel:
the full mature language is normal. A familiar conditional becomes decisive only
after another clue has constrained which Dark powder is relevant.

## BOSS

Clues:
1. Plant occurs exactly once across the pair.
2. Fluid does not have Mineral.
3. If Powder has Dark, then Fluid has Plant.
4. Exactly one is true: Powder has Dark / Fluid has Mineral.

Individual survivor counts:
- 5 / 9;
- 6 / 9;
- 5 / 9;
- 5 / 9.

Sequential intersection:
- 9 -> 5 -> 3 -> 2 -> 1.

Crucially, every three-clue subset still leaves at least two candidates. All four
facts are mutually necessary for uniqueness.

Intended feel:
a compact proof rather than a longer checklist. Familiar count, exclusion,
conditional and XOR grammar are interlocked. The last step is meaningful because
the previous three facts have reduced the field to a pair of plausible
near-misses.

## Current interpretation

The matched comparison supports the proposed semantic distinction:

- RICH: familiar rules combine, but at least one clue may still make a large
  reduction;
- HARD: several weaker partial facts must all be carried together;
- MAX: full mature grammar is available and conditional/composite reasoning is
  ordinary;
- BOSS: familiar clue families become mutually dependent enough that no proper
  large subset of the clue package already solves the puzzle.

This example deliberately does not test:
- increasing property-card richness;
- alternate field shapes;
- higher-order exact-one/exact-count forms;
- compound/nested conditionals;
- submission economics;
- player-facing wording quality.

Those are separate axes and should not be added to this matched comparison unless
needed to distinguish the bands further.
