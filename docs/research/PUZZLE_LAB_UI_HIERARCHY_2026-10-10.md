# Puzzle Lab hierarchy and answer-order proposal — 2026-10-10

Status: design proposal; no new layout or generator weights implemented.
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
