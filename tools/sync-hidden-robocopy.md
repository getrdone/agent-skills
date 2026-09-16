# Hidden robocopy sync (no PowerShell window)

Keep a git clone of this repo. Pull when you want GitHub changes. Robocopy that clone into each agent home.

Do not schedule `powershell.exe`. Call `C:\Windows\System32\robocopy.exe` from Task Scheduler with Hidden=true.

Example arguments:

```
F:\__ai-projects\agent-skills  %USERPROFILE%\.grok\skills-from-repo  /E /XO /XD .git  /NFL /NDL /NJH /NJS /NP /R:1 /W:1
```

Avoid `/MIR` until the destination is only a mirror.

Purge retired local folders if they still exist: html-page-standard, studio-web, interactive-components, modern-css-design, modern-html-aeo, optimized-deliverables, modern-web-development.

Page work is `skills/web-studio/` only.
