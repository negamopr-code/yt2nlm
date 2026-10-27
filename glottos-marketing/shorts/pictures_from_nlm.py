#!/usr/bin/env python3
"""Pictures for a Stop-Saying-lane Short from ONE NotebookLM video overview — no Claude (user 2026-09-30: "in future
we can say to nlm to generate the video overview with no text whatsoever on it, then we cut ... and we are ready to go").

  .nlmvenv/bin/python shorts/pictures_from_nlm.py shorts/units/<unit>.json

1. picture brief (the unit's words + examples, in order) -> text source in the Glottos production notebook of the first
   pool account that isn't rate-limited (state/nlm-accounts.json order; failover like nlm_jobs.py)
2. `nlm video create --format explainer` with a pictures-only, no-text style prompt; poll; download
3. faster-whisper word timestamps of NotebookLM's own narration: the first time each word is said (in order) = its scene;
   3 candidate frames just after it, the one with the least text + most drawing wins
4. shorts/detext.py (own process): text + watermark inpainted, square crop -> state/shorts/<id>/pic-NN.png
5. writes state/shorts/<id>/pictures.json {beat: {file, t, word}} (the builder reads it; the unit file is never touched,
   so its language approval stays valid) + contact.jpg for the visual check; deletes the temporary source.
The narration audio is only used for timing and is discarded (the Short's voice is Kokoro)."""
import json, os, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
NLM = str(ROOT / ".nlmvenv/bin/nlm"); TTSPY = str(ROOT / ".ttsvenv/bin/python")
FF = str(ROOT / ".nlmvenv/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2")
ACC = json.load(open(ROOT / "state/nlm-accounts.json"))
# 09-30: the custom watercolour --style-prompt made NotebookLM bake a BLUE title card over every picture (L2-1 rejected);
# S3 (whiteboard style) left its pictures free and gave the one Short that took off (kvCFmAhXcH8) -> whiteboard is the default.
STYLE = ("Hand-drawn watercolour and ink illustrations, like a picture book: one big, clear, full-frame picture per scene. "
         "Absolutely NO text anywhere on screen: no words, titles, labels, captions, lists, cards, numbers or speech bubbles.")

def sh(args, prof, timeout=600):
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                       env={**os.environ, "HOME": "/home/node", "NLM_PROFILE": prof})
    return r.returncode, (r.stdout or "") + (r.stderr or "")

def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)

def main(unit_path):
    u = json.load(open(unit_path)); out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    words = [(i, b) for i, b in enumerate(u["beats"], 1) if b["kind"] == "word"]
    brief = "\n".join(f"Scene {n}: {b['card']['headline'].rstrip('.!')} — {b['card'].get('use','')} {b['card']['sub']}. Say \"{b['card']['headline'].rstrip('.!')}\" "
                      f"first, then show one big picture of this moment: {b['card'].get('use','')} {b['card']['sub']}." for n, (i, b) in enumerate(words, 1))
    src = f"PICTURE BRIEF for a short vocabulary video. Five scenes, in this order.\n{brief}"
    focus = ("Five scenes, one per numbered item, in exactly this order. In each scene say the word or phrase first, then describe "
             "the picture in one short sentence. Every scene is a full-screen illustration with no text on it at all. Keep it short. "
             "Do not draw a magnifying glass anywhere.")      # user 2026-10-05: a glass that magnifies nothing makes no sense
    video = out / "nlm-pictures.mp4"
    if not video.exists():
        pool = [p for p in ACC["pool"] if ACC["notebooks"].get(p)]
        for prof in pool:
            nb = ACC["notebooks"][prof]
            rc, o = sh([NLM, "source", "add", nb, "--text", src, "--title", f"PICTURE BRIEF {u['id']} (delete after)", "--wait", "--profile", prof], prof)
            sid = (re.search(r"Source ID: (\S+)", o) or [None, None])[1]
            if not sid: log(f"{prof}: source add failed: {o.strip()[-200:]}"); continue
            rc, o = sh([NLM, "video", "create", nb, "--format", "explainer", "--style", os.environ.get("NLM_VIDEO_STYLE", "whiteboard"), "--language", "en",
                        "--source-ids", sid, "--focus", focus, "-y", "--profile", prof], prof)
            aid = (re.search(r"Artifact ID: (\S+)", o) or [None, None])[1]
            if not aid:
                log(f"{prof}: video create refused ({o.strip()[-160:]}) -> next account")
                sh([NLM, "source", "delete", sid, "-y", "--profile", prof], prof); continue
            log(f"{prof}: video generating {aid}")
            for _ in range(120):                                    # up to 60 min
                time.sleep(30)
                rc, o = sh([NLM, "studio", "status", nb, "--json", "--profile", prof], prof, 120)
                try: st = {a["id"]: a for a in json.loads(o[o.index("["):])}.get(aid, {}).get("status")
                except Exception: st = None
                if st in ("completed", "failed", "error"): break
            log(f"{prof}: status {st}")
            if st == "completed":
                sh([NLM, "download", "video", nb, "--id", aid, "--output", str(video), "--no-progress"], prof, 900)
            sh([NLM, "source", "delete", sid, "-y", "--profile", prof], prof)
            if video.exists(): break
        if not video.exists(): sys.exit("no video from any account (rate limits?) — rerun later")
    log("video", video)
    # when is each word said?
    from faster_whisper import WhisperModel
    wm = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=2, download_root=str(ROOT / "state/whisper-models"))
    segs, info = wm.transcribe(str(video), word_timestamps=True)
    heard = [(w.start, re.sub(r"[^a-z']", "", w.word.lower())) for sg in segs for w in sg.words]; dur = info.duration
    del wm
    res, pos = {}, 0
    for n, (i, b) in enumerate(words, 1):
        key = [re.sub(r"[^a-z']", "", x.lower()) for x in b["card"]["headline"].split()][:2]
        t = None
        for j in range(pos, len(heard) - len(key) + 1):
            if [h[1] for h in heard[j:j + len(key)]] == key: t, pos = heard[j][0], j + 1; break
        if t is None:                                           # not heard: spread evenly as a fallback
            t = dur * n / (len(words) + 1); log(f"beat {i}: '{' '.join(key)}' not heard -> fallback t={t:.1f}")
        best = None
        for k, dt in enumerate((1.0, 2.5, 4.0)):
            fr = out / f"nlmframe-{i:02d}-{k}.png"
            subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{min(t + dt, dur - 0.2):.2f}", "-i", str(video), "-frames:v", "1", str(fr)], check=True)
            o = subprocess.run([TTSPY, str(ROOT / "shorts/detext.py"), str(fr), str(out / f"pic-{i:02d}-{k}.png"), "--crop"],
                               capture_output=True, text=True).stdout
            ntext = len(re.findall(r"^text ", o, re.M))
            if best is None or ntext < best[0]: best = (ntext, k, t + dt)
        os.replace(out / f"pic-{i:02d}-{best[1]}.png", out / f"pic-{i:02d}.png")
        res[str(i)] = {"file": str((out / f"pic-{i:02d}.png").relative_to(ROOT)), "t": round(best[2], 2), "word": b["card"]["headline"], "text_boxes": best[0]}
        log(f"beat {i}: {b['card']['headline']} at {best[2]:.1f}s ({best[0]} text boxes removed)")
    json.dump(res, open(out / "pictures.json", "w"), indent=2)
    from PIL import Image
    ims = [Image.open(ROOT / r["file"]).resize((300, 300)) for r in res.values()]
    c = Image.new("RGB", (len(ims) * 310, 300), "white")
    for k, im in enumerate(ims): c.paste(im, (k * 310, 0))
    c.save(out / "contact.jpg", quality=85); log("done", out / "pictures.json")

if __name__ == "__main__": main(sys.argv[1])
