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
- 25 are consumed by at least one authored downstream ordinary recipe or build blueprint;
- 18 already have a measured structural entry through a Technology-owned or default-visible downstream recipe/blueprint;
- 17 have a static vendor-stock candidate;
- the union of measured structural/vendor channels covers 26 outputs;
- 8 remain uncovered by this first pass;
- among the 9 outputs with no downstream craft/build consumer, 8 have a vendor-stock candidate and only 1 has neither measured demand nor vendor sample channel.

The uncovered set is informative rather than simply missing data: seven have authored blueprint consumers whose actual non-Technology unlock/visibility source is not yet classified, while one has no measured ordinary consumer, blueprint consumer, vendor-stock candidate or direct visible `QuestDefinition` expression reference.

Do not interpret the first-pass counts as chronological progression proof. Vendor availability timing is unresolved, direct `QuestDefinition` expression scanning does not cover arbitrary FlowCanvas/dialogue content, and blueprint-only consumers can be unlocked by separate `UnlockCraft` paths.

The next entry-point research question is therefore narrow:
1. classify the real unlock/visibility source for the seven blueprint-only targets;
2. then inspect the single no-consumer/no-vendor target for dialogue/FlowCanvas/sample/progression channels;
3. only if those fail, define the smallest product fallback for targets with no natural vanilla lead.


## Accepted research-lead creation rule — 2026-10-04

Status: **product direction accepted; exact UI presentation remains provisional**.

The primary way an AlchemyRiddle research task is created is:

> **When vanilla first exposes a visible need for an alchemical product whose formula is not already known to the player, that product becomes an available research lead.**

The mod must not expose a global catalog of undiscovered products. It reacts to knowledge vanilla has already legitimately surfaced.

The trigger should be based on the resulting visible vanilla need, not narrowly on one progression mechanism. A need may become visible because a Technology unlock exposes a downstream recipe, a quest/progression path unlocks a craft separately, or another vanilla path makes the requirement visible.

Scope boundary:
- If vanilla explicitly teaches/gives the formula as part of the same progression path, the product is not an AlchemyRiddle unknown-formula puzzle merely because it is crafted at an alchemy station.
- If vanilla creates a need but also offers a non-crafting solution such as purchasing the product, AlchemyRiddle may record the product as a research lead but must not present research/crafting as the only correct solution.

### Provisional journal UX

A persistent alchemy journal is the working UX direction for choosing among discovered research leads and resuming interrupted investigations.

When a new unknown-product lead is created, a native-style transient notification is desirable in principle, conceptually like:

- “New entry added to the alchemy journal”
- “Unknown alchemical product added to the journal”

Exact wording/presentation is **not selected** and should be tested later against spoiler/steering risk. In particular, an early product need may intentionally be solvable by finding or buying the item; a notification should not falsely imply that the player is required to synthesize it.

The journal/notification mechanism remains a presentation hypothesis, not a production architecture decision. Do not research the exact popup host seam until that UI is selected as implementation work.

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


## Paper prototype round 1 — 2026-10-04

Status: **accepted player-facing UX evidence; all five tested cores rejected in their current form**.

Five deliberately different paper prototypes were walked answer-blind from the common entry point:

`visible need for unknown product X -> journal entry -> player selects X -> first meaningful investigation`.

The prototypes used fictional products/reagents and did not disclose real vanilla formulas. The purpose was to test player reasoning and subjective legibility before formal corpus simulation.

### Prototype 1 — purchased progressive constraints

The journal offered paid research actions that progressively disclosed positional/property constraints, with stronger or different clues carrying different resource costs.

Observed player behavior:
- resource price materially affected choice; forgetting to display the price invalidated one decision and required rollback;
- once a cheap action had a predictable information payoff, the rational strategy became to keep buying information until concrete ingredients emerged;
- the player described the loop as buying the answer piece by piece rather than solving it;
- multiple intermediate steps felt like grind when they did not require inference.

Conclusion: **reject as core deductive loop**. It can function as guided disclosure/fallback, but in its tested form it is effectively staged answer purchase.

### Prototype 2 — global property-count queries

The player selected a known reagent as a sample, but the test actually answered a global question such as how many target ingredients shared that reagent's property family.

Observed player behavior:
- the first query had no evidence-based reason to prefer one family over another, so the player invented thematic/lore justification merely to choose;
- selecting a concrete item but receiving only an abstract family-level answer felt semantically misleading;
- after receiving a global result, the player's natural next question was local/positional, but the offered query language did not let the player ask it.

Conclusion: **reject in tested form**. A valid query system must make the first query meaningfully choosable and let newly produced questions be investigated directly.

### Prototype 3 — per-slot compatibility oracle

The player could cheaply ask whether a concrete ingredient was compatible with a concrete slot for the selected product.

Observed player behavior:
- the player immediately recognized the finite slot-filtered search space and began testing candidates in list order;
- independent positive compatibility marks naturally implied that the marked ingredients would compose a valid recipe;
- when three individually compatible ingredients failed together, the result felt deceptive rather than revelatory;
- after that failure the rational strategy became systematic enumeration of remaining candidates.

Conclusion: **reject as core**. A deduction-grid presentation does not create deduction when the underlying action is a yes/no membership oracle. Independent local truths must not imply a whole-recipe relation that the system then violates without prior rule support.

### Prototype 4 — compositional property algebra

The target exposed a property/signature and known ingredients had visible properties. Pair experiments plus transformation rules were intended to let the player derive the recipe through a small algebra.

Observed player behavior:
- this was the first prototype that caused genuine attempts to reason rather than merely buy/query candidates;
- however, the player repeatedly had to reread the rule system and was uncertain what symbols/arrows meant;
- ambiguity over whether interactions were ordered, whether pair results collapsed state, and how three ingredients composed dominated the task;
- the player eventually wanted to test all three ingredients together because the pair grammar was not sufficient to form a reliable mental model.

Conclusion: **promising principle, rejected complexity level**. Genuine inference appeared, but the tested transformation grammar was too close to a standalone logic game for Graveyard Keeper's broader management loop. If property composition survives, its rule set must be drastically simpler and locally obvious.

### Prototype 5 — two explicit competing hypotheses

A free initial clue reduced a two-slot recipe to exactly two candidate formulas. The player could perform a cheap discriminating test on either side before committing real ingredients.

Observed player behavior:
- the player immediately saw that either test had identical information value;
- the choice between tests was therefore a choice in presentation only, not a reasoning decision;
- the cheap test still had economic value because it avoided risking two real ingredients;
- once one hypothesis was rejected, the remaining formula was perceived as already fully known; the required final vanilla synthesis felt ceremonial;
- the player compared the interaction to choosing between two buttons where either button necessarily resolves the problem.

Conclusion: **reject as core deductive puzzle**. Efficient binary discrimination is not sufficient when the player has no substantive reason to choose one experiment over another and no inference beyond executing the forced discriminator.

### Cross-prototype findings

The round established several stronger design constraints:

1. **Information gain alone is not enough.** A mechanically efficient test can still be boring if the player has no reasoned choice of what to test.
2. **The experiment-selection decision must matter.** Two actions with identical expected consequences are not meaningful agency merely because their labels differ.
3. **Do not make the journal a recipe vending machine.** Repeatedly purchasing finer constraints converges to staged disclosure even when no exact ingredient is directly printed.
4. **Do not disguise enumeration as deduction.** A yes/no oracle over candidates remains brute-force search with cheaper steps.
5. **Local positive facts must compose predictably.** If several individually positive slot facts do not imply a viable combined hypothesis, the system must make the missing relation explicit before the player is encouraged to combine them.
6. **Some genuine rule application is desirable, but the grammar must fit Graveyard Keeper.** Prototype 4 produced the most actual reasoning but exceeded the acceptable teaching/working-memory burden.
7. **Final vanilla synthesis should be evidential, not ceremonial.** The player should reach it with a justified hypothesis that still benefits from real verification, rather than after the system has already proved the exact formula beyond reasonable doubt.
8. **Experiment cost is part of the puzzle.** The player consistently considered cheap diagnostic cost versus risking real ingredients. Resource economics can make a test worthwhile, but cannot substitute for intellectual content.
9. **Every action surface must show cost at decision time.** Omitted cost materially changes behavior.
10. **Candidate completeness must be knowable.** Across all prototypes, the player identified a global uncertainty: if an undiscovered/unprocessed reagent could still be required, no closed candidate-space deduction is trustworthy. A future design must either:
   - guarantee and communicate that the currently relevant candidate pool is complete for target X;
   - base reasoning on properties/laws that remain valid even when unseen reagents exist; or
   - explicitly surface “insufficient reagent knowledge” as a legitimate research state rather than allowing false closure.

### Resulting design target

The next candidate should not start from “what clue can we sell?” or “what yes/no question can the journal answer?”

It should instead aim for:

`visible need X -> useful but incomplete starting observation -> player forms more than one plausible explanation -> player chooses an experiment because different possible outcomes would discriminate between those explanations -> result is locally interpretable -> journal preserves the evidence -> player revises the explanation -> vanilla synthesis tests a still-player-owned hypothesis`.

The key unresolved challenge is to create **meaningful experiment selection without a heavy bespoke logic algebra**.

No production architecture is selected. Production mutation remains **BLOCKED**.


## Paper prototype round 2 and target experience refinement — 2026-10-04

Status: **accepted player-facing UX evidence; no production architecture selected**.

Three second-generation prototypes were tested after round 1. The design target was simultaneously refined by the user: alchemy should make a broad Graveyard Keeper player feel like a **successful researcher/alchemist** after a small amount of thought, without becoming a standalone hardcore logic game or consuming disproportionate time/attention.

### Target player experience

The desired experience is not maximal puzzle depth. It is:

- a brief role-play of doing real alchemical investigation;
- a small, legible reasoning step;
- a satisfying moment of “I worked that out” / “I am clever”;
- low rule-reading and working-memory burden;
- little or no grind-like enumeration;
- short enough to fit among Graveyard Keeper's many other systems.

The design should bias toward **competence and insight**, not difficulty for its own sake.

### Prototype 6 — comparative “warmer/colder” substitution

A trial mixture could be compared against a target after changing one component; feedback reported whether the reaction moved closer, farther away, or preserved character with changed strength.

Observed:
- the substitution rule itself was immediately understandable and well received;
- however, there was still no evidence-based starting mixture;
- the player therefore chose the first listed mixture and then performed coordinate search: change one variable, keep the warmer result, move to the next candidate;
- after several moves the interaction remained directed enumeration rather than hypothesis-driven inference.

Conclusion: **reject as core**. Simple comparative feedback solves legibility but not meaningful experiment selection.

### Prototype 7 — reference sample with orthogonal observable reactions

The player possessed a small sample of target product and could compare trial mixtures against three concrete reactions: heating, water dilution, and salt contact.

Observed:
- the player initially had to discover what each test meant;
- controlled substitutions produced a real hypothesis that heating primarily tracked powder, water tracked fluid, and salt tracked essence;
- the player then used that hypothesis to select informative tests and successfully chose a final formula before all observations were filled in;
- the final vanilla synthesis functioned as genuine verification of a player-owned hypothesis;
- this was the strongest “I am investigating” loop so far.

However:
- once the mapping from tests to slots was inferred, subsequent recipes would collapse into three independent candidate searches;
- the system therefore contains an interesting **one-time meta-discovery**, but risks becoming organized slot-by-slot enumeration afterward.

Conclusion: **retain as a promising design ingredient, not yet a reusable core**. Concrete observable experiments and an exemplar/sample create good role-play and legibility; repeated recipes need target-specific interaction so the same solved diagnostic routine does not trivialize every case.

### Prototype 8 — simple universal adjacency rule plus target-specific constraint

Known ingredient signs and a universal rule (“adjacent components in a stable mixture must have different signs”) were combined with one target-specific fact (“exactly two signs occur in the formula”) and a comparative link test.

Observed before the first experiment completed:
- although each individual rule was simple, the combined representation felt mentally bulky;
- the user explicitly noted that Graveyard Keeper players are generally more casual than a dedicated puzzle audience and that alchemy should provide a brief competence high rather than demand sustained formal reasoning;
- while choosing the first trial, the player immediately selected two adjacent reagents with the same sign, violating the just-restated universal rule;
- the rule had therefore already fallen out of working memory during ordinary choice construction.

Conclusion: **reject this complexity envelope**. “Only a few simple rules” is not enough if several dimensions must be held simultaneously during candidate construction. The practical test is whether the rule remains naturally usable while acting, not whether it is concise on paper.

### Additional vanilla-legibility observations

The player identified several pre-puzzle uncertainties that may need separate UX treatment:

- vanilla does not make the powder/fluid/essence positional grammar sufficiently obvious at first glance;
- candidate semantics for “fluid” are broader than decomposition-derived alchemical fluids and may include ordinary liquids such as water, oil, alcohol or blood, increasing perceived search space;
- a future puzzle must distinguish what counts as a relevant candidate without falsely rewriting vanilla mechanics.

These are research/design questions, not accepted production changes.

### Updated core-design criterion

A promising core should satisfy all of the following simultaneously:

1. **One-screen mental model:** the currently relevant rule and evidence should remain usable without rereading several interacting rules.
2. **Small initial choice set:** the first meaningful experiment should not begin from a large arbitrary Cartesian product.
3. **Predict before observing:** the player should be able to state a simple expectation before paying for an experiment.
4. **Concrete observation:** prefer visible/alchemical phenomena over abstract oracle language where possible.
5. **Target-specific inference:** solving the general system once must not reduce every later recipe to the same slot-by-slot routine.
6. **Short competence arc:** a typical investigation should produce useful understanding quickly enough to feel clever rather than diligent.
7. **Final synthesis retains uncertainty:** the real craft should confirm a justified hypothesis, not merely enact an answer already fully disclosed by the research UI.
8. **External memory, low reading burden:** the journal should preserve evidence compactly, but the player should not need to reread a large experiment log to continue.
9. **Candidate-space trust:** the player must know whether current reagent knowledge is sufficient to solve the target.

### Current direction after round 2

The strongest ingredient discovered so far is the **reference-sample / concrete-observation** pattern from prototype 7, especially controlled comparison and a final synthesis performed before exhaustive proof.

The strongest unresolved problem is **repeatability without routinization**: how to give each target a tiny distinct inference without introducing a heavy formal rule system or reverting to candidate enumeration.

No production architecture is selected. Production mutation remains **BLOCKED**.


## Broad design-space survey and corpus screening — 2026-10-04

Status: **accepted research/design checkpoint; no production architecture selected**.

This pass deliberately widened the solution space after paper-prototype round 2 instead of iterating immediately on the reference-sample idea. The purpose was to prevent the strongest current prototype ingredient from becoming architecture by momentum.

### Frozen target experience for this survey

The candidate core should aim for a short micro-deduction, roughly on the order of a few minutes rather than a standalone logic-game session:

- one currently relevant thought/rule at a time;
- a natural target-specific starting observation;
- the player can predict what an experiment might distinguish before paying for it;
- concrete, preferably diegetic/alchemical feedback;
- a meaningful choice of experiment rather than a forced information button;
- persistent external memory with low rereading burden;
- target-specific variation so solving the general system once does not routinize every later recipe;
- a justified player-owned hypothesis before final synthesis when possible;
- final vanilla synthesis remains preferred evidence, but direct resolution is allowed after genuine logical exhaustion.

### Morphological map

The design space is better described by independent axes than by one monolithic "alchemy puzzle" idea:

1. **Investigation anchor** — visible downstream need, physical target sample, a known reference product/recipe, a prior failed mixture, or a discovered relation to another known recipe.
2. **Hidden object of reasoning** — exact tuple, relation to a known tuple, whole-mixture signature, ingredient-role relation, latent property relation, or a small target-specific reaction law.
3. **Player intervention** — substitute one component, compare full mixtures, apply a diagnostic condition/probe, perturb a known recipe, construct a counterexample, or use vanilla synthesis.
4. **Observation shape** — aggregate match/strength, categorical phenotype, directional difference, relational outcome, native goo evidence, or a bounded positive/negative example.
5. **Inference unit** — eliminate a whole hypothesis, attribute a difference, infer a relation, infer one causal role, or revise a small rule.
6. **Repetition model** — one universal law, universal test vocabulary with target-specific cases, authored per-target cases, or a hybrid.
7. **External memory** — compact facts/hypotheses in the journal rather than a raw chronological log.
8. **Resolution** — final craft while uncertainty remains small, or explicit resolution when the evidence has already made the formula unique.

This map exposes an important degree of freedom that earlier prototypes underused: the project does **not** require one elegant universal algorithm that automatically generates every puzzle. The corpus is bounded enough that a common experimental grammar may coexist with target-specific authored/selected cases.

### Anti-tunnel-vision reference findings

External design references reinforce several distinctions:

- **Mastermind** is useful less for its colored pegs than for controlled hypothesis testing: changing one factor between experiments can make the comparison itself carry the inference. Scientific-reasoning literature explicitly uses it to teach controlled experiments, hypothesis discrimination and severe testing.
- **Zendo** demonstrates player-authored counterexamples against a hidden rule, but its own guidance also highlights the difficulty of choosing rules that are actually pleasant to infer. For AlchemyRiddle, the transferable part is "build a focused experiment for the current hypothesis", not an open-ended secret-law system.
- **Alchemists** shows the strength of stable hidden properties plus persistent deduction notes, while also illustrating a complexity level that would be too large to copy directly into Graveyard Keeper.
- **The Search for Planet X** shows explicit-scope research actions and externalized notes, but its hour-scale formal deduction loop is not the desired pacing.
- **Black Box** shows how a small deterministic interaction law can make probes meaningful because every result constrains the same stable hidden object.

Reference sources consulted in this pass:
- https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1000578
- https://www.looneylabs.com/games/zendo
- https://www.looneylabs.com/sites/default/files/literature/Zendo%20Rules%20Book%202.pdf
- https://alchemists.czechgames.com/rules/
- https://renegadegamestudios.com/the-search-for-planet-x/
- https://www.theblackbox.games/

### Hidden-corpus structural screening

The accepted anonymous 43-formula / 34-output corpus was re-used directly rather than asking for another runtime capture.

#### Reference-formula proximity

Comparing exact same-arity tuples:

- **23 / 24** ordinary two-slot formulas have another ordinary formula at Hamming distance 1;
- the remaining two-slot formula's nearest neighbor is distance 2;
- only **2 / 19** ordinary three-slot formulas have a distance-1 neighbor;
- **17 / 19** three-slot formulas have nearest distance 2.

Consequence: "modify a known neighboring recipe" is structurally attractive for two-slot alchemy but cannot be the sole universal mechanism for three-slot alchemy without adding a stronger abstraction or accepting two simultaneous unknown changes.

#### Shared-motif density

Among three-slot formulas, exact two-ingredient overlap with a formula for a different output is rare:

- only **2 / 19** three-slot formulas have such a two-ingredient neighbor;
- the other **17 / 19** share at most one ingredient with every different-output three-slot formula.

All 43 ordinary formulas nevertheless belong to one connected graph when a single shared ingredient is sufficient for an edge. Single-ingredient relations are therefore broadly available but usually too weak by themselves to provide a short target-specific deduction.

#### Goo-class disclosure strength

Within each normal positional slot, goo identity is one-to-one among ingredients that participate in the ordinary success corpus.

Consequence: a clue of the form "slot 2 uses goo class G" is, for the current corpus, effectively a disguised exact-ingredient reveal. Goo remains useful as a semantic alphabet, but target-level clues should prefer relations, aggregate effects or controlled comparisons if the intended quality is deductive narrowing rather than staged disclosure.

#### Multiple valid formulas

Seven ordinary outputs have alternative formulas. Any target-sample comparison, scoring or hypothesis system must treat the hidden answer as a **set of valid formulas** and avoid penalizing the player for converging on a different vanilla-valid formula.

### Solution-family survey

#### 1. Whole-mixture aggregate comparison

A complete trial mixture is compared with the selected target and returns a deterministic **aggregate** observation about the mixture as a whole rather than slot-local membership. A Mastermind-like match/resonance count is the simplest abstract form; a more diegetic version could express the same information as reaction strength or number of matching phases.

Strengths:
- one-screen rule;
- target remains stable;
- controlled substitution can support real comparative inference;
- final craft can remain a genuine hypothesis test.

Risks:
- without a useful starting state or bounded candidate pool, it degrades into coordinate search;
- numeric feedback can feel like an oracle/minigame unless strongly integrated into alchemical presentation.

**Retain for prototype.**

#### 2. Known-recipe differential / analogy

Start from a recipe the player already knows and investigate how the target differs from that reference. Experiments identify which part of the known reaction must change and why.

Strengths:
- natural starting hypothesis rather than an arbitrary first mixture;
- strongly supports "change one thing, observe the difference";
- especially good structural fit for the two-slot corpus.

Risks:
- weak universal coverage for three-slot formulas;
- actual progression must provide an appropriate known reference at the time the target becomes relevant.

**Retain for prototype, explicitly as a possible station-specific/hybrid mechanism rather than a presumed universal core.**

#### 3. Common assay vocabulary + target-specific micro-cases

Use a small stable set of experiment verbs/observations, but author or select a short case for each target so the relevant comparison and hypothesis structure varies by product. The rule vocabulary stays learnable; the content does not collapse into one solved routine.

Strengths:
- directly attacks the round-2 repeatability/routinization problem;
- the bounded 34-output corpus makes per-target validation realistic;
- difficulty and experiment count can be tuned to the desired competence arc;
- does not require inventing one deep universal algebra that happens to generate the authored vanilla tuples.

Risks:
- higher content/localization/testing burden;
- bad authoring could become arbitrary flavor-text trivia or a hidden fixed click sequence;
- case clues must be grounded in stable, taught experiment semantics rather than unexplained bespoke lore.

**Retain as the strongest broad family to prototype.**

#### 4. Target-bound vanilla-goo hybrid

Keep native failed-mixture/goo evidence as a meaningful part of the loop, but add a target-specific anchor so the player has a reason to run a particular experiment and can interpret the resulting evidence in relation to X.

Strengths:
- maximizes continuity with vanilla;
- reuses a real existing semantic layer;
- may require less wholly new puzzle vocabulary.

Risks:
- the verified vanilla three-slot failure path is stochastic and not locally attributable enough on its own;
- a target anchor strong enough to repair that may simply become a new oracle layered on top;
- per-slot goo hints are too revealing under the current corpus.

**Retain for one prototype as the "least replacement" control, but do not assume it will survive.**

#### 5. Stable property/signature algebra

Give ingredients stable traits and derive target behavior compositionally.

**Do not prioritize another full prototype yet.** Round 1 prototype 4 and round 2 prototype 8 already show that even concise multi-rule composition exceeds the desired working-memory envelope. Reopen only if a one-rule formulation emerges.

#### 6. Pair-compatibility / membership probing

Ask whether ingredient A, pair A+B, or slot candidate A is compatible with target X.

**Reject as core.** This remains enumeration with a cheaper oracle unless a richer relation changes the inference structure.

#### 7. Explicit whole-formula hypothesis cards + discriminating tests

Present a few complete candidate formulas and let the player choose a discriminator.

**Do not prioritize.** Prototype 5 showed that a small explicitly enumerated hypothesis set easily becomes a forced binary button press, while also disclosing too much of the answer surface.

#### 8. Downstream-use / lore-derived clue system

Infer ingredients from what the target is used for or from authored flavor associations.

**Supplement only.** The vanilla formula corpus is authored and current evidence does not establish a universal semantic law tying downstream use to recipe composition. Such context can motivate an investigation but should not silently become arbitrary mechanical truth.

#### 9. Pure vanilla-goo teaching

Teach the existing failure rule and preserve vanilla experimentation.

**Supplement only.** Already disproved as a complete targetability solution and particularly weak for three-slot local inference.

#### 10. Progressive research disclosure

Pay/time-gate increasingly precise clues until the answer is effectively known.

**Fallback quality floor only.** It can remove wiki dependence but remains level-2 guided disclosure rather than the target deductive experience.

### Prototype shortlist after the survey

The next blind paper-prototype round should contain four orthogonal candidates:

1. **Authored micro-case with a common assay vocabulary** — test whether curated target-specific setup can provide variety without feeling arbitrary.
2. **Whole-mixture aggregate resonance** — test a Mastermind-like controlled-comparison loop with a deliberately useful starting observation, not a random first guess.
3. **Known-recipe differential** — test the strong two-slot structural opportunity and whether "modify what I already know" feels naturally alchemical.
4. **Target-bound vanilla-goo hybrid** — test the least-replacement design and determine whether a target anchor can rescue native feedback without becoming an oracle.

The prototypes should stay answer-blind and fictional. Their first purpose is **player-experience discrimination**, not proving corpus-wide mechanics. Only families that survive that pass should receive a formal solver/information-gain implementation against all 34 targets.

No production architecture is selected. Production mutation remains **BLOCKED**.


### Prototype 9 — authored micro-case: live observations

Status: **closed as a blind prototype; retain only as a viable but experientially weak fallback/control pattern**.

Early findings before the first experiment resolves:

- Any experiment that consumes a limited target sample must show **current sample count**, **whether the sample is replenishable**, and **the practical replacement path/cost** before the player commits.
- The same applies symmetrically to reagent-consuming tests. A player's rational experiment choice depends on the relative acquisition/replacement burden of target samples versus ordinary reagents.
- Therefore prototype evaluation must not assume “sample expensive, reagents cheap” (or the reverse) without defining it. If actual Graveyard Keeper progression makes that relation target-dependent, the production design must either expose the relevant costs clearly or avoid relying on hidden acquisition economics to create meaningful choice.
- Irrecoverable loss of the only research sample is undesirable for the intended broad-player experience. Current prototype assumption: depleted samples can be reacquired, though potentially at a nontrivial cost.


Additional live finding after the first comparative test:

- The prototype must present the currently legal research actions explicitly in the UI after every observation. Keeping the action set only in tutorial text or in the player's memory is unacceptable for the intended low-working-memory experience.
- Recipe arity and unresolved slots must remain visually explicit. After confirming a two-reagent phenomenon inside a three-slot recipe problem, the player may naturally feel that they have an “obvious recipe candidate” even though the third slot is still completely unconstrained.
- Therefore observations about a pair must not visually collapse into a near-complete recipe unless there is a justified rule connecting that observation to all remaining recipe slots. The UI should distinguish “confirmed phenomenon/relation” from “complete formula hypothesis.”


### Paper-prototype interface discipline

Blind paper prototypes must simulate a usable player-facing interface rather than relying on conversation history or the facilitator's memory. Otherwise the test measures the user's ability to remember the chat, not the proposed game mechanic.

For every decision point, present a compact but complete state panel containing at least:

- **Current research target** and recipe arity/station where relevant.
- **Available candidate reagents**, grouped by slot/category.
- **Current resources and costs** that materially affect the decision: target-sample portions, reagent costs/consumption, and whether/how depleted resources can be reacquired.
- **Known rules / research model** needed to interpret experiments. Rules introduced earlier must remain accessible; do not require the player to remember tutorial prose from previous turns.
- **Research notebook / established findings**: a persistent summary of experiments already performed and the observations/inferences actually established. Preserve the distinction between raw observation, supported hypothesis, and confirmed formula fact.
- **Unresolved state**: e.g. unknown recipe slots or live competing explanations.
- **Currently legal actions**, including their costs and required selections.

After every experiment, update this same state panel before asking for the next choice. The prototype should behave as though the player can inspect this information at any time in the real UI.

Do not omit interface information merely because it appeared earlier in the chat. If a prototype only works when the player scrolls back through the conversation, treat that as an interface/test-design defect rather than player error.


Additional prototype 9 finding — dominated experiment choice:

- The initial comparative trial `Iron Dust + Brine` was informationally redundant because the player was already told that this pair produces mechanism A's film. Re-performing a known reaction consumed resources without discriminating the live hypotheses.
- Meanwhile the target-sample heat test was an explicit direct discriminator between A and B. Therefore the action menu contained a **strictly dominated experiment**: one option spent resources for no new information while another directly resolved the stated ambiguity.
- This is a prototype-design failure, not a player mistake. Meaningful research choice requires each offered experiment to have a plausible information role under the player's current knowledge; known-outcome demonstrations should not masquerade as investigative options.
- Future blind prototypes should be checked before play for obvious dominance/redundancy among available experiments. If one action cleanly partitions all live hypotheses and another cannot change belief state, the latter should either be removed, repurposed, or have a different justified objective.


Additional prototype 9 finding — implicit inference rule and hidden-state precommitment:

- The player's proposed continuation is logically coherent **if** the research grammar contains an explicit rule that identifying mechanism A in the target establishes that the corresponding A-producing reagent pair is present in the target recipe. Under that stronger rule, the heat test narrows the three-slot formula to exactly three complete candidates differing only in the essence slot, after which vanilla synthesis can test them.
- The live prototype did not actually state that inheritance rule. It therefore oscillated between two different models: (a) target phenotype merely resembles a known reaction, which does not imply ingredient membership; and (b) target phenotype identifies a constituent reaction pair, which does. This ambiguity is a prototype-specification defect.
- A short residual synthesis search is not automatically a product failure. The product contract permits final crafting to serve as hypothesis verification, and even logical exhaustion can resolve the answer. What matters is whether prior research did meaningful target-specific narrowing and whether the remaining attempts feel like a bounded verification step rather than the primary discovery method.
- Future blind prototypes must precommit all hidden state before player interaction: the hidden formula / valid-answer set, observation model, inference rules, experiment outcomes, costs, and stopping/resolution conditions. Do not select or adapt the hidden answer after seeing player choices. If that precommitment was not made, stop the blind test rather than retrofitting outcomes.


Prototype 9 experience assessment — viable but weak:

- The player accepted the core logic: a meaningful research step may narrow a large formula space to a small residual set, and vanilla crafting may then verify the remaining hypotheses.
- However, **logical viability is not sufficient**. In this instance the experience felt weak/boring: one obvious diagnostic test did most of the narrowing, then the remaining essence slot would be resolved by up to three straightforward synthesis attempts.
- This likely satisfies “works” but only weakly satisfies the intended competence fantasy. The player is not building or testing a rich enough chain of reasoning to strongly feel “I worked that out”; instead the interaction risks feeling like one gate followed by bounded cleanup enumeration.
- Therefore retain this pattern as a viable fallback/control structure, not as a leading design. Future prototypes should seek a similarly short loop while giving the player at least one genuinely meaningful intermediate hypothesis choice or inference, without increasing working-memory burden.


Prototype 9 final disposition:

- **Logic:** viable in the stronger explicitly specified form where a diagnostic mechanism legitimately maps to a constituent reagent relation.
- **Blind-test integrity:** compromised by underspecified inference semantics and failure to precommit the hidden formula before play; do not treat the specific playthrough as clean comparative evidence.
- **Experience signal:** weak/boring relative to the product target. One obvious discriminator performed most of the research work, leaving a short cleanup search.
- **Retain/reject:** retain as a fallback/control structure, not a leading architecture.
- **Next prototype:** whole-mixture aggregate resonance, with facilitator state fully precommitted and persisted before the first player choice.


### Prototype 10 — active blind test

Status: **active**. Complete facilitator state was precommitted before the player's first action under the paper-prototype protocol. Do not expose its hidden contents during blind play.

Prototype 10 begins only after commit identity of that state exists. Player-facing observations must be generated from the precommitted model without adaptation.


### Prototype 10 — result

Status: **completed blind prototype**.

Player-facing sequence:
1. Initial calibration: White Ash + Dew + Echo -> resonance 1/3.
2. Player changed only the powder: Black Chalk + Dew + Echo -> 0/3.
   - Deduction: White Ash is the correct powder; Dew and Echo are excluded.
3. Player kept White Ash/Echo and changed the liquid: White Ash + Brine + Echo -> 2/3.
   - Deduction: Brine is the correct liquid.
4. Player tested White Ash + Brine + Spark -> 2/3.
   - Since White Ash and Brine were already established correct, Spark is excluded and Shadow is uniquely determined as the essence.

Meaningful paid resonance tests: **3**.

Player-experience findings:
- The rules were immediately described as simple, clear and understandable.
- The player naturally used controlled one-variable changes without prompting.
- Each result supported an immediate local deduction.
- The interaction stayed within a very small working-memory envelope.
- The formula was uniquely determined without brute-force enumeration and without needing a ceremonial final craft.
- However, the interaction pattern is structurally close to systematic coordinate/slot isolation: once the aggregate-score rule is understood, the natural strategy is to change one slot at a time and infer that slot from score deltas.
- This means the prototype is mechanically cleaner and more satisfying than prototype 9, but it may still become routine quickly across many recipes rather than sustaining an "alchemical investigation" fantasy.

Blind-test integrity:
- hidden formula, scoring semantics, legal actions, costs and stopping rules were precommitted before the player's first move;
- no outcome or rule was changed during play.

Disposition: **retain for comparison; promising on clarity and deduction, but flag routinization/coordinate-isolation risk for post-play evaluation before promoting it as a leading architecture.**


### Post-prototype-10 player preference / hybrid hypothesis

Player evaluation of prototype 10:

- It felt **better than the earlier straightforward enumeration-style prototypes**, even though the player also agreed that the natural strategy risks becoming algorithmic slot-by-slot isolation.
- The clean aggregate rule was a positive: it was easy to understand, locally interpretable, and gave a stronger sense of deduction than simply trying candidates in sequence.
- The current weakness becomes much more serious at realistic Graveyard Keeper candidate counts. With many eligible powders/liquids/essences, a pure “change one slot and watch the score” loop would require too much candidate scanning and would feel like systematic coordinate search.

A promising **hypothesis to revisit after the current blind-prototype round**, not an accepted architecture, is to keep one very simple universal deduction rule (such as whole-mixture match/resonance) and add **one additional information layer grounded in legible in-world substance properties**.

Desired character of that second layer:
- materially reduce the candidate set rather than disclose an exact ingredient;
- feel connected to Graveyard Keeper’s alchemy/material world instead of like an abstract solver UI;
- preferably use properties that are intuitive from real-world expectations, vanilla presentation, or consistently taught in-game semantics;
- examples of the desired *kind* of clue include visible color/family, ordered/symmetric behavior suggesting an “order”-like property, thermal/solubility/reaction behavior, smell/appearance, or another physically legible observation;
- avoid arbitrary authored flavor text whose mechanical meaning exists only because the mod says so;
- avoid turning the extra layer into a second hidden recipe book or a fixed one-click discriminator.

The appeal is a two-layer structure:
1. a simple global rule that supports clean deduction;
2. a world-grounded clue that narrows which candidates are worth testing.

Do not pivot the active research plan around this yet. Finish the remaining orthogonal blind prototypes first, then compare whether this hybrid deserves a dedicated prototype against the survivors.


### Prototype 11 — active blind test

Status: **active**. Hidden formula, known-reference library, deterministic comparison outcomes, costs and stopping rules were precommitted before the player's first action in `docs/prototypes/PROTOTYPE_11_STATE.md`.

Purpose: test whether reasoning from already-known recipes feels more naturally alchemical and less like slot-by-slot probing than freely constructed aggregate tests.


### Prototype 11 — result

Status: **completed blind prototype**.

Player-facing sequence:
1. Free opening comparison: target vs Clear Solution (White Ash + Dew + Echo) -> 1/3.
2. Player chose Dry Fixative (White Ash + Brine + Spark) -> 2/3.
   - Deduction: White Ash is confirmed; exactly one of Brine / Spark is correct.
3. Player chose Chalk Tincture (Black Chalk + Dew + Spark) -> 0/3.
   - Because Black Chalk and Dew were already excluded, Spark is excluded.
   - Therefore Brine is confirmed.
4. Player chose Dark Extract (Crystal Dust + Spirit + Shadow) -> 1/3.
   - Crystal Dust and Spirit are already excluded, so Shadow is confirmed.
   - Unique target formula is therefore White Ash + Brine + Shadow.

Meaningful paid comparisons: **3**.

Player-experience findings:
- The comparison concept itself felt appealing / "прикольная система": reasoning from already-known recipes felt more naturally alchemical than arbitrary free-form probing.
- Keeping the full formulas of known reference products visible is necessary UI state; names alone are insufficient because the player must reason from their ingredient overlap.
- The specific prototype path was too straightforward. After the opening clue, every remaining reference recipe was useful and the player essentially progressed through the available comparison set. There was little real experimental-selection pressure beyond ordering.
- In particular, the player did not face a meaningful choice among a richer set containing weak, redundant, dominated or differently informative references. The scenario therefore demonstrated the deduction grammar but did **not** prove that selecting the next comparison can itself be an interesting decision.
- The final Dark Extract comparison became a binary check of Shadow because the other two ingredients were already excluded. This cleanly completes the deduction but is effectively a forced final step.

Blind-test integrity:
- hidden target, reference library, comparison outcomes, costs and stopping rules were precommitted before play;
- no rule or result was adapted after player choices.

Disposition: **retain as promising for world fit and clarity, but prototype 11 is insufficient evidence for experiment-choice quality.** A stronger future version would need a richer reference library where several comparisons are legal but differ meaningfully in expected information, without requiring the player to compute a large optimization problem.


### Prototype 12 — active blind test

Status: **active**. Hidden formula, target clue, goo-family system, deterministic target-bound failure outcomes, costs and stopping rules were precommitted before the player's first action in `docs/prototypes/PROTOTYPE_12_STATE.md`.

Purpose: test whether a minimal target-specific anchor can make vanilla-style goo evidence into a useful target-directed puzzle without turning it into an answer oracle.


### Prototype 12 — result

Status: **completed blind prototype**, with one facilitator-contamination caveat.

Player-facing sequence:
1. Initial target research stated that the three recipe ingredients belong to three different goo families and exactly one family is Death.
2. The player initially tried to design a clean experiment to locate Death, found the interaction cognitively awkward, and deliberately chose a mixed probe instead:
   - Bone Powder + Pure Water + Order Essence.
   - Result: failed synthesis with target trace {Order, Life}.
3. From that observation, the player independently reconstructed:
   - the trace implies one attempted non-Order/non-Life reagent was the positional anchor;
   - therefore Bone Powder is the correct powder;
   - the remaining liquid/essence families are Order and Life in unknown assignment;
   - only two formulas remain: Bone Powder + Pure Water + Life Essence, or Bone Powder + Plant Juice + Order Essence.
4. The player chose the first remaining formula:
   - Bone Powder + Pure Water + Life Essence.
   - Result: **successful synthesis**.

Meaningful ordinary alchemy attempts: **2**.

Player-experience findings:
- The first experimental-choice problem felt cognitively muddy. The player spent noticeable effort trying to construct a clean diagnostic and then gave up on a principled test, choosing a mixed probe partly to see what would happen.
- The first informative trace did support a real multi-step deduction. The player had to reason through what the unordered goo pair implied, nearly reintroduced Chaos by mistake, corrected the reasoning, and reached the two remaining formulas.
- This is evidence of genuine reasoning effort, but the subjective quality was not clearly satisfying: the player described the mechanic/prototype/game as “мутненькая” and “not quite right / not ideal.”
- Target-bound goo therefore improves target relevance relative to vanilla failure goo, but the current rule imposes a comparatively opaque interpretation burden and does not naturally suggest a good first experiment.
- Once the first trace is interpreted, the endgame collapses to choosing between two formulas and synthesizing one; this part is straightforward.
- The mechanism reuses the vanilla-style goo vocabulary in a meaningful way, but the added target-binding semantics are sufficiently non-obvious that they risk feeling like bespoke puzzle logic rather than intuitive alchemy.

Facilitator/test-method caveat:
- After the first target trace, the facilitator prematurely supplied the full logical consequence before the player had independently worked it out.
- The player explicitly identified this as invalidating part of the blind cognitive test, then intentionally ignored that explanation and reconstructed the reasoning independently.
- Future blind prototypes must present **observations and previously established facts only**. New deductions must remain player work until the player states them; the facilitator may then verify/correct them. This applies even when prior prototypes had simpler deductions where the contamination was less noticeable.

Disposition: **do not promote Prototype 12 as-is.** Retain the useful concept that vanilla-like semantic families can carry target-relevant evidence, but treat the current target-bound-goo rule as too opaque / cognitively muddy for a leading architecture without substantial simplification.
