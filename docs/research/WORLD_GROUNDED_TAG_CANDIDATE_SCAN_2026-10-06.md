# World-grounded tag candidate scan — 2026-10-06

Status: **candidate research only; no property assignment change accepted; production remains BLOCKED.**

## New user-facing design preference

The user explicitly values **visible property density** as part of puzzle texture,
not only formal information gain.

Current distribution:
- 16 one-property reagents;
- 14 two-property reagents;
- 5 three-property reagents.

Soft preference, **not a hard quota**:
- two-property cards should feel like the normal/core case;
- one-property cards are useful simple / early-game exceptions;
- three-property cards are useful richer / later-game exceptions;
- a distribution in the rough neighbourhood of 25% / 50% / 25% for
  one/two/three-property cards is aesthetically attractive to the user;
- do not optimize to a pretty histogram if it damages world grounding,
  learnability or reasoning quality.

The current practical ceiling remains three visible properties per reagent until
explicitly reopened.

## Search method

Do not invent tags directly from puzzle mathematics.

For all 35 accepted ordinary reagent identities:
1. inspect every authored non-goo decomposition source and obvious world/source
   semantics;
2. propose global deterministic source categories;
3. apply each candidate category consistently to every reagent whose source
   satisfies it;
4. measure:
   - one/two/three-property distribution;
   - duplicate-signature reduction;
   - number of cards that would exceed three properties;
   - effect on accepted puzzle / sequence / reasoning-diversity screens;
5. only then consider a matched blind player-facing comparison.

A candidate is stronger when it:
- is obvious or cheaply learnable from Graveyard Keeper itself;
- applies to several reagents/forms, not one hand-picked card;
- separates currently duplicated/shallow signatures;
- enriches one-/two-property cards without flooding existing three-property
  cards;
- does not require a hidden taxonomy explanation.

## Initial strong candidates from full source scan

### Organ
World basis includes normal/dark anatomical organs:
- intestines / dark intestines;
- brain / dark brain;
- heart / dark heart.

It naturally spans Powder, Fluid and Essence families and separates multiple
currently shallow/duplicated corpse-derived signatures.

Naive additive application touches about six accepted reagents.

Important conflict:
- the Life Fluid and Life Essence are already three-property cards;
- naive addition would make them four-property cards.

Therefore **Organ is a strong semantic candidate but cannot simply be appended
globally while preserving the current three-property ceiling**.

Possible later solution families to compare, not yet accepted:
- rare four-property exception;
- taxonomy refinement/hierarchy;
- replacement/rebalancing of broad parent categories;
- narrower world-grounded subtype such as dark-organ lineage.

Do not choose among these yet.

### Metal
World basis:
- gold nugget;
- silver nugget.

Cleanly separates Gold Powder and Silver Powder from Graphite Powder inside the
current Mineral signature.

Naive additive application:
- affects two reagents;
- creates no four-property cards.

Semantically very clean but narrower than Organ.

### Flower
Direct flower sources occur across several forms, including toxic/order/life
families.

Naive additive application would distinguish several plant-derived reagents, but
it would also push multiple already-rich Fluid/Essence cards above three
properties.

Promising semantic axis; poor fit as a simple additive tag under the current
ceiling.

### Cultivated crop / farmed plant
Direct crop sources include cabbage/pumpkin, hops, hemp, onion and carrot.

This axis can enrich several one-/two-property plant reagents and is intuitive
from normal gameplay.

Naive additive application would push at least the already three-property
Slowing Powder above the current ceiling.

Promising but not yet clean.

## Narrower secondary candidates

- cremation / combustion-derived: strongly grounded for Ash and Salt, but narrow
  and does not separate those two from each other;
- dark-organ lineage: applies cleanly to Death Powder / Fluid / Essence and stays
  within three properties, but is less general/elegant than Organ;
- mushroom/fungal: too narrow in the current ordinary corpus to justify on its
  own.

Existing categories such as Slime/Insect already capture several source families;
do not duplicate them under synonymous new labels.

## Immediate design consequence

The next step should treat this as a **taxonomy design problem**, not merely an
append-tags problem.

The three-property ceiling plus the user's preference for a richer 1/2/3 spread
means candidate evaluation must consider:
- which old broad tags remain;
- whether new subcategories coexist with or refine broad categories;
- whether any hierarchy is worth its extra rule complexity.

Do not accept a hierarchy merely to save a preferred histogram.

No runtime test is required.
