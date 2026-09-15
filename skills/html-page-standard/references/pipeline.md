# Pipeline

## Why three passes

screenshot-to-html optimizes `render ≈ picture`.
studio-web optimizes a living page (semantics, contrast, motion, AEO).
Those two success tests fight if they share the first draft.

Tokenize sits between them so repair can change 40 lines instead of 1,000.

## A — clone

Trigger: user attaches a screenshot, full-page capture, or raster mockup.

1. Load screenshot-to-html only.
2. Keep the source image next to the page as `source.png` (or original filename).
3. Write `clone.html`. Single file is fine at this stage.
4. No TUNE comments, no theme sheet, no JSON-LD, no layout pack.
5. Stop and show the file. Do not "improve" spacing.

## B — tokenize

Trigger: clone exists, or user says tokenize / TUNE / theme tokens.

1. Do not change the look.
2. Extract rhythm into `core.css` TUNE blocks.
3. Extract palette into `theme-default.css`.
4. Point `clone.html` or the new `index.html` at both files.
5. Set `data-theme="default"` on `<html>`.
6. Stop.

## C — repair

Trigger: tokens exist, user wants a real page.

1. studio-web `web.repair` only.
2. Snapshot before a destructive rewrite (`clone.html` stays the visual contract).
3. Promote to `index.html` if not already.
4. Stable region ids. One h1. Real buttons and links.
5. Motion and JS are allowed if they do not change the screenshot composition.
6. JSON-LD only when it matches visible content.

## Later

- Second look → new `theme-*.css` only.
- Second arrangement → one layout pack per page type, not per page.
- Moodboard with no facsimile → skip A, studio-web `web.build`, still emit TUNE + theme files.
