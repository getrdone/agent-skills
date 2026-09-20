# Local dev servers (wrangler Pages) — consult only

**Agent:** freebuff · **Model:** z-ai/glm-5.3-flash · **Thinking:** not exposed · **Date:** 2026-09-17

This is not a lane. Any agent starting, restarting, or "fixing" a local preview server for a
Cloudflare Pages project (`npx wrangler pages dev …`) follows this file. Written after ~1 hour was
lost going back and forth on a "broken page" whose actual problem was the server layer.

---

## The failure signature (recognize it in 30 seconds, not 45 minutes)

A local wrangler server is in the **zombie state** when ALL of these hold:

- `netstat -ano | grep :<port>` shows one or more `LISTENING` rows for the port, **but**
- `curl -m 8 http://127.0.0.1:<port>/` returns `000` (connection accepted then dropped / no response), and
- the wrangler log files show no fresh request lines.

This means the wrangler parent (node) is dead or wedged while orphaned `workerd.exe` children — and
sometimes stale socket state — still hold the port. **It is a server problem. Do not debug the page
code, do not read the HTML, do not hunt for CSS/JS bugs.** A page cannot be broken-or-fixed while the
server answers nothing.

Second signature, easy to miss: killing the `LISTENING` PIDs and the `workerd.exe` processes **does
not clear the port** — listeners respawn with new PIDs. That means a live wrangler/node parent is
still running and re-spawning workers. You must kill the parent tree, not the children.

---

## Recovery procedure — the ONLY path (do not improvise around it)

Run these in order; do not skip the verification steps.

1. **Kill everything wrangler-related by command line, not by port.**
   ```powershell
   powershell -NoProfile -Command 'Get-CimInstance Win32_Process |
     Where-Object { $_.CommandLine -match "wrangler" } |
     ForEach-Object { taskkill /F /PID $_.ProcessId }'
   taskkill //F //IM workerd.exe
   ```
   Note: `taskkill //F //IM node.exe` is **banned** — it kills unrelated node processes.
   Killing by port PID alone is insufficient (respawn trap above). Killing by command-line match
   catches the parent node + cmd + bash wrappers in one pass.

2. **Verify the port is actually clear before starting anything.**
   ```bash
   netstat -ano | grep ":<port> " | grep LISTENING   # must print NOTHING
   tasklist | grep -iE "workerd"                      # must print NOTHING
   ```
   If listeners reappear, repeat step 1 — a parent is still alive.

3. **Start exactly ONE instance, detached, with log redirection** (never foreground — AGENTS.md §8).
   ```bash
   cd <project>/versions/<current> && (npx wrangler pages dev public --port <port> --ip 127.0.0.1 \
     > <hub>/wrangler-<port>.log 2> <hub>/wrangler-<port>.err.log &)
   ```
   Log naming is fixed: `wrangler-<port>.log` / `wrangler-<port>.err.log` at the hub root. One stack
   per port. The version folder's README documents the port — use it, don't invent one.

4. **Wait ~20 s, then verify with curl, not with a browser.**
   ```bash
   curl -s -m 8 -o /dev/null -w "%{http_code}\n" http://127.0.0.1:<port>/          # expect 200
   curl -s -m 8 http://127.0.0.1:<port>/ | grep -o 'fd-page-version" content="[^"]*'
   ```
   The `fd-page-version` grep proves you are serving the version folder you think you are. Report
   the URL + version to the user only after both checks pass.

---

## Standing rules

- **After any session/PC restart, wrangler is dead.** Before starting new work: kill strays (step 1),
  verify ports, then start fresh. Never assume an old instance survived. (`01-NOW.md` and AGENTS.md §8
  both say this — this file is the procedure.)
- **Time-box: 10 minutes.** If a local server is not healthy after ~10 minutes of incremental fixes,
  stop debugging and run the full recovery procedure from step 1. Zombie debugging has no middle
  ground — a clean sweep always beats another probe.
- **A user report of "the page doesn't work" on a local URL gets a server health check FIRST**
  (step 4's curl) before any code is read. The 2026-09-17 hour was lost reading page code while the
  server answered nothing.
- **One heavy job / one stack per port.** Two wrangler instances fighting over one port is the
  classic cause of the zombie state. Check the hub's `01-NOW.md` for the currently assigned port.

(Real case: 2026-09-17, Final Days landing page v10.11.2 — 5 zombie listener PIDs on :8822/:8820,
curl 000, an hour of page debugging produced nothing; kill-by-commandline + one fresh detached
instance + curl verify fixed it in under a minute. `__Final.Days.International/01-NOW.md`.)
