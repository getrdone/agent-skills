"""Authoritative skill lifecycle. Codex | GPT-6 | thinking not exposed | 2026-09-20.
Standard library only. No subprocess job timeout, automatic retry, reset, or model change.
"""
from pathlib import Path
import argparse,contextlib,datetime,hashlib,json,os,re,shutil,stat,subprocess,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
TEXT={'.md','.yaml','.yml','.json','.txt'}
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,obj):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 tmp=p.with_name(p.name+'.pending');tmp.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');os.replace(tmp,p)
def files(root):
 for base,dirs,names in os.walk(root,followlinks=False):
  for d in list(dirs):
   q=Path(base)/d
   if d in {'.git','_wip','__pycache__'}:dirs.remove(d)
   elif q.is_symlink() or (os.name=='nt' and q.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT):
    raise ValueError('Linked directory must be explicitly inventoried: '+str(q))
  for n in names:
   q=Path(base)/n
   if q.is_symlink():raise ValueError('Linked file must be explicitly inventoried: '+str(q))
   if not n.endswith('.pending'):yield q
def contained(p,base):
 p=Path(p).resolve();base=Path(base).resolve()
 if p==base or not p.is_relative_to(base):raise ValueError('Path escapes intended root: '+str(p))
 return p
def backup(source,destination):
 source=Path(source).resolve();destination=Path(destination).resolve()
 if destination.is_relative_to(source):raise ValueError('Backup destination must be outside source')
 if destination.exists():raise FileExistsError(destination)
 destination.mkdir(parents=True); entries=[];links=[];directories=[]
 with zipfile.ZipFile(destination/'snapshot.zip','w',zipfile.ZIP_DEFLATED,compresslevel=3) as z:
  for base,dirs,names in os.walk(source,followlinks=False):
   for d in list(dirs):
    p=Path(base)/d
    if p.is_symlink() or (os.name=='nt' and p.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT):
     links.append({'path':str(p.relative_to(source)),'target':os.readlink(p)});dirs.remove(d)
    else:directories.append(str(p.relative_to(source)))
   for n in names:
    p=Path(base)/n;before=p.stat();data=p.read_bytes();after=p.stat()
    if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):raise RuntimeError('Source changed during backup: '+str(p))
    name=p.relative_to(source).as_posix();z.writestr(name,data)
    entries.append({'path':name,'size':len(data),'sha256':hashlib.sha256(data).hexdigest(),'mtime_ns':after.st_mtime_ns})
 save(destination/'manifest.json',{'source':str(source),'created':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':entries,'directories':directories,'links':links})
 verify_backup(destination);print('Verified backup:',destination)
def verify_backup(destination):
 destination=Path(destination);m=load(destination/'manifest.json')
 with zipfile.ZipFile(destination/'snapshot.zip') as z:
  if set(z.namelist())!={x['path'] for x in m['files']}:raise ValueError('Unexpected or missing snapshot members')
  for e in m['files']:
   if hashlib.sha256(z.read(e['path'])).hexdigest()!=e['sha256']:raise ValueError('Backup hash mismatch: '+e['path'])
 return m
def restore(snapshot,destination,selected=None):
 snapshot=Path(snapshot);destination=Path(destination).resolve();m=verify_backup(snapshot)
 if destination.exists() and any(destination.iterdir()):raise ValueError('Restore requires an empty destination; never overwrite live work')
 destination.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(snapshot/'snapshot.zip') as z:
  matches=[e for e in m['files'] if selected is None or e['path']==selected]
  if not matches:raise ValueError('Selected restore file not found')
  for e in matches:
   p=contained(destination/e['path'],destination);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(e['path']))
   if sha(p)!=e['sha256']:raise RuntimeError('Restore mismatch')
  if selected is None:
   for d in m.get('directories',[]):contained(destination/d,destination).mkdir(parents=True,exist_ok=True)
 save(destination/'RESTORE-RESULT.json',{'verified_files':len(matches),'links_not_recreated':m.get('links',[])})
 print('Restore verified:',len(matches),'files')
def seal(root=ROOT):
 index=load(root/'release-index.json')
 for name,sel in index['skills'].items():
  folder=root/'skills'/name
  for ver in (folder/'versions').iterdir():
   if not ver.is_dir():continue
   content={p.relative_to(ver).as_posix():sha(p) for p in files(ver) if p.name!='manifest.json'}
   path=ver/'manifest.json'
   previous=load(path) if path.exists() else None
   if previous and previous.get('sealed') and previous['files']!=content:raise RuntimeError('Immutable release changed: '+str(ver))
   save(path,{'schema':1,'name':name,'version':ver.name,'sealed':True,'files':content,'dependencies':{'library_release':index['release']},'provenance':'Local authoritative adaptation; source notices and licenses retained.'})
 manifest={p.relative_to(root).as_posix():sha(p) for p in files(root) if p.name!='library-manifest.json' and not p.relative_to(root).as_posix().startswith('_docs/run-')}
 save(root/'library-manifest.json',{'schema':1,'release':index['release'],'files':manifest})
 print('Sealed',len(index['skills']),'skills;',len(manifest),'files')
def validate(root=ROOT):
 index=load(root/'release-index.json');whole=load(root/'library-manifest.json');errors=[]
 actual_files={p.relative_to(root).as_posix() for p in files(root) if p.name!='library-manifest.json' and not p.relative_to(root).as_posix().startswith('_docs/run-')}
 for rel in sorted(actual_files-set(whole['files'])):errors.append('Unsealed library file: '+rel)
 for rel,h in whole['files'].items():
  p=contained(root/rel,root)
  if not p.is_file() or sha(p)!=h:errors.append('Library hash: '+rel)
 for name,sel in index['skills'].items():
  folder=root/'skills'/name
  for key in ['current','stable']:
   actual=(folder/key.upper()).read_text().strip()
   if actual!=sel[key]:errors.append('Selector mismatch: '+name+' '+key)
   release=folder/'versions'/actual
   if not (release/'SKILL.md').exists():errors.append('Missing release: '+str(release));continue
  for release in (folder/'versions').iterdir():
   m=load(release/'manifest.json')
   actual_release={p.relative_to(release).as_posix() for p in files(release) if p.name!='manifest.json'}
   if actual_release!=set(m['files']):errors.append('Release file inventory: '+str(release))
   for rel,h in m['files'].items():
    p=contained(release/rel,release)
    if not p.is_file() or sha(p)!=h:errors.append('Release hash: '+str(p))
 if errors:raise RuntimeError('\n'.join(errors[:30]))
 return {'skills':len(index['skills']),'files':len(whole['files']),'hashes':'pass'}
@contextlib.contextmanager
def lock(path):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 f=path.open('a+b');f.seek(0);f.write(b'0');f.flush();f.seek(0)
 try:
  if os.name=='nt':
   import msvcrt;msvcrt.locking(f.fileno(),msvcrt.LK_NBLCK,1)
  else:
   import fcntl;fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except OSError:f.close();raise RuntimeError('Another library operation holds the lock')
 try:yield
 finally:
  if os.name=='nt':f.seek(0);msvcrt.locking(f.fileno(),msvcrt.LK_UNLCK,1)
  else:fcntl.flock(f,fcntl.LOCK_UN)
  f.close()
def native_entry(body,release,library):
 # The installed entry contains the actual instructions. Resource references are direct.
 text=body
 def link(m):
  raw=m[1]
  if re.match(r'[a-z]+:|#|/|<',raw,re.I):return m[0]
  path,sep,anchor=raw.partition('#');p=(release/path).resolve()
  return ']('+p.as_posix()+(sep+anchor if sep else '')+')' if p.exists() else m[0]
 text=re.sub(r'\]\(([^)\s]+)\)',link,text)
 text=text.replace('repo:',library.as_posix()+'/')
 fmend=text.find('---',3)+3
 note='\n\nAuthoritative release resources: `'+release.as_posix()+'`. Resolve unqualified resource paths relative to that directory; repository-root paths relative to `'+library.as_posix()+'`. This entry contains the current instructions. For an explicitly requested historical release, read its complete instructions from the same library release tree. No legacy aliases or fallback loading.\n'
 return text[:fmend]+note+text[fmend:]
def sync(config,dry=False,root=ROOT):
 cfg=load(config);validation=validate(root);state=Path(os.path.expandvars(cfg['state'])).resolve()
 targets=[]
 for x in cfg['homes']:
  p=Path(os.path.expandvars(x['path'])).resolve()
  if p.name!='skills' or p==root or p.is_relative_to(root):raise ValueError('Unsafe destination '+str(p))
  for q in [p,*p.parents]:
   if q.exists() and (q.is_symlink() or (os.name=='nt' and q.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)):raise ValueError('Reparse destination '+str(q))
  targets.append((x,p))
 index=load(root/'release-index.json');manifest=load(root/'library-manifest.json');gen=sha(root/'library-manifest.json')[:16]
 payload=state/'releases'/gen;result={'generation':gen,'validation':validation,'updated':0,'removed':0,'preserved_divergences':0,'homes':[],'dry_run':dry}
 if dry:print(json.dumps({'generation':gen,'homes':[str(p) for _,p in targets],'skills':len(index['skills']),'dry_run':True}));return result
 with lock(state/'sync.lock'):
  if not (payload/'library-manifest.json').exists():
   stage=state/'staging'/gen;stage.mkdir(parents=True,exist_ok=True)
   for rel,h in manifest['files'].items():
    p=contained(stage/rel,stage);p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists() or sha(p)!=h:shutil.copy2(root/rel,p)
    if sha(p)!=h:raise RuntimeError('Payload mismatch '+rel)
   shutil.copy2(root/'library-manifest.json',stage/'library-manifest.json')
   payload.parent.mkdir(parents=True,exist_ok=True);os.replace(stage,payload)
  else:validate(payload)
  stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
  baseline=load(root/'_tools/managed-baseline.json') if (root/'_tools/managed-baseline.json').exists() else {}
  for config,p in targets:
   oldpath=state/'installed'/((config['id'])+'.json')
   old=load(oldpath)['files'] if oldpath.exists() else baseline
   desired={}
   if config.get('discover',True):
    for name,sel in index['skills'].items():
     release=payload/'skills'/name/'versions'/sel['current']
     desired[name+'/SKILL.md']=native_entry((release/'SKILL.md').read_text(encoding='utf-8-sig'),release,payload).encode('utf-8')
     meta=release/'agents/openai.yaml'
     if meta.exists():
      desired[name+'/agents/openai.yaml']=meta.read_bytes()
      # Native UI metadata resolves icons relative to the native skill root.
      for icon in re.findall(r'^\s*icon_(?:small|large):\s*[\"\x27]?([^\s\"\x27]+)',meta.read_text(encoding='utf-8-sig'),re.M):
       resource=contained(release/icon,release)
       if not resource.is_file():raise RuntimeError('Missing native icon: '+str(resource))
       desired[name+'/'+icon]=resource.read_bytes()
   beforeback=state/'backups'/stamp/config['id'];owned={}
   for rel in sorted(set(old)|set(desired)):
    dst=contained(p/rel,p);data=desired.get(rel);exists=dst.exists();newhash=hashlib.sha256(data).hexdigest() if data is not None else None
    previoushash=sha(dst) if exists else None
    if exists and previoushash!=newhash:
     # Every replacement/removal is recoverable, including divergent local edits.
     b=contained(beforeback/rel,beforeback);b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(dst,b)
     if previoushash!=old.get(rel):result['preserved_divergences']+=1
    if data is None:
     if exists:dst.unlink();result['removed']+=1
    else:
     if previoushash!=newhash:
      dst.parent.mkdir(parents=True,exist_ok=True);tmp=dst.with_name(dst.name+'.pending');tmp.write_bytes(data);os.replace(tmp,dst);result['updated']+=1
     if sha(dst)!=newhash:raise RuntimeError('Installed hash mismatch')
     owned[rel]=newhash
   # Only remove empty directories under managed skill names, never unrelated/system trees.
   for name in index['skills']:
    d=p/name
    if d.exists():
     for base,dirs,fs in os.walk(d,topdown=False):
      q=contained(base,p)
      if not any(q.iterdir()):q.rmdir()
   save(oldpath,{'generation':gen,'files':owned,'discover':config.get('discover',True)})
   result['homes'].append({'id':config['id'],'skills':sum(r.endswith('/SKILL.md') for r in owned),'hashes':'pass'})
  save(state/'current.json',{'generation':gen,'library':str(payload)})
  save(state/'last-sync.json',result)
 print(json.dumps(result,indent=2));return result
def git_update(repo):
 repo=Path(repo).resolve()
 def git(*args):return subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True,check=True).stdout.strip()
 if git('status','--porcelain'):raise RuntimeError('Uncommitted changes; preserve and reconcile before Git update')
 branch=git('branch','--show-current')
 if not branch:raise RuntimeError('Detached HEAD; select a branch explicitly')
 git('fetch','origin');upstream=git('rev-parse','--abbrev-ref','@{upstream}')
 ahead,behind=map(int,git('rev-list','--left-right','--count','HEAD...'+upstream).split())
 if ahead and behind:raise RuntimeError('Branches diverged; no reset or automatic reconciliation')
 if behind:git('merge','--ff-only',upstream)
 print(json.dumps({'repository':str(repo),'head':git('rev-parse','HEAD'),'ahead':ahead,'fast_forwarded':behind>0}))
def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
 for name in ['seal','validate']:sub.add_parser(name)
 s=sub.add_parser('sync');s.add_argument('--config',type=Path,default=ROOT/'_tools/agent-homes.json');s.add_argument('--dry-run',action='store_true')
 b=sub.add_parser('backup');b.add_argument('source');b.add_argument('destination')
 r=sub.add_parser('restore');r.add_argument('snapshot');r.add_argument('destination');r.add_argument('--file')
 g=sub.add_parser('git-update');g.add_argument('repository')
 a=p.parse_args()
 if a.command=='seal':seal()
 elif a.command=='validate':print(json.dumps(validate(),indent=2))
 elif a.command=='sync':sync(a.config,a.dry_run)
 elif a.command=='backup':backup(a.source,a.destination)
 elif a.command=='restore':restore(a.snapshot,a.destination,a.file)
 elif a.command=='git-update':git_update(a.repository)
if __name__=='__main__':
 try:main()
 except Exception as e:print('ERROR:',e,file=sys.stderr);sys.exit(1)
