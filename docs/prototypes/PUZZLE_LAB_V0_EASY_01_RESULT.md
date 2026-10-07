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
Visual verification of the new rendering remains pending because the browser
connection timed out. Server was not restarted; in-memory human state was not
deliberately reset. Next interaction: player reviews the presentation and the
debrief; author a new precommitted onboarding case after the learning issue is
addressed. No exact ongoing player state can be recovered from this record.
