"""Install current startup guidance directly; no legacy launchers. Codex GPT-6, 2026-09-20."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,shutil
import library

ROOT=Path(__file__).resolve().parents[1]
START='<!-- BEGIN AUTHORITATIVE SKILLS -->';END='<!-- END AUTHORITATIVE SKILLS -->'
def context(root):
 return f'''# Authoritative skills

Library: `{root.as_posix()}`. Installed copies are generated. Payload: `C:/Users/noise/.agents/skill-library` (`current.json`).

Default voice: lean-output and i-have-adhd. Talk to a person. No inner-agent chatter. No jargon walls.

Video Library is a default for all specifically requested videos: resolve `skills/video-library/CURRENT`, record the request once before retrieval, and increment the existing video counter for each new request. Web/cloud sessions without local access must send a verified handoff to local ChatGPT Work/Codex through available messaging tools, or clearly provide an unsent pending handoff if no route exists. This is an explicit exception to named-only specialist loading.

When a specialist is needed, read CATALOG.md for the name, then load that skill's CURRENT file. Follow only that release. Do not load the rest until named. Never mix releases. Never load retired names (html-page-standard, studio-web, modern-html-aeo, modern-css-design, interactive-components, optimized-deliverables) — use web-studio.

Project memory is on disk, not chat: 01-NOW.md every session; 02-TASKS.md for the queue; 03-MEMORY.md before changing anything that looks decided; image-slots.md before any image path or generate/promote. Graphics does not edit HTML. Code does not invent image paths.

Drafts go in project `_wip/<task>/`. Reusable tools go in `_tools/` after checking `{(root/'_tools/TOOLS.md').as_posix()}`.
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
