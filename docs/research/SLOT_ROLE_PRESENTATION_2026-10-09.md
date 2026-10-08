# Slot-role scanning — explicit presentation trial

2026-10-09. User authorizes trying bold complete role names with small monochrome
versions of the existing card silhouettes. The user subsequently reports improved
readability; no measured error reduction. Follow-up palette/guidance/button preview
is owned by `LAB_GUIDANCE_AND_HIERARCHY_2026-10-09.md` and awaits its own review.
Research Lab only; production remains BLOCKED. No new puzzle or logical rule.

## Owner, scope and preservation

`app.mjs:clueContents` is the final clue DOM writer. Previously it decorated only
quoted properties. In explicit `?roles=1` mode, unquoted complete Russian role
words receive a `strong.clue-role` wrapper and decorative SVG; known singular
case forms retain their exact spelling/capitalization. Whole-word Unicode bounds
avoid highlighting pieces of longer words. Only roles present in the current
fixture are decorated. Quoted properties still use the original tag renderer.

Card and clue icons share the same path dictionary: powder pile, fluid flask,
essence hexagon. Inline icons are 20x17 pixels, current text color, aria-hidden
and nonfocusable; readable role words remain the accessible content. Role/icon
stay together on wrap. No icon legend, color meanings, click action, automatic
deduction or answer-dependent styling is introduced.

Normal URLs retain historical rendering. Comparison on solved case 19:
`http://127.0.0.1:4182/?roles=1`; original `http://127.0.0.1:4182/`.
Same fixture, cookie and completed session; no replay or fresh human trial.
Frozen wording/AST/graph/budgets, known observations and submitted formula unchanged.
The query flag is a bounded comparison aid, not accepted production settings UI.

## Verification and next interaction

Node syntax check and all 42 existing deterministic/HTTP tests pass.
Browser verifies six decorated role occurrences including accusative essence;
all four clue textContent strings exactly match the original rendering. Visual
inspection at the current desktop viewport shows small monochrome silhouettes,
bold complete words, retained property colors and readable wrapping. Solved state
and Science 7 preserved during this original review. Screenshot is private beside
case 19 (`role-preview.png`). Later browser-session changes are documented in the
follow-up record; recover the actual solved session rather than a preview.

No new tests written for this reversible presentation trial. No model/wording
changes. Next interaction: user's visual comparison, then retain/refine/reject
the trial. Reduced reading errors require subsequent human evidence, not merely
the verified DOM or passing logical harness tests.
