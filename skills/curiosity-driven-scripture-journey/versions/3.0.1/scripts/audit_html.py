#!/usr/bin/env python3
"""Deterministic static audit for Scripture Journey HTML candidates (v3.0.0).

Mechanical quality floor only. This does not score beauty or learning quality.
"""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang=""; self.main=False; self.h1=0; self.charset=False; self.viewport=False
        self.meta_desc=False; self.ids=[]; self.hash_links=0; self.img_no_alt=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html": self.lang=(a.get("lang") or "").strip()
        elif tag=="main": self.main=True
        elif tag=="h1": self.h1+=1
        elif tag=="meta":
            if "charset" in a: self.charset=True
            n=(a.get("name") or "").lower()
            if n=="viewport" and (a.get("content") or "").strip(): self.viewport=True
            if n=="description" and (a.get("content") or "").strip(): self.meta_desc=True
        elif tag=="a" and (a.get("href") or "").strip()=="#": self.hash_links+=1
        elif tag=="img" and "alt" not in a: self.img_no_alt+=1
        if a.get("id"): self.ids.append(str(a["id"]))
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

def audit(path: Path):
    text=path.read_text(encoding="utf-8")
    p=P(); p.feed(text)
    issues=[]
    def err(code,msg): issues.append({"severity":"error","code":code,"message":msg})
    def warn(code,msg): issues.append({"severity":"warning","code":code,"message":msg})
    if not p.lang: err("HTML_LANG_MISSING","html must declare lang.")
    if not p.charset: err("CHARSET_MISSING","charset meta is required.")
    if not p.viewport: err("VIEWPORT_MISSING","viewport meta is required.")
    if not re.search(r"<title>\s*[^<]+\s*</title>",text,re.I|re.S): err("TITLE_MISSING","non-empty title is required.")
    if not p.meta_desc: err("META_DESCRIPTION_MISSING","meta description is required.")
    if not p.main: err("MAIN_MISSING","main landmark is required.")
    if p.h1!=1: err("H1_COUNT",f"expected exactly one H1; found {p.h1}.")
    if p.hash_links: err("PLACEHOLDER_HASH_LINK",f"found {p.hash_links} unresolved href=# link(s).")
    if p.img_no_alt: err("IMG_ALT_MISSING",f"found {p.img_no_alt} image(s) without alt.")
    dup=[k for k,v in Counter(p.ids).items() if v>1]
    if dup: err("DUPLICATE_ID","duplicate id values: "+", ".join(sorted(dup)))
    if re.search(r"@media\s*\([^)]*(?:min|max)-width\s*:",text,re.I):
        err("VIEWPORT_COMPONENT_BREAKPOINT","viewport width media query found; use intrinsic/container component layout.")
    motion=bool(re.search(r"(?:animation\s*:|transition\s*:|animation-name\s*:|scroll-timeline|view-timeline)",text,re.I))
    if motion and not re.search(r"prefers-reduced-motion",text,re.I):
        err("REDUCED_MOTION_MISSING","motion is present without prefers-reduced-motion accommodation.")
    interactive=bool(re.search(r"<(?:a|button|input|select|textarea)\b",text,re.I))
    if interactive and not re.search(r":focus(?:-visible)?",text,re.I):
        err("FOCUS_STYLE_MISSING","interactive controls exist without detectable focus styling.")
    if re.search(r"font-family\s*:\s*(?:Inter|Arial|system-ui)(?:\s*[,;])",text,re.I):
        warn("GENERIC_FONT_RISK","generic/system-first font detected; verify intentional visual DNA.")
    errors=sum(i["severity"]=="error" for i in issues)
    return {"file":str(path),"result":"PASS" if errors==0 else "FAIL","errors":errors,
            "warnings":len(issues)-errors,"issues":issues}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("html",nargs="+",type=Path)
    ap.add_argument("--json",action="store_true",dest="as_json")
    a=ap.parse_args()
    results=[audit(p) for p in a.html]
    if a.as_json: print(json.dumps(results,indent=2))
    else:
        for r in results:
            print(f"{r['result']} {r['file']} ({r['errors']} errors, {r['warnings']} warnings)")
            for i in r["issues"]: print(f"  {i['severity'].upper()} {i['code']}: {i['message']}")
    raise SystemExit(1 if any(r["result"]=="FAIL" for r in results) else 0)

if __name__=="__main__":
    main()
