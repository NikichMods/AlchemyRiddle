# Prototype 18 Facilitator State

**FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY**

Status: precommitted before first player action.

## Purpose

Test **unhappy-path robustness** of the leading adjacent-compatibility core.

Prototype 17 was a happy path:
- one old stable Powder+Liquid edge;
- one natural continuation test;
- continuation was stable;
- first full synthesis succeeded.

Prototype 18 keeps the same simple grammar but makes the tempting branch fail at the second stage. The player should have to revise the hypothesis without falling into pair-matrix completion.

Primary question:
**Does one meaningful negative compatibility result produce satisfying branch revision, or does the loop become tedious/punitive?**

## Spoiler boundary

All reagent names, target facts, compatibility results and hidden formula are fictional.

## Universal player-visible law

A valid 3-component formula is prepared in two stages:

1. Powder + Liquid must form a **STABLE** base.
2. Liquid + Essence must also be **STABLE**.

A microtest mixes one concrete adjacent pair and returns:
- **STABLE**; or
- **INCOMPATIBLE / SEPARATES**.

Compatibility is a reusable empirical fact about the pair, independent of the current target.

Powder–Essence is never tested.

## Candidate pool

Powders:
- P1 Bloom Powder — {Plant}
- P2 Hive Powder — {Insect}

Liquids:
- L1 Nectar Solution — {Plant, Insect}
- L2 Shell Solution — {Insect, Mineral}

Essences:
- E1 Carrion Essence — {Insect, Corpse}
- E2 Stonebone Essence — {Mineral, Corpse}

## Initial target research

The target contains:
- Plant in exactly **one** component;
- Corpse in exactly **one** component;
- Mineral in exactly **one** component.

These facts leave exactly two target hypotheses:

H1:
- P1 Bloom Powder
- L2 Shell Solution
- E1 Carrion Essence

H2:
- P2 Hive Powder
- L1 Nectar Solution
- E2 Stonebone Essence

Do not enumerate these automatically for the player.

## Prior empirical knowledge

Journal contains one old compatibility observation:
- P2 Hive Powder + L1 Nectar Solution -> **STABLE**

This makes H2 the naturally tempting branch.

No Liquid+Essence compatibility is known.
No compatibility involving P1+L2 is known.

## Hidden compatibility table

Powder–Liquid:
- P1 + L1 -> STABLE
- P1 + L2 -> STABLE
- P2 + L1 -> STABLE
- P2 + L2 -> STABLE

Liquid–Essence:
- L1 + E1 -> STABLE
- L1 + E2 -> **INCOMPATIBLE**
- L2 + E1 -> **STABLE**
- L2 + E2 -> STABLE

## Hidden valid answer

P1 Bloom Powder
+ L2 Shell Solution
+ E1 Carrion Essence

## Intended unhappy-path sequence

Natural first hypothesis:
- H2 is attractive because its first edge P2+L1 is already known STABLE.

Most direct continuation test:
- L1 + E2 -> **INCOMPATIBLE**.

This completely falsifies H2 because target facts already make E2 the only Essence compatible with H2's mark counts.

The remaining target hypothesis is H1.

Player may:
- synthesize H1 immediately as a logically forced target hypothesis; or
- spend the second Research Charge testing either P1+L2 or L2+E1.
Both return STABLE.

The final synthesis of H1 succeeds.

## Alternative legal tests

All adjacent pair tests are legal and use the hidden table.

Because the candidate set is intentionally tiny, some suboptimal tests may be weak. Record whether the player feels trapped or punished if they do not choose the intended falsification test.

## Resources

Start with **2 Research Charges**.

Each microtest costs 1.
Full synthesis consumes real selected reagents but no Research Charge.

There is no recharge within the prototype.

## Player-facing journal

Show:
- candidate reagents + provenance marks;
- target facts Plant x1 / Corpse x1 / Mineral x1;
- prior P2+L1 -> STABLE;
- each new raw microtest result;
- remaining charges.

Do not:
- list H1/H2 automatically;
- recommend the continuation test;
- state deductions until the player does.

## Evaluation targets

Record:
- whether the player naturally identifies the tempting H2 branch;
- whether L1+E2 is chosen as a meaningful continuation test;
- emotional/readability response to INCOMPATIBLE;
- whether the negative result feels informative rather than punitive;
- whether the player pivots cleanly to H1;
- whether one extra positive confirmation is desired before synthesis;
- whether resource pressure feels fair;
- overall comparison with Prototype 17 happy path.

## Integrity rule

All target facts, hidden formula, prior observation, compatibility outcomes and resource limits are immutable for the blind run.


## Live checkpoint 1

Player chose Nectar Solution + Stonebone Essence because the known stable Hive Powder + Nectar Solution branch would need Stonebone Essence to satisfy Mineral x1.

Raw outcome: **INCOMPATIBLE / SEPARATES**.

Resources: 1 / 2 Research Charges remain.

No facilitator deduction; await player inference.
