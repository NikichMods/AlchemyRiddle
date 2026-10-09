# Temporary friends playtest

2026-10-09. Separate research-harness deployment; production remains BLOCKED.
No puzzle mechanics, generator, ranking, economy or accepted board UI changes.

## Scope and identity

User authorizes a temporary Cloudflare Quick Tunnel on the host PC, without an
account/domain/server rental or GitHub Pages. Do not message friends. Email access
is available in current Cloudflare but unselected; no addresses or registration
invented. Anyone holding the unprotected URL can access the playtest.

Preserve the original case-20 server on 4183, its fixture and solved human session.
Serve an unchanged private copy of the **synthetic** case-20 fixture on a separate
loopback port, initially 4184, with a separate private session directory. Identity:
`lab-v0-interest-20`, fixture SHA256
`8f6689613e1149c9c2ce61734523179debfc83ff89160e6bf3dc835021a185a9`.
See `../prototypes/PUZZLE_LAB_V0_INTEREST_20_STATE.md` for frozen semantics and
private facilitator precommit. Starting each friend session is fresh play, not a
copy of the owner's solved session. No real-corpus fixture is exposed.

One active writer per checkout: implementation uses a separate app-managed
worktree based on `61415a9`, branch `research/puzzle-lab-tunnel`. Do not write or
switch the original `research/puzzle-lab-v0` checkout to run this deployment.

## Mechanism and evidence boundary

The existing server owns request validation and persistence. Public mode adds
one exact `https://<name>.trycloudflare.com` origin alongside existing loopback
hosts. No wildcard hosts or forwarded-header trust. Public POST requires matching
Origin, JSON content type and same-site request context. Cross-site browser
requests are rejected. Public mode requires durable storage and rejects debug
and fixture watching. Served assets remain the existing explicit allowlist;
answer/hidden graph, source, private files and facilitator routes are unavailable.
HTTPS sessions use an HttpOnly/Secure/SameSite=Strict host-only cookie lasting
30 days. Public-instance local QA uses a separate persistent `lab_playtest`
cookie so checking another localhost port cannot replace the owner's cookie.
Existing local mode retains its cookie behavior. At most 500 loaded
sessions in public mode bounds incidental session allocation; this is a small
friend harness, not a general public service. Input body limit remains 20,000
characters. Public malformed/internal errors do not expose filesystem paths.

State writes are atomic and model-hash bound. After reading an async request body,
actions clone the latest session state, so simultaneous tabs cannot overwrite an
already committed action with an earlier snapshot. Session JSON retains the
existing paid experiments, submissions, selected cards and resources. Do not
commit raw player sessions, identifiers, cookies, tunnel links or logs to Git.

Question for new tests: do the network boundary and durable multiplayer behavior
hold through the real HTTP handler? Existing local tests do not exercise an HTTPS
tunnel Host/Origin. Two bounded HTTP tests reuse the existing evaluator and
persistence rather than reconstructing chemistry; they exercise the exact handler
including source/debug rejection, wrong hosts/origins, cookies, refresh, two
players, earned experiments and restart. Add them to existing Lab CI.

## Run / stop

Requirements: Node 24; official Windows amd64 cloudflared; frozen synthetic
`fixture.json` and `cloudflared.exe` in a private directory outside every Git
checkout. Session files, logs and `running.json` stay there. The launcher verifies
private location, blocks port 4183 and refuses an occupied port or a duplicate
running instance. It starts hidden processes; Stop verifies executable path and
process start time before stopping only its own tunnel/server. Existing sessions
are retained. A failed startup stops its children.

From the isolated checkout in PowerShell:

```powershell
$privateLab = 'ABSOLUTE_PRIVATE_DIRECTORY'
& .\research\PuzzleLab\playtest.ps1 -Mode Start -PrivateDirectory $privateLab
& .\research\PuzzleLab\playtest.ps1 -Mode Status -PrivateDirectory $privateLab
& .\research\PuzzleLab\playtest.ps1 -Mode Stop -PrivateDirectory $privateLab
```

Start prints the URL. It proves local startup only; test the HTTPS URL before
inviting friends. `-Protocol http2` and `-Region us` are explicit diagnostic
options if the default auto/global route fails; do not assume they repair any
network. `-CloudflaredPath` can select another official binary.

Keep the PC awake, internet connected, server and tunnel processes alive. Stopping
cloudflared invalidates the URL; creating a new Quick Tunnel changes its hostname.
Cloudflare offers no uptime guarantee. A connection retry within the same process
does not create a new URL. Stored sessions survive server restart with the same
fixture and cookie. **New hostname means a different browser cookie scope**:
old play files remain on disk but are not automatically resumed at a new link.
Likewise another browser/device, private-window closure or cookie deletion can
start a new player session. Automatic transfer/recovery across links is not
implemented or promised. Two tabs of the same browser profile share a player;
different profiles/cookie jars are independent players.

The launcher does not install a Windows service, modify firewall rules, start
automatically after login, or keep the PC awake.

## Five-task series: intended result and decisions still open

User's desired follow-up: five sequential tasks; a persistent 1–5 selector;
completion of task N opens N+1; task 1 teaches and task 5 offers a boss-like
challenge with a gradual transition. This is a dedicated playtest curriculum,
not a replacement for production's independent arity ladders or generator policy.
No five-task implementation is silently included in external-access work.

The current Lab has one fixture per server, one state per browser session, no
campaign manifest, level switch/unlock state or guided tutorial. Existing case 01
is explicitly REVISE as onboarding; an easy puzzle is not sufficient teaching.
Case 20 has positive one-player boss-like reception, not a calibrated population
ceiling. All five frozen models must pass the prototype precommit protocol before
friends play. Do not simply assign historical fixture numbers to difficulty bands.

Recommended narrow design, **proposal awaiting selection**:

- Author a fixed five-fixture synthetic manifest; no runtime generator or new
  scoring weights. Prefer one three-slot ladder to avoid compressing two separate
  onboarding grammars into five sessions; user choice remains open.
- Teach roles, exhaustive properties, all-clues binding, adjacent pair outcomes,
  journal and synthesis in the first guided task. Tutorial may explain its own
  fictional model; later independent tasks remain free of facilitator deductions.
- Use 2–4 to practice and combine count/XOR/implication and observation-driven
  branch elimination under increasing interaction depth, then the frozen case-20
  copy as candidate 5. Exact fixtures, tutorial script and human difficulty
  gradient need separate validation. Case 20 must not introduce an untaught rule.
- Unlock on existing server-confirmed successful synthesis; persist five separate
  task states plus unlocked/current level for each player. Completed levels can
  be viewed without erasing progress. Reload returns to the same active board.
- Keep existing unlimited Lab refill and costs. Prefer no automatic replay/reset
  during first blind runs; a new trial must not erase the original evidence.
- Begin with anonymous browser sessions and existing experiment histories.
  Decide whether voluntary nickname, action timestamps, completion time and a
  short end-of-series feedback form are needed. Current histories do not measure
  time, reasoning quality, understanding or subjective enjoyment.

Material decisions before building the series: same three-slot grammar vs two-to-
three transition; what the tutorial demonstrates and when help ends; the exact
five validated models; unlock rule if successful synthesis is not desired;
return/replay/retry behavior; session recovery after a new tunnel URL; desired
research observations and friend-facing expectations about data retention.
No account system, email registration, full analytics or public-service
architecture is needed merely to host a few friends.

## Official references

- [Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/):
  no account/domain; hostname changes per creation; link ends on stop; 200
  in-flight request limit; no SSE; no uptime guarantee. Lab uses finite polling.
- [Downloads](https://developers.cloudflare.com/tunnel/downloads/): official binary
  links; Windows updates are manual.
- [Email protection announcement, 2026-10-02](https://developers.cloudflare.com/changelog/post/2026-10-02-protected-quick-tunnels/):
  `--allowed-mail`, one-time email PIN, no visitor Cloudflare account required.
- [Tunnel parameters](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/):
  auto/QUIC/HTTP2 transport and optional US region. These do not guarantee
  connectivity through any particular ISP.

## Verification record

Local suite: 45/45 pass on Node 24 using `--test-isolation=none` where the sandbox
blocks child-process test isolation. Original 4183 root continues to return 200.
Private copied fixture matches the frozen SHA256. Startup, owned-process status
and Stop/Start have been exercised; original server never stopped.
The actual friend server on 4184 also passed two independent HTTP-cookie sessions:
one paid adjacent experiment persisted at Science 18, another stayed at Science
20 with empty history. These are marked private QA, not human trial results.
Original human session is still solved at Science 8; private precommit fixture
matches the copied model. In-app browser refresh preserved a selected card after
introducing the persistent isolated local cookie; initial session-only-cookie
QA did not preserve it in that browser. Public HTTPS browser persistence awaits
a reachable tunnel. Tests also cover concurrent tabs with a slow request body.

Network verification is separate: official cloudflared 2026.10.0 checksum matches
the upstream release asset digest. Initial global HTTP2 registered then returned
Cloudflare 1033/530; auto/global QUIC registered but repeatedly timed out; US HTTP2
also registered but did not yield a working public response. Registration alone
is not proof of public usability. A bounded comparison with supported official
2026.9.3 (upstream SHA256 verified) is used to test a version-regression hypothesis.
The previous version also returned HTTP 530 with body `error code: 1033`, despite
registered HTTP2 connectivity. This does not support a 2026.10.0-only regression.
Official status page inspection did not show a general Tunnel incident at the
time; absence of a posted incident is not proof that the service is healthy.
Root cause remains unestablished. A mobile-data visitor check is requested;
the generated URL must not be described as working merely from registration.
