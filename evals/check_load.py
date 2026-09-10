#!/usr/bin/env python3
"""
check_load.py - score a captured agent run against router-fixtures.yaml.

Agent: claude | Model: claude-opus-5 | Thinking: not exposed | Date: 2026-09-10

Agents are not scriptable from here, so the honest shape is manual capture, automatic
checking. Paste a fixture prompt into an agent, copy the block it emits, save it, run this.

    python evals/check_load.py --list
    python evals/check_load.py --fixture css-footer-contrast --capture evals/captures/css-footer-contrast.txt
    python evals/check_load.py --all                     # scores every capture present
    python evals/check_load.py --all --baseline out.json # record a run for comparison

A capture is whatever the agent printed, as long as it contains the declaration block:

    SKILL: curiosity-driven-scripture-journey
    LANES: web.repair
    LOAD:  references/web-experience.md
    LOAD:  repo:COLOR-PSYCHOLOGY.md
    BRIEF: daniel-8/project-brief.md  (stage: approved-for-build)

Verdicts
    PASS         everything required loaded, nothing forbidden, within budget
    MISSING      a required path did not load
    EXTRA        a forbidden path loaded
    OVER         more files than the lane's budget
    WRONG-SKILL  the wrong skill answered, or a forbidden one did

This checks ROUTING ONLY. It says nothing about whether the output was any good - that is
what the quality gates are for, and calling this a quality harness would be dishonest.
"""

from __future__ import annotations
import argparse, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, 'router-fixtures.yaml')
CAPTURES = os.path.join(HERE, 'captures')


# --- a deliberately small YAML reader: this file's shape only, no dependency -------------
def load_fixtures(path: str):
    """Parse router-fixtures.yaml without requiring PyYAML."""
    try:
        import yaml                                    # noqa: F401
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f).get('fixtures', [])
    except ImportError:
        pass

    fixtures, cur, key = [], None, None
    with open(path, encoding='utf-8') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            if line.startswith('- id:'):
                if cur:
                    fixtures.append(cur)
                cur = {'id': line.split(':', 1)[1].strip()}
                key = None
                continue
            if cur is None:
                continue
            m = re.match(r'^  (\w+):\s*(.*)$', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val.startswith('[') and val.endswith(']'):
                    inner = val[1:-1].strip()
                    cur[key] = [x.strip() for x in inner.split(',') if x.strip()] if inner else []
                    key = None
                elif val in ('', '>', '|', '>-', '|-'):
                    cur[key] = [] if val == '' else ''
                elif val == 'null':
                    cur[key] = None
                    key = None
                elif val.isdigit():
                    cur[key] = int(val)
                    key = None
                elif val in ('true', 'false'):
                    cur[key] = (val == 'true')
                    key = None
                else:
                    cur[key] = val.strip('"\'')
                    key = None
                continue
            m = re.match(r'^\s+- (.*)$', line)
            if m and key:
                cur.setdefault(key, [])
                if isinstance(cur[key], list):
                    cur[key].append(m.group(1).strip().strip('"\''))
                continue
            if key and isinstance(cur.get(key), str):
                cur[key] = (cur[key] + ' ' + line.strip()).strip()
    if cur:
        fixtures.append(cur)
    return [f for f in fixtures if 'id' in f]


def parse_capture(text: str):
    out = {'skill': None, 'lanes': [], 'load': [], 'brief': None}
    for line in text.splitlines():
        s = line.strip()
        low = s.lower()
        if low.startswith('skill:'):
            out['skill'] = s.split(':', 1)[1].strip() or None
        elif low.startswith('lanes:'):
            out['lanes'] = [x.strip() for x in s.split(':', 1)[1].split(',') if x.strip()]
        elif low.startswith('load:'):
            p = s.split(':', 1)[1].strip()
            if p:
                out['load'].append(p)
        elif low.startswith('brief:'):
            out['brief'] = s.split(':', 1)[1].strip() or None
    return out


def score(fx: dict, cap: dict):
    problems = []

    want_skill = fx.get('expect_skill')
    if want_skill and cap['skill'] != want_skill:
        problems.append(('WRONG-SKILL', f"expected {want_skill}, got {cap['skill'] or 'none'}"))
    if want_skill is None and 'expect_skill' in fx and cap['skill']:
        problems.append(('WRONG-SKILL', f"expected no skill, got {cap['skill']}"))
    for bad in fx.get('forbid_skill', []) or []:
        if cap['skill'] == bad:
            problems.append(('WRONG-SKILL', f"forbidden skill loaded: {bad}"))

    loaded = set(cap['load'])
    for req in fx.get('expect_load', []) or []:
        if req not in loaded:
            problems.append(('MISSING', req))
    for bad in fx.get('forbid', []) or []:
        if bad in loaded:
            problems.append(('EXTRA', bad))

    cap_max = fx.get('max_files')
    if isinstance(cap_max, int) and len(loaded) > cap_max:
        problems.append(('OVER', f'{len(loaded)} files loaded, budget {cap_max}'))

    if fx.get('expect_brief') and not cap['brief']:
        problems.append(('MISSING', 'BRIEF: line — resume fixtures must declare the brief'))

    want_lanes = set(fx.get('expect_lanes', []) or [])
    if want_lanes and not want_lanes.issubset(set(cap['lanes'])):
        problems.append(('MISSING', 'lanes ' + ', '.join(sorted(want_lanes - set(cap['lanes'])))))

    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--fixtures', default=FIXTURES)
    ap.add_argument('--captures', default=CAPTURES)
    ap.add_argument('--fixture')
    ap.add_argument('--capture')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--baseline', help='write results as JSON for later comparison')
    a = ap.parse_args()

    fixtures = load_fixtures(a.fixtures)
    if not fixtures:
        print(f'No fixtures parsed from {a.fixtures}', file=sys.stderr)
        return 2

    if a.list:
        print(f'{len(fixtures)} fixture(s) in {os.path.basename(a.fixtures)}:\n')
        for fx in fixtures:
            print(f"  {fx['id']}")
            print(f"      {fx.get('prompt', '')}")
        return 0

    jobs = []
    if a.fixture:
        fx = next((f for f in fixtures if f['id'] == a.fixture), None)
        if not fx:
            print(f'No fixture id {a.fixture!r}', file=sys.stderr)
            return 2
        cap_path = a.capture or os.path.join(a.captures, fx['id'] + '.txt')
        jobs.append((fx, cap_path))
    elif a.all:
        for fx in fixtures:
            p = os.path.join(a.captures, fx['id'] + '.txt')
            if os.path.exists(p):
                jobs.append((fx, p))
        if not jobs:
            print(f'No captures found in {a.captures}.')
            print('Paste a fixture prompt into an agent, save its LANES/LOAD block as')
            print(f'{a.captures}/<fixture-id>.txt, then re-run.')
            return 0
    else:
        ap.print_help()
        return 0

    results, failed = [], 0
    for fx, cap_path in jobs:
        if not os.path.exists(cap_path):
            print(f"  ??  {fx['id']:32} no capture at {cap_path}")
            continue
        cap = parse_capture(open(cap_path, encoding='utf-8', errors='replace').read())
        problems = score(fx, cap)
        results.append({'id': fx['id'], 'problems': problems, 'loaded': len(cap['load'])})
        if problems:
            failed += 1
            print(f"  FAIL  {fx['id']}")
            for kind, detail in problems:
                print(f"          {kind:12} {detail}")
        else:
            print(f"  PASS  {fx['id']:32} ({len(cap['load'])} file(s))")

    total = len(results)
    print(f"\n{total - failed}/{total} passed.")
    if a.baseline:
        with open(a.baseline, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f'baseline written: {a.baseline}')
    return 1 if failed else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except BrokenPipeError:          # piped to head/less
        sys.exit(0)
