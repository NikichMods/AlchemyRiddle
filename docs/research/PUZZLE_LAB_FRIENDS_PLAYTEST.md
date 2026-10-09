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

The user then disabled Happ's visible packet-analysis toggle and reconnected.
The Xray process creation time confirms a new core instance. The bounded SOCKS
TLS comparison was unchanged (required SNI resets; region name/no SNI reaches
certificate rejection), and a fresh IPv4 HTTP2 tunnel still timed out publicly
with TCP/UDP pre-check failures and handshake EOF. Thus the tested local toggle
does not explain/remove the failure; actual generated configuration and provider
handling remain unknown. Restore packet analysis and keep Global OFF. Next
bounded diagnostic is another existing VPN exit, if available; the user is asked
about availability. Do not claim server-side filtering or destination rewriting
as proven, and do not compensate by weakening TLS verification.

The user confirms that no alternative VPN exit is available in the existing
subscription. The current connector still reports TLS EOF/timeouts on 7844.
Another-exit comparison cannot be performed with the available setup. Cloudflare
documents 7844 for both supported tunnel transports; substituting ordinary HTTPS
port 443 is not a supported remedy. Next choices are a provider-side connectivity
check or an explicitly accepted alternative tunnel service. No alternative
account, deployment, purchase or service switch has been authorized yet.

User chooses continued route diagnosis. Read-only inspection finds cloudflared
edge TCP sockets using the Happ TUN source/interface. During a bounded socket
sampling interval and explicit SOCKS TLS comparison, no direct Xray-owned TCP
socket to the published global edge endpoints on 7844 was observed. This confirms
the connector enters TUN; absence in sampled sockets does not prove the selected
proxy outbound or eliminate short-lived connections. The TLS SNI comparison is
unchanged. The accessible daemon log contains lifecycle/DNS-protection events,
not per-request routing decisions. No Xray access/error log or generated config
file was found in the examined app data/core/temp locations; the service-owned
core command line is not exposed to the current token. Do not broaden into
subscription databases or dump process memory. Next evidence is the in-app Xray
log while the connector retries; ask the user to show its log view. No settings,
service restart, TLS trust change or alternative deployment made in this step.

After the user selects Info and reconnects, their core-log paste and private
diagnostic archive supply the missing per-request evidence. Requests at local
22:08:09 and 22:08:20 target global edge IPs on TCP 7844, sniff the expected HTTP2
SNI, select `[tun-in -> proxy]`, and emit a VLESS outbound request to the original
Cloudflare IP via the selected VPN endpoint on 443. Thus the actual connector's
proxy route is directly observed. Destination-name replacement is not supported
for these attempts. The report's selected config is not a full generated TUN
config; avoid treating its ordinary SOCKS/HTTP inbounds as the TUN definition.
The user reports the separate TUN log empty; empty log is not a TUN failure.

A bounded native TCP/TLS probe through TUN (no SOCKS intermediary) to the same
published edge IP/7844 reproduces required-SNI ECONNRESET versus alternate-SNI
and no-SNI certificate-chain rejection using Node's default roots. Certificate
verification remains enabled. This is a handshake-progress comparison, not
successful authenticated TLS or a usable tunnel. It makes blanket TCP-7844
blocking insufficient as an explanation and confirms the SNI-dependent symptom
on the connector's transport path. Exact reset origin (provider processing,
upstream network, edge behavior) remains unknown. Next useful evidence is the
VPN provider's correlated destination/dial/error logs and any TLS-name handling.
No provider message sent. Restore routine Warning logging after collection;
retain raw report/config/logs privately, never in Git. No mechanics or server
code changed by this diagnostic step.

- [Tunnel firewall destinations and TLS SNI](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/)
  distinguish region discovery names from HTTP2 `h2.cftunnel.com` on port 7844.
- [Happ routing](https://www.happ.su/main/dev-docs/routing)
  documents subscription-scoped profiles and reconnect for applying changes.

## ngrok preflight — 2026-10-10

User considers ngrok and asks about Russian visitor access and selective Happ
rules before registration. This is not a completed ngrok deployment. Official
[ERR_NGROK_9040](https://ngrok.com/docs/errors/err_ngrok_9040) describes IP-based
agent rejection; a dated first-person Russian-IP report exists, but it does not
establish a current blanket visitor restriction. Agent/dashboard and visitor
connectivity must be assessed separately.

A bounded ordinary-selective-mode host check reports RU for a separate country
control request. ngrok.com fails TLS EOF and dashboard access fails, whereas a
random unassigned ngrok-free.app hostname returns ngrok's HTTP 404/3200 offline
endpoint response. This proves a public-edge response on this host's tested
path, not playable content, not every domain/provider, and not a friend's network.
The control does not establish identical egress for every destination under
selective routing. No live puzzle or account is published by this check.

Suggested subscription-scoped Proxy suffix rules: ngrok.com, ngrok-agent.com,
ngrok-free.app, ngrok-free.dev and ngrok.app, using the existing `domain:` syntax.
The first covers dashboard/API/download subdomains; official default agent
ingress is connect.ngrok-agent.com:443. Both free-domain families appear in
current official docs/blog; use the actual account-assigned hostname for the
server's exact external-origin allowlist. Do not replace exact host checks with
a blanket provider wildcard. No route/profile changes made by the agent.
Next: user applies selective rules and reconnects; verify website and agent
separately, then test the actual puzzle URL from an independent Russian visitor
connection without VPN. Do not promise VPN-free play based on the offline probe.

## Happ rule persistence checkpoint, 2026-10-10

The user's earlier private support report contains 32 proxy domain rules and
20 proxy IP rules, including the Cloudflare additions. A subsequent user
screenshot contains only the seven baseline domain rules plus five newly added
ngrok rules. Those seven baseline rules exactly match the report's embedded
default profile snapshot. This establishes loss/reversion of the visible edited
set, but does not establish its cause. Subscription update success entries do
not prove that an update overwrote routing. The separate on-disk routing file
predates these edits and is not evidence of the current active runtime profile.

A private recovery text file combines all 52 report rules and the five new
ngrok rules, deduplicated (57 lines). It is outside Git; personal domains and
raw support reports must remain private. No Happ setting was changed by the
agent. Next check: user restores the complete Proxy field, saves, reopens the
editor and reconnects to verify persistence before interpreting further network
tests. Earlier core logs still directly establish proxy routing for the recorded
Cloudflare attempts; later missing rules do not invalidate that observation.

## Official references

## Ngrok running checkpoint, 2026-10-10

User completed local account-token setup. Official agent authenticated and
assigned its account dev-domain endpoint. Public HTTPS API returned 200 with
unchanged `lab-v0-easy-01`, two slots of two cards and secure persistent HttpOnly
cookie. The real browser showed ngrok Visit Site once, then the complete puzzle;
selected card survived refresh and process restart. Two independent automated
cookie clients confirmed isolation, one paid action persisted in history, and
both resumed identical states after Stop/Start. These private sessions are QA,
not human trial results. Public fixture/debug/facilitator/rules requests returned
404; HTML, JS, CSS and support assets match local source. Endpoint hostname
remained unchanged across the exercised restart. No third-party visitor-network
result yet; local requests to a public address are not that evidence.

`ngrok-playtest.ps1` is the retained Start/Stop/Status launcher; the private
command wrappers now reference it. Stop verifies process executable/start time,
stops only the owned tunnel and separate Lab, and keeps all sessions. Start
rejects occupied ports, original port 4183 and private directories within Git.
It discovers the actual ngrok HTTPS endpoint and configures it as both exact
public origin and explicitly approved ngrok origin. The server still matches
Host and action Origin against that single address; no request wildcard is
accepted. Automatic approval review rejected initial generic ngrok-family
recognition; explicit per-start ngrok-origin approval was implemented instead.
Full HTTP/evaluator suite passes 46/46; PowerShell syntax parsed successfully.
Stop/Start and public asset checks exercised on Windows. Hosted CI passed for
exact source `bdb8a86050b432e6c4b95ae80a89f12cf5951f2f`
([run 38004004714](https://github.com/NikichMods/AlchemyRiddle/actions/runs/38004004714));
that suite verifies HTTP/evaluator behavior, not Windows launching or visitor
network accessibility. Original solved case-20 session and frozen 2x2 fixture
SHA256 values still match their preserved values.

Operating instructions: keep the computer awake, network/VPN connection,
ngrok process and Lab running. Stop-Playtest ends availability immediately;
reboot, sleep or lost connectivity interrupt it. The assigned account dev domain
is reused on normal restarts (verified once); domain/account changes may change
the URL. A stable address does not mean an always-running website. Free-plan
Visit Site screen is visitor-facing. Players should retain the same browser
profile/cookies to resume. Clearing cookies or another browser creates a new
player. No signup/email gate added. Credential, live hostname, raw logs,
recovery lists and session files remain outside Git. Never publish ngrok.yml.

References: [official agent onboarding](https://ngrok.com/agent-setup/prompt.md),
[free plan limits](https://ngrok.com/docs/pricing-limits/free-plan-limits).

Current research-data envelope: durable state retains current selection, remaining
Science, playing/solved/exhausted status and paid-action history (submitted tuple,
success/cost; pair outcomes and refills where supported by the frozen fixture).
It is not a timestamped click/event log: selection changes overwrite current
selection, and actions have no timestamps. File creation/modification times are
operational metadata, not reliable completion durations. Anonymous cookie
sessions are not unique persons; different browsers/cookie resets create extra
sessions, and polling/probes create empty QA sessions. Explicit private automated
QA identifiers must be excluded before reporting human results. No player names,
identity mapping, visit analytics or facilitator dashboard are implemented.
Future timing/sequence instrumentation and participant identifiers require a
separate agreed measurement design; do not silently change an ongoing trial.

Ngrok preparation checkpoint, 2026-10-10: the user has created an account and
chosen Share Localhost. Official Windows amd64 standalone agent 3.39.11 was
downloaded through the official download-page link; Authenticode status Valid,
signer ngrok, Inc.; executable SHA256
`d339bcbd0713233337e860163f5249eea679cf26750a5700510dbc241d201748`.
Private account setup helper uses hidden token input and an explicit private
config file outside Git. The user enters the credential locally; it must never
be requested in chat or copied to source/logs. No ngrok endpoint has been started.
Neither local 4183 nor 4184 listener was observed at this checkpoint; original
case-20 files were not changed or restarted. Next: local account setup, exact
ngrok public-origin support retaining existing Host/Origin/session protections,
then start and verify the separate synthetic 2x2 instance and actual external URL.

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
