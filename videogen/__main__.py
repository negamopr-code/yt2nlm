"""CLI:
    python -m videogen samples                  # 3 voice samples -> user picks
    python -m videogen brand-extract            # palette from old channel videos
    python -m videogen topics                   # show the current topic queue
    python -m videogen make N [--format shorts|long] [--topic WORD]
    python -m videogen serve                    # review queue + upload (phase B)
    python -m videogen clean ID                 # drop heavy intermediates
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="videogen")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("samples")
    sub.add_parser("brand-extract")
    sub.add_parser("topics")
    mk = sub.add_parser("make")
    mk.add_argument("n", type=int, nargs="?", default=1)
    mk.add_argument("--format", choices=["shorts", "long"], default="shorts")
    mk.add_argument("--topic", default=None)
    sub.add_parser("serve")
    cl = sub.add_parser("clean")
    cl.add_argument("id")
    args = p.parse_args(argv)

    if args.cmd == "samples":
        from . import config, script, topics as tp, tts
        cfg = config.load_config()
        state = config.load_state()
        q = tp.uncovered(tp.build_queue(cfg, state), state, "shorts", True)
        cached = Path("/tmp") / "videogen_sample_script.json"
        # sample script: use any existing rendered script, else generate one
        s = None
        for it in state["items"].values():
            sp = Path(it["dir"]) / "script.json"
            if sp.exists():
                s = json.loads(sp.read_text())
                break
        if s is None:
            s = script.generate(q[0], cfg, "shorts")
        tts.make_samples(s, cfg["voice_rate"])
        print("pick a voice by setting `voice` in state/videogen.config.json")
        return 0
    if args.cmd == "brand-extract":
        from . import brand
        brand.extract(Path("/tmp"))
        return 0
    if args.cmd == "topics":
        from . import config, topics as tp
        cfg = config.load_config()
        state = config.load_state()
        for t in tp.uncovered(tp.build_queue(cfg, state), state, "shorts",
                              cfg["recover_legacy"])[:25]:
            print(f"{t['score']:6.1f}  {t['target']:20}  {t['source']['kind']}")
        return 0
    if args.cmd == "make":
        from . import pipeline
        made = pipeline.make(args.n, args.format, args.topic)
        print("rendered:", made)
        return 0
    if args.cmd == "serve":
        from . import server
        server.main()
        return 0
    if args.cmd == "clean":
        from . import config
        state = config.load_state()
        it = state["items"].get(args.id)
        if not it:
            print("unknown id", file=sys.stderr)
            return 1
        d = Path(it["dir"])
        for sub_dir in ("work", "slides", "audio"):
            shutil.rmtree(d / sub_dir, ignore_errors=True)
        print(f"cleaned intermediates of {args.id} (final.mp4/thumb/srt kept)")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
