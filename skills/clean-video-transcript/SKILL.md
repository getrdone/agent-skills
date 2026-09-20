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

# clean-video-transcript

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Read [CURRENT](CURRENT) or [STABLE](STABLE) to select the release. Previous releases are available only on explicit selection.
