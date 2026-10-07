---
name: studio-web
description: Master web craft for Grok, Codex, Claude, and Scripture Journey. Use for HTML CSS JS pages, landing pages, ministry sites, web.build, web.repair, section edits, AEO SEO GEO, Core Web Vitals, container queries, motion, interactivity, and polished studio-quality pages. Do not load modern-html-aeo, modern-css-design, interactive-components, or optimized-deliverables with this skill.
metadata:
  version: "1.1"
  type: workflow
  canonical: getrdone/agent-skills
---

# Studio Web — one craft, two lanes

This skill is the **only** web implementation skill. Load this file after the router resolves CURRENT to 1.1.

Canonical Journey web long-form lives in CDSJ `web-experience.md`. Local clone `G:\\__AI-projects\\agent-skills\\`.

Declare before extra files:

```text
STUDIO-WEB: 1.1
LANE: web.build | web.repair
CHANGE: <section ids or new page>
FROZEN: <ids not to touch>
```

## Lanes

- `web.build` — this file + `references/page-anatomy.md`. Journey pages also load CDSJ web-experience + visual-system.
- `web.repair` — this file + `references/repair-contract.md` only.

Journey content stays in CDSJ other lanes. This skill owns HTML/CSS/JS craft.

## Constitution

1. Works in a real browser. Dead primary controls = FAIL.
2. Looks premium. Cream + Inter as the whole personality = FAIL.
3. Motion and JS are first-class. Full motion default. reduced-motion is an optional query.
4. Performance without flattening. Fix the asset, do not delete the picture.
5. Readable text. Target 7:1. Floor WCAG 2.2 AA.
6. Container-query-first. No viewport min-width for component layout. TUNE tokens for type, stack, inset, gutter, measure, radius, motion — `references/page-anatomy.md`.
7. One primary action per view.
8. Surgical by default. Snapshot `index_vN.html` only before an outline rewrite.

## Build

Canonical `deliverables/index.html`. Network webfonts. Stable region ids. Hero image eager. JS CONFIG at top. JSON-LD only if it matches visible content.

## Repair

Follow `references/repair-contract.md`. Edit named ids only. Edit TUNE tokens for size/space. Do not regenerate the whole file from memory.

## Quality

PASS / FAIL / BLOCKED. Journey pages run CDSJ `scripts/audit_html.py` when that repo is the work root.
