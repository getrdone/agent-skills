#!/usr/bin/env python3
"""
check_links.py - dead-reference janitor for getrdone/agent-skills.

Agent: claude | Model: claude-opus-5 | Thinking: not exposed | Date: 2026-09-10

Finds local file references that do not resolve, and (with --load-map) references that
exist but no lane loads. Both are silent quality killers: a dead pointer sends an agent
looking for a file that moved, and an orphaned reference is knowledge nothing can reach.

    python tools/check_links.py                 # CURRENT release only (default)
    python tools/check_links.py --all-versions  # include versions/ history
    python tools/check_links.py --load-map      # also run the orphan check
    python tools/check_links.py -v              # list every reference checked

Exit code 1 if anything is broken. Safe to wire into a pre-commit hook or CI.

WHAT IT DELIBERATELY IGNORES
  - anything inside a fenced code block (examples, templates, file-shape diagrams)
  - tokens with a placeholder or glob character:  < > * | whitespace
  - URLs, absolute Windows paths, anchors, and `~` paths
  - filenames owned by another repository (see EXTERNAL below) - a pointer to the
    private source library is not a dead link in this repo
"""

from __future__ import annotations
import argparse, os, re, sys

EXTS = ('.md', '.yaml', '.yml', '.py', '.ps1', '.html', '.json', '.svg', '.sql', '.psd1')
SCAN = ('.md', '.yaml', '.yml')

# Filenames that legitimately live in another repo or on the operator's machine.
EXTERNAL = {
    'registry.yaml', 'record.yaml', 'content.md', 'notes.md',
    'source-library.lock.yaml', 'sources.sqlite3', 'schema.sql',
    'GLOSSARY.md', 'people.json', 'folder-map.psd1', 'config.psd1',
    'build-translator-pdf.ps1',
}
# Reference prefixes owned upstream (provenance blocks quote them on purpose).
EXTERNAL_PREFIX = ('skills/premium-frontend-ui', 'skills/gsap-framer-scroll-animation',
                   'references/gsap.md', 'references/framer.md',
                   'design-resources/', 'sources/', 'database/', 'indexes/')

# Artifacts that live in a WORK folder, never in this repo. Naming them here is correct;
# resolving them here would be wrong. See WORKSPACE.md.
WORKFOLDER_PREFIX = ('prompts/', 'deliverables/', 'planning/', 'mood/',
                     'references/dynamic-symmetry/', 'sources/intake/')

LINK = re.compile(r'\]\(([^)\s]+)\)')
TICK = re.compile(r'`([^`\n]+)`')
FENCE = re.compile(r'^\s*(```|~~~)')
PLACEHOLDER = re.compile(r'[<>*|\s…]')


def strip_fences(text: str):
    """Yield (lineno, line) for lines outside fenced code blocks."""
    inside = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            yield i, line


def candidates(line: str):
    """Markdown links are always checked. Backticked text is only checked when it looks
    like a path (contains a separator) - a bare filename in prose is prose."""
    for m in LINK.finditer(line):
        yield m.group(1)
    for m in TICK.finditer(line):
        if '/' in m.group(1):
            yield m.group(1)


def is_checkable(ref: str) -> bool:
    if not ref or PLACEHOLDER.search(ref):
        return False
    if ref.startswith(('http://', 'https://', 'mailto:', '#', '~', '/')):
        return False
    if re.match(r'^[A-Za-z]:[\\/]', ref) or '\\' in ref:
        return False
    if not ref.endswith(EXTS):
        return False
    if os.path.basename(ref) in EXTERNAL:
        return False
    if any(ref.startswith(p) for p in EXTERNAL_PREFIX):
        return False
    if any(ref.startswith(p) for p in WORKFOLDER_PREFIX):
        return False
    if os.path.splitext(os.path.basename(ref))[0] == '':      # a bare '.md'
        return False
    return True


def bases_for(path: str, root: str, ref: str, cur: str | None):
    """Every base a relative path in this file may legitimately resolve against."""
    out = [os.path.dirname(path), root]
    norm = path.replace('\\', '/')
    m = re.search(r'(.*?/versions/[^/]+)/', norm)
    if m:
        out.insert(1, m.group(1))          # a version's files resolve under that version
    elif cur and ref.startswith(('references/', 'scripts/')):
        # A file that sits ABOVE versions/ (a router, a README) naming a versioned path.
        # The path-resolution rule says those resolve under the CURRENT release.
        m2 = re.search(r'(.*?/skills/[^/]+)/', norm + '/')
        if m2:
            out.insert(1, os.path.join(m2.group(1), 'versions', cur))
    return out


def current_version(root: str) -> str | None:
    p = os.path.join(root, 'skills', 'curiosity-driven-scripture-journey', 'CURRENT')
    if os.path.exists(p):
        return open(p, encoding='utf-8').read().strip()
    return None


def walk(root: str, all_versions: bool, cur: str | None):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ('.git', 'node_modules', '__pycache__')]
        rel_dir = os.path.relpath(dp, root).replace('\\', '/')
        if not all_versions and '/versions/' in '/' + rel_dir + '/':
            m = re.search(r'/versions/([^/]+)', '/' + rel_dir)
            if m and cur and m.group(1) != cur:
                continue
        for f in fn:
            if f.endswith(SCAN):
                yield os.path.join(dp, f)


def check_links(root: str, all_versions: bool, verbose: bool):
    cur = current_version(root)
    broken, checked = [], 0
    for path in walk(root, all_versions, cur):
        try:
            text = open(path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for lineno, line in strip_fences(text):
            for ref in candidates(line):
                if not is_checkable(ref):
                    continue
                checked += 1
                if any(os.path.exists(os.path.normpath(os.path.join(b, ref)))
                       for b in bases_for(path, root, ref, cur)):
                    if verbose:
                        print(f'  ok   {os.path.relpath(path, root)}:{lineno}  {ref}')
                    continue
                broken.append((os.path.relpath(path, root).replace('\\', '/'), lineno, ref))
    return broken, checked


def check_load_map(root: str):
    """Every reference file in the CURRENT release must appear in load-map.yaml."""
    cur = current_version(root)
    if not cur:
        return ['no CURRENT file - cannot locate the release'], 0
    base = os.path.join(root, 'skills', 'curiosity-driven-scripture-journey', 'versions', cur)
    lm = os.path.join(base, 'load-map.yaml')
    refs = os.path.join(base, 'references')
    if not os.path.exists(lm):
        return [f'missing {os.path.relpath(lm, root)}'], 0
    if not os.path.isdir(refs):
        return [f'missing {os.path.relpath(refs, root)}'], 0
    body = open(lm, encoding='utf-8', errors='replace').read()
    orphans = []
    names = sorted(f for f in os.listdir(refs) if f.endswith('.md'))
    for name in names:
        if f'references/{name}' not in body:
            orphans.append(f'references/{name} is in the tree but no lane loads it')
    return orphans, len(names)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--root', default=here, help='repository root (default: parent of tools/)')
    ap.add_argument('--all-versions', action='store_true', help='also scan versions/ history')
    ap.add_argument('--load-map', action='store_true', help='also check for orphaned references')
    ap.add_argument('-v', '--verbose', action='store_true')
    a = ap.parse_args()

    root = os.path.abspath(a.root)
    cur = current_version(root)
    print(f'check_links: {root}' + (f'   CURRENT={cur}' if cur else ''))

    broken, checked = check_links(root, a.all_versions, a.verbose)
    print(f'\n{checked} local reference(s) checked.')
    if broken:
        print(f'{len(broken)} BROKEN:\n')
        for f, ln, ref in broken:
            print(f'  {f}:{ln}\n      -> {ref}')
    else:
        print('No broken local references.')

    orphans = []
    if a.load_map:
        orphans, n = check_load_map(root)
        print(f'\nload-map: {n} reference file(s) in the CURRENT release.')
        if orphans:
            print(f'{len(orphans)} ORPHANED:\n')
            for o in orphans:
                print(f'  {o}')
        else:
            print('Every reference is reachable from at least one lane.')

    if broken or orphans:
        print('\nFAIL')
        return 1
    print('\nPASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
