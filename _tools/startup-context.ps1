# Fresh job context from the canonical library. No Git pull or automatic restart.
# Codex | GPT-6 | 2026-09-20
$ErrorActionPreference = 'Stop'
$libraryRoot = Split-Path -Parent $PSScriptRoot
$release = (Get-Content -LiteralPath (Join-Path $libraryRoot 'release-index.json') -Raw | ConvertFrom-Json).release
$context = "Authoritative skills release: $release at $libraryRoot. Default voice: lean-output and i-have-adhd — talk to a person, no inner-agent chatter. When a specialist is needed, read CATALOG.md for the name, then load that skill's CURRENT file only. Do not load the rest until named. Never mix releases. Never load retired names; use web-studio. Project memory is on disk: 01-NOW.md, 02-TASKS.md, 03-MEMORY.md, image-slots.md. Graphics does not edit HTML. Code does not invent image paths. Drafts in project _wip; tools in _tools after checking TOOLS.md."
@{hookSpecificOutput=@{hookEventName='SessionStart';additionalContext=$context}} | ConvertTo-Json -Compress -Depth 4
