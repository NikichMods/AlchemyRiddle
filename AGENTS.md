# Project Working Contract

This repository follows the canonical global development rules in `NikichMods/DevRules`.

Before substantive technical work, read:
- `ENGINEERING_RULES.md`
- `CI_POLICY.md`
- `GIT_WORKFLOW.md`
- `PROJECT_BOOTSTRAP.md`
- `RUNTIME_TEST_HARNESS.md` when installed-runtime evidence is relevant
- `LICENSE_POLICY.md` and `CHATGPT_PROJECT_SETUP.md` when their subject is relevant

This file contains only project-specific additions, constraints, verified facts, and explicit exceptions.

## Project identity

- Project name: **AlchemyRiddle**
- Repository: `NikichMods/AlchemyRiddle`
- Target/runtime: **Graveyard Keeper 1.407**, Windows PC; intended NikichMods BepInEx 5 mod ecosystem
- Purpose: make vanilla alchemy independently solvable as a deductive puzzle, without revealing unknown formulas, requiring a wiki, or relying on brute-force enumeration.

## Scope and current phase

The project is in **design/research phase**. Do not treat any proposed UX or mechanics as accepted production architecture until the solution-space comparison is complete and the user selects a direction.

Canonical product requirements and acceptance envelope: `docs/PRODUCT_REQUIREMENTS.md`.

Canonical design/research status and open questions: `docs/DESIGN_RESEARCH.md`.

Production code must not begin merely because a plausible hook or UI design is found. First establish the vanilla information model, search-space behavior, targetability problem, and solution-family trade study.

## Mandatory project-specific start-of-work checks

Before substantive work:
1. inspect current repository state, branches/history and this `AGENTS.md`;
2. read `docs/PRODUCT_REQUIREMENTS.md` and task-relevant local evidence;
3. read `NikichMods/GraveyardKeeperResearch/AGENTS.md` and `docs/RESEARCH_INDEX.md`;
4. inspect relevant accepted shared research before fresh host-internals work;
5. verify unfamiliar Graveyard Keeper internals directly before relying on them;
6. keep research/probes clearly separate from production behavior.

Repository evidence and accepted runtime evidence outrank chat memory.

## Shared Graveyard Keeper research

Cross-project Graveyard Keeper 1.407 research is centralized in `NikichMods/GraveyardKeeperResearch`.

Reusable vanilla facts discovered here must be promoted to the appropriate shared canonical research document and indexed in `docs/RESEARCH_INDEX.md`. Product-specific puzzle semantics, UX choices, candidate identity, release state, and acceptance remain canonical in this repository.

At bootstrap, the shared research index contains farming/fertilizer, crafting, UI and other reusable facts, but no canonical alchemy-system research entry. Treat exact alchemy mechanics as open until established from current evidence.

## Evidence and anti-spoiler contract

The real 1.407 recipe corpus may be inspected internally and used as a hidden test corpus when required.

User-facing discussion must not disclose:
- exact ingredients of recipes the user has not explicitly asked to reveal;
- concrete formula paths that effectively reveal an unknown vanilla recipe;
- answer tables disguised as design analysis.

Report research in abstract/aggregate form where possible: counts, equivalence classes, ambiguity, candidate-set sizes, information gain, number of meaningful experiments, exceptional cases, ownership seams, and lifecycle behavior.

Do not persist copied game assemblies, bulk decompiled source, extracted proprietary assets, or full game-data/recipe dumps. Preserve distilled derived facts, identifiers, bounded evidence, original research tooling, and aggregate test results.

## Product invariants

Unless separately accepted:
- vanilla alchemy recipes remain unchanged;
- vanilla progression, economy and save state remain unchanged;
- success must remain the player's deduction, not delayed answer disclosure;
- every informational step should support genuine reasoning;
- the system needs a route from a required unknown product to a relevant investigation, not merely better interpretation of random failed mixtures;
- brute-force enumeration and wiki lookup must not be required for the intended puzzle path.

## Git / version / acceptance workflow

- `main` is the stable/documentation baseline.
- Research-only work uses `research/<topic>` when separation improves reviewability.
- Build-bearing production work uses `dev/<version>` or a semantic feature branch.
- Research-only work does not consume numbered production versions.
- Runtime behavior reaches `main` only after the exact candidate is tested and explicitly accepted where runtime acceptance is required.
- Numbered handed artifacts are immutable.
- Stable public distribution uses GitHub Releases unless deliberately changed.
- Handoff filenames use ASCII hyphens and no spaces; installed DLL should remain version-independent once its canonical name is established.

## Licensing

Original project software source uses MPL-2.0 under `NikichMods/DevRules/LICENSE_POLICY.md`. See `LICENSE` and `LICENSING.md`.

## CI / build specifics

This is a public repository. Standard GitHub-hosted runner minutes are not scarce. Use CI when compilation, tests, reproducible research tooling, or artifacts advance the work.

Do not scaffold production build machinery by assumption during the design phase. Establish the actual source/runtime seams first, then derive the smallest compatible build/test setup from verified NikichMods Graveyard Keeper practice.

## Long-lived sources of truth

- `AGENTS.md`
- `docs/PRODUCT_REQUIREMENTS.md`
- `docs/DESIGN_RESEARCH.md`
- `docs/CHATGPT_PROJECT_INSTRUCTIONS.md`
- `docs/TEST_BUILD_LOG.md` once numbered handoff builds exist
- `README.md`
- `CHANGELOG.md` once user-facing versions exist

Mutable hypotheses and candidate state belong in repository evidence/docs/history, not ChatGPT Project Instructions.
