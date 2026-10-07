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
