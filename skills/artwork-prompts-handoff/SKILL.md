---
name: artwork-prompts-handoff
description: >
  Create a numbered, paste-ready artwork prompt pack for manual generation in the user's chosen tools.
  Use only when the user explicitly asks for prompts, an art handoff, or says they will generate the
  images themselves. Do not intercept ordinary requests to generate or edit an image directly.
---

# artwork-prompts-handoff

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Current release: [1.1.0](versions/1.1.0/SKILL.md). Previous releases are available only on explicit selection.
