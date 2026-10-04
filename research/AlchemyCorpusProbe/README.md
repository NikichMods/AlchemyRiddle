# Alchemy Corpus Probe 0.2.0

Research-only, read-only probe for **AlchemyRiddle** on **Graveyard Keeper 1.407**.

## Research question

For each ordinary picker-compatible mixed-alchemy output, does vanilla already provide a natural pre-formula exposure channel that could create an AlchemyRiddle research lead without showing the player a global catalog of unknown products?

This pass first measures authored structural channels rather than trying to reconstruct the exact chronological first moment in every progression path.

## Research-method checkpoint

Already accepted evidence establishes:
- mixed-alchemy control flow and picker rules;
- the 43 ordinary picker-compatible formulas / 34 ordinary outputs;
- Technology recipe ownership and craft visibility semantics;
- static vendor sale rules.

The current repository does not contain the proprietary loaded balance payload, and the public decompile contains code/schema rather than the authored 1.407 balance tables. Therefore one loaded-`GameBalance` read-only probe is the lowest-assumption exact path.

## Exposure channels measured

For each anonymous target output the probe counts:

- downstream ordinary recipes that require it;
- downstream build blueprints that require it;
- authored recipes/blueprints that are visible without a craft unlock;
- visible Technology craft unlocks whose consumer recipe requires it;
- whether those Technology nodes are ordinary-visible or progression-hidden/invisible;
- static vendor-stock candidates derived without constructing Vendor instances;
- exact quoted item-ID references in visible serialized `QuestDefinition` expressions.

The quest-expression channel is intentionally **incomplete**: FlowCanvas/dialogue content outside `QuestDefinition` is not claimed to be covered. Vendor results are **candidate sample channels**, not chronology proof.

## Safety / spoiler boundary

The probe:
- uses no Harmony patches;
- executes no craft and mutates no balance, inventory, player, save, unlock, vendor, or UI state;
- enumerates loaded definitions once after normal gameplay starts, then becomes inert;
- never logs display names, raw item IDs, raw output IDs, formulas, technology names, recipe names, vendor names, or quest names;
- replaces target identities with opaque `Txxxx` symbols.

## Runtime handoff

1. Replace the old probe DLL with `AlchemyCorpusProbe-0.2.0.dll` in a BepInEx plugin folder.
2. Launch Graveyard Keeper 1.407 and load any save until normal gameplay is visible.
3. No alchemy interaction, inventory setup, crafting, saving, Technology purchase, trading, or quest action is required.
4. Exit normally and return the full `BepInEx/LogOutput.log`.

Exposure records are bounded by `AR_EXPOSURE_BEGIN` and `AR_EXPOSURE_DONE`.
