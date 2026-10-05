# Fixed reagent tag model — secondary exploration

**Status: NON-CANONICAL / SECONDARY CHAT BRANCH**

This document records the first evidence-backed screen requested in the
secondary ChatGPT branch. It is not an accepted production model.

## Scope

The loaded Graveyard Keeper 1.407 ordinary picker-compatible success corpus
uses **35 distinct final alchemical ingredient definitions**:

- 15 Powder;
- 8 Fluid;
- 8 Essence;
- 4 Universal.

This is the relevant population for the current puzzle corpus. It is narrower
than the full picker-eligible definition envelope (16 Powder, 9 Fluid,
8 Essence, 19 Universal).

Of the 35 used ingredients:
- 24 are the eight regular semantic families, each represented by
  Powder / Fluid / Essence;
- 11 are singleton/special ingredients.

## Draft fixed tag vocabulary

The working vocabulary is deliberately world-legible and source-grounded:

- Растение
- Труп
- Минерал
- Насекомое
- Животное
- Рыба
- Слизь
- Вода

These are AlchemyRiddle design abstractions, not vanilla fields.

Interpretation: a final vanilla reagent receives a stable set of affinities
derived from the meaningful classes of its authored source/acquisition paths.
The tags belong to the **final reagent type**, not to individual stack units.

For gameplay readability, `Насекомое` is currently used as a broad small-
arthropod/product bucket (including web / beeswax / honey provenance). This is
a naming/detail question, not yet an accepted taxonomy.

## Draft assignment

### Universal

| Reagent | Fixed tags |
| --- | --- |
| Алкоголь | Растение |
| Вода | Вода |
| Кровь | Труп |
| Масло | Растение, Труп |

Notes:
- Alcohol is ultimately produced from booze whose ordinary source chain is
  plant fermentation.
- Oil has both plant-derived seed-oil and corpse-fat acquisition paths, so its
  fixed type-level cloud includes both.

### Powder

| Reagent | Fixed tags |
| --- | --- |
| Белый порошок | Труп, Минерал |
| Золотой порошок | Минерал |
| Пепел | Труп |
| Порошок графита | Минерал |
| Порошок жизни | Труп, Минерал |
| Порошок замедления | Растение, Минерал, Насекомое |
| Порошок здоровья | Растение |
| Порошок порядка | Насекомое, Минерал |
| Порошок смерти | Труп |
| Порошок ускорения | Растение, Насекомое |
| Порошок хаоса | Животное, Насекомое |
| Серебряный порошок | Минерал |
| Соль | Труп |
| Токсичный порошок | Растение |
| Электрический порошок | Рыба |

### Fluid

| Reagent | Fixed tags |
| --- | --- |
| Раствор жизни | Труп, Растение, Насекомое |
| Раствор замедления | Растение, Труп, Насекомое |
| Раствор здоровья | Растение |
| Раствор порядка | Растение, Насекомое, Слизь |
| Раствор смерти | Труп, Слизь |
| Раствор токсичности | Растение, Слизь |
| Раствор ускорения | Насекомое, Слизь |
| Раствор хаоса | Животное, Насекомое |

### Essence

| Reagent | Fixed tags |
| --- | --- |
| Экстракт жизни | Труп, Растение, Насекомое |
| Экстракт замедления | Насекомое |
| Экстракт здоровья | Растение |
| Экстракт порядка | Растение, Слизь |
| Экстракт смерти | Труп, Слизь |
| Экстракт токсичности | Растение, Слизь |
| Экстракт ускорения | Растение, Слизь |
| Экстракт хаоса | Насекомое |

## Reproducibility checkpoint

The new `research/TagModelScreen/tag_model_screen.py` helper was designed so
the exact formula corpus remains private input.

Before applying the new tag screen, the private ordinary three-slot data was
cross-checked against the accepted structural baseline:

- 19 formulas;
- 16 outputs;
- 10 Powder-slot candidates;
- 9 Fluid-slot candidates;
- 9 Essence-slot candidates;
- 810 Cartesian triples;
- 19 stable Powder-Fluid edges;
- 18 stable Fluid-Essence edges;
- 47 two-edge-compatible chains.

The baseline matches the previously accepted screen.

## First information-diversity result

With the fixed draft tags above, exact tag clouds are **not globally unique**.

### Signature diversity by alchemy form

| Form | Reagents | Distinct tag signatures |
| --- | ---: | ---: |
| Powder | 15 | 9 |
| Fluid | 8 | 7 |
| Essence | 8 | 5 |
| Universal | 4 | 4 |

Important collisions include:

- `Минерал`: Golden powder / Graphite powder / Silver powder;
- `Труп`: Ash / Death powder / Salt;
- `Труп + Минерал`: White powder / Life powder;
- `Растение`: Health powder / Toxic powder;
- `Растение + Труп + Насекомое`: Life solution / Slowing solution;
- `Растение + Слизь`: Order / Toxic / Acceleration extracts;
- `Насекомое`: Slowing / Chaos extracts.

Therefore provenance-style tags cannot be expected to identify every final
reagent by themselves.

## Full-field three-slot screen

A second screen asked a deliberately strong question:

If the player sees the full ordinary 10 x 9 x 9 three-slot structural field,
and target research may state exact counts (including zero) for the draft tags,
how far can tag facts alone narrow the first-stage Powder+Fluid branches?

For outputs with multiple vanilla formulas, only facts that are true for
**every** formula of that output were allowed.

Result:
- 11 / 16 outputs can be reduced to at most four Powder+Fluid branches by some
  subset of the common exact tag-count facts;
- 5 / 16 remain above four branches even if every common exact tag-count fact
  is supplied.

This supports the user's prior intuition: the natural coarse tag vocabulary
does **not** provide enough information diversity to carry the whole puzzle on
the unrestricted field.

It does not show that the tag model is unusable. Candidate-surface curation,
compatibility relations and other clue types can supply the missing
information.

## Multi-formula invariant issue

A full aggregate tag vector is not always an intrinsic property of an output.

For several outputs with multiple valid vanilla formulas, the different
correct formulas have different total tag counts under this draft model.
Therefore a target clue such as "exactly X Plant, Y Corpse, Z Mineral..." cannot
automatically specify the complete vector of one hidden formula while
preserving every vanilla alternative as equally valid.

Preferred direction for later screens:
- derive target facts that are common to all vanilla formulas for that output;
- allow a subset of exact counts, zero-count exclusions, ranges or other
  invariant statements;
- do not silently invalidate an alternate vanilla recipe merely to make the
  clue vector prettier.

## What this establishes

Promising:
- a fixed type-level tag cloud avoids per-unit provenance and inventory
  variants;
- the vocabulary is strongly world-grounded and easy to teach through Study;
- the model has real, but deliberately incomplete, information content.

Not established:
- whether this exact vocabulary/naming is final;
- whether a curated 3x3x3 surface plus these tags gives enough diversity;
- whether the two-slot corpus can use the same tag grammar satisfactorily;
- what additional relational clues should supplement tags;
- whether every fully researched puzzle can be forced to a unique formula.

## Next research step

Before redesigning two-slot or three-slot UX, screen this same fixed tag model
under the accepted bounded-candidate convention:

1. determine whether each ordinary target can receive a small candidate surface
   containing all of its valid vanilla formulas;
2. measure how much invariant tag information is needed inside that surface;
3. identify the remaining ambiguity classes;
4. only then decide whether tags need refinement or compatibility/other clues
   are sufficient to resolve them.
