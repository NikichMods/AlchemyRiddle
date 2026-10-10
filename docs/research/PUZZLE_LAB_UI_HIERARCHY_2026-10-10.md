# Puzzle Lab hierarchy and answer-order proposal — 2026-10-10

Status: user selected the recommended workbench and soft presentation-order preparation; implemented in the research Lab. Production remains blocked.
The user rejects the implemented three-column mockup grouping because it loses
hierarchy. Elimination dim/dashed behavior and pair deselection are accepted;
the elimination control must be a slashed circle, superseding the first cross.

## Recommended workbench

Keep composition conditions directly above the large candidate board. Give this
area the strongest hierarchy. A single adjacent compatibility investigation
area owns both current powder/liquid and liquid/essence pairs, their check
buttons, and accumulated prior/earned observations. Separate current controls
from quieter history inside that same area, not across distant panels. Place a
compact selected formula and final synthesis action after that investigation.
Clues remain visible while experimenting; no locked wizard and no automatic
elimination or inference. This presents read -> choose -> investigate -> revise
-> synthesize as an available loop, not compulsory paid checks.

Alternative: vertically stacked composition/selection, investigation, synthesis
sections, all open. Clear reading order and responsive behavior, but more scroll
and weaker simultaneous comparison. A full pair matrix is a possible secondary
view; avoid making two matrices the default focus for this small field.

## Selected-pair feedback proposal

Only public knownRelations may drive compatibility color. Unknown is neutral;
known compatible is green/check; known incompatible is red/slashed-circle.
An incomplete pair has no compatibility verdict. Keep selection distinguishable
from knowledge, and accompany color with symbols/text.
Powder outline represents powder/liquid; essence outline liquid/essence.
Liquid outline splits left powder/liquid and right liquid/essence, including
half top/bottom segments. Adjacent compact status labels explain each side.
A selected liquid alone must not inherit a verdict from a different partner.
Two green edges establish pair compatibility only, not satisfaction of clues or
correctness of the formula. Current-pair controls and journal share this language.

## Structural generator concern and accepted direction

The user reports repeated first-natural-guess successes and requests a soft
penalty, not a ban, against answer placement at the start of forward or reverse
visible enumeration after composition and starting knowledge. Treat this as a
possible structural issue, superseding an isolated-fixture interpretation; no
frequency estimate is established from the reported examples.
Existing accepted research correction estimates paid route length; it does not
explicitly score displayed answer position. Preserve that weak correction,
validity, diversity and reasoning criteria. Proposed additional diagnostic:
construct public residual hypotheses using all composition conditions and known
positive/negative observations (unknown is possible, a known stable edge is not
a compulsory recipe ingredient). Measure first-hit positions for forward/reverse
card order and branches starting from each displayed known stable pair. Compare
small presentation permutations of the same model with and without a bounded
soft positional penalty. No arbitrary exact coefficient accepted yet.
Apply only as a preference among otherwise comparable candidates; preserve
occasional early success and easy-level intent. Do not reorder the live frozen
trial during play. This penalty reduces accidental first hits; it cannot make a
tiny residual search or uninteresting clauses into a deductive puzzle. Separately
measure residual enumeration cost versus public research routes. Any scoring
implementation requires reproducible paired comparison before adoption.

## Design sources

- Nielsen Norman Group, [Visual hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/): scale, contrast and grouping guide attention.
- Nielsen Norman Group, [Closeness of actions and objects](https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/): keep controls near the objects they affect.
- W3C, [Use of color](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html): communicate states beyond color alone.

These principles support the proposal; they do not validate this specific game
layout. Next layout acceptance needs a visible prototype and a small human check:
can a player locate clues, investigate the selected pair, find its observation,
and return to the hypothesis without facilitator navigation help?

## Implementation and verification

The workbench keeps conditions above candidates at left, current pair controls
and prior/earned journal at right, then a compact selected formula/final action
below candidates. No locked progression. Liquid outlines have independent halves;
public observation symbols supplement color. Unknown and incomplete remain neutral.
The exclusion symbol is a centered SVG circle/slash inside its circular hover
background, avoiding font baseline alignment differences.

`research/PuzzleLab/card-order.mjs` is an authoring-only presentation pass;
`author-card-order.mjs` prepares a new private fixture with a fresh ID, refuses
source/output overwrites and writes a private adjacent audit. The serving process
never imports these files and never changes a frozen field. Run after model and
wording generation, before precommit and first play. This is the implemented Lab
preparation seam, not integration into a nonexistent finished production generator.
All subsequent Lab authoring must include this pass; old frozen cases stay intact.

For each ordering, residual tuples satisfy all public conditions and exclude
known negative edges; positive observations supply optional pair-first branches.
Score is mean of (1/forward-rank + 1/reverse-rank)/2 over the whole residual list
and each answer-containing positive branch. Irrelevant positive branches do not
force the answer. Select among permutations with positive weight exp(-2*score).
Strength 2 is a bounded research default for this separate 0..1 score, not a
replacement for existing 0.25 route/diversity weights or production calibration.
Small fields are exhaustive when within the 128-order default pool limit;
larger pools use bounded seeded shuffle samples including the original order.
Every order remains eligible. Seed, strength, ranks, expected scores and pool
coverage are retained privately for reproducibility. Singleton/two-option
branches may offer no positional improvement; that is not a validity failure.

55 local tests pass, including two independent liquid states, no hidden-graph
access, seeded reproducibility, model immutability, public negative pruning,
optional positive priors, singleton cases, lower expected positional score and
continued early-hit eligibility. The current private frozen trial was passed
through the real authoring CLI into a separate non-serving review artifact:
128 orders, uniform expected proxy 0.5609375, weighted 0.5550747. This is a small
mechanical improvement on one negative diagnostic case, not measured human
engagement or calibrated guessing probability. Active fixture hash unchanged.

Public HTTPS browser QA uses the existing facilitator-classified test session:
known compatible left edge, unknown then earned incompatible right edge,
excluded-card appearance and selected-state/mark persistence after reload.
Only that test session spends 2 Science on a pair check; no human session reset
or fixture replacement. No server/tunnel restart required. Screenshots remain
private. Independent visitor-network availability is not newly established.

Final desktop refinement: the synthesis action sits beside its compact selected
formula/status, rather than underneath a tall duplicate summary. At narrow mobile
widths it returns to a single column. Public icon geometry confirms exact shared
centers and no horizontal overflow. Hosted CI lookup from the local shell failed
to connect; do not present it as successful CI evidence.

Final public viewport check: 852px high, synthesis button bottom 816.42px, no
horizontal overflow. The main action is visible without scrolling in this tested
desktop viewport; long accumulated journals may still extend below it. Two-slot
composition-only cases reclaim the hidden compatibility column. Browser proof
is retained privately; the test session's 28 Science reflects one QA pair check,
not a change to the 30-Science starting budget.
