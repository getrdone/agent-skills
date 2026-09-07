# Branching Journey (choose-your-own-adventure)

Use to design and build a curiosity-driven Scripture Journey whose reader chooses their own path — while the page still keeps one governing promise, one honest payoff, and full high-trust ethics.

Authored fresh for this skill (no strong community source exists for web-native branching Scripture journeys; lightly informed by game-narrative and text-adventure patterns). Read with `web-experience.md` (build standard), `scripture-study.md` (study content), `learning-and-writing.md` (writing), and the next-path presentation rules in `web-experience.md`.

## Why branch

A linear page teaches; a branching page *pulls*. Letting the reader choose turns curiosity into a conversation: each fork is a real question the reader answers by deciding where to go next. Branching works when it deepens engagement without breaking the learning map or hiding the answer manipulatively.

High-trust limits (from the shared spine):

- Every branch is legitimate and rewarding — no "wrong" choice that punishes, no trap doors, no gotcha dead ends.
- Choices must open real curiosity gaps and lead to real content, never to the same content restated as if it were new.
- No manufactured suspense, fear escalation, or "choose wrong and lose."
- Branching organizes the path; it must never withhold the answer manipulatively.

## Structure: a graph of nodes, not a linear page

Model the journey as **nodes** (each a question or idea with content and payoff) connected by **choices** (outgoing links).

- **Entry node** — the familiar anchor and the one governing question.
- **Spine** — the core path that carries the main promise; every excursion returns here.
- **Branch nodes** — explorations the reader can take or skip (evidence, background, a sub-question, a person, a tension).
- **Convergence** — branches rejoin the spine at a payoff, so the reader never feels lost.
- **Terminal step** — whenever the journey continues, a node ends with a next step using the featured-direct-plus-four-alternates pattern (one primary continuation, two more direct, one moderately related, one wildcard); the final node resolves instead of fanning out.

Recommended shapes, simplest first:

1. **Spine with excursions** (default) — a clear main line; branches loop back to it.
2. **Hub-and-spoke** — one central passage; choices explore its facets and return.
3. **Decision tree with convergence** — choices fork, then reconverge at a shared payoff.
4. **Multiple angles** — different paths end on different *angles* of the same truth (never contradicting truths).

Avoid a free graph with no visible spine (readers get lost) and cycles that trap without a clear way back.

## Choice design (the writing)

- **Lead with the question or statement; trail with the verse reference** — same rule as the next-path section. The reader's first read is the curiosity gap; the citation follows as a receipt.
- **Make choices genuinely different.** Two choices that lead to the same payoff are not a choice; they are decoration. Each option opens a distinct gap.
- **Rank by scale and placement, never by internal labels.** The primary path is visually dominant; the alternates are quieter. Do not print taxonomy ("related", "wildcard") for the reader.
- **Keep the fan-out small.** Two to four choices on ordinary branch nodes; reserve the full featured-plus-four (five choices) for the terminal step only, and treat it as a ceiling, not a target.
- **Each choice names a curiosity, not an instruction.** "When shepherds fail" (a gap) beats "Read about bad shepherds" (an order).

## Mechanics (interactive journey)

- Prefer real links (`<a href>`) or clear buttons to real nodes so paths are shareable and deep-linkable (`#fragment` or URL).
- Keep each node's truth, question, and answer in semantic HTML.
- JavaScript may drive state, transitions, progress, visited marks, resume (`localStorage`), and motion—**build and verify that experience**; do not leave half-wired controls.
- Full transition motion is default; optional simplify only under `prefers-reduced-motion: reduce`.

Layered features to include when they serve the design:

- **Progress + location** — breadcrumb or "you are here."
- **Visited state** — mark nodes already seen.
- **Resume** — continue where the reader left off.
- **Transition motion** — purposeful reveals between nodes.

## Example node shape (illustrative)

```markdown
## What kind of sheep am I?            ← node: one question

[content + honest payoff, with cited verses — KJV first, then others]

**Continue** — the first line is the featured primary and must be visually dominant; the rest are quieter alternates:
- **The Shepherd who knows your name — John 10**  ← featured primary
- When shepherds fail — Ezekiel 34
- Confidence when enemies remain — Psalm 27
- Can any place hide you? — Psalm 139
```

## Writing and pacing

- One question per node; one honest payoff per node (experience sequence: Attention → Emotion → Clarity → Progress → Payoff → Reflection → Next Curiosity).
- Reveal context in small, just-in-time pieces; do not front-load a full outline.
- Define hard terms in plain language; spell out verse ranges ("verses 8–11," never "vv.").
- End every node on a real payoff plus a clear next choice — never a dead end.

## Checklist (per branching journey)

- [ ] One governing promise; every branch serves it.
- [ ] Spine is visible; every excursion returns or converges.
- [ ] Every choice leads with a question/statement and trails the verse reference.
- [ ] No fake choices (distinct gaps per option) and no punitive dead ends.
- [ ] Navigation works in a browser (links/buttons, deep links); JS interactions verified.
- [ ] Progress, visited state, and resume available when designed.
- [ ] Full motion by default; keyboard and touch accessible on real controls.
- [ ] No choice pre-closes its gap (no leaked payoff); passes the next-path presentation rules.
- [ ] Quality gates run before release.
