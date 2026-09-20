---
name: lean-output
description: Activate when the user wants concise, high-density answers with low token cost. Triggers include lean, brief, short answer, no fluff, tldr, token savings, high information density, skip preamble.
metadata:
  version: "1.2"
  type: style
  status: testing
  note: Refines 1.1 to prevent over-trimming while preserving high information density.
---

# lean-output

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Current release: [1.1.0](versions/1.1.0/SKILL.md). Previous releases are available only on explicit selection.
