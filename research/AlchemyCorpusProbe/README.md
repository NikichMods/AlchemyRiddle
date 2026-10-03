# Alchemy Corpus Probe 0.1.0

Research-only, read-only probe for **AlchemyRiddle** on **Graveyard Keeper 1.407**.

## Research-method checkpoint

Static 1.407 source already establishes the mixed-craft control flow, slot-category filtering, recipe-discovery state, and stochastic goo-selection algorithm. It does not contain the loaded authored balance corpus required to establish exact mixed-recipe counts, alternative-formula multiplicity, ingredient populations, authored failure definitions, or candidate overlap.

Checked first:
- `NikichMods/GraveyardKeeperResearch/AGENTS.md`
- `NikichMods/GraveyardKeeperResearch/docs/RESEARCH_INDEX.md`
- `NikichMods/GraveyardKeeperResearch/docs/ALCHEMY_SYSTEM.md`
- accepted 1.407 source reference `Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9`
- existing StudyRewardInsight runtime probes/datasets

No accepted existing artifact contains the full mixed-alchemy balance corpus.

## Decision

Use one narrow read-only loaded-`GameBalance` probe. It emits aggregate statistics plus an **anonymized structural corpus**.

## Safety / spoiler boundary

The probe:
- uses no Harmony patches;
- executes no craft and mutates no balance, inventory, player, save, unlock, or UI state;
- enumerates loaded definitions once after normal gameplay starts, then becomes inert;
- never logs display names, raw item IDs, raw output IDs, or exact human-readable formulas;
- replaces identities with opaque structural symbols.

## Runtime handoff

1. Put `AlchemyCorpusProbe-0.1.0.dll` in a BepInEx plugin folder.
2. Launch Graveyard Keeper 1.407 and load any save until normal gameplay is visible.
3. No alchemy interaction, inventory setup, crafting, or saving is required.
4. Exit normally and return the full `BepInEx/LogOutput.log`.

Records are bounded by `AR_CORPUS_BEGIN` and `AR_CORPUS_DONE`.
