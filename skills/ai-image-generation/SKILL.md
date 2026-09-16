---
name: ai-image-generation
description: >
  Generate or edit images via the inference.sh belt CLI (GPT-Image-2, FLUX, Gemini,
  Grok Imagine, Seedream, Reve, and related apps). Use ONLY when the user explicitly
  requests AI image generation / editing / upscaling through belt or this skill by name.
  Do not auto-fire on casual "image", "thumbnail", or "art" requests — those stay with
  artwork-prompts-handoff or ordinary judgment.
---

# AI Image Generation (belt / inference.sh)

<!-- Provenance
Source: qu-skills / inference-sh ai-image-generation
URL: https://mcpservers.org/agent-skills/qu-skills/ai-image-generation
Canonical SKILL: https://github.com/inference-sh/skills/blob/main/tools/image/ai-image-generation/SKILL.md
Install hint (upstream): npx skills add https://github.com/qu-skills/skills --skill ai-image-generation
Companion CLI skill (upstream): npx skills add belt-sh/cli
Last synced: 2026-09-11
Check cadence: ~quarterly
Re-sync: fetch upstream SKILL.md and diff models table + examples
-->

<!-- Agent: Reminder | Model: Grok | Thinking: not exposed | Date: 2026-09-11 | Folded external skill into SJ agent-skills; explicit-only routing. -->

## Hard gate

Run this skill **only** when Steve (or another agent on his behalf) explicitly asks to:
- generate / edit / upscale an image **with belt / inference.sh**, or
- use **ai-image-generation** / **GPT-Image-2 / FLUX / Grok Imagine / Seedream / Reve** via belt.

Otherwise: do **not** load this skill. Prefer `artwork-prompts-handoff` for paste-ready human packs, or other existing design paths.

Requires: `belt` CLI installed and `belt login` completed on the machine that will run commands. Do not invent API keys. Costs and prompts go to hosted services — confirm before a large batch.

## Quick start

```bash
belt login
belt app list --category image
belt app run falai/flux-dev-lora --input '{"prompt": "a cat astronaut in space"}'
```

## Models (common)

| Model | App ID | Best for |
|-------|--------|----------|
| GPT-Image-2 | `openai/gpt-image-2` | Text-to-image, editing, inpainting |
| FLUX Dev LoRA | `falai/flux-dev-lora` | High quality + LoRA styles |
| FLUX.2 Klein LoRA | `falai/flux-2-klein-lora` | Fast LoRA (4B/9B) |
| P-Image | `pruna/p-image` | Fast / economical |
| P-Image-LoRA | `pruna/p-image-lora` | Fast + preset LoRAs |
| P-Image-Edit | `pruna/p-image-edit` | Fast edits |
| Gemini 3 Pro Image | `google/gemini-3-pro-image-preview` | Google latest |
| Gemini 2.5 Flash Image | `google/gemini-2-5-flash-image` | Fast Google |
| Grok Imagine | `xai/grok-imagine-image` | xAI; aspect ratios |
| Seedream 4.5 | `bytedance/seedream-4-5` | 2K–4K cinematic |
| Seedream 4.0 | `bytedance/seedream-4-0` | High quality 2K–4K |
| Seedream 3.0 | `bytedance/seedream-3-0-t2i` | Text rendering |
| Reve | `falai/reve` | NL editing + text on image |
| ImagineArt 1.5 Pro | `falai/imagine-art-1-5-pro-preview` | Ultra-fidelity 4K |
| FLUX Klein 4B | `pruna/flux-klein-4b` | Ultra-cheap |
| Topaz Upscaler | `falai/topaz-image-upscaler` | Upscale |

## Example commands

```bash
# GPT-Image-2
belt app run openai/gpt-image-2 --input '{"prompt": "professional product photo of sneakers, studio lighting", "quality": "high"}'

# Edit from URL
belt app run openai/gpt-image-2 --input '{"prompt": "change the background to a beach at sunset", "images": ["https://your-image.jpg"]}'

# FLUX
belt app run falai/flux-dev-lora --input '{"prompt": "professional product photo of a coffee mug, studio lighting"}'

# Grok Imagine
belt app run xai/grok-imagine-image --input '{"prompt": "cyberpunk city at night", "aspect_ratio": "16:9"}'

# Reve (text on image)
belt app run falai/reve --input '{"prompt": "A poster that says HELLO WORLD in bold letters"}'

# Seedream 4.5
belt app run bytedance/seedream-4-5 --input '{"prompt": "cinematic portrait, golden hour lighting"}'

# Upscale
belt app run falai/topaz-image-upscaler --input '{"image_url": "https://..."}'

# Stitch
belt app run infsh/stitch-images --input '{"images": ["https://img1.jpg", "https://img2.jpg"], "direction": "horizontal"}'
```

## Dynamic Symmetry (required)

Before any generate/edit that places a subject in frame, load [`skills/dynamic-symmetry/SKILL.md`](../dynamic-symmetry/SKILL.md). Stamp crop / rectangle / armature / focal. Put Dynamic Symmetry placement instructions in the prompt in full words (never “DS”). Upscale-only jobs may skip if no recompose.

## Procedure

1. Confirm the user explicitly wants belt/inference.sh generation (this skill).
2. Confirm `belt` is available; if not, point at [CLI install](https://raw.githubusercontent.com/inference-sh/skills/refs/heads/main/cli-install.md) and stop.
3. Load Dynamic Symmetry; choose crop + armature; write the stamp.
4. Pick the smallest suitable model from the table (or the one they named).
5. Run `belt app run …` with a clear JSON `--input` that includes composition placement. Save outputs under the project’s normal asset path (see `WORKSPACE.md`) — do not dump into skill folders.
6. Show the result path(s) + Dynamic Symmetry stamp; do not schedule follow-up generation unless asked.

## Related upstream packs (optional)

```bash
npx skills add inference-sh/skills@infsh-cli
npx skills add inference-sh/skills@p-image
npx skills add inference-sh/skills@gpt-image
npx skills add inference-sh/skills@flux-image
npx skills add inference-sh/skills@image-upscaling
```

Docs: https://inference.sh/docs/apps/running · https://inference.sh/docs/examples/image-generation
