# Standards Governance

Use this file only when creating or changing the reusable `modern-html-css-aeo` standard, its validators, syncing, fixtures, or release process.

## Responsibility boundary

- Keep `modern-html-css-aeo` universal across Scripture, health, client, landing-page, dashboard, and other web projects.
- Keep Scripture doctrine/content mechanics in the Scripture lane.
- Keep YouTube implementation in the YouTube lane.
- Share the cross-channel experience constitution and visual/learning principles without copying every channel-specific rule into the web standard.

## Standard build order

Do not package a release before completing:

1. architecture and routers;
2. mandatory planning and approval gates;
3. visual-direction, typography, color, composition, inspiration, and anti-repetition systems;
4. progressive JavaScript and correct motion policy;
5. technical, planning, and experience validators;
6. compatibility and rollback architecture;
7. tests against real benchmark projects.

## Versioning

Use `MAJOR.MINOR.BUILD` plus stable rule IDs.

- **BUILD:** corrections, implementation fixes, or non-normative clarification; cannot add a new `MUST`.
- **MINOR:** backward-compatible capabilities or requirements; must pass compatibility testing.
- **MAJOR:** deleted rules, changed meaning, breaking architecture, migrations, or incompatible validator changes; never auto-adopt.

Represent normative rules in a machine-readable registry, for example:

```json
{
  "id": "WEB.JS.PROGRESSIVE.001",
  "since": "3.2.0",
  "level": "MUST",
  "breaking": false
}
```

## Release manifest

Each release must declare:

```json
{
  "version": "3.2.0",
  "breaking": false,
  "migrationRequired": false,
  "changedRuleIds": [],
  "addedRuleIds": [],
  "removedRuleIds": [],
  "validatorChanges": [],
  "affectedAreas": []
}
```

Determine compatibility from the version, rule diff, manifest, validator changes, and an actual project test. Never trust the label alone.

## Project synchronization

- Do not use Git submodules as the living-standard mechanism.
- Keep a project config naming the source/channel, accepted major, update behavior, and compatibility requirement.
- Sync the candidate standard into a managed local cache at task start.
- Compare the candidate manifest and rule diff, run compatibility tests against the project, and adopt only on pass.
- On a minor/build failure, return to the last-known-good standard and produce a compatibility report.
- On a major change, stop automatic adoption and produce a migration report.

## Benchmark fixtures

Use real pages to test the standard without turning them into templates:

- a technically compliant but visually generic page;
- a more refined page with typography, imagery, and progressive interaction;
- additional projects representing materially different content and architecture.

Regression testing must cover semantic HTML, accessibility, progressive enhancement, performance hazards, metadata/schema, BEM/project conventions, planning status, visual-direction presence, and experience review.

## Release principle

Technical correctness is the floor. Release only when the standard can guide agents from a good idea through approved content and visual direction into a semantic, accessible, fast, discoverable, interactive, varied, and rewarding experience.

