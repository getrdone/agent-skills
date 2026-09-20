# Release and recovery operations

Use Python 3.11+ and the standard-library-only _tools/library.py. On this machine the bundled runtime is C:/Users/noise/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe.

1. Backup: `python _tools/library.py backup <source> <new-snapshot-directory>`. Includes hidden/ignored files and Git state. Source is never modified. Keep credentials and private configuration in local-only snapshots.
2. Restore rehearsal: `python _tools/library.py restore <snapshot> <empty-directory>`. Select a file with `--file <relative-path>`. The command refuses to overwrite a populated directory; links are reported for explicit reconstruction.
3. Create a new immutable release folder. Preserve the current release. Update selectors and release-index.json. Resolve all current references directly within the library and keep attribution.
4. Run `python _tools/library.py seal`, then `validate`. Seal refuses changes to an already sealed release. Changes to tools and shared files require resealing the repository manifest.
5. Inspect `sync --dry-run`; then run `sync`. It first validates every release and builds a complete payload outside native discovery roots. Only then are complete entrypoints atomically published. Backups precede every managed replacement/removal. System and unrelated skills are untouched.
6. Git updates are explicit and separate. `git-update <repo>` refuses dirty/diverged checkouts and only fast-forwards. Publish reviewed changes using explicit paths; never force-push or stage unrelated work.

All configured homes and generated installation hashes are recorded under the configured state directory. .codex managed duplicates are retired in favor of .agents discovery; .system remains untouched. Previous generated payloads are retained for rollback. Rollback chooses a retained generation or release explicitly and performs the same verified sync; do not run archived scripts as startup hooks.

The Windows scheduled task runs the canonical _tools/sync-hidden.vbs directly. Its launcher resolves the bundled Python runtime or the machine-local SKILL_PYTHON environment variable. No legacy launchers are required. The task has no execution time limit, retains IgnoreNew overlap behavior and runs hidden. Startup hooks read current selectors rather than pinning CDSJ versions.

For scheduled-run diagnostics, inspect `last-run.json` and `logs/sync-latest.log` in the configured installation state directory. They record the exit status and command output even when the launcher is hidden. Task Scheduler also receives the same exit status. `last-sync.json` describes the last successful reconciliation; a later failed attempt must not be mistaken for that success.
