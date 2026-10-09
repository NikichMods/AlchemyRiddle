# SPDX-License-Identifier: MPL-2.0
[CmdletBinding()]
param(
  [ValidateSet('Start','Stop','Status')][string]$Mode='Status',
  [Parameter(Mandatory)][string]$PrivateDirectory,
  [Parameter(Mandatory)][string]$NodePath,
  [int]$Port=4184
)
$ErrorActionPreference='Stop'
$PrivateDirectory=[IO.Path]::GetFullPath($PrivateDirectory)
$toolDirectory=Join-Path $PrivateDirectory 'ngrok'
$recordPath=Join-Path $toolDirectory 'running.json'
function Find-OwnedProcess($entry) {
  if (!$entry) { return $null }
  $process=Get-Process -Id $entry.id -ErrorAction SilentlyContinue
  if ($process -and $process.Path -eq $entry.path -and
      $process.StartTime.ToUniversalTime().ToString('o') -eq ([DateTime]$entry.startedAt).ToUniversalTime().ToString('o')) { return $process }
  return $null
}
function Process-Record($process) {
  return @{id=$process.Id;path=$process.Path;startedAt=$process.StartTime.ToUniversalTime().ToString('o')}
}
function Probe-Public($url) {
  $headers=@{'ngrok-skip-browser-warning'='puzzle-lab-check'}
  $expected=Get-Content -LiteralPath (Join-Path $PrivateDirectory 'fixture.json') -Raw | ConvertFrom-Json
  $state=Invoke-RestMethod "$url/api/state" -Headers $headers -TimeoutSec 8
  if ($state.id -ne $expected.id -or
      (@($state.slots | ForEach-Object {$_.cards.Count}) -join ',') -ne
      (@($expected.slots | ForEach-Object {$_.cards.Count}) -join ',')) { throw 'Unexpected public puzzle' }
  foreach ($asset in @('index.html','app.mjs','style.css','support.mjs')) {
    $route=if ($asset -eq 'index.html') {'/'} else {"/$asset"}
    $response=Invoke-WebRequest "$url$route" -Headers $headers -UseBasicParsing -TimeoutSec 8
    if ($response.Content -cne [IO.File]::ReadAllText((Join-Path $PSScriptRoot $asset))) { throw "Unexpected asset: $asset" }
  }
}
$record=$null
if (Test-Path -LiteralPath $recordPath) { $record=Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json }
if ($Mode -eq 'Stop') {
  if ($record) { foreach ($entry in @($record.tunnel,$record.server)) { $owned=Find-OwnedProcess $entry; if ($owned) {Stop-Process -InputObject $owned} } }
  Write-Output 'Playtest stopped; sessions retained. Original Lab untouched.'
  exit
}
if ($Mode -eq 'Status') {
  if (!$record) { Write-Output 'Playtest not started.'; exit }
  $confirmed=$false;$problem=$null
  try { Probe-Public $record.url; $confirmed=$true } catch {$problem=$_.Exception.Message}
  [pscustomobject]@{URL=$record.url;ServerRunning=[bool](Find-OwnedProcess $record.server);TunnelRunning=[bool](Find-OwnedProcess $record.tunnel);PublicPuzzleConfirmed=$confirmed;Error=$problem}
  exit
}
if ($record -and ((Find-OwnedProcess $record.server) -or (Find-OwnedProcess $record.tunnel))) { throw 'Already running; use Status or Stop first.' }
if ($Port -eq 4183 -or $Port -lt 1024 -or $Port -gt 65535) {throw 'Choose a separate unprivileged port, not 4183.'}
$ancestor=$PrivateDirectory
while ($ancestor) {
  if (Test-Path -LiteralPath (Join-Path $ancestor '.git')) {throw 'Private data must be outside Git.'}
  $ancestor=Split-Path $ancestor -Parent
}
$fixture=Join-Path $PrivateDirectory 'fixture.json'
$agentPath=(Resolve-Path -LiteralPath (Join-Path $toolDirectory 'ngrok.exe')).Path
$configPath=(Resolve-Path -LiteralPath (Join-Path $toolDirectory 'ngrok.yml')).Path
$NodePath=(Resolve-Path -LiteralPath $NodePath).Path
if (!(Test-Path -LiteralPath $fixture)) {throw 'Frozen synthetic fixture is required.'}
foreach ($localPort in @($Port,4040)) {
  $listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$localPort)
  try {$listener.Start()} finally {$listener.Stop()}
}
$tunnel=$null;$server=$null
try {
  $tunnel=Start-Process -FilePath $agentPath -ArgumentList @('http',"http://127.0.0.1:$Port",'--config',('"{0}"' -f $configPath),'--inspect=false','--log=stdout','--log-format=json') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $toolDirectory 'agent.stdout.log') -RedirectStandardError (Join-Path $toolDirectory 'agent.stderr.log')
  $url=$null;$deadline=[DateTime]::UtcNow.AddSeconds(25)
  while (!$tunnel.HasExited -and [DateTime]::UtcNow -lt $deadline) {
    try {
      $tunnels=Invoke-RestMethod 'http://127.0.0.1:4040/api/tunnels' -TimeoutSec 1
      $url=@($tunnels.tunnels | Where-Object {$_.proto -eq 'https' -and $_.config.addr -eq "http://127.0.0.1:$Port"})[0].public_url
      if ($url) {break}
    } catch {}
    Start-Sleep -Milliseconds 300
  }
  if (!$url -or $url -notmatch '^https://[a-z0-9-]+\.(ngrok-free\.dev|ngrok-free\.app|ngrok\.app)$') {throw 'No expected HTTPS ngrok endpoint; inspect private agent logs.'}
  $server=Start-Process -FilePath $NodePath -ArgumentList @(('"{0}"' -f (Join-Path $PSScriptRoot 'server.mjs')),('"--fixture={0}"' -f $fixture),('"--state-dir={0}"' -f (Join-Path $PrivateDirectory 'sessions')),"--port=$Port","--public-origin=$url","--approved-ngrok-origin=$url") -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $toolDirectory 'server.stdout.log') -RedirectStandardError (Join-Path $toolDirectory 'server.stderr.log')
  $ready=$false
  for ($i=0;$i -lt 25 -and !$server.HasExited;$i++) {
    try {$response=Invoke-WebRequest "http://127.0.0.1:$Port/api/state" -UseBasicParsing -TimeoutSec 1; if ($response.StatusCode -eq 200) {$ready=$true;break}} catch {}
    Start-Sleep -Milliseconds 200
  }
  if (!$ready) {throw 'Local Puzzle Lab did not start.'}
  @{url=$url;port=$Port;server=(Process-Record $server);tunnel=(Process-Record $tunnel)} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $recordPath -Encoding UTF8
} catch {
  foreach ($process in @($server,$tunnel)) {if ($process -and !$process.HasExited) {Stop-Process -InputObject $process}}
  throw
}
try {Probe-Public $url; Write-Output "Public puzzle and assets verified: $url"} catch {Write-Warning "Processes running, but public verification failed: $($_.Exception.Message)"}
Write-Output 'Browser visitors may need to click Visit Site once. Independent visitor network test is still required.'
