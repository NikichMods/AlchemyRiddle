# AlchemyRiddle

**AlchemyRiddle** is a production mod project for **Graveyard Keeper 1.407**.

Product goal: make vanilla alchemy a self-contained deductive puzzle that can be solved without a wiki, brute-force enumeration, or advance disclosure of recipe formulas.

The project is currently in **design/research phase**. No production mechanism has been selected yet.

## Core principle

> Do not make alchemy easier by revealing answers. Make it explainable and solvable.

The intended player experience is: **"I worked out this recipe."**

## Current phase

Before production code, the project will:

- reconstruct the exact vanilla alchemy model for Graveyard Keeper 1.407;
- quantify the real search space and information supplied by failed experiments;
- test whether a common deduction framework can solve all or almost all vanilla recipes;
- simulate answer-blind players against the real recipe corpus;
- audit overlap with current alchemy mods;
- compare materially different puzzle architectures before selecting the smallest mechanism that satisfies the acceptance envelope.

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
