# Scripture Journey v3 — development and experience workflow

## 1. Two-stage operating model

### Phase A — Develop the Journey

Do not begin substantial production HTML merely because a topic exists. Develop the idea until the user can judge the *journey*, not just the rendered page.

Build a compact Journey Concept from:

- central question and audience curiosity;
- why-care and primary payoff;
- evidence sequence, difficult texts, objections/tensions, and truth boundaries;
- broad title/idea field;
- user-selected favorites and synthesis of why they work;
- learner jobs: what the reader must notice, compare, inspect, predict, resolve, retrieve, reflect on, or choose;
- emotional/progression arc;
- 2–4 credible visual metaphors / experience archetypes;
- interaction opportunities that arise naturally from the evidence;
- next-curiosity paths;
- locked decisions and open decisions.

A Journey Concept may live inside the canonical project brief. Do not create another Markdown file merely to hold the same state.

### Phase B — Create the Experience

Begin production after the concept is developed enough that the build agent is not simultaneously inventing theology, curriculum, title, visual metaphor, interaction architecture, and implementation.

Production sequence:

1. Translate learner jobs into the smallest effective learning-tool set.
2. If visual direction is unresolved, propose 2–4 genuinely different experience concepts before coding.
3. Select or inherit a content-fitting page archetype.
4. Build an agent-versioned candidate; never overwrite canonical output during iteration.
5. Run the deterministic HTML audit.
6. Run independent design, learning, accessibility, performance/code, and applicable security/error-handling reviews.
7. Fix blocking issues and re-run the affected reviews.
8. Present the candidate for human taste/direction review only after mechanical defects are resolved.
9. Promote only the accepted deliverable.

The user may explicitly order a direct build. In that case, make missing assumptions visible and keep agent-invented choices candidate-level.

## 2. Ideation modes

Breadth is intentional because apparently weak categories can contain useful seeds.

- **Quick:** about 24–32 ideas across strongest categories plus a deliberate minority of unusual/weak-fit territory.
- **Standard (default):** about 36–48 ideas with broad category coverage and real variation.
- **Full Matrix:** all 17 YouTube-planner categories × exactly 4 lines = 68 ideas.
- **Deep:** about 80–120 ideas when the user explicitly wants exhaustive exploration.

Do not automatically prune ideas because the agent rates the category weak.

### Selection synthesis

After the user marks favorites, analyze why they work:

- curiosity mechanism;
- theological/content angle;
- wording rhythm;
- implied promise;
- emotional tone;
- visual potential;
- teachability / continuation potential.

Then produce a second set of hybrids, refinements, and neighboring concepts. Do not merely rephrase the selections.

## 3. Learner jobs before named patterns

First identify what the learner needs to *do* with the evidence. Typical jobs include:

- notice a contrast;
- compare passages or sources;
- inspect context;
- predict an implication;
- resolve an apparent contradiction;
- arrange or trace an evidence sequence;
- retrieve the main conclusion;
- reflect or choose a next question.

Then choose the smallest effective set of learning patterns/interactions. A substantial journey will often use 2–5, but no fixed count or family quota overrides usefulness.

An interaction fails when it is merely a styled container, hides core truth for no reason, duplicates another interaction's job, or adds clicks without improving understanding.

## 4. Experience-concept gate

Before production HTML, define 2–4 credible experience concepts unless the user already approved one. Each concept states:

- page archetype;
- dominant visual metaphor;
- what visibly changes as the learner advances;
- primary composition and eye path;
- imagery strategy;
- typography personality;
- interaction signature;
- motion character;
- how the ending visually resolves the opening.

Useful archetypes include evidence trail, visual investigation, unfolding case, document/exhibit, comparison journey, timeline, story-led journey, layered diagram, map/trail, immersive photographic journey, editorial feature, and interactive explorer.

### Generic-article fail condition

A repeated hero + centered reading column + repeated cards/sections is not a neutral default. If the content does not specifically call for that architecture, treat it as a concept failure and develop another composition.

Existing Hell Journey and Psalm 23 generations may be inspected as regression examples, never as positive design benchmarks.

## 5. Markdown restraint

Do not create a Markdown file for every internal pass.

Prefer:

- one canonical `project-brief.md` for durable decisions;
- one shared `NOW.md` for status/navigation;
- agent-versioned files for actual deliverables and human-useful prompt packs;
- a review report only when it has durable handoff/audit value.

Transient reasoning, critic scratch notes, and checklists should remain ephemeral. SQLite project-state storage is explicitly deferred beyond v3.0.0.
