# Alchemy target progression skeleton — 2026-10-06

Status: **bounded progression model for sequence-diversity research; accepted as a coarse research approximation, not a canonical playthrough chronology; production remains BLOCKED.**

## Question

The property-depth / sequence-diversity screen needs some approximation of the
order in which alchemical targets become relevant.

A full Graveyard Keeper story simulation is not justified at this stage.

The smallest useful model asks only:

1. when can the player use the two-slot and three-slot alchemy apparatus;
2. through what kind of event does an ordinary alchemical product first become
   naturally useful/needed;
3. which broad progression bucket should constrain sequence simulations.

This document intentionally does **not** reconstruct exact NPC-relation timing,
weekday routing, technology-point spending order, or one canonical save.

## Evidence base

Primary project/shared evidence:
- `GraveyardKeeperResearch/docs/ALCHEMY_SYSTEM.md`;
- accepted AlchemyRiddle 1.407 ordinary corpus:
  - 18 ordinary two-slot outputs / 24 formula variants;
  - 16 ordinary picker-compatible three-slot outputs / 19 formula variants;
  - the separate picker-incompatible three-slot success definition remains
    outside this ordinary progression model.

Secondary progression cross-checks used only for coarse ordering:
- current Graveyard Keeper technology-tree reference for the Anatomy & Alchemy
  branch;
- current item/workstation reference pages for downstream uses;
- public story-catalog evidence for a small number of scripted formula/quest
  cases.

Exact vanilla formula ingredient rows remain outside this document.

## 1. Recipe knowledge and product demand are different axes

Do not model “a recipe was unlocked” as equivalent to “the player now needs
this product”.

The native game has separate channels:
- technology unlocks alchemy apparatus and downstream recipes/actions;
- mixed alchemy formulas are normally discovered through experimentation or
  separate scripted/random recipe-discovery channels;
- quests and newly visible downstream crafts can create a concrete need for an
  alchemical product before the player knows its formula.

For AlchemyRiddle sequence modeling, **first meaningful demand for the product**
is the relevant trigger.

## 2. Ordinary-output demand-channel fingerprint

Across the accepted 34 ordinary picker-compatible target outputs, the coarse
first-use shape is:

### Downstream material / craft component — 16 outputs
- **6 two-slot** outputs feed ordinary downstream systems such as writing,
  church production, fertilizer or later embalming;
- **10 three-slot** outputs feed systems such as embalming injections,
  fertilizer, incense or book production.

These are the strongest technology-driven target candidates because the player
can see a useful downstream recipe/action that requires the unknown product.

### Direct-use consumables — 8 outputs
- **2 two-slot** direct-use potions;
- **6 three-slot** direct-use potions.

These do not automatically create a strong goal-first research lead merely by
existing. Their first meaningful need is player-driven (combat, travel,
survivability, convenience) unless another authored task requests them.

### Direct story/system demand — 2 outputs
- one two-slot product is an explicit Merchant quest material;
- one two-slot product is required by the zombie/resurrection system after that
  story branch opens.

These give strong authored goal-first leads independent of downstream
technology recipes.

### DLC/remodelling-specific targets — 8 outputs
- eight two-slot coloured-paint outputs belong to the special remodelling/DLC
  use family.

Keep these as a distinct progression bucket rather than letting them dominate
the base-game target-order approximation.

Aggregate check:
- 16 downstream-component;
- 8 direct-use;
- 2 direct story/system;
- 8 DLC/remodelling;
- **34 total ordinary outputs**.

This classification is about target demand, not formula difficulty.

## 3. Minimal progression buckets

### P0 — pre-alchemy

Before the Clotho alchemy introduction:
- no normal AlchemyRiddle deduction should be considered available;
- source materials may already have been encountered/studied, but that does not
  yet define an alchemy target sequence.

### P1 — Beginning of Alchemy / two-slot capable

The first alchemy technology unlocks:
- alchemy mill;
- hand mixer;
- alchemy workbench tier I.

Research implication:
- the **two-slot ladder can begin**;
- practical Powder/Fluid identities can start accumulating;
- not all 18 two-slot outputs should be treated as simultaneous natural goals:
  their downstream/story uses mature at different times.

This is the correct bucket for the first two-slot tutorial and early two-slot
practice.

### P2 — early demand expansion before full three-slot capability

After the first alchemy unlock, other technologies/story lines can expose
downstream needs.

Important structural observation:
- the Embalming Liquids technology is downstream of Beginning of Alchemy and
  exposes early injection recipes;
- some of those downstream recipes require products that are themselves
  three-slot alchemy outputs;
- the tier-II alchemy workbench is only unlocked by **Advanced Alchemy**, a
  separate later node.

Therefore a player can plausibly **see a need for a three-slot product before
having three-slot apparatus**.

Do not collapse:
- target lead visible;
- arity puzzle can be started;
- reagent can be practically produced.

These are separate state transitions.

### P3 — Advanced Alchemy / three-slot capable

Advanced Alchemy unlocks:
- alchemy workbench tier II;
- distillation capability needed for normal Essence production.

Research implication:
- the **three-slot ladder can begin** here;
- existing queued three-slot leads become actionable;
- two-slot and three-slot investigations now naturally interleave.

This is the correct bucket for the first three-slot tutorial validated by
Prototype 35.

### P4 — mature / late mixed demand

Later technologies and story branches expose:
- higher embalming tiers;
- stronger fertilizers;
- advanced incense/church production;
- hard-cover/book production;
- later quest requests;
- DLC/remodelling targets.

Crucially, some of these late needs point back to **two-slot** products.

Therefore chronological progression does not imply:
`all two-slot targets -> all three-slot targets`.

This independently supports the already accepted product decision to maintain
two arity-specific difficulty ladders that can interleave.

## 4. What this means for sequence-diversity simulation

Do not generate a random permutation of all 34 targets.

Use bucket-constrained sequences:

1. begin with P1 two-slot candidates;
2. add P2 downstream/story leads as they become visible;
3. after P3, mix both arities while advancing each arity's own difficulty state;
4. introduce P4 and special/DLC targets later;
5. direct-use consumables may enter as optional targets rather than mandatory
   chronology anchors.

Within a bucket, deliberately vary order instead of pretending one exact
playthrough order is known.

This gives sequence diversity a realistic chronology constraint without
reconstructing the whole quest graph.

## 5. Reagent-knowledge approximation

The accepted theoretical/practical split means exact practical mastery is **not
a hard candidate-field boundary**.

Therefore the first sequence screen does not need a perfect save-state model of
all 35 reagent identities.

Track identity exposure instead:

- identity already known before the investigation;
- newly exposed **true** component identity;
- newly exposed **decoy** identity;
- practical source/preparation already known vs still unknown.

For the first sequence screen:
- treat unnecessary new decoy identities as a cost;
- permit a new true identity when the target deduction needs it;
- do not block a puzzle solely because practical production is not yet mastered.

A later refinement may bracket identity knowledge with conservative and generous
progression states if the sequence result proves sensitive to this cost.

## 6. What was deliberately not researched

Not needed yet:
- exact relation thresholds for every NPC;
- exact weekday order;
- exact technology-point purchase order;
- a complete story DAG;
- exact probability/order of random Alchemy Recipe scroll unlocks;
- one deterministic list of 34 target timestamps.

Those details should be researched only if the sequence-diversity conclusion is
sensitive to the coarse P0-P4 model.

## 7. Immediate next quantitative use

The next property-depth experiment can now be bounded:

- use the current 1/2/3-property model as control;
- generate good medium/late puzzle choices subject to P1-P4 target availability;
- penalize recently reused reagent identities and exact tag signatures;
- measure remaining choice reserve;
- measure new true-identity and new-decoy exposure separately;
- compare current model against counterfactual property enrichment only if the
  control shows a real sequence-level bottleneck.

No full progression archaeology or installed-runtime test is required before
that screen.
