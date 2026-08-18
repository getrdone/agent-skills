---
name: modern-html-aeo
description: Use when building or refining self-contained HTML5 pages that must be clean, small, visually strong, conversion-oriented, a pleasure to use, and optimized for AEO GEO SEO and Core Web Vitals from the first outline. Elevates beauty, delight, and purposeful motion as first-class goals.
---

# Modern HTML5 + AEO/GEO/SEO + Conversion Design

Build self-contained HTML5 pages where structure, visual design, usability, conversion flow, performance, security, beauty, and answer-engine optimization are designed together from the start. Nothing is bolted on later.

## Non-negotiable order of work

1. Clarify primary goal, audience, key entities, and conversion action.
2. Design information architecture + visual hierarchy + conversion path together.
3. Plan Core Web Vitals, security posture, interaction model, and delight.
4. Only then write the HTML, CSS, and JavaScript.

## Core principles (apply to every decision)

**Security**  
Code must be robust and difficult to break, hack, or disrupt. Prefer simple, well-understood patterns. Avoid unnecessary complexity or exposure. Do not add significant code bloat in the name of security.

**Speed**  
Everything must act, react, and *look* fast to the user. Optimize for perceived performance. Break long work into stages or chunks when needed. Protect LCP, INP, and CLS as first-class constraints.

**Usability + Delight**  
- The finished page or element must be easy, pleasant, and delightful for the end user.  
- Interactions should feel responsive, intentional, and satisfying.  
- The code itself must remain easy for a lightly technical person to find, understand, and modify.

These principles sit above stylistic preferences.

## Design principles (from the first outline)

### Visual hierarchy & Gestalt
- Clear focal point and visual order via size, weight, contrast, and position.
- Deliberate use of proximity, similarity, continuity, figure-ground, and common region.
- Tight grouping of related items; consistent whitespace between groups.
- Stable vertical rhythm and spacing scale.

### Conversion & end-user usability
- One primary action per view — make it visually dominant.
- Reduce friction: clear labels, immediate feedback, minimal required input, forgiving interactions.
- Design for scanning while guiding the eye to the next step.
- Progressive disclosure for secondary content.
- Every interaction must feel responsive and intentional.

### Beauty, delight, and purposeful motion
- Purposeful micro-interactions and motion are first-class design tools.
- Use motion to give feedback, guide attention, reveal hierarchy, and create pleasure.
- Prefer high-quality CSS motion (scroll-driven animations, transitions, transforms). Use JavaScript freely when it improves the experience.
- Visual tone must match content and audience. No lifeless or purely utilitarian defaults.

## Technical requirements

### HTML
- Valid, semantic HTML5.
- Logical heading hierarchy (one H1, no skipped levels).
- Structure that serves accessibility, answer engines, and clarity.
- Prefer a single self-contained file unless the project already uses a clear multi-file structure.

### CSS
- Modern CSS only (Grid, Flexbox, container queries, cascade layers, `:has()`, nesting, relative colors, scroll-driven animations).
- **Container-query-first is mandatory.** Never use `@media (min-width: …)` for component layout. Components respond only to their parent container (`@container` + `cqi`). This is the rule that prevents future editing when layouts change.
- Apply the `modern-css-design` skill for every CSS decision. Use its progressive load router: load only the single reference group needed for the current work (layout, color, effects, etc.). Never load the full CSS corpus.
- Combine container queries with fluid techniques (`clamp()`, `cqi`, logical properties, `auto-fit`/`minmax`).
- No design frameworks unless explicitly requested.
- Small, purposeful rules. Remove unused styles.
- Layout stability is mandatory (protect CLS).

### JavaScript
- Prefer vanilla JS. Use a library only when it is clearly the better tool for the job.
- **Object-oriented + DRY**. Organize related behavior into clear objects or modules. Do not repeat logic.
- **Configuration first**. All easy-to-change values (selectors, timings, text, thresholds, options) must live in a single, well-commented configuration object or section at the top of the script so a lightly technical user can find and edit them quickly.
- Keep main-thread work light. Defer or chunk non-critical work.
- Interactions must feel fast and give immediate feedback (support good INP).

### AEO / GEO / SEO + Core Web Vitals
- Clear primary entity and supporting entities in natural language.
- Answer-engine-ready phrasing.
- Correct JSON-LD that matches visible content.
- Strong title, meta description, Open Graph, and Twitter cards.
- Core Web Vitals as design constraints from the start:
  - LCP — critical rendering path and hero resources
  - INP — light, responsive event handling
  - CLS — reserved space, stable layout, no unexpected shifts
- Local/GEO signals only when relevant and consistent.
- Content must remain highly scannable and extractable even when advanced interaction or motion is present.

## Code quality rules
- Smallest effective code that still satisfies Security, Speed, Usability, and Delight.
- No dead code, leftover comments, or unused CSS/JS.
- Readable naming and consistent formatting.
- Configuration must be obvious and centralized.
- Self-contained preferred.

## Output rules
- Deliver pages that already embody the planned hierarchy, conversion path, visual system, performance strategy, security posture, and delight.
- When iterating, protect these decisions unless the new request explicitly requires changing them.
- Prefer precise edits over full rewrites.
- Do not default to a bland or motion-free baseline. Design the full experience.
