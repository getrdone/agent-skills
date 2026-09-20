# Preserve the existing trigger and principal; back up before changing the task.
[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$BackupDirectory)
$ErrorActionPreference = 'Stop'
$taskName = 'AgentSkillsRobocopy'
$task = Get-ScheduledTask -TaskName $taskName -ErrorAction Stop
New-Item -ItemType Directory -Path $BackupDirectory -Force | Out-Null
$snapshot = Join-Path $BackupDirectory ('AgentSkillsRobocopy-' + (Get-Date -Format 'yyyyMMdd-HHmmss-ffff') + '.xml')
$xml = Export-ScheduledTask -TaskName $taskName
[IO.File]::WriteAllText($snapshot, $xml)
if ([IO.File]::ReadAllText($snapshot) -ne $xml) { throw 'Task backup mismatch' }
$launcher = Join-Path $PSScriptRoot 'sync-hidden.vbs'
if (-not (Test-Path -LiteralPath $launcher)) { throw 'Missing canonical launcher' }
$action = New-ScheduledTaskAction -Execute "$env:WINDIR\System32\wscript.exe" -Argument ('//B //NoLogo "' + $launcher + '"')
$settings = $task.Settings
$settings.ExecutionTimeLimit = 'PT0S'
$settings.MultipleInstances = 'IgnoreNew'
Set-ScheduledTask -TaskName $taskName -Action $action -Settings $settings | Out-Null
Enable-ScheduledTask -TaskName $taskName | Out-Null
Get-ScheduledTask -TaskName $taskName | Select-Object TaskName,State,@{n='ExecutionTimeLimit';e={$_.Settings.ExecutionTimeLimit}},@{n='Overlap';e={$_.Settings.MultipleInstances}}
