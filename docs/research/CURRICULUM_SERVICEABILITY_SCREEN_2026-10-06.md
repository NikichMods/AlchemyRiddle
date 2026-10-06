# Curriculum serviceability screen — 2026-10-06

Status: **accepted bounded quantitative research; production remains BLOCKED**.

## Question

The player chooses the alchemy target. The curriculum separately wants to control
what kind of reasoning is introduced or practised next.

The concrete risk was:

> Can a player-selected formula variant fail to support the curriculum beat we
> want next, forcing either a bad puzzle or a deferred lesson?

This screen isolates **formula-identity serviceability**. It does not yet model
every dynamic save-state restriction.

## Method

Research helper:
`research/TagModelScreen/curriculum_serviceability_screen.py`.

The exact vanilla formula rows remain private/ephemeral. The named private
working corpus was reconstructed from previously accepted runtime evidence and
validated before this screen.

Three-slot reconstruction reproduced the complete accepted ordinary baseline
exactly:

- 19 formula variants;
- 16 outputs;
- 10 Powder-role candidates;
- 9 Fluid-role candidates;
- 9 Essence-role candidates;
- 810 Cartesian triples;
- 19 stable Powder-Fluid edges;
- 18 stable Fluid-Essence edges;
- 47 fully compatible chains.

The current accepted **Dark + Organ** property model was used.

### Two-slot serviceability contract

Scope:
- mandatory progression core only: 16 formula variants / 10 outputs;
- candidate identity pool deliberately restricted to identities present in that
  mandatory core: 12 first-role / 9 second-role identities;
- therefore this is a conservative lower bound relative to the previously
  established larger ordinary two-slot participant pool.

For each target, every 2x2 field containing the true pair was tested.

A curriculum-introduction package:
- uses 2-3 individually partial clues under the accepted compact weakness rule;
- contains exactly one clue from the concept being introduced;
- uses only already-earlier concept families as support;
- every clue is necessary;
- resolves to one unique pair.

Tested introductions:
- XOR;
- forward positive implication;
- forward negative-consequent implication;
- reverse implication direction.

A BREATHE/control package uses only familiar literal/count facts.

### Three-slot relation-introduction contract

Every 2x2x2 field containing the true formula was tested.

A retained first-relation tutorial surface:
- uses exactly two familiar literal/count clues;
- each clue alone leaves 3-7 of 8 triples;
- together they leave exactly two live hypotheses;
- those hypotheses differ only in Powder or Essence while the middle Liquid is
  fixed;
- one adjacent relation test can eliminate the non-target continuation because
  its edge is INCOMPATIBLE while the true edge is STABLE.

This intentionally mirrors the player-accepted Prototype 35 shape.

Later three-slot logical-family capacity reuses the accepted
`reasoning_diversity_screen.py` option model.

## Result 1 — target identity does not block the tested two-slot curriculum

All **16 / 16** mandatory two-slot formula variants can support every tested
low-load beat on a 2x2 field.

Serviceable 2x2 field rate by target variant:

| Beat / introduced concept | Variants | Minimum | Median | Mean |
|---|---:|---:|---:|---:|
| BREATHE / simple facts | 16/16 | 90.9% | 100% | 98.3% |
| XOR | 16/16 | 90.9% | 100% | 98.3% |
| Forward positive implication | 16/16 | 62.5% | 95.5% | 89.1% |
| Forward negative-consequent implication | 16/16 | 56.8% | 100% | 91.5% |
| Reverse implication direction | 16/16 | 90.9% | 100% | 98.3% |

This is stronger than merely finding one lucky field per recipe. Even the
weakest tested concept/target combination has many valid 2x2 surfaces under the
accepted compact envelope.

Because the candidate pool is intentionally narrower than the full ordinary
two-slot pool, adding legitimate extra candidate identities can only increase
the available surface reserve; it is not needed for this PASS.

## Result 2 — over-constraining clue symmetry creates artificial failures

A sensitivity control added a rule that is **not** part of the accepted
curriculum:

> every individual clue in a 2x2 field must split the four pairs exactly 2/2.

Under that extra restriction:
- XOR still works for 16/16 targets;
- forward positive implication falls to 15/16;
- forward negative implication falls to 15/16;
- reverse implication falls to 13/16.

Interpretation:

The corpus itself is not the bottleneck. A scheduler can manufacture
serviceability conflicts by imposing unnecessarily rigid aesthetic/strength
rules.

Keep the accepted **bounded envelope** rather than demanding identical clue
partitions.

## Result 3 — any ordinary three-slot target can carry the first relation lesson

All **19 / 19** ordinary three-slot formula variants support a Prototype-35-like
2x2x2 relation-introduction puzzle.

Across target variants, the fraction of all 2x2x2 surfaces that support that
shape is:
- minimum **79.2%**;
- median **88.9%**;
- mean **91.2%**;
- maximum **100%**.

Orientation detail:
- a Fluid-Essence purposeful tutorial path exists for **19 / 19** variants;
- a Powder-Fluid path exists for **12 / 19** variants.

Therefore the first three-slot target does **not** need to be preselected by the
mod merely to teach adjacent STABLE / INCOMPATIBLE relations.

If a single tutorial orientation is desirable, Fluid-Essence is structurally
universal under this bounded screen. That is an available simplification, not
yet a required UX decision.

## Result 4 — later three-slot logical families are not target-gated either

Using the existing accepted 3x3x3 retained-option model, every one of the
19 ordinary three-slot formula variants has valid options containing each major
shared logical family:
- literal;
- exact count;
- XOR;
- positive implication;
- negative-consequent implication.

The reserve is large rather than marginal. The sampled minimum retained-option
count per target was in the hundreds for every family.

This is consistent with the previous reasoning-diversity result: the corpus has
ample logical-family capacity and accidental repetition is a scheduling problem,
not a formula-capacity problem.

## Generator consequence

The feared primary conflict:

`player chose recipe X -> X cannot carry the next curriculum concept`

is **not observed** for the tested core curriculum.

Therefore do **not** build a complicated scheduler whose normal job is to wait
for a "compatible" future recipe before it can teach the next concept.

Prefer the simpler policy:

1. the player selects the target;
2. the selected arity's independent curriculum state chooses the desired beat;
3. the generator searches only puzzle candidates for that selected target;
4. hard validity / anti-bruteforce / novelty limits apply first;
5. curriculum fit and anti-repeat then choose among valid candidates;
6. if the desired beat is genuinely infeasible in the player's actual current
   state, gracefully fall back to a mastered PRACTICE / COMBINE / BREATHE shape
   and keep the pending introduction for later.

The fallback remains important because actual save state can still restrict
serviceability through:
- progression-limited known identities;
- accumulated learned relations that over-resolve a field;
- future relation-topology concepts not covered by this screen.

But it is a **guardrail**, not the expected normal path caused by formula
identity.

## What this closes

Closed for now:
- no target recipe needs to be reserved for XOR / implication introduction;
- no special first three-slot target needs to be reserved for the basic relation
  lesson;
- the scheduler does not need a target-selection layer merely to satisfy the
  curriculum;
- free player target choice is compatible with the current curriculum model at
  the formula-identity level.

Still open:
- exact INTRODUCE / PRACTICE / COMBINE / BREATHE cadence;
- exact rule for when a concept becomes familiar/mastered;
- dynamic fallback frequency under progression-limited knowledge and accumulated
  relation history;
- later three-slot bridge/residual-topology introduction policy.

## Next highest-leverage generator question

With target-serviceability no longer a primary blocker, the next generator
parameter to define should be the **smallest curriculum state machine**:

- what state is stored per independent two-slot / three-slot ladder;
- what shared concept familiarity transfers across arities;
- when INTRODUCE becomes PRACTICE/mastered;
- when COMBINE and BREATHE are selected without turning the wave-shaped
  curriculum into a rigid four-step metronome.

No installed-runtime test is required for this result.
