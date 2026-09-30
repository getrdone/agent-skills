# Fresh job context from the canonical library. No Git pull or automatic restart.
# Codex | GPT-6 | 20260920
# Agent: grok · Model: Grok 4.6 · Thinking: not exposed · Date: 20260920
# Keep this script ASCII. Grok's SessionStart hook runs it with powershell.exe (Windows PowerShell 5.1), which misparses UTF-8 punctuation such as em-dashes.
$ErrorActionPreference = 'Stop'
$libraryRoot = Split-Path -Parent $PSScriptRoot
$release = (Get-Content -LiteralPath (Join-Path $libraryRoot 'release-index.json') -Raw | ConvertFrom-Json).release
$context = "Authoritative skills release: $release at $libraryRoot.  Video Library is a default for specifically requested videos: load skills/video-library/CURRENT, record each new request once with its counter, and send web/cloud handoffs to local ChatGPT Work/Codex using available messaging tools; label unsent handoffs honestly. Default voice: lean-output and i-have-adhd - talk to a person, no inner-agent chatter. When a specialist is needed, read CATALOG.md for the name, then load that skill's CURRENT file only. Do not load the rest until named. Never mix releases. Never load retired names; use web-studio. Project memory is on disk: 01-NOW.md, 03-MEMORY.md, image-slots.md; the task queue is the single database todos.db, read with _agent-control\bin\open-tasks.ps1. Dates are YYYY-MMDD, e.g. 2026-0930. History is opt-in; provenance goes in the commit trailer. Graphics does not edit HTML. Code does not invent image paths. Drafts in project _wip; tools in _tools after checking TOOLS.md."
@{hookSpecificOutput=@{hookEventName='SessionStart';additionalContext=$context}} | ConvertTo-Json -Compress -Depth 4
