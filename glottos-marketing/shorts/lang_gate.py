#!/usr/bin/env python3
"""English-language gate for Shorts units (user rule 2026-09-27: every scenario is checked by a language
expert before it is produced; "learn a word naked" must never ship again).

  python3 shorts/lang_gate.py text    <unit.json>     # print every spoken/on-screen line to review
  python3 shorts/lang_gate.py approve <unit.json> --by glottos-language-editor --notes "..."
  python3 shorts/lang_gate.py verify  <unit.json>     # exit 1 if the text changed since approval

The approval stores a hash of ALL text (speech + card headline/sub). Any later edit invalidates it,
and build_short_v2.py refuses to render an unapproved unit."""
import hashlib, json, sys, time

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
    cmd, path = sys.argv[1], sys.argv[2]; u = json.load(open(path))
    if cmd == "text":
        for k, v in lines(u): print(f"{k:22} | {v}")
    elif cmd == "approve":
        args = dict(zip(sys.argv[3::2], sys.argv[4::2]))
        u["language_approval"] = {"hash": digest(u), "by": args.get("--by", "?"), "notes": args.get("--notes", ""),
                                  "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
        json.dump(u, open(path, "w"), indent=2, ensure_ascii=False); print("approved", digest(u))
    elif cmd == "verify":
        ok, a = verify(u); print("OK" if ok else "NOT APPROVED (text changed or never checked)", a.get("by", "")); sys.exit(0 if ok else 1)
