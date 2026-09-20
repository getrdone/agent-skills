---
name: web-studio
description: >-
  Parent web craft for Grok, Codex, and Claude. Routes page work to
  deliverable-clone, deliverable-images, deliverable-theme, or deliverable-polish.
  Use for landing pages, ministry sites, screenshot-to-page, tokens, and one-off HTML edits.
  Do not use for Wix Velo. Use the authoritative library and preserve the existing project stack.
metadata:
  type: workflow
  version: "1.2.1"
  family: web-studio
  canonical: getrdone/agent-skills
---

# web-studio

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Current release: [1.2.0](versions/1.2.0/SKILL.md). Previous releases are available only on explicit selection.
