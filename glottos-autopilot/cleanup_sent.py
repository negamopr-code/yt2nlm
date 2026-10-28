#!/usr/bin/env python3
"""Delete local video files of everything already on YouTube (user 2026-10-18: "you need a script or something which clean up the
videos which are already sent to youtube. Meaning no videos should be stored in our local memory or container if we already have
sent video to youtube"). No Claude.

SENT = out/yt/status.json says the video has a YouTube id and its state is public / scheduled / private (truth = yt-studio uploads
ledger + channel snapshot, built by yt_sendq.py). "deleted" on YouTube is NOT sent: its file stays so it can be uploaded again.
For each sent video:
  1. its full status record goes into out/yt/sent-archive.json (yt_sendq.py keeps listing archived videos, so the Videos tab, the
     lab's local-id -> YouTube-id link and the send controller lose nothing);
  2. deleted: out/<vid>.mp4, its -hd1440 sibling / original, out/.hd/<vid>.mp4, and in state/shorts/<unit>/ every video and audio
     file (*.mp4 *.webm *.mov *.wav *.m4a *.mp3 *.aac) and the frames/ folder (render stills);
  3. kept: pictures (pic-NN.png are reused by the long-video builder), thumbnails, json, txt - small, and not videos.
Safety: nothing younger than 30 min, nothing while an upload runs, only states listed above, a dry run unless --apply.
  python3 cleanup_sent.py            # dry run: what would go, and how much space
  python3 cleanup_sent.py --apply    # delete
"""
import glob, json, os, shutil, subprocess, sys, time

OUT = "/workspace/glottos-auto/out"; STATE = "/workspace/glottos-marketing/state/shorts"
ST = f"{OUT}/yt/status.json"; ARCH = f"{OUT}/yt/sent-archive.json"
SENT = {"public", "scheduled", "private"}
MEDIA = ("*.mp4", "*.webm", "*.mov", "*.wav", "*.m4a", "*.mp3", "*.aac")
APPLY = "--apply" in sys.argv


def jload(p, d):
    try: return json.load(open(p))
    except Exception: return d


def jsave(p, o):
    t = p + ".tmp"; json.dump(o, open(t, "w"), indent=1, ensure_ascii=False); os.replace(t, p)


def size(p):
    if os.path.isdir(p):
        return sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(p) for f in fs if os.path.isfile(os.path.join(dp, f)))
    return os.path.getsize(p) if os.path.exists(p) else 0


def busy():
    # [u]/[p] brackets: the pattern must not match this check's own "sh -c" command line (it did: always "busy")
    return subprocess.run("pgrep -f 'yt-studio.*[u]pload.py|\\.hd/.*[p]art.mp4' >/dev/null || docker exec yt-studio pgrep -f '[u]pload.py' >/dev/null",
                          shell=True).returncode == 0


def main():
    if busy():
        print("cleanup: an upload is running - skipped"); return
    st = jload(ST, {"videos": []}); arch = jload(ARCH, {}); now = time.time()
    _j = jload(f"{OUT}/yt/jobs.json", {}); jobs = {x.get("vid"): x for x in (_j.values() if isinstance(_j, dict) else _j)}
    targets, freed, n = [], 0, 0
    for v in st.get("videos", []):
        y = v.get("youtube") or {}
        if v.get("archived") or not y.get("id") or y.get("state") not in SENT: continue
        vid = v["vid"]; base = vid[:-len("-hd1440")] if vid.endswith("-hd1440") else vid
        # 2026-10-28 (h116): a send whose job ended "failed" (upload half-done, never on the channel) still had state "private" from the
        # uploads ledger -> its only copy was deleted. Keep the file unless the send job finished (or there is no job record at all).
        j = jobs.get(base) or jobs.get(vid)
        if j and j.get("status") != "done": continue
        files = [f"{OUT}/{base}.mp4", f"{OUT}/{base}-hd1440.mp4", f"{OUT}/.hd/{base}.mp4", f"{OUT}/.hd/{base}-hd1440.mp4"]
        unit = f"{STATE}/{os.path.basename(base)}"
        if os.path.isdir(unit):
            files += [p for pat in MEDIA for p in glob.glob(f"{unit}/{pat}")]
            if os.path.isdir(f"{unit}/frames"): files.append(f"{unit}/frames")
        files = [p for p in dict.fromkeys(files) if os.path.exists(p)]
        if any(now - os.path.getmtime(p) < 1800 for p in files): continue        # still being written / just rendered
        if not files: continue
        rec = dict(v); rec.update(archived=True, archived_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        targets.append((vid, y, rec, files))
    for vid, y, rec, files in targets:
        s = sum(size(p) for p in files); freed += s; n += 1
        print(f"{'DELETE' if APPLY else 'would delete'} {vid} ({y['state']} {y['id']}): {len(files)} item(s), {s / 1e6:.0f} MB")
        if APPLY:
            arch[vid] = rec; jsave(ARCH, arch)                                     # archive first, then delete
            for p in files:
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    print(f"cleanup: {n} sent video(s), {freed / 1e9:.2f} GB {'freed' if APPLY else 'would be freed (dry run, add --apply)'}")


if __name__ == "__main__":
    main()
