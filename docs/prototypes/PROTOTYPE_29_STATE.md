# Prototype 29 — Residual-answer topology

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: **precommitted before the player's first action**.

Base:
- repo: `NikichMods/AlchemyRiddle`
- base main: `d08c5d627cea8fe845b7bad9b056af2caa990633`
- branch: `research/prototype-29-residual-answer`
- production remains **BLOCKED**

## Research question

Can the accepted bridge+constraint grammar support a target recipe that lies on **none of the starting stable bridges**, while still giving the player a short deductive path rather than dumping them into post-bridge enumeration?

Success condition:
- starting bridges are genuinely useful, not fake bait;
- each starting bridge corresponds to a real target-consistent hypothesis;
- closing those hypotheses materially shrinks the solution space;
- after both are ruled out, exactly one target-consistent residual formula remains;
- the residual answer can be articulated as a consequence of prior evidence rather than guessed from the untested remainder.

This prototype changes topology only. It intentionally keeps clue grammar moderate and familiar.

## Controls

- 3x3x3 field
- exactly two prior STABLE relations
- zero prior INCOMPATIBLE relations
- mixed anchor orientation from an already-accepted topology family
- 8 Research Charges
- adjacent microtest costs 1
- full synthesis costs 0
- Powder+Essence cannot be directly tested
- three-column candidate presentation
- prior/new journal distinction
- no new experiment feedback semantics

## Player-facing target

**Реагент расхождения**

## Candidate field

### Powders
- P1 **Студенистый порошок** — {Слизь}
- P2 **Пыльцевой порошок** — {Растение, Насекомое}
- P3 **Сумрачный порошок** — {Труп}

### Liquids
- L1 **Зелёный раствор** — {Растение}
- L2 **Мёртвый раствор** — {Труп}
- L3 **Каменный раствор** — {Минерал, Насекомое}

### Essences
- E1 **Кристальная эссенция** — {Минерал}
- E2 **Живая эссенция** — {Растение}
- E3 **Вязкая эссенция** — {Слизь, Насекомое}

## Target-specific constraints

Player-visible:

1. **Слизь не встречается ни в одном компоненте.**
2. **Растение встречается ровно в одном компоненте.**
3. **Из двух компонентов — порошка и раствора — признак «Труп» есть ровно у одного.**

These are intentionally simpler than Prototype 28. The prototype isolates residual topology.

## Prior laboratory knowledge

Exactly two prior STABLE relations:
- **P2 + L2 -> STABLE**
- **L1 + E1 -> STABLE**

No prior incompatibilities.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> INCOMPATIBLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> INCOMPATIBLE
- P2 + L2 -> STABLE
- P2 + L3 -> INCOMPATIBLE
- P3 + L1 -> STABLE
- P3 + L2 -> INCOMPATIBLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> INCOMPATIBLE
- L1 + E3 -> STABLE
- L2 + E1 -> STABLE
- L2 + E2 -> INCOMPATIBLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden target

**P3 + L3 + E2**

This target uses neither starting stable relation.

## Designed target-consistent candidate set

The three target constraints admit exactly three triples:

1. **P2 + L2 + E1**
   - contains prior bridge P2+L2;
   - both adjacent links are STABLE;
   - compatible non-target.

2. **P3 + L1 + E1**
   - contains prior bridge L1+E1;
   - both adjacent links are STABLE;
   - compatible non-target.

3. **P3 + L3 + E2**
   - contains neither prior bridge;
   - both adjacent links are STABLE;
   - TARGET.

No other triple satisfies all three target constraints.

## Intended deduction topology

The player can start from either prior bridge.

### Starting bridge P2+L2
- P2 carries Plant; L2 carries Corpse.
- Slime absence is already satisfied.
- Plant exactly once means Essence cannot carry Plant.
- E3 is excluded by Slime.
- Therefore E1 is the unique target-consistent continuation.
- P2+L2+E1 is a fully stable compatible non-target.

### Starting bridge L1+E1
- L1 carries Plant; E1 carries Mineral.
- Slime absence excludes P1 and E3.
- Plant exactly once excludes P2 because P2 also carries Plant.
- P3 is the unique target-consistent Powder.
- P3+L1+E1 is a fully stable compatible non-target.

### Residual deduction
After those two target-consistent formulas are ruled out:
- P1 and E3 remain globally impossible because Slime is forbidden;
- remaining Powder cases:
  - P2 implies L2 by the Powder/Liquid Corpse-XOR and then E1 by the Plant-count rule -> already ruled out;
  - P3 can pair with L1 or L3:
    - L1 implies E1 -> already ruled out;
    - therefore the only unruled target-consistent case is **P3+L3+E2**.
- This is intended to feel like a residual proof, not a blind search.

The player may synthesize the residual triple immediately or verify adjacent relations first. Both are acceptable.

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
- whether the player automatically assumes the answer must be on a starting bridge;
- whether each bridge feels useful after it fails;
- whether two failed bridge hypotheses naturally prompt a global re-read of the clue space;
- whether the residual candidate feels **deduced** or merely **the only thing left to try**;
- whether the player can articulate why the residual triple is uniquely target-consistent;
- whether the player feels a need to enumerate unseen branches;
- working-memory burden after the second bridge closes;
- whether prior/new journal state supports the transition.

After completion ask:
- did “answer outside bridges” feel fair;
- did bridge failures feel productive or like bait;
- did the final residual branch produce an “aha” or an anticlimax;
- should off-bridge targets be medium/high-difficulty variety, or common enough to prevent meta-learning;
- whether two bridges were enough, or a later case should test three.

Possible dispositions:
- **RESIDUAL ANSWER RETAIN**
- **RETAIN SPARINGLY / LATER DIFFICULTY**
- **BRIDGES FEEL LIKE BAIT**
- **POST-BRIDGE ENUMERATION RETURNED**
- **RESIDUAL TOO OBVIOUS / REVISE**

# Starting checkpoint

- active prototype: **29**
- Research Charges: **8 / 8**
- prior journal:
  - P2 + L2 -> STABLE
  - L1 + E1 -> STABLE
- no new actions
- awaiting player's first action


## Live checkpoint 1 — fast-forwarded bridge resolution

Player explicitly fast-forwards through the two starting bridges and asks for the resulting journal/state.

Design observation:
- a prior STABLE bridge could itself already violate one of the target-specific clues and therefore be immediately irrelevant to the current target;
- this is a potentially useful topology variant;
- risk: players may conflate STABLE with “belongs to the target recipe,” so future presentation must keep chemical compatibility distinct from target relevance.

Bridge 1 reasoning:
- prior P2+L2 is STABLE;
- Slime absence excludes E3;
- P2 already supplies the single allowed Plant, so E2 is excluded;
- only E1 remains target-consistent.
Player action sequence:
- microtest L2+E1 -> STABLE;
- full synthesis P2+L2+E1 -> compatible non-target.
Charges after microtest: 7/8.

Bridge 2 reasoning:
- prior L1+E1 is STABLE;
- L1 already supplies the single allowed Plant;
- P1 is excluded by Slime absence;
- P2 is excluded because it would add a second Plant;
- P3 satisfies the Powder/Liquid Corpse XOR with L1.
Player action:
- full synthesis P3+L1+E1 -> compatible non-target.
Charges remain: 7/8.

Journal after the fast-forward:
- [Prior] P2+L2 -> STABLE
- [Prior] L1+E1 -> STABLE
- [New] L2+E1 -> STABLE
- P2+L2+E1 -> not target
- P3+L1+E1 -> not target

Important protocol note:
- full synthesis outcomes do not silently create separate pair facts, so P3+L1 is not added as an independently established journal relation.

Current interaction point:
- both starting bridge hypotheses are closed as compatible non-targets;
- Research Charges: 7/8;
- awaiting player's residual deduction / next action.


## Live completion

Player UX observation before final synthesis:
- seeing logically impossible candidates visually struck out was strongly positive;
- player suggests optional manual annotation such as strike-through / exclusion marking could support external memory and active deduction;
- this is a UI hypothesis only; implementation cost and ownership are not yet researched.

Residual reasoning:
- P1 and E3 are eliminated by Slime absence;
- the two bridge-based target-consistent hypotheses P2+L2+E1 and P3+L1+E1 were already ruled out by full synthesis;
- the player identifies the remaining off-bridge candidate P3+L3+E2 and chooses to synthesize it directly.

Player action:
- full synthesis P3 + L3 + E2.

Outcome:
- **TARGET EFFECT OBTAINED**.

Resources:
- Research Charges used: 1 / 8;
- Research Charges remaining: **7 / 8**;
- microtests: 1;
- full syntheses: 3;
- compatible non-target syntheses: 2;
- successful target syntheses: 1.

Prototype 29 blind play complete.
