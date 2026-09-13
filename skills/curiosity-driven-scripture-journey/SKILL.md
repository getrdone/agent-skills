---
name: curiosity-driven-scripture-journey
description: Plan, package, design, write, build, or review a curiosity-driven Scripture content project. Use for titles, descriptions, thumbnails, YouTube packaging, Bible-study questions and copy, topic discovery, ministry landing pages, and high-trust faith content. Version router — resolve CURRENT unless the user names a version or says stable.
---

# Curiosity-Driven Scripture Journey — version router

1. If the user names an exact version, load `versions/<version>/manifest.yaml` and that version's `SKILL.md`.
2. If the user says `stable`, resolve `STABLE`.
3. Otherwise resolve `CURRENT`.
4. Read that version's `load-map.yaml`, match the request to its lanes, and load **only** the files those lanes name.
5. Do not silently mix Scripture Journey reference files from another version.
6. Shared cross-skill dependencies are governed by the selected release manifest and the repository commit containing that release.
7. For a new or materially revised color theme, use the selected release's `palette` lane. It opens the canonical `color-palette-composition` skill; load Color Psychology only when contextual interpretation materially changes the palette decision.

Current: **3.2.0** (file `CURRENT`)
Stable: **3.0.1** (file `STABLE`)

## Path resolution (read this before opening any file)

**Every relative path inside a version's `SKILL.md`, `load-map.yaml`, or reference files resolves under
`versions/<resolved-version>/`.** When 3.2.0 says `references/quality-gates.md`, the file is
`versions/3.2.0/references/quality-gates.md`. When `v3-quality.md` says `scripts/audit_html.py`, the file
is `versions/3.2.0/scripts/audit_html.py`.

There is **no** `references/` or `scripts/` directory beside this file, and there must never be one again.
A second copy of a reference at the skill root is how two agents obeying the same instruction end up with
different content. Paths prefixed `repo:` in `load-map.yaml` resolve from the repository root.

## Declare what you loaded

Before loading anything, emit:

```text
LANES: <lane>[, <lane>...]
LOAD:  <one path per line — exactly the files you open>
BRIEF: <path>/project-brief.md  (stage: <status>)     # when a work folder exists
```

Refuse a full-tree load. If a lane's `max_files` is not enough, say so in one line and name the extra file.

## Workspace

File naming, file I/O, and continuity are defined **only** in repo root
[`WORKSPACE.md`](../../WORKSPACE.md). Read it when creating or naming files. No skill or reference
restates its rules.

## Version history

`versions/` is history. Load a past release only when the user names it. Skill scanners (Grok
`[skills].ignore`, junctions to this folder) must not advertise `versions/*/SKILL.md` as separate skills.

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->
<!-- Agent: Codex · Model: GPT-5 · Thinking: not exposed · Date: 2026-09-09 · Released 3.2.0 color psychology and text-readability requirements. -->
<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-09-09 · Router description includes titles/descriptions so auto-invoke matches. -->
<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Deleted the duplicate root references/ tree and root manifest.yaml; stated the one path-resolution rule; added load-map routing and the LOAD declaration. -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Added the release-resolved canonical palette route. -->
