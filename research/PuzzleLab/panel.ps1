# SPDX-License-Identifier: MPL-2.0
[CmdletBinding()]
param([ValidateSet('Start','Stop','Status')][string]$Mode='Start',
  [Parameter(Mandatory)][string]$PrivateDirectory,[Parameter(Mandatory)][string]$NodePath,[int]$Port=4185)
$ErrorActionPreference='Stop'
$PrivateDirectory=[IO.Path]::GetFullPath($PrivateDirectory)
$path=Join-Path $PrivateDirectory 'ngrok/panel-process.json'
$record=$null;$process=$null
if(Test-Path -LiteralPath $path){$record=Get-Content -LiteralPath $path -Raw | ConvertFrom-Json;$candidate=Get-Process -Id $record.id -ErrorAction SilentlyContinue
  if($candidate -and $candidate.Path -eq $record.path -and $candidate.StartTime.ToUniversalTime().ToString('o') -eq ([DateTime]$record.startedAt).ToUniversalTime().ToString('o')){$process=$candidate}}
if($Mode -eq 'Stop'){if($process){Stop-Process -InputObject $process;Wait-Process -InputObject $process -Timeout 5 -ErrorAction SilentlyContinue};Write-Output 'Private panel stopped; playtest and sessions untouched.';exit}
if($Mode -eq 'Status'){[pscustomobject]@{PanelRunning=[bool]$process;URL=if($record){"http://127.0.0.1:$($record.port)/"}else{$null}};exit}
if($process){Write-Output "Private panel: http://127.0.0.1:$($record.port)/";exit}
if($Port -in @(4183,4184) -or $Port -lt 1024 -or $Port -gt 65535){throw 'Choose a separate unprivileged panel port.'}
$ancestor=$PrivateDirectory
while($ancestor){if(Test-Path -LiteralPath (Join-Path $ancestor '.git')){throw 'Private directory must be outside Git.'};$ancestor=Split-Path $ancestor -Parent}
if(!(Test-Path -LiteralPath (Join-Path $PrivateDirectory 'sessions'))){throw 'Private playtest directory not found.'}
$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$Port)
try{$listener.Start()}finally{$listener.Stop()}
$NodePath=(Resolve-Path -LiteralPath $NodePath).Path
$process=Start-Process -FilePath $NodePath -ArgumentList @(('"{0}"' -f (Join-Path $PSScriptRoot 'admin.mjs')),('"--private-dir={0}"' -f $PrivateDirectory),('"--node={0}"' -f $NodePath),"--port=$Port") -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $PrivateDirectory 'ngrok/panel.stdout.log') -RedirectStandardError (Join-Path $PrivateDirectory 'ngrok/panel.stderr.log')
@{id=$process.Id;path=$NodePath;startedAt=$process.StartTime.ToUniversalTime().ToString('o');port=$Port} | ConvertTo-Json | Set-Content -LiteralPath $path -Encoding UTF8
Write-Output "Private panel: http://127.0.0.1:$Port/"
