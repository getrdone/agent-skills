---
name: skill-router
description: Load a managed skill from the library when the user names it or types /skill-name. Ordinary chat loads no other managed skill.
---

# skill-router

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Read [CURRENT](CURRENT) or [STABLE](STABLE) to select the release. Previous releases are available only on explicit selection.
