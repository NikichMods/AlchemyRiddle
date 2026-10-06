# Difficulty Curriculum Corpus Screen — 2026-10-06

Status: **accepted quantitative research candidate; production remains BLOCKED**.

Purpose: test whether the externally validated difficulty-curriculum model is
structurally realizable on the concealed ordinary Graveyard Keeper 1.407
alchemy corpus before spending blind-play effort on tuning thresholds.

Exact vanilla formula rows and the temporary de-anonymizing join remain outside
the public repository.

## Research-method checkpoint

Question:
- can the accepted two-slot and three-slot puzzle grammars realize the proposed
  onboarding / early / later curriculum shapes across the ordinary corpus;
- which clue families are actually required by capacity, and which can be
  introduced for variety / cognitive progression rather than necessity;
- can the first three-slot investigation genuinely **teach** the adjacent
  STABLE/INCOMPATIBLE relation, rather than include a decorative relation after
  property clues have already nearly solved the puzzle?

Existing path:
- reuse the accepted anonymized runtime corpus and fixed eight-property model;
- reuse the existing TagModelScreen family rather than author another runtime
  probe;
- reconstruct the private formula input from retained project evidence and the
  previously verified identity join;
- validate the reconstruction against the accepted structural baselines before
  running a new screen.

Justification for new research code:
- the existing helpers answer older capacity / progression / adaptive-knowledge
  questions but do not distinguish pedagogical clue-family tiers or enforce that
  a tutorial relation experiment performs necessary information work;
- a small private-input Python helper is therefore the lowest-assumption,
  reproducible extension.

Helper:
`research/TagModelScreen/difficulty_curriculum_screen.py`.

CI:
- initial helper: run **37473968274**, success;
- tightened tutorial criterion: run **37474605321**, success.

## Private-input recovery validation

The recovered private corpus reproduced every relevant accepted baseline.

Two-slot:
- 24 ordinary formula variants;
- 18 outputs;
- 15 first-slot participants;
- 9 second-slot participants;
- 23 / 24 variants have another ordinary formula at Hamming distance 1.

Three-slot:
- 19 ordinary picker-compatible formula variants;
- 16 outputs;
- 10 Powder x 9 Fluid x 9 Essence = 810 structural triples;
- 19 stable Powder-Fluid edges;
- 18 stable Fluid-Essence edges;
- exactly 47 chains satisfy both adjacent stable-edge relations.

Therefore the new pass operates on the same accepted corpus rather than an
approximate reconstruction.

## Two-slot curriculum result

The screen separates the accepted logical language into progressively richer
families:

1. **simple** — slot-local property presence/absence and exact pair counts;
2. **XOR** — simple plus exact-one-of-two relations;
3. **forward positive implication** — Powder -> Fluid implication with a
   positive consequent;
4. **forward negative implication** — the same direction may also imply absence;
5. **reverse implication** — Fluid -> Powder, carrying the previously accepted
   reverse-reference cognitive cost.

The result is an existence screen: a variant passes when at least one
target-containing candidate field of that shape can produce the specified
deduction. It does not claim every possible field is good.

### Tutorial: simple 2x2 is sufficient across the corpus

For all **24 / 24** ordinary two-slot formula variants there exists a 2x2 field
where:
- the grammar is simple only;
- two individually partial simple clues uniquely identify the target pair under
  the compact small-field clue-strength policy.

Consequence:
- the two-slot tutorial does not need XOR or implication for structural
  coverage;
- the cleanest onboarding hypothesis is stronger than the earlier generic
  “2-3 simple clues” envelope: **2x2 + two simple partial facts** is supported
  for every ordinary variant.

This is capacity evidence, not yet proof that every such authored/generated case
is equally pleasant in blind play.

### Early: XOR is optional richness, not a rescue mechanism

On both 2x3 and 3x2 compact fields:
- simple grammar alone provides unique resolution for **24 / 24** variants with
  at most three clues;
- **21 / 24** variants can already be made unique with only two simple clues;
- adding XOR allows **24 / 24** variants to have a two-clue unique field.

Consequence:
- XOR does not need to be introduced because simple clues fail;
- it can be introduced deliberately as a new reasoning concept on a low-load
  case, then used to make later clue packages shorter / more relational.

### Medium: field orientation is itself a curriculum tool

Under the stricter weak-clue policy, where every individual clue must leave at
least two thirds of the field alive:

For **2x3**:
- simple + XOR does not uniquely solve any variant within 2-3 clues;
- adding forward positive implication still does not produce full unique
  coverage;
- adding forward negative consequents still does not produce full unique
  coverage;
- the **full grammar including reverse implication** provides a unique
  three-clue field for **24 / 24** variants.

For **3x2**:
- simple + XOR likewise does not provide strict unique resolution;
- adding **forward positive implication alone** produces a unique three-clue
  field for **24 / 24** variants.

This asymmetry is useful because reverse-reference clues already have a known
cognitive cost.

Working curriculum consequence:
- when implication is first introduced, prefer a **3 Powder x 2 Fluid** field
  when an equally good candidate surface exists;
- this lets the new concept be taught in the cheaper left-to-right
  Powder -> Fluid direction;
- strict 2x3 cases that require reverse implication are better candidates for a
  later COMBINE beat rather than the first implication lesson.

This is a generator preference, not a hard requirement on every target.

### Late: negative/reverse forms are not required for corpus coverage

On 3x3 fields under the strict weak-clue policy:
- simple + XOR + **forward positive implication** already provides a unique
  three-clue field for **24 / 24** variants.

Consequence:
- negative-consequent and reverse-direction implication remain valuable
  difficulty/variety tools;
- they are not structurally required merely to make the ordinary two-slot
  corpus solvable;
- therefore their introduction can follow the novelty curriculum rather than
  being forced early by edge cases.

## Three-slot tutorial result

The first pass exposed a flaw in the original tutorial screen: requiring only a
small branch count allowed cases where property clues had already reduced the
field to two concrete formulas. Such a puzzle would technically contain the
relation mechanic while not actually needing it.

The tutorial criterion was therefore tightened before acceptance.

### Tight tutorial criterion

A candidate tutorial must:
- use a compact target-containing field;
- use only **simple, already-familiar property clues**;
- leave **2-3** live Powder-Fluid first-stage branches;
- leave at least **3 concrete full formula hypotheses** before the relation
  experiment;
- have a real adjacent pair whose actual result is INCOMPATIBLE and where that
  **single informative experiment** reduces the remaining full hypotheses to at
  most two.

Thus the new STABLE/INCOMPATIBLE concept has required information value rather
than ceremonial presence.

### 2x2x2 passes every ordinary variant

For **19 / 19** ordinary picker-compatible three-slot formula variants there
exists a 2x2x2 field satisfying the strict tutorial criterion.

In every passing variant:
- only **one simple familiar property clue** is needed in at least one valid
  tutorial field;
- the screened field can leave **four concrete formula hypotheses** before the
  relation experiment;
- one informative adjacent incompatibility test can then reduce the hypothesis
  set to at most two.

This is the strongest new result of the pass.

It validates the intended conceptual handoff:

`familiar property reasoning -> several real hypotheses remain -> learn/test one
adjacent chemical relation -> relation materially narrows the problem`.

The three-slot tutorial therefore does **not** need a larger field merely to
make the new relation concept useful.

### Larger compact shapes are fallbacks, not tutorial defaults

The same strict tutorial structure also exists for every variant on the
screened 2x3x2 and 3x2x2 shapes.

However:
- 2x3x2 needed two simple clues in the first passing construction for all 19
  variants;
- 3x2x2 needed one simple clue for 7 variants and two for 12;
- both add visible candidates without solving a corpus-coverage problem that
  2x2x2 already solves.

Therefore 2x2x2 should remain the preferred first three-slot onboarding shape.
Use a larger compact field only when another real constraint later requires it
(for example save-specific identity exposure or a better generated information
trajectory), not merely to make the tutorial look substantial.

## Integration with earlier medium/late evidence

This pass does not replace the already accepted 3x3x3 evidence.

Earlier screens establish:
- every ordinary three-slot output supports a bounded 3x3x3 field inside the
  accepted 2-4 first-stage-branch envelope;
- every output supports a balanced two-weak-fact start;
- 14 / 16 outputs support the stricter progressive three-fact pattern;
- adaptive accumulated relation knowledge remains robust across varied knowledge
  densities and shifts difficult fresh cases toward earned expertise rather than
  hard failure;
- direct, mirrored, mixed and residual-answer topologies have positive blind-play
  evidence.

Together with the new compact tutorial result, the corpus now has evidence for
both ends of the intended ladder:
- a genuinely simple relation-teaching first three-slot puzzle;
- richer bounded 3x3x3 mid/late cases using the full accepted architecture.

## What this screen establishes

The current difficulty curriculum is **structurally viable across the ordinary
corpus**.

In particular:
- the first two-slot lesson can be simpler than Prototype 33: 2x2 + two simple
  partial facts;
- XOR may be taught because it enriches reasoning, not because the corpus forces
  it;
- the first implication lesson has a quantitatively preferred 3x2 orientation
  that avoids reverse-reference cost;
- reverse/negative forms can be reserved for later combination/variety;
- the first three-slot lesson can be 2x2x2 and make exactly one new relation
  concept perform real deductive work;
- larger fields are not inherently “more advanced” and are unnecessary as
  tutorial padding.

## What remains unproved

This is structural/corpus evidence, not a complete difficulty model.

Still open:
- whether the corrected two-slot 2x2 tutorial subjectively feels as clear and
  satisfying as its mathematical structure suggests;
- whether the 2x2x2 three-slot tutorial actually teaches the relation mechanic
  cleanly to the player;
- exact clue wording and presentation;
- exact cadence of INTRODUCE / PRACTICE / COMBINE / BREATHE cases;
- save-specific identity-exposure cost, because this screen does not model the
  player's exact currently known reagent catalog;
- final Science price / wrong-submission feedback / brute-force economics;
- exact numeric thresholds for medium/late difficulty labels.

## Smallest useful next blind validation

Do not blind-test every band.

The corpus has already answered the capacity questions. The next perceptual
uncertainties are concentrated at the two **onboarding boundaries**:

1. corrected two-slot onboarding:
   **2x2 + two simple partial facts, no composite clue**;
2. first three-slot onboarding:
   **2x2x2 + one familiar simple property clue + one genuinely informative
   adjacent relation experiment**.

Testing these two in sequence also measures the most important transfer claim:
whether the player carries the property-constraint language from two-slot into
three-slot so that the relation mechanic can be the single salient novelty.

After those onboarding cases pass, return to generator/progression modeling
rather than exhaustively paper-testing every nominal difficulty band.
