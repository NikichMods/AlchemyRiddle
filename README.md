# AlchemyRiddle

**AlchemyRiddle** is a production mod project for **Graveyard Keeper 1.407**.

Product goal: make vanilla alchemy a self-contained deductive puzzle that can be solved without a wiki, brute-force enumeration, or advance disclosure of recipe formulas.

The project is currently in **design/research phase**. The core two-slot and three-slot puzzle architectures are selected and extensively screened/prototyped; production implementation remains blocked pending final product/generator closure and runtime ownership research.

## Core principle

> Do not make alchemy easier by revealing answers. Make it explainable and solvable.

The intended player experience is: **"I worked out this recipe."**

## Current phase

Before production code, the project is now closing the remaining product/generator contract and then must verify the concrete Graveyard Keeper ownership/lifecycle seams needed for implementation.

Current selected cores:
- two-slot: fixed reagent properties + logical constraints;
- three-slot: adaptive knowledge-aware properties + adjacent STABLE/INCOMPATIBLE relations + logical constraints.

The current design also includes target-first journal entry, persistent investigations, early mature difficulty, anti-bruteforce formula submission, theoretical formula knowledge separated from practical reagent acquisition, and a Dark + Organ property model.

See:

- `AGENTS.md`
- `docs/PRODUCT_REQUIREMENTS.md`
- `docs/DESIGN_RESEARCH.md`
- `docs/CHATGPT_PROJECT_INSTRUCTIONS.md`

Cross-project Graveyard Keeper research is maintained in `NikichMods/GraveyardKeeperResearch`.

## Spoiler policy

Technical research may inspect real vanilla recipes internally when necessary, but project discussion and durable design evidence should prefer aggregate/abstract results. Do not expose exact unknown recipe formulas to the player or in user-facing project discussion unless explicitly requested.

## License

Original project software source is licensed under MPL-2.0. See `LICENSE` and `LICENSING.md`.
