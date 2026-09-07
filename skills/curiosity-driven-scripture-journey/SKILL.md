---
name: curiosity-driven-scripture-journey
description: Version router for the Curiosity-Driven Scripture Journey skill.
---

# Curiosity-Driven Scripture Journey — version router

1. If the user names an exact version, load `versions/<version>/manifest.yaml` and that version's `SKILL.md`.
2. If the user says `stable`, resolve `STABLE`.
3. Otherwise resolve `CURRENT`.
4. Load only references belonging to the resolved Scripture Journey version.
5. Do not silently mix Scripture Journey reference files from another version.
6. Shared cross-skill dependencies are governed by the selected release manifest and the repository commit containing that release.

Current: **3.0.0**  
Stable: **3.0.0**
