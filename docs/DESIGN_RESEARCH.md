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


## Post-prototype synthesis — prototypes 1–12 and external puzzle-design comparison

Status: **working synthesis / next-research hypothesis, not selected production architecture**.

### What the 12 prototypes now establish

The failed and surviving prototypes separate four distinct design jobs that should not be forced into one mechanic:

1. **Candidate-domain reduction** — turn the real alchemy inventory into a small enough set that choosing an experiment is tractable.
2. **Experimental discrimination** — let the player test a hypothesis in a way whose result supports a local, understandable inference.
3. **World grounding** — make clues feel like observations about Graveyard Keeper substances and known alchemy, rather than queries against an abstract hidden database.
4. **External memory** — preserve observations, established facts and live hypotheses without performing the deduction for the player.

The strongest evidence from the prototypes:
- Prototype 4 showed that stable ingredient properties can create genuine reasoning, but a multi-rule algebra exceeds the intended working-memory envelope.
- Prototype 7 produced the strongest “I am investigating” feeling through concrete assays and observable reactions, but its fixed assay-to-slot mapping would routinize later recipes.
- Prototype 10 showed that a single aggregate whole-mixture rule is unusually clear and naturally induces controlled-variable experiments. Its failure is scale: with realistic candidate counts it becomes coordinate search.
- Prototype 11 showed that comparison to already-known recipes feels more naturally alchemical and makes prior knowledge useful, but the tested reference set created an almost forced linear sequence rather than meaningful experiment selection.
- Prototype 12 showed that target-binding can rescue relevance of vanilla-style goo, but an opaque anchor/trace interpretation rule adds the wrong kind of cognitive burden.
- Prototypes 1/3/5/6 reinforce that cheap information, binary discrimination, or directed improvement are not enough when the player's rational action is still “query candidates until the answer appears.”

### Working design convergence: two-layer deduction

The most promising general structure after prototypes 1–12 is:

**Layer A — world-grounded coarse evidence**
- use a small, taught vocabulary of substance properties / observable behavior;
- clues should reduce the candidate domain materially but should not identify an exact ingredient in an exact slot;
- properties should preferably come from vanilla presentation, real-world intuition, existing semantic families, Study/decomposition knowledge, or a consistently taught assay vocabulary;
- target observations may be authored/selected per output because the real corpus is bounded.

**Layer B — one simple universal discrimination rule**
- after the property layer has reduced the search space, use a very low-complexity experimental rule such as whole-mixture aggregate matching or carefully chosen reference-recipe comparison;
- controlled changes should allow strong local conclusions;
- the player, not the journal, performs the new deduction;
- final synthesis is used when it still tests a justified hypothesis, and may be skipped when logical exhaustion has already made the formula unique.

This structure directly addresses the main weakness of Prototype 10: the simple rule is retained, but it is no longer responsible for searching a large raw ingredient space.

### Property-layer constraints from the real 1.407 corpus

The native goo taxonomy is a useful source vocabulary but cannot simply be exposed positionally:
- eight semantic classes span Powder / Fluid / Essence forms;
- within a normal positional slot, goo identity is effectively one-to-one among ingredients participating in ordinary success formulas;
- therefore a clue equivalent to “slot 2 has goo class G” is too close to directly naming the ingredient.

Promising property clues must therefore be **coarser, cross-slot, aggregate, relational, or compound-level**. Examples of the design shape (not accepted literal rules):
- the target contains exactly one ingredient from a semantic family, without saying which slot;
- the target exhibits a visible/thermal/dilution behavior shared by several reagents;
- two ingredients share/opppose a broad property;
- a known recipe is relevant because it shares an observable property pattern, not because the system directly reveals a matching slot.

### External-design principles that fit the evidence

Relevant transferable patterns:
- Mastermind / control-of-variables reasoning: controlled one-factor changes produce strong attributable conclusions; this explains why Prototype 10 felt better than sequential candidate probing.
- Zendo: prediction and counterexample construction can be satisfying, but rule authors systematically underestimate difficulty; use fewer/easier rules than initially seems necessary.
- Alchemists: stable hidden properties plus experiments and a deduction record can create genuine scientific reasoning, but its full formal grid is much too heavy for the intended Graveyard Keeper micro-puzzle.
- The Case of the Golden Idol: bounded vocabularies and deliberately limited relevant information can support player-owned deduction while reducing brute-force validation; playtesting must tune the path between triviality and confusion.
- Strange Horticulture: world-grounded identification can vary which observable feature matters (shape, description, smell/feel) while keeping the task intuitive; this is a particularly close reference for a possible Graveyard Keeper property layer.
- Outer Wilds: player discoveries naturally require an external knowledge record; its prototype testing directly motivated an in-game computer because testers began taking their own notes.
- The Search for Planet X: research actions can have explicit scopes and results that combine with persistent notes, but its hour-scale formal deduction is a complexity ceiling rather than a pacing model for this project.
- Baba Is You / The Witness: a small stable rule language can support deep reasoning, but too many simultaneously active rules or too much supporting setup quickly becomes overwhelming; AlchemyRiddle should favor one reusable discrimination rule plus target-specific evidence rather than stacking several abstract laws.

### Next research checkpoint

Before another fictional hybrid prototype, test whether a useful **Graveyard-Keeper-native property vocabulary actually exists**.

For the 35 ordinary success-corpus ingredient definitions, inspect non-spoiler metadata that a player could plausibly know or be taught:
- native semantic/goo family;
- Powder/Fluid/Essence/Universal form;
- Study/decomposition relationships;
- ingredient/source/material family;
- existing names/descriptions and visible presentation where legally/reliably inspectable;
- any other already-verified vanilla attributes with clear player-facing meaning.

Then propose a very small property vocabulary and quantify, without exposing formulas:
- distribution of each property across slots;
- candidate-set reduction from target-level aggregate clues;
- ambiguity / collision rates;
- whether all 34 ordinary outputs can receive at least one useful non-oracular starting clue;
- how many targets would need authored exceptions.

Only if that screen is promising should the next blind round test:
1. **property-gated aggregate resonance** (Prototype 10 core + world-grounded candidate reduction);
2. **property-guided known-recipe differential** (Prototype 11 core + world-grounded selection of useful references).

Production mutation remains **BLOCKED**.


## Native-property vocabulary research method checkpoint

Status: **accepted next research step; research/probe only, production remains BLOCKED**.

### Core research question

Determine whether existing Graveyard Keeper 1.407 information can support, for each unknown alchemy target, one or two player-legible **world-grounded starting constraints** that:
- materially shrink the plausible ingredient/formula domain;
- do not identify an exact ingredient in an exact slot;
- can reasonably be known or learned at the target's progression point;
- help the player choose a meaningful next experiment;
- fit the short micro-deduction / low-working-memory product target.

The goal is not to inventory all game metadata. Collect only information that could plausibly become:
1. a candidate-grouping property;
2. a target-side clue;
3. an experiment-selection reason;
4. a progression/completeness constraint;
5. a resource-cost constraint.

### Evidence classes to distinguish

Every potential clue/property must be classified by how the player could know it:

1. **Native-visible** — already shown directly by vanilla UI/presentation at the relevant state.
2. **Native-derived / player-learned** — not one tooltip field, but naturally inferable from normal play (source/provenance, decomposition relation, previously observed reaction, known recipe).
3. **Mod-taught but world-grounded** — the mod introduces a consistent label/assay vocabulary derived from stable vanilla substance relationships.
4. **Pure authored puzzle semantics** — mechanically invented per-target meaning with weak grounding. Keep as last resort and do not let it silently become the main property layer.

System-only metadata that the player could not plausibly know is research input, not automatically a valid clue.

### Data domains to inspect

#### A. Ingredient presentation / identity
For the 35 ordinary success-corpus ingredients:
- localized display name and ordinary tooltip content;
- item icon / visible color / silhouette / material presentation where reliably inspectable;
- Powder / Fluid / Essence / Universal form;
- standard crafting-location presentation and other player-visible item metadata;
- Study-complete versus unstudied presentation differences.

Purpose: find characteristics that are legible without requiring the player to memorize internal IDs or hidden taxonomies.

#### B. Native alchemical relations
- goo/semantic family;
- Study-gated decomposition information;
- decomposition source/result relationships;
- native per-tier alchemy/slot metadata;
- relationships between different forms that arise from the same underlying semantic material.

Purpose: identify a small reusable vocabulary that is genuinely connected to vanilla alchemy.

Constraint already known: positional goo-class disclosure is effectively oracular in the ordinary success corpus, so useful clues must be coarser/cross-slot/aggregate/relational.

#### C. Acquisition and provenance
For each relevant ingredient:
- whether it is crafted, decomposed, gathered/dropped, bought, quest/granted, or obtainable through another native path;
- immediate source material(s) and processing station;
- relevant object/location/station family;
- technology/unlock dependency where established;
- whether several reagents form an intuitively recognizable provenance group.

Purpose: test clues such as plant/mineral/corpse-derived or “obtained through the same material chain” only when those distinctions are actually supported and player-legible.

Do not equate an internal source relation with player knowledge automatically.

#### D. Progression / candidate completeness
At the point a target becomes a legitimate research topic:
- which alchemical ingredients can plausibly already be known/possessed/studied;
- which relevant ingredient forms are still undiscovered or progression-inaccessible;
- whether the UI can truthfully present a closed candidate set;
- whether “insufficient reagent knowledge” must be an explicit state.

Purpose: avoid puzzles whose logical closure depends on ingredients the player does not yet know exist.

#### E. Acquisition burden / experiment economics
Classify relevant reagents coarsely by replacement burden:
- trivial/common;
- processed but readily reproducible;
- time/schedule/growth gated;
- scarce/expensive/otherwise disruptive.

Purpose: an intellectually valid experiment can still be bad gameplay if it burns disproportionately costly materials for little information. Do not infer exact subjective cost from sell price alone.

#### F. Target-side evidence
For each of the 34 ordinary target outputs:
- how/where the player can first have a reason to know the target exists;
- what is visible at that point: name, icon, downstream use, technology context, vendor sample, dialogue/context, etc.;
- whether a **physical sample of the target actually exists** before the formula is known;
- if not, what legitimate object supplies the observation: downstream use, trace/sample supplied by progression, comparison target, known reference, or an explicitly mod-created research abstraction.

Purpose: prevent designs that assume the player can smell, heat, inspect or color-read a product they do not possess.

Accepted exposure audit already proves only channel existence for much of the corpus, not chronological first exposure, and leaves unresolved cases. Reuse that evidence before creating new probes.

#### G. Known-recipe / knowledge network
At plausible target-entry states:
- what already-known formulas or known alchemical materials can serve as references;
- whether several references differ meaningfully in expected discriminatory value;
- whether prior knowledge can make the next experiment more informed rather than simply add more buttons.

Purpose: evaluate the Prototype-11 hybrid without assuming an unrealistically convenient known-recipe library.

### Property-quality screen

A candidate property/clue is promising only if it scores well on all of these dimensions:

- **legibility** — player can understand what the property means without decoding hidden implementation semantics;
- **grounding** — the property feels like a fact about the substance/world, not a database query;
- **availability** — the player can legitimately know it at the relevant progression point;
- **reduction power** — it removes a meaningful amount of uncertainty;
- **non-oracularity** — it does not collapse to one exact ingredient/slot by itself;
- **consistency** — the same vocabulary behaves coherently across targets;
- **experimental usefulness** — it suggests or differentiates reasonable next tests;
- **memory fit** — it can be represented compactly in the journal;
- **coverage** — enough of the 34-output corpus can use it without many arbitrary exceptions.

No fixed numeric threshold is accepted yet. Measure the distributions first.

### Research output

The desired research artifact is not a recipe dump. It is a bounded hidden feature model plus aggregate results:

- ingredient-property matrix for the 35 ordinary success ingredients;
- target-entry/evidence matrix for the 34 ordinary outputs;
- provenance/progression/cost classifications where evidence supports them;
- candidate-set partition sizes for each plausible property;
- collision and over-specificity rates;
- coverage of one-property and two-property starting clues;
- count of targets needing authored exceptions;
- representative anonymized examples of strong/weak clue shapes.

Exact formulas remain hidden in user-facing reporting.

### Research sequence / anti-probe rule

1. First inspect static schema/control flow and existing accepted research to identify the real owners of candidate metadata.
2. Reuse the existing Corpus Probe and accepted exposure evidence where possible.
3. Only then define the exact residual unknowns that require loaded balance/runtime data.
4. If a new probe is required, prefer **one bounded read-only extension** that captures the needed ingredient/target feature matrix rather than several exploratory probes.
5. Visual/perceptual claims that cannot be established reliably from metadata should be evaluated separately from structural data; do not pretend an asset field proves what a player visually perceives.

Likely next candidate research families after this screen:
- property-gated aggregate resonance;
- property-guided known-recipe differential;
- target-specific observable assay vocabulary if native properties support it.


## Native-property static owner audit — 2026-10-04

Status: **static owner map closed; one bounded loaded-balance capture is justified next**.

Pinned host reference: `Kupie/GYK_DECOMP@6abf79199d92482af1c7573870dd9a20ec2270b9`.

Shared reusable corrections/facts were promoted to `NikichMods/GraveyardKeeperResearch/docs/ALCHEMY_SYSTEM.md` at shared commit `324ee9b2b91988a02d648a4bdcc9bc38ec2dd0fe`.

### What static inspection can already prove

#### Player-facing identity / presentation
- Item name: `ItemDefinition.GetItemName(true)` -> localized item ID.
- Base description: `GetItemDescription(...)` -> localized `<item_id>_d`, with base-ID fallback for quality-suffixed variants.
- Standard tooltip: name + description are always the first rows; Study/crafting-location rows may follow.
- Icon owner: `ItemDefinition.GetIcon()` -> explicit `icon` or default `i_<item_id>`; standard item cells resolve it through `EasySpritesCollection`.
- Crafting-location tooltip: `GameBalance.GetItemCraftsIn`, built from non-hidden, non-`dont_show_in_hint` output-producing crafts and localized `craft_in` objects.

Implication: names, descriptions, icon keys and vanilla crafting-station exposure are valid structural inputs. Icon **appearance** remains a perceptual question; an icon key alone is not evidence of color/shape semantics.

#### Study / decomposition
- `GetSurveyCraft()` resolves `surv:<base-id>` / `surv:<id>`.
- `GameSave.IsSurveyComplete` is backed by `completed_one_time_crafts`.
- `BaseCraftGUI.CommonOpen(... AlchemyDecompose)` shows an authored decomposition craft only after Study of its input source.
- `ItemDefinition.GetItemDetails()` builds alchemy details only for source items whose own `alch_type == None`, then derives `decomposes` from authored `AlchemyDecompose` crafts.
- For an item already typed Powder / Fluid / Essence / Universal, `GetItemDetails()` returns before constructing an alchemy-details block.
- Although `BubbleWidgetAlchemyItem` contains a `DetailsType.Slots` renderer, the pinned 1.407 decompile contains no writer for `DetailsType.Slots` or `ItemDetailsAlchemy.slots`.

Implication: the verified native knowledge relation is **studied source material -> available decomposition type(s)**. Do not design around a presumed populated per-tier slot-compatibility table.

#### Semantic/goo family
- `GetGooFromAlchemyIngridient` normalizes quality suffixes and known alchemy/decomposition prefixes, then maps the remaining semantic identity to `goo_<identity>`.
- Existing runtime evidence already proves 19 goo identities among 35 ordinary success ingredients, including eight cross-form Powder/Fluid/Essence families.

Implication: the semantic family is structurally tied to material identity rather than being a decorative result label. It remains too specific when revealed together with a fixed slot.

#### Provenance / acquisition graph
There is no single authoritative `source` field. Relevant owners are:
- ordinary / decomposition producers: `GameBalance.craft_data -> CraftDefinition.output / needs / craft_in / craft_type`;
- direct world-object drops: `GameBalance.objs_data -> ObjectDefinition.drop_items`;
- vendor eligibility: `ItemDefinition.product_types / product_tier / base_count` plus `VendorDefinition` product types and modifiers;
- technology unlock ownership: `TechDefinition.crafts`, plus `hidden / invisible`;
- scripted/quest grants and exact world placement are separate channels and cannot be inferred completely from those balance tables.

`CraftDefinition` also owns `craft_time`, `energy`, `hidden`, `needs_unlock` and `dont_show_in_hint`, which are useful inputs for a coarse replacement-burden model.

Implication: provenance should be modeled as a graph of production/acquisition relationships. A station ID, internal product tag or object `zone_id` must not automatically be promoted to a player-facing provenance label.

#### Candidate completeness / progression
- actual craft visibility is save-dependent through `GameSave.IsCraftVisible`;
- Study completion is save-dependent;
- `unlocked_crafts`, `unlocked_techs`, `completed_one_time_crafts` and other progression state are persistent owners;
- one arbitrary runtime save cannot prove a universal progression order.

Implication: the next property capture should characterize the **authored global vocabulary**, not pretend to solve chronological candidate completeness. Exact target-entry progression remains a later graph/flow question, reusing the accepted 0.2.0 exposure audit.

### Static dead ends / downgraded candidates

- `product_types` is primarily a vendor/filter taxonomy. It may help discover clusters, but is not itself a demonstrated player-legible material property.
- `ItemDetailsAlchemy.slots` is not currently a verified populated metadata source.
- `ObjectDefinition.zone_id` / object IDs are not sufficient evidence of the location a player associates with an ingredient.
- `base_price` alone is not a valid replacement-cost metric; acquisition processing, growth/schedule gating and context switching matter.
- icon IDs do not prove visual color/shape semantics.

### Exact residual loaded-balance question

For the **35 ordinary success-corpus ingredients**, capture enough non-formula metadata to answer:

1. What does the player-facing item identity look like in the loaded game?
   - localized name;
   - localized base description;
   - icon key;
   - alchemy form.
2. What native semantic/material relations exist?
   - goo family;
   - authored `AlchemyDecompose` source item(s);
   - Survey craft existence for those source items.
3. What immediate acquisition/provenance relationships exist?
   - non-Mixed producer crafts and their stations;
   - direct object-drop producer definitions;
   - static vendor-stock candidacy;
   - product tier / base price / base count as supporting—not decisive—cost inputs.
4. Which of those relationships are already surfaced by the standard tooltip?
   - `GetItemCraftsIn` station set;
   - description presence.

For the **34 ordinary target outputs**, capture:
- localized name / base description / icon key;
- the already-measured structural/vendor entry counts and representative context categories, without any formula ingredients.

Do **not** log target formulas in this pass.

### Proposed one-pass research probe

A single read-only `AlchemyCorpusProbe 0.3.0` extension is justified because the authored 1.407 balance/localization population is not present in the public decompile or current repository evidence.

The probe should:
- run once after normal game start;
- make no Harmony patches and mutate no save/balance/UI/inventory;
- recompute the ordinary 35-ingredient / 34-output scope internally;
- log a dedicated bounded `AR_PROPERTY_* ` section;
- avoid `AR_RECIPE` formula rows entirely in 0.3.0;
- use a fresh property-symbol namespace not intended to correlate with earlier formula symbols;
- include localized names/descriptions only as transient runtime research input; do not commit bulk game text to the repository;
- log relationships needed for provenance, but not extract or persist image assets;
- leave visual icon interpretation for a later perceptual pass if structural/property screening says it is worth doing.

Expected result after the returned runtime log:
- build the hidden 35-ingredient feature/provenance matrix;
- propose a small player-legible property vocabulary;
- quantify partition/reduction quality against the hidden 34-output corpus without publishing formulas;
- decide whether property-gated resonance / property-guided known-recipe comparison deserve the next blind prototypes.

No production behavior is READY. This is research-only work.


### Property/provenance probe 0.3.0 — runtime candidate

Status: **compiled research candidate; runtime evidence pending**.

Identity:
- research branch: `research/vanilla-alchemy-model`;
- source: `163f07939701cff70b3a90565e125c0107d245a9`;
- GitHub Actions run: `37207458475`, conclusion **success**;
- handoff DLL: `AlchemyCorpusProbe-0.3.0.dll`;
- DLL SHA-256: `981ffda9dce0b223cfcb993d376762d81e4d1e7063b321f3c2e5c500be121af8`;
- CI artifact ZIP SHA-256: `d4db4bd4b3e7d7a47c6ebc88b7accaeb8401ab06f360e288c211081fd9d31d48`.

The probe is research-only and read-only. It emits no `AR_RECIPE` formula rows; it captures bounded `AR_PROPERTY_*` presentation/provenance records for the 35 ordinary success-corpus ingredients plus non-formula target context for the 34 ordinary outputs.

Acceptance evidence still required:
- one installed-runtime launch on Graveyard Keeper 1.407;
- successful `AR_PROPERTY_BEGIN ... AR_PROPERTY_DONE` completion without `AR_PROPERTY_ERROR`;
- returned full BepInEx log for property/provenance analysis.

No production behavior becomes READY from this candidate.


## Native-property runtime screen — 2026-10-04

Status: **accepted property/provenance evidence; property layer is viable enough for a hybrid blind prototype. Production remains BLOCKED.**

### Probe 0.3.0 acceptance

Installed-runtime evidence from Graveyard Keeper 1.407 completed the exact research candidate recorded above:

- \`AR_PROPERTY_BEGIN\` and \`AR_PROPERTY_DONE\` both present;
- \`ordinary_formulas=43\`;
- \`ingredients=35\`;
- \`targets=34\`;
- \`formula_rows_logged=0\`;
- no \`AR_PROPERTY_ERROR\`.

The 0.3.0 runtime candidate is therefore **accepted for its bounded property/provenance question**.

Shared reusable host facts were promoted to \`NikichMods/GraveyardKeeperResearch/docs/ALCHEMY_SYSTEM.md\` at shared commit \`9ec5234322e14ddc72d015dd23268fa82a528d19\`.

#### Loaded-mod contamination control

The runtime contained other mods, so do not promote arbitrary timing/economy values as pristine vanilla merely because the probe saw them.

The fields used for the property screen are nevertheless accepted:

- exact installed Alchemy Research Redux 0.1.8 source state (\`p1xel8ted/Graveyard-Keeper-Mods@85a88e96cd5c3864f772a03d461a9ac4935df310\`) reads mixed-alchemy definitions for preview/recipe memory and changes UI/inventory interaction; it does not rewrite \`craft_data\`, decomposition definitions, item definitions, vendors or drops;
- exact historical Decomp Delight 0.1.9 source (\`p1xel8ted/Graveyard-Keeper-Mods@0e6aa4e67dda0c9eeaef8f0effea72253a327eb5\`) reads \`AlchemyDecompose\` records and appends a tooltip row only;
- Queue Everything did run in the supplied environment, but its runtime diagnostic for this load was \`converted=0 halved=0 fireAdjusted=0\`; the active forced-multicraft mutation does not affect the identity/source/decomposition fields used below.

Therefore ingredient identity, alchemy form, goo family, authored decomposition-source relations, target presentation and the bounded provenance classifications below are accepted. Craft time/energy and unrelated producer-economy details are not used as vanilla balance evidence.

### Native presentation result

The hoped-for ordinary description channel is effectively absent for ingredients:

- **35/35** ordinary success-corpus ingredients have empty base descriptions in the tested Russian localization.
- Only **8/34** ordinary targets have non-empty base descriptions, all in the consumable-elixir/effect family.

Therefore free-text vanilla descriptions do **not** provide a general property language for AlchemyRiddle. No further description-mining pass is justified.

Icon keys remain available structural evidence, but the provenance signal below is already strong enough that a visual-asset/perceptual pass is not the next cheapest research step.

### Provenance vocabulary

The useful native-derived relation is not “this reagent has hidden property X”. It is:

> **this reagent can be obtained from at least one studied/source material of class X**

A reagent may belong to more than one provenance class because vanilla can decompose different source materials into the same reagent. This overlap is intentional and must be taught explicitly if the mechanic uses it.

Candidate world-grounded vocabulary:

- **botanical** — at least one plant/crop/fungus/plant-product source;
- **anatomical** — at least one corpse/anatomy source or direct anatomy-derived producer;
- **mineral** — at least one stone/ore/mineral/gem source;
- **creature** — at least one animal/insect/animal-product source;
- **slime/jelly** — at least one ordinary slime/jelly source (distinct from the universal goo fallback vocabulary);
- **combustion** — obtained through the cremation/pyre channel;
- **universal form** — native \`AlchemyType.Universal\`; this is structural rather than provenance, but the player can learn it from the fact that these reagents fit any normal alchemy slot.

The classification used for the hidden quantitative screen is:

| Ingredient | Form | Coarse properties |
| --- | --- | --- |
| Alcohol | Universal | universal |
| White powder | Powder | anatomical, mineral |
| Water | Universal | universal |
| Gold powder | Powder | mineral |
| Blood | Universal | anatomical, universal |
| Oil | Universal | anatomical, universal |
| Ash | Powder | combustion |
| Graphite powder | Powder | mineral |
| Life powder | Powder | anatomical, mineral |
| Slowing powder | Powder | botanical, mineral, creature |
| Health powder | Powder | botanical |
| Order powder | Powder | mineral, creature |
| Death powder | Powder | anatomical |
| Acceleration powder | Powder | botanical, creature |
| Chaos powder | Powder | creature |
| Life solution | Fluid | botanical, anatomical, creature |
| Slowing solution | Fluid | botanical, anatomical, creature |
| Health solution | Fluid | botanical |
| Order solution | Fluid | botanical, creature, slime/jelly |
| Death solution | Fluid | anatomical, slime/jelly |
| Toxic solution | Fluid | botanical, slime/jelly |
| Acceleration solution | Fluid | creature, slime/jelly |
| Chaos solution | Fluid | creature |
| Silver powder | Powder | mineral |
| Salt | Powder | combustion |
| Toxic powder | Powder | botanical |
| Life extract | Essence | botanical, anatomical, creature |
| Slowing extract | Essence | creature |
| Health extract | Essence | botanical |
| Order extract | Essence | botanical, slime/jelly |
| Death extract | Essence | anatomical, slime/jelly |
| Toxic extract | Essence | botanical, slime/jelly |
| Acceleration extract | Essence | botanical, slime/jelly |
| Chaos extract | Essence | creature |
| Electric powder | Powder | creature |

This table is **not** a recipe table and contains no target formula mapping.

### Property distribution / non-oracularity

Within the 35 ordinary formula-participating ingredients, the normal slot-compatible pools are:

- slot 1: 19 candidates (15 Powder + 4 Universal);
- slot 2: 12 candidates (8 Fluid + 4 Universal);
- slot 3: 12 candidates (8 Essence + 4 Universal).

Positive coarse-property group sizes:

| Property | Slot 1 | Slot 2 | Slot 3 |
| --- | ---: | ---: | ---: |
| botanical | 4 | 5 | 5 |
| anatomical | 5 | 5 | 4 |
| mineral | 7 | 0 | 0 |
| creature | 5 | 5 | 3 |
| slime/jelly | 0 | 4 | 4 |
| combustion | 2 | 0 | 0 |
| universal form | 4 | 4 | 4 |

A **single** such property is therefore generally useful but not an exact-name oracle. The strongest ordinary slot split in this vocabulary still leaves multiple candidates.

However, exposing the **complete property vector** for every reagent would overfit:
- slot 1 produces 11 distinct signatures among 19 candidates, including 4 singleton signatures;
- slot 2 produces 9 signatures among 12 candidates, including 6 singletons;
- slot 3 produces 7 signatures among 12 candidates, including 3 singletons.

Therefore the accepted design constraint is:

**use one or two properties as observations/constraints; do not expose a complete static “property dossier” as the puzzle solution layer.**

### Target-level aggregate clue screen

The old accepted anonymized 0.2 formula corpus was cross-walked internally to the 0.3 property identities using stable alchemy form / goo-family structure and then validated against the normal picker contract for all 43 ordinary formulas. Exact formulas remain unpersisted/unpublished here; only aggregate results follow.

For outputs with alternative valid formulas, a target-level property count is usable only when that count is identical for **every valid formula for that output**. Invariance across all 34 outputs:

- botanical count invariant: **29/34**;
- anatomical: **28/34**;
- mineral: **30/34**;
- creature: **30/34**;
- slime/jelly: **33/34**;
- combustion: **33/34**;
- Universal-ingredient count: **34/34**.

Every one of the 34 outputs has at least **three** invariant properties in this seven-property vocabulary.

Using only the six world-origin properties (excluding Universal form), **32/34** outputs have at least one invariant **positive** property count. The remaining two multi-formula outputs can still receive a non-oracular aggregate constraint through Universal count or an invariant zero-count origin constraint.

Thus the real corpus needs **no authored exception merely to obtain one consistent coarse starting constraint**.

### Aggregate reduction power

For a bounded structural screen, use only the 35 ordinary formula-participating ingredients. This is deliberately **not** claimed to be the player's progression-specific search space.

Picker-compatible distinct-item envelopes inside that scope:
- two-slot: **224** candidate mixtures;
- three-slot: **2,572** candidate mixtures.

For each target, select its strongest invariant single aggregate property-count clue:
- two-slot residual: min **23**, median **84**, max **103**;
- three-slot residual: min **75**, median **540**, max **960**.

For the strongest pair of invariant property-count clues:
- two-slot residual: min **10**, median **28**, max **76**;
- three-slot residual: min **16**, median **158**, max **448**.

Interpretation:
- the property layer can remove a large amount of uncertainty without naming the answer;
- it is **not sufficient by itself**, especially for three-slot formulas;
- this is exactly the desired role for Layer A: reduce the domain before a simpler experimental discriminator;
- even two strongest clues remain non-oracular in this bounded corpus.

Important limit: these numbers are optimistic with respect to a real player because the native picker has additional eligible ingredients that never participate in an ordinary success formula, and progression-specific availability is still unresolved. Do not present 224 / 2,572 as the player's actual candidate counts or silently discard eligible decoys in production.

### Exact identity of the earlier exposure gap

Combining the accepted 0.2 exposure signatures with the 0.3 target presentation resolves the former anonymous 8-target gap.

The **seven blueprint-only unresolved targets** are:
- Yellow paint;
- Green paint;
- Brown paint;
- Red paint;
- Dark-green paint;
- Dark-violet paint;
- Violet paint.

The single target with **no counted downstream ordinary consumer, blueprint consumer, Technology/default-visible entry or static vendor sample candidate** is:
- **Spices**.

This changes the target-entry research problem from “8 unknown targets” to:
- one repeated **paint-family visibility/progression** problem covering seven targets;
- one genuine **Spices orphan** requiring a separate legitimate discovery trigger or an explicit product decision.

Do not treat the seven paints as seven independent mechanism problems unless later progression evidence proves they differ materially.

### Property-screen disposition

The native-derived provenance vocabulary **passes the viability screen**:

- it is materially grounded in real GK source/decomposition relationships;
- single properties create useful multi-candidate groups;
- complete signatures are too revealing and are rejected;
- every ordinary output can receive at least one invariant coarse aggregate constraint without choosing a privileged formula;
- one/two such clues materially reduce, but do not solve, the real formula space;
- the remaining uncertainty is large enough that a second deduction layer is still necessary.

Main conceptual weakness to test next:
- provenance is a statement about **how a reagent can be obtained**, not an intrinsic physical property of the final reagent;
- a clue such as “two components can be obtained from plant material” is world-grounded but may still feel like a database constraint unless its presentation/research fiction is convincing;
- the next prototype must therefore test both deduction value and whether this provenance language feels naturally alchemical.

No additional runtime probe is justified before that UX test.

### Solution-space checkpoint after property screen

Two previously retained hybrids remain useful:

1. **property-gated aggregate resonance** — combine the successful clarity/control-of-variables grammar of Prototype 10 with the now-verified coarse provenance layer;
2. **property-guided known-recipe differential** — combine Prototype 11's stronger alchemical/world fit with provenance-based reference selection.

Select **property-gated aggregate resonance first** for the next blind test because:
- its universal discrimination rule is already proven clear;
- the property screen directly addresses its known scale failure;
- it requires no assumption about what reference recipes are already known at a target's progression point;
- it therefore tests the new property layer with fewer moving parts.

Known-recipe differential remains the next comparison candidate if the property layer itself survives.

Production mutation remains **BLOCKED**.


## Native-property vocabulary screen — accepted 0.3.0 results

Status: **property layer is promising enough for the next paper-prototype round; architecture still unselected**.

This screen joins the hidden ordinary-formula corpus with Probe 0.3.0 presentation/provenance evidence without publishing exact vanilla formulas.

### What vanilla gives us, and what it does not

**Weak / insufficient by itself**
- Base ingredient descriptions: empty for all 35 ordinary success ingredients.
- Base target descriptions: populated for only 8/34 targets.
- Crafting station: useful as presentation/provenance evidence, but for the regular alchemical forms it mostly tracks Powder / Fluid / Essence production and does not create a rich independent semantic partition.
- Price/vendor metadata: supporting economy evidence only, not a substance property.
- Icon keys: potential pointer for a later perceptual pass, not proof of visible color/shape semantics.

**Strong**
- Native semantic families are explicitly reflected in the regular reagent names and goo identities.
- Authored decomposition/producer relations connect reagents to concrete world materials: plants/crops, creatures/insects and their products, anatomical remains, minerals, jellies/slimes and special production paths.

### Candidate broad provenance vocabulary

For design screening only, immediate non-goo source relations were grouped into four deliberately coarse, player-legible candidate properties:

- **botanical / growing material**;
- **creature / insect-derived**;
- **anatomical / remains-derived**;
- **mineral / inorganic source**.

An ingredient may have more than one property because vanilla can provide several production routes.

These are **not claimed to be native fields**. They are candidate mod-taught labels derived from actual authored source relationships. Their wording and category boundaries remain open to playtest.

### Non-oracularity warning for native semantic families

The complete unordered multiset of native goo/semantic families is too informative.

Across the 43 ordinary formulas:
- **37 / 43** formulas have a semantic-family multiset that no other ordinary formula shares;
- the remaining six formulas fall into three collisions of size two;
- maximum ambiguity after revealing the complete family multiset is therefore only **2 formulas**.

Conclusion: exposing the whole target family signature would behave too much like a hidden recipe book. Family evidence must be partial/coarse.

A single “exactly one component belongs to family X” fact is much safer. Inside the 35-participant structural universe it leaves:
- **29** legal two-slot mixtures from 224;
- **505** legal three-slot mixtures from 2,572.

Two distinct exact-family-presence facts leave 2 two-slot assignments or 74 three-slot assignments; this is already very strong evidence and should not be stacked casually.

### Broad provenance clue power

Using only the four broad provenance properties above, and requiring a target-side clue to remain true for **every valid formula of that output**:

- **31 / 34** ordinary outputs have at least one positive slot-level provenance fact that is invariant across their entire valid-answer set;
- choosing the strongest such fact narrows the affected slot to **3–6 candidate ingredients**, median **4**, inside the 35-participant structural universe;
- every single-formula target is covered;
- most alternate-formula targets are also covered.

Adding one cautious native semantic-family invariant (“exactly one component is family X”) raises simple positive-property coverage to **32 / 34** outputs.

The only two outputs not covered by this minimal invariant vocabulary are the two outputs with **three alternative formulas**. Probe 0.3.0 identifies the only three-formula ordinary targets as **White Paint** and **Black Paint**. Treat these as an explicit exception class rather than weakening the common rule system around them.

### Full-mixture candidate-space screen

This is intentionally **not** a progression-specific search-space claim. It uses only the 35 success-participating ingredients as a common structural comparison universe.

Legal positional mixtures over those 35 participants:
- two-slot: **224**;
- three-slot: **2,572**.

For the 32 outputs covered by the minimal provenance/semantic vocabulary, allowing the best **up to two** invariant positive clues from:
- one broad provenance property tied to a slot; and/or
- one exact native-family presence count of 1;

gives:
- covered two-slot outputs: **16 / 18**, median **14** surviving mixtures, range **2–29**;
- covered three-slot outputs: **16 / 16**, median **74** surviving mixtures, range **74–480**.

Interpretation:
- for two-slot alchemy, a small property layer can plausibly put aggregate resonance into the intended short-deduction regime;
- for three-slot alchemy, two simple starting facts are usually helpful but not sufficient by themselves to guarantee a very short aggregate-score solve.

Information-theory sanity check:
- a two-slot exact-match score has three outcomes (0/1/2), so 14 candidates require at least 3 observations in the worst case;
- a three-slot score has four outcomes (0/1/2/3), so 74 candidates require at least 4 observations in the worst case.

This is a lower bound, not a predicted player path. Actual progression may shrink the candidate set, while the globally eligible inventory may enlarge it.

### Design consequence

The property hypothesis survives the real-corpus screen.

The emerging architecture shape is stronger than “add more hints”:

1. **world-grounded property evidence** reduces one or more ingredient domains to a tractable set;
2. **one simple experimental grammar** then supports controlled-variable deduction;
3. the journal preserves evidence but does not infer the answer.

The screen specifically strengthens **property-gated aggregate resonance** as the next blind prototype family.

It does **not** yet prove property-guided known-recipe differential, because that design additionally depends on which reference formulas the player plausibly knows at each target's entry point. Keep that family live, but defer its next prototype until reference/progression availability is characterized or a bounded fictional test is clearly useful.

### Next blind-prototype requirement

Prototype 13 should no longer use a toy 3x3x3 candidate table.

Use a realistically uneven candidate structure informed by this screen:
- a larger raw slot pool;
- one or two world-grounded starting observations that create groups on the order of 3–6 candidates rather than naming a reagent;
- one simple universal experiment rule;
- no facilitator deductions;
- at least one plausible but non-dominant experiment choice;
- explicit ingredient cost/replenishment;
- valid-answer-set semantics precommitted.

The purpose is to test whether the two-layer structure actually feels like **“I understood the substance, designed an experiment, and worked it out”** rather than merely reducing a search tree.


### Information-support consequence — accepted before Prototype 13

The player must **not** be expected to remember where every alchemical reagent came from or reconstruct provenance/semantic classifications from long-term memory.

If a puzzle clue relies on a property such as provenance, semantic family, preparation method or another taught classification, the mod must make the relevant known information directly inspectable at puzzle time.

Working product requirement:
- the journal/research UI should include a compact **substance reference / compendium** for already-known alchemical reagents;
- for each known reagent, expose only information the player has legitimately learned or the mod consistently teaches (for example broad provenance, semantic family, preparation relation, and later any accepted assay properties);
- the clue UI should support filtering or visually grouping candidates by those properties so the challenge is **deduction**, not remembering inventory trivia or consulting a wiki;
- expanded item tooltips may duplicate the same facts contextually, but tooltip enrichment alone is insufficient because the player also needs a consolidated cross-reagent view;
- the reference surface is external memory, not an auto-solver: it may show facts and matching known substances, but must not infer the target formula or mark newly deduced recipe constraints before the player establishes them.

This strengthens rather than weakens the property-layer direction: provenance can be used as a puzzle language only if the information system makes that language inspectable and self-contained.


### Prototype 13 — active blind test

Status: **active**. Hidden formula, player-visible compendium, residue observations, aggregate-resonance rule, resource model and deterministic outcomes were precommitted before the player's first action in \`docs/prototypes/PROTOTYPE_13_STATE.md\`.

Purpose: test the leading two-layer hypothesis on a larger, uneven candidate surface: inspectable world-grounded property evidence first, then one simple whole-mixture exact-match score. The substance compendium is explicitly external memory and may match visible properties, but must not perform new recipe deductions for the player.


### Prototype 13 — observed completion

Status: **completed blind play; explicit subjective evaluation still pending**.

Play sequence:
- all-Death reference -> 0/3;
- White Powder substitution -> 0/3;
- Graphite Powder substitution -> 1/3;
- Life Extract substitution -> 2/3;
- Order Solution substitution -> exact success.

Observed findings:
- The two-layer structure successfully gave the player a clear first research goal from the property layer.
- The player independently invented a null-reference/control experiment and then used one-variable substitutions, strongly supporting the value of controlled-variable reasoning seen in Prototype 10.
- The inspectable substance reference avoided any need to remember provenance/family facts from prior gameplay.
- After the powder and Life position were resolved, the remaining liquid slot became straightforward sequential candidate search; the player identified this explicitly before the final test.
- The player also raised reagent-burn cost as a likely gameplay problem because every logical test consumes a full three-component mixture and always includes an essence.

Do not yet promote Prototype 13 to a selected architecture. Record the player's explicit evaluation before assigning retain/revise/reject disposition.


### Prototype 13 — final evaluation

Player rating: approximately **2 / 5**.

Disposition: **REVISE; retain components, reject the tested loop as the final architecture.**

The prototype is a meaningful improvement over vanilla because the player always had a rational next action and never needed external memory or a wiki. However, the optimal path still decomposed into coordinate search:
1. establish a null/control reference;
2. enumerate the small powder domain;
3. use the Life-family invariant to localize the Life component;
4. enumerate the remaining liquid domain.

The strongest positive moment was not the resonance score itself but the player's independent decision to create a **null reference** and then reason from controlled substitutions.

The substance compendium was accepted as a natural in-game support surface. It should remain a standing product requirement if future puzzles use provenance/family facts.

Experiment cost did not invalidate the prototype, but full-mixture consumption on every information-gathering action is a real friction. Possible future mitigation may include a dedicated research consumable / testing medium that amortizes vanilla reagents into multiple experiment charges. This is an economy/UX question and should not be used to excuse a weak deduction loop.

Design requirement opened by Prototype 13:
**the next candidate must create at least one cross-slot or relational deduction that can resolve late-stage ambiguity without simply scanning the last remaining slot.**

Prototype 10 comparison recovered from prior evidence:
- Prototype 10 tested whole-mixture aggregate resonance alone.
- The player used controlled one-variable changes and solved the case in three paid tests after calibration.
- It was praised for clarity and low working-memory load, but already showed the same structural risk: the natural strategy is coordinate isolation / slot-by-slot scanning.

Therefore Prototype 13 confirms rather than fixes Prototype 10's main weakness. Property gating improves orientation and scale, but does not by itself make aggregate resonance non-enumerative.


### Known-formula comparison as a retained design primitive

Accepted design note after Prototype 13:

Comparison against already-known alchemical products remains a **high-value optional primitive**, not a selected architecture and not something the next prototype must be built around.

Why retain it:
- it makes prior discovery compound into future investigative capability;
- known formulas/products can act as in-world references rather than passive completion records;
- a comparison can potentially express **relations across multiple slots at once**, which is exactly the weakness exposed by aggregate-resonance coordinate search;
- it fits the product fantasy that an experienced alchemist reasons from accumulated knowledge.

Constraints:
- do not make “number of known recipes” the progression currency by itself;
- a reference is useful only when it offers a meaningful relation to the current target, not just another button;
- avoid exposing exact unknown ingredients through overly specific similarity counts;
- known-product comparison should plug into the same journal/compendium information system and remain understandable without wiki memory.

This primitive should be considered alongside other cross-slot mechanisms when selecting Prototype 14. It may be used, combined, or omitted depending on which rule produces the cleanest deduction.


## Post-Prototype-13 cross-slot solution-space pass

Status: **exploratory; no Prototype 14 mechanism selected yet**.

The purpose is broader than fixing Prototype 13's final-slot cleanup. A candidate should be evaluated as a possible new puzzle grammar.

Evaluation dimensions:
- can the complete rule be explained in one short player-facing statement;
- can the player justify *why this experiment now* before seeing its result;
- does one observation constrain more than one slot;
- can late-stage ambiguity be resolved by inference rather than sequential candidate scanning;
- is the evidence world-grounded rather than a disguised correctness oracle;
- does accumulated alchemical knowledge become more useful over time;
- does the journal/compendium keep working-memory burden low;
- does the mechanism avoid reconstructing a hidden recipe book;
- can the rule plausibly cover the bounded vanilla corpus without heavy per-recipe exception authoring.

### Family A — overlapping section resonance

Candidate experiment:
- submit a complete powder + liquid + essence mixture;
- the analyzer has two overlapping sections: powder/liquid and liquid/essence;
- each section reports whether **at least one selected ingredient in that section is exactly correct for the target**.

Example inference shape:
- right section is negative -> both selected liquid and essence are wrong;
- left section is positive -> because the selected liquid is now known wrong, the selected powder must be correct.

Strengths:
- one-sentence rule;
- genuinely overlapping information; the middle slot participates in both observations;
- candidate-driven experiments and clean controlled-variable reasoning.

Weaknesses:
- still an exact-correctness oracle in disguise, with weak world grounding;
- a late single-slot ambiguity can still collapse into sequential scanning;
- known recipes do not naturally become more useful.

Disposition: useful **control candidate**, but unlikely to be the desired final grammar unless a much more natural in-world interpretation appears.

### Family B — target relation assay

Candidate rule:
- reagents expose a small set of inspectable properties in the compendium;
- an assay reveals **one relationship between two target slots**, rather than a property of one slot;
- representative relation: “these two components share at least one provenance class” / “these two do not”.

Example inference shape:
- if powder is already established and the assay says powder and essence share provenance, the known powder properties immediately constrain the essence domain;
- later knowledge about the essence also constrains the powder, so the clue is symmetric and cross-slot.

Strengths:
- directly attacks Prototype 13's final-slot scan;
- reuses world-grounded properties and the accepted compendium;
- one relation can remain useful at several stages of the solve;
- does not need exact ingredient-match feedback.

Weaknesses:
- if the player simply chooses from a menu of equally priced relation queries, this risks becoming “buy a clue” again, reproducing the weakness of Prototype 2;
- the assay menu must make experiment choice hypothesis-driven rather than arbitrary;
- the property relation must stay extremely small/simple to avoid Prototype 4/8 rule-grammar overload.

Disposition: **strongest candidate for a new core grammar**, provided experiment selection itself can be made meaningful.

### Family C — relational comparison with a known formula

Candidate rule:
- choose an already-known potion as a reference;
- comparison does **not** report exact ingredient matches;
- it reports a coarse relationship between the target's structure and the reference's structure, using the same small relational vocabulary as Family B.

Representative implementation:
- every formula has two adjacent “bonds” (powder-liquid and liquid-essence) defined by a simple visible relation such as whether the pair shares provenance;
- comparing target residue with a known potion reports whether neither, one, or both of those relation states are shared, without identifying an unknown ingredient.

Strengths:
- prior recipe discovery becomes analytical capability rather than passive completion;
- reference choice can be meaningful when known formulas have genuinely different relation patterns;
- evidence is cross-slot by construction;
- fits the fantasy of an experienced alchemist reasoning by analogy;
- can coexist with direct property clues instead of replacing them.

Weaknesses:
- if many known recipes have equivalent relational signatures, reference choice becomes fake choice as in Prototype 11;
- if the relational signature is made too rich to avoid equivalence, cognitive load can climb toward Prototype 4;
- as a standalone mechanism it may identify only a structural signature, not enough to finish a recipe.

Disposition: **high-value companion primitive, not yet proven as a standalone core**. Most promising use is as one way of obtaining/triangulating Family-B-style relational facts.

### Current synthesis

Do not evaluate these families only by “does it remove the last scan from Prototype 13”. The broader acceptance question is whether the mechanism creates a clear, interpretable experimental puzzle.

Current preference:
1. test **Family B** as the cleanest new grammar;
2. preserve **Family C** as the most promising way to make accumulated known recipes matter;
3. keep **Family A** as a simple control because it proves whether cross-slot feedback alone is enough even without semantic grounding.

A Prototype 14 candidate should not be precommitted until its experiment-choice problem is solved. In particular, a menu of arbitrary relation assays is not acceptable merely because the resulting clues are logically useful.


## Goal-first research projects — retained fallback / onboarding family

Accepted exploratory design family after the cross-slot pass.

### Core idea

Even if the final product retains a stronger deductive puzzle for formula discovery, Graveyard Keeper's reagent-acquisition layer can be made substantially more coherent by reversing the direction of research:

\`need reagent R -> create research topic R -> pay research cost / perform research work -> learn authored source routes for R -> obtain/study/process a suitable source\`

This contrasts with the vanilla-feeling direction:

\`find source item S -> spend faith to Study S without knowing why -> unlock decomposition -> process S -> discover which reagent appeared\`.

The goal-first flow removes the major targeting gap. It turns research into a player-chosen project anchored in an actual need.

### Representative interaction

A journal/research-station entry may say:
- required reagent: known by name, production route unknown;
- action: “Research preparation of R”;
- cost may use Graveyard Keeper-native research currencies such as faith, paper, ink or energy/time;
- execution may use the ordinary hold-to-work/progress-bar interaction;
- result: the journal records the valid source item(s) / preparation station(s) for that reagent.

The exact cost and whether all sources or only one practical source are revealed remain open.

### Relationship to vanilla Study

This is **not** just tooltip enrichment. If it replaces source-first Study gating, it materially changes vanilla progression semantics:
- today the source item is studied first and then its decomposition route becomes available;
- the proposed direction may instead research the desired reagent first and then reveal and/or authorize a source route.

Therefore production adoption would require an explicit product decision because progression/economy are preserved by default.

Possible implementations to compare later:
1. **informational only** — target research reveals source routes, but vanilla Study is still required before decomposition;
2. **target research substitutes for Study** — completing the reagent project marks relevant decomposition knowledge as learned;
3. **hybrid** — research identifies sources, then studying one selected source completes practical unlock.

The hybrid may preserve the fantasy of examining a material while eliminating blind Study.

### Design classification

If research directly reveals how to make a reagent or even a finished formula, this is **guided disclosure (quality level 2)** rather than deductive discovery.

That is acceptable as:
- an onboarding layer;
- a reagent-acquisition subsystem;
- a deliberately simple fallback architecture if the stronger puzzle system fails;
- a solution for early scripted cases where the game already names one or more formula components and the remaining problem is only “how do I obtain this reagent?”

It should not be mislabeled as the level-3/4 deductive target.

### Progression hypothesis

Do not assume two-slot and three-slot alchemy require entirely different systems yet.

A promising difficulty ladder is:
1. **goal-first reagent research** — teaches target-driven investigation with almost no deduction;
2. **two-component formula discovery** — first short micro-deductions using the same journal/compendium and possibly known-formula comparison;
3. **three-component formula discovery** — introduces the richer cross-slot / relational grammar only when the player already understands the information system.

This could make the puzzle system itself part of progression instead of exposing the full rule set at once.

### Why two-slot recipes deserve separate evaluation, not automatic separate architecture

Existing corpus analysis already showed that ordinary two-slot formulas have much stronger nearest-known-formula overlap than ordinary three-slot formulas. This makes two-slot recipes especially promising for:
- simple analogy with an already-known formula;
- one-relation comparisons;
- one known/strongly constrained component plus deduction of the other;
- tutorial cases for the compendium/reference system.

Therefore Prototype 14 selection should consider the player's **progression stage and recipe arity**, not only one generic three-slot end-state puzzle.

### Simplest-mod fallback

A complete non-puzzle fallback can now be stated clearly:

\`visible need for product/reagent X -> journal research project -> pay bounded research resources/work -> reveal the next required production knowledge -> craft it normally\`.

This would replace blind discovery with a coherent chain of research/crafting/resource tasks that already fits Graveyard Keeper's general gameplay grammar.

It would not satisfy the project's ideal “I deduced the formula” goal, but it is a credible minimum viable redesign and should remain available as the explicit level-2 fallback rather than being rediscovered later.


### Prototype 14 — selected blind candidate

Status: **precommitted; blind play ready**.

After progression research pinned representative Life Powder -> Heal Potion -> Glue states, the post-Prototype-13 solution-space pass selected a minimal **Family B + Family C hybrid** for the next blind test.

Universal grammar under test:
- every known reagent exposes a small world-grounded origin-mark set in the substance compendium;
- two formula components are **related** when their origin-mark sets overlap;
- a 2-slot formula therefore has one pair relation;
- a 3-slot formula has a three-edge relation triangle across all component pairs;
- comparing an unknown target with an already-known reference mixture reports only **how many pair-relation states match**, never exact ingredient matches and never which pair matched.

Why select this over pure Family B:
- it preserves the cross-slot relational inference needed after Prototype 13;
- the reference mixture gives experiment selection an object the player can choose for a reason instead of presenting a flat menu of paid relation queries;
- already-known formulas can become future analytical capability;
- one rule scales naturally from 2-slot to 3-slot;
- comparison operates on relationship structure rather than hidden ingredient correctness, reducing recipe-book/oracle risk.

Why not promote it yet:
- reference choice may still feel like choosing among clue buttons;
- the three-pair triangle may be too cognitively dense;
- relation signatures can collide, so aggregate target evidence must do real work as the first layer;
- progression/runtime integration and exact economy remain unselected.

The blind test uses fictional/isomorphic formulas so no real vanilla recipe is revealed. Complete immutable facilitator state is precommitted in \`docs/prototypes/PROTOTYPE_14_STATE.md\`.

Prototype 14 is a progression slice:
1. reagent-information onboarding is assumed from the accepted goal-first / compendium model;
2. a short 2-slot tutorial analogue tests whether the relation rule is legible;
3. a 3-slot main analogue tests whether reference selection plus aggregate origin evidence removes Prototype 13's late slot scan.

Production mutation remains **BLOCKED**.


### Prototype 14 — stopped after 2-slot tutorial

Disposition: **STOP / REVISE. Do not run the precommitted 3-slot stage.**

The 2-slot tutorial exposed a grammar failure before the main test:
- “related” was not immediately legible;
- the player naturally interpreted comparison as checking a **specific shared origin identity** (for example Corpse+Corpse), not an abstract boolean “has any overlap / has no overlap” state;
- showing only a precomputed relation label for the known reference hid the known formula that was supposed to make accumulated knowledge useful;
- the first action was nearly forced because the only meaningful choices were “compare against the sole reference” or “synthesize essentially at random”;
- after the comparison, the player's natural strategy drifted toward matrix enumeration.

This is not treated as fatigue-only evidence. The player produced a coherent alternative interpretation of the rule, demonstrating that the abstraction itself was under-specified from a natural player perspective.

Retain:
- cross-slot relations remain promising;
- known formulas remain promising as accumulated analytical knowledge;
- the strongest Prototype-13 moment remains **constructing a control/reference and reasoning from a controlled difference**.

Reject from Prototype 14:
- anonymous “RELATED / UNRELATED” relation state;
- hidden structural-signature score against one reference;
- references presented without their actual known composition.

### Concrete-reference redesign pass

Goal: preserve relational reasoning and known-formula value while making the object of comparison explicit and player-chosen.

#### Variant 1 — one-reference named motif

A known formula is shown in full. The player selects one concrete visible relation from it, e.g. “both selected components have botanical provenance”, and assays whether the target has that same named relation.

Strengths:
- matches the player's intuitive interpretation of Prototype 14;
- very easy to explain;
- known formula composition matters directly.

Weakness:
- mechanically close to buying a yes/no property clue;
- with only one useful reference, action choice can again be forced.

Disposition: **retain as a minimal/fallback assay, not preferred core**.

#### Variant 2 — native same-principle relation

Use the vanilla semantic families directly: two components either express the same alchemical principle across forms or different principles.

Strengths:
- much more native and legible than overlapping provenance tags;
- no invented “related” vocabulary is required;
- known formula composition makes the relation self-evident.

Real-corpus screen:
- equality-pattern information is much coarser than exposing the full semantic-family signature, so it is not automatically oracular;
- however, the ordinary formula corpus is strongly dominated by “different principle” relations, particularly in two-slot formulas;
- therefore this relation is too structurally imbalanced to serve as the universal discrimination grammar.

Disposition: **retain as occasional clue/relation where useful, reject as universal core**.

#### Variant 3 — paired positive/negative controls

A concrete question is calibrated using **two already-known formulas**:
- positive control visibly demonstrates the named relation;
- negative control visibly lacks it;
- the target is assayed under the same condition and reports which control behavior it matches.

Example shape:
- question: “Do the target's Powder and Liquid both have botanical provenance?”
- known formula A visibly supplies a positive control;
- known formula B visibly supplies a negative control;
- target outcome is “matches positive” or “matches negative”.

The known compositions are always shown. The player is never asked to trust a hidden summary like “reference is RELATED”.

Strengths:
- experiment semantics are explicit before paying the cost;
- uses known formulas as real laboratory knowledge rather than passive unlock count;
- naturally implements the player's successful null/control reasoning from Prototype 13;
- several possible control questions can partition current hypotheses differently, creating a reason to choose one experiment over another;
- one observation constrains two slots together.

Risks:
- it is still fundamentally a query system and may still feel like purchasing a clue;
- suitable positive/negative controls may not always exist in the actual save state;
- auto-selecting the best controls would turn the journal into a solver;
- requiring the player to hunt manually through many known recipes could become bookkeeping.

Disposition: **selected for the next bounded blind test** because it isolates the exact open question: does explicit experimental control turn a relation query into satisfying player-owned deduction?

### Prototype 15 scope decision

Do not force one grammar across progression merely for elegance.

Known-recipe comparison is not guaranteed to be available for the very first 2-slot target. Prototype 15 therefore tests the paired-control idea directly as a **3-slot mid-progression mechanism**, where accumulated known formulas are plausible. The early reagent and first 2-slot experiences remain separate open design jobs.

Production architecture remains **BLOCKED**.


### Prototype 15 — paired-control blind test

Status: **precommitted; blind play ready**.

Prototype 15 tests Variant 3 from the concrete-reference redesign pass:
- known formulas are shown in full as positive/negative controls;
- each paid assay asks one explicit named two-slot question;
- two available assays cross-cut the current hidden hypothesis set differently;
- no abstract relation state or hidden similarity score is used;
- the test is intentionally 3-slot-only; early 2-slot design remains open rather than being forced into the same grammar.

Complete immutable facilitator state is in \`docs/prototypes/PROTOTYPE_15_STATE.md\`.

Production mutation remains **BLOCKED**.


### Prototype 15 — observed completion

Status: **completed blind play; subjective evaluation pending**.

Observed solve:
- Assay B positive -> player established Powder and Liquid both carry Insect.
- Assay A positive -> player established Liquid and Essence both carry Insect.
- Player combined those cross-slot facts with the initial Plant-count and Corpse-count constraints and derived the unique hidden formula.
- No failed synthesis attempts occurred; the final answer was deduced before synthesis.

This is the first post-Prototype-13 candidate in which the player reached the final formula through a genuine multi-fact cross-slot inference rather than sequentially scanning the last unresolved slot.

However, the presentation/mechanism has serious UX objections already observed during play: high information load, artificial/high-level control framing, unclear value of negative controls, and assay choice driven mostly by slot order rather than hypothesis quality. Do not promote the mechanism until the player's explicit subjective evaluation is recorded.


### Prototype 15 — final evaluation

Overall player rating: **~3/5**.

Accepted design finding:
- the **final deduction structure is a major success**: multiple cross-slot facts can combine with coarse initial constraints to produce a unique formula without slot-by-slot scanning or synthesis enumeration;
- the player described this resolution as exemplary and exactly the kind of reasoning the mod should create;
- therefore the post-Prototype-13 requirement is now sharper: target **fact interaction**, not merely cross-slot feedback. The desirable solve has several individually simple facts whose intersection suddenly collapses the recipe space.

Rejected wrapper:
- paired positive/negative controls;
- compound assay questions over selected slot pairs;
- heavy meta-reasoning about properties of already-known formulas;
- any design where the laboratory fiction is more complicated than the deduction it is meant to support.

Updated architecture direction:
1. keep the goal-first / compendium layer for targetable investigation and external memory;
2. keep coarse world-grounded properties because they are useful inputs to deduction;
3. seek **natural evidence sources** that each yield one small fact, preferably through direct observation / ordinary GK actions;
4. allow those facts to constrain multiple slots or interact across the formula;
5. aim for the Prototype-15 endgame shape: two or three understandable observations combine into one forced answer;
6. known recipes may contribute one such observation, but are optional evidence primitives rather than the core grammar.

New primary design question:
**What simple, natural, Graveyard-Keeper-native actions can yield the cross-slot facts needed for a Prototype-15-quality final deduction without feeling like a menu of abstract queries?**

This supersedes the narrower question of how to improve known-formula comparison.

Production architecture remains **BLOCKED**.
