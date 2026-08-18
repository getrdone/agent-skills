---
name: modern-css-design
description: Container-query-first CSS. Zero viewport breakpoints for components. All responsive logic via @container, cqi units, style queries, auto-fit/fill, wrap detection, relative colors, native primitives, and purposeful motion. Use when writing or refining any CSS, layouts, themes, effects, or design systems.
---

# Modern CSS Design — Container-Query-First

## CORE PRINCIPLE (non-negotiable)

**Never use `@media (min-width: …)` for component layout.**

Components must respond only to their parent container. Moving a card from main → sidebar → modal requires zero CSS edits.

Allowed `@media` only for true viewport concerns:
- `prefers-color-scheme`, `prefers-contrast`
- `print`
- Root-level chrome (never components)

Everything else = `@container` + `cqi` + intrinsic grid/flex.

## Progressive Load Router (token discipline)

Load **only** the reference that matches the current need. Do not load multiple groups unless the task genuinely spans them.

| Need | Load this file |
|------|----------------|
| Layout, grid, responsive behavior, wrap detection, fluid type, auto-fit/fill | `references/01_intrinsic_layout_engine.md` |
| Color systems, theming, dark mode, relative colors, oklch, style queries | `references/02_style_queries_theming.md` |
| Nesting, `:has()`, combinators, CSS state machines, logic that replaces JS | `references/03_css_logic_no_breakpoints.md` |
| Scroll-driven animations, glows, gradient buttons, directional effects | `references/04_effects_motion_intrinsic.md` |
| Native dialog/modals, form validation, intrinsic buttons | `references/05_primitives.md` |
| Reset, foundations, underrated props, fouls to avoid, starter template | `references/06_foundations.md` |

## Quick Start Pattern (always apply)

```css
@layer reset, tokens, base, components;

@layer base {
  :where(main, aside, section, article, .card, .grid, .wrapper) {
    container-type: inline-size;
    container-name: layout;
  }
}

/* Intrinsic grid — works at any container size */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
  gap: clamp(0.75rem, 3cqi, 1.5rem);
}

/* Fluid, container-aware type */
h2 {
  font-size: clamp(1.15rem, 4cqi + 0.25rem, 1.85rem);
  text-wrap: balance;
}
```

## Lint Rules (apply before finishing any CSS)

- [ ] No `@media (min-width` for layout?
- [ ] Parents have `container-type: inline-size`?
- [ ] Using `cqi` / `cqw` instead of `vw` inside components?
- [ ] `minmax(min(XXXpx, 100%), 1fr)` to prevent overflow?
- [ ] Base styles work without any `@container` (narrow-first)?
- [ ] Colors in `oklch` + relative color syntax where variants exist?

## How to use with modern-html-aeo

When building full pages, modern-html-aeo owns the page structure and conversion flow.  
This skill owns every CSS decision. Follow the router above so only the needed reference enters context.
