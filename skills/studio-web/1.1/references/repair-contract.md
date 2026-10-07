# Repair contract — change one slice, keep the page

Use this file only on `web.repair`. Do not load visual-system, motion, or anti-slop docs.

## Start

1. Name the section id(s). If the user said "the next-path block", resolve to `#next-path`.
2. Read **only** that HTML region, the matching `/* region:… */` CSS, and any JS that selects those ids.
3. Read `03-MEMORY.md` locks (or the brief) for frozen copy and visual DNA. Do not reopen them.
4. Emit:

```text
LANE: web.repair
CHANGE: #next-path
FROZEN: #hero, #primary, tokens
```

## Size and heading tweaks

If the user wants type or space changed ("hero title smaller", "more air under the title", "less side padding"):

- Edit the matching `/* TUNE — page */` or `/* TUNE — region:… */` custom properties (`--type-*`, `--*-stack`, `--*-inset`, `--space-gutter`, `--measure`).
- Do not add a new `font-size`, `padding`, `margin`, or `gap` elsewhere when a token exists.
- Do not switch to `@media (min-width: …)`.
- TUNE tokens for CHANGE are in scope even if other page tokens stay frozen.

## Allowed edits

- Copy inside the named region
- CSS inside the matching region block
- TUNE tokens for that region
- JS handlers whose selectors are inside CHANGE
- Contrast/focus/label fixes scoped to CHANGE
- One new asset slotted into an existing image hook

## Forbidden on repair

- New page outline or new region ids
- Global token / font / palette swap
- Regenerating `index.html` from a remembered older version
- "While I am here" restyles of frozen regions
- Loading retired helper skills

## Method (token-cheap)

1. Locate bounds with ripgrep (`id="hero"`, `/* region:hero */`).
2. Read that line range only.
3. Replace that range in place.
4. If the tool requires a full-file write, still change only the intended range. Do not reflow unrelated markup.

## Snapshot rule

Copy `index.html` → `index_vN.html` **only** when the next edit would replace the document outline (region list changes). Everyday copy/CSS fixes overwrite the canonical file.

## Done

Chat reports: path, ids changed, ids frozen, verify status (clicked / not clicked). No full file dump.
