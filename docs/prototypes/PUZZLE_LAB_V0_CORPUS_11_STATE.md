# Puzzle Lab V0 — corpus case 11

Status: PRECOMMITTED, awaiting first player choice (2026-10-07).

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
