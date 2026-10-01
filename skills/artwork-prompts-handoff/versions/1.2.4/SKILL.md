---
name: artwork-prompts-handoff
description: >
  Create a numbered, paste-ready artwork prompt pack for manual generation in the user's chosen tools.
  Use only when the user explicitly asks for prompts, an art handoff, or says they will generate the
  images themselves. Do not intercept ordinary requests to generate or edit an image directly.
---

# Artwork prompts handoff

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-08 -->
<!-- Agent: freebuff | Model: Space Bunny | Thinking: not exposed | Date: 2026-09-24 · Released 1.2.1 with the set-differentiation gate after a repeated-motif evaluation failure. -->
<!-- Agent: Buffy · Model: not exposed | Thinking: not exposed | Date: 2026-09-30 · Released 1.2.4 with the hard 2000-character prompt budget. -->

Use this skill only for an explicit manual-generation handoff. If the user asks the agent to generate or edit the image directly, use the appropriate available image or design capability instead.

## Prompt length budget (hard requirement)

**Every prompt block must be fewer than 2000 characters.** This is a hard ceiling, not a target. A user may ask for a tighter budget for one pack; that tighter number becomes the ceiling for that pack and the 2000-character figure stays the outer limit.

1. **Count the characters of the text inside each ```text fence, not the surrounding notes.** Markdown headings, alt text, target filenames, and the negative list in Shared visual language are not part of the count.
2. **Print the measured count in the pack** on a `**Prompt length:** N characters` line under each block, so the human can audit the rule without re-counting and so a later edit that breaks it is visible.
3. **Never ship a prompt at or above the ceiling.** If a prompt runs long, cut it — do not ship it and hope.
4. **Compress; never truncate.** Cutting means rewriting a long sentence into a shorter equivalent, dropping a duplicated adjective, or collapsing a repeated clause. Never end a block mid-sentence and never delete a trailing clause of the negative list to save characters.
5. **Cut in this order, keeping every exclusion that changes the image:** drop restatement of the subject; merge repeated "no" clauses; shorten palette and lighting phrasing that restates Shared visual language; shorten the mood list; shorten the Dynamic Symmetry description. Cut the subject description and the negative list last, because those are what the generation tool acts on.
6. **Never shorten by removing a locked exclusion.** A campaign lock, a legal avoidance, or a "must never appear" instruction outranks the budget. A prompt that cannot be written under the ceiling without dropping a lock is a prompt to take to the user, not to trim.
7. **Self-contained still wins.** The budget does not license "same as above," "as described earlier," or any other external reference. Every prompt repeats everything it needs, compressed if necessary.

Past roughly two thousand characters, image tools start dropping the tail of a long instruction list. That is why this is a hard rule and not a style preference: the exclusions that keep a generated image usable are exactly the words that stop arriving.

## Required prompt opening rule

Every prompt must begin with a concrete subject or concept sentence for that specific image or clip. Do not open with only mood, composition, lighting, or an abstract phrase.

A sufficient opening identifies the subject, scene, object, figure, setting, or symbolic concept that the image represents; uses plain language a generation tool can build from; and is specific to the requested asset rather than a reusable generic opener.

This is a hard requirement for every prompt. Do not replace the subject sentence with only atmosphere, style, composition, lighting, or a generic concept label. If the asset is intentionally abstract, state what the concept represents in concrete terms.

## Set differentiation gate (hard requirement)

A cohesive set must not become a repeated set. Before writing the prompt list for two or more related assets, create a compact **set differentiation matrix** with one row per asset. The matrix must lock:

- **Primary subject** — the main object, figure, or scene that carries the asset.
- **Representation medium** — stone, handwriting, LCD, photograph, diagram, archival material, or another materially distinct medium.
- **Historical or contextual register** — the time, place, or interpretive frame the asset evokes.
- **Question or job** — what distinct question, role, or teaching beat the asset serves.
- **Visual treatment** — the dominant Dynamic Symmetry armature, focal placement, material emphasis, and negative-space strategy.

Then apply this anti-repetition gate:

1. Two neighboring assets must not share the same primary subject, representation medium, contextual register, question, and focal placement.
2. If the user wants a deliberately repeated motif, keep the repetition intentional and vary at least two other dimensions: subject, medium, register, question, or composition.
3. Never fill a set with several near-identical paper cards, screens, symbols, or hero props merely because they are easy to describe. If a card series is requested, each card must have a distinct representational job and focal object.
4. Place the matrix before the prompt list in the pack. The matrix is a planning gate, not optional commentary.
5. Before handoff, compare the matrix rows again. If two rows still describe the same image with different titles, redesign one row before writing the final prompt.

This gate is about meaningful visual difference, not random variety. Assets should still share palette, light, mood, and editorial quality; they should not share their central visual idea by default.

## Alternate art directions for the same subject

When a user wants a second look at a subject — "modern," "high-tech," "illustrated," "older" — build it as a **separate numbered set inside the same pack**, not as extra rows of the existing set.

1. Give the alternate set its own matrix and its own anti-repetition check.
2. Number it as a continuation of the pack (`p04`–`p06`), never as a second set reusing `p01`–`p03`.
3. State plainly in the human instructions that the sets are alternatives and **must not be mixed** — a viewer who sees one frame from each reads two campaigns, not one.
4. **Keep the shared visual language, including every palette and content lock.** A register change is a change of material, light, and subject treatment, not a licence to add a colour or a motif the campaign forbids. A high-tech set that reads "high-tech" because of material and light alone is more disciplined than one that reaches for the trend's default colours.
5. Register changes still obey the opening rule, the negative list, and the length budget.

## Image review handoff (hard requirement)

When reviewing generated images for the user, make the files auditable. The user must be able to map every observation back to the exact image they supplied.

1. Put the exact filename in backticks at the start of every observation, ranking entry, shortlist item, warning, or approval note.
2. Prefer a compact review table with: `Filename | What I see | What works | Payoff/claim note | Action`.
3. If two files are identical or near-identical, list both exact filenames and mark the relationship explicitly. Never refer to images only as “the first one” or “the stone image.”
4. Default to a curiosity/payoff review, not a fact-checking audit. Note literal claims or historical precision only when they would materially mislead relative to the user’s stated project frame.
5. Separate a project-supported interpretive frame from a literal universal claim. A visual metaphor about technology, authority, control, or coercion can be valid for the project without claiming that every device literally contains the number.
6. A strong ad image may compress or imply historical details that the transcript does not spell out one by one. Judge whether the visual promise is directionally aligned with the video’s actual subject and payoff, not whether every visual detail is spoken verbatim.

A review without filenames is incomplete. When filenames are missing from the user’s attachment metadata, say so and ask for them rather than guessing.

## Load with visual work

**Always** load [`skills/dynamic-symmetry/SKILL.md`](../../../dynamic-symmetry/versions/1.1.0/SKILL.md) before writing prompts (skim glossary; open method if needed). Stamp each prompt with rectangle + armature.

If the task is ministry/Scripture/video packaging, also load the Scripture Journey visual lane
(`skills/curiosity-driven-scripture-journey/versions/<CURRENT>/references/visual-system.md`).
Resolve `<CURRENT>` from that skill's `CURRENT` file — never from a copy at its root.

## When this skill fires

- “Write image prompts” or “make me a prompt pack.”
- “I’ll generate the images myself.”
- A project explicitly requires a recorded human-generation handoff with filenames and production notes.
- A user asks for an existing pack to be shortened, or asks for a prompt-length limit to be enforced from now on.

## Output: the prompts pack

A prompts pack is a **deterministic deliverable** (repo root [`WORKSPACE.md`](../../../../WORKSPACE.md) §3): it is written from the project's visual direction, not chosen between competing versions. Write the canonical name on the first pass.

```text
prompts/artwork-prompts.md              # standard project scaffold
<stem>.artwork-prompts.md               # flat series folders
```

- A re-run for the same art direction **overwrites** the pack. Assets already generated keep their ticked checkboxes — carry them forward rather than resetting the file.
- Use `_vN` only when the user wants the previous pack kept for comparison, or when a page pass changed the art direction and both packs must exist side by side.
- If the user explicitly asked two agents for **rival** packs, that is a bake-off and the agent suffix applies for its duration (WORKSPACE §3b, the one surviving use).
- If `prompts/` does not exist, create it. Never delete an existing pack.

## Artwork asset IDs and filenames

Use the series/topic stem followed by an underscore and a two-digit prompt number for **both** the prompt ID and the asset filename: `<topic>_p01`, `<topic>_p02`, and so on. Example: an Antichrist set uses `antichrist_p01.webp` through `antichrist_p06.webp`, and its matrix and prompt headings use the matching IDs. Choose one short, lowercase topic stem for the pack; use a kebab-case stem if it has multiple words. Preserve the number when an asset is revised so its prompt, review notes, and file still match. Do not use bare `p01` filenames or rename assets by subject. See `WORKSPACE.md` §3 for the library's file-naming authority.

**Pairing with a page draft:** when prompts ship with an HTML journey pass, keep the two in step. If the page is a bake-off draft (`index_<agent>.html`), the pack that belongs to it carries the same token. Otherwise both are canonical and both are simply current.

## File structure (required)

```markdown
# Artwork prompts — <project / episode / topic>

**Status:** awaiting human generation  
**Created:** <date>  
**Agent:** <exact agent name that produced this file>  
**Model:** <exact model the agent ran on>  
**Thinking:** <exact thinking level, or not exposed>  
**Agent vision summary:** 2–4 sentences: what the set must achieve together + the shared visual language that will tie every image>

## How to use (human)

1. Open your tool (Canva, Leonardo, Midjourney, Photoshop gen, etc.).
2. Work **top to bottom**; one prompt = one asset.
3. Save each file using the exact **Target filename**.
4. Tick the checkbox when done.

## Set differentiation matrix — required before generation

| Asset | Primary subject | Representation medium | Register | Question / job | Visual treatment |
|---|---|---|---|---|---|
| topic_p01 | ... | ... | ... | ... | ... |
| topic_p02 | ... | ... | ... | ... | ... |

**Anti-repetition check:** <state what changed between neighboring rows and why the set is not a repeated motif.>

## Shared visual language (mandatory – apply to every prompt)

This is the single most important rule. All images in the set must feel like they belong to the same family.

- **Shared style / medium:** (e.g. painterly impressionistic with visible brushwork, or soft cinematic realism, etc.)
- **Shared color grade / palette:** list the core colors that must appear across the set
- **Shared lighting approach:** (e.g. soft golden first light, cool overcast, etc.)
- **Shared mood adjectives:** 4–7 words that every image must carry
- **Composition standard:** Dynamic Symmetry (never abbreviate as “DS”)
- **Global avoid list:** fear-porn, nude/sexual imagery, fake evidence, clutter, text-on-image unless explicitly required, modern objects, logos, watermarks, signatures, neon/candy colors, stock-photo look, cartoon/anime, children’s Bible illustration, glossy 3D, plastic textures

## Prompt list

### topic_p01 — <short title>
- [ ] **Done**
- **Agent:** <name of agent writing this prompt> · **Model:** <model>
- **Role:** hero | section background | thumbnail | etc.
- **Target filename:** `deliverables/assets/topic_p01.jpg`
- **Dimensions:** 16:9 — 1920×1080 (or exact required size)
- **Prompt length:** <measured character count> characters
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

### topic_p02 — …
```

**Critical rules for every prompt**

1. One prompt = one image. Never combine assets.
2. The prompt itself must be fully self-contained and copy-paste ready. All style, color, lighting, composition, and negative instructions live inside the prompt text.
3. Always expand “DS” to the full words **Dynamic Symmetry**.
4. Dimensions must appear both in the notes above the prompt and inside the prompt when the tool benefits from it.
5. Begin the notes section with the agent name and model.
6. Creative concepts are required, but every image must share the same visual language defined at the top of the file so the set feels cohesive rather than like disconnected islands.
7. After assets exist, do not regenerate the whole prompts file unless asked.
8. For every set, complete the differentiation matrix and the final anti-repetition check before handing off the pack.
9. **Stay under 2000 characters per prompt and print the measured count** in each entry's notes (see Prompt length budget).

## Agent behavior after handoff

1. Stop generative-art work at the prompts file (plus any layout wireframes that don't need pixels).
2. Tell the user clearly: “Credits/API not used — prompts are in `…`. Generate in order and drop files in `…`.”
3. When the user says assets are ready, read `mood/` / `deliverables/assets/`, match filenames, continue layout/HTML/thumbnail pairing.
4. If an asset is missing, point to the exact `P0n` still unchecked—don't invent a new full set.

## Optional later: paid MCP

Only if the user says to use Canva/Leonardo **and** confirms credits:

- Follow machine MCP docs in `G:\__ai-projects\_agent-control\mcp\README.md`
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
- [ ] The set differentiation matrix exists and shows a meaningful difference between related assets
- [ ] The anti-repetition check confirms that the set is not made from near-identical repeated motifs
- [ ] Any image review identifies every observation by exact filename and marks duplicates explicitly
- [ ] Every needed asset has role, filename, aspect, paste-ready prompt
- [ ] Prompt IDs, matrix rows, target filenames, and saved assets use the same `<topic>_pNN` stem and number
- [ ] **Every prompt block is under 2000 characters and its measured count is printed in the pack**
- [ ] Any alternate art direction is a separately numbered set with its own matrix, and the instructions say not to mix the sets
- [ ] User knows where to save files and how to call the agent back
- [ ] Previously ticked checkboxes were carried forward, not reset

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed | Date: 2026-09-10 · Prompts pack is canonical on first write; naming rules now live only in WORKSPACE.md §3. -->
<!-- Agent: Buffy · Model: GPT-5 · Thinking: not exposed | Date: 2026-09-24 · Released 1.2.0 with the mandatory concrete subject/concept opening rule; unapproved image examples remain outside the active release. -->
<!-- Agent: freebuff · Model: Space Bunny · Thinking: not exposed | Date: 2026-09-24 · Released 1.2.2 with filename-first image reviews and curiosity/payoff evaluation guidance after a multi-image review. -->
<!-- Agent: Codex · Model: GPT-6 · Thinking: not exposed | Date: 2026-09-28 · Release 1.2.3 uses Steve's topic_pNN artwork naming convention. -->
