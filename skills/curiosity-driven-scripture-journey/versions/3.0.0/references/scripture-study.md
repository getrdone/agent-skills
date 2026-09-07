# Scripture Journey Content

<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-08-21 -->

Use this file for Bible-study questions, Scripture Journey Pages, evidence plans, interactions, pathways, and Scripture-specific review.

## Constitution

- Center one sincere Bible question.
- Let Scripture and context lead; do not begin with a conclusion and hunt for proof-texts.
- Reward the curiosity that brought the learner to the page.
- Deliver the promised answer with the available evidence.
- Preserve learner dignity and freedom. No fear, guilt, pressure, scoring, shame, or implied teacher superiority.
- Distinguish what the text says, what an interpretation proposes, what an application suggests, and what remains uncertain.
- Treat growth metrics as diagnostic signals, never as permission to weaken truth or manipulate attention.

## Topic and content plan

When generating **topic ideas**, **verse-study ideas**, or **titles** for a Scripture asset, use the mandatory **17-category × 4** matrix in `references/youtube-planning.md` (same categories as YouTube Video Planner v1.1.1). Do not substitute a short freeform list.



Before substantial production, define:

- core curiosity question;
- target adult reader and likely prior understanding;
- why the question genuinely matters;
- precise promised payoff;
- primary and supporting passages in context;
- source/translation requirements;
- pinned source-library snapshot, applicable approved source records, and claim-level alignment plan;
- strongest early evidence;
- payoff ladder;
- honest surprise or unexpected connection;
- known anchor → scaffolding → new insight;
- 3–5 selected learning-pattern IDs from at least two families, with a distinct job, placement, feedback/payoff, and accessible fallback for each;
- visual evidence opportunities;
- reflection moment;
- interaction opportunities;
- featured direct continuation;
- two additional direct continuations, one moderately related question, and one wildcard;
- claims or interpretations that require qualification.

Reject or revise a topic when the promised payoff is unavailable, the evidence plan is too weak, or the only appeal depends on fear, sensationalism, or withheld answers.

## Content sequence

Adapt length to the requested experience, but preserve this logic:

1. **Promise confirmation:** plainly name the question and what will be examined.
2. **Familiar anchor:** begin from a verse, fact, or lived question the learner can recognize.
3. **First evidence payoff:** provide meaningful evidence early; do not spend the opening on setup.
4. **Progressive evidence:** add one distinct piece at a time, with just-in-time context.
5. **Interaction/reflection:** invite a comparison, observation, choice, or pause that aids understanding without testing worth.
6. **Primary answer:** state what the evidence supports in plain language.
7. **Boundaries:** identify remaining interpretation or uncertainty when relevant.
8. **Next curiosity:** offer one featured direct continuation and four alternates when continuation exists.

## Interaction rules

- Use `learning-patterns.md` to select the pattern mix; load only the selected family files. A substantive journey normally uses 3–5 patterns from at least two families, not one repeated interaction.
- Study truth, citations, and the primary answer live in the HTML document.
- Interactions (verse focus, translation compare, ordering games, scroll progress, map trails, branching) **may use JavaScript**—build and browser-verify the full interactive design. Do not strip JS to pass a purity checklist.
- Do not make the learner guess a doctrine to unlock the answer.
- When using multiple choice, make it observational or reflective rather than graded. Give kind, immediate feedback.
- A progress bar may show orientation, but avoid school-like “Step 1 of 6” language when a quieter progress cue works.
- Optional interactions should deepen learning; the core answer must still be readable in the page source.
- Dynamic state must also be available through text, keyboard behavior, and assistive-technology announcements. A visual or auditory effect alone is not feedback.

## Reading and theological integrity

- For **teaching body copy**, aim for 3rd–5th-grade readability without sounding childish; keep sentences short and define larger terms immediately. Spell out “verses 8–11.” This does **not** restrict titles, hooks, or specialized creative/copywriting skills used alongside the study.
- Quote accurately and identify the exact translation and edition.
- Do not silently choose, prescribe, rewrite, harmonize, or paraphrase a Bible translation. Translation selection is passage-specific unless the user explicitly approves one version for a defined larger scope. The user may choose KJV for one passage, NLT for the next, AMP for another, or one version throughout.
- Preserve surrounding context and genre; do not splice verses to manufacture a claim.
- Do not treat present-day theological consensus, denominational popularity, institutional acceptance, or the number of adherents as evidence that a view is biblically true.
- Use calm, confident language; avoid “proves,” “obviously,” or adversarial “I’m right/you’re wrong” framing unless the evidence truly requires a firm factual correction.

## Research authority and source order

Load `resources-and-authority.md` for SME order, links, vault paths, tools, and **plain-language scope** (teaching vs creative packaging).
Load `source-governance.md` for the cross-repository workflow, SQLite query rules, conflict handling, and alignment manifest.


Use this order without treating later sources as replacements for earlier evidence:

1. **Scripture compared with Scripture:** begin with the passage in its immediate context, then compare the wider witness of Scripture. Respect genre, speaker, audience, time, covenant setting, repeated language, and the Bible’s complete teaching. Do not build doctrine from an isolated phrase.
2. **Hebrew, Aramaic, and Greek textual work:** when material to the question, examine sourced lexical range, grammar, syntax, verb forms, tense/aspect, textual variants, and translation choices. Context selects among possible meanings; a dictionary possibility is not automatically the meaning in the verse.
3. **Reformation and named Reformer witnesses:** identify the writer, work, date, passage, and doctrinal setting. Preserve real differences among Reformers.
4. **Early Adventist pioneer witnesses:** use named pioneers and primary documents with dates and historical settings. Preserve development and disagreement.
5. **Approved trusted sources:** use the project’s registered teachers, organizations, studies, and research collection with provenance and attribution.
6. **Contemporary theological material, when useful:** use it to document a named view, answer an alternative reading, or support linguistic, archaeological, bibliographic, or historical research—not to establish truth by majority or modern consensus.

Every commentary, Reformer, pioneer, teacher, lexicon, grammar, and trusted source remains subordinate to Scripture and must be tested against the biblical text. Prefer primary sources and direct documents. Name traditions and writers precisely; never invent a source, page, date, quotation, position, agreement, or translation wording.

Lexical, historical, cultural, ancient-practice, translation, doctrinal, quotation, and external factual claims require traceable sources. Put a citation beside the claim it supports and add a complete record to the end references. Label inference, reconstruction, interpretation, deduction, and practical likelihood rather than presenting them as established facts. Preserve internal provenance even when the public study remains Scripture-first.

## Translation review

For every translation used, record the exact version/edition, provider, rights or public-domain status, required attribution, and whether full text, limited quotation, or only an outbound link is allowed.

Every cited verse or passage must have a human review opportunity before public wording is locked. Default the review display to **KJV first**, followed by **NLT, CSB, WEB, and NASB at minimum**. Additional useful versions may include AMP, ESV, DBY, NKJV, ASV, RSV, HNV, YLT, and BBE. This order is a review default, not a prescribed publication choice.

Record the selection separately for each cited unit, for example:

```yaml
passage_translation_selections:
  Psalm 23:1: KJV
  Psalm 23:2-3: NLT
  Psalm 23:4: AMP
```

Allow one explicit action to apply a selected version throughout a defined document or project, but never infer that choice from the first approved verse. A public page shows only the wording approved for each passage and permitted by the relevant translation terms.

Notice when wording changes the apparent meaning. Compare the underlying terms and context before building an explanation on one English rendering. Do not automatically replace biblical “fear” with “reverence”; show the selected wording, then explain the sourced semantic range and context when material. Verify ambiguous spoken references with the user before encoding or citing them.

An internal verse comparison may open an optional accessible panel: KJV first; NLT, CSB, WEB, and NASB next; additional versions on request; and version labels always visible. Highlight wording differences only as comparison aids, never as proof. The reviewer must be able to approve the version for that passage, change it later, or apply one version throughout an explicitly defined scope. Authorized external tools such as Blue Letter Bible may supplement manual research; do not install an unverified scraper or community integration.

## Evidence trail by channel

- **Scripture Journey web page:** place inline citations beside supported claims. Add compact semantic end matter, using `<details>` and `<summary>` where appropriate, for Bible passages/translations, references, further reading, and external links. Keep the core answer and evidence in semantic HTML. End matter must work with keyboard and screen reader; premium CSS/JS on the journey chrome is expected.
- **Markdown/planning:** use footnotes or short markers where helpful and end with `References`. Separate Scripture, original-language tools, Reformation, early Adventist pioneers, approved trusted sources, other historical material, contemporary commentary, and creative inspiration when mixing them could blur authority.
- **Video:** show a short readable reference when a quotation, document, historical claim, or key evidence appears. Preserve the full reference in the script/research record and description.
- **YouTube description:** keep the concise main description, then add a labeled source block for Bible passages/translations, quoted documents, historical sources, further study, rights notices, and attribution. The bibliography does not count toward the main prose word target.

## Next-path architecture

When the study should continue, provide:

1. **Featured direct continuation:** the most natural next question in the same thread.
2. **Direct continuation:** another next question in the same thread.
3. **Direct continuation:** a third useful same-thread route.
4. **Moderately related:** a looser but meaningful connection.
5. **Wildcard:** a genuinely different Bible subject that offers an exit ramp and signals range.

Suggested internal shape:

```yaml
featured_next_path:
alternate_paths:
  - relationship: direct
  - relationship: direct
  - relationship: moderately-related
  - relationship: wildcard
```

Never use “Go Deeper” in customer-facing HTML or Markdown; avoid it internally as well. Vary visible wording, layout, imagery, and metaphor by project while keeping semantic and accessibility behavior consistent.

Present these as obvious sequential links rather than boxed tiles unless the approved visual direction has a strong reason to do otherwise.

## Content completion check

- Can the core question be stated in one sentence?
- Does the opening immediately confirm it?
- Does each section add evidence or clarity?
- Are small payoffs distributed through the journey?
- Is the primary answer explicit rather than implied?
- Are interpretive limits honest?
- Is every material claim supported, qualified, or blocked against the pinned source-library snapshot?
- Are expansions traceably rooted in Scripture, Spirit of Prophecy, or labeled scripturally aligned reasoning?
- Does the next recommended question arise naturally from the answer?
