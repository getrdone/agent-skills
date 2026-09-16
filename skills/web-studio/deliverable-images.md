# Deliverable — images

```text
WEB-STUDIO: 1.0
HTML-DELIVERABLE: images
```

Structure already exists. Fill graphics. Stop before theme.

## Require

- A living page from **clone** (or an existing page the user named).
- `DELIVERABLE.md` with stack + image slot inventory.
- `references/image-slots.md`

## Method

1. Do not re-clone layout. Do not retoken theme. Do not polish unrelated copy.
2. Load `skills/dynamic-symmetry/SKILL.md` (required). For each slot, stamp crop / rectangle / armature / focal **before** generating. Prefer the page’s existing stamp from clone when the slot matches that crop.
3. Inventory empty or placeholder slots from `DELIVERABLE.md` / markup.
4. Load **one** image-direction skill that matches the ask:
   - Web landing / section art / hero graphics → `skills/imagegen-frontend-web/SKILL.md`
   - Mobile app screens → `skills/imagegen-frontend-mobile/SKILL.md`
   - Brand boards / logo systems → `skills/brandkit/SKILL.md`
   - Anti-slop taste check on art direction → `skills/design-taste-frontend/SKILL.md`
5. Generate or place assets into the named slots. Prefer in-session image tools. Every prompt must include Dynamic Symmetry placement in full words (never “DS”).
6. Use `skills/ai-image-generation/SKILL.md` **only** when the user explicitly asks for belt / inference.sh (still with Dynamic Symmetry stamp).
7. Keep slot names stable. Do not invent a second art system beside the page.
8. Stop. Show which slots were filled + each slot’s Dynamic Symmetry stamp. Do not open theme or polish.

## Stop test

- Every required slot has a real file or an explicit labeled deferral.
- Every generated slot has a Dynamic Symmetry stamp (crop, rectangle, armature, focal).
- Layout/DOM regions unchanged aside from `src` / image URLs.
- No theme token edits in this phase.

## Do not

- Open `deliverable-theme.md` or `deliverable-polish.md` in the same turn unless the user chained phases by name
- Crop the source mockup as the final hero policy
- Replace a living video/control region with one baked screenshot
