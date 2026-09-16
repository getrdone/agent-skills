# Deliverable — theme

```text
WEB-STUDIO: 1.1
HTML-DELIVERABLE: theme
```

Look only. Existing tree is frozen.

## Require

- A living page and `DELIVERABLE.md` (infer once and write the stamp if missing).
- `references/tokenize-contract.md`
- Prefer images phase already done (or explicit placeholders the user accepted).

## Method

1. Do not clone. Do not regenerate images. Do not change sentences.
2. For a new or materially revised palette, load `skills/color-palette-composition/SKILL.md` first.
3. Fill TUNE (rhythm) and theme (color) tokens:
   - static-html → `core.css` TUNE + `theme-default.css` (or `theme-<name>.css`)
   - React → `app/globals.css` `:root` TUNE + `:root[data-theme="default"]`
4. Point existing utilities at tokens where they already match. Do not restyle sections.
5. A second look is a new theme file or `data-theme` value. Same DOM.
6. Stop. Show the token file.

## Do not

- Add or remove sections
- Fork `index-dark.html` / `page-dark.tsx`
- Put `--space-*` or `--type-*` in a theme block to fix a look
- Open clone or images in this turn
