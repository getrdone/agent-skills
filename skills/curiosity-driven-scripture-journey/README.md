# curiosity-driven-scripture-journey

Canonical home: **https://github.com/getrdone/agent-skills**  
Path: `skills/curiosity-driven-scripture-journey/`

Plan, package, design, write, build, or review Scripture content projects: topic discovery, Bible-study journeys, YouTube titles and packaging, visuals, and web experiences.

## Load
1. Repo root `CATALOG.md` matched this skill.
2. Read `SKILL.md` — it is a version router. Resolve `CURRENT` (or `STABLE`, or a named version).
3. Read `versions/<resolved>/SKILL.md`. **Every relative path in it resolves under `versions/<resolved>/`.**
4. Load only the files that version's `load-map.yaml` lists for the matched lanes.

## Related processing
Source-vault inventory / registration helpers live under:

`processing/source-vault/`

Consumer projects keep their own `sources/registry.yaml` and library files; this skill + processing package define the rules and tooling.
