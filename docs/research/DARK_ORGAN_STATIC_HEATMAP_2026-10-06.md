# Dark + Organ static heatmap — 2026-10-06

Status: bounded sanity-check complete. No new tag proposal. Production remains BLOCKED.

## Question

After Dark + Organ, is there still a broad signature/card-density problem that
justifies another taxonomy pass?

This is a static check only. Similarity is measured within the same reagent role.

## Result

Working distribution:
- 1 property: 12
- 2 properties: 11
- 3 properties: 8
- 4 properties: 4

| Role | Cards | Distinct signatures | Cards in exact-duplicate groups |
|---|---:|---:|---:|
| Powder | 15 | 12 | 5 |
| Fluid | 8 | 8 | 0 |
| Essence | 8 | 6 | 4 |
| Universal | 4 | 4 | 0 |

Only 9 of 35 cards remain in a same-role exact-duplicate group.

The four residual duplicate groups are:
- Powder: three cards with Mineral only;
- Powder: two cards with Corpse only;
- Essence: two cards with Insect only;
- Essence: two cards with Plant + Slime.

Density concentration:
- one-property cards: 12 total, 7 in duplicate groups;
- two-property cards: 11 total, 2 in a duplicate group;
- three-property cards: 8 total, all unique in-role;
- four-property cards: 4 total, all unique in-role.

Fluid and Universal cards are completely unique by visible signature.

Close but non-identical subset/superset pairs remain, but these are not treated
as defects because they preserve at least one discriminator and can support
useful deduction.

## Interpretation

There is no broad remaining taxonomy problem. Residual duplication is local and
concentrated in intentionally simple cards.

Recommendation:
- do not search for a third broad tag merely to remove these four clusters;
- treat Dark + Organ as provisionally sufficient;
- reopen only if blind play or sequence generation shows a concrete stale-repeat
  problem, or if another strong broad short world-grounded tag appears
  independently.

A synthetic split test of the four residual groups is not justified by this
sanity-check alone.

No runtime test is required.
