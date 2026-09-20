# Canonical Windows distribution entrypoint. Codex | GPT-6 | 2026-09-20
[CmdletBinding()]
param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$runtime = $env:SKILL_PYTHON
if (-not $runtime) {
    $bundled = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    if (Test-Path -LiteralPath $bundled) { $runtime = $bundled }
    else { $runtime = (Get-Command python -ErrorAction Stop).Source }
}
$configPath = Join-Path $PSScriptRoot 'agent-homes.json'
$configuration = Get-Content -LiteralPath $configPath -Raw | ConvertFrom-Json
$stateDirectory = [Environment]::ExpandEnvironmentVariables($configuration.state)
$logDirectory = Join-Path $stateDirectory 'logs'
New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
$logPath = Join-Path $logDirectory 'sync-latest.log'
$arguments = @((Join-Path $PSScriptRoot 'library.py'), 'sync', '--config', $configPath)
if ($DryRun) { $arguments += '--dry-run' }
$exitCode = 1
try {
    if (-not (Test-Path -LiteralPath $runtime -PathType Leaf)) { throw "Python executable not found: $runtime" }
    $ErrorActionPreference = 'Continue'
    & $runtime @arguments 2>&1 | Tee-Object -FilePath $logPath
    $exitCode = $LASTEXITCODE
    if ($null -eq $exitCode) { $exitCode = 1 }
} catch {
    $_ | Out-File -LiteralPath $logPath -Append -Encoding utf8
} finally {
    $ErrorActionPreference = 'Stop'
    @{finished_at=(Get-Date).ToString('o');exit_code=$exitCode;dry_run=[bool]$DryRun;log=$logPath} |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $stateDirectory 'last-run.json') -Encoding utf8
}
exit $exitCode
