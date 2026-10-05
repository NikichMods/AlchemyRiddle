# Prototype 21 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test the structured-start finding from Prototype 20R:

**Does a similarly small 3x3x3 reasoning problem feel more interesting when the initial state already contains several intersecting relational facts, without exposing a complete stable chain or effectively pre-solving the target?**

This prototype is not intended to be harder than Prototype 20R. It keeps working-memory demand modest and changes the topology of starting information.

## Research-method checkpoint

Exact unknown:
- whether richer legitimate starting relational structure improves the player's sense of deduction and reduces the feeling of self-directed pair enumeration.

Existing evidence:
- Prototype 16 showed that a complete pre-known adjacent chain over-directs the puzzle;
- Prototypes 17-19 showed that sparse compatibility anchors are useful;
- Prototype 20R showed that a no-anchor state is viable but under-structured.

Why a new blind paper test is justified:
- the uncertainty is experiential/cognitive;
- no runtime probe or host-internals research is needed;
- a controlled paper prototype isolates the starting-information topology directly.

## Universal player-visible law

A valid three-component formula is prepared in two stages:
1. Порошок + Жидкость must be STABLE.
2. Жидкость + Эссенция must be STABLE.

A microtest checks one concrete adjacent pair and returns:
- СТАБИЛЬНО;
- НЕСОВМЕСТИМО.

Compatibility is reusable empirical knowledge about the pair.
Порошок + Эссенция is never tested directly.

## Candidate pool

Порошки:
- P1 Травяной порошок — {Растение}
- P2 Панцирный порошок — {Насекомое}
- P3 Каменный порошок — {Минерал}

Жидкости:
- L1 Медовый раствор — {Растение, Насекомое}
- L2 Солёный раствор — {Насекомое, Минерал}
- L3 Могильный раствор — {Растение, Труп}

Эссенции:
- E1 Тленная эссенция — {Труп}
- E2 Кристальная эссенция — {Растение, Минерал}
- E3 Костяная эссенция — {Минерал, Труп}

## Initial target research

The target contains:
- Растение in exactly one component;
- Труп in exactly one component;
- Минерал in exactly one component.

Applying only these target facts leaves three target-compatible triples:
- P1 + L2 + E1;
- P2 + L1 + E3;
- P3 + L1 + E1.

Do not enumerate these automatically for the player.

## Prior empirical knowledge

The journal already contains three pair observations:
- P2 Панцирный порошок + L1 Медовый раствор -> **СТАБИЛЬНО**;
- P3 Каменный порошок + L1 Медовый раствор -> **НЕСОВМЕСТИМО**;
- L2 Солёный раствор + E1 Тленная эссенция -> **СТАБИЛЬНО**.

These are old reusable compatibility facts, not target-specific clues.

They intentionally create:
- one rejected target-compatible branch;
- one surviving branch with its first-stage edge known stable;
- one surviving branch with its second-stage edge known stable.

No surviving branch has both adjacent edges known.

## Hidden compatibility table

Powder-Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> STABLE
- P1 + L3 -> INCOMPATIBLE
- P2 + L1 -> STABLE
- P2 + L2 -> INCOMPATIBLE
- P2 + L3 -> STABLE
- P3 + L1 -> INCOMPATIBLE
- P3 + L2 -> STABLE
- P3 + L3 -> STABLE

Liquid-Essence:
- L1 + E1 -> STABLE
- L1 + E2 -> STABLE
- L1 + E3 -> INCOMPATIBLE
- L2 + E1 -> STABLE
- L2 + E2 -> INCOMPATIBLE
- L2 + E3 -> STABLE
- L3 + E1 -> INCOMPATIBLE
- L3 + E2 -> STABLE
- L3 + E3 -> STABLE

## Hidden valid answer

P1 Травяной порошок
+ L2 Солёный раствор
+ E1 Тленная эссенция

## Intended logical structure

Target facts leave three target-compatible branches.

Prior compatibility:
- eliminates the P3 + L1 branch;
- partially supports P2 + L1 + E3 via its known stable first edge;
- partially supports P1 + L2 + E1 via its known stable second edge.

Thus two live hypotheses remain, each supported by a different half of the staged compatibility chain.

Missing decisive edges:
- P1 + L2 -> STABLE;
- L1 + E3 -> INCOMPATIBLE.

Either is a natural hypothesis-driven microtest:
- testing P1 + L2 completes the eventual target's stable chain;
- testing L1 + E3 falsifies the competing branch.

The player may then synthesize the surviving/preferred hypothesis or spend the second charge on confirmation.

## Resources

Start with **2 Research Charges**.
Each microtest costs 1.
Full synthesis costs no Research Charge.

## Player-facing journal

Show:
- all candidates and property marks;
- target facts Растение ×1 / Труп ×1 / Минерал ×1;
- all three prior pair observations;
- new raw pair outcomes;
- remaining charges.

Do not:
- enumerate the three target-compatible triples;
- state which prior fact eliminates/supports which target hypothesis;
- show a compatibility matrix;
- recommend a next pair;
- infer deductions after a new result before the player does.

## Evaluation targets

Record:
- whether the starting state feels more interesting than Prototype 20R;
- whether the three prior pair facts feel like useful structure rather than answer disclosure;
- whether the player notices interactions between target properties and old pair knowledge;
- whether the first new experiment feels chosen for a reason;
- whether the player experiences the two half-supported branches as a satisfying comparison;
- whether the puzzle feels easier, harder, or simply better-shaped;
- whether any starting fact feels redundant or too directive;
- overall subjective rating relative to Prototypes 18-20R.

## Integrity rule

All target facts, candidate properties, prior observations, hidden compatibility outcomes, formula and resource limits are immutable for the blind run.

## Live activation checkpoint

Status: active blind play; awaiting the player's first action.

Current state:
- candidate pool: 3x3x3 above;
- target facts: Растение ×1, Труп ×1, Минерал ×1;
- prior pair observations: 3;
- Research Charges: 2/2;
- completed new microtests: none;
- legal next action: any adjacent pair microtest or full synthesis.


## Live checkpoint 1

Player observation before the first microtest:
- noticed that differing Research Charge budgets across prototypes can itself act as meta-information about expected solve length;
- explicitly asked not to treat that as the main issue for this run.

Player reasoning before the first microtest:
- considered the known stable P2 Панцирный порошок + L1 Медовый раствор edge;
- applied the target facts and identified E3 Костяная эссенция as a natural continuation because L1 supplies Растение, while E3 supplies Минерал + Труп;
- chose to test whether L1 + E3 is stable.

Player action:
- microtest L1 Медовый раствор + E3 Костяная эссенция.

Raw outcome: **INCOMPATIBLE / НЕСОВМЕСТИМО**.

Resources:
- Research Charges remaining: **1 / 2**.

No facilitator deduction from the fresh result. Await player inference / next action.


## Live checkpoint 2

Player inference after the first new microtest:
- rejected the obvious continuation of the known stable P2 + L1 branch after L1 + E3 returned INCOMPATIBLE;
- shifted attention to the other pre-known stable relation L2 + E1;
- reasoned that L2 + E1 together already supply Минерал + Труп, leaving Растение as the remaining target property;
- identified P1 Травяной порошок as the natural Powder candidate for that role;
- chose to test P1 + L2.

Player action:
- microtest P1 Травяной порошок + L2 Солёный раствор.

Raw outcome: **STABLE / СТАБИЛЬНО**.

Resources:
- Research Charges remaining: **0 / 2**.

No facilitator deduction from the fresh result. Await player inference / final action.
