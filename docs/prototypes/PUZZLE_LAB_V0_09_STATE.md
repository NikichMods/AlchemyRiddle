# Puzzle Lab V0 — case 09 checkpoint

Target: Свет под водой, lab-v0-09. Three slots, three candidates each.
Precommitted model: research/PuzzleLab/fixtures/lantern-09.json.
Facilitator record: research/PuzzleLab/fixtures/LANTERN_09_FACILITATOR.md
(hidden spoilers; do not link during blind play).

Initial state: playing; selected {}, marks {}, notes empty, history empty;
Science 3, submission cost 1; Research Charges 6, new pair test cost 1;
three stable prior observations, no negative priors, no replenishment.
All personally discovered stable/incompatible results persist. Final synthesis
is available without first testing unknown pairs; the risk is shown explicitly.

Next interaction: fresh blind play, user narrates choices and reasoning.
Do not infer new constraints for the player or disclose hidden results/answer.

Handoff correction: the previous UI-only update retained the exhausted case 08
session, confusing the user into believing it was a fresh puzzle. The server
must actually run case 09 and the visible tab must show a fresh empty state and
three available checks before this case is handed off. Ordinary refresh of an
active investigation should continue to preserve its choices and observations.

## Completed blind play — 2026-10-07

Browser history and narration agree. Status solved; selected p2/f2/e1; Science 2,
Research 1; notes and marks unchanged. Exact action sequence:
1. p3/f1 incompatible (Research -1).
2. f1/e1 incompatible (Research -1).
3. f1/e3 incompatible (Research -1).
4. p2/f2 stable (Research -1).
5. f2/e1 stable (Research -1).
6. p2/f2/e1 synthesis success (Science -1).

The player checked tag-linked branches, used learned negative edges without
retesting them, rejected all three initial bridges as full-formula starting
points, then formed and investigated a new chain. Five experiments, no failed
synthesis. Explicit positive acceptance: felt like a researcher, sequential,
interesting, satisfying. Count-two was explicitly welcomed after repeated
count-one clauses. Keep this as positive investigative-route evidence, not a
calibrated difficulty rating or controlled UI comparison.

UI feedback: long green prior rows drew attention away from tag constraints and
looked like personally earned success. Wants compact shape-coded reagent IDs,
without long names in journal rows, while retaining hover linkage. Unknown-pair
summary mixed risk with enabled-action wording; needs the two-stable-pair rule
at the research controls. Requests optical vertical centering of property tags.

Subsequent presentation revision: reagent codes inside powder-mound/flask/faceted
silhouettes, full pair names in hover titles and accessible button labels; prior
rows neutral, no success checkmark, discovered results retain text and symbols.
No full-width green journal backgrounds. Short local research/whole-formula
explanation, unknown summary only says compatibility is not yet known. Tags use
flex centering and consistent height. Completed player state preserved, not a
fresh puzzle or restart. Next: mature/boss contrast, then quality-contract synthesis.
