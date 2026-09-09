---
name: curiosity-driven-scripture-journey
description: Plan, package, design, write, build, or review a curiosity-driven Scripture content project. Use for titles, descriptions, thumbnails, YouTube packaging, Bible-study questions and copy, topic discovery, ministry landing pages, and high-trust faith content. Version router — resolve CURRENT unless the user names a version or says stable.
---

# Curiosity-Driven Scripture Journey — version router

1. If the user names an exact version, load `versions/<version>/manifest.yaml` and that version's `SKILL.md`.
2. If the user says `stable`, resolve `STABLE`.
3. Otherwise resolve `CURRENT`.
4. Load only references belonging to the resolved Scripture Journey version.
5. Do not silently mix Scripture Journey reference files from another version.
6. Shared cross-skill dependencies are governed by the selected release manifest and the repository commit containing that release.

Current: **3.2.0** (file `CURRENT`)  
Stable: **3.0.1** (file `STABLE`)

`versions/` is history. Load it only when the user names that release. Skill scanners (Grok `[skills].ignore`, junctions to this folder) must not advertise `versions/*/SKILL.md` as separate skills.

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->

<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Released 3.2.0 color psychology and text-readability requirements. -->
<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-09-09 · Router description includes titles/descriptions so auto-invoke matches. -->
