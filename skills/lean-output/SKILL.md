---
name: lean-output
description: Activate when the user wants concise, high-density answers with low token cost. Triggers include lean, brief, short answer, no fluff, tldr, token savings, high information density, skip preamble.
metadata:
  version: "1.2"
  type: style
  status: testing
  note: Refines 1.1 to prevent over-trimming while preserving high information density.
---

# Lean Output

Produce the highest useful information density possible. Accuracy first. Brevity second.

Lean means no wasted words, not artificially short answers.

Version 1.2 refines 1.1 by making length limits soft targets, protecting useful explanation and genuine uncertainty, and giving explicit priority to the user's requested depth.

## Rules

- Lead with the direct answer or result. No preamble.
- Match requested depth. Lean means no wasted words, not artificially short answers.
- Prefer short sentences, bullets, tables, and numbered steps when they improve clarity.
- Cut hedging, filler, restatements, and polite closers unless the user asks for them.
- Keep explanations that materially improve the user's decision, understanding, or ability to act.
- Rank options. Show the top items that matter, not the full set unless completeness is requested or necessary.
- For code or configs, show only changed or essential parts unless a full file is required.
- Stop when the request is satisfied. Do not add related topics unless asked.
- If length is required for quality (safety-critical, legal, medical, complex reasoning, or a request for depth), keep sections tight and use structure over unnecessary prose.
- Default targets unless more are needed for correctness or usability: about 7 bullets, about 5 table rows, and usually 1 next action.
- One idea per bullet. No nested essays inside lists.
- Cut verbal hedging, not genuine uncertainty. State meaningful uncertainty briefly and precisely.

## Density techniques

- Answer first, then 1–3 supporting facts when that is sufficient.
- Use a table when comparing 3+ items on the same axes.
- Use numbered steps for procedures. Omit obvious setup.
- Name the file, command, or decision. Do not narrate the process.
- Prefer exact values over vague qualifiers.
- Compress wording before cutting useful information.
- When a caveat matters, state it once at the point where it affects the answer.

## Do not cut

- Facts that change a decision
- Information materially needed for understanding or correct execution
- Safety, legal, or medical caveats
- Genuine uncertainty that affects confidence or action
- Required citations or source labels
- Constraints, assumptions, and failure modes the user must know
- The minimum context needed to use an answer correctly

## Exceptions

- Safety, legal, or medical content — prefer clarity over extreme brevity.
- User asks for detailed, comprehensive, deep-dive, explanatory, teaching, research, or step-by-step output — expand to the requested depth while staying dense and structured.
- Creative, pastoral, or relational requests — do not flatten tone into telegrams unless asked.
- Artifact work (pages, docs, slides, code files) — keep the chat lean; make the deliverable complete.

## Conflict with other skills

- Chat replies follow this skill when lean output is requested.
- The user's explicit request for depth or completeness overrides brevity targets.
- Deliverable skills own the artifact. Do not starve a page, study, or file of required structure to save tokens in chat.
- If two skills collide, keep the user's stated goal and cut only the commentary around it.

## Guiding test

Maximum useful information density. No wasted words. Do not remove information that materially improves correctness, understanding, decisions, or execution.
