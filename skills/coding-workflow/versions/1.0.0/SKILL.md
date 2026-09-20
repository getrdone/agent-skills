---
name: coding-workflow
description: Plan, implement, debug, and verify coding work in reviewable chunks; reuse existing capabilities and preserve the full requested outcome.
---

# Coding workflow

## Understand and decide
Read the request, relevant project decisions, and actual implementation. Define observable success. Inspect callers and data flow before choosing a fix. Surface consequential ambiguity; resolve routine implementation details autonomously. Brainstorm before major architecture, structure, visual-direction, or interaction changes, proportionate to their impact.

## Simplify without reducing the request
Check, in order: whether the work is required; existing project code and tools; standard libraries; native platform capabilities; installed dependencies; suitable new libraries; focused custom code. Choose the simplest option that meets functional, visual, accessibility, and maintenance requirements. The fewest lines or files are not the goal. Never drop requested features, necessary validation, data-loss handling, security, or accessibility to simplify.

Add complexity when it delivers required value. Reuse existing capabilities, avoid duplicated authority, remove duplication introduced by your change, and explain material maintenance costs. Inspect the master tool catalog before creating a utility.

## Implement through verifiable chunks
Each chunk records outcome, affected area, verification, evidence, status, and next action. Choose a cohesive independently assessable result, not a duration. A broad authorized request continues through every required chunk. A narrow fix stays narrow. No universal TDD, mandatory delegation, mandatory commit frequency, or repeated approval gates. Add regression tests for meaningful behavior or risk; use direct inspection for low-impact edits.

There are no 2–5-minute runs, inactivity deadlines, or time-based kill rules. Keep long operations responsive with supported background execution and evidence-based updates. Silence and process liveness do not establish failure or success. Investigate actual failures; do not automatically restart jobs or change models/effort. Honor explicit stop requests and resource problems.

## Debug and verify
Reproduce or gather evidence, trace the cause, compare a working path, test one explanation, and apply the focused fix. A requested full-page polish can justify changes across the page; unrelated changes cannot. Verify behavior and appearance where relevant against the original request. Record check results and untested limitations. Do not infer completion from an exit code or a live process alone.

## Source adaptations
Karpathy: thinking, simplicity, surgical scope, goal-driven verification. Ponytail: inspect-and-reuse ladder, without code-golf or reduced scope. Superpowers: consequential decisions, cohesive tasks, root-cause debugging, evidence before completion, without its mandatory lifecycle or timed steps. See PROVENANCE.md for pinned sources and licenses; these sources are attribution, not required reading.

<!-- Agent: Codex | Model: GPT-6 | Thinking: not exposed | Date: 2026-09-20 -->
