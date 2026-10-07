# Puzzle Lab V0 — corpus case 11

Status: COMPLETED, human trial solved and reviewed (2026-10-08).
Original precommit below is preserved as historical initial state.

User authorized one live human test after accepting the weak ranking correction
and field-feasibility floor. Production remains BLOCKED. This measures human
investigation, not game resource acquisition balance.

## Immutable model

Identity `lab-v0-corpus-11`; displayed title `Неизвестная смесь`. Full model is
private, outside Git, in the existing AlchemyRiddle screen-inputs directory.
Never surface these facilitator artifacts during blind play:

- `corpus-11.json`: SHA256 `ce8fa0416592d619b73eca691cdd295516d2ef04858e99ea2570e470567d8a51`.
- `corpus-11-facilitator.json`: SHA256 `751fee1fb960ae90acef3f4f0818e99b3f7bde5822961b1ab3255862eb7dbd4e`.
- Public initial state: `research/PuzzleLab/fixtures/corpus-11.public.json`, SHA256 `042d4ebd3bcfaff7ad1d499242783c455746485f11d9f8a6573589c277d995ae`.

Facilitator artifact precommits source, selection, complete properties, every legal
pair outcome, submission evaluation and stop rules. Anonymous identities preserve
actual corpus properties and compatibility without disclosing a vanilla recipe.
Both clues are necessary; one full answer exists. Never rebuild after play starts.

## Initial public state and operation

Nine cards, three per slot, complete properties and two composition clues.
Empty selection, observations and history; playing. No prior observations.
Initial Science 20. New pair costs 2 and reports stable/incompatible; known pairs
and invalid requests are free. Full triple costs 5 and reports success/failure.
Wrong submissions leave play active; success stops it. Logical deduction may
justify submission without personally testing every edge.

Explicit +10 Science refill is unlimited and free in the Lab. Paper/game
acquisition is not modeled. No attempt cap, timeout or resource-exhaustion failure.
Selection and help are free. No facilitator deductions or additional clues.

## Recovery and next interaction

Serve the private fixture on loopback port 4174 with private corpus-11-sessions
state directory. Actions are atomically saved with fixture hash; case-specific
HttpOnly cookie restores the same session across restarts. Historical sessions
are unaffected. Restore latest durable state before resuming; never replace the
human trial by assumption. Read docs/PAPER_PROTOTYPE_PROTOCOL.md before play.

Next interaction: player reads the board and makes the first choice. Invite the
player's reasoning without offering eliminations or simulated-route hints.
Capture paid actions, reasoning and final reaction at the next material checkpoint.
Opening the board is not a completed human test.

Before handoff: 25 Node tests pass, including historical rules, shared costs/refill
and HTTP restart restoration. Actual private fixture validated for unique answer,
clue necessity and spoiler-free public projection.

## Human outcome — 2026-10-08

Durable session and frozen file identity verified. Solved; 13 distinct paid pair
checks, two full submissions (failure then success), two +10 refills. Total cost
36 Science (26 pairs +10 submissions), final Science 4. No fixture change or
facilitator intervention during play. No reliable solve-time measurement.
Final public state: research/PuzzleLab/fixtures/corpus-11.completed.public.json.
Derived replay audit: research/PuzzleLab/corpus-11-audit.json.
Anonymous identities below do not expose the source vanilla recipe.

Pair sequence: p3:f2 negative, p3:f1 negative, p3:f3 negative, f1:e2 negative,
f3:e2 stable, p2:f3 negative; failed p1:f3:e2 submission; p1:f3 stable,
f1:e1 negative, f3:e1 negative, p1:f1 stable, p1:f2 negative, f2:e2 stable,
p2:f2 stable; successful p2:f2:e2 submission. First refill followed pair 1;
second followed pair 12.

Initial visible clues admit five triples. First three checks all lie on a
then-unrefuted tag-valid proposal and legitimately reject the dark powder branch.
Checks 4–10 (seven checks) lie on no remaining triple satisfying all visible clues.
They establish real compatibility facts, but cannot resolve this target within
its existing clues. These are replay classifications, not judgments of the player.

Failure p1:f3:e2 satisfies clue 1 and has both stable edges, but fails clue 2:
both fluid f3 and essence e2 lack Slime, whereas exactly one must have it.
Narration after dark-powder rejection correctly assigns Dark to essence, then
attributes Slime to that essence despite its card lacking Slime. The narration
also tentatively merges the two clauses later. These observations support a
branch/condition tracking problem; they do not establish its exclusive cause.
The player subsequently revisits the assumptions and solves independently.

Player reaction: both clauses repeat exactly-one with matching property terms;
would prefer varied formulations. Initial reaction less interesting; later stuck
and surprised that two stable edges did not ensure success. Requested potentially
more guiding composition information; final reflection that this may be a worst
route. Record the desire, not an accepted decision to add clues.

Precommitted simulation: balanced policy mean 2.5 (range 2–3), candidate-first mean
3.6167 (range 2–6). Both maintain all tag constraints perfectly. Actual 13 is not
a worst tie-break within those policies; seven checks occurred outside their
allowed target hypotheses. Existing simulation therefore has an unmeasured human
condition-tracking assumption. One player/trial cannot estimate average human
checks, establish rarity of mistakes or reject the selected puzzle core.

Selector inspection: baseline_score compares families/semantic atoms against prior
selected packages. Case preparation supplies chosen=[] and step=0, so its baseline
score is zero for all pool rows; weak route term distinguishes selection. This
single-case selection does not incorporate the ten human Lab cases as history.
option_family_set collapses repeated family entries. There is no direct preference
against two XOR clauses inside one package. Thus previous diversity work concerns
sequence clumping, and does not guarantee within-puzzle variety.

Judgment: formally valid and blind integrity held; this case does not establish
pleasant ordinary difficulty or human pacing acceptance. Revise/review this package
rather than dismiss the outcome as unlucky play. Keep selected cores, old gates,
weak correction and feasibility floor. No generator semantics or UI changed.
Next bounded step proposed: compare existing pool candidates on within-package
repetition and branch-tracking burden; determine a review/soft preference before
another blind case. Changing weights, adding clues or automatic deduction requires
an owning decision; do not silently implement those from this outcome.
