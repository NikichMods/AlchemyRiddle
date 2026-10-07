# FACILITATOR SPOILERS — DO NOT SURFACE DURING BLIND PLAY

Case lab-v0-09, Свет под водой. Synthetic richer three-slot example; complete
immutable outcome model is lantern-09.json. Precommitted before player choices.
Names vary by slot but carry no mechanics beyond the exhaustive visible tags.

Answer p2/f2/e1. Four tag-compatible triples: p1/f1/e3, p2/f1/e1,
p2/f2/e1, p3/f1/e1. Exactly one also has both stable adjacent edges.
All other legal adjacent pairs outside stablePairs are incompatible.
Removing each clue leaves respectively 2, 2, 2, 3 fully valid formulas;
all four clauses are necessary in combination with the empirical model.

Initial priors: p1/f1, p2/f1, f2/e2, all stable. No incompatible priors.
Unknown outcomes are not implied by tags. Known pair tests are free and do not
consume charges; new adjacent tests cost 1 Research Charge, 6 available.
Full synthesis costs 1 Science, 3 available; incorrect synthesis preserves play
while Science remains. No replenishment. Success stops synthesis; failure with
zero Science exhausts play. No answer disclosure or deduction hints.

A bounded route through tag-compatible branches can test f1/e3 (false), f1/e1
(false, rejects both remaining f1 branches), p2/f2 (true), f2/e1 (true), then
submit. Four investigations suffice; this is a facilitator feasibility witness,
not a player-facing recommendation. Six-charge envelope allows exploration.

Initial intended UI: empty selection/marks/notes/history, playing, Science 3,
Research 6. Candidates above composition and compatibility; actions at right.
Future reloads preserve this player's current state rather than simulate a new
case. A fresh handoff must change fixture identity and verify initial state.

## Outcome

Explicitly accepted after five pair investigations and one successful synthesis.
See case-09 checkpoint for exact action order and subjective evidence. Frozen
fixture unchanged. No answer hints supplied during play.
