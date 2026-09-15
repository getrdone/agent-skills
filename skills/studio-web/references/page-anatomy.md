# Page anatomy — stable sections

Build pages so a later agent or a human can change one region without rewriting the file.

## Required region ids

Use these ids (rename only when the brief names a different spine). Keep them stable across repairs.

| id | Role |
|---|---|
| `site-header` | Brand, nav |
| `hero` | Promise + primary action |
| `primary` | Main teaching or product path |
| `evidence` | Proof, verses, quotes, figures |
| `interact` | Map, trail, calculator, quiz, form |
| `next-path` | Featured continuation + quieter alternates |
| `site-footer` | Citations, legal, secondary links |

Add topic-specific ids (`sheol-map`, `timeline-70`) as needed. Never recycle an id for a different job.

## Markup contract

```html
<section id="hero" data-region="hero" aria-labelledby="hero-title">
  <!-- region content only -->
</section>
```

- One H1 on the page. Region titles are H2.
- Do not wrap the whole page in a JS-gated shell. First paint must include hero heading and primary answer text.
- Keep citations next to the claims they support.

## CSS contract

```css
/* region:hero */
#hero { }
/* end:hero */
```

- Tokens live in TUNE blocks. Repairs do not invent a second token set.
- Component layout uses `@container` + `cqi`. No viewport width breakpoints for components.
- Humans change numbers in TUNE only. Agents must not scatter raw `font-size`, `padding`, `margin`, or `gap` when a token already exists.

## Human TUNE block (required on every page)

One labeled block at the top of the stylesheet. Edit numbers here for type, vertical space, horizontal space, measure, radius, and motion. Downstream rules only consume `var(--…)`.

```css
/* ============================================================
   TUNE — page
   Edit these numbers. Everything else reads these tokens.
   cqi = 1% of the component's own width, not the browser window.
   stack = vertical gap / padding-block
   inset = horizontal padding-inline
   gutter = gap between sibling columns or chips
   ============================================================ */
:root {
  --font-display: "Source Serif 4", Georgia, serif;
  --font-body: "Source Sans 3", system-ui, sans-serif;

  --type-body: clamp(1rem, 2.4cqi, 1.125rem);
  --type-lead: clamp(1.05rem, 2.8cqi, 1.3rem);
  --type-h2: clamp(1.5rem, 4cqi, 2.25rem);
  --type-h3: clamp(1.2rem, 3cqi, 1.6rem);
  --type-kicker: 0.75rem;
  --type-small: 0.875rem;
  --leading-body: 1.6;
  --leading-display: 1.15;
  --measure: 38rem;

  --space-stack-xs: 0.35rem;
  --space-stack-s: 0.75rem;
  --space-stack-m: 1.25rem;
  --space-stack-l: clamp(2rem, 6cqi, 3.5rem);
  --space-stack-xl: clamp(3rem, 10cqi, 6rem);
  --space-section: var(--space-stack-xl);

  --space-inset-s: 1rem;
  --space-inset-m: clamp(1.25rem, 4cqi, 2rem);
  --space-inset-l: clamp(1.5rem, 6cqi, 3rem);
  --space-gutter: clamp(0.75rem, 3cqi, 1.5rem);

  --radius-s: 0.35rem;
  --radius-m: 0.75rem;
  --line: 1px;

  --move-fast: 160ms;
  --move-med: 320ms;
}

/* TUNE — region:hero
   Region tokens override page tokens for this container only. */
#hero {
  container-type: inline-size;
  container-name: hero;
  --hero-title: clamp(2.25rem, 9cqi, 4.75rem);
  --hero-lead: clamp(1.05rem, 3cqi, 1.35rem);
  --hero-stack: var(--space-stack-l);
  --hero-inset: var(--space-inset-l);
}

#hero {
  padding-block: var(--hero-stack);
  padding-inline: var(--hero-inset);
}
#hero h1 { font-size: var(--hero-title); line-height: var(--leading-display); }
#hero .lead { font-size: var(--hero-lead); }
```

Same pattern on `#primary`, `#evidence`, `#interact`, `#next-path`: each is a container; each may set `--<id>-title`, `--<id>-stack`, `--<id>-inset`, `--<id>-gutter`.

### What lives in TUNE

| Knob | Token family | Human ask |
|---|---|---|
| Body / heading / kicker size | `--type-*`, `--hero-title` | "hero title smaller" |
| Line height | `--leading-body`, `--leading-display` | "body feels tight" |
| Column width | `--measure` | "lines too long" |
| Vertical rhythm | `--space-stack-*`, `--space-section`, `--hero-stack` | "more air under the title" |
| Side padding | `--space-inset-*`, `--hero-inset` | "hero is tight to the edges" |
| Gap between items | `--space-gutter` | "cards too close" |
| Corners / rules | `--radius-*`, `--line` | "softer cards" |
| Motion time | `--move-fast`, `--move-med` | "snappier hover" |
| Faces | `--font-display`, `--font-body` | "swap the display face" |

Color stays in the locked palette tokens (`--color-*`), not in TUNE, unless the user asked to retune color.

### Rules

- Every major region is a container (`container-type: inline-size`). Sizes use `cqi` so a narrow column shrinks without a viewport breakpoint.
- Override on the **region**, not on each tag across the file.
- Name tokens after the job (`--hero-stack`), not a pixel guess (`--pad-72`).
- Keep the TUNE comments. Copy repairs leave this block alone unless the user asked to change size or space.
- One place per concern: page tokens in `:root`, region tokens on `#hero`, `#primary`, etc.

## JS contract

```js
const CONFIG = {
  /* timings, selectors, copy hooks — point at stable ids */
};
```

Do not bind behavior to nth-child order of sections.

## Assets

- Hero image — real file or designed CSS/SVG stand-in in the same slot. `fetchpriority="high"`.
- Other images — `loading="lazy"` + `decoding="async"` + width/height or aspect-ratio.
- Filenames under `deliverables/assets/` stay stable (`p01-hero.webp`). Repair does not rename.

## What a later agent may assume

If `id="hero"` exists, it is still the hero. Frozen decisions live in `03-MEMORY.md` or the brief, not in comments scattered through CSS.
