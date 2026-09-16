# Tokenize contract (Pass B)

Fill `assets/core.template.css` and `assets/theme-default.template.css`. Keep comment banners.

## TUNE — page (`:root` in `core.css`)

Required tokens (studio-web names):

- Faces: `--font-display`, `--font-body`
- Type: `--type-body`, `--type-lead`, `--type-h2`, `--type-h3`, `--type-kicker`, `--type-small`
- Leading: `--leading-body`, `--leading-display`
- Measure: `--measure`
- Stack: `--space-stack-xs`, `--space-stack-s`, `--space-stack-m`, `--space-stack-l`, `--space-stack-xl`, `--space-section`
- Inset: `--space-inset-s`, `--space-inset-m`, `--space-inset-l`
- Gutter: `--space-gutter`
- Radius / rule: `--radius-s`, `--radius-m`, `--line`
- Motion: `--move-fast`, `--move-med`

Numbers come from the screenshot rhythm, not from a generic pretty scale.

## TUNE — region

Every major region:

```css
#hero {
  container-type: inline-size;
  container-name: hero;
  --hero-title: ...;
  --hero-lead: ...;
  --hero-stack: var(--space-stack-l);
  --hero-inset: var(--space-inset-l);
}
```

Same pattern on `#site-header`, `#primary`, `#evidence`, `#interact`, `#next-path`, `#site-footer` (or the ids the page actually has). Token names are `--<id>-title`, `--<id>-stack`, `--<id>-inset`, `--<id>-gutter`.

TUNE does not set `grid-template-columns` or `order`.

## Theme file

Only look tokens:

- `--color-surface`, `--color-surface-2`
- `--color-ink`, `--color-ink-muted`
- `--color-accent`, `--color-accent-ink`
- `--color-line`, `--color-overlay`
- optional `--font-display` / `--font-body` override when the *look* needs a different pairing

Do not redefine `--space-*` or `--type-*` in a theme to "fix" a look.

Bind theme with:

```css
:root[data-theme="default"] { }
```

## After tokenize

Component rules consume `var(--…)` only. If a leftover raw length is required for a one-off, put it in `@layer page` with a comment, not in TUNE.
