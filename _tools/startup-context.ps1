# Fresh job context from the canonical library. No Git pull or automatic restart.
# Codex | GPT-6 | 2026-09-20
$ErrorActionPreference = 'Stop'
$libraryRoot = Split-Path -Parent $PSScriptRoot
$release = (Get-Content -LiteralPath (Join-Path $libraryRoot 'release-index.json') -Raw | ConvertFrom-Json).release
$context = "Authoritative skills release: $release at $libraryRoot. Read CATALOG.md when discovering skills; coding work uses coding-workflow. Resolve CURRENT/STABLE dynamically, never a legacy skill or alias. Follow WORKSPACE.md: drafts, temporary plans and diagnostic artifacts belong in project _wip; reusable project tools belong in _tools. Search the master _tools/TOOLS.md before creating utilities. Complete the full authorized request in small verifiable chunks without time quotas, inactivity deadlines, or automatic kills. Suitable modular architectures and Motion, GSAP, Remotion and Lottie are allowed. Read project 01-NOW.md and 02-TASKS.md; consult 03-MEMORY.md before changing settled decisions."
@{hookSpecificOutput=@{hookEventName='SessionStart';additionalContext=$context}} | ConvertTo-Json -Compress -Depth 4
