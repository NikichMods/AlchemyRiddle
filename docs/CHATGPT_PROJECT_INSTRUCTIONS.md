# ChatGPT Project Instructions — AlchemyRiddle

We are working on **AlchemyRiddle**.

Repository: `NikichMods/AlchemyRiddle`  
Target/runtime: Graveyard Keeper 1.407, Windows PC; NikichMods BepInEx 5 mod ecosystem

Purpose: make vanilla alchemy independently solvable as a deductive puzzle without wiki lookup, brute-force enumeration, or advance revelation of unknown recipe formulas. The player should be able to say: “I worked out this recipe.”

## Mandatory startup / recovery

Before substantive technical work:

1. inspect the current target repository, relevant branches/commits/PRs/build/test evidence;
2. read the current global contract in `NikichMods/DevRules`: `ENGINEERING_RULES.md`, `CI_POLICY.md`, `GIT_WORKFLOW.md`, `PROJECT_BOOTSTRAP.md`, and `RUNTIME_TEST_HARNESS.md` when runtime evidence is relevant;
3. read this repository's current `AGENTS.md`;
4. read `docs/PRODUCT_REQUIREMENTS.md`, `docs/DESIGN_RESEARCH.md`, and task-relevant local evidence;
5. before fresh Graveyard Keeper internals research, read `NikichMods/GraveyardKeeperResearch/AGENTS.md`, then `docs/RESEARCH_INDEX.md` and relevant canonical shared docs.

Repository state and accepted evidence outrank chat memory and old handoffs.

## Product / spoiler contract

Keep the outcome separate from any first implementation idea. No research-target, journal, property/signature system, slime tutorial, or hybrid is accepted architecture merely because it was discussed.

Core invariant: **do not make alchemy easier by giving the answer; make it explainable and solvable.**

A valid design must provide a reasoned path from a required unknown product to targeted investigation, not only make random failed mixtures easier to interpret. Experiments should produce information the player can reason from; the system must not become a hidden recipe book that reveals the answer gradually.

Do not reveal exact ingredients/formulas for recipes the user has not explicitly asked to know. Technical research may inspect real recipes internally as a hidden test corpus, but report aggregate/abstract results: counts, candidate-set sizes, ambiguity, information gain, exceptional cases and meaningful experiment counts.

Vanilla formulas, progression, economy and save behavior are preserved by default until evidence and an explicit product decision justify a change.

## Working behavior

Follow DevRules evidence-first workflow, solution-space selection checkpoint, research-method checkpoint, and per-change production evidence gate.

Before substantial implementation or deep mechanism-specific research, compare the useful solution families and prefer the least-complex mechanism that fully satisfies the acceptance envelope. Re-open the choice if a path fails, materially expands host/runtime uncertainty, or exposes a simpler adequate alternative.

Before the first production-source mutation for every materially independent behavior change, make the DevRules gate reviewable:
- observable property;
- canonical owner;
- final writer / consumer / commit point where applicable;
- blast radius;
- preserved invariants;
- acceptance evidence;
- state: **READY** or **BLOCKED**.

There is no exception for small, obvious, presentation-only or follow-up changes. **BLOCKED means research/probe only.**

Gate granularity and candidate/build granularity are separate. Several independently READY changes may share one coherent candidate if combined acceptance remains attributable. Do not bundle BLOCKED or independent unverified mechanisms merely to reduce builds/test cycles.

Before creating new probe/harness code, state the exact unknown and check whether accepted local/shared evidence, direct inspection, an existing exact artifact, or a short real-runtime action answers it more cleanly. Prefer fewer assumptions/moving parts over fewer user clicks.

Do not guess APIs, IDs, lifecycle, formulas, state ownership, final writers or UI semantics when evidence can establish them.

Immediately before any downloadable artifact handoff, re-read applicable DevRules handoff rules and verify the exact intended file, filename/version/identity and real downloadable path.

## Research ownership

Reusable Graveyard Keeper 1.407 host/runtime facts belong in `NikichMods/GraveyardKeeperResearch` and its index. Product-specific puzzle rules, UX decisions, candidate/release state and acceptance belong in AlchemyRiddle.

Do not commit copied game assemblies, bulk decompiled source, extracted proprietary assets or full recipe/game-data dumps. Persist distilled derived facts, identifiers, bounded evidence, aggregate statistics and original tooling.

## User-operation boundary

Use available GitHub/tools/CI/research capabilities directly rather than asking the user to perform mechanical technical work.

Ask the user only for product/design decisions, credentials/consent tools cannot provide, or installed-runtime/perceptual evidence that genuinely requires the real game.

This repository is public; do not conserve standard GitHub-hosted runner minutes artificially.

## Conversation continuity

No special handoff prompt is required inside this ChatGPT Project. Recover current state from GitHub/canonical evidence before substantive work.

Checkpoint decision-bearing state at natural boundaries. Before a planned chat migration, persist material uncheckpointed state first. If an unexpected cutoff leaves a material decision unavailable, recover from canonical evidence and ask rather than guess.

## Iteration report

After a substantial iteration, report briefly:
- what was unknown;
- what is now proved/changed;
- what remains open;
- whether the user needs to perform any runtime test, and exactly which one.

Do not repeat accepted tests without a concrete reason.
