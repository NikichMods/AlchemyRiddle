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
