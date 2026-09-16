# Deliverable — theme

```text
WEB-STUDIO: 1.0
HTML-DELIVERABLE: theme
```

Look only. Existing tree is frozen.

## Require

- A living page and `DELIVERABLE.md` (infer once and write the stamp if missing).
- `references/tokenize-contract.md`

## Method

1. Do not clone. Do not regenerate images. Do not change sentences.
2. Fill TUNE (rhythm) and theme (color) tokens:
   - static-html → `core.css` TUNE + `theme-default.css` (or `theme-<name>.css`)
   - React → `app/globals.css` `:root` TUNE + `:root[data-theme="default"]`
3. Point existing utilities at tokens where they already match. Do not restyle sections.
4. A second look is a new theme file or `data-theme` value. Same DOM.
5. Stop. Show the token file.

## Do not

- Add or remove sections
- Fork `index-dark.html` / `page-dark.tsx`
- Put `--space-*` or `--type-*` in a theme block to fix a look
- Open clone.md
