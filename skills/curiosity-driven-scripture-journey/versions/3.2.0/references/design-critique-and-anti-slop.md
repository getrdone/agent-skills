# Design Critique & Anti-Slop (surface mode, detectors, iteration verbs)

Use to raise the floor on AI-generated frontend: pick the right design mode per surface, catch the common "AI slop" tells before shipping, and run focused iteration passes instead of vague "make it better."

Complements `visual-system.md` (visual DNA, color, composition) and `web-experience.md` (semantic/accessibility standard).

> **Source provenance — folded knowledge (keep in sync).**
> 1. `pbakaus/impeccable` — https://github.com/pbakaus/impeccable · https://impeccable.style — surface mode, detectors, iteration verbs. License: Apache 2.0 (built on Anthropic `frontend-design`).
> 2. `anthropics/skills` → `frontend-design` — https://github.com/anthropics/skills/tree/main/skills/frontend-design — **AI-design cluster list** (cream/terracotta, acid-green dark, broadsheet, SaaS-card kit, template chrome). License: see that repo `LICENSE.txt`.
> 3. Emerging community fingerprint (spot-check only, not a full fold): `ravidsrk/slop-detect` `definitions@2026.09` — https://github.com/ravidsrk/slop-detect — Inter/Geist/Space Grotesk, VibeCode purple CTAs, gradient-clip headlines, aurora blobs, bento walls, sparkles/"AI magic".
> **Last synced:** 2026-09-10 · **Check cadence:** every ~90 days, or whenever shipped UI starts looking samey again.
> **How to re-sync:** (1) diff impeccable skill + detector docs; (2) re-fetch Anthropic `frontend-design/SKILL.md` and merge any new numbered clusters into **AI-design clusters** below; (3) skim `slop-detect` / current essays for *new* named fingerprints not already listed — add only durable tells, not one-off memes. Optional companion: `npx impeccable install` for CLI detect; this file stays the agent-facing source so install is not required.
> **Next check due:** ~2026-12-10.

## Surface mode (choose before designing)

Every surface has a **mode** — what the visitor came to do. Design judgment changes by mode, and one project can hold all four. Judge each surface by its own mode, not by what the company sells.

- **Persuade** — landing, marketing, portfolio → emotional, bold, memorable.
- **Operate** — app UI, dashboard, tool → clear, efficient, calm.
- **Read** — article, study, long-form → typographic, quiet, scannable.
- **Experience** — showcase, gallery → immersive, cinematic, atmospheric.

## AI-design clusters (Anthropic calibration — avoid as unchosen defaults)

These are legitimate for *some* briefs. They are defaults rather than choices when they appear regardless of subject. Project locks and brand DNA always win when they intentionally use one of these looks.

1. **Cream + terracotta studio** — warm cream ground (near `#F4F1EA`), high-contrast serif display, terracotta/warm-clay accent (near `#D97757`, Claude’s interaction accent — reads as a tell on client work).
2. **Acid dark** — near-black ground with a single bright acid-green or vermilion accent.
3. **Broadsheet pastiche** — hairline rules, zero border-radius, dense newspaper columns as a costume rather than a content-driven layout.
4. **SaaS-card kit** — content chopped into identical rounded cards; one border-radius on everything; the same soft grey shadow (`rgba(0,0,0,.1)`) under each; gradient washes as decoration.
5. **Template chrome** — tracked-out ALL-CAPS eyebrow above every heading; meta joined with middle dots (`A · B · C`); `WORD — fragment` labels with a spaced em dash; tinted near-black (`#0B0B0B`, `#111`) standing in for black; monospace for small data labels; `→` appended to link/button text.

Also treat as generated-page tells (same source): single-word italic/color accent in a headline; ALL-CAPS labels for their own sake; decorative typographic labels above content; numbered `01 / 02 / 03` markers when the content is not actually a sequence; scattershot fade-and-slide-up on every section / hover on every card (prefer one orchestrated moment, plus motion that answers user action).

## Emerging 2026 fingerprints (add only when still common)

Supplement the clusters above; re-validate on each sync — drop stale tells, add only ones that keep showing up unprompted:

- **Slop font stack** — Inter / Geist / Space Grotesk (or Instrument Serif italic accent) as the non-choice default.
- **VibeCode purple** — filled indigo/violet CTAs and purple→blue/cyan hero washes.
- **Gradient-clip H1** — `background-clip: text` rainbow/gradient headlines.
- **Aurora / glow field** — blurred radial/conic “blobs” behind heroes with no subject meaning.
- **Bento wall** — Apple-keynote mixed-span rounded card grid used as filler layout.
- **Gradient letter avatars** — testimonial initials on gradient discs.
- **Sparkles / “AI magic”** — ✨ or Sparkles icon chrome on features that are not generative.
- **Uniform mega-radius** — same exaggerated `rounded-2xl` (or larger) on cards, buttons, inputs, and images so hierarchy disappears.
- **Pulsing Live/New pills** — status chrome on things that are neither live nor new.
- **Centered-everything hero** — hero, subhead, body, and feature blurbs all center-locked with a three identical feature cards row.

## Anti-slop detectors (check before shipping)

The tells that make AI interfaces look generic. Avoid these unless a real brand/accessibility reason overrides — then push back *with the reason*.

- Overused fonts: Arial, Inter, system defaults, or “local fonts only” → load distinct **webfonts**.
- Cream paper + sage + Fraunces/Inter as a mindless Scripture template → derive palette/type from this piece’s DNA.
- Purple-to-blue gradients, dark glows, glassmorphism on everything.
- Gray text on colored backgrounds → check contrast; tint, don't gray.
- Pure black / pure gray → always tint toward a hue.
- Cards nested in cards; a rounded-square icon tile above every heading.
- Static page with dead JS hooks or no motion “for accessibility” → full motion default; verify interactions work.
- Bounce/elastic easing → feels dated; use purposeful easing.
- Side-tab borders, cramped padding, small touch targets, skipped heading levels, over-long lines.

Run the **AI-design clusters** and **Emerging 2026 fingerprints** lists against the page before calling a visual pass done. These are floors, not laws. Ignoring one without a reason produces worse output than the rule itself.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-10 · Folded Anthropic frontend-design clusters + 2026 fingerprint tells; set 90-day re-sync. -->

## Iteration verbs (the "loop until perfect" vocabulary)

A shared set of focused passes, so refinement is a named action instead of "make it nicer." Map each verb to a single pass in `quality-gates.md`.

- **Evaluate:** `critique` (hierarchy, clarity, emotional resonance) · `audit` (accessibility, performance, responsive).
- **Refine:** `bolder` · `quieter` · `distill` · `typeset` · `layout` · `colorize` · `animate` · `delight` · `overdrive`.
- **Simplify:** `clarify` (UX copy) · `adapt` (devices) · `optimize` (performance).
- **Harden:** `harden` (edge cases, overflow, errors) · `onboard` (empty/first-run states) · `polish` (final pass before shipping).

Run one verb per pass; don't blur several disciplines into one vague revision.
