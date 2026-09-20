# Interaction (consult only)

This is not a lane.

Clone places real controls (button, form fields, share). Theme does not add JS. Polish completes the requested interactions.

Defaults:

- Play control is a button or video element, not a picture of a triangle.
- Forms have labels, names, and a visible submit.
- Keyboard focus visible. `prefers-reduced-motion` respected.
- Add carousel, modal or tab behavior when the request and user experience justify it; reuse suitable components.

## Animating shadows, borders, and filters — the paint-budget gotcha (2026-09-17)

Any transition/animation of `box-shadow` (blur/offset/color), `filter` (brightness, drop-shadow, blur), or `background-color` of a large/gradient surface forces a **repaint every frame**. On wide viewports the compositor keeps up; on narrow ones (or busy pages) the browser drops to ~30fps and the animation looks choppy — while the identical CSS looks perfectly smooth on the agent's own headless-Chrome screenshot. The CSS is not wrong; the paint budget is.

Rule for ALL animation style requests in ALL projects:

- Prefer not to transition costly `box-shadow` effects directly when performance is affected. Put the hover/focus shadow on a `::after`/`::before` layer (`position: absolute; inset: 0; z-index: -1; border-radius: inherit;`) and animate that layer's **opacity only**.
- Same for `filter` effects (glow, brightness): pre-render them on a pseudo-layer and fade the layer.
- Prefer compositor-friendly properties where they achieve the effect: `opacity`, `transform` (translate/rotate/scale). Other properties may trigger layout or paint; profile the actual result.
- `background-color` lifts on small buttons are usually fine, but if smoothness is questioned, prefer a `::before` color layer faded by opacity over transitioning the property itself.

**It is testable — do not judge motion by screenshots.** A screenshot cannot show choppiness. Verify with a frame-diff:

1. Extract frames: `ffmpeg -i clip.mp4 /tmp/f/%04d.png` (any screen recording, 60fps ideal).
2. Run `_agent-tools\scripts\analyze_video_choppiness.js <frame-dir>` — prints per-frame RMS delta.
3. Smooth = runs of consecutive nonzero deltas at the capture rate. Choppy = nonzero deltas interleaved with `0.0` frames and ~2× step size (browser skipping frames).
4. Compare recordings from the two widths the user disputes; the fix is verified when both show continuous runs.

(Real case: a landing CTA hover was smooth on desktop, choppy at tablet — frame-diff proved every-other-frame skipping; moving the hover shadow to an opacity-animated `::after` fixed it at every width. Background: found via 2026-09-17 Final Days session, `01-NOW.md`.)
