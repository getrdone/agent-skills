---
name: html-page-standard
description: Default contract for new static HTML pages from screenshots, bitmap mockups, or raster designs. Use for HTML projects, landing pages, clone a screenshot, tokenize CSS, TUNE blocks, theme tokens, studio-web repair after clone, layout packs. Do not use for Wix Velo-only edits or when the user names a different pipeline.
metadata:
  type: workflow
  version: "1.0"
  canonical: getrdone/agent-skills
---

# HTML page standard

Canonical pipeline for static HTML going forward. This skill is the router. Do not implement a whole page from this file alone.

Declare before writing files:

```text
HTML-PAGE-STANDARD: 1.0
PASS: A-clone | B-tokenize | C-repair | layout-pack
```

Load only the owner of the current pass. Never let screenshot-to-html and studio-web co-author the first draft.

## Pass owners

| Pass | Owner | Output |
|---|---|---|
| A-clone | `screenshot-to-html` only | `source.png` + `clone.html` |
| B-tokenize | this skill + `references/tokenize-contract.md` | `core.css` + `theme-default.css` |
| C-repair | studio-web 1.1 `web.repair` | `index.html` from clone, semantics, a11y, motion |
| layout-pack | this skill + `references/layout-packs.md` | optional `layout-*.css` |

If the user gives a live URL or existing HTML (no screenshot to clone), skip A. Tokenize if tokens are missing, then C.

If the screenshot is only a mood, not a facsimile, skip A and use studio-web `web.build` instead. Say so before writing.

## Hard rules

1. One pass per turn unless the user explicitly chains them.
2. Every new page ships TUNE + a theme file even when there is only one look.
3. TUNE owns rhythm. Theme owns look. Layout packs own arrangement. HTML owns copy.
4. After Pass B, no raw `font-size`, `padding`, `margin`, or `gap` when a token exists.
5. No viewport width breakpoints for component layout. Regions are `@container` + `cqi`.
6. Themes must not change the DOM. Layout packs must not change the palette.
7. Do not add a second theme or a layout pack on page one unless asked.
8. Wix Velo work is out of scope.

## Folder contract

```text
<page>/
  source.png
  clone.html
  core.css
  theme-default.css
  index.html
```

Optional later: `theme-<name>.css`, `layout-<name>.css`. Root attributes: `data-theme="default"` and `data-layout="default"`.

Layers: `@layer reset, core, theme, layout, page;`

## Load map

- Pass A — load screenshot-to-html. Stop when `clone.html` matches the picture.
- Pass B — load `references/tokenize-contract.md`. Copy `assets/core.template.css` and `assets/theme-default.template.css`, then fill numbers from the clone. Do not redesign.
- Pass C — load studio-web 1.1, lane `web.repair`, plus `references/page-anatomy.md` from that skill. FROZEN: visual contract, TUNE numbers, theme palette unless named. CHANGE: region ids, semantics, real controls, contrast, motion that does not change the picture.
- Layout pack — load `references/layout-packs.md` only when asked.
- Scaffold reminder — `references/project-scaffold.md`.
- Prompt patterns — `references/prompts.md`.

## Surgical map

| Ask | File |
|---|---|
| tighter, bigger type, more air, measure, radius, motion | `core.css` TUNE block |
| night paper, gold, overlay, hairline | `theme-*.css` |
| stacked vs split hero | `data-layout` + layout pack |
| wrong sentence | `index.html` |

## Do not

- Mix Pass A visual cloning with studio-web constitution.
- Put grid columns or `order` in TUNE.
- Put `--space-*` or type scale in a theme file.
- Fork `index-dark.html` / `index-camp.html`.
- Run the full theme × layout visual matrix except hero + primary CTA.
