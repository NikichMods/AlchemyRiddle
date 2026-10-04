# Runtime Alchemy Corpus — 2026-10-04

Status: **accepted runtime research evidence; no production architecture selected**

## Evidence identity

Runtime capture:
- Graveyard Keeper **1.407**, Steam, BuildGUID `f96cf41d85547064385631ec4c2e6977`;
- BepInEx **5.4.23.5**;
- `AlchemyRiddle Corpus Probe 0.1.0`;
- probe source: `research/vanilla-alchemy-model@88287548f0095c0d8ddecd2d490c410401d43a93`;
- CI build run: `37156365576`, conclusion **success**;
- probe is read-only and logs anonymized symbols rather than vanilla item/result IDs.

The raw user runtime log is evidence input and is not committed. This document preserves only aggregate/structural derived facts.

## Captured mixed-alchemy corpus

The loaded 1.407 balance contains, under the alchemy mixed-craft family:

- **509** mixed definitions total;
- **44** definitions classified by the probe as success formulas;
- **465** auxiliary/failure definitions;
- three station IDs in the family, of which one contains only a zero-arity auxiliary placeholder.

By the two ordinary alchemy station families:

| Station class | Success formulas | Success arity | Distinct success outputs | Outputs with multiple formulas | Maximum formulas for one output |
| --- | ---: | ---: | ---: | ---: | ---: |
| Two-slot | 24 | 2 | 18 | 4 | 3 |
| Three-slot | 20 | 3 | 17 | 3 | 2 |

Across all 44 success-classified records there are **35 distinct outputs**. Seven outputs have alternative formulas: five have two formulas and two have three.

### Standard-picker compatibility exception

Cross-checking every success-classified formula against the verified `AlchemyItemPickerFilter` contract found:

- **43 / 44** formulas conform to the normal positional picker rules;
- **1** three-slot definition violates the normal slot-category contract in all three positions.

That one definition must not be silently treated as an ordinary player-solvable formula. Its authored/runtime role remains open.

For the currently ordinary picker-compatible corpus, the structural working set is therefore:

- **43 formulas**;
- **34 distinct outputs**;
- formula multiplicity: **27** outputs with one formula, **5** with two formulas, **2** with three formulas.

This is a scope model, not a claim that the exceptional definition is unused by every possible scripted/game path.

## Ingredient/filter envelope

The loaded item definitions contain:

- 16 Powder;
- 9 Fluid;
- 8 Essence;
- 19 Universal.

Under the verified picker rule, Universal is allowed in any slot and the same item cannot be selected twice.

If every eligible item definition were simultaneously available to the player, the positional filter would therefore permit at most:

- **961** distinct two-slot ordered selections;
- **24,788** distinct three-slot ordered selections.

These are **combinatorial filter envelopes**, not progression-specific player search spaces: actual inventory, Study state, unlock timing and acquisition reduce what a player can attempt at a given moment.

The 43 ordinary picker-compatible formulas use **35 unique ingredient definitions**:

- 15 Powder;
- 8 Fluid;
- 8 Essence;
- 4 Universal.

## Goo-class structure

For the 35 ingredients that participate in ordinary picker-compatible success formulas, the native `GetGooFromAlchemyIngridient` mapping collapses them to **19 distinct goo identities**.

Those 19 classes have a strong native structure:

- **8** classes each contain exactly one Powder, one Fluid and one Essence participant;
- **11** classes are singleton participants: 7 Powder and 4 Universal.

Within each normal positional slot, goo identity is one-to-one among the ingredients that actually participate in the ordinary success corpus. This means the vanilla goo taxonomy is potentially a high-information semantic substrate rather than mere flavor.

The authored auxiliary table is also highly regular:

- the two-slot station has one base placeholder plus **21** one-goo-key auxiliary definitions;
- the three-slot station has one base placeholder, **21** one-goo-key definitions, and **420** ordered two-goo-key definitions (`21 x 20`).

Do not infer the visible output count of those auxiliary crafts from the key shape alone; the current probe recorded only the primary non-tech output identity.

## Design consequences

### 1. The target is a set of valid formulas, not always one hidden answer

Because seven ordinary outputs have alternative formulas, a target-directed puzzle should normally ask the player to discover **a valid formula for product X**, not reconstruct one privileged canonical tuple.

### 2. The corpus is small enough for a deliberately designed puzzle

Forty-three ordinary formulas / thirty-four ordinary outputs is a bounded design problem. We do not need a generic solver for an unbounded crafting language.

### 3. Blind enumeration is structurally unattractive

Even the raw picker envelope is hundreds of two-slot selections and tens of thousands of three-slot selections, while only a tiny fraction are success formulas. This reinforces the product requirement that brute force is not the intended path.

### 4. Vanilla already contains a semantic layer worth exploiting

The goo mapping groups many Powder/Fluid/Essence forms into shared semantic classes. A future property/signature design may be able to reuse that native structure rather than invent an unrelated second taxonomy.

That is a design opportunity, not an architecture decision.

### 5. One exceptional definition must remain outside the common model for now

A normal rule system should not be distorted around the single success-classified definition that the normal alchemy picker cannot construct. Establish its role separately if the final supported scope would otherwise include it.


## Pre-formula exposure audit — Probe 0.2.0

Status: **accepted runtime research evidence; coverage is partial rather than a full progression proof**.

Evidence identity:
- Graveyard Keeper **1.407**, Steam, BuildGUID `f96cf41d85547064385631ec4c2e6977`;
- BepInEx **5.4.23.5**;
- `AlchemyRiddle Corpus Probe 0.2.0`;
- probe source: `research/vanilla-alchemy-model@ed295d6ba1dd2b29f20ff265623d594c3c7b773f`;
- CI build run: `37164012120`, conclusion **success**;
- DLL SHA-256 `29a6cf946459761c1e3b8d61a7b82338ec1f4b943826b6eb5dadccd5f0ad15e6`.

The probe evaluated the **34 ordinary picker-compatible mixed-alchemy outputs** and asked whether loaded vanilla data already contains an authored pre-formula exposure candidate without publishing target identities.

Measured coverage:
- **25 / 34** outputs are used by at least one authored downstream ordinary recipe or build blueprint;
- **9 / 34** have no downstream craft/build consumer in the loaded balance;
- **16 / 34** outputs have at least one visible Technology-owned downstream consumer recipe;
- **5 / 34** have at least one downstream recipe/blueprint visible without a craft unlock;
- the union of those structural channels covers **18 / 34** outputs;
- **17 / 34** have at least one static vendor-stock candidate;
- structural and vendor candidates together cover **26 / 34** outputs;
- **8 / 34** are not covered by the measured channels;
- direct exact quoted item-ID references in visible serialized `QuestDefinition` expressions were **0 / 34**.

Overlap structure:
- 9 outputs have both a structural entry and a vendor-stock candidate;
- 9 have a structural entry but no vendor candidate;
- 8 have a vendor candidate but no structural entry;
- 8 have neither measured entry type.

### Uncovered-output structure

The 8 currently uncovered anonymous targets are not one homogeneous class:

- **7 / 8** are consumed by one or more authored build blueprints, but those blueprints are neither default-visible nor linked to a counted visible Technology craft unlock in this pass;
- **1 / 8** has no ordinary downstream consumer, no blueprint consumer, no static vendor-stock candidate, and no direct visible `QuestDefinition` expression reference.

Looking at downstream demand before visibility classification gives an even cleaner partition:
- **25** outputs have an authored downstream craft/build consumer;
- of the remaining **9**, **8** have a static vendor-stock candidate and **1** has neither measured demand nor vendor sample channel.

Therefore **8 uncovered does not mean 8 proven impossible vanilla entry points**. The seven blueprint-only cases may be unlocked by non-Technology progression such as `UnlockCraft` from FlowCanvas/SmartExpression or another authored path. The one no-consumer/no-vendor case is the strongest current candidate for a genuinely missing natural target entry, but dialogue/FlowCanvas/sample channels remain unproven.

### Interpretation limits

- A static vendor-stock candidate proves only that the loaded vendor/item rules can support a sample channel; it does **not** prove the exact progression moment at which the player can first see or buy that product.
- The zero `QuestDefinition` count is intentionally narrow. It does not inspect arbitrary FlowCanvas/dialogue graph content and must not be reported as “no quest/dialogue mentions”.
- This pass measures **channel existence**, not exact chronological first exposure.
- Blueprint consumer presence by itself does not establish visibility; authored `needs_unlock` blueprints require their real unlock source to be classified.

### Product consequence

The “do not reveal a global catalog; create a research lead when vanilla first gives the player a reason to know the product” direction is structurally plausible for a majority of the ordinary corpus. A universal implementation still needs a fallback or additional vanilla-channel discovery for the unresolved cases.

The immediate research priority is narrower than another whole-corpus scan: classify the unlock/visibility source for the **seven blueprint-only uncovered targets**, then investigate the **single no-consumer/no-vendor target** separately.


## What remains open

Before production architecture is selected:

- design several complete player-facing puzzle loops from a clean slate;
- decide how a player selects or acquires a target product to investigate;
- determine what initial clue exists before the first experiment;
- define what an experiment can reveal without becoming staged formula disclosure;
- decide whether native goo is a taught clue, a core mechanic, or merely one evidence source;
- determine whether a journal/state surface is needed;
- test candidate designs answer-blind against the hidden corpus;
- measure median/worst-case meaningful experiments and unresolved ambiguity;
- establish the role of the one picker-incompatible success-classified definition;
- inspect auxiliary output multiplicity only if the chosen design needs exact vanilla failure presentation.

The runtime corpus is a **test oracle and design constraint**, not a reason to force one of the previously discussed architecture families.


## Property / provenance corpus — Probe 0.3.0

Status: **accepted runtime research evidence; no production architecture selected**

### Evidence identity

Runtime capture:
- Graveyard Keeper **1.407**;
- `AlchemyRiddle Corpus Probe 0.3.0`;
- probe source: `research/vanilla-alchemy-model@163f07939701cff70b3a90565e125c0107d245a9`;
- CI build run: `37207458475`, conclusion **success**;
- handoff DLL SHA-256: `981ffda9dce0b223cfcb993d376762d81e4d1e7063b321f3c2e5c500be121af8`;
- returned runtime block completed from `AR_PROPERTY_BEGIN` through `AR_PROPERTY_DONE` with no `AR_PROPERTY_ERROR`;
- the probe reported **43 ordinary formulas, 35 participating ingredients and 34 ordinary targets**, and intentionally emitted **zero formula rows**.

The raw returned log remains evidence input and is not committed.

### Player-facing presentation population

For the 35 ordinary success-corpus ingredients:
- **0 / 35** have non-empty base item-description text in the loaded Russian localization returned by `GetItemDescription`;
- names and icon keys are populated;
- the 24 regular semantic alchemy forms constitute eight Powder / Fluid / Essence triplets with player-facing family names corresponding to the native goo semantics;
- the remaining 11 participants are singleton/special material identities rather than members of those eight three-form families.

For the 34 ordinary target outputs:
- **8 / 34** have non-empty base descriptions in this capture, concentrated in consumable elixir/effect text;
- therefore vanilla item-description prose is not a corpus-wide starting-clue source.

### Provenance population

The loaded authored data provides materially richer provenance than item descriptions:

- **29 / 35** participating ingredients have at least one non-goo `AlchemyDecompose` source in addition to any same-family goo source;
- examples of authored source relations include plant/crop materials, insects/animal products, anatomical remains and minerals;
- several of the six remaining special ingredients still have ordinary non-decomposition producer paths (for example autopsy, press or pyre-style production), so “29 decomposition-backed” must not be read as “only 29 have meaningful provenance”;
- provenance remains a graph rather than one authoritative source tag.

This validates provenance as a real research substrate. It does **not** validate any particular broad category label as vanilla semantics; broad categories used by AlchemyRiddle are product-design abstractions over these authored source relations.

### Cross-probe identity join

Probe 0.1.0 assigned its `N....` symbols from the lexicographically sorted raw mixed-craft need IDs. Probe 0.3.0 intentionally used a fresh presentation-oriented symbol namespace.

For analysis only, the 35 ordinary success ingredients were joined across the captures by the verified native ID/family structure and the 0.3 presentation records. The reconstructed join was checked against:
- `AlchemyType`: **0 mismatches**;
- the equivalence partition induced by the old `AR_GOO_MAP` rows versus the 0.3 native goo identities: **0 mismatches**.

The exact de-anonymizing symbol map is intentionally not committed because it would turn the previously anonymized formula corpus into a public recipe mapping. Only aggregate derived results are persisted.

### Exposure-audit identity refinement

Probe 0.3.0 supplies player-facing identities for the previously anonymous target records.

The eight targets left uncovered by the 0.2.0 measured structural/vendor entry channels are:
- seven paint products that have authored blueprint consumers but whose visibility/unlock source was not established by that pass;
- **Spices**, which has no measured ordinary downstream consumer, blueprint consumer or static vendor candidate.

The seven blueprint-only cases are the yellow, green, brown, red, dark-green, dark-violet and violet paints.

This refines target identity only; it does not close their real first-exposure chronology or FlowCanvas/dialogue unlock path.

### Limits

- The property probe intentionally captured only the 35 ingredients that participate in ordinary successful formulas, not all 52 globally eligible Powder / Fluid / Essence / Universal definitions.
- Therefore candidate-space measurements built from the 35-item matrix are **structural design screens**, not progression-specific player search spaces.
- Icon keys are not perceptual evidence of what color/shape a human player sees.
- Broad provenance categories are AlchemyRiddle design hypotheses, not native fields.
