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
