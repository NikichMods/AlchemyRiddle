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
