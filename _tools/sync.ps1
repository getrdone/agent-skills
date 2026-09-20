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
$arguments = @((Join-Path $PSScriptRoot 'library.py'), 'sync', '--config', (Join-Path $PSScriptRoot 'agent-homes.json'))
if ($DryRun) { $arguments += '--dry-run' }
& $runtime @arguments
exit $LASTEXITCODE
