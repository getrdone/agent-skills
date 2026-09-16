---
name: web-studio
description: >-
  Parent web craft for Grok, Codex, and Claude. Routes page work to
  deliverable-clone, deliverable-images, deliverable-theme, or deliverable-polish.
  Use for landing pages, ministry sites, screenshot-to-page, tokens, and one-off HTML edits.
  Do not use for Wix Velo. Do not load html-page-standard, studio-web,
  modern-web-development, modern-html-aeo, modern-css-design, interactive-components,
  or optimized-deliverables.
metadata:
  type: workflow
  version: "1.1"
  family: web-studio
  canonical: getrdone/agent-skills
---

# Web studio

This file is the router. Do not build a page from this file alone.

Declare before writing files:

```text
WEB-STUDIO: 1.1
HTML-DELIVERABLE: clone | images | theme | polish
STACK: static-html | react-tailwind-shadcn
SOURCE: <one file or none>
EDIT: <one line or none>
```

Then open **only** the matching file:

| User intent | Open |
|---|---|
| New page from one screenshot, mockup, or HTML source | `deliverable-clone.md` |
| Fill / generate graphics for named image slots on an existing clone | `deliverable-images.md` |
| Palette, type, rhythm, data-theme on an existing page | `deliverable-theme.md` |
| One named fix (copy, control, one image swap) | `deliverable-polish.md` |

## Default phase order

1. **clone** — layout / structure first  
2. **images** — graphics into named slots (image-direction skills)  
3. **theme** — tokens / palette / rhythm  
4. **polish** — one named fix  

One phase per turn unless the user chains phases by name.

If the user already has a living page, do not open clone.

## Defaults

- Ministry / Scripture Journey / Final Days — `STACK: static-html` unless the user names React.
- Stack is written in `DELIVERABLE.md` at clone and does not change unless the user names a migration.
- Other skills (Scripture Journey, YouTube, copy) call this family. They do not invent an HTML pipeline.

## Consult / required companions

- **Dynamic Symmetry (required on clone + images)** — `skills/dynamic-symmetry/SKILL.md` (see `references/dynamic-symmetry.md` pointer)
- Writing style — `references/voice.md` plus the calling skill’s brief
- Interaction — `references/interaction.md`
- Image slot names — `references/image-slots.md`
- New/revised palettes — `skills/color-palette-composition/SKILL.md` (from theme)
- Anti-slop taste on polish — `skills/design-taste-frontend/SKILL.md` or `skills/high-end-visual-design/SKILL.md`

## Do not

- Keep or mention `html-page-standard` as an alias
- Load `studio-web`, `modern-web-development`, or any `claude-skills` nest
- Run clone + images + theme + polish in one turn unless the user chains them by name
- Flatten a finished React tree to static HTML to “simplify”
- Replace a video or hero region with one baked screenshot

<!-- Agent: Grok · Model: Grok 4.5 · Date: 2026-09-16 · Added images phase; wired image-direction companions. -->
