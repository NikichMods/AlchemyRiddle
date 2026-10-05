# Prototype 28 — Composite clue grammar

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base:
- repo: `NikichMods/AlchemyRiddle`
- base main: `31b4559d8dade2e79843469ee605f1c208906215`
- branch: `research/prototype-28-composite-clues`
- production remains **BLOCKED**

## Research question

Can composite target clues — conditional cross-slot rules and exact-one-of-two relations — enrich the accepted bridge+constraint grammar without materially increasing working-memory burden or scope confusion?

This prototype intentionally changes only clue grammar. It does not test residual-answer topology.

## Controls

- field: 3x3x3
- exactly two prior STABLE relations
- zero prior INCOMPATIBLE relations
- mixed anchor orientation retained from an already-accepted topology family
- 8 Research Charges
- adjacent microtest costs 1
- full synthesis costs 0
- Powder+Essence cannot be directly tested
- three-column candidate presentation
- prior/new journal distinction

## Player-facing target

**Реагент увязки**

## Candidate field

### Powders
- P1 **Травяной порошок** — {Растение}
- P2 **Мрачный порошок** — {Труп, Насекомое}
- P3 **Каменный порошок** — {Минерал}

### Liquids
- L1 **Мрачный раствор** — {Труп}
- L2 **Кристальный раствор** — {Минерал}
- L3 **Живой раствор** — {Слизь, Насекомое}

### Essences
- E1 **Густая эссенция** — {Слизь}
- E2 **Сухая эссенция** — {Труп}
- E3 **Зелёная эссенция** — {Растение, Насекомое}

## Target-specific composite constraints

Player-visible:

1. **Если порошок имеет признак «Растение», эссенция должна иметь признак «Слизь».**
2. **Из двух компонентов — раствора и эссенции — признак «Труп» есть ровно у одного.**
3. **Если раствор имеет признак «Минерал», порошок не может иметь признак «Насекомое».**

Semantic notes:
- clue 1 is implication, not biconditional;
- clue 2 is XOR over Liquid/Essence Corpse presence;
- clue 3 is implication with negative consequent.

Do not paraphrase into stronger rules during play.

## Prior laboratory knowledge

Exactly two prior STABLE relations:
- **P2 + L3 -> STABLE**
- **L2 + E2 -> STABLE**

No prior incompatibilities.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> STABLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> INCOMPATIBLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> INCOMPATIBLE
- L2 + E2 -> STABLE
- L2 + E3 -> STABLE
- L3 + E1 -> STABLE
- L3 + E2 -> STABLE
- L3 + E3 -> INCOMPATIBLE

## Hidden target

**P3 + L2 + E2**

## Designed compatible non-target

**P2 + L3 + E2**

Both obey all three target clues and both adjacent relations are stable.

## Target-consistent branch structure

Facilitator-only summary:

Starting bridge **P2+L3**:
- clue 2 requires E2, because L3 lacks Corpse and E2 is the only Essence carrying Corpse;
- clue 1 does not trigger (P2 is not Plant);
- clue 3 does not trigger (L3 is not Mineral);
- L3+E2 is STABLE;
- P2+L3+E2 is compatible non-target.

Starting bridge **L2+E2**:
- clue 2 is already satisfied: L2 lacks Corpse, E2 has Corpse;
- clue 1 excludes P1 because P1 is Plant but E2 lacks Slime;
- clue 3 excludes P2 because L2 is Mineral and P2 carries Insect;
- P3 is the sole target-consistent Powder continuation;
- P3+L2 is STABLE;
- P3+L2+E2 is TARGET.

Thus all three composite clues have an intended material role:
- clue 2 resolves the Essence continuation of the first bridge;
- clue 1 excludes P1 on the second bridge;
- clue 3 excludes P2 on the second bridge.

The answer remains on a starting bridge. Residual-answer topology is intentionally deferred to a later prototype.

## Experiment semantics

Microtests:
- P+L or L+E only
- cost 1
- output STABLE / INCOMPATIBLE

Full synthesis:
- target -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**
- compatible non-target -> **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**
- otherwise -> **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; ПОЛНАЯ УСТОЙЧИВАЯ ЦЕПОЧКА НЕ ПОДТВЕРЖДЕНА.**
- cost 0
- does not silently add unknown pair facts

## Evaluation focus

During play record:
- whether implication direction is understood without rereading;
- whether XOR wording is immediately clear;
- whether the player accidentally treats implication as biconditional;
- whether cross-slot clue scope is easy to retain after digressions;
- whether three composite clues feel richer or mentally heavier than Prototype 27's simple varied clues;
- whether each clue visibly earns its screen presence;
- whether the player still naturally reasons from bridges;
- whether the puzzle remains a 1–3 minute micro-deduction rather than a logic-grid task.

After completion ask:
- did the composite clues feel better, equal, or worse than simple varied clues;
- which clue type was most/least natural;
- whether any wording required active parsing rather than direct reasoning;
- whether this family should be retained broadly, limited to later difficulty, or rejected/revised.

Possible dispositions:
- **COMPOSITE CLUES RETAIN**
- **RETAIN SPARINGLY / LATER DIFFICULTY**
- **SCOPE/Wording REVISE**
- **TOO HEAVY**

# Starting checkpoint

- active prototype: **28**
- Research Charges: **8 / 8**
- prior journal:
  - P2 + L3 -> STABLE
  - L2 + E2 -> STABLE
- no new actions
- awaiting player's first action


## Live checkpoint 1

Player reports that three composite clues shown at once feel dense and more appropriate for a later/high-difficulty investigation than an introductory one.

On the P2+L3 bridge, the player naturally ignores the two implications whose antecedents are false and uses the exact-one-of-two Corpse clue to select E2.

Action: full synthesis P2+L3+E2.
Outcome: compatible chain; target effect absent.
Research Charges: 8/8.

Awaiting next player action.


## Live completion

Player evaluation before final synthesis:
- initial visual impression of three composite clues was intimidating, but actual local reasoning was easier than expected;
- revised difficulty estimate: **mid difficulty**, definitely not introductory, but not necessarily high difficulty;
- player positively values that some hypotheses can be derived directly from clue logic without first spending a microtest;
- do not require every investigation to consume experiments mechanically;
- preserve variety: some investigations may need relation tests, some may yield a plausible synthesis directly from clues and known bridges;
- an immediate first-move successful recipe is acceptable occasionally, but should not become a frequent generator pattern;
- player naturally re-read and self-corrected clue scope while evaluating the second bridge, suggesting the composite grammar remains manageable in practice.

Player reasoning on prior L2+E2:
- clue 1 excludes P1: if Powder is Plant, Essence would need Slime; E2 is not Slime;
- clue 3 excludes P2: L2 is Mineral and P2 carries Insect;
- therefore P3 remains.

Player action:
- full synthesis P3 + L2 + E2.

Outcome:
- **TARGET EFFECT OBTAINED**.

Resources:
- Research Charges used: 0 / 8;
- Research Charges remaining: **8 / 8**;
- full syntheses: 2;
- microtests: 0;
- compatible non-target syntheses: 1;
- successful target syntheses: 1.

Prototype 28 blind play complete.


## Final player evaluation

Disposition: **COMPOSITE CLUES RETAIN**.

Player evaluation:
- all three tested clue families felt natural:
  - implication A -> B;
  - exact-one-of-two / XOR;
  - implication A -> not B;
- no clue family felt intrinsically awkward or confusing;
- composite clues are suitable after the player already understands the basic clue language;
- three composite clues together feel visually dense at first, but in play resolve to roughly medium difficulty because inactive implications can be ignored locally;
- clue-led investigations that require zero microtests are desirable as one valid solution pattern, provided they do not become the dominant meta-pattern.

New presentation/difficulty principle:
- with slot order Powder -> Liquid -> Essence, clue wording that reasons in the same left-to-right direction is cognitively cheaper;
- a clue that begins from a later slot and refers backward to an earlier slot (for example Liquid -> Powder) is not invalid, but it carries extra cognitive cost because it runs against the visual/read order;
- clue direction should therefore be treated as part of the puzzle's difficulty budget;
- easier/mid cases should preferentially use left-to-right relations, while reverse-direction relations can be used deliberately to raise complexity.

Prototype 28 complete. Production remains BLOCKED.
