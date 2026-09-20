# Image veils, seams, and adaptive masks (consult only)

How to make an image-backed section dissolve into the page instead of ending in a
hard line. Every rule here came from live production bugs (Final Days landing page,
2026-09-16/17 sessions — footer mountains, hero backdrop, question-card art) and is
written for ANY project that lays images under or behind web content.

## The core problem: image rectangles meet page backgrounds

A `background-image` on a section is a rectangle. The page around it is a color or
another gradient. Where the two meet, the eye sees a seam — even when both sides are
"the same" paper color, because the image has texture, gradients, or opacity that the
flat page color does not. The seam shows up:

- where a hero image ends and the body begins,
- where a footer image begins and the body ends,
- at clipped edges of overflow-hidden layers,
- on ONE width only (the bug reports as "breakpoint-specific" when it is really
  geometry-specific: the seam is wherever the rectangle edge happens to land).

## The fix: mask the whole layer, alpha zero at the meeting edge

Mask the image layer itself so its alpha reaches 0 exactly at the edge where it meets
the page. The image dissolves; no seam can exist because the layer contributes nothing
at the boundary.

```css
.section::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: var(--img) center top / cover no-repeat;
  /* dissolve to nothing at the bottom edge */
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, #000 45%, transparent 97%);
  mask-image: linear-gradient(to bottom, #000 0%, #000 45%, transparent 97%);
}
```

**Why this beats a gradient underlay alone:** a gradient over the image
(`linear-gradient(transparent → paper)` stacked on the image) can still leave a hard
last row if the element clips, and it does nothing at the side/bottom edges of the
layer box. The mask kills the layer's own alpha — the seam physically cannot render.

**Why it is adaptive:** the mask percentages are relative to the ELEMENT's rendered
height, not to pixels. Tall mobile hero, short desktop hero — the fade always
completes at the element's bottom edge. This is the same property that makes the
footer veil rule below work.

Dials: first stop = where the fade STARTS (raise it for a later, shorter fade);
last stop = where alpha reaches 0 (keep it ≤ 100% so the fade truly completes).

## Rules (testable, all projects)

1. **Any image layer that meets a page background gets a single-layer mask to zero
   alpha at the meeting edge.** Do not rely on gradient underlays, opacity alone, or
   the image "happening to fade" in its artwork.

2. **Single-layer masks only — never `mask-composite`.** Browsers disagree on the
   default composite operator (Firefox ADD vs webkit SOURCE-IN). A two-gradient mask
   that looks correct in Chrome can render union-shaped in Firefox. If a shape needs
   intersection, NEST two elements (outer masks x, inner masks y) instead of
   compositing. Real case: a two-gradient intersect mask rendered fine in Chrome and
   wrong in Firefox; the single radial mask replaced it and rendered identically
   everywhere.

3. **Bottom-anchored art + full-element mask = broken on short viewports.** If the
   mask spans the element but the image anchors `center bottom`, the image's hard top
   edge can land OUTSIDE the fade zone on small screens. Fix: size the veil layer to
   the image itself — `position: absolute; inset: auto 0 0 0;
   aspect-ratio: <img-w>/<img-h>; background-size: 100% 100%;` — so the fade is
   image-relative at every width. (Real case: footer mountain veil showed a hard top
   edge on large phones.)

4. **When the element's height is responsive, anchor the mask to the element and let
   it scale** (rule 1). When the image has a fixed composition that must survive
   (rule 3), anchor the LAYER to the image. Pick deliberately; do not mix.

5. **Never re-anchor composed art; flip the whole layer.** `background-position`
   changes crop a top-left-composed image and blank the cards. To mirror art between
   corners: keep the anchor, `transform: scaleX(-1)` on the layer.

6. **Mask + rounded corners:** a mask measures to the RECT edges; rounded-corner arcs
   cut inside them. Points just inside an arc keep partial mask then clip to zero at
   the border-radius rim = chroma edge at corners. If the masked layer sits inside a
   rounded container, use an SVG-data-URI mask of a blurred rounded rect, or inset
   the mask's solid zone so it fully clears the arcs.

7. **Verify like the interaction rules demand:** screenshot the seam area at BOTH the
   reported width and one other width before debugging (the seam moves with width);
   after the fix, verify the fade completes — last visible image row should be at
   alpha ~0. `mask-composite` in the file = fail. `//` comments anywhere in the CSS
   = fail (they can kill the whole stylesheet).

## Quick audit recipe

For each image-backed section on a page:

- Does the image layer meet the page background at any edge? → needs a mask (rule 1).
- Grep the stylesheet for `mask-composite` → replace with nested single-layer masks.
- Bottom-anchored image + mask? → check the layer is image-sized (rule 3).
- Rounded corners near the fade? → check arcs vs mask solid zone (rule 6).
- Check at narrow AND wide widths — seams are geometry, not breakpoints.

## Worked examples (Final Days landing, all live-verified 2026-09-17)

- Hero backdrop → body: `.hero::before` masked `#000 0% → #000 45% → transparent 97%`.
  Gradient underlay kept for mid-hero tone; mask guarantees zero contribution at the
  bottom edge. DIALS: 45% = fade start, 97% = alpha zero.
- Footer veil: image-sized layer (rule 3) + mask var; inset:0 + cover so the fade
  begins at the footer's top edge at every responsive height.
- Question-card art: flipped layer (`scaleX(-1)`) instead of re-anchoring (rule 5).
- Player glow edge: SVG blurred-rounded-rect mask following corner arcs (rule 6),
  replacing linear-gradient masks that measured to the rect and left corner chroma.
