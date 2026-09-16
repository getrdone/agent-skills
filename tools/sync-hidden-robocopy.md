# Hidden robocopy sync

Canonical tool: `G:\__ai-projects\_agent-tools\sync-agent-skills\`

- Source: `G:\__ai-projects\_agent-skills\skills`
- Destinations: `agent-homes.txt` (`.grok`, `.codex`, `.agents`, `.claude`, `.cursor`, `.openclaw`, …)
- Task: `AgentSkillsRobocopy` (15 minutes, hidden)
- Register: `register-sync-hidden.cmd`
- Manual: `sync-all-agents.cmd`
- Purge: `purge-retired-local.cmd` / `purge-retired-local.cmd 1`

Copies **`skills\` only** (not the repo root). Does not `git pull`. Avoid `/MIR` until a home is only a mirror.

Allowlist / layout standard: `../CATALOG.md`. Page work: `skills/web-studio/` only (`clone` → `images` → `theme` → `polish`).
