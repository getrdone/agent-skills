---
name: studio-web
description: Master web craft for Grok, Codex, Claude, and Scripture Journey. Use for HTML CSS JS pages, landing pages, ministry sites, web.build, web.repair, section edits, AEO SEO GEO, Core Web Vitals, container queries, motion, interactivity, and polished studio-quality pages. Do not load modern-html-aeo, modern-css-design, interactive-components, or optimized-deliverables with this skill.
metadata:
  type: workflow
  canonical: getrdone/agent-skills
---

# Studio Web — version router

Versions live in subfolders. Do not treat a git branch name as a release.

```text
skills/studio-web/
  SKILL.md          # this router
  CURRENT           # default release, e.g. 1.1
  1.1/SKILL.md
  1.1/references/
```

1. If the user names a version (`1.1`, `studio-web/1.1`), load that folder's `SKILL.md`.
2. Otherwise read `CURRENT` and load `studio-web/<that>/SKILL.md`.
3. Every relative path in a release (`references/page-anatomy.md`) resolves under that version folder.
4. Do not mix files from two releases.

Current: **1.1** (file `CURRENT`)

Declare after resolving:

```text
STUDIO-WEB: 1.1
LANE: web.build | web.repair
```

Then open only `1.1/SKILL.md` and the reference that lane names.
