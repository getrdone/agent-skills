# Claude Code — burn-day mission (agent-skills)

**Repo:** `F:\__ai-projects\agent-skills` → `https://github.com/getrdone/agent-skills`  
**Constraint:** Expand capability and knowledge density. **No bloat.** Every addition must earn its keep by making agents faster, more consistent, or less wrong on real Final Days / ministry workflows. Prefer deepening CURRENT skills over inventing parallel ones. Prefer deleting/folding duplicates over stacking.

## What this repo is today (ground truth)

- Shared multi-agent skill brain (Grok/Claude/Codex/Cursor/…).
- Thin catalog: only **3** live skills — `curiosity-driven-scripture-journey` (versioned, CURRENT **3.2.0**), `clean-video-transcript`, `artwork-prompts-handoff`.
- Heavy CDSJ reference tree (learning patterns, design, YouTube packaging, source governance, quality gates) with full `versions/` history.
- Cross-cutting: `WORKSPACE.md`, `DESIGN-DIRECTIVES.md`, `COLOR-PSYCHOLOGY.md`, `tools/TOOLS.md`, `processing/source-vault/`.
- External Cloudflare skills stay **symlinked**, not forked.
- UBP translator tooling was **moved out** to `getrdone/ubp-tools` — do not re-absorb.

## Operating rules for this burn day

1. Read `CATALOG.md` + `WORKSPACE.md` + CURRENT CDSJ `SKILL.md` before proposing structure changes.
2. Output in this order: (A) diagnosis of gaps, (B) ranked idea list, (C) concrete file/PR plan for the top 3–5, (D) what you will **not** build and why.
3. For each idea: **problem it solves**, **why not bloat**, **touch points** (files/skills), **acceptance test** an agent can run in one session.
4. Prefer: better routing, better evals/gates, better references with provenance, better tools registry, fewer agent mistakes. Avoid: fluffy essays, fifth YouTube matrix, re-adding retired TOPIC-BOARD.
5. If you add a skill: one CATALOG row, short triggers, lean SKILL.md that points to references — do not paste novels into SKILL.md.
6. Leave `versions/` alone unless cutting history or fixing CURRENT pointers.

---

## Wild-but-core idea seeds (challenge, improve, or kill)

Use these as provocations. Replace weak ones. Keep the spirit: leverage, not decoration.

### A. Routing & anti-bloat core

1. **Skill router eval harness** — fixture prompts → expected CATALOG skill (+ version). Fail if wrong skill loads or whole repo gets preloaded. This is the highest-leverage “meta tool.”
2. **Token budget ledger** — each skill declares max files/tokens to load; a tiny checker fails PRs that break the lean-load contract.
3. **Dead-reference janitor** — scan CURRENT for orphaned/duplicate refs; propose merges; especially chase duplicated docs across `versions/3.x`.
4. **Trigger collision map** — detect overlapping triggers between skills; force disambiguation rules into CATALOG.
5. **“Judgment mode” playbook** — when no skill matches, a short STANDARD for how agents invent process without inventing a new skill every time.

### B. CDSJ depth (robust, not fatter)

6. **Honest-curiosity adversarial suite** — expand the reject standard into golden failing titles/descriptions; agents must score them.
7. **Source-alignment verifier** — given a titles pack + SQLite/source vault, assert every claim maps to a registered source ID (or flag “unbacked”).
8. **Episode state machine** — formal states (ingest → titles → descriptions → art → page → publish) with `STATUS.md` schema and illegal transitions.
9. **Thumbnail brief compiler** — from titles + visual-system tokens → one paste-ready Leonardo/Canva brief; no new design philosophy, just binding existing ones.
10. **AEO/SEO claim lint** — forbid medical/prophetic overclaim patterns; require “high-trust” phrasing gates already implied by quality docs.
11. **Branching journey simulator** — textual walkthrough of `branching-journey.md` paths to catch dead ends before build.
12. **Multi-agent draft reconciliation protocol** — rules for merging `*_grok` / `*_claude` drafts into canonical without losing the chosen voice.

### C. Transcript → packaging pipeline

13. **clean-video → CDSJ bridge skill** — one command path: cleaned transcript + Quick Reference → title matrix inputs (not a mega-skill; a thin adapter).
14. **Quick Reference quality grader** — verse/EGW order + highlight usefulness checks; catch empty or out-of-order end-matter.
15. **Speaker/series fingerprint spelling packs** — extend SPELLING.md modularly per series without bloating the base file.

### D. Source vault & knowledge ops

16. **source-vault → agent Q&A contract** — how agents query registry.yaml / SQLite without dumping the library into context.
17. **Provenance freshness cron doc** — automate EXTERNAL fold re-sync checks (impeccable, awesome-copilot) into a single report skill.
18. **Private library quarantine rules** — harden Bohr transcript quarantine into a reusable intake checklist with examples.

### E. Tools & agent ops

19. **TOOLS.md → executable capability matrix** — each tool: auth needed, agent can drive?, failure modes, “use when.”
20. **MCP/connector playbooks** — thin skills for mailbox.org / Telnyx / GitHub patterns already used in real ops (Final Days), without embedding secrets.
21. **Workspace auto-scaffold tests** — create a fake topic folder and assert AGENTS/NOW/draft naming conventions.
22. **Install-wiring dry-run** — document and script a `--check` mode for junctions/sync so agents stop re-running install blindly.

### F. Design system leverage

23. **Palette → CSS token compiler** — from DESIGN-DIRECTIVES + COLOR-PSYCHOLOGY → a validated token snippet for landing pages (a11y contrast check required).
24. **Anti-slop screenshot rubric** — checklist agents use when reviewing UI screenshots against design-critique refs.
25. **Brand-pack loader** — how to bind `design-resources` pack per project without copying files into agent-skills.

### G. “Crazy” bets that still pay rent

26. **Skill mutation budget** — any new skill must delete or fold ≥1 obsolete path (net complexity ≤ 0 unless Steve waives).
27. **Agent amnesia drills** — cold-start prompts with only CATALOG; measure whether CURRENT CDSJ still produces shippable titles.
28. **Single “ministry day” runbook** — one page that chains transcript clean → titles → descriptions → art handoff → page gates for a real episode (uses existing skills only).
29. **Public vs private skill split plan** — what could open-source vs what stays Final Days–private (decision doc, not a rewrite).
30. **Version gravity well** — make CURRENT so good that agents never need to open `versions/`; add a “why not load history” warning.

---

## Deliverables Steve wants from Claude today

1. `IDEAS-RANKED.md` — your ranked list (include kills of weak seeds).
2. Implement **only** the top items that are clearly high leverage (prefer harnesses, bridges, gates, janitors).
3. PR-ready commits with agent trailers matching repo style.
4. Update `CATALOG.md` only when routing truly changes.
5. End-of-day note: what became more robust vs what was correctly refused as bloat.

## Explicit non-goals

- Rebuilding UBP inside this repo.
- Forking Cloudflare skills.
- Restoring TOPIC-BOARD.
- Duplicating CDSJ references into new skill folders.
- Mass rewriting `versions/**` history.

---

## UPDATE 2026-09-10 — whole-stack revision

Steve clarified scope: **agent-skills + Scripture Journey + media-organizer (+ pages/stories)**.  
Read and prefer: `F:\__ai-projects\STACK-ROBUSTNESS-PLAN.md`.

Key change: **Do split CDSJ into loadable packs** behind one router + `PROJECT-STATUS` continuity. Do not create disconnected rival skills.  
Also design media-organizer toward **offline orchestrator → GUI/exe**.

Re-rank ideas against that plan; implement STATUS+router+pack map before cosmetic skills.

---

## UPDATE 2026-09-10b — reasoned plan (HTML), not agree-mode

**Read this first:** `F:\__ai-projects\STACK-ROBUSTNESS-PLAN.html`

Critical revision vs earlier pack-split note:
- Do **not** physically split CDSJ into packs/ or new CATALOG skills on this burn day.
- Do ship `load-map.yaml` (soft lanes → exact reference files), PROJECT-STATUS contract, router LOAD emission, and eval fixtures.
- Fear-bait packaging conflicts with CDSJ spine — honest stakes / curiosity only.
- media-organizer: M0 orchestrator + job JSON before GUI; GUI wraps existing scripts.
- Markdown `STACK-ROBUSTNESS-PLAN.md` is obsolete pointer only.

---

## UPDATE 2026-09-10c — stem convention + idea board + Claude self-check

Steve locked:
- Centralized CDSJ (no pack split).
- Real/honest stakes OK; manufactured fear-for-click forbidden.
- Progressive stems with append-in-place (not per-agent draft sprawl):
  `stem.titles.md` → `stem.titles+descriptions.md` → `stem.titles+descriptions+visuals.md`
  SELECTED at top (user-owned); agents append dated Run sections; `_vN` only for rare snapshots.

Idea board (expanded harness defs): open/save from chat attachment or recreate at
`F:\__ai-projects\STACK-HARDENING-IDEAS.html`

Claude independent reasoning prompt:
`F:\__ai-projects\CLAUDE-REASONING-CHECK-PROMPT.html`
Paste that prompt into Claude Code; require output `HARDENING-PLAN-CLAUDE.html`.
