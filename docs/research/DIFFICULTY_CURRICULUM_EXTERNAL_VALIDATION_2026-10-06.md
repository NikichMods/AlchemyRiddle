# Difficulty Curriculum External Validation — 2026-10-06

Status: **external design-research evidence; no production architecture mutation**.

Purpose: independently stress-test the post-Prototype-33 difficulty-curriculum proposal against established learning research and published puzzle/deduction-game design practice. This note does not replace the canonical product decisions in `docs/PRODUCT_REQUIREMENTS.md` or the current recovery state in `docs/DESIGN_RESEARCH.md`.

## Question

Does the proposed AlchemyRiddle difficulty model have a sound external basis?

Current proposal under review:
- separate two-slot and three-slot difficulty ladders;
- curriculum bands (tutorial / early / medium / late / boss) rather than one global chronology;
- difficulty treated as multidimensional rather than as field size or clue count alone;
- later difficulty primarily from interaction among known ideas rather than raw search-space inflation;
- three-slot onboarding adds the relation layer on top of concepts learned in two-slot;
- theoretical-new-identity exposure is a cost/penalty rather than a hard readiness gate;
- informative experiments are allowed to vary in count, including zero where existing evidence is already sufficient.

## External evidence

### 1. Cognitive-load research: complexity depends on interacting elements and expertise

Sweller, van Merriënboer, and Paas' review of Cognitive Load Theory emphasizes **element interactivity**: difficulty depends on how many pieces of information must be processed together, not simply on the raw number of visible elements. The same task also becomes effectively less complex as the learner acquires schemas that package several elements into one. The review also describes **expertise reversal** and **guidance fading**: support useful to novices can become redundant or counterproductive as expertise increases.

Source:
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019), "Cognitive Architecture and Instructional Design: 20 Years Later", Educational Psychology Review.
  https://link.springer.com/article/10.1007/s10648-019-09465-5

Relevant consequence for AlchemyRiddle:
- do **not** reduce difficulty to field size, clue count, or one additive score;
- the same clue form has different cost before and after the player has learned it;
- a 2x2 puzzle with several interacting conditional clues can legitimately be harder than a larger field with simpler relations;
- generator evaluation must include player expertise / previously learned clue families.

This strongly supports the Prototype-33 observation that small field size alone does not make a tutorial.

### 2. New ideas should be introduced under reduced surrounding load, then combined later

The same cognitive-load literature supports part-to-whole sequencing and fading of guidance: initially reduce the number/interactivity of concepts, then add interactions as competence grows.

A practical puzzle-design analogue appears repeatedly in published design writing:
- early puzzles teach one mechanic in a simple context;
- later puzzles combine already-learned mechanics;
- introducing a new mechanic is a reason to temporarily lower surrounding puzzle difficulty rather than increase every axis monotonically.

Sources:
- Sweller et al. (2019), above.
- Damien Allan, "Designing Video Game Puzzles", Game Developer (2017):
  https://www.gamedeveloper.com/design/designing-video-game-puzzles
- "Simple mechanics, complex puzzle creation — Part 3: Fun challenges", Game Developer:
  https://www.gamedeveloper.com/design/simple-mechanics-complex-puzzle-creation-part-3-fun-challenges

The Game Developer puzzle-design article explicitly warns against forcing a perfectly steady difficulty curve and recommends giving the player a breather when introducing a new mechanic.

Relevant consequence:
- the curriculum should be **wave-shaped**, not monotonically harder on every dimension;
- introduce a new clue/relation family in a deliberately easier investigation;
- only after the player has demonstrated that concept should later investigations combine it with existing concepts under higher load.

### 3. The Witness: teach rule families separately, combine mastered ideas later

Published discussion of *The Witness* describes early puzzle sequences as teaching how a rule works and later puzzles adding elements and increasing difficulty. Jonathan Blow describes designing around what is happening in the player's head, and the game's structure repeatedly uses simple sequences to teach concepts before more difficult combinations.

Sources:
- "Bearing Witness / Designing the Puzzles of The Witness", Game Developer:
  https://www.gamedeveloper.com/business/bearing-i-witness-i-
- "Feature: Jonathan Blow On Designing The Witness", Game Developer:
  https://www.gamedeveloper.com/design/feature-jonathan-blow-on-designing-i-the-witness-i-

Relevant consequence:
- AlchemyRiddle's two-slot ladder can teach the shared logical vocabulary;
- the first three-slot investigation should **not** re-teach everything at higher difficulty;
- it should keep familiar property logic easy and introduce one genuinely new concept: adjacent STABLE / INCOMPATIBLE relations;
- later three-slot investigations may then combine that relation grammar with richer clue logic.

This supports independent arity onboarding plus cross-arity transfer.

### 4. Desirable difficulty: harder is useful only when it serves learning

Bjork's "desirable difficulties" work distinguishes difficulty that improves retention/transfer from difficulty that merely impairs immediate performance. Interleaving and variation can improve learning, but combinations of individually useful difficulties are not automatically additive; too many together can become counterproductive.

Sources:
- Bjork Learning and Forgetting Lab, "Research — Desirable Difficulties":
  https://bjorklab.psych.ucla.edu/research/
- R. Bjork & E. Bjork, "Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning":
  https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/RBjork_inpress.pdf

Relevant consequence:
- "boss" difficulty should not mean maximizing field size + clue complexity + relation density + unfamiliar identities simultaneously;
- late difficulty should be produced by carefully selected interactions among mastered concepts;
- independent two-slot / three-slot ladders may interleave in play, but new concepts should still receive local onboarding rather than assuming transfer that has not occurred.

### 5. Outer Wilds: knowledge is progression; external memory is part of the design

The *Outer Wilds* team explicitly designed progression around player knowledge rather than avatar upgrades. Their paper-prototype work found that testers naturally wrote discoveries down, which directly reinforced the need for the ship computer to preserve learned information. The team also reported that curiosity about a new fact depends on sufficient familiarity with the surrounding context; if everything is new, a specific novelty is not salient.

Sources:
- "Live, die, repeat: How Outer Wilds piques curiosity...", Game Developer:
  https://www.gamedeveloper.com/design/live-die-repeat-how-i-outer-wilds-i-piques-curiosity-in-an-ambivalent-solar-system
- "Demaking Outer Wilds", Game Developer:
  https://www.gamedeveloper.com/design/demaking-outer-wilds

Relevant consequence:
- AlchemyRiddle is correct to treat accumulated reagent/relation knowledge as real progression;
- the journal/compendium is not merely convenience UI: external memory is part of making a knowledge-driven game cognitively tractable;
- early investigations should minimize unnecessary simultaneous exposure to unfamiliar reagent identities;
- theoretical-new-identity exposure should remain a soft generator cost, especially at onboarding/early stages.

### 6. Deduction games confirm the danger of a free answer oracle

Lucas Pope documented the *Return of the Obra Dinn* validation problem directly: immediate per-answer correctness feedback made exhaustive guessing trivial, while withholding all feedback until the end felt unsatisfying. His solution was to validate correct fates in groups rather than individually.

*The Case of the Golden Idol* developers describe the same fundamental problem: constrained answer entry makes brute force possible, so they avoided validating every field independently and settled on coarser feedback.

Sources:
- Lucas Pope, Obra Dinn development log, "Fate Validation" (2017):
  https://dukope.com/devlogs/obra-dinn/tig-30/
- "Pursuing the 'Aha!' moment with deductive reasoning game The Case of the Golden Idol", Game Developer:
  https://www.gamedeveloper.com/design/case-of-the-golden-idol

Relevant consequence:
- AlchemyRiddle's existing rule "no free unlimited success/failure confirmation" is strongly externally supported;
- however, **1 Science per submission is not validated by these examples**. A price is one possible anti-bruteforce mechanism, not automatically the correct one;
- later economy work must test whether the price makes blind enumeration unattractive without punishing an honest reasoned hypothesis excessively;
- exact wrong-answer feedback remains a significant design lever.

### 7. Turing Machine and Alchemists corroborate the core information-game shape

*Turing Machine* explicitly presents a deduction game built around asking bounded questions of verifiers and advertises problems ranging from simple to very complex. Its official material includes introductory problems for new players and more challenging modes that alter the structure/ambiguity of verification rather than merely enlarging a board.

*Alchemists* uses experiments to obtain partial information about hidden properties and supplies a deduction grid as persistent external reasoning support.

Sources:
- Turing Machine official page:
  https://www.scorpionmasque.com/en/turingmachine
- Alchemists official rules:
  https://alchemists.czechgames.com/rules/

Relevant consequence:
- bounded information-producing actions plus persistent external notation are established, legible deduction-game primitives;
- AlchemyRiddle's experiments should remain information actions, not ritual actions;
- forcing a minimum experiment count for every puzzle is unnecessary.

## Stress-test result

The proposed curriculum survives the external comparison. No evidence found suggests replacing the current two-slot or three-slot core architectures.

Three refinements should be carried into the next curriculum pass:

### A. Add an explicit novelty budget

Track not only clue complexity but **how many rule/concept families are new to this player in this investigation**.

Working direction:
- tutorial: introduce at most one genuinely new reasoning concept at a time;
- when a concept is new, keep field size / clue interaction / relation topology below the normal band ceiling;
- once learned, the same concept becomes cheaper and may be combined with others.

Cross-arity implication:
- property/count/XOR/conditional concepts learned in two-slot reduce their novelty cost in three-slot;
- adjacent compatibility remains a new concept and deserves its own low-load introduction.

### B. Replace a monotonic curve with alternating learning and challenge beats

A difficulty band is an envelope, not an obligation for every next puzzle to dominate the previous puzzle on every axis.

Within and between bands:
1. introduce a new concept under reduced load;
2. give one or more normal uses;
3. combine it with previously learned concepts;
4. occasionally provide a lower-load breather before the next conceptual escalation.

The player's sense of increasing mastery should come from handling richer combinations, not from every puzzle being strictly harder than the last.

### C. Track brute-force attractiveness separately from nominal puzzle difficulty

Formula submission is an oracle. The later generator/economy design should explicitly evaluate:
- number of clue-consistent candidates before submission;
- cost of one wrong submission;
- number of submissions a resource-rich player can afford;
- information revealed by a wrong submission;
- whether blind sequential guessing is ever cheaper/easier than the intended reasoning path.

Do not assume a fixed Science price solves this automatically.

## Current judgement

External evidence **strengthens** the current architecture rather than undermining it.

Most strongly supported parts:
- multidimensional difficulty;
- field size as only one contributor;
- separate onboarding for the two arities;
- cross-arity transfer of mastered concepts;
- difficulty growth through interaction among known ideas;
- persistent journal/compendium;
- limiting unnecessary novelty early;
- preventing free high-resolution answer validation.

Primary correction:
- make **novelty relative to player expertise** a first-class budget;
- make the difficulty curve intentionally non-monotonic at concept-introduction points.

No runtime test is required for this external validation pass.
