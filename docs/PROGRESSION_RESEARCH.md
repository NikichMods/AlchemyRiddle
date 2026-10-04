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
