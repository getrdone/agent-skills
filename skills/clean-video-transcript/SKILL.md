---
name: clean-video-transcript
description: >
  Clean raw video transcripts (sermons, lectures, teaching series, YouTube captures, and similar)
  into full polished markdown: remove timestamps/fillers, fix domain spellings (Bible/EGW when
  applicable), normalize paragraphs, require Video URL + Video ID in the header, and append a
  presentation-order Quick Reference of Bible verses, Ellen White, and other sources with one-line
  highlights. Use when the user says clean transcript(s), clean video transcript, remove timestamps,
  add verse/EGW reference list, Quick Reference end-matter, or runs /clean-video-transcript.
---

# Clean video transcript

Applies to **any** video-derived transcript (sermons, lectures, panels, documentaries, etc.).

## Load first (this skill only — not the whole agent-skills repo)
1. `references/SPEC.md` — cleaning rules + required Quick Reference end-matter (**authoritative**).
2. `references/SPELLING.md` — Bible / EGW / historicist name forms when content is biblical/SDA.
3. `examples/end-matter-sample.md` — shape of the end tables only.

If the consumer project has its own clean examples, prefer those for tone; still never abridge real output.

## Workflow
1. **Inventory** — find raw `*.txt` with timestamps / download headers; skip files that already meet SPEC “already clean” (unless re-clean or “add Quick Reference only”).
2. **Clean body** — write sibling `*.md` per SPEC; do not edit source `.txt` unless asked.
3. **Header** — title, speaker/series as known, `Video:` URL, **`Video ID:`** bare id.
4. **Spell-check** — SPELLING.md when biblical/EGW; otherwise fix ASR carefully for the domain.
5. **Quick Reference** — append end-matter: Bible, EGW/SOP, Other — **presentation order**. Omit empty categories.
6. **Verify** — SPEC checklist; report paths + word-count ratio.

## Parallelism
Batch multi-file jobs (e.g. ~4 per agent); never abridge to finish faster.

## Cost control
- Load only this skill’s files after CATALOG match — not every skill in the repo.
- Prefer in-place end-matter append when body is already clean.
- Do not download videos unless the transcript is missing or corrupt.
