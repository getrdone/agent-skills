---
name: ai-image-generation
description: >
  Generate or edit images via the inference.sh belt CLI (GPT-Image-2, FLUX, Gemini,
  Grok Imagine, Seedream, Reve, and related apps). Use ONLY when the user explicitly
  requests AI image generation / editing / upscaling through belt or this skill by name.
  Do not auto-fire on casual "image", "thumbnail", or "art" requests — those stay with
  artwork-prompts-handoff or ordinary judgment.
---

# ai-image-generation

Resolve an explicitly requested release, `STABLE` when requested, otherwise `CURRENT`. Read that release's manifest.json and SKILL.md under `versions/<release>/`. All resources belong to that release; do not mix releases. The complete authoritative library is this repository, not legacy or upstream files.

Read [CURRENT](CURRENT) or [STABLE](STABLE) to select the release. Previous releases are available only on explicit selection.
