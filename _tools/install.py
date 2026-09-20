"""Install current startup guidance directly; no legacy launchers. Codex GPT-6, 2026-09-20."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,shutil
import library

ROOT=Path(__file__).resolve().parents[1]
START='<!-- BEGIN AUTHORITATIVE SKILLS -->';END='<!-- END AUTHORITATIVE SKILLS -->'
def context(root):
 return f'''# Authoritative skills and working conventions

The complete managed skill library is `{root.as_posix()}`. Read its CATALOG.md to discover skills and its WORKSPACE.md for working conventions. Installed skills are generated distributions; do not use old aliases, redirect files, archived guidance or upstream files as missing instruction dependencies.

Coding work uses coding-workflow. Web implementation uses web-studio and accepted project design decisions. Load relevant specialists progressively without a numerical cap. Resolve CURRENT/STABLE or an explicitly requested release dynamically; never mix releases.

Use project `_wip/<task>/` for drafts, temporary plans, diagnostic captures and intermediate artifacts. Use project `_tools/` for reusable utilities. Keep established source, tests, assets, accepted documentation and deliverables in their proper locations. Consult `{(root/'_tools/TOOLS.md').as_posix()}` before writing a tool; project tool indexes link directly to that master.

Complete the full authorized request through cohesive verifiable chunks: outcome, affected area, check, evidence, status and next action. No 2–5-minute requirements, inactivity deadlines, time-based job kills, automatic retries, silent model changes or repeated approval gates. Long operations remain responsive; honor explicit stop requests and actual failures.

Preserve a suitable stack. Modular source, dependencies, Motion/Framer Motion, GSAP, Remotion and Lottie are allowed when appropriate. Self-contained delivery is an explicit export request. Project identity and accessibility govern design choices; illustrative examples are not mandatory styles.
'''
def install(user,backup_root):
 user=Path(user);backup_root=Path(backup_root);records=[]
 def write(p,body):
  p=Path(p);before=p.read_text(encoding='utf-8-sig') if p.exists() else ''
  if START in before:
   begin=before.index(START);finish=before.index(END,begin)+len(END);after=before[:begin]+START+'\n'+body+'\n'+END+before[finish:]
  else:after=before.rstrip()+'\n\n'+START+'\n'+body+'\n'+END+'\n'
  if after==before:return
  if p.exists():
   backup=backup_root/p.relative_to(user);backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,backup)
   if library.sha(backup)!=library.sha(p):raise RuntimeError('Startup backup mismatch')
  p.parent.mkdir(parents=True,exist_ok=True);p.write_text(after,encoding='utf-8')
  records.append({'path':str(p),'sha256':library.sha(p)})
 body=context(ROOT)
 for rel in ['.codex/AGENTS.md','.grok/rules/authoritative-skills.md','.claude/CLAUDE.md','.freebuff/AGENTS.md','.openclaw/AGENTS.md','.gemini/GEMINI.md']:
  write(user/rel,body)
 cursor=user/'.cursor/rules/authoritative-skills.mdc'
 if not cursor.exists():cursor.parent.mkdir(parents=True,exist_ok=True);cursor.write_text('---\ndescription: Authoritative managed skills and workspace conventions\nalwaysApply: true\n---\n')
 write(cursor,body)
 # Native global Grok hook is supported independently of project trust.
 hook=user/'.grok/hooks/authoritative-skills.json';data={'hooks':{'SessionStart':[{'hooks':[{'type':'command','command':'powershell.exe -NoProfile -ExecutionPolicy Bypass -File "'+str(ROOT/'_tools/startup-context.ps1')+'"'}]}]}}
 if hook.exists():
  dest=backup_root/hook.relative_to(user);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(hook,dest)
 library.save(hook,data);records.append({'path':str(hook),'sha256':library.sha(hook)})
 library.save(backup_root/'installation.json',records);print(json.dumps({'startup_files':len(records),'backup':str(backup_root)},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--user',default=os.environ.get('USERPROFILE',str(Path.home())));p.add_argument('--backup',required=True);a=p.parse_args();install(a.user,a.backup)
