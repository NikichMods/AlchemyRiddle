# Secondary chat branch — exploratory notes

**Status: NON-CANONICAL / SECONDARY CHAT BRANCH**

Origin: a branched ChatGPT conversation created after the large design-question checkpoint on 2026-10-05.

Purpose: preserve exploratory ideas from this lighter parallel conversation without allowing them to overwrite or silently compete with the main design line.

## Promotion rule

Nothing in this file is an accepted product or architecture decision merely because it was discussed here.

When the primary conversation later reaches the same decision area:
- compare these notes against the primary branch's reasoning;
- explicitly promote only the parts that remain useful;
- move accepted conclusions into the canonical owner, normally `docs/DESIGN_RESEARCH.md` and/or `docs/PRODUCT_REQUIREMENTS.md`;
- do not treat this file as current project truth when it conflicts with canonical main-line documents.

## Preliminary ideas raised in this secondary branch

These are exploratory positions, not commitments.

### Candidate surface

A deliberately bounded candidate field such as 3x3x3 may simply be presented as part of the puzzle format, without an in-world explanation for why exactly those candidates appear.

A stronger but more complex alternative remains possible: expose a larger known set and let target tags plus automatic/manual filtering reduce it to a manageable working field.

### Two-component alchemy

Desired product direction:
- two-component alchemy should ideally be a natural, simpler, self-contained teaching step before three-component alchemy;
- a possible grammar is to give a target multiset of tags and ask the player to choose a Powder + Liquid pair whose visible tag totals satisfy it;
- this needs separate prototyping because adjacent compatibility alone risks becoming direct recipe disclosure in a two-slot formula.

### Tags / properties

The current broad semantic tags such as Plant, Corpse, Mineral and Insect feel natural and game-compatible.

Possible acquisition:
- Study at the research table unlocks an item's alchemical property/tag information;
- the item's tooltip can then display those properties.

Important unresolved problem:
- vanilla processing collapses different source items into the same alchemical reagent item;
- if provenance-derived tags depend on the original source, a single vanilla stack such as one Life Powder type cannot simultaneously remember whether each unit came from Plant, Corpse, Mineral, Insect, Fish, etc.;
- solving this by creating many persistent inventory variants would risk inventory clutter and save/removal complexity;
- a possible alternative is virtual/source-specific research representations that exist only inside the puzzle/research interface rather than as separate inventory items.

This source-collapse problem is a major architecture/research issue, not a settled design.

### Starting information and prior relations

It is acceptable in principle for the system to surface deliberately useful prior compatibility knowledge; the player may infer some authorial friendliness.

A possible mix is:
- one genuinely useful relation;
- one misleading or dead-end relation;
- one neutral contextual relation;
- perhaps 4-5 shown relations rather than a tiny hand-picked set.

Exact salience/relevance rules remain open.

### Deduction endpoint

Preliminary preference:
- it is acceptable for the player to reach two plausible formulas and commit to one using residual/circumstantial reasoning;
- but if the player fully uses the intended research opportunities, there should ideally always exist a path to a unique answer.

These two statements are not considered contradictory: early commitment may be optional, while exhaustive intended investigation should resolve uniqueness.

### Experiment cost

Tentative idea only:
- introduce a crafted generic research consumable such as a "sample box";
- craft it from a small assortment of real materials to communicate that it represents mixed experimental samples;
- microtests consume this abstract resource rather than consuming recipe ingredients one-for-one.

Concerns:
- introduces a new persistent game entity;
- save compatibility and mod removal behavior would need research;
- may be unnecessary complexity.

Do not treat this as accepted.

### Progression and missing candidates

If the intended candidate field includes an item the player has not studied, the UI could show an unknown/unavailable slot or tell the player which material needs Study first.

Concern:
- forcing the player to research a distractor that cannot belong to the final recipe may feel like imposed busywork.

Possible stronger alternative:
- derive/filter the working field from currently known items and target tags rather than prescribing exact hidden-answer-centered distractors.

### Filtering idea

In an idealized version, the player could start from the larger known reagent set and use target tag information to narrow it:
- automatically;
- semi-automatically;
- or by selecting tag filters in the research UI.

This could make the bounded field emerge from visible rules rather than from unexplained author selection, but may raise UI and cognitive-complexity costs.

## Explicit unresolved questions from this branch

1. Can the vanilla "collapsed reagent" model coexist with source/provenance tags without creating inventory variants?
2. Should tags attach to vanilla reagent types, original source items, virtual research representations, or something else?
3. Can two-component alchemy use tag-total deduction as a tutorial while remaining interesting and not trivial?
4. Is an unexplained bounded candidate field acceptable as a product convention, or should it be derivable from tags/filtering?
5. How much deliberately useful prior compatibility information can be surfaced before meta-reading overwhelms in-world deduction?
6. Should full intended research guarantee a unique formula in every puzzle?
7. Can progression gating avoid forcing study of irrelevant distractors?
8. Is an abstract experiment consumable worth the persistence/save complexity?

## Branch handling

This file and its Git branch exist specifically to keep this secondary conversation separate from the stable/main design line.

Repository branch: `research/secondary-chat-2026-10-05`.

Do not merge this branch wholesale. Promote individual accepted findings only after comparison with the primary conversation.


## Analysis after the first broad answer

This analysis remains NON-CANONICAL and belongs only to the secondary exploratory branch.

### Emerging coherent architecture candidate

The user's answers suggest a potentially coherent family of rules:

1. A bounded candidate surface may be accepted as a puzzle convention without an in-world derivation rule.
2. Study reveals stable alchemical properties/tags.
3. Two-slot alchemy can teach tag-composition deduction in a simpler self-contained form.
4. Three-slot alchemy can reuse the same tags but add adjacent compatibility as the new relational layer.
5. Full intended research should ideally guarantee a unique formula, while the player may commit earlier when two plausible hypotheses remain.
6. Starting compatibility knowledge may be answer-aware and deliberately helpful, provided the system does not become mechanically predictable.

This is promising because it creates pedagogical progression:
- two slots: composition/signature constraints;
- three slots: composition/signature constraints + compatibility graph.

### Important distinction: reagent tag vocabulary vs target clue projection

A reagent can have one stable, immutable tag set everywhere in the game while individual puzzles expose only some aggregate constraints over that tag vocabulary.

Therefore the concern that a richer tag vocabulary needed for two-slot puzzles must automatically overload three-slot puzzles is not necessarily fatal. The same reagent tags can remain visible, while the target clue selects/emphasizes only the dimensions relevant to the current investigation.

This needs UI validation because irrelevant visible tags can still create cognitive noise.

### Major architecture problem: vanilla reagent identity collapses provenance

The user's strongest new concern is valid and fundamental.

If tags such as Plant / Corpse / Mineral / Insect are properties of the ORIGINAL SOURCE item, but vanilla processing collapses multiple different sources into the same Powder/Solution/Essence item, then source provenance is lost at the exact point where the alchemy formula operates.

Therefore provenance-dependent tags cannot be attached naively to vanilla inventory stacks without one of these costs:
- splitting one vanilla reagent type into multiple source-specific item variants;
- tracking per-unit provenance metadata inside otherwise identical stacks;
- moving the puzzle to virtual source-specific representations that are not the actual vanilla recipe ingredients.

All three create complexity or semantic mismatch.

A cleaner possibility is to make tags properties of the FINAL VANILLA ALCHEMICAL REAGENT TYPE rather than the source item. If Plant / Corpse / Mineral / Insect are retained, they would need to be interpreted as fixed affinities/classifications of the processed reagent, not literal per-unit provenance.

This becomes a high-priority research/design question: **what is the canonical owner of a tag?**

### Two-slot alchemy

The tag-total idea is especially promising as a tutorial grammar.

Possible structure:
- show a bounded Powder x Liquid field;
- every candidate has immutable visible tags;
- target research gives an aggregate tag signature/count requirement;
- the player chooses the pair whose combined tag vector satisfies the target;
- compatibility is either absent from two-slot puzzles or only used as a final confirmation, because a two-item compatibility edge is otherwise too close to direct formula disclosure.

This would teach the same tag language later reused by three-slot puzzles without forcing the three-slot compatibility mechanic into a shape where it leaks the answer.

Quantitative screening would be needed to see whether a fixed tag vocabulary can make real two-slot recipes uniquely or near-uniquely identifiable at a comfortable candidate-field size.

### Candidate surface

The user is willing to treat a 3x3x3 field as an authored puzzle convention: the mod may simply present those candidates, with no lore justification for why exactly they are present.

This is a legitimate product simplification if accepted in the primary line. It converts the current "candidate-surface legitimacy" blocker from a mandatory world-model problem into a tuning/fairness problem.

The remaining requirement would be weaker:
- the field must still support genuine deduction;
- it must not be so answer-shaped that selection itself effectively reveals the recipe;
- its construction should be stable enough that players cannot exploit a trivial meta-rule.

### Starting knowledge / first-ever puzzle

Study can naturally unlock tag/property knowledge.

For the player's first alchemy puzzle, where no prior compatibility graph exists:
- two-slot tag-composition puzzles can work with zero prior relations;
- early three-slot puzzles can be constructed so target tags alone reduce the space enough;
- later puzzles can increasingly benefit from accumulated compatibility knowledge.

This creates a natural progression path and reduces the need for artificial tutorial-only exceptions.

### Helpful prior relations and meta-information

The user is comfortable with deliberately answer-aware selection of prior relations.

A plausible rule family is:
- guarantee at least one relation that is genuinely useful;
- fill the rest with neutral or misleading-but-legitimate known relations;
- vary the count and usefulness so the player cannot infer an exact meta-rule such as "exactly one displayed relation is on the answer path."

This is friendlier than showing the whole graph while retaining some uncertainty.

### Deduction endpoint

The user's two preferences are compatible and can be expressed as two completion levels:

- **Early commitment:** the player may synthesize while multiple plausible formulas remain, accepting residual uncertainty.
- **Guaranteed full solve:** if the player uses the intended available research completely, there should be a route to a unique formula.

This is a strong design target because it preserves agency without making the puzzle formally underdetermined.

### Experiment cost

The "sample box" idea is conceptually coherent but probably premature.

Its useful principle is more important than the specific item:
- experiments may consume an abstract research resource funded by ordinary materials rather than burning exact recipe ingredients one-for-one.

Before introducing a persistent new inventory object, compare cheaper mechanisms:
- a UI-only research-charge balance;
- immediate conversion of ordinary materials into charges;
- use of an existing resource only if it does not distort vanilla economy.

Save/removal complexity should be treated as a cost of the persistent-item implementation, not as a reason to discard the resource abstraction itself.

### Progression and unknown candidates

Showing forced unknown distractor slots is risky because it can compel irrelevant Study work.

Potentially better patterns:
- only unlock a puzzle when enough relevant candidate knowledge exists;
- allow the candidate surface to adapt to studied reagents;
- or state that knowledge is insufficient without naming an exact distractor, e.g. "you still lack a studied Powder with property X."

The user's filtering idea is the strongest immersion-oriented alternative: let visible target tags reduce a larger known reagent set automatically or semi-automatically until a manageable working field emerges.

This may solve candidate-surface legitimacy at the cost of UI complexity and should be evaluated only after the tag model is stable.

### Highest-value next research questions on this branch

1. What owns a tag: source item, processed vanilla reagent type, virtual research representation, or something else?
2. Can a fixed source-independent tag vocabulary over FINAL vanilla reagent types still feel as natural as Plant / Corpse / Mineral / Insect?
3. Can the real two-slot recipe corpus be made into satisfying tag-composition puzzles using that same vocabulary?
4. If the candidate field is accepted as authored convention, how answer-shaped may it be before it stops feeling like deduction?
5. Can full research guarantee uniqueness while preserving optional earlier commitment?


## Foundation screen checkpoint

The secondary branch has now completed the first requested foundation pass:
- identified the 35 final reagent definitions actually participating in the ordinary successful corpus;
- drafted fixed type-level provenance/affinity tags for all 35;
- restored a reproducible tag-screen helper with the accepted three-slot structural baseline;
- found that the coarse natural tag model has useful but insufficient global information diversity;
- identified the multi-formula invariant problem for complete target tag vectors.

Detailed non-canonical evidence: `docs/explorations/TAG_MODEL_DRAFT_2026-10-05.md`.

Do not promote this model to main without primary-line review.


## Integration status — CLOSED 2026-10-05

This exploratory chat branch has now been reviewed against the canonical main
line.

The accepted evidence and decisions worth retaining were promoted individually
to `main`, culminating in canonical continuation commit:

`8b2ab3c908ec6a65629f7a58b4cfc71016dc9309`
— `Integrate secondary branch and set adaptive comparison task`.

Do **not** resume project work from this branch and do **not** merge it
wholesale. Recover current state from `main`, especially the final
`Secondary-branch integration checkpoint — 2026-10-05` in
`docs/DESIGN_RESEARCH.md`.

The immediate canonical next task is the quantitative comparison between:
1. the fixed bounded tag-centric three-slot puzzle baseline; and
2. the adaptive knowledge-aware variant that incorporates the player's
   accumulated STABLE / INCOMPATIBLE adjacent-pair graph.

The broader project backlog remains canonical in `main`; this branch covered
only a subset of the overall AlchemyRiddle design questions.
