# Learning Pattern Router

Use this file whenever an agent must choose, combine, implement, or review teaching strategies for a Scripture Journey. A pattern is a reusable learner experience with a specific learning job. It is not a visual theme, page template, or engagement trick.

## Architecture decision

Keep one `curiosity-driven-scripture-journey` skill. Make its teaching system atomic at the reference level:

- this file is the compact selector and composition contract;
- four family files hold self-contained pattern cards;
- `learning-pattern-sources.md` holds observed platform flows and research provenance;
- agents load only the family files selected for the current task.

Do not create one skill per pattern. That would create competing triggers, duplicate the Scripture constitution, and make cross-pattern composition harder. Do not put all pattern detail back into `SKILL.md`; that would make every small task pay the context cost.

## Required composition rule

For a substantive Scripture Journey, select **3–5 patterns from at least two families**. Use fewer only for a genuinely narrow answer, repair, caption, or single component.

Every selected pattern must have a named learning job. At least one selected pattern must support learner agency or access. Include an active-discovery pattern when the evidence can be inspected, compared, arranged, or manipulated honestly. Never add an interaction only to make a page feel busy.

One journey may use several patterns; one segment should normally have one dominant pattern plus, at most, one supporting pattern. Vary the mix across journeys so the experience does not become a repeated template.

An active-discovery card already includes a fixed reveal or explanation. Add `LP-FM-01` only when feedback must change in response to what the learner did; do not select it merely to repeat the active pattern's standard payoff.

## Pattern families

| Family | Load when the learner needs | Pattern IDs |
| --- | --- | --- |
| Guided understanding | orientation, explanation, scaffolding, manageable reading | `LP-GU-01`–`LP-GU-05` in `pattern-guided-understanding.md` |
| Active discovery | prediction, comparison, manipulation, ordering, transfer | `LP-AD-01`–`LP-AD-05` in `pattern-active-discovery.md` |
| Feedback and mastery | correction, help, recovery, retrieval, remediation | `LP-FM-01`–`LP-FM-05` in `pattern-feedback-and-mastery.md` |
| Access, agency, and momentum | equivalent modalities, read-along, accessible state, progress, reflection | `LP-AA-01`–`LP-AA-05` in `pattern-access-agency-momentum.md` |

Load `learning-pattern-sources.md` only when auditing evidence, extending the catalog, or explaining provenance. It is not required to implement a known pattern.

## Fast selector

| Current learning job | Start with | Common support |
| --- | --- | --- |
| Confirm what the journey will answer | `LP-GU-01` | `LP-AA-04` |
| Connect a familiar verse or concern to a new distinction | `LP-GU-02` | `LP-GU-04` |
| Model how to inspect Scripture in context | `LP-GU-03` | `LP-FM-02` |
| Keep a dense explanation manageable | `LP-GU-04` | `LP-GU-05` |
| Let the learner investigate before being told | `LP-AD-01` | `LP-FM-01` |
| Make a relationship or context change visible | `LP-AD-02` | `LP-AA-03` |
| Examine two passages, translations, claims, or contexts | `LP-AD-03` | `LP-GU-05` |
| Understand chronology, structure, speakers, or evidence order | `LP-AD-04` | `LP-FM-01` |
| Apply a principle to a fresh case | `LP-AD-05` | `LP-AA-05` |
| Explain why an observation needs correction | `LP-FM-01` | `LP-FM-03` |
| Help without giving the answer immediately | `LP-FM-02` | `LP-GU-03` |
| Turn an incomplete attempt into another useful try | `LP-FM-03` | `LP-FM-01` |
| Help an important idea remain retrievable later | `LP-FM-04` | `LP-AA-04` |
| Repair a missing prerequisite without derailing the journey | `LP-FM-05` | `LP-FM-02` |
| Let learners choose how to receive equivalent meaning | `LP-AA-01` | `LP-AA-02` |
| Support early readers, low-vision readers, or auditory access | `LP-AA-02` | `LP-AA-03` |
| Make dynamic interaction perceivable without color or sight alone | `LP-AA-03` | any interactive pattern |
| Orient the learner and distribute small payoffs | `LP-AA-04` | `LP-GU-04` |
| Close the promise and open a sincere next question | `LP-AA-05` | any evidence pattern |

## Recommended mixes

These are starting combinations, not page templates.

| Journey shape | Suggested mix | Why |
| --- | --- | --- |
| New-to-the-Bible adult | `LP-GU-01`, `LP-GU-02`, `LP-GU-04`, `LP-FM-02`, `LP-AA-05` | visible route, respectful bridge, small chunks, help on demand, clear close |
| Passage or translation comparison | `LP-AD-03`, `LP-GU-05`, `LP-FM-01`, `LP-AA-03`, `LP-AA-05` | inspection, optional context, explanation, accessible state, synthesis |
| Prophetic chronology or evidence trail | `LP-AD-04`, `LP-AD-01`, `LP-GU-04`, `LP-AA-03`, `LP-AA-04` | order evidence, invite revision, manage load, preserve access and orientation |
| Contested interpretation | `LP-GU-03`, `LP-AD-03`, `LP-GU-05`, `LP-FM-01`, `LP-AA-05` | model method, compare honestly, expose qualifications, explain limits, preserve choice |
| Family or younger learner | `LP-GU-04`, `LP-AD-02`, `LP-AA-02`, `LP-AA-04`, `LP-AA-05` | short units, meaningful play, read-along, calm progress, reflection |
| Returning learner or review | `LP-FM-04`, `LP-FM-05`, `LP-AD-05`, `LP-AA-04`, `LP-AA-05` | retrieval, repair, transfer, progress, next question |
| Long source-rich study | `LP-GU-01`, `LP-GU-05`, `LP-AD-03`, `LP-AA-04`, `LP-AA-05` | map first, keep depth optional, compare sources, orient, synthesize |

## Pattern-plan contract

Before outlining a substantial journey, record the selected patterns in the canonical brief or planning file:

```yaml
learning_pattern_plan:
  - id: LP-GU-02
    job: connect the familiar question to the first new distinction
    placement: opening after the promise
    learner_action: notice the repeated phrase in two passages
    feedback: acknowledge the observation, then name the distinction
    accessible_fallback: both passages and the prompt remain readable without JavaScript
    evidence_material:
      - the two approved passages and their immediate contexts
  - id: LP-AD-03
    job: compare wording without treating one English rendering as proof
    placement: evidence section 2
    learner_action: compare two approved translations and surrounding context
    feedback: reveal the material wording difference and its limits
    accessible_fallback: stacked comparison table with version labels
    evidence_material:
      - approved translation text and sourced lexical/context notes
```

For each pattern, specify:

1. the learning job;
2. where it appears;
3. what the learner does;
4. what feedback or payoff follows;
5. the non-JavaScript or assistive-technology equivalent when interactive;
6. the evidence or source material it uses.

If one of these is missing, the pattern is not implementation-ready.

## Selection constraints

- **Scripture is not a game score.** Never grade belief, use a doctrine answer as a lock, or imply spiritual worth from performance.
- **Core truth stays available.** Interaction may deepen or personalize the route; it may not conceal the primary answer, passage, citation, or interpretive boundary.
- **Observation before evaluation.** Prefer “What changes between these two verses?” to “Which doctrine is correct?”
- **Choice without labeling.** Offer equivalent text, audio, visual, or interactive forms when useful. Do not assign a person a fixed “visual,” “auditory,” or other learning-style identity.
- **Age is not ability.** Adapt sentence length, motor demand, pacing, and prior knowledge. Do not make adult novice content childish or assume an older learner needs less accessibility.
- **One variable at a time.** In interactive comparisons or manipulatives, change one meaningful dimension when possible so the result can be understood.
- **Feedback explains.** A color, confetti burst, check mark, or “try again” alone is not teaching feedback.
- **Progress is orientation.** Use calm progress cues and distributed payoffs; do not create streak anxiety, loss aversion, or false urgency.
- **Theological boundaries remain explicit.** Clearly distinguish text, context, interpretation, application, and uncertainty in every pattern.

## Adaptation by channel

| Channel | Pattern implementation |
| --- | --- |
| Static Markdown or document | use predictions as pause prompts, comparisons as tables, hints as graduated callouts, and details as clearly labeled appendices |
| Semantic HTML page | keep the complete evidence path in HTML; enhance with controls, state, feedback, and optional depth |
| Video | make the learner action a pause-and-notice prompt; provide the reveal and explanation on screen and in the script |
| Live or small group | let learners predict privately, discuss observations, then inspect the passage together; avoid public performance pressure |
| Social post or short | use one micro-pattern only, usually familiar anchor, compare-and-notice, or retrieval; link to the full evidence path |

## Review test

A substantive journey passes its pattern review only when:

- 3–5 appropriate patterns from at least two families are named;
- every pattern performs a different or clearly supporting learning job;
- the sequence contains explanation, participation, payoff, and learner agency without becoming formulaic;
- no interaction tests belief, withholds truth, or rewards mere clicking;
- dynamic states have equivalent text and keyboard behavior;
- the pattern plan respects translation rights, citations, context, and interpretive limits;
- the pattern mix fits this question rather than copying the previous journey.
