#!/usr/bin/env python3
"""English-language gate for Shorts units (user rule 2026-09-27: every scenario is checked by a language
expert before it is produced; "learn a word naked" must never ship again).

  python3 shorts/lang_gate.py text    <unit.json>     # print every spoken/on-screen line to review
  python3 shorts/lang_gate.py approve <unit.json> --by glottos-language-editor --notes "..."
  python3 shorts/lang_gate.py verify  <unit.json>     # exit 1 if the text changed since approval
  python3 shorts/lang_gate.py caps    <unit.json|script.md>  # exit 1 if SPOKEN text has an ALL-CAPS word

CAPS rule (user 2026-09-29, S3 "BIG" was read aloud as "B-I-G"): TTS and NotebookLM voices spell out
capitalised words. Spoken text must write the word in lower case ("ten words for big"); capitals are fine
on cards/titles only. `approve` refuses a unit whose speech fails this check. For script.md (specials →
NotebookLM video) the spoken lines are the "> " quote lines, [bracket] notes excluded.

The approval stores a hash of ALL text (speech + card headline/sub). Any later edit invalidates it,
and build_short_v2.py refuses to render an unapproved unit."""
import hashlib, json, re, sys, time

# spelled out on purpose / read correctly as letters
CAPS_OK = {"OK", "TV", "UK", "US", "USA", "AI", "A1", "A2", "B1", "B2", "C1", "C2", "PS", "ID", "GPS"}

def spoken(path):
    """(label, text) of everything a voice will SAY"""
    if path.endswith(".json"):
        return [(f"beat {i} speech", b["speech"]) for i, b in enumerate(json.load(open(path))["beats"], 1)]
    out = []
    for n, l in enumerate(open(path, encoding="utf-8"), 1):
        if l.lstrip().startswith(">"): out.append((f"line {n}", re.sub(r"\[[^\]]*\]", "", l.lstrip()[1:])))
    return out

def caps_hits(path):
    return [(k, w, t.strip()) for k, t in spoken(path) for w in re.findall(r"\b[A-Z][A-Z0-9'-]*[A-Z0-9]\b", t) if w not in CAPS_OK]

def lines(u):
    out = []
    for i, b in enumerate(u["beats"], 1):
        out.append((f"beat {i} speech", b["speech"]))
        for k, v in (b.get("card") or {}).items(): out.append((f"beat {i} card.{k}", v))
        for k, v in (b.get("quiz") or {}).items():
            if isinstance(v, str) and k not in ("reveal_panel",): out.append((f"beat {i} quiz.{k}", v))
    return out

def digest(u): return hashlib.sha256(json.dumps(lines(u), ensure_ascii=False).encode()).hexdigest()[:16]

def verify(u):
    a = u.get("language_approval") or {}
    return a.get("hash") == digest(u), a

if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]; u = json.load(open(path)) if path.endswith(".json") else None
    if cmd == "text":
        for k, v in lines(u): print(f"{k:22} | {v}")
    elif cmd == "caps":
        hits = caps_hits(path)
        for k, w, t in hits: print(f"CAPS {k}: '{w}' will be SPELLED OUT by the voice -> write it in lower case | {t[:120]}")
        print("OK: no all-caps words in spoken text" if not hits else f"FAIL: {len(hits)} all-caps word(s) in spoken text"); sys.exit(1 if hits else 0)
    elif cmd == "approve":
        if caps_hits(path): sys.exit("REFUSED: all-caps word in speech (voice spells it letter by letter) -> run `caps`, fix, re-approve")
        args = dict(zip(sys.argv[3::2], sys.argv[4::2]))
        u["language_approval"] = {"hash": digest(u), "by": args.get("--by", "?"), "notes": args.get("--notes", ""),
                                  "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
        json.dump(u, open(path, "w"), indent=2, ensure_ascii=False); print("approved", digest(u))
    elif cmd == "verify":
        ok, a = verify(u); print("OK" if ok else "NOT APPROVED (text changed or never checked)", a.get("by", "")); sys.exit(0 if ok else 1)
