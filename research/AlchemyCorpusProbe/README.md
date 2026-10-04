# Alchemy Corpus Probe 0.3.0

Research-only, read-only probe for **AlchemyRiddle** on **Graveyard Keeper 1.407**.

## Exact research question

Can the 35 ingredients used by ordinary mixed-alchemy success formulas be described by a small set of player-legible, world-grounded properties strongly enough to narrow future target investigations without revealing formulas?

This pass captures **item presentation and provenance**, not recipe answers.

## Why a loaded-balance probe is required

Static 1.407 inspection already establishes the owners of:
- item name / description / icon key;
- alchemy form and goo-family normalization;
- Study / decomposition relationships;
- craft producers and crafting stations;
- direct object drops;
- static vendor eligibility;
- target downstream-consumer / Technology entry channels.

The public decompile contains schema/control flow, not the authored loaded 1.407 population or localized strings. Existing accepted probes intentionally anonymized the ingredient identities. One bounded loaded-`GameBalance` capture is therefore the lowest-assumption path for the remaining property-vocabulary question.

## Captured ingredient data

For only the 35 ingredients that participate in ordinary picker-compatible success formulas, the probe records:

- localized display name and base description;
- icon key;
- Powder / Fluid / Essence / Universal type;
- native goo family and localized goo name when available;
- standard-tooltip crafting stations;
- vendor/product-tier/base-price/base-count support fields;
- non-Mixed producer crafts, their stations and immediate inputs;
- AlchemyDecompose source item presentation and one-hop acquisition summary;
- direct world-object drop definitions;
- static vendor-stock candidates.

These are research inputs. Internal trade tags, object IDs, price fields, station relations and icon keys are **not automatically treated as player-facing semantic properties**.

## Captured target data

For the 34 ordinary mixed-alchemy outputs, the probe records:

- localized name, base description and icon key;
- number of valid formulas only;
- downstream ordinary/build consumer counts;
- visible Technology-owned consumer counts;
- static vendor-sample candidate count;
- narrow visible QuestDefinition-expression reference count;
- product tier/base-price support fields.

**No target formula ingredients are logged in 0.3.0.**

## Safety / mutation boundary

The probe:
- uses no Harmony patches;
- executes no craft;
- mutates no balance, inventory, save, unlock, vendor or UI state;
- runs once after normal gameplay starts, then becomes inert;
- does not extract image assets;
- does not emit `AR_RECIPE` formula rows;
- uses localized names/descriptions only as transient research input.

Do not commit the returned runtime log or bulk localized game text to the public repository. Persist only distilled facts and aggregate analysis.

## Runtime handoff

1. Replace the old probe DLL with `AlchemyCorpusProbe-0.3.0.dll` in the same BepInEx plugin folder.
2. Launch Graveyard Keeper 1.407 and load any save until normal gameplay is visible.
3. No alchemy interaction, inventory setup, crafting, saving, Technology purchase, trading or quest action is required.
4. Exit normally and return the **full** `BepInEx/LogOutput.log`.

Property records are bounded by `AR_PROPERTY_BEGIN` and `AR_PROPERTY_DONE`.
