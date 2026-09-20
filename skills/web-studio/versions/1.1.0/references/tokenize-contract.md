# Tokenize contract (theme)

Keep a visible TUNE / theme banner in the token file.

## TUNE — rhythm (`:root`)

- Faces — `--font-display`, `--font-body`
- Type — `--type-body`, `--type-lead`, `--type-h2`, `--type-h3`, `--type-kicker`, `--type-small`
- Leading — `--leading-body`, `--leading-display`
- Measure — `--measure`
- Stack — `--space-stack-xs` through `--space-stack-xl`, `--space-section`
- Inset — `--space-inset-s`, `--space-inset-m`, `--space-inset-l`
- Gutter — `--space-gutter`
- Radius / rule — `--radius-s`, `--radius-m`, `--line`
- Motion — `--move-fast`, `--move-med`

Numbers come from the source rhythm. Do not put these in a theme block.

## Theme — look only

- `--color-surface`, `--color-surface-2`
- `--color-ink`, `--color-ink-muted`
- `--color-accent`, `--color-accent-ink`
- `--color-line`, `--color-overlay`

Bind with `:root[data-theme="default"]` or a `theme-*.css` file.

Do not flatten stacks. Do not replace images.

## Field lessons (2026-09-16 — Final Days landing, live-preview verified)

Real bugs from production passes. Check all three when tokenizing or theming any page.

1. **`cqi` scales against the element's own container, not the page.** Identical clamps in
   narrow cards compute smaller than in wide containers — a page's primary heading can become
   the smallest h2 silently. Before shipping heading sizes: compare **computed px at desktop
   width** across every heading band, not the clamp declarations. Narrow-container headings
   need a raised floor and/or a shared cap.

2. **`:root` used as a theme fallback bleeds into other themes.** `:root, [data-theme="a"] { }`
   makes theme A's tokens the default everywhere — every other theme inherits A's values for
   anything they don't redeclare. Use `:root:not([data-theme])` for the no-theme fallback.
   Verify by switching every theme live and checking each theme's computed tokens.

3. **A full-element mask over a bottom-anchored image breaks on short viewports.** The mask's
   fade zone spans the element; the image anchors bottom — on small screens the image's hard
   top edge lands outside the fade. Fix: size the veil layer to the image itself
   (`inset: auto 0 0 0` + `aspect-ratio: <img-w>/<img-h>`, `background-size: 100% 100%`) so
   the fade is image-relative at every width. To mirror composed art between corners, flip the
   whole layer (`transform: scaleX(-1)`) — re-anchoring a top-left-composed image to
   `right top` crops the subject out of view.

<!-- Agent: freebuff · Model: Buffy · Thinking: not exposed · Date: 2026-09-16 · Added field lessons from Final Days v10.9.3 passes. -->

4. **Flat/blocked motion is usually an interpolation problem, not a duration problem.** A
   hover that moves three properties (transform + filter + shadow) on the same basic ease
   reads as mechanical steps, especially `filter: brightness()` — sRGB filter interpolation
   is visibly steppy on subtle shifts. Better tools, combined:
   - Prefer **color transitions over filter transitions** — `color-mix(in oklch, var(--token) 86%, white)`
     on `background-color` interpolates perceptually uniformly (smooth by construction).
   - Keep durations short for controls (0.15s feels instant, 0.25s+ feels deliberate) —
     let the **easing curve carry the character**, not a long duration.
   - The best micro-interactions combine methods: a token-derived color lift + a transform
     lift + a shadow expansion, all on a shared custom bezier, so the whole element moves
     as one gesture rather than three separate snaps.
   - Always verify under `prefers-reduced-motion` — every transition here collapses via the
     global kill switch.

## Verification practice (learned the same passes — treat as strong default, not law)

- **Static review misses what live preview catches.** Every CSS bug above passed a code-diff
  read and died within minutes in a real browser. When the work touches theming, motion, or
  responsive masks, actually switch the themes / widths before calling it done — computed
  styles, not assumptions.
- **Surface a local server for the human to review.** Don't ask Steve to trust a description —
  register the preview (e.g. static serve on a free port, away from the project's usual 8797)
  so he can click it himself. A watch/auto-reload server is the ideal (accepting file-change
  hooks where the harness supports them); a plain static server that gets restarted on demand
  is acceptable. Not 100% mandatory — but the default expectation for visual work.
- **No screenshot verification (HARD RULE, Steve 2026-09-18).** Do not capture screenshots
  (cdp_shot.js or any browser capture) to verify changes — it burns session time. Workflow:
  surgical edit → static audit (`audit_page.js`) → grep the served file to confirm the edit
  landed → hand the human a short checklist of exactly what to eyeball. Exception: one
  capture only when a visual bug report is genuinely unexplainable from code, or when Steve
  explicitly asks.
- **Never use `//` comments in CSS.** They are not valid CSS; a parser that hits one can
  discard the rest of the block or the entire stylesheet depending on what follows. Use
  `/* ... */` only — and never put semicolons inside a comment that sits between declarations.

<!-- Agent: freebuff · Model: Buffy · Thinking: not exposed · Date: 2026-09-16 · Motion lesson + verification practice added from Final Days v10.9.3 hover tuning. -->

## Discoverability requirements (every public page, before deploy)
Added 2026-09-16 from the Final Days canonical-tag catch (theme/boost query variants
and a share route were all indexable as duplicates). Rule: **a page without a canonical
tag is a bug**, not a nicety.

1. Canonical tag pointing at the clean production URL — required the moment a page can
   be reached by more than one URL (query params, share routes, trailing variants).
2. JSON-LD structured data describing what the page IS (VideoObject / FAQPage / Article).
   Renders nothing on-page, so it never conflicts with approved visual design.
3. robots.txt that explicitly ALLOWS AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot,
   PerplexityBot, Google-Extended) unless the client says otherwise.
4. llms.txt at the site root summarizing the site for agentic search.
5. Deep prose on real crawlable pages, not behind forms or client-side JS; keep the form
   as the human funnel, not the content gate.

<!-- Agent: freebuff · Model: Buffy · Date: 2026-09-16 · Discoverability section added per Steve directive (canonical best-practice). -->

## Blending lesson: cool-over-warm goes olive (2026-09-17, Final Days)
color-mix(in oklch, <cool accent> N%, var(--paper-2)) with a warm paper lands between
hues and reads olive/green. For hover/active surface washes, derive from the accent hue
directly with relative color syntax: oklch(from var(--cta) 0.96 0.035 h) — theme hue
preserved, high lightness, low chroma, no paper in the blend. Tune L/C per theme family;
verify the wash in at least one warm-paper and one cool-paper theme.
