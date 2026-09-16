---
name: multi-cli-dispatch
description: >-
  Use when dispatching work across goBot, Grok CLI, or Codex exec — job cards,
  per-run effort, background watcher, DONE/BLOCKED without babysitting, delete gate.
---
# Multi-CLI dispatch

## When
Steve needs a job on **goBot**, **Grok CLI**, or **Codex** with a chosen effort, running in the background without agents watching the CLI.

## Defaults
- **cwd:** `G:\__ai-projects` unless the job names a child project.
- **Effort:** per job (`low` | `medium` | `high`; `extra-heavy` only with `-AllowExtraHeavy`).
- **Avoid:** Grok extra-heavy and Codex Astra unless the card explicitly requires them.
- **Never** two jobs share the same `slice_id` (dual-drive). Different efforts = different slice_ids.

## Background self-sufficiency
1. `New-Job.ps1` → `Start-JobLane.ps1`
2. Ensure watcher: `Start-JobWatcher.ps1` (polls ~30s; writes `STATUS-BOARD.md` + `notify/`)
3. Do **not** poll CLIs from chat. Read board / notify, or wait for the notify routine.

Watcher **moves job folders only** — never deletes project/media files.

## Parallel multi-effort (same project)
**Yes:** enqueue N jobs with N slice_ids, e.g. `-ProjectTag final-days-switcher -Effort low` … `-Effort high`.

**Guardrail:** do not let all of them **write the same files**. Prefer review-only outputs, separate branches/worktrees, or apply only the winning effort afterward. Parallel *writers* on one `index.html` waste quota and collide.

## Delete gate
See `jobs/DELETE-POLICY.md`. Report-only by default. Steve must add `APPROVE-DELETE.md` after reviewing `DELETE-PROPOSAL.md`. Use `Test-ApproveDelete.ps1` before any apply job. **No silent deletes.**

## Scripts
Root: `G:\__ai-projects\_agent-control\jobs\`

- `bin\New-Job.ps1 -Goal "…" -Lane grok|codex|gobot -Effort medium -Cwd <path> [-ProjectTag tag]`
- `bin\Start-JobLane.ps1 -Id <id>`
- `bin\Complete-Job.ps1 -Id <id>` (watcher usually calls this)
- `bin\Watch-Jobs.ps1` / `bin\Start-JobWatcher.ps1`
- `bin\Test-ApproveDelete.ps1 -JobDir <dir>`

## Kick shapes
- Grok: `grok --prompt-file … --cwd … --reasoning-effort low|medium|high`
- Codex: `codex exec -` from cwd (effort is prompt-level; avoid Astra)

## Markers
- `DONE.flag` — finished (JSON summary)
- `BLOCKED.md` — needs Steve
- `CLAIM.md` — gobot lane claim in chat (not a human block)
