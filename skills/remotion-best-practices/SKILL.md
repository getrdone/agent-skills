---
name: remotion-best-practices
description: Router for all Remotion skills. Load only when the user asks for Remotion, compositions, captions, Player, Studio, or related video-code work.
version: 4.0.506
---

# remotion-best-practices

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Current release: [1.1.0](versions/1.1.0/SKILL.md). Previous releases are available only on explicit selection.
