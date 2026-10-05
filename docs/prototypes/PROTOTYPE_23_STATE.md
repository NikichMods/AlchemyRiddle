# Prototype 23 — Compatibility is not identity

**FACILITATOR SPOILERS — DO NOT SURFACE DURING LIVE PLAY**

Status: **precommitted before the player's first action**.

Base research state:
- repository: `NikichMods/AlchemyRiddle`;
- base `main`: `c59e6070236ea39dceee8ac4b4a8c72aef083e08`;
- research branch: `research/prototype-23-compatibility-identity`;
- production architecture remains **BLOCKED**.

## Research-method checkpoint

Exact remaining uncertainty:
- after a player has assembled a fully adjacent-compatible three-component chain,
  can a non-target synthesis be communicated without invalidating the pair facts;
- does that disconfirmation preserve a clear, hypothesis-driven next move;
- does the resulting uncertainty feel like investigation rather than another
  brute-force layer.

Existing evidence:
- Prototype 22 strongly favors the adaptive knowledge-aware architecture over the
  fixed tag-centric baseline in the tested player-facing shape;
- the real three-slot compatibility graph proves adjacent compatibility is not
  formula-equivalent: complete compatibility leaves more chains than authored
  formulas;
- no further host/runtime probe is needed for this cognitive/UI question.

Method:
- one focused adaptive paper prototype is the least-complex adequate test;
- resource scarcity is deliberately removed as the tested variable;
- no production source mutation is permitted.

### Blindness caveat

The player already knows from the preceding discussion that Prototype 23 is
intended to contain a plausible fully compatible non-target chain.

Therefore this prototype **cannot** validly test:
- surprise at discovering compatibility != recipe identity;
- whether an unprimed player would first learn the false heuristic.

It **can** still test:
- whether the actual feedback is legible;
- whether pair knowledge remains trustworthy;
- whether the post-disconfirmation reasoning path is satisfying and bounded.

## Player-visible universal rules

Target: fictional unknown product **Реагент покоя**.

Recipe arity:
- Powder + Liquid + Essence.

Adjacent compatibility:
1. Powder + Liquid can be tested for **СТАБИЛЬНО / НЕСОВМЕСТИМО**.
2. Liquid + Essence can be tested for **СТАБИЛЬНО / НЕСОВМЕСТИМО**.
3. Powder + Essence is not a legal pair test.

Meaning:
- both adjacent stable relations are **necessary** for a viable staged mixture;
- they are **not sufficient** to prove that the triple produces the requested
  target.

Full synthesis outcomes:
- exact target formula -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- non-target triple with both adjacent relations stable ->
  **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**
- any other non-target triple ->
  **ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ; СМЕСЬ НЕ ПОДТВЕРЖДАЕТ ПОЛНУЮ СТАБИЛЬНУЮ ЦЕПОЧКУ.**

A non-target synthesis excludes only that exact triple as the recipe for the
current target. Previously established pair relations remain true.

A full synthesis does not silently add pairwise relation records that were not
already established by microtests/history.

## Resource model

- Research Charges at start: **6 / 6**.
- One adjacent microtest costs **1**.
- Full synthesis costs **0**.
- Six charges are intentionally enough that resource exhaustion should not drive
  the test.
- Candidate reagent quantities are not modeled.

## Candidate pool

### Powders
- P1 **Пепельный порошок** — {Растение, Труп}
- P2 **Белёсый порошок** — {Минерал}
- P3 **Горький порошок** — {Минерал, Труп}

### Liquids
- L1 **Зеленоватый раствор** — {Растение, Минерал}
- L2 **Густой раствор** — {Насекомое, Труп}
- L3 **Бледный раствор** — {Растение, Насекомое}

### Essences
- E1 **Кристальная эссенция** — {Минерал}
- E2 **Сухая эссенция** — {Труп}
- E3 **Тёмная эссенция** — {Насекомое, Труп}

## Target-specific fact

Player-visible:
- **Минерал встречается ровно в одном из трёх компонентов.**

No other target-specific property fact is available at start.

## Prior laboratory knowledge

This is the complete prior-relation set internal to the current 3x3x3 field.
Every listed relation is shown; none is hidden based on target usefulness.

- P1 Пепельный порошок + L1 Зеленоватый раствор -> **СТАБИЛЬНО**
- P3 Горький порошок + L3 Бледный раствор -> **СТАБИЛЬНО**
- P2 Белёсый порошок + L2 Густой раствор -> **СТАБИЛЬНО**
- P2 Белёсый порошок + L3 Бледный раствор -> **НЕСОВМЕСТИМО**
- L2 Густой раствор + E2 Сухая эссенция -> **НЕСОВМЕСТИМО**
- L1 Зеленоватый раствор + E3 Тёмная эссенция -> **НЕСОВМЕСТИМО**
- L3 Бледный раствор + E2 Сухая эссенция -> **НЕСОВМЕСТИМО**

The synthetic history is intentionally constructed to create the focused UX
condition. It is not evidence about how often this exact knowledge shape occurs
in real progression.

## Complete hidden compatibility table

### Powder-Liquid
- P1 + L1 -> STABLE
- P1 + L2 -> INCOMPATIBLE
- P1 + L3 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE
- P2 + L3 -> INCOMPATIBLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

### Liquid-Essence
- L1 + E1 -> STABLE
- L1 + E2 -> STABLE
- L1 + E3 -> INCOMPATIBLE
- L2 + E1 -> STABLE
- L2 + E2 -> INCOMPATIBLE
- L2 + E3 -> INCOMPATIBLE
- L3 + E1 -> STABLE
- L3 + E2 -> INCOMPATIBLE
- L3 + E3 -> STABLE

## Hidden target formula

**P3 Горький порошок + L3 Бледный раствор + E3 Тёмная эссенция**

Synthesis:
- P3 + L3 + E3 -> **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**.

## Designed fully compatible non-target chain

**P1 Пепельный порошок + L1 Зеленоватый раствор + E2 Сухая эссенция**

Facts:
- P1 + L1 is pre-known STABLE;
- L1 + E2 is hidden STABLE until tested;
- the target fact Минерал ×1 is satisfied;
- L1 + E3 is pre-known INCOMPATIBLE;
- E1 would make Минерал ×2 and is target-fact inconsistent.

Thus L1 + E2 is the single target-fact-consistent continuation of the salient
P1 + L1 anchor.

If synthesized:
- output exactly:
  **СВЯЗИ УСТОЙЧИВЫ. ИСКОМЫЙ ЭФФЕКТ ОТСУТСТВУЕТ.**
- journal retains:
  - P1 + L1 STABLE;
  - L1 + E2 STABLE;
- journal additionally records:
  - P1 + L1 + E2 -> **НЕ РЕЦЕПТ «РЕАГЕНТА ПОКОЯ»**.

Do not describe either stable pair as disproved.

## Other structurally viable chain

P1 + L3 + E1 is also fully compatible and satisfies Минерал ×1:
- P1 + L3 -> hidden STABLE;
- L3 + E1 -> hidden STABLE.

This prevents the hidden model from collapsing to only the designed decoy and
target chain.

The adaptive old-knowledge surface nevertheless gives the player a shorter
reasoned route through the two visible stable anchors than through this entirely
unknown chain.

## Expected-but-not-forced path

A likely path is:
1. follow old stable P1 + L1;
2. use Минерал ×1 plus known L1 + E3 incompatibility to identify E2 as its
   only viable continuation;
3. test L1 + E2 -> STABLE;
4. synthesize P1 + L1 + E2 -> compatible non-target;
5. retain both pair facts, exclude the exact triple;
6. pivot to old stable P3 + L3;
7. target fact excludes E1; known L3 + E2 incompatibility excludes E2;
8. test L3 + E3 -> STABLE or infer it as the only continuation, depending on the
   player's standard of evidence;
9. synthesize P3 + L3 + E3 -> SUCCESS.

This path is not to be recommended or narrated to the player. Other legal paths
must resolve from the same precommitted tables.

## Facilitator protocol

At every decision point show:
- all candidates and properties;
- target fact;
- all old and new relation records;
- exact triple-level exclusions learned by synthesis;
- resources;
- legal actions.

Do not:
- enumerate surviving triples;
- identify the designed decoy;
- identify the target;
- derive the player's next inference before they state it;
- reinterpret a pair result after synthesis.

When a compatible non-target synthesis occurs, use the precommitted wording
verbatim enough to preserve these two separate facts:
1. the adjacent links remain stable;
2. this exact triple is not the requested product.

## Starting checkpoint

- active prototype: **23**;
- player-facing state activated in the current chat;
- Research Charges: **6 / 6**;
- no new actions;
- no synthesis exclusions;
- legal next action: any adjacent microtest or any full synthesis;
- awaiting the player's first action.



## Live checkpoint 1-2

The player followed the pre-known P1+L1 stable anchor, applied the single-Mineral target fact, and chose L1+E2 as the only target-consistent untested continuation. The microtest result was STABLE; charges are 5/6.

The player then chose full synthesis P1+L1+E2 because both adjacent links are established STABLE and the triple satisfies the target property constraint.

Deterministic synthesis result: both adjacent links remain STABLE, but the requested target effect is absent. Record the exact triple P1+L1+E2 as NOT the recipe for the current target. Pair facts P1+L1 and L1+E2 remain true. No facilitator deduction has been supplied after the synthesis result.



## Live checkpoint 3

Player evaluation of compatible non-target synthesis:
- wording equivalent to "links are stable; requested effect is absent" was judged immediately clear and conceptually strong;
- player understood that pair knowledge remains valid while the exact triple is rejected;
- presentation may be polished later, but the core distinction compatibility != target identity was successfully communicated.

Player inference:
- P1+L1 branch is exhausted for the current target after the exact P1+L1+E2 triple was rejected and the other continuations are either target-inconsistent or already incompatible;
- player pivoted to the pre-known stable P3+L3 anchor;
- because P3 already contains the single allowed Mineral and L3 contains none, the Essence must add no Mineral.

Player attempted to choose microtest L3+E2.
Protocol intervention:
- L3+E2 is already present in the prior journal as INCOMPATIBLE;
- no Research Charge is consumed and no duplicate experiment is performed;
- this lapse is recorded as UX evidence that seven surfaced prior relation records may exceed comfortable scanability and can cause useful known facts to be overlooked.

Resources remain 5/6.
Awaiting player's next action.



## Live checkpoint 4

Player UX note:
- when a player attempts an already-known pair test, the UI should explicitly
  surface that the result is already in the journal instead of silently doing
  nothing; this preserves clarity and helps recover overlooked knowledge.

Player action:
- microtest L3 Бледный раствор + E3 Тёмная эссенция.

Raw outcome:
- **СТАБИЛЬНО**.

Resources:
- Research Charges remaining: **4 / 6**.

No facilitator deduction supplied.

Current interaction point:
- awaiting player's inference / next action.



## Live completion

Player inference after L3+E3 returned STABLE:
- P3+L3 is known STABLE;
- L3+E3 is now known STABLE;
- the triple satisfies the target fact Mineral x1;
- player therefore chose full synthesis P3+L3+E3.

Deterministic synthesis result:
- **ИСКОМЫЙ ЭФФЕКТ ПОЛУЧЕН**;
- P3+L3+E3 is the recipe for the current target.

Resources:
- Research Charges used: 2 / 6;
- Research Charges remaining: 4 / 6;
- full synthesis attempts: 2;
- compatible non-target syntheses: 1;
- successful target syntheses: 1.

Observed path:
1. Follow pre-known stable P1+L1 anchor.
2. Test L1+E2 -> STABLE.
3. Synthesize P1+L1+E2 -> stable links, target effect absent.
4. Preserve both pair facts and exclude only the exact triple.
5. Pivot to pre-known stable P3+L3 anchor.
6. Attempted L3+E2, but journal already contained INCOMPATIBLE; no charge spent.
7. Test L3+E3 -> STABLE.
8. Synthesize P3+L3+E3 -> target effect obtained.

Prototype 23 player interaction is complete. Await explicit subjective evaluation before assigning final disposition.



## Final player evaluation

Rating: **approximately 4.5 / 5**.

Disposition: **PASS / RETAIN** for the tested adaptive three-slot interaction.

Player experience:
- the prototype was enjoyable, not oppressive, not long and not overextended;
- it required real comparison and thought, but stayed comfortably lightweight;
- the player explicitly liked the resulting loop;
- the compatible-but-non-target synthesis did not feel like a contradiction or
  a broken clue;
- the message equivalent to "links are stable; requested effect is absent" was
  immediately understood and judged a strong conceptual UI result.

Interpretation of residual search:
- the player described the remaining process as technically a form of
  enumeration, but importantly **not blind/brute-force enumeration**;
- the initial evidence first collapses a very large possibility space into a
  small set of theory-supported candidate hypotheses;
- the player then investigates those remaining hypotheses;
- a failed target synthesis is a normal informative research result rather than
  wasted random guessing;
- this bounded hypothesis-checking feels acceptable and appropriately
  alchemical.

Important product-fit conclusion:
- AlchemyRiddle should not optimize for maximum logical sophistication;
- alchemy is one mechanic inside Graveyard Keeper, not a standalone hardcore
  puzzle game;
- the desired investigation should be **atomic**: the player enters the
  mechanic, thinks and experiments for a short bounded period, resolves the
  research without needing to leave, lose context and return later;
- modest cognitive effort is desirable, but excessive working-memory or
  multi-session reasoning is not.

Post-disconfirmation path:
- moving from the compatible non-target chain to the next justified hypothesis
  felt natural;
- the extra uncertainty added satisfying investigation rather than an
  objectionable brute-force layer.

Additional UX evidence:
- seven surfaced prior relation records felt too numerous / easy to overlook;
- one target-property fact felt somewhat sparse;
- a potentially better dosage may use fewer surfaced old relations and somewhat
  richer target-property information;
- attempting a microtest whose outcome is already known should produce an
  explicit "already researched" style response showing the known result and
  consume no resource.

Blindness limitation:
- the player knew in advance that Prototype 23 was designed around a compatible
  non-target chain, so this test does not prove the surprise/teaching effect for
  an unprimed player;
- it does validate the feedback semantics and the post-disconfirmation
  reasoning loop.

Prototype 23 status:
- logically valid;
- facilitator model remained precommitted;
- 2 meaningful new microtests;
- 2 synthesis attempts;
- 1 compatible non-target synthesis;
- 1 successful target synthesis;
- no resource interruption;
- final player evaluation strongly positive.

The compatibility-vs-identity risk exposed by Prototype 22 is therefore
**resolved for the tested interaction shape**.

Production architecture remains **BLOCKED**.
