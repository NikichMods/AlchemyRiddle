# Temporary friends playtest

2026-10-09. Separate research-harness deployment; production remains BLOCKED.
No puzzle mechanics, generator, ranking, economy or accepted board UI changes.

## Current immediate outcome: one 2x2 puzzle first

User narrows the next step to one ordinary starting 2x2 puzzle opening through
an external URL; defer the five-level series until that works. Use an unchanged
private copy of existing synthetic `lab-v0-easy-01`, «Тихий свет» (two powders,
two fluids, two necessary conditions, one answer), fixture SHA256
`afee9cef67f4e770acce819e10b3e1198fe09305efbeeaf68b07af0f6bd2e08d`.
Existing source/FACILITATOR.md is the complete precommit; copy it privately with
the fixture. Keep its costs, finite budget and stop semantics unchanged. This
does not rehabilitate its historical REVISE-as-onboarding verdict or add a
guided tutorial. It represents no unknown vanilla recipe.

The previous case-20 friends copy/tunnel is stopped with its data preserved;
the original solved human instance on 4183 is unaffected. The 2x2 instance uses
a new private directory and separate sessions on the freed 4184 port.

A fresh 2026.10.0/global/HTTP2 tunnel returned the exact 2x2 public model over
HTTPS at startup (including ID and candidate shape), then browser access about
40 seconds later returned 1033. Subsequent HTTPS API/HTML/JS/CSS requests all
returned 530/1033; local cloudflared metrics still reported one connection and
one served request. Thus brief API success is directly established; sustained
page accessibility is not. Smaller puzzle content alone did not fix access.

Launcher Start now probes the exact fixture ID/shape and complete served
HTML/JS/CSS against local assets before printing successful public response.
Status repeats the live probe rather than representing an earlier successful
startup as current availability. No address is claimed working solely from
process startup or edge registration. A failed public probe leaves the local
instance available for diagnosis and labels external access unconfirmed.

Cloudflare [documents Russian ISP disruptions](https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/service-disruption/)
and [defines 1033](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1033/)
as inability to find a healthy connector. ISP restrictions are a hypothesis for
this host, not a proven cause. An existing local network-filter service is
present; no service, firewall, proxy or VPN settings were changed. Existing VPN
availability is requested from the user as potential comparison evidence.
The host filter's published TCP/UDP port lists do not include tunnel port 7844;
its mere presence does not establish it as the cause. Do not stop or reconfigure
it on that assumption. A second controlled 2x2 launch with full-asset probing
timed out on HTTPS API both at startup and on a later live Status check. The
local 2x2 board is visibly verified in the browser; its private precommit and
initial public snapshot are frozen separately. No player action was performed.
Original solved case-20 session bytes still match the prior recorded private
SHA256; root 4183 returns 200. No working external link is established.

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

## Selective VPN diagnostic, pending application

Read-only host inspection confirms an active VPN TUN interface and the current
HTTP2 connector socket entering that interface. This does **not** establish its
eventual proxy/direct outbound. Startup connectivity pre-checks passed DNS and
TCP/UDP 7844, but later logs show repeated control-stream/edge disconnects and
a DNS refresh timeout. Passing a short handshake is not sustained availability.
The user supplied prior selective-VPN context; local routing metadata contains
multiple same-named profiles, so changes must target the active subscription.
No VPN, routing, firewall or Zapret settings have been changed.

Next bounded diagnostic: preserve the current profile and add only Quick Tunnel
creation/discovery names plus `h2.cftunnel.com` to its proxy destinations for the
current HTTP2 transport, reconnect the VPN, then restart only the friend harness
and repeat full public asset/session checks. Domain rules may depend on TUN
sniffing; their presence alone does not prove the connector's outbound. Avoid
global proxy or broad Cloudflare network rules. Native Windows UI control is
unavailable in this agent session, so applying the Happ UI change requires the
user; blind edits to its live storage are not a supported substitute.

After the user reported adding the narrow domain rules and reconnecting, only
the 2x2 friend harness was restarted. The new public API probe timed out; edge
TLS handshakes repeatedly ended with EOF while startup connectivity pre-checks
passed. Original 4183 still returned 200. The previously located routing metadata
file predates this test and does not establish whether current UI edits applied.
Neither successful proxy routing nor a VPN-specific failure is proven. Next
evidence required: active subscription/profile Proxy rules and current VPN mode
in the Happ UI. No working URL or HTTPS session-persistence result is established.

The user identified the running Flowseal Zapret bundle as a possible TLS cause.
Read-only inspection of its registered service command shows no TCP/UDP 7844 in
the WinDivert port filters, making direct handling of tunnel traffic unlikely;
this does not rule out effects on VPN outer transport or other network layers.
A bounded temporary-stop/public-probe/restore diagnostic was attempted, but
Windows denied opening the service for stop. The test did not run, the service
remained Running, and no settings or startup mode changed. This is an OS service
permission limit, not evidence for or against the conflict hypothesis.

The user then disabled Zapret. Inspection found neither its service nor a winws
process. Both the existing tunnel probe and a fresh same-version/global/HTTP2
friend-harness start still timed out publicly with repeated TLS handshake EOF.
Original 4183 returned 200. Disabling Zapret did not remove the observed failure;
this does not support Zapret as the primary cause. The user is asked to restore
their usual Zapret setup; because the service is now absent, simply starting that
service is unavailable. No service recreation or configuration change is made
by the agent. Active Happ routing remains the next unverified boundary.

User screenshots confirm Mixed/Xray TUN and all four requested domain rules in
the selected profile. They do not prove the connector's selected outbound.
The user then enabled Global Proxy and reconnected for a bounded comparison.
A control HTTPS request to Cloudflare trace returned `loc=DE`/`colo=FRA` without
publishing the client IP. The new HTTP2 tunnel failed at edge discovery: SRV DNS
queries returned no usable records, and the public probe returned 530. Ordinary
A records resolved through the host; Google DoH returned the expected SRV records.
Thus German egress is verified for that control request, not a working connector.
Xray's documented handling of non-A/AAAA queries depends on DNS forwarding, which
is consistent with this symptom but does not establish the exact Happ fault.

Next narrow test: restore Global OFF, retain the existing domain rules, and add
only the twenty explicit global-region IPv4 tunnel endpoint addresses published
by Cloudflare as /32 proxy destinations. This avoids relying on TLS domain
sniffing, preserves normal default-direct routing, and avoids broad Cloudflare
CIDR/port rules. Success still requires a fresh complete public probe. No system
DNS edit, disabled TLS verification, private subscription edit or unsupported
internal cloudflared deployment flag is introduced.

After the user added the /32 endpoint rules and restored selective mode, a fresh
global/HTTP2 connector with IPv4 still failed publicly. DNS and API pre-checks
passed; TCP/UDP 7844 checks failed and connector handshakes ended with EOF. The
launcher now exposes `-EdgeIPVersion 4` for repeatable IPv4-only endpoint tests
and records the setting rather than depending on an inherited environment flag.

A bounded local SOCKS CONNECT to one published endpoint on 7844 succeeded. TLS
with SNI `h2.cftunnel.com` reset; TLS to the same IP via the same proxy with a
region-discovery name or no SNI reached certificate verification, where Node's
ordinary trust store rejected the leaf chain. TLS verification was never disabled.
Google DoH returned no A records for `h2.cftunnel.com`. These observations support
an SNI/destination-override hypothesis, not a proven Happ configuration fault or
a successful tunnel. Xray documents that sniffing can replace a destination IP
with the detected name; `routeOnly` or a domain exclusion prevents that rewrite:
[Sniffing configuration](https://xtls.github.io/en/config/inbound.html).
Next evidence: actual Happ Xray/TUN sniffing settings before changing them.

During this check original port 4183 stopped responding; the agent did not stop
that server. The original solved human session still matches its frozen private
SHA256. Ask whether the owner/other chat stopped it before attempting a competing
restart. The original checkout and session contents remain untouched.

- [Tunnel firewall destinations and TLS SNI](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/)
  distinguish region discovery names from HTTP2 `h2.cftunnel.com` on port 7844.
- [Happ routing](https://www.happ.su/main/dev-docs/routing)
  documents subscription-scoped profiles and reconnect for applying changes.

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
Final bounded US/QUIC comparison also returned 530 and failed edge connections
with QUIC timeouts; the extra diagnostic tunnel was stopped. The separate main
friend server/tunnel remain running for the requested mobile-network check.
Deployment status: **local READY; external access BLOCKED by observed 1033/530**,
not completed. No evidence yet establishes availability from a friend's network.
Further useful evidence is an independent visitor result or a changed host
network/service condition, rather than repeating the same successful local tests.

Hosted Puzzle Lab CI passed for source `1d01066b503d1a367d386965ae634e187b3a7935`
([run 37953244942](https://github.com/NikichMods/AlchemyRiddle/actions/runs/37953244942)).
This verifies the HTTP/evaluator suite on Node 24/Linux, not the Windows launcher
or Cloudflare network. Private desktop Start/Stop/Status command files reference
the retained isolated worktree and absolute bundled Node path, so ordinary
desktop launch does not depend on the chat's PATH. Default next launch selects
official 2026.10.0; the live version comparison instance is 2026.9.3. No public
link, raw logs, cookie or player data are tracked in this document.
