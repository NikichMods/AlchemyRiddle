# Browser campaign simulation — reviewable proposal, 2026-10-10

Status: user requests the capability; transfer, difficulty-label, refill and
optional-practice principles were accepted 2026-10-10. Numbered curriculum and
implementation remain proposed, not implemented merely by being written here. Current research
generator `29cb7fd` is accepted as working baseline. Production remains BLOCKED.

## Intended outcome and existing implementation

The user wants to inspect and play an approximate complete alchemy research
progression in the existing attractive browser workspace: selected level,
two/three-slot type, intended difficulty, persistent learned relations and
cumulative Science consumed per player. The purpose is to observe how the core
behaves over a playthrough, including knowledge-driven shortcuts, without the
rest of Graveyard Keeper. Preserve the research-versus-production boundary.

Inspected sibling worktree/branch `research/puzzle-lab-tunnel`, source `c7f3b1c`:
`createLab` still serves one fixture per instance; durable cookie sessions and
telemetry exist. A separate loopback-only facilitator panel controls the playtest
and reports pseudonymous sessions/action timelines. This is not a campaign
generator or a cross-level knowledge store. The public connection and panel
should be reused after normal Git integration, not rewritten. Current friend
sessions and original solved cases must remain unchanged.

Lowest-risk sequence: first implement/test the campaign locally using an isolated
instance/data directory, then make its player mode available through the existing
online route. Developer level/state controls stay in the private local surface.
Hosting choice does not define simulation semantics. No accounts, paid hosting,
new public admin surface or production mod implementation are implied.

## Progression and level representation

Canonical requirements already specify independent ladders: 16 non-decorative
two-slot formula variants and 19 three-slot variants. This provides 35 core
completionist investigation positions, not 35 logical condition types or an
expected natural game playthrough. Eight optional decorative two-slot variants
are additional side content; don't make them necessary to reach mature play.
They have no fixed extra late rungs: start from current two-slot state, and count
completion as ordinary two-slot practice (explicitly accepted 2026-10-10).

Proposed developer view shows both ladders and an illustrative mixed chronology.
Each developer entry shows its within-arity position, arity, intended band, pedagogical role,
target and state (unstarted/active/solved). Mixed chronology is an approximate
scenario of target demand/capability exposure, not fixed game story order.
The full 35-step view supports coverage inspection. A shorter natural-demand
scenario should also exercise roughly the 8/10 strongly motivated outputs per
arity, without claiming every player solves those exact counts.

The accepted progression shape is compact explicit teaching in roughly the first
four investigations of each arity, richer combinations, mature/MAX around six or
seven, then varied mature play, occasional relief and selected boss peaks.
Exact step assignments remain tuning. Show difficulty and arity to all players;
omit “provisional” in the normal UI, but record intended rather than calibrated
measured difficulty in research evidence. Don't use paid-check count alone as a
label. The explicit proposed 16/19 map is now in
`CAMPAIGN_LADDERS_AND_NAMES_2026-10-10.md`. Existing independently authored fixtures are exemplars, not automatically
a coherent campaign.

Player mode progresses through its scenario with one active unsolved puzzle.
Developer mode can inspect/start a rung and inspect its starting knowledge.
Opening an already-started level resumes its frozen puzzle and state. Jumping to
an unvisited rung cannot silently invent knowledge of all earlier experiments;
use a named explicit starting-state scenario, or an actual saved checkpoint.
Developer sandbox experiments must not contaminate player progression/statistics.

## Consistent renamed real corpus and accepted knowledge rules

User clarification 2026-10-10 supersedes the independently synthetic corpus
proposal: use the accepted real corpus privately, changing ingredient/product
display names while preserving tags, formulas, identity sharing, alternate-output
groups and derived three-slot relations. This gives an exact structural basis
instead of imitating aggregate shape. Keep source and reverse mapping private;
do not publish a bulk extracted corpus. Renaming reduces direct spoilers but does
not guarantee that experienced players cannot recognize signatures/topology.
The stand remains an approximation of gameplay availability, demand and economy,
not proof of installed-mod behavior. Navigation: `../CURRENT_ROADMAP.md`.

Before carrying knowledge, define stable global reagent identities, property
assignments and the three-slot relation graph for that campaign version. Local
card positions such as P1/G2 are not identity keys. A renamed/reordered card must
still refer to the same reagent; two independent fixtures using the same position
code must not create false prior knowledge. Audit exemplars before any reuse.

Carry-forward rules accepted 2026-10-10:

- An explicit paid pair experiment immediately records its observed stable or
  incompatible outcome, even if the full formula hypothesis later fails or the
  investigation is unfinished.
- A legitimately solved/known three-slot formula establishes its two adjacent
  stable relations even when those pairs were not individually tested. Starting
  known formulas may be seeded as explicit knowledge scenarios. Do not assume a
  two-slot success proves a three-slot relation without an accepted scope rule.
- A failed whole-mixture test records that mixture result. It alone does not
  identify which adjacent relation was incompatible; avoid fabricated pair facts.
- Preserve incompatible observations across levels as well as stable ones.
  This resolves the previously unspecified negative-reuse decision for the
  campaign. Historical stable-only initial-Lab models remain reproducible.
- Generator input includes actual earned knowledge. Don't hide it to manufacture
  difficulty. A shortened later solution can be legitimate progress.

Store observed facts and source (experiment/known formula) separately from player
hypotheses. Showing relevant earned facts does not automatically solve composition
conditions for the player. Existing route estimator accepts stable priors only;
negative-prior simulations must be extended/verified rather than claimed supported.

Name the renamed stand world through a portable curated semantic catalogue with
varied complete phrase forms; proposed examples and anti-answer safeguards are
in `CAMPAIGN_LADDERS_AND_NAMES_2026-10-10.md`. Target titles must not hint at the
hidden answer; reagent names normally resonate with visible tags. This synthetic
authoring does not replace real vanilla names in the future mod.

## Player profile, Science and research evidence

Proposed first profile is pseudonymous and persistent in the same browser; no
claim of cross-device identity. Profile owns per-arity completion, earned facts,
current frozen investigation, completed investigations and total spending.
Reload/server restart must preserve them. Different players remain independent.

Show current Science, Science spent on this investigation and cumulative Science
spent on accepted paid actions. Count both successful and unsuccessful paid
experiments/checks at their actual costs; denied/unpaid actions add zero.
Refills affect balance and a separately recorded refill count, not consumption.
Completing a level, opening history or reloading must not spend or recount money.
Retain provisional 2 Science per pair and 5 per full formula in this simulation.
Explicit tutorial demonstrations and historical finite-budget fixtures require
their own declared protocol; don't silently mutate them into campaign economy.

Native Science acquisition remains outside the stand. Refill support is an
explicit stand allowance required in every new campaign mode, including guests
and online players; log it so affordability failures are distinguishable
from puzzle difficulty. This measures subsystem costs, not vanilla grind/Faith/
inventory/progression economy. Science spending is a contextual per-player
measure; new puzzle seeds and starting knowledge affect it.

Reuse existing telemetry/pseudonyms and private facilitator panel. Extend reports
with campaign/version, puzzle identity/seed, within-arity step and intended band,
starting knowledge, paid results, cumulative costs and completion. Preserve first
blind runs separately from repeats/developer trials. Visibility time is not
reasoning time. These records must let us distinguish recall benefits, useful
deductions, flat enumeration and abandoned/blocked progression.

## Implementation order and acceptance checks

1. Review/tune the explicit ladder/mixed-scenario map; transfer rules are accepted.
2. Privately transform/verify the renamed real corpus and freeze campaign identity/content.
3. Integrate the existing Lab/panel work with the accepted research baseline;
   implement profile, one active frozen puzzle, progression and spending ledger.
4. Add developer selection/checkpoint inspection and run a local campaign.
5. Verify independent players, reload/restart, knowledge carry-forward, identity
   under reordered cards, failed-hypothesis knowledge, no false inference from
   failed mixtures, no duplicate spending, and generator behavior when search
   yields no valid package. Never relax validity to fill a level.
6. Make the same campaign's player mode available online after local checks.

No automatic publishing or replacing of the running friends' trial is authorized
by this proposal. New campaign sessions need separate identity/storage. Main
generator grammar/selection weights remain the accepted baseline unless campaign
evidence exposes a concrete defect requiring its own decision.
