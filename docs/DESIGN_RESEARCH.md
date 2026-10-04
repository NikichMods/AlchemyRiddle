# Design / Research Phase

Status: **OPEN — no production architecture selected**

## Research objective

Establish whether Graveyard Keeper 1.407's vanilla alchemy can support a coherent, targetable deduction puzzle with an added information layer, and identify the smallest mechanism that satisfies `docs/PRODUCT_REQUIREMENTS.md`.

## Evidence baseline at bootstrap

- Canonical shared source: `NikichMods/GraveyardKeeperResearch`.
- Required entry points: `AGENTS.md` and `docs/RESEARCH_INDEX.md`.
- Bootstrap began with no canonical shared alchemy-system entry.
- Static 1.407 host research has now been promoted to `NikichMods/GraveyardKeeperResearch/docs/ALCHEMY_SYSTEM.md` (shared-research commit `330087a2419c430e4baa3e31ae0477905cab0f4c`).
- The current loaded-`GameBalance` corpus has now been captured with `AlchemyRiddle Corpus Probe 0.1.0` from source `88287548f0095c0d8ddecd2d490c410401d43a93`; aggregate results are canonical in `docs/RUNTIME_CORPUS_ANALYSIS.md`.
- Answer-blind solver statistics and architecture-specific information-gain measurements remain open.

## Current verified vanilla findings

Verified against the accepted 1.407 decompile reference `Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9`; reusable host facts are canonical in the shared alchemy document.

- Mixed alchemy is owned by `MixedCraftGUI` / `CraftType.MixedCraft`, not the ordinary fixed-recipe card path.
- Native positional ingredient classes are Powder, Fluid and Essence; Universal items are accepted by the slot filter as an override.
- Exact ingredient identity **and position** are part of the mixed-craft recipe key.
- When an exact formula is absent, the failure path searches same-arity mixed-craft definitions sharing at least one ingredient in the same position, randomly chooses a qualifying definition, then derives goo identities from its other positions.
- Therefore vanilla goo is a real information signal, but it is stochastic and structurally points toward some qualifying mixed-craft definition rather than toward a player-selected desired output.
- The save tracks completed exact mixed crafts separately from simplified unlocked mixed-craft keys; scripted `UnlockRandomAlchemy` / `UnlockAlchemy` paths can mark formulas known without experimental discovery.
- Native Study-gated alchemy metadata already exists for decomposition classes and per-tier slot compatibility.

### Design implication already established

**Explaining the goo rule is insufficient as the complete product.** It can repair the interpretation gap, but the static vanilla algorithm contains no target-output channel that answers: “why should this experiment move me toward product X?”

That does not yet choose a replacement architecture. It establishes a required capability for any accepted architecture: some coherent target-specific information path must exist in addition to, or on top of, vanilla forward-discovery feedback.

## Accepted runtime corpus checkpoint — 2026-10-04

The anonymized read-only runtime probe completed successfully on Graveyard Keeper 1.407. See `docs/RUNTIME_CORPUS_ANALYSIS.md` for evidence identity, aggregate counts and caveats.

Key product-level facts:
- 44 records satisfy the probe's success-formula syntax classifier, but only **43** conform to the standard alchemy picker contract; one three-slot definition is a structural exception whose role remains open.
- The ordinary picker-compatible working corpus contains **43 formulas for 34 outputs**.
- Seven ordinary outputs have alternative formulas, so the target problem is generally “find a valid formula for X”, not “recover one unique canonical tuple”.
- The loaded category/filter envelope is vastly larger than the success corpus, so blind enumeration remains a poor intended path.
- The native goo conversion exposes **19 semantic classes** across the 35 ingredients used by ordinary success formulas; eight classes span Powder/Fluid/Essence forms.
- The auxiliary failure-definition table is regular and combinatorial rather than ad hoc.

### Design sequencing decision

Do not force the runtime corpus through the previously discussed candidate families. First design several complete player-facing loops from a clean slate:

`target X -> initial clue -> chosen experiment -> interpretable observation -> player inference -> next experiment/hypothesis -> vanilla verification`.

Then formalize the promising rulesets and test them against the concealed corpus. The quality ladder in `docs/PRODUCT_REQUIREMENTS.md` keeps guided/staged disclosure as a legitimate fallback improvement, while the intended target remains genuine deduction.

## Player-model exercise checkpoint — 2026-10-04

Status: **accepted product/UX evidence; not new host/runtime evidence**.

A guided answer-blind walkthrough was performed with fictional reagent names while preserving the verified vanilla failure-selection rules. The user began from the realistic position of having experimented with alchemy but never successfully discovered a vanilla mixed recipe. The purpose was not to solve a particular real formula, but to determine what a player can understand, infer, remember and resume.

### Two-slot result

Once the hidden vanilla algorithm was explicitly explained, a failed two-slot mixture could be interpreted as two competing local hypotheses: either the first attempted ingredient is the correctly positioned anchor and the goo describes the required second-slot class, or vice versa.

That loop can produce genuine deduction:
- observe a goo result;
- form two local hypotheses;
- test one exact candidate;
- reject it on failure or accept it on success;
- if rejected, test the remaining candidate.

However, this is only usable after the player is taught a rule close to the internal algorithm. It remains stochastic, consumes real reagents, and discovers **some structurally nearby valid recipe**, not a player-requested product.

### Three-slot result

The three-slot case exposed a more severe usability problem. A failed attempt can encode two non-anchor positions even when more than one attempted ingredient was already correct. Therefore:
- changing one slot can legitimately return the same apparent goo result;
- repeated controlled one-variable experiments need not yield locally legible evidence about the changed variable;
- a rational player may end up ignoring the goo signal and brute-forcing the changed slot around an accidentally good partial mixture.

In the walkthrough, this strategy reached success only because the initial mixture happened to contain two correct positional ingredients. The success therefore demonstrated local enumeration around a lucky partial match, not a robust deduction path.

### Resource and interruption cost

Alchemy attempts are not abstract free guesses. Reagents are acquired and processed through the wider Graveyard Keeper loop. Running out of a reagent can interrupt the reasoning chain with energy recovery, farming, corpse handling, NPC schedules, production, church activity and other tasks.

The cost of an experiment is therefore:
- consumed alchemical components;
- acquisition/processing work to replace them;
- **context-switch cost**: the player may return later without remembering the experiment history, previous inference or intended next test.

This is a first-class product constraint, not merely QoL polish.

### Persistence / external-memory requirement

Vanilla Study-gated alchemy metadata can preserve some ingredient/decomposition knowledge, but it does not preserve the player's experimental investigation as a usable reasoning state.

The final design must therefore provide enough persistent external memory for the player to recover:
- what was tried;
- what was observed;
- what facts have actually been established or excluded;
- what uncertainty remains.

This requirement does **not** select a recipe journal, automatic solver or next-step recommendation. The implementation mechanism remains open. A valid memory surface must preserve the player's reasoning rather than replace it.

### Genre-fit conclusion

Graveyard Keeper is not presented as a dedicated hardcore logic-puzzle game. In that context, opaque stochastic clues that require uninterrupted note-taking are likely to read as broken/noisy UX rather than as intentionally difficult puzzle design.

The desired alchemy puzzle can still require thought, but its rules, feedback, experiment economics and resumability must fit the interruption-heavy management/adventure loop around it.

### What vanilla is worth preserving

The walkthrough does not justify replacing all of vanilla alchemy. Potentially valuable foundations remain:
- the real vanilla formulas and normal alchemy-table success interaction;
- positional Powder/Fluid/Essence structure;
- native goo semantic classes as a possible taught information substrate;
- experimental discovery as the decisive act rather than automatic formula unlock.

What should not be relied on as the sole puzzle path:
- undisclosed knowledge of the internal failure-selection algorithm;
- stochastic goo from an arbitrary nearby recipe;
- human working memory across gameplay interruptions;
- repeated expensive low-information attempts;
- blind slot enumeration around accidental partial matches;
- forward discovery as a substitute for target-directed investigation.

### Updated design contract

A complete candidate loop must now demonstrate all of the following:

`target X -> useful starting constraint -> affordable meaningful experiment -> locally interpretable observation -> player inference -> persistable reasoning state -> justified next experiment -> vanilla verification`.

The next design phase should build small player-facing paper prototypes against this contract before choosing a production architecture.


## External deduction-system reference study — 2026-10-04

Comparative design research covered Alchemists / Little Alchemists, Turing Machine, The Search for Planet X, Black Box, Mastermind / Wordle, Zendo, Outer Wilds, Return of the Obra Dinn and Potion Craft.

The strongest recurring pattern was:

`fixed investigation target -> player-selected query/probe -> deterministic bounded observation -> persistent evidence -> player inference -> explicit hypothesis test`.

Useful transferable principles:

- **Stable subject:** feedback remains about the same hidden target/rule/state until the player changes the investigation.
- **Known query semantics:** before paying for an experiment, the player knows what kind of fact it can reveal.
- **Deterministic evidence:** repeating the same state/query does not randomly refer to a different hidden solution.
- **Externalized knowledge:** attempts, observations and established constraints persist outside human working memory.
- **Layered complexity:** players learn simple rules first; harder deductions combine already-known rules.
- **Proportionate information economy:** stronger/more precise tests may cost more, but low-information experiments should not impose substantial resource or context-switch cost.

Most relevant inspiration roles:

- **Alchemists / Little Alchemists:** stable hidden ingredient properties, deduction grid, information-bearing experiments, progressive teaching.
- **Turing Machine / Black Box:** player-chosen well-defined tests of hidden structure.
- **The Search for Planet X:** multiple research actions with explicit information scope/cost and a final hypothesis test.
- **Outer Wilds / Obra Dinn:** persistent evidence organization without automatically choosing the conclusion.
- **Mastermind / Wordle:** fixed-target deterministic feedback; position-local feedback reduces cognitive load.
- **Zendo:** reusable-law induction and a direct warning that hidden rules must be simpler for players than designers tend to expect.
- **Potion Craft:** legible ingredient behavior lets players intentionally steer toward a desired effect and preserve discovered routes, but its spatial-navigation architecture would exceed the current preserved-invariant envelope.

Important mismatch: Graveyard Keeper's success formulas are authored sparse tuples; current evidence does not establish a universal property-combination law that generates them. Therefore Alchemists-like property deduction cannot simply be copied without an added semantic/target-information layer.

No architecture is selected. The next design step remains paper-prototyping several complete player loops using different subsets of these principles.


## Entry-point hypothesis — 2026-10-04

Status: **accepted direction for research; first runtime coverage pass complete, unresolved progression channels remain**.

Do not expose a global catalog of all undiscovered alchemical products. AlchemyRiddle should remain silent about a product until vanilla gameplay has already given the player a legitimate reason to know that product exists.

Working knowledge states:

- **unknown product** — no AlchemyRiddle research entry;
- **known existence / open lead** — vanilla has exposed the product or created a visible need for it, but the formula is unknown;
- **known recipe** — the formula has been completed/unlocked through the normal game path.

Candidate vanilla lead sources include:

- a Technology-unlocked downstream recipe that becomes visible at its workstation and requires an unknown alchemical product;
- an already-visible ordinary recipe or blueprint that requires the product;
- acquiring or being able to acquire a physical sample;
- a quest/dialogue/progression requirement or mention.

Technology-tree presentation must not be conflated with workstation recipe presentation: the tree can unlock a recipe without showing its ingredient needs; the research lead may arise when that unlocked recipe is later viewed at the relevant station.

A future persistent research surface may also preserve **why** a lead exists (for example, needed by a known recipe/task or obtained as a sample), which helps both targetability and continuity without revealing the hidden formula.

### Runtime coverage result

Read-only anonymized loaded-`GameBalance` probe 0.2.0 completed successfully.

Across the **34 ordinary picker-compatible mixed-alchemy outputs**:
- 18 have a measured structural entry through a Technology-owned or default-visible downstream recipe/blueprint;
- 17 have a static vendor-stock candidate;
- the union covers 26 outputs;
- 8 remain uncovered by this first pass.

The uncovered set is informative rather than simply missing data: seven have authored blueprint consumers whose actual non-Technology unlock/visibility source is not yet classified, while one has no measured ordinary consumer, blueprint consumer, vendor-stock candidate or direct visible `QuestDefinition` expression reference.

Do not interpret the first-pass counts as chronological progression proof. Vendor availability timing is unresolved, direct `QuestDefinition` expression scanning does not cover arbitrary FlowCanvas/dialogue content, and blueprint-only consumers can be unlocked by separate `UnlockCraft` paths.

The next entry-point research question is therefore narrow:
1. classify the real unlock/visibility source for the seven blueprint-only targets;
2. then inspect the single no-consumer/no-vendor target for dialogue/FlowCanvas/sample/progression channels;
3. only if those fail, define the smallest product fallback for targets with no natural vanilla lead.


## Current competitor / overlap audit

Checked current public descriptions and the current source tree rather than relying on remembered behavior.

### Alchemy Research Redux

Current source-tree changelog declares **0.1.9 (2 October 2026)**. The Nexus detail page can lag at 0.1.8 even while current Nexus listings show a 2 October update, so source is the stronger version-state signal for behavior comparison.

Observed capability:
- result preview for ingredient combinations that the mod considers known;
- current code records exact successful mixes and loads known recipes into its own persisted recipe list;
- 0.1.8 added last-mix refill / optional auto-refill;
- 0.1.9 fixes preview refresh behavior.

Overlap with AlchemyRiddle: **known-result presentation / repetition QoL**, not target-directed discovery of an unknown product.

### Decomp Delight / Item Description — Display Element

These expose the decomposition element of researched items. This overlaps with **ingredient/property legibility** and may be compatible with a future property/signature solution family, but it does not provide a route from an unknown desired mixed product to its formula.

### Useful Alchemy

This is effectively a visual external recipe reference. It solves recall/look-up by showing recipe schemes and is intentionally outside AlchemyRiddle's desired discovery model.

### Current overlap conclusion

No inspected current mod provides the whole capability:

`unknown required product -> target-specific investigation -> interpretable experiments -> deductively justified vanilla formula`.

This conclusion is provisional only with respect to the broader ecosystem search; repeat the audit before release if scope materially changes.

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
