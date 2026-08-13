# Motion & Premium UI (scroll animation + immersive design)

Use for scroll-driven motion, premium landing-page polish, micro-interactions, and immersive page architecture. Complements `web-experience.md` (semantic/accessibility standard) and `visual-system.md` (visual DNA, color, composition, motion principles).

> **Source provenance — folded from community skills (keep in sync).**
> Distilled from two vetted, high-install skills in the `github/awesome-copilot` repo (37.8K⭐; Gen Agent Trust Hub / Socket / Snyk: pass):
> - `premium-frontend-ui` — creative philosophy (what/why). https://skills.sh/github/awesome-copilot/premium-frontend-ui
> - `gsap-framer-scroll-animation` — technical recipes (how). https://skills.sh/github/awesome-copilot/gsap-framer-scroll-animation
>
> Raw source: `https://github.com/github/awesome-copilot` → `skills/premium-frontend-ui/SKILL.md` and `skills/gsap-framer-scroll-animation/SKILL.md` (plus its `references/gsap.md` and `references/framer.md`).
>
> **Last synced:** 2026-08-13 · **Check cadence:** quarterly, or whenever a build feels dated.
> **How to re-sync:** fetch the raw SKILL.md files above, diff against this file, fold any new recipes/archetypes/rules, then bump the `Last synced` date and note the change in the git commit.

## Library selector

| Need | Use |
|---|---|
| Vanilla JS / Webflow / Vue | **GSAP** |
| Pinning, horizontal scroll, complex timelines | **GSAP** |
| React / Next.js, declarative style | **Framer Motion** (`motion`) |
| `whileInView` entrance animations | **Framer Motion** |

## Setup

### GSAP

```bash
npm install gsap
```

```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger); // MUST call before any ScrollTrigger usage
```

### Framer Motion (Motion v12)

```bash
npm install motion            # new package name since mid-2025
# or: npm install framer-motion — still works, same API
```

```js
import { motion, useScroll, useTransform, useSpring } from 'motion/react';
// legacy: import { motion } from 'framer-motion' — also valid
```

## The 5 most common scroll patterns

**1. Fade-in on enter (GSAP)**

```js
gsap.from('.card', {
  opacity: 0, y: 50, stagger: 0.15, duration: 0.8,
  scrollTrigger: { trigger: '.card', start: 'top 85%' }
});
```

**2. Fade-in on enter (Framer Motion)**

```jsx
<motion.div
  initial={{ opacity: 0, y: 40 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: '-80px' }}
  transition={{ duration: 0.6 }}
/>
```

**3. Scrub / scroll-linked (GSAP)**

```js
gsap.to('.hero-img', {
  scale: 1.3, opacity: 0, ease: 'none',
  scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
});
```

**4. Scroll-linked (Framer Motion)**

```jsx
const { scrollYProgress } = useScroll({ target: ref, offset: ['start end', 'end start'] });
const y = useTransform(scrollYProgress, [0, 1], [0, -100]);
return <motion.div style={{ y }} />;
```

**5. Pinned timeline (GSAP)**

```js
const tl = gsap.timeline({
  scrollTrigger: { trigger: '.section', pin: true, scrub: 1, start: 'top top', end: '+=200%' }
});
tl.from('.title', { opacity: 0, y: 60 }).from('.img', { scale: 0.85 });
```

## Critical rules (apply always)

- **GSAP:** call `gsap.registerPlugin(ScrollTrigger)` before any use.
- **GSAP scrub:** always use `ease: 'none'` — easing feels wrong while scrub is active.
- **GSAP React:** use `useGSAP` from `@gsap/react`, never plain `useEffect` (it auto-cleans ScrollTriggers).
- **GSAP debug:** add `markers: true` in dev; remove before production.
- **Framer:** `useTransform` output must go into the `style` prop of a `motion.*` element, not a plain `div`.
- **Framer Next.js:** add `'use client'` at the top of any file using motion hooks.
- **Both:** animate only `transform` and `opacity` — avoid `width`, `height`, `box-shadow`.
- **Both:** always honor `prefers-reduced-motion`.
- **Premium polish:** animation should enhance, never overwhelm — motion is connective tissue, not decoration.

## Premium creative foundation (commit before layout code)

Pick one strong visual identity before writing CSS — never default to generic, unopinionated code:

- **Editorial Brutalism** — high-contrast monochromatic palette, oversized type, sharp rectangular edges, raw grid structure.
- **Organic Fluidity** — soft gradients, deeply rounded corners, glassmorphism overlays, bouncy spring physics.
- **Cyber / Technical** — dark-mode dominant, glowing neon accents, monospaced type, rapid staggered reveals.
- **Cinematic Pacing** — full-viewport imagery, slow cross-fades, profound negative space, scroll-dependent storytelling.

## Immersive page architecture

- **Entry sequence (preload):** a blank screen is unacceptable — a lightweight preloader resolves fonts/images/3D, then reveals fluidly (split-door, scale-up zoom, staggered text sweep).
- **Hero:** full-bleed `100vh`/`100dvh`; break headlines into span-wrapped words/characters for cascading entrances; add subtle floating elements or background clipping for depth.
- **Fluid contextual navigation:** sticky header that reacts to scroll (hide on scroll-down, reveal on scroll-up); hover states that reveal rich content (mega-menus with image previews).

## High-fidelity micro-interactions

- **Magnetic components:** calculate distance between pointer and button, pull the button toward the cursor.
- **Custom tracking elements:** custom cursor following the mouse with lerp interpolation for smooth drag.
- **Dimensional hover states:** CSS transforms (`scale`, `rotateX`, `translate3d`) for weight and tactile feedback.

## Typography & visual texture

- **Type hierarchy:** extreme scale contrast — headlines via `clamp()` up to ~12vw; body 16–18px minimum.
- **Fonts:** prefer variable fonts or premium typefaces over system defaults.
- **Atmospheric grain:** CSS/SVG noise overlay with `mix-blend-mode: overlay`, opacity `0.02–0.05`.
- **Lighting & glass:** `backdrop-filter: blur()` + ultra-thin semi-transparent borders for frosted depth.

## Performance & accessibility

- Animate only `transform` and `opacity` (composited layers); fiercely avoid `width`, `height`, `top`, `margin`.
- Apply `will-change: transform` sparingly on complex movers, and remove it post-animation.
- Wrap custom-cursor logic and heavy hover animations in `@media (hover: hover) and (pointer: fine)`.
- Wrap heavy continuous animation in `@media (prefers-reduced-motion: no-preference)`; never trade accessibility for flair.

## Implementation ecosystem

- **React / Next.js:** Framer Motion (layout transitions, spring physics) · Lenis (`@studio-freight/lenis`) for smooth scroll · React Three Fiber (`@react-three/fiber`) for 3D.
- **Vanilla / HTML / Astro:** GSAP (timeline sequencing) · Lenis via CDN (scroll smoothing) · SplitType (safe typography chunking).

## Deeper recipes (in source repo, not duplicated here)

The source skill keeps two fuller references — `references/gsap.md` (ScrollTrigger API, 10 recipes, `useGSAP`, Lenis, `matchMedia`, accessibility) and `references/framer.md` (`useScroll`/`useTransform` API, 8 recipes, variants, Motion v12, Next.js). Pull those on re-sync when a pattern beyond the five above is needed.
