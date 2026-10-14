#!/usr/bin/env python3
"""ONE full-frame drawn picture of a situation for a Short's first frame (user 2026-10-11: the Shorts are swiped because
frame 0 is a dark page of text; both expert corpora: frame 0 must be a picture of the situation, understood without sound).
Same road as mascot_host.py: no local image model -> NotebookLM infographic with the logo + a written brief as sources and
a focus prompt asking for one illustration without text. Portrait. The sources are deleted afterwards.
  .nlmvenv/bin/python shorts/scene_from_nlm.py <out.png> <style> <profile> "<scene description>" [--no-mascot]
--no-mascot (lab repair 2026-10-14, user go-ahead): the same clay boy in ~40 pictures made the H62/H63 Shorts look alike
(YouTube similarity / "AI slop" repetition) -> no logo source, no character sheet; the scene is drawn on its own, in the
style passed (vary it per word)."""
import json, os, re, subprocess, sys, time
from pathlib import Path
ROOT = Path("/workspace/glottos-marketing"); NLM = str(ROOT / ".nlmvenv/bin/nlm")
ACC = json.load(open(ROOT / "state/nlm-accounts.json"))
CHAR = """CHARACTER SHEET - the anotherwordfor.net mascot (see the attached logo image).
A cheerful cartoon boy of about 12: messy chestnut-brown hair, big round white eyes with small dark pupils, a round pink nose,
rosy cheeks. He wears a long-sleeved leaf-green sweater, light-blue jeans and red-and-white sneakers.
NEW SCENE WANTED: {scene}
Composition: PORTRAIT 9:16, like a phone screen. The boy is BIG, in the middle and lower part of the picture, his face clearly
visible with a strong, exaggerated, funny expression. The TOP QUARTER of the picture is calm, plain background (space for a
word later). Bright, saturated, high-contrast colours; one simple scene, few objects, nothing small."""
FREE = """SCENE BRIEF for one illustration (no recurring character, no mascot, no logo).
SCENE WANTED: {scene}
Composition: PORTRAIT 9:16, like a phone screen. ONE simple, clear scene that a viewer understands in one second, the main
subject BIG in the middle of the picture. Bright, saturated, high-contrast colours; few objects, nothing small."""
FOCUS_FREE = ("Draw exactly ONE single full-frame illustration of the brief's SCENE WANTED. No cartoon boy mascot, no logo. "
              "Absolutely NO text, no title, no labels, no captions, no letters, no numbers, no icons, no magnifying glass, "
              "no panels or boxes: just the picture, filling the whole portrait frame.")
FOCUS = ("Draw exactly ONE single full-frame cartoon illustration of the character sheet's NEW SCENE, keeping the mascot "
         "recognisable (hair, eyes, nose, green sweater). Absolutely NO text, no title, no labels, no captions, no letters, "
         "no numbers, no icons, no panels or boxes: just the picture, filling the whole portrait frame.")
def sh(args, prof, timeout=600):
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout, env={**os.environ, "HOME": "/home/node", "NLM_PROFILE": prof})
    return (r.stdout or "") + (r.stderr or "")
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)
def main(dst, style, prof, scene, free=False):
    dst = Path(dst); dst.parent.mkdir(parents=True, exist_ok=True); nb = ACC["notebooks"][prof]; sids = []
    srcs = ([["--text", FREE.format(scene=scene), "--title", "SCENE BRIEF (delete after)"]] if free else
            [["--file", str(ROOT / "state/brand/awf-logo-orig.png"), "--title", "MASCOT LOGO (delete after)"],
             ["--text", CHAR.format(scene=scene), "--title", "SCENE BRIEF (delete after)"]])
    for args in srcs:
        o = sh([NLM, "source", "add", nb, *args, "--wait", "--profile", prof], prof)
        m = re.search(r"Source ID: (\S+)", o)
        if m: sids.append(m[1])
        else: log(prof, "source add failed:", o.strip()[-200:])
    try:
        if len(sids) < len(srcs): return 1
        o = sh([NLM, "infographic", "create", nb, "--orientation", "portrait", "--detail", "concise", "--style", style,
                "--focus", FOCUS_FREE if free else FOCUS, "--source-ids", ",".join(sids), "-y", "--profile", prof], prof)
        aid = (re.search(r"Artifact ID: (\S+)", o) or [None, None])[1]
        if not aid: log(prof, "create refused:", o.strip()[-200:]); return 1
        log(prof, style, "generating", aid); st = None
        for _ in range(60):
            time.sleep(20)
            o = sh([NLM, "studio", "status", nb, "--json", "--profile", prof], prof, 120)
            try: st = {a["id"]: a for a in json.loads(o[o.index("["):])}.get(aid, {}).get("status")
            except Exception: st = None
            if st in ("completed", "failed", "error"): break
        if st == "completed": sh([NLM, "download", "infographic", nb, "--id", aid, "--output", str(dst), "--no-progress"], prof, 300)
        log(prof, style, st, dst if dst.exists() else "NO FILE"); return 0 if dst.exists() else 1
    finally:
        for s in sids: sh([NLM, "source", "delete", s, "-y", "--profile", prof], prof)
if __name__ == "__main__": sys.exit(main(*sys.argv[1:5], free="--no-mascot" in sys.argv[5:]))
