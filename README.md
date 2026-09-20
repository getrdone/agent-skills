# Authoritative agent skill library

This repository contains the complete managed skill instructions and resources. Installed copies are generated distributions. No legacy aliases, redirect stubs or fallback loading are supported. Historical attribution is provenance, not a required dependency.

Read CATALOG.md to discover capabilities; load only task-relevant skills and references. For coding, use coding-workflow. For web work, use web-studio and the accepted project design specification. File placement and working conventions are in WORKSPACE.md. Search _tools/TOOLS.md before creating a utility.

Each skill has CURRENT/STABLE selectors and immutable releases. Root SKILL.md selects a release; installed entrypoints contain the selected release instructions. Historical releases are explicitly selectable and excluded from discovery. Release manifests contain all file hashes. tools do not silently mix versions.

Temporary work belongs in project _wip; reusable utilities belong in project _tools. Complete broad requests through verifiable chunks without duration quotas, inactivity deadlines or automatic job termination. Modular files and suitable animation libraries are available.

## Maintenance

Run `python _tools/library.py validate` before release, then `python _tools/library.py sync --config _tools/agent-homes.json`. Sync verifies the release manifest, preserves divergent installed files, and updates only manifest-owned files. Use --dry-run to inspect changes. Git updates are separate: `python _tools/library.py git-update <repository>` fast-forwards a clean checkout only. No reset, force-push or automatic model switching.

Recovery copies live in the separate private zzz-repo-archive repository; they are never consulted during normal skill use. Migration coverage and release evidence are in _docs. Operational SQLite memory is a desired next project to evaluate; it is not implemented here.
