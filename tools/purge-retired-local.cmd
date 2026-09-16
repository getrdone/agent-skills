@echo off
set DOIT=%1
for %%H in ("%USERPROFILE%\.grok\skills" "%USERPROFILE%\.grok\skills-from-repo\skills" "F:\__ai-projects\agent-skills\skills") do (
  for %%N in (html-page-standard studio-web interactive-components modern-css-design modern-html-aeo optimized-deliverables modern-web-development modern-web-development-v2) do (
    if exist "%%~H\%%N" (
      echo FOUND %%~H\%%N
      if /I "%DOIT%"=="1" rd /s /q "%%~H\%%N"
    )
  )
)
if /I not "%DOIT%"=="1" echo Dry run. Re-run: purge-retired-local.cmd 1
