# Curiosity-Driven Scripture Journey changelog

## Unreleased

- Clarified honest curiosity vs manufactured suspense for titles, thumbnails, and pre-click copy: an honest, concrete gap is required packaging; empty reaction bait, stacked opaque teasers, unsupported insinuation, and trailer language are banned.
- Title and description generation must apply the What not to do list before writing any line (skill gates + YouTube packaging operating sequence).
- Replaced the description example “What he did next… is what you need to see” with a grounded remaining-beat rule.
- Tightened Contrarian/Novelty so “nobody told you” / church-hid-this claims require documentary support.
- Writing-router frameworks (PAS, AIDA, BAB, 4Ps, FAB) now require real problems, voluntary action, and supportable transformations.
- Integrity and YouTube gates distinguish honest curiosity gaps from manufactured suspense.
- Expanded router metadata so titles, descriptions, packaging, thumbnails, Bible-study work, and high-trust faith content reliably invoke the skill.
- Prevented historical `versions/*/SKILL.md` files from being advertised as separate skills.
- Replaced mandatory `TOPIC-BOARD.md` session tracking with `NOW.md`; `SERIES-BOARD.md` is now optional for multi-episode inventories.

### Hardening pass — 2026-09-10 (claude / claude-opus-5)

- Deleted the duplicate live reference tree at the skill root. It shadowed `versions/3.2.0/references/`,
  and its `learning-and-writing.md` was 14 lines behind — still teaching pre-v3 ideation with no
  knowledge of Quick / Standard / Full Matrix / Deep. Two obedient agents could load
  "references/learning-and-writing.md" and get different instructions.
- Deleted the stale root `manifest.yaml`, which claimed `release: 3.1.0` while `CURRENT` said 3.2.0.
- Stated the one path-resolution rule in the router: every relative path inside a version's files
  resolves under `versions/<resolved-version>/`.
- Added `versions/3.2.0/load-map.yaml` — the machine form of the route table, with per-lane file
  budgets and conditional loads. Every reference is reachable from at least one lane.
- Route table: added the missing `develop` row (`v3-workflow.md` appeared in no row) and the
  `release` row (`v3-quality.md`, `scripts/audit_html.py`); split the single HTML row into
  `web.repair` and `web.build`, which stops a footer fix from pulling the whole design tree.
- `resources-and-authority.md` was named in the shared spine but in no route-table row; it is now
  in the `study` lane.
- Runs must declare `LANES:` / `LOAD:` / `BRIEF:` before opening any file.
- Honest curiosity: rule 8 now bans *manufactured* fear rather than fear itself, with a
  four-question accept/reject test and twelve worked examples deciding the line. Real stakes in the
  subject matter pass; dread invented by the packaging fails.
- `project-brief.md` gains machine state on its existing `status` field (`stem`, `last_lanes`,
  `open_gates`, `last_agent`, `last_updated`) plus a required resume rule. No second state file.
- File naming, file I/O, and continuity now live only in repo `WORKSPACE.md`; nine restatements
  across eight files became pointers.
- Removed the source-governance pointer to a `query_sources` helper script that exists nowhere in
  this repository; the query helper belongs to the source-library repo.

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
<!-- Agent: grok · Model: Grok 4.6 · Date: 2026-09-09 · Honest curiosity vs manufactured suspense for titles/pre-click copy. -->
