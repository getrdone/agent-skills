---
name: artwork-prompts-handoff
description: >
  Create a numbered, paste-ready artwork prompt pack for manual generation in the user's chosen tools.
  Use only when the user explicitly asks for prompts, an art handoff, or says they will generate the
  images themselves. Do not intercept ordinary requests to generate or edit an image directly.
---

# Artwork prompts handoff

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->

Use this skill only for an explicit manual-generation handoff. If the user asks the agent to generate or edit the image directly, use the appropriate available image or design capability instead.

## Load with visual work

**Always** load [`skills/dynamic-symmetry/SKILL.md`](../dynamic-symmetry/SKILL.md) before writing prompts (skim glossary; open method if needed). Stamp each prompt with rectangle + armature.

If the task is ministry/Scripture/video packaging, also load the Scripture Journey visual lane
(`skills/curiosity-driven-scripture-journey/versions/<CURRENT>/references/visual-system.md`).
Resolve `<CURRENT>` from that skill's `CURRENT` file — never from a copy at its root.

## When this skill fires

- “Write image prompts” or “make me a prompt pack.”  
- “I’ll generate the images myself.”  
- A project explicitly requires a recorded human-generation handoff with filenames and production notes.  

## Output: the prompts pack

A prompts pack is a **deterministic deliverable** (repo root [`WORKSPACE.md`](../../WORKSPACE.md) §3): it is written from the project's visual
direction, not chosen between competing versions. Write the canonical name on the first pass.

```text
prompts/artwork-prompts.md              # standard project scaffold
<stem>.artwork-prompts.md               # flat series folders
```

- A re-run for the same art direction **overwrites** the pack. Assets already generated keep their
  ticked checkboxes — carry them forward rather than resetting the file.
- Use `_vN` only when the user wants the previous pack kept for comparison, or when a page pass changed
  the art direction and both packs must exist side by side.
- If the user explicitly asked two agents for **rival** packs, that is a bake-off and the agent suffix
  applies for its duration (WORKSPACE §3b, the one surviving use).
- If `prompts/` does not exist, create it. Never delete an existing pack.

**Pairing with a page draft:** when prompts ship with an HTML journey pass, keep the two in step. If the
page is a bake-off draft (`index_<agent>.html`), the pack that belongs to it carries the same token.
Otherwise both are canonical and both are simply current.

## File structure (required)

```markdown
# Artwork prompts — <project / episode / topic>

**Status:** awaiting human generation  
**Created:** <date>  
**Agent:** <exact agent name that produced this file>  
**Model:** <exact model the agent ran on>  
**Agent vision summary:** <2–4 sentences: what the set must achieve together + the shared visual language that will tie every image>

## How to use (human)

1. Open your tool (Canva, Leonardo, Midjourney, Photoshop gen, etc.).
2. Work **top to bottom**; one prompt = one asset.
3. Save each file using the exact **Target filename**.
4. Tick the checkbox when done.

## Shared visual language (mandatory – apply to every prompt)

This is the single most important rule. All images in the set must feel like they belong to the same family.

- **Shared style / medium:** (e.g. painterly impressionistic with visible brushwork, or soft cinematic realism, etc.)
- **Shared color grade / palette:** list the core colors that must appear across the set
- **Shared lighting approach:** (e.g. soft golden first light, cool overcast, etc.)
- **Shared mood adjectives:** 4–7 words that every image must carry
- **Composition standard:** Dynamic Symmetry (never abbreviate as “DS”)
- **Global avoid list:** fear-porn, nude/sexual imagery, fake evidence, clutter, text-on-image unless explicitly required, modern objects, logos, watermarks, signatures, neon/candy colors, stock-photo look, cartoon/anime, children’s Bible illustration, glossy 3D, plastic textures

## Prompt list

### P01 — <short title>
- [ ] **Done**
- **Agent:** <name of agent writing this prompt> · **Model:** <model>
- **Role:** hero | section background | thumbnail | etc.
- **Target filename:** `deliverables/assets/p01-short-name.jpg`
- **Dimensions:** 16:9 — 1920×1080 (or exact required size)
- **Dynamic Symmetry armature:** Root 3 / Phi / etc. + short placement note
- **Alt text:** …
- **Notes:** (any special instructions)

**Prompt (copy everything inside the block):**

```text
<full self-contained prompt that includes:
- subject, setting, time of day, lighting
- the shared style + color grade + mood from the Shared visual language section above
- Dynamic Symmetry composition instructions written out
- exact dimensions if the tool needs them
- everything that must appear and everything that must be avoided
- no external references such as “same as above”>
```

### P02 — …
```

**Critical rules for every prompt**

1. One prompt = one image. Never combine assets.
2. The prompt itself must be fully self-contained and copy-paste ready. All style, color, lighting, composition, and negative instructions live inside the prompt text.
3. Always expand “DS” to the full words **Dynamic Symmetry**.
4. Dimensions must appear both in the notes above the prompt and inside the prompt when the tool benefits from it.
5. Begin the notes section with the agent name and model.
6. Creative concepts are required, but every image must share the same visual language defined at the top of the file so the set feels cohesive rather than like disconnected islands.
7. After assets exist, do not regenerate the whole prompts file unless asked.

## Agent behavior after handoff

1. Stop generative-art work at the prompts file (plus any layout wireframes that don’t need pixels).  
2. Tell the user clearly: *“Credits/API not used — prompts are in `…`. Generate in order and drop files in `…`.”*  
3. When the user says assets are ready, read `mood/` / `deliverables/assets/`, match filenames, continue layout/HTML/thumbnail pairing.  
4. If an asset is missing, point to the exact `P0n` still unchecked—don’t invent a new full set.

## Optional later: paid MCP

Only if the user says to use Canva/Leonardo **and** confirms credits:

- Follow machine MCP docs in `F:\__ai-projects\_agent-control\mcp\README.md`  
- Still keep or update the prompts file as the creative record  

## Relationship to other skills

| Skill / doc | Role |
|-------------|------|
| `dynamic-symmetry` | Canonical armature / crop / placement (required) |
| `curiosity-driven-scripture-journey` → `visual` lane | Vision, type, palette, motion language |
| its `packaging` lane | Title selected before final thumbnail art when packaging video |
| This skill | **Human generation handoff** |

## Done when

- [ ] `prompts/artwork-prompts.md` exists with shared style lock + numbered prompts  
- [ ] Every needed asset has role, filename, aspect, paste-ready prompt  
- [ ] User knows where to save files and how to call the agent back  
- [ ] Previously ticked checkboxes were carried forward, not reset

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 · Prompts pack is canonical on first write; naming rules now live only in WORKSPACE.md §3. -->
