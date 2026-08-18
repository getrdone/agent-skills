---
name: interactive-components
description: Use when building or refining interactive UI elements such as accordions, tabs, filters, calculators, forms, modals, carousels, or progressive disclosure. Requires Core Web Vitals compliance (LCP, INP, CLS). Elevates beauty, delight, and purposeful motion as first-class goals alongside performance and accessibility.
---

# Interactive Components

Build interactive elements that are fast, accessible, stable, **beautiful**, and delightful. Core Web Vitals remain non-negotiable. Motion and richer interaction are encouraged when they improve clarity, feedback, or pleasure of use.

## Non-negotiable Rules

1. **Core Web Vitals constraints**
   - **LCP** — Do not delay the largest contentful paint. Never put critical text or hero content behind JS. Avoid layout-affecting scripts in the critical path.
   - **INP** — Interactions must respond in under 200 ms. Keep event handlers light. Debounce expensive work. Prefer CSS transitions and the Web Animations API over continuous JS animation loops.
   - **CLS** — Reserve space for every interactive region before it becomes active. Set explicit dimensions or aspect-ratio. Never insert content that shifts layout after load.

2. **Progressive enhancement (accessibility baseline)**
   - Core content and primary actions should remain usable if JavaScript fails.
   - This is a resilience and accessibility requirement — **not** a design constraint that forces the page to start bland.
   - Design the full delightful experience first. Then ensure the critical path still works without JS.

3. **Accessibility required**
   - Full keyboard support and visible focus states.
   - Correct ARIA only when native semantics are insufficient.
   - Screen-reader announcements for dynamic changes (use `aria-live` sparingly and correctly).

4. **Beauty, delight, and purposeful motion**
   - Purposeful motion and micro-interactions are first-class. Use them to give feedback, guide attention, and create pleasure.
   - Prefer high-quality CSS motion (including scroll-driven animations, transitions, and transforms). Use JavaScript freely when it improves the experience.
   - Do not treat motion as optional decoration that must be minimized by default.

## Preferred Patterns (in order of preference for quality + performance)

1. Native HTML + modern CSS (details/summary, dialog, popover, scroll-driven animations, container queries, :has())
2. Lightweight vanilla JS with strong configuration objects, event delegation, and CSS custom properties for state
3. Small, focused libraries only when complexity truly demands it
4. Framework components only if the host page already depends on that framework

## Forbidden Patterns

- Blocking the main thread with heavy computation on interaction
- Layout shifts from late-loading interactive regions
- Auto-playing media or animations without user intent
- Third-party widgets that inject large scripts or cause CLS
- Custom scroll-jacking or non-standard gesture handling that hurts INP
- Treating progressive enhancement as a reason to ship a plain, lifeless page

## Decision Checklist (run before proposing code)

- Does this interaction improve clarity, feedback, or delight?
- Will this component cause a layout shift when it activates?
- Is the interaction cost under 200 ms on mid-tier mobile?
- Can modern CSS (including motion) solve a large part of the need elegantly?
- Is any additional JS clean and well-structured?

## Output Style

- Design and show the full intended experience (including motion and interaction) first.
- Ensure progressive enhancement and Core Web Vitals compliance are present, but do not lead with a stripped-down version as the primary deliverable.
- Prefer small, high-quality, copy-pasteable snippets.
- Call out any remaining Core Web Vitals risks.

## References

Load only when needed:

- `references/cwv-patterns.md` — concrete LCP / INP / CLS patterns for common interactive components
- `references/native-first.md` — native HTML solutions that often replace heavier JS components
