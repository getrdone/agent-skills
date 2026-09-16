---
name: web-studio
description: Parent web craft for Grok, Codex, and Claude. Routes page work to deliverable-clone, deliverable-theme, or deliverable-polish. Use for landing pages, ministry sites, screenshot-to-page, tokens, and one-off HTML edits. Do not use for Wix Velo. Do not load html-page-standard, studio-web, modern-web-development, modern-html-aeo, modern-css-design, interactive-components, or optimized-deliverables.
metadata:
  type: workflow
  version: "1.0"
  family: web-studio
  canonical: getrdone/agent-skills
---

# Web studio

This file is the router. Do not build a page from this file alone.

Declare before writing files:

```text
WEB-STUDIO: 1.0
HTML-DELIVERABLE: clone | theme | polish
STACK: static-html | react-tailwind-shadcn
SOURCE: <one file or none>
EDIT: <one line or none>
```

Then open **only** the matching file:

| User intent | Open |
|---|---|
| New page from one screenshot, mockup, or HTML source | `deliverable-clone.md` |
| Palette, type, rhythm, data-theme on an existing page | `deliverable-theme.md` |
| One named fix (copy, control, one image swap) | `deliverable-polish.md` |

If the user already has a living page, do not open clone.

## Defaults

- Ministry / Scripture Journey / Final Days — `STACK: static-html` unless the user names React.
- Stack is written in `DELIVERABLE.md` at clone and does not change unless the user names a migration.
- Other skills (Scripture Journey, YouTube, copy) call this family. They do not invent an HTML pipeline.

## Consult only (never a fourth lane)

- Writing style — `references/voice.md` plus the calling skill’s brief
- Interaction — `references/interaction.md`
- Image slot names — `references/image-slots.md`

## Do not

- Keep or mention `html-page-standard` as an alias
- Load `studio-web` or `modern-web-development`
- Run clone + theme + polish in one turn unless the user chains them by name
- Flatten a finished React tree to static HTML to “simplify”
- Replace a video or hero region with one baked screenshot

<!-- Agent: Grok · Model: Grok 4.6 · Date: 2026-09-15T21:05:00-07:00 · First release. -->
