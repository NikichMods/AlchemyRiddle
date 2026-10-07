# Puzzle Lab V0 easy-01 — first player feedback, 2026-10-07

Status: **REVISE as onboarding/positive exemplar**. Formal validity remains
proved; intellectual interest and wording were not accepted by the player.

Model: `research/PuzzleLab/fixture.json`, id `lab-v0-easy-01`, precommitted in
`research/PuzzleLab/FACILITATOR.md`. The fixture was not changed after feedback.

Player report:
- four occurrences of the same Plant property across two conditions felt
  repetitive and impoverished;
- the conditional was read as directly requiring Plant powder and Plant fluid;
- the player reported an unsuccessful submission and perceived the two clues
  as pointing to different answers;
- card layout did not make the two slot columns visually distinct enough;
- property tags need consistent semantic colors, also visible in clue text;
- Dark should remain visible against the dark page background.

Evidence limits: the supplied screenshot shows the clue panel only. Browser
automation timed out, so exact selections, marks, notes, history and remaining
Science were not recovered. Do not reconstruct the submitted tuple from the
player's verbal interpretation. Prior technical smoke-test state is not human
test evidence.

The facilitator explained after the reported failed attempt that a conditional
does not assert its antecedent and that two Plant components violate exactly-one.
This is now debrief, not an intact fresh blind attempt. Replaying this same
fixture cannot establish fresh blind onboarding acceptance.

Decision: retain as a formally valid negative onboarding example; revise the
teaching/presentation before using another positive case. Do not generalize
this failure to all implication puzzles. In particular, repeated property text
and introductory conditional semantics need separate attention from formal
uniqueness. Do not silently replace clues or the answer in a played fixture.

Presentation change: colored labeled property badges appear consistently on
cards and in clue text; each slot has a bordered group and a boxed legend.
Colors communicate identity only, not extra logic. Palette covers the accepted
ten-property vocabulary; Russian names beyond the current fixture are tentative
display aliases, not accepted terminology. Unknown properties use a neutral
fallback. The current fixture/budget/evaluator remain unchanged.

Checks: JavaScript syntax, seven rules/HTTP tests and diff whitespace checks pass.
Visual verification was subsequently completed in a new browser tab after the
old tab remained unresponsive. Server was not restarted; human state survived.
Next interaction: player reviews the presentation and debrief; author a new
precommitted onboarding case after the learning issue is addressed.

## Recovered player state — 2026-10-07 loading incident

Recovered from the rendered new tab, sharing the same browser session:
- selected Powder p2 (Бархатная пыль), Fluid f1 (Лунная влага);
- no marked/excluded cards;
- notes empty;
- exactly one submitted pair, p2 + f1, failure, cost 1 Science;
- remaining Science 0; exhausted, submission disabled;
- target, cards and both clues unchanged from the precommitted fixture;
- debrief already started; no fresh blind continuation is possible.

This supersedes the earlier recovery limitation without changing what was
known at the original feedback checkpoint. Both selected components are Plant,
so the failed pair satisfies the implication but violates exactly-one.
