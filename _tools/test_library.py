"""Behavioral lifecycle tests. Codex | GPT-6 | 2026-09-20."""
import unittest,tempfile,json,hashlib,contextlib,io,re
from pathlib import Path
import library as lib

class Lifecycle(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name);self.root=self.base/'library';self.root.mkdir()
  p=self.root/'skills/example/versions/1.0.0';p.mkdir(parents=True)
  (p/'SKILL.md').write_text('---\nname: example\ndescription: Test a fixture\n---\n# Example\nRead [check](check.md).')
  (p/'check.md').write_text('Fixture resource, not a legacy dependency.')
  f=p.parents[1];(f/'SKILL.md').write_text('Select CURRENT');(f/'CURRENT').write_text('1.0.0');(f/'STABLE').write_text('1.0.0')
  lib.save(self.root/'release-index.json',{'release':'fixture','skills':{'example':{'current':'1.0.0','stable':'1.0.0'}}})
  lib.save(self.root/'_tools/managed-baseline.json',{'example/old.md':'baseline-hash'})
  self.home=self.base/'native/skills';self.home.mkdir(parents=True)
  (self.home/'.system').mkdir();(self.home/'.system/keep.md').write_text('system')
  (self.home/'unrelated').mkdir();(self.home/'unrelated/SKILL.md').write_text('unrelated')
  (self.home/'example').mkdir();(self.home/'example/old.md').write_text('divergent user edit')
  self.config=self.base/'config.json'
  lib.save(self.config,{'state':str(self.base/'state'),'homes':[{'id':'test','path':str(self.home)}]})
  lib.seal(self.root)
 def tearDown(self):self.temp.cleanup()
 def test_restore_and_selected_restore(self):
  source=self.base/'original';source.mkdir();(source/'.hidden').write_bytes(b'hidden');(source/'file.txt').write_text('preserved');(source/'empty').mkdir()
  snapshot=self.base/'backup';lib.backup(source,snapshot)
  lib.restore(snapshot,self.base/'restored');self.assertEqual((self.base/'restored/.hidden').read_bytes(),b'hidden');self.assertTrue((self.base/'restored/empty').is_dir())
  lib.restore(snapshot,self.base/'selected','file.txt');self.assertFalse((self.base/'selected/.hidden').exists())
  with self.assertRaises(ValueError):lib.restore(snapshot,source)
 def test_file_link_is_recorded_without_following(self):
  source=self.base/'links';source.mkdir();target=self.base/'external.txt';target.write_text('external resource')
  try:(source/'resource.txt').symlink_to(target)
  except OSError:self.skipTest('Host does not grant symbolic-link creation')
  snapshot=self.base/'links-backup';lib.backup(source,snapshot)
  manifest=lib.load(snapshot/'manifest.json')
  self.assertEqual(manifest['files'],[]);self.assertEqual(manifest['links'][0]['path'],'resource.txt')
 def test_hash_sync_divergence_removal_and_idempotence(self):
  a=lib.sync(self.config,root=self.root);self.assertEqual(a['removed'],1);self.assertGreater(a['preserved_divergences'],0)
  self.assertTrue((self.home/'.system/keep.md').exists());self.assertTrue((self.home/'unrelated/SKILL.md').exists())
  self.assertFalse((self.home/'example/old.md').exists())
  body=(self.home/'example/SKILL.md').read_text();self.assertIn('Fixture',next((self.base/'state/releases').glob('*/skills/example/versions/1.0.0/check.md')).read_text())
  self.assertIn('/releases/',body);self.assertEqual(len(list((self.home/'example').rglob('SKILL.md'))),1)
  b=lib.sync(self.config,root=self.root);self.assertEqual(b['updated'],0);self.assertEqual(b['removed'],0)
  self.assertTrue(list((self.base/'state/backups').rglob('old.md')))
 def test_tampered_release_blocks_sync(self):
  p=self.root/'skills/example/versions/1.0.0/check.md';p.write_text('changed')
  with self.assertRaises(RuntimeError):lib.sync(self.config,root=self.root)
  with self.assertRaises(RuntimeError):lib.seal(self.root)
 def test_native_metadata_assets_and_unsealed_files(self):
  release=self.root/'skills/example/versions/1.0.0'
  (release/'manifest.json').unlink() # fixture draft, never a published release
  (release/'agents').mkdir();(release/'assets').mkdir()
  (release/'agents/openai.yaml').write_text('interface:\n  icon_small: assets/icon.svg\n')
  (release/'assets/icon.svg').write_text('<svg/>')
  lib.seal(self.root);lib.sync(self.config,root=self.root)
  self.assertEqual((self.home/'example/assets/icon.svg').read_text(),'<svg/>')
  (self.root/'unexpected.md').write_text('not sealed')
  with self.assertRaises(RuntimeError):lib.validate(self.root)
 def test_shadow_home_removes_only_managed_files(self):
  c=lib.load(self.config);c['homes'][0]['discover']=False;lib.save(self.config,c);lib.sync(self.config,root=self.root)
  self.assertFalse((self.home/'example/old.md').exists());self.assertTrue((self.home/'.system/keep.md').exists())
 def test_bad_destination_preflight_and_dry_run(self):
  c=lib.load(self.config);c['homes'][0]['path']=str(self.base/'wrong');lib.save(self.config,c)
  with self.assertRaises(ValueError):lib.sync(self.config,root=self.root)
  self.assertFalse((self.base/'state').exists())
 def test_restore_path_traversal_rejected(self):
  with self.assertRaises(ValueError):lib.contained(self.base/'elsewhere',self.root)
 def test_publish_allowlist(self):
  other=self.root/'skills/other/versions/1.0.0';other.mkdir(parents=True)
  (other/'SKILL.md').write_text('---\nname: other\ndescription: Other fixture\n---\n# Other\n')
  folder=other.parents[1];(folder/'SKILL.md').write_text('Select CURRENT');(folder/'CURRENT').write_text('1.0.0');(folder/'STABLE').write_text('1.0.0')
  index=lib.load(self.root/'release-index.json');index['skills']['other']={'current':'1.0.0','stable':'1.0.0'};lib.save(self.root/'release-index.json',index)
  lib.seal(self.root)
  c=lib.load(self.config);c['homes'][0]['publish']=['example'];lib.save(self.config,c)
  lib.sync(self.config,root=self.root)
  self.assertTrue((self.home/'example/SKILL.md').exists());self.assertFalse((self.home/'other').exists())
  c['homes'][0]['publish']=['missing'];lib.save(self.config,c)
  with self.assertRaises(ValueError):lib.sync(self.config,root=self.root)
  c['homes'][0]['publish']=[];lib.save(self.config,c)
  lib.sync(self.config,root=self.root)
  self.assertFalse((self.home/'example/SKILL.md').exists())
  del c['homes'][0]['publish'];lib.save(self.config,c)
  lib.sync(self.config,root=self.root)
  self.assertTrue((self.home/'example/SKILL.md').exists());self.assertTrue((self.home/'other/SKILL.md').exists())
  dry=lib.sync(self.config,True,root=self.root);self.assertTrue(dry['dry_run']);self.assertEqual(dry['homes'][0]['skills'],2)

class CuriosityPolicy(unittest.TestCase):
 """Regression checks for the active Scripture Journey trust policy."""

 ROOT = Path(__file__).resolve().parents[1]
 SKILL = ROOT / 'skills' / 'curiosity-driven-scripture-journey'

 def setUp(self):
  self.version = (self.SKILL / 'CURRENT').read_text(encoding='utf-8').strip()
  self.release = self.SKILL / 'versions' / self.version
  self.assertTrue(self.release.is_dir(), f'missing active release: {self.release}')

 def read(self, relative):
  return (self.release / relative).read_text(encoding='utf-8')

 def test_current_release_matches_manifest(self):
  manifest = json.loads(self.read('manifest.json'))
  self.assertEqual(manifest['version'], self.version)
  self.assertEqual(manifest['sealed'], True)

 def test_banned_influence_methods_have_explicit_prohibitions(self):
  story = self.read('references/story-craft.md').lower()
  for phrase in (
   'banned influence and reprogramming methods',
   'the following are hard bans',
   'hypnosis',
   'theta states',
   'subliminal',
   'nlp-style',
   'coercive emotional conditioning',
   'affirmation-only',
   'manifestation',
  ):
   self.assertIn(phrase, story)
  for relative in (
   'SKILL.md',
   'references/learning-and-writing.md',
   'references/scripture-study.md',
   'references/youtube-planning.md',
   'references/quality-gates.md',
   'references/branching-journey.md',
   'references/learning-patterns.md',
  ):
   text = self.read(relative).lower()
   self.assertTrue(
    any(marker in text for marker in ('hard ban', 'banned', 'do not use', 'must not', 'never')),
    f'{relative} lost its influence-method prohibition',
   )

 def test_banned_methods_cannot_reappear_as_instructions(self):
  pattern = re.compile(
   r'\b(?:use|using|apply|prescribe|practice|teach|try|run)\s+'
   r'(?:hypnosis|hypnotherapy|theta|brainwave entrainment|subliminal|NLP|'
   r'affirmation-based mind reprogramming|manifestation)\b',
   re.IGNORECASE,
  )
  negative = ('do not', 'never', 'hard ban', 'banned', 'not use', 'must not', 'rejected')
  for relative in (
   'SKILL.md',
   'references/story-craft.md',
   'references/learning-and-writing.md',
   'references/scripture-study.md',
   'references/youtube-planning.md',
   'references/quality-gates.md',
   'references/branching-journey.md',
   'references/learning-patterns.md',
  ):
   for number, line in enumerate(self.read(relative).splitlines(), 1):
    if pattern.search(line) and not any(marker in line.lower() for marker in negative):
     self.fail(f'{relative}:{number} presents a banned method as an instruction: {line}')

 def test_neuroscience_requires_explicit_user_approval(self):
  story = self.read('references/story-craft.md').lower()
  for phrase in (
   'approval-gated neuroscience',
   'ask the user whether that use is acceptable',
   'if the user does not explicitly approve it',
   'source and evidence strength',
   'what the evidence does not establish',
  ):
   self.assertIn(phrase, story)
  for relative in (
   'SKILL.md',
   'references/learning-and-writing.md',
   'references/scripture-study.md',
   'references/youtube-planning.md',
   'references/quality-gates.md',
   'references/branching-journey.md',
  ):
   text = self.read(relative).lower()
   self.assertTrue(
    'neuroscience' in text and ('approval' in text or 'approve' in text or 'ask the user' in text),
    f'{relative} lacks the neuroscience approval gate',
   )


# Agent: Buffy | Model: GPT-5 · Thinking: not exposed | Date: 2026-09-24 | Added Scripture Journey influence-method and neuroscience-policy regression checks. -->

if __name__=='__main__':unittest.main()
