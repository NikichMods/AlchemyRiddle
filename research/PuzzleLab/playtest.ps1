# SPDX-License-Identifier: MPL-2.0
[CmdletBinding()]
param(
  [ValidateSet('Start','Stop','Status')][string]$Mode = 'Status',
  [Parameter(Mandatory)][string]$PrivateDirectory,
  [string]$NodePath,
  [string]$CloudflaredPath,
  [int]$Port = 4184,
  [ValidateSet('auto','http2','quic')][string]$Protocol = 'auto',
  [ValidateSet('global','us')][string]$Region = 'global'
)
$ErrorActionPreference = 'Stop'
$PrivateDirectory = [IO.Path]::GetFullPath($PrivateDirectory)
$recordPath = Join-Path $PrivateDirectory 'running.json'
function Test-PublicPuzzle([string]$Url, [string]$FixturePath) {
  $probe = @{puzzleMatched=$false;assetsMatched=$false;checkedAt=[DateTime]::UtcNow.ToString('o');error=$null}
  try {
    $expected = Get-Content -LiteralPath $FixturePath -Raw | ConvertFrom-Json
    $publicPuzzle = Invoke-RestMethod "$Url/api/state" -TimeoutSec 8
    $probe.puzzleMatched = $publicPuzzle.id -eq $expected.id -and
      (@($publicPuzzle.slots | ForEach-Object { $_.cards.Count }) -join ',') -eq
      (@($expected.slots | ForEach-Object { $_.cards.Count }) -join ',')
    if (!$probe.puzzleMatched) { throw 'Unexpected public puzzle response' }
    foreach ($asset in @('index.html','app.mjs','style.css')) {
      $path = if ($asset -eq 'index.html') {'/'} else {"/$asset"}
      $response = Invoke-WebRequest "$Url$path" -UseBasicParsing -TimeoutSec 8
      $expectedAsset = [IO.File]::ReadAllText((Join-Path $PSScriptRoot $asset))
      if ($response.Content -cne $expectedAsset) { throw "Incomplete or unexpected public asset: $asset" }
    }
    $probe.assetsMatched = $true
  } catch { $probe.error = $_.Exception.Message }
  return $probe
}
function Find-OwnedProcess($entry) {
  $candidate = Get-Process -Id $entry.id -ErrorAction SilentlyContinue
  if ($candidate -and $candidate.Path -eq $entry.path -and
      $candidate.StartTime.ToUniversalTime().ToString('o') -eq ([DateTime]$entry.startedAt).ToUniversalTime().ToString('o')) { return $candidate }
  return $null
}
if (Test-Path -LiteralPath $recordPath) { $record = Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json }
if ($Mode -eq 'Status') {
  if (!$record) { Write-Output 'Playtest is stopped.'; exit }
  $probe = Test-PublicPuzzle $record.url (Join-Path $PrivateDirectory 'fixture.json')
  [pscustomobject]@{URL=$record.url;ServerRunning=[bool](Find-OwnedProcess $record.server);TunnelRunning=[bool](Find-OwnedProcess $record.tunnel);PublicPuzzleConfirmed=($probe.puzzleMatched -and $probe.assetsMatched);PublicError=$probe.error;Sessions=(Join-Path $PrivateDirectory 'sessions')}
  exit
}
if ($Mode -eq 'Stop') {
  if ($record) {
    foreach ($entry in @($record.tunnel,$record.server)) {
      $owned = Find-OwnedProcess $entry
      if ($owned) { Stop-Process -InputObject $owned }
    }
  }
  Write-Output 'Playtest stopped; sessions retained. Original Lab is unaffected.'
  exit
}
if ($record -and ((Find-OwnedProcess $record.server) -or (Find-OwnedProcess $record.tunnel))) {
  throw 'This playtest is already running. Use Status or Stop first.'
}
$fixture = Join-Path $PrivateDirectory 'fixture.json'
if (!(Test-Path -LiteralPath $fixture)) { throw 'Put a frozen synthetic fixture.json in the private directory first.' }
if (!$CloudflaredPath) { $CloudflaredPath = Join-Path $PrivateDirectory 'cloudflared.exe' }
if (!$NodePath) { $NodePath = (Get-Command node -ErrorAction Stop).Source }
$CloudflaredPath = (Resolve-Path -LiteralPath $CloudflaredPath).Path
$NodePath = (Resolve-Path -LiteralPath $NodePath).Path
$serverScript = Join-Path $PSScriptRoot 'server.mjs'
# Require a private location outside any Git checkout, including worktree .git files.
$ancestor = $PrivateDirectory
while ($ancestor) {
  if (Test-Path -LiteralPath (Join-Path $ancestor '.git')) { throw 'Session data must be outside Git.' }
  $ancestor = Split-Path $ancestor -Parent
}
# Never use the preserved player's port, nor an occupied local port.
if ($Port -eq 4183 -or $Port -lt 1024 -or $Port -gt 65535) { throw 'Choose a separate unprivileged port, not 4183.' }
$probe = [Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$Port)
try { $probe.Start() } finally { $probe.Stop() }
$tunnel = $null; $server = $null
try {
  $tunnelArgs = @('tunnel','--no-autoupdate','--url',"http://127.0.0.1:$Port",'--protocol',$Protocol)
  if ($Region -eq 'us') { $tunnelArgs += @('--region','us') }
  $tunnel = Start-Process -FilePath $CloudflaredPath -ArgumentList $tunnelArgs -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $PrivateDirectory 'tunnel.stdout.log') -RedirectStandardError (Join-Path $PrivateDirectory 'tunnel.stderr.log')
  $deadline = [DateTime]::UtcNow.AddSeconds(55)
  $url = $null
  while ([DateTime]::UtcNow -lt $deadline -and !$tunnel.HasExited) {
    $log = Get-Content -LiteralPath (Join-Path $PrivateDirectory 'tunnel.stderr.log') -Raw -ErrorAction SilentlyContinue
    if ($log -match 'https://[a-z0-9-]+\.trycloudflare\.com') { $url = $Matches[0]; break }
    Start-Sleep -Milliseconds 300
  }
  if (!$url) { throw 'Quick Tunnel did not return a URL. Inspect private tunnel.stderr.log.' }
  $server = Start-Process -FilePath $NodePath -ArgumentList @(('"{0}"' -f $serverScript),('"--fixture={0}"' -f $fixture),('"--state-dir={0}"' -f (Join-Path $PrivateDirectory 'sessions')),"--port=$Port","--public-origin=$url") -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $PrivateDirectory 'server.stdout.log') -RedirectStandardError (Join-Path $PrivateDirectory 'server.stderr.log')
  $ready = $false
  for ($i=0;$i -lt 30 -and !$server.HasExited;$i++) {
    try { $response = Invoke-WebRequest "http://127.0.0.1:$Port/" -UseBasicParsing -TimeoutSec 1; $ready = $response.StatusCode -eq 200; if ($ready) { break } } catch {}
    Start-Sleep -Milliseconds 200
  }
  if (!$ready -or $tunnel.HasExited) { throw 'Playtest startup failed. Inspect private logs.' }
  $record = @{url=$url;port=$Port;protocol=$Protocol;region=$Region;fixtureSHA256=(Get-FileHash -LiteralPath $fixture).Hash.ToLower();server=@{id=$server.Id;path=$server.Path;startedAt=$server.StartTime.ToUniversalTime().ToString('o')};tunnel=@{id=$tunnel.Id;path=$tunnel.Path;startedAt=$tunnel.StartTime.ToUniversalTime().ToString('o')}}
  $record | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $recordPath -Encoding utf8
  # A URL and registered connection do not prove that the puzzle can be reached.
  $publicProbe = Test-PublicPuzzle $url $fixture
  $record.publicProbe = $publicProbe
  $record | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $recordPath -Encoding utf8
  Write-Output "Local puzzle: http://127.0.0.1:$Port/"
  if ($publicProbe.puzzleMatched -and $publicProbe.assetsMatched) { Write-Output "Public puzzle and complete assets responded: $url" }
  else { Write-Output "PUBLIC ACCESS NOT CONFIRMED: $url"; Write-Output $publicProbe.error }
  Write-Output 'Keep this PC awake and online. Stop with the same script and -Mode Stop.'
} catch {
  foreach ($child in @($server,$tunnel)) { if ($child -and !$child.HasExited) { Stop-Process -InputObject $child } }
  throw
}
