# Design / Research Phase

Status: **OPEN — no production architecture selected**

## Research objective

Establish whether Graveyard Keeper 1.407's vanilla alchemy can support a coherent, targetable deduction puzzle with an added information layer, and identify the smallest mechanism that satisfies `docs/PRODUCT_REQUIREMENTS.md`.

## Evidence baseline at bootstrap

- Canonical shared source: `NikichMods/GraveyardKeeperResearch`.
- Required entry points: `AGENTS.md` and `docs/RESEARCH_INDEX.md`.
- The shared index currently contains reusable crafting, farming/fertilizer, UI, dialogue, perk and other runtime research, but no canonical alchemy-system entry.
- Therefore exact alchemy mechanics, formula-space structure and recipe-discovery ownership remain **open research questions** for this project until directly established.

## Phase A — reconstruct vanilla mechanics

Establish for Graveyard Keeper 1.407:

- alchemical component categories and slot constraints for the relevant workstations;
- the number of valid formulas and outputs in scope;
- alternative formulas and duplicate-output cases;
- exact failed-experiment/slime behavior and what information it encodes;
- the persistent state that represents known ingredients/formulas/results;
- how formulas become known/unlocked;
- UI/runtime seams that display, consume and persist those facts;
- special cases that do not follow the common model.

Do not publish exact unknown formulas in user-facing reports.

## Phase B — quantify the puzzle

Use the real recipe corpus as a hidden test corpus and measure:

- naive combination-space size;
- candidate-set reduction from each vanilla failure signal;
- ambiguity that remains after reasonable experiments;
- whether existing information alone can target a named unknown output;
- how many meaningful experiments are needed under plausible strategies;
- recipes/outputs that are structurally exceptional.

The key distinction is between:
- **forward discovery**: from a mixture toward any successful result;
- **targeted discovery**: from a required unknown output toward its formula.

The mod must solve the second problem, not merely improve the first.

## Phase C — answer-blind simulation

For each representative recipe class, simulate a player that does **not** know the answer:

1. record only information legitimately available at that point;
2. choose an experiment from the current rules/evidence;
3. apply only the information the player could infer from its result;
4. update the candidate set;
5. repeat until the formula is uniquely justified or the method fails.

Record aggregate path length and failure/ambiguity statistics, not formula disclosures.

If a proposed system's solver needs hidden answer knowledge to choose the next experiment, the system fails the product goal.

## Phase D — solution-family trade study

Compare materially different families, at minimum:

1. **Vanilla-signal teaching** — make current failure information legible and teach its rule.
2. **Targeted investigation** — allow a required/selected unknown product to seed product-specific constraints without directly revealing the formula.
3. **Property/signature deduction** — expose consistent alchemical properties that let experiments infer structural constraints.
4. **Deduction journal** — persist established/excluded facts and candidate-state reasoning.
5. **Hybrid minimal system** — combine only the components required to cover the acceptance envelope.

Compare:
- acceptance coverage, especially targetability;
- information gain and median/worst-case meaningful experiment count;
- rule coherence and player teachability;
- amount of new UI/state;
- coupling to vanilla internals;
- persistence/save impact;
- localization burden;
- compatibility/overlap with other alchemy mods;
- failure modes and maintenance burden;
- whether the design is truly deduction or merely staged answer disclosure.

## Competitor / overlap audit

Before scope is frozen, verify current versions and actual behavior of existing alchemy mods, including **Alchemy Research Redux** and other relevant current alternatives.

Classify overlap by capability rather than title:
- unknown-formula disclosure;
- known-recipe presentation;
- failed-experiment assistance;
- ingredient/property information;
- targeted research of an unknown output;
- journal/history;
- progression/balance changes.

Do not rely on remembered descriptions or old versions.

## Decision gate before production code

Production mutation is **BLOCKED** until the design phase establishes:

- a sufficiently complete vanilla information model;
- measured search-space behavior;
- a viable targetability mechanism;
- answer-blind corpus simulation showing the approach works across the intended scope;
- competitor overlap understood;
- a solution-space comparison and user-selected direction.

After direction selection, each materially independent production behavior change still requires its normal DevRules READY/BLOCKED evidence gate.
