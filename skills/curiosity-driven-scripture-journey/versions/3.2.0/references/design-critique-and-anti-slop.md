# Design Critique & Anti-Slop (surface mode, detectors, iteration verbs)

Use to raise the floor on AI-generated frontend: pick the right design mode per surface, catch the common "AI slop" tells before shipping, and run focused iteration passes instead of vague "make it better."

Complements `visual-system.md` (visual DNA, color, composition) and `web-experience.md` (semantic/accessibility standard).

> **Source provenance — folded from a community skill (keep in sync).**
> `pbakaus/impeccable` — https://github.com/pbakaus/impeccable · https://impeccable.style
> License: Apache 2.0 (built on Anthropic's `frontend-design` skill).
> **Last synced:** 2026-08-13 · **Check cadence:** quarterly, or whenever AI-slop creeps back into output.
> **How to re-sync:** diff against the source repo's skill + detector docs. The full 23-command skill and the 59-rule detector CLI can also be installed as a *companion* via `npx impeccable install` (adds a design hook + `npx impeccable detect` for deterministic anti-pattern scanning); this file keeps the knowledge so agents don't need the install.

## Surface mode (choose before designing)

Every surface has a **mode** — what the visitor came to do. Design judgment changes by mode, and one project can hold all four. Judge each surface by its own mode, not by what the company sells.

- **Persuade** — landing, marketing, portfolio → emotional, bold, memorable.
- **Operate** — app UI, dashboard, tool → clear, efficient, calm.
- **Read** — article, study, long-form → typographic, quiet, scannable.
- **Experience** — showcase, gallery → immersive, cinematic, atmospheric.

## Anti-slop detectors (check before shipping)

The tells that make AI interfaces look generic. Avoid these unless a real brand/accessibility reason overrides — then push back *with the reason*.

- Overused fonts: Arial, Inter, system defaults, or “local fonts only” → load distinct **webfonts**.
- Cream paper + sage + Fraunces/Inter as a mindless Scripture template → derive palette/type from this piece’s DNA.
- Purple-to-blue gradients, dark glows, glassmorphism on everything.
- Gray text on colored backgrounds → check contrast; tint, don't gray.
- Pure black / pure gray → always tint toward a hue.
- Cards nested in cards; a rounded-square icon tile above every heading.
- Static page with dead JS hooks or no motion “for accessibility” → full motion default; verify interactions work.
- Bounce/elastic easing → feels dated; use purposeful easing.
- Side-tab borders, cramped padding, small touch targets, skipped heading levels, over-long lines.

These are floors, not laws. Ignoring one without a reason produces worse output than the rule itself.

## Iteration verbs (the "loop until perfect" vocabulary)

A shared set of focused passes, so refinement is a named action instead of "make it nicer." Map each verb to a single pass in `quality-gates.md`.

- **Evaluate:** `critique` (hierarchy, clarity, emotional resonance) · `audit` (accessibility, performance, responsive).
- **Refine:** `bolder` · `quieter` · `distill` · `typeset` · `layout` · `colorize` · `animate` · `delight` · `overdrive`.
- **Simplify:** `clarify` (UX copy) · `adapt` (devices) · `optimize` (performance).
- **Harden:** `harden` (edge cases, overflow, errors) · `onboard` (empty/first-run states) · `polish` (final pass before shipping).

Run one verb per pass; don't blur several disciplines into one vague revision.
