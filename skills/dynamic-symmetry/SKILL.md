---
name: dynamic-symmetry
description: >-
  Soft-standard composition for any image generation and visual layout.
  Choose a lawful rectangle (root / phi / 1.5), apply an armature (diagonals,
  reciprocals, eyes), place focal points with crop integrity. Use for heroes,
  thumbnails, section art, brand boards, and page region placement. Never
  abbreviate as "DS" in user-facing text — always write Dynamic Symmetry.
metadata:
  type: workflow
  version: "1.0"
  canonical: getrdone/agent-skills
---

# Dynamic Symmetry

**Soft standard** for placement work: image generation, crops, thumbnails, heroes, and layout regions. Skip only if the user forbids grids or the task is pure copy with no visual placement.

Always write **Dynamic Symmetry** in full (never “DS” in prompts or user-facing notes).

## Load order

1. Skim [`references/glossary.md`](references/glossary.md)
2. Open [`references/method.md`](references/method.md) when building or reviewing a frame
3. Prefer black-line PNG overlays from the grid pack when available (see Pack below)

## Required stamp (every image or layout placement)

Declare before generating or locking regions:

```text
DYNAMIC-SYMMETRY: 1.0
CROP: <delivery ratio, e.g. 16:9 | 9:16 | 1:1 | page>
RECTANGLE: <root 3 | phi | 1.5 | root-phi | …>
ARMATURE: <basic | MAD | theme-of-N | …>
GRID: <pack filename or "constructed basic armature">
FOCAL: <what sits on which line/eye>
```

## 15-second workflow

1. Lock the **delivery crop** (platform or page slot).
2. Match nearest **root / phi / 1.5** rectangle (e.g. 16:9 ≈ root 3).
3. Load matching **BLACK PNG** or construct the **basic armature**.
4. Place the **hero** on a strong diagonal/eye; support on echoes.
5. Use **MAD / themes** only for multi-zone frames.
6. Keep **crop integrity** — do not compose in one ratio and deliver another.
7. Record rectangle + grid in `DELIVERABLE.md` / visual-direction / prompt notes.

## Who must load this skill

| Work | When |
|------|------|
| Any **image generation** or art direction | Always, before generating |
| **web-studio** clone | First pass — region/hierarchy placement |
| **web-studio** images | Always |
| **web-studio** polish (layout/image placement) | When reviewing or moving focal elements |
| Thumbnails, brand boards, turnarounds, belt/inference images | Always when composing a frame |
| Scripture Journey `visual` lane | Always when composition matters |

Other skills **route here**; they do not keep a second copy of the method.

## Pack (safe grids)

Local agent path (binaries gitignored; not pushed to GitHub):

```text
G:\__ai-projects\_resources\design-resources\dynamic-symmetry-grids\
  US grid sizes/BLACK PNG HORIZONTAL/
  US grid sizes/BLACK PNG VERTICAL/
  extra-from-affinity/   # white-bg, extended JPEG, 11x14
  Diagonal Gauge*.jpg
```

Use **US … BLACK PNG** folders (A4 in the source pack was a duplicate). Prefer black-line PNGs; white-bg extras are OK when overlays need visibility on dark comps. Never put nude/sexually explicit study imagery from method PDFs into any deliverable.

## Do not

- Default every subject to rule-of-thirds hotspots
- Abbreviate Dynamic Symmetry as “DS” in prompts or user-facing text
- Duplicate this method inside other skills — link here instead
- Change crop ratio after composing (breaks the armature)

<!-- Agent: Grok · Model: Grok 4.5 · Date: 2026-09-16 · Extracted as canonical skill; CDSJ and image/layout paths route here. -->
