---
name: clean-video-transcript
description: >
  Clean raw video transcripts into full polished Markdown: remove timestamps and subtitle artifacts,
  fix careful domain spellings, normalize paragraphs, preserve cited sources exactly as spoken,
  require Video URL + Video ID, and add either a presentation-order Quick Reference or section-aware
  Scripture Guides, documentary sources, a master index, and source follow-up. Use for transcript
  cleanup, follow-along transcript downloads, verse/source lists, or /clean-video-transcript.
---

# Clean video transcript

Applies to any video-derived transcript: sermons, lectures, teaching series, panels, documentaries, and similar material.

**Workspace:** follow repo root [`WORKSPACE.md`](../../WORKSPACE.md). Write the canonical name only when the user has selected or requested the final; otherwise use the required agent suffix. Update an existing series or topic board when one exists.

## Load first

1. `references/SPEC.md` — body preservation, source integrity, and end-matter rules (**authoritative**).
2. `references/SPELLING.md` — Bible, EGW, and historicist name forms when applicable.
3. `examples/end-matter-sample.md` — compact and section-aware examples.

If the consumer project has approved clean examples, match their tone and design while still obeying the preservation and source-integrity rules.

## Choose the output pattern

- **Compact transcript:** one short or single-topic presentation → one global Quick Reference after the body.
- **Section-aware follow-along edition:** multiple major topics, a download/lead magnet, or an explicit request for study aids → end each topic with a Scripture Guide and documentary sources, then add a Master Scripture Index and Source Follow-up Needed at the end.
- **HTML companion:** when requested, produce a semantic, no-JavaScript-readable document with theme tokens and accessible navigation in addition to the text document.

## Workflow

1. **Inventory** — find raw transcript sources and identify already-clean files. Never overwrite the raw source unless asked.
2. **Map sections** — identify the opening, major teaching topics, transitions, conclusion, and every named Scripture or external source.
3. **Clean body** — remove timestamps and subtitle artifacts; join line-broken speech; add restrained descriptive headings; do not abridge or rewrite the message.
4. **Preserve sources** — keep every quotation, attribution, date, statistic, title, and source claim exactly as it appears in the transcript. Research is additive only.
5. **Header** — include title, speaker/channel when known, `Video:` URL, and bare `Video ID:`.
6. **Spell-check** — use `SPELLING.md` when biblical/EGW; otherwise correct ASR only when the intended word is clear.
7. **Build reference apparatus** — use the selected compact or section-aware pattern. Added passages must be labeled `Related study passage`.
8. **Verify sources** — assign a verification tier, link the strongest located edition, document discrepancies outside the transcript, and retain unresolved items in `Source Follow-up Needed`.
9. **Verify fidelity and accessibility** — run the SPEC checklist, report word-count/token coverage, and visually inspect rendered document formats.

## Non-negotiable source rule

Never replace, silently correct, delete, or paraphrase a transcript source because another source seems stronger or because the original cannot be found. Add authoritative originals, corroborating material, and context alongside it. If verification remains incomplete, leave a precise follow-up note so a future researcher can add screenshots, books, pamphlets, or archival scans without reconstructing the problem.

## Parallelism

For batch jobs, divide by whole files or self-contained sections. One owner must perform the final source-preservation and cross-section index pass. Never abridge to finish faster.

## Cost control

- Load only this skill's files after a catalog match.
- Prefer an end-matter-only pass when the transcript body is already clean and verified.
- Do not download video media unless the transcript is missing or corrupt.

<!-- Agent: Codex · Model: GPT-5 · Date: 2026-08-21 · Change: section-aware transcript and additive source-verification standard. -->
