# Curiosity-Driven Scripture Journey changelog

## Unreleased

- Expanded router metadata so titles, descriptions, packaging, thumbnails, Bible-study work, and high-trust faith content reliably invoke the skill.
- Prevented historical `versions/*/SKILL.md` files from being advertised as separate skills.
- Replaced mandatory `TOPIC-BOARD.md` session tracking with `NOW.md`; `SERIES-BOARD.md` is now optional for multi-episode inventories.

## 3.2.0 — 2026-09-09

- Added evidence-calibrated color psychology requirements for all color selection, recommendation, generation, comparison, and review.
- Requires color decisions to account for intended response, audience and cultural context, Scripture context, plausible alternate readings, evidence strength, semantic role, and non-color cues.
- Strengthened Scripture-specific safeguards: color symbolism must be verified from the passage and may not be used as doctrinal proof or fear pressure.
- Made readable text a hard quality gate: target 7:1 contrast for sustained reading where practical; WCAG 2.2 AA remains the floor; test final-size text at worst-case points over gradients, transparency, imagery, video, and interactive states.
- Requires an accessible, readable equivalent whenever a nonessential artistic low-legibility exception is approved.
- Added release metadata for compatibility, color-psychology routing, contrast targets, and affected areas: visual direction, palettes, thumbnails, artwork, web theming, and accessibility.

## 3.1.0 — 2026-09-08

- Consolidated the useful container-query and interactive-component rules into the routed web experience.
- Retired the competing `modern-css-design`, `interactive-components`, and `optimized-deliverables` skills.
- Replaced the locally maintained Cloudflare skill with the official external `cloudflare/skills` source.
- Moved UBP translator tooling to `getrdone/ubp-tools`.
- Narrowed artwork prompt handoff routing and corrected transcript draft naming.

## 3.0.1 — 2026-09-07
- Requires layered abuse protection on public write endpoints.
- Defaults to low-friction/invisible controls and escalates to Turnstile-like challenges only when justified.
- Requires same-origin write endpoints to avoid wildcard CORS.
- Separates phone capture from SMS send-readiness; ambiguous international numbers are preserved for review rather than rejected or guessed.
- Prohibits automatic SMS to numbers not classified as send-ready.

## 3.0.0 — 2026-09-07
- Separates Journey Development from Experience Production.
- Adds Quick (~24–32), Standard (~36–48 default), Full Matrix (68), and Deep (~80–120) ideation modes.
- Keeps weak-fit ideation territory intentionally available and adds post-selection synthesis.
- Routes learning tools from learner jobs instead of fixed pattern quotas.
- Adds an experience-concept gate and generic-article fail condition.
- Adds iterative independent design/learning/accessibility/engineering review.
- Separates WCAG conformance from Experience Class A/AA/AAA craft.
- Adds deterministic HTML audit tooling.
- Treats existing Hell and Psalm outputs as regression examples, not positive benchmarks.
- Adds Markdown-restraint guidance.
- Explicitly defers SQLite project-state storage.

## 2.0.0 — legacy snapshot
Snapshot of the previously unversioned skill tree for rollback and reproducibility.

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->
