---
name: multi-cli-dispatch
description: >-
  Use when dispatching work across goBot, Grok CLI, or Codex exec — job cards,
  per-run effort, background watcher, DONE/BLOCKED without babysitting, delete gate.
---

# multi-cli-dispatch

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Read [CURRENT](CURRENT) or [STABLE](STABLE) to select the release. Previous releases are available only on explicit selection.
