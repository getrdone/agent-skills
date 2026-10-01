# artwork-prompts-handoff

Default path for artwork when API credits (Canva / Leonardo / etc.) are not in play:

1. Agent writes `prompts/artwork-prompts.md` with every paste-ready prompt and a set differentiation matrix.
2. Human generates assets one by one in their own tools.
3. Files land in `mood/` or `deliverables/assets/` with matching topic-prefixed IDs, such as `antichrist_p01.webp`.
4. Agent continues layout with real files.

The matrix is a hard planning gate for sets of two or more related assets. Cohesion comes from shared palette, light, mood, and editorial discipline; it does not justify repeating the same primary prop, medium, question, and focal placement across every asset.

Every prompt block is under 2000 characters, and each entry prints its measured character count. Past roughly that length, image tools drop the tail of a long instruction list — which is exactly where the negative instructions live. Compress a prompt that runs long; never truncate it, and never cut a locked exclusion to fit.

A second art direction for the same subject ("modern", "high-tech") is a separately numbered set in the same pack with its own matrix, continuing the numbering. It keeps the shared visual language including every palette and content lock, and the human instructions say the sets are alternatives and must not be mixed.

When reviewing generated images, identify every observation by exact filename, mark duplicates, and evaluate curiosity/payoff separately from literal fact-checking unless the user asks for fact-checking.

Entry: `SKILL.md`

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 2026-09-28 · Release 1.2.3 -->
<!-- Agent: Buffy | Model: not exposed | Thinking: not exposed | Date: 2026-09-30 · Release 1.2.4 — hard 2000-character prompt budget, measured counts printed in the pack, and a rule for alternate art-direction sets. -->
