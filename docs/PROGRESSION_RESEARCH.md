# Vanilla Alchemy Progression Research

Status: **active research; production architecture remains BLOCKED**

Target: Graveyard Keeper 1.407.

This document owns AlchemyRiddle-specific progression analysis: when an alchemical need can become visible, when it becomes actionable, what knowledge is guaranteed versus merely possible, and which real progression states are suitable anchors for onboarding / 2-slot / 3-slot puzzle design.

## Method

Do not model vanilla alchemy as one canonical linear walkthrough. Graveyard Keeper permits branch-order variation.

For each target or teaching opportunity, record a **partial-order / reachability** model with two distinct milestones:

1. **earliest visible need** — a player-facing quest, dialogue, craft/build recipe or other authored consumer can expose a need for the item;
2. **earliest actionable research state** — the player has the station/capability required to investigate or synthesize the relevant alchemy class.

At each milestone distinguish:
- **must already know/have** — entailed by the same prerequisite path;
- **may already know/have** — available through an independent branch or optional exploration;
- **not established** — chronology/visibility is still unproved.

Repository/runtime evidence outranks walkthrough memory and community ordering. Community sources may be used only to locate a candidate path for direct verification.

## Accepted technology backbone

Loaded 1.407 Technology evidence establishes:

- hidden **The Beginning Of Alchemy** has no Technology parent and grants the 2-component alchemy bench, hand mixer and alchemy mill;
- **Embalm 1** depends on The Beginning Of Alchemy and grants the research-table construction plus two embalming-liquid recipes;
- **Alchemy storage** also depends on The Beginning Of Alchemy;
- **Advanced alchemy** depends on Alchemy storage and grants the 3-component alchemy bench plus Distillation Cube II;
- **Embalm 2** requires both Embalm 1 and Advanced alchemy.

Therefore two-component synthesis capability is introduced by The Beginning Of Alchemy, while normal three-component synthesis capability is downstream of Advanced alchemy.

## Visible need can precede actionable alchemy

The Embalm 1 authored craft set consumes ordinary alchemical products including Acid and Alkali, while Advanced alchemy is on the sibling Alchemy-storage branch.

Consequently the Technology graph permits a state where a 3-component-product need is visible from Embalm 1 while the normal 3-component bench is not yet unlocked.

This is now a standing audit rule: **do not equate first visible need with first actionable research state**.

Embalm 2 is cleaner as a guaranteed-actionable three-component anchor because its prerequisites already include Advanced alchemy. Its authored recipes consume further ordinary alchemical products such as Glue / Preservative-class inputs.

Exact “first globally” chronology is not yet claimed; these are partial-order facts.

## Scripted formula disclosure is branch-dependent

Accepted runtime evidence from the Astrologer quest path shows:

- the Acid task becomes visible;
- the player can ask where the required items can be found;
- that branch opens the native alchemy discovery dialog for Acid through a forced scripted unlock.

Therefore Acid must not be treated as universally unknown whenever another system first needs it.

However, the current Technology graph does not make the Astrologer branch a prerequisite of Embalm 1 / Advanced alchemy. The progression model must therefore classify Acid formula knowledge as potentially **branch-dependent** until a mandatory cross-branch prerequisite is proved.

This is precisely why known-formula references must be selected from the actual save state, not assumed from one walkthrough order.

## Merchant / Spices anchor — partially proved

Existing quest-graph evidence establishes that the Merchant curse chain has a visible task and a completion interaction gated by the Spices item.

Thus Spices is a real target-directed quest need.

What remains unproved in accepted internal evidence:
- the exact Clotho branch that teaches or unlocks the Spices formula;
- whether that branch reveals the complete formula directly before the Merchant hand-in becomes actionable;
- which required reagent-acquisition knowledge is guaranteed at that point.

Do not yet treat remembered/community wording as canonical.

## Candidate first two-component anchor — not yet accepted

Heal Potion is a real ordinary 2-component mixed-alchemy formula in loaded balance data.

External/community descriptions suggest Clotho's early Lost Memories interaction can be satisfied through a Heal Potion route and is tied to the first alchemy unlock/tutorial flow. This is a strong candidate for the earliest real 2-slot teaching anchor, but the exact authored FlowCanvas path has not yet been verified internally.

Required evidence:
- exact Clotho root-to-branch prerequisites;
- what item/resource requirement is presented;
- whether the formula is supplied, scripted-unlocked, or left unknown;
- timing relative to The Beginning Of Alchemy.

## Candidate three-component anchor

Do **not** use the Astrologer's Acid request as a generic unknown-formula prototype: a verified authored path explicitly reveals Acid.

For progression design, two distinct 3-slot milestones are useful:
- **early visible but possibly not actionable:** Embalm 1 exposes Acid/Alkali-class needs before Advanced alchemy is structurally required;
- **guaranteed actionable:** Embalm 2 is downstream of Advanced alchemy and exposes additional 3-slot-product needs.

The final “first normal unknown 3-slot formula” anchor remains open until scripted unlock paths are censused.

## Exact residual research questions

The next runtime/static census should answer only the remaining progression questions:

1. In Clotho's initial alchemy-introduction branch, what task/resource requirements are authored and what alchemy knowledge is explicitly revealed or unlocked?
2. In the Merchant-cure / Spices branch, is the Spices formula explicitly revealed/unlocked, and at what authored transition?
3. Across loaded authored FlowCanvas/item-expression sources, which ordinary mixed-alchemy outputs have explicit \`UnlockAlchemy\` / \`UnlockRandomAlchemy\` disclosure channels, and which graph/item owns each channel?
4. Which early 2-slot and 3-slot target needs remain genuinely unknown at their earliest actionable state after those scripted disclosures are accounted for?

Do not emit exact ingredient formulas in the research output. Named outputs, arity, graph ownership, task/phrase anchors and whether a disclosure occurs are sufficient.


## Progression Probe 0.1.0 — runtime candidate

Status: **built; runtime evidence pending**.

Research-method checkpoint:
- exact unknown: authored early Clotho/Merchant alchemy disclosure semantics and the corpus-wide set of explicit scripted alchemy formula unlock channels;
- accepted static/runtime evidence already closes Technology ownership, mixed-craft arity, decomposition ownership, Merchant Spices goal existence and the Astrologer Acid scripted-unlock example;
- direct static repository inspection cannot enumerate the serialized live FlowCanvas graphs available only in the installed game;
- existing DayWheelQuestMarkers 1.1.14 provides accepted parser lineage for serialized node/connection and CustomFunctionCall UID topology;
- therefore the least-assumption residual method is one read-only loaded-graph census, not a new gameplay walkthrough.

Candidate identity:
- source branch: \`research/vanilla-alchemy-model\`;
- exact source / workflow head: \`3b0b112dcdbf749990b3e8b281a45c46e1c4a2de\`;
- CI run: \`37233252401\`, conclusion **success**;
- artifact ID: \`11314855758\`;
- handoff DLL: \`AlchemyProgressionProbe-0.1.0.dll\`;
- DLL SHA-256: \`002351ad4ae31172c96c31c6c4a0573ee8f5bc1a37f346043ae35bc68843c217\`;
- target: Graveyard Keeper 1.407.

Probe contract:
- read-only; no save/balance/inventory/craft-unlock mutation;
- scans loaded GameBalance plus loaded \`FlowCanvas.FlowScriptController\` serialized graphs;
- records named output / arity / owner for explicit \`UnlockAlchemy\` and \`UnlockRandomAlchemy\` channels;
- records bounded node/edge neighborhoods around the early Clotho/Merchant focus terms;
- logs **zero exact mixed-formula IDs and zero ingredient-formula rows**.

Acceptance evidence requested:
- load any existing save into the game world once with the exact DLL installed;
- return the resulting \`LogOutput.log\`;
- expected terminal markers: \`AR_PROGRESSION_BEGIN\`, \`AR_PROGRESSION_SUMMARY\`, \`AR_PROGRESSION_DONE\`;
- any \`AR_PROGRESSION_ERROR\` blocks acceptance.


## Progression Probe 0.1.0 — accepted runtime capture

Runtime evidence: user capture \`LogOutput(5).log\`, Graveyard Keeper 1.407.

Acceptance:
- probe loaded successfully;
- \`AR_PROGRESSION_BEGIN\` and \`AR_PROGRESSION_DONE\` are present;
- no \`AR_PROGRESSION_ERROR\` occurred;
- summary: 114 controllers seen, 104 unique serialized graphs, 5 focus graphs;
- formula privacy contract held: \`formula_rows_logged=0\`.

Observed disclosure census:
- item-level channels: one \`UnlockRandomAlchemy\` item and the dedicated Memory Tincture recipe item;
- serialized FlowCanvas text search found zero literal \`UnlockAlchemy\` / \`UnlockRandomAlchemy\` calls.

**Important limitation:** zero literal FlowCanvas \`UnlockAlchemy\` calls is **not** evidence that authored dialogue never reveals recipes. Earlier accepted runtime evidence showed Acid being presented through \`TechUnlockDialogGUI\`. Static decompile proves \`Flow_UnlockTech\` opens that same \`TechUnlockDialogGUI\` and can therefore be the owning mechanism for authored recipe/technology disclosure without any literal \`UnlockAlchemy\` expression in the serialized graph.

The 0.1.0 focus capture also proves:
- Clotho's loaded graph contains a \`Flow_UnlockTech\` on the \`npc_clotho_task_1\` path;
- the same graph contains explicit early AnswerData/SmartRes nodes whose serialized windows contain \`pot_heal\`, \`alchemy_1_yellow\`, and \`The Beginning Of Alchemy\`;
- the Merchant graph makes \`merchant_curse\` visible and unlocks the Clotho-directed phrase \`@сlotho_merch\`.

Do **not** yet infer exact early requirements or recipe disclosure from these windows: 0.1.0 did not log the actual SmartRes fields or the \`Flow_UnlockTech.tech id\`.

Residual question is now narrowed to:
1. exact SmartRes values attached to Clotho's first alchemy-related answers;
2. exact \`tech id\` values for all \`Flow_UnlockTech\` nodes, and whether those technologies own ordinary mixed-alchemy crafts;
3. any direct \`Flow_UnlockCraft\` channels that unlock ordinary mixed-alchemy crafts.

A 0.1.1 probe, if required, should log only those bounded fields and no exact ingredient formulas.


## Progression Probe 0.1.1 — runtime candidate

Status: **built; runtime evidence pending**.

0.1.1 exists only to close the bounded residual left by accepted 0.1.0:
- enumerate \`Flow_UnlockTech\` and classify any ordinary mixed-alchemy targets owned by the unlocked tech;
- enumerate \`Flow_UnlockCraft\` and classify direct ordinary mixed-alchemy craft unlocks;
- record exact SmartRes price/lock/reward semantics for the early Clotho answer sets, including the menu answer they attach to;
- preserve the spoiler boundary by logging target names/arity only, never ingredient formulas.

Candidate identity:
- source branch: \`research/vanilla-alchemy-model\`;
- exact source / workflow head: \`18d4ad9ffc10b7a9e83d9178514f817a80277c58\`;
- CI run: \`37234084616\`, conclusion **success**;
- artifact ID: \`11314956708\`;
- handoff DLL: \`AlchemyProgressionProbe-0.1.1.dll\`;
- target: Graveyard Keeper 1.407.

Requested runtime action:
- replace 0.1.0 with this exact DLL;
- load any existing save into the game world once;
- return \`LogOutput.log\`.


## Progression Probe 0.1.1 — accepted runtime capture

Runtime evidence: user capture \`LogOutput(6).log\`, Graveyard Keeper 1.407.

Acceptance:
- exact probe 0.1.1 loaded successfully;
- \`AR_PROGRESSION_BEGIN\` and \`AR_PROGRESSION_DONE\` are present;
- no \`AR_PROGRESSION_ERROR\` occurred;
- summary: 114 controllers, 104 unique serialized graphs, 28 \`Flow_UnlockTech\` rows, 62 \`Flow_UnlockCraft\` rows, 13 bounded Clotho answer rows;
- privacy contract held: \`formula_rows_logged=0\`.

Authored unlock census:
- none of the 28 resolved \`Flow_UnlockTech\` nodes owns an ordinary picker-compatible mixed-alchemy target;
- none of the 62 \`Flow_UnlockCraft\` nodes directly unlocks an ordinary picker-compatible mixed-alchemy formula;
- Clotho's early \`Flow_UnlockTech\` is exactly **The Beginning Of Alchemy** and owns only the 2-slot bench, hand mixer and alchemy mill construction unlocks, not a finished mixed formula;
- the previously accepted Astrologer/Acid forced discovery therefore remains a special scripted-recipe channel rather than evidence that \`Flow_UnlockTech\` normally distributes mixed formulas.

Existing full GameBalance evidence additionally contains only:
- one item-level explicit \`UnlockAlchemy(...)\` owner: the Memory Tincture recipe item;
- one item-level \`UnlockRandomAlchemy()\` owner: the random alchemy recipe item.

### Early Clotho branch — now internally pinned

The initial Clotho answer set contains:
- \`сlotho_pot\`: requires 1 **Heal Potion**, rewards +20 relation;
- \`сlotho_vat\`: requires 1 Cauldron, rewards +10 relation;
- \`@сlotho_bee\`: requires 1 Bee, rewards +5 relation;
- \`@сlotho_intence\`: requires 1 **Life Powder**, rewards +5 relation.

This is the native authored split between:
- bringing the finished two-component alchemy product, or
- completing the reagent-side route with concrete precursor requirements.

No ordinary mixed formula is attached to Clotho's early \`Flow_UnlockTech\` / \`Flow_UnlockCraft\` path.

## Accepted progression anchors for puzzle prototyping

These anchors define representative **clean progression states**, not a claim that Graveyard Keeper has one global linear chronology. Actual save-state recipe knowledge always wins: if a formula is already known through prior crafting, a random recipe, or a specific authored reveal, AlchemyRiddle must bypass research for that formula.

### Onboarding / reagent anchor: Life Powder

Use Clotho's early **Life Powder** requirement as the native-grounded reagent-learning anchor.

Why:
- it is explicitly requested inside the same initial alchemy-introduction interaction;
- The Beginning Of Alchemy opens the decomposition/mixing infrastructure;
- it naturally teaches Study -> decomposition -> reagent identity before requiring the player to reason about a full formula;
- it is optional in vanilla because the finished Heal Potion route can bypass it, so the mod must not pretend this tutorial is globally mandatory.

### First clean two-slot target anchor: Heal Potion

Use **Heal Potion** as the first clean 2-slot unknown-formula prototype anchor.

Why:
- Clotho explicitly requests the finished product in the initial alchemy quest;
- it is an ordinary 2-component mixed-alchemy output;
- Clotho's early technology/craft unlock path does not hand out an ordinary mixed formula;
- therefore it provides exactly the desired product shape: visible authored need first, unknown formula second.

The target has alternate valid vanilla formulas, so the design goal is **discover a valid formula for Heal Potion**, not reconstruct a privileged canonical formula.

### First clean guaranteed-actionable three-slot anchor: Glue

There is no single globally well-defined chronological “first 3-slot formula” because Technology branches can be taken in different orders and several needs unlock together.

For prototyping, use **Glue** as the clean guaranteed-actionable 3-slot anchor:
- \`Embalm 2\` requires both \`Embalm 1\` and **Advanced alchemy**;
- therefore normal 3-component synthesis capability is structurally available before this need can be unlocked;
- the first \`Embalm 2\` authored recipe in loaded balance consumes Glue, while the same technology also exposes Preservative-class and another 3-slot-product need;
- no accepted ordinary-formula \`Flow_UnlockTech\` / \`Flow_UnlockCraft\` disclosure applies to Glue;
- unlike Acid, Glue is not currently a proved special scripted-reveal exception.

This is a **prototype anchor**, not a universal chronology claim. At runtime, if Glue is already known in the save, choose another still-unknown target from the same eligible progression state rather than creating a fake puzzle.

## Progression research checkpoint

The progression question is sufficiently closed for the next design phase.

No further runtime probe is required before resuming paper prototypes.

Current representative sequence:
1. **Life Powder** — teach/rehearse reagent research and decomposition;
2. **Heal Potion** — first clean 2-slot unknown-target deduction;
3. **Glue** — first clean guaranteed-actionable 3-slot deduction.

The next unknown belongs to puzzle design, not progression reconstruction: how the selected property vocabulary plus universal experiment grammar should make each of these states solvable, short, non-oracular and non-enumerative.
