#!/usr/bin/env python3
"""Build a faceless, AWF-branded YouTube Short from one JSON "unit".

  .nlmvenv/bin/python shorts/build_short.py shorts/units/ep01.json  -> state/shorts/<id>/final.mp4

unit = {id, series, episode, voice, rate, slides:[{type, speech, ...}]}
slide types: text{headline, sub?} · curve{headline, points:[[label,pct_forgotten]], source}
             word{word, pos, meaning, example, register} · cta{headline, sub}
Brand (user rule 2026-09-27): the real anotherwordfor.net logo (state/brand/awf-logo-channel.jpg)
on every frame, never a NotebookLM mark. Light warm theme = the channel's legacy look.
"""
import asyncio, html, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FFMPEG = "/workspace/glottos-auto/node_modules/ffmpeg-static/ffmpeg"
LOGO = ROOT / "state/brand/awf-logo-channel.jpg"
W, H = 1080, 1920
C = {"bg": "#FAF7F2", "ink": "#1F1A17", "muted": "#6B625B", "accent": "#705246", "hot": "#E4572E", "blue": "#1E6FE8"}

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:{C['bg']};color:{C['ink']};font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;
     display:flex;flex-direction:column;padding:120px 150px 400px 84px}}
.top{{display:flex;align-items:center;gap:22px}} .top img{{width:96px;height:96px;border-radius:18px}}
.brand{{font-size:40px;font-weight:700;color:{C['accent']};letter-spacing:.5px}}
.pill{{margin-top:44px;align-self:flex-start;background:{C['accent']};color:#fff;font-size:30px;font-weight:700;
       letter-spacing:3px;padding:14px 26px;border-radius:40px}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px}}
h1{{font-size:92px;line-height:1.08;font-weight:800;letter-spacing:-1px}}
h1 em{{font-style:normal;color:{C['hot']}}}
.sub{{font-size:46px;line-height:1.3;color:{C['muted']}}}
.card{{background:#fff;border-radius:36px;padding:56px;box-shadow:0 18px 50px rgba(60,40,20,.12);display:flex;flex-direction:column;gap:26px}}
.word{{font-size:110px;font-weight:800;color:{C['blue']}}} .pos{{font-size:40px;color:{C['muted']}}}
.ex{{font-size:52px;line-height:1.3;border-left:10px solid {C['hot']};padding-left:30px}}
.reg{{align-self:flex-start;font-size:32px;font-weight:700;color:{C['accent']};border:3px solid {C['accent']};border-radius:30px;padding:8px 22px}}
.src{{font-size:30px;color:{C['muted']}}}
.foot{{font-size:34px;color:{C['muted']}}}
"""

def mark(t):  # *word* -> highlighted
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(t))

def curve_svg(points):
    # points: [[label, pct_forgotten]] ; retention = 100 - pct
    pw, ph, x0, y0 = 846, 700, 30, 90          # fits the 846px safe content width
    xs = [x0 + i * (pw - x0 - 90) / (len(points)) for i in range(len(points) + 1)]
    ys = [y0 + (ph - 140) * (1 - r / 100) for r in [100] + [100 - p for _, p in points]]
    path = " ".join(f"{'M' if i == 0 else 'L'}{xs[i]:.0f},{ys[i]:.0f}" for i in range(len(xs)))
    dots = "".join(f'<circle cx="{xs[i+1]:.0f}" cy="{ys[i+1]:.0f}" r="14" fill="{C["hot"]}"/>'
                   f'<text x="{xs[i+1]:.0f}" y="{ys[i+1]-34:.0f}" font-size="40" font-weight="800" text-anchor="middle" fill="{C["hot"]}">−{p}%</text>'
                   f'<text x="{xs[i+1]:.0f}" y="{ph-50}" font-size="32" text-anchor="middle" fill="{C["muted"]}">{html.escape(l)}</text>'
                   for i, (l, p) in enumerate(points))
    return (f'<svg width="{pw}" height="{ph}" viewBox="0 0 {pw} {ph}"><line x1="{x0}" y1="{ph-100}" x2="{pw-10}" y2="{ph-100}" stroke="#d9d0c7" stroke-width="4"/>'
            f'<text x="{x0}" y="{y0-40}" font-size="32" fill="{C["muted"]}">100% = what you learned</text>'
            f'<path d="{path}" fill="none" stroke="{C["blue"]}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>{dots}</svg>')

def slide_html(u, s):
    body = ""
    if s["type"] == "text":
        body = f'<h1>{mark(s["headline"])}</h1>' + (f'<div class="sub">{mark(s["sub"])}</div>' if s.get("sub") else "")
    elif s["type"] == "curve":
        body = f'<h1 style="font-size:72px">{mark(s["headline"])}</h1>{curve_svg(s["points"])}<div class="src">{html.escape(s.get("source",""))}</div>'
    elif s["type"] == "word":
        body = (f'<div class="sub">{mark(s.get("lead","Learn it like this:"))}</div><div class="card"><div class="word">{html.escape(s["word"])}</div>'
                f'<div class="pos">{html.escape(s["pos"])} · {html.escape(s["meaning"])}</div><div class="ex">“{html.escape(s["example"])}”</div>'
                f'<div class="reg">{html.escape(s["register"])}</div></div>')
    elif s["type"] == "cta":
        body = f'<h1 style="font-size:80px">{mark(s["headline"])}</h1><div class="sub">{mark(s.get("sub",""))}</div>'
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="top"><img src="file://{LOGO}"><div class="brand">anotherwordfor.net</div></div>'
            f'<div class="pill">{html.escape(u["series"].upper())} · EP {u["episode"]}</div>'
            f'<div class="main">{body}</div><div class="foot">{html.escape(s.get("foot","Save this · follow for the next word"))}</div></body></html>')

def dur(path):
    r = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True)
    h, m, sec = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).groups()
    return int(h) * 3600 + int(m) * 60 + float(sec)

async def tts(text, voice, rate, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate).save(str(out))

def main(unit_path):
    u = json.load(open(unit_path)); out = ROOT / "state/shorts" / u["id"]; out.mkdir(parents=True, exist_ok=True)
    segs = []
    for i, s in enumerate(u["slides"], 1):
        h = out / f"s{i:02d}.html"; png = out / f"s{i:02d}.png"; mp3 = out / f"s{i:02d}.mp3"; seg = out / f"s{i:02d}.mp4"
        h.write_text(slide_html(u, s))
        subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--allow-file-access-from-files", f"--window-size={W},{H}", f"--screenshot={png}", f"file://{h}"],
                       capture_output=True, timeout=120)
        asyncio.run(tts(s["speech"], u.get("voice", "en-US-ChristopherNeural"), u.get("rate", "+8%"), mp3))
        d = dur(mp3) + 0.45
        subprocess.run([FFMPEG, "-y", "-loop", "1", "-i", str(png), "-i", str(mp3), "-t", f"{d:.2f}",
                        "-vf", f"scale={W}:{H},zoompan=z='min(zoom+0.0006,1.04)':d=1:s={W}x{H}:fps=30,format=yuv420p",
                        "-af", "apad", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                        "-ar", "44100", "-ac", "2", "-shortest", str(seg)], capture_output=True, check=True)
        segs.append(seg); print(f"slide {i}: {d:.1f}s", flush=True)
    lst = out / "segs.txt"; lst.write_text("".join(f"file '{p}'\n" for p in segs))
    final = out / "final.mp4"
    subprocess.run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(final)],
                   capture_output=True, check=True)
    print(f"FINAL {final} {dur(final):.1f}s", flush=True)

if __name__ == "__main__":
    main(sys.argv[1])
