# Puzzle Lab V0

Local research harness, not a game mod or a published website. Original source
is MPL-2.0. No third-party packages, game assets or real recipes are included.

From the repository root, with Node.js 24:

```sh
node research/PuzzleLab/server.mjs
node --test research/PuzzleLab/lab.test.mjs
```

For the current blind calibration case (Тихая гавань):

```sh
node research/PuzzleLab/server.mjs --fixture=research/PuzzleLab/fixtures/harbor-06.json
```

The default fixture remains the original case for historical reproduction.
Do not open facilitator records during blind play. Current player checkpoint:
`docs/prototypes/PUZZLE_LAB_V0_06_STATE.md`. Difficulty labels and progression UI
are deliberately deferred pending a separate product decision.

If a restricted execution environment blocks the test runner's child process,
use `node --test --test-isolation=none research/PuzzleLab/lab.test.mjs`.

Open http://127.0.0.1:4173. Stop with Ctrl+C. Another port may be selected with
`--port=4174`. The server binds only to IPv4 loopback. `localhost` is also
accepted when it resolves to IPv4.

HTML/CSS/browser-JS changes trigger live reload and preserve session state.
The browser checks public presentation/fixture state with finite requests every
two seconds; no permanent EventSource stream is opened during navigation.
Changes to `server.mjs` or `rules.mjs` require a server restart. A valid changed
fixture triggers reload and resets sessions; invalid edits retain the last
valid fixture and print an error. Do not edit a fixture during blind play.

Replace the default fixture with `--fixture=path/to/fixture.json`. The fixture
owns cards, properties, structured clues, answer and Science budget. The rules
module evaluates and renders the same clue structure, preventing independently
authored wording from drifting from its logic. Startup requires one unique
answer. V0 supports two or three slots, exact counts, implication, shared-property and
forbidden-conjunction clues used by the committed fixtures.

Player mode has no debug link, answer data, candidate solver or automatic
exclusions. The answer stays server-side. Manual exclusions are annotations and
do not block selection. Sessions survive page reload through an HttpOnly cookie;
all state is in process memory, not durable storage. Notes and the current
player state can be downloaded as JSON. Exports contain no hidden answer.

Facilitator use only, after blind play or while privately authoring:

```sh
node research/PuzzleLab/server.mjs --debug
```

Visit `/facilitator` for an explicit spoiler warning and opt-in link to JSON
containing the fixture, per-tuple clue truth table and current sessions. The
live clue-compatible set is the rows with all clue values true. Player marks
remain independent. These routes return 404 unless debug is explicitly enabled.
This is accidental-spoiler separation, not an anti-cheat system: a local user
can inspect repository files, clear cookies or restart the server.

The first fixture is a proposed easy positive case, not a player-accepted
inference-quality exemplar. Facilitator semantics and test status are recorded
in `FACILITATOR.md` (contains fictional spoilers). V0's single Science budget is
a bounded calibration choice, not production balance.

Three-slot fixture research: both adjacent pairs must be STABLE in addition to
all target clues. `compatibility.stablePairs` defines the stable edges; all other
legal adjacent pairs are incompatible. `knownRelations` seeds prior observations.
These facilitator fields remain server-side except observed relation results.
`researchCharges` / `pairTestCost` fund unknown adjacent tests separately from
Science / submissionCost. Repeating known pairs is free; the UI disables them.
No Powder-Essence test, automatic exclusion or derived candidate set is offered.
The initial knowledge state is fixed for calibration, not a production generator.
Workspace interaction: click a candidate to select it; click again to deselect.
Pair/formula actions are directly under the candidate grid. Pair states use only
already observed knowledge; no tag-based deductions are supplied. The journal
separates prior vs current-investigation observations and the two adjacent pair
types, with polarity colors/icons and matching-selection highlights. General
rules, notes and full action history are in expandable reference sections.
Case 06 is retained with its historical mixed-polarity initial observations;
new blind cases start with stable bridges only, per the clarified product policy.
