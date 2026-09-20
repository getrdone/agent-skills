# evals — router harness

<!-- Agent: claude · Model: claude-opus-5 · Thinking: not exposed · Date: 2026-09-10 -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Updated fixture inventory after adding palette-routing coverage. -->

Does the right skill answer, and does it open only the files it should?

| File | Role |
|------|------|
| `router-fixtures.yaml` | 27 fixture prompts with expected skill, lanes, loads, forbidden loads, and advisory load sizes |
| `check_load.py` | Scores a captured run against a fixture. No dependencies; uses PyYAML if present, falls back to a small parser if not |
| `../_wip/eval-captures/` | Where you save what an agent printed. Gitignored except this note |

## How to run

Agents are not scriptable from here, so this is **manual capture, automatic checking**. Pretending
otherwise would make the harness a lie about what it measures.

```bash
python evals/check_load.py --list                    # see the fixtures
# paste one fixture's prompt into an agent
# copy the LANES / LOAD block it emits into _wip/eval-captures/<fixture-id>.txt
python evals/check_load.py --all
```

A capture only needs the declaration block somewhere in it:

```text
SKILL: curiosity-driven-scripture-journey
LANES: web.repair
LOAD:  references/web-experience.md
BRIEF: daniel-8/project-brief.md  (stage: approved-for-build)
```

## Verdicts

`PASS` · `MISSING` (required path or lane absent) · `EXTRA` (forbidden path loaded) ·
`WRONG-SKILL`.

## What this does not measure

Routing only. It says nothing about whether the titles were good or the page was beautiful —
that is what `quality-gates.md` is for. Two fixtures carry an `assert_behaviour` note you check
by eye; everything else is mechanical.

## Evidence

Save captures and comparison results in `_wip/eval-captures/`. Advisory load sizes never fail a run: load the material needed to finish the authorized request. Routing evidence supplements substantive verification.
