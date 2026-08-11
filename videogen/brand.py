"""Brand kit: palette extracted from the channel's old videos + safe defaults."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from .config import FFMPEG, REPORTS, STATE_DIR

BRAND_VIDEOS = ["nRk0gf1RscE", "qjC7HOeoi2E"]     # old "Another Word For …"
FONT_HEAD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_BODY = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

DEFAULT_BRAND = {
    "bg": "#101d2e", "card": "#1a2c44", "accent": "#3fa7f5",
    "text": "#f2f6fa", "muted": "#8fa3b8",
    "register": {"formal": "#7c5cff", "informal": "#ff9d3f", "neutral": "#3fa7f5"},
    "font_head": FONT_HEAD, "font_body": FONT_BODY,
    "watermark": "anotherwordfor.net",
}


def load_brand() -> dict:
    p = STATE_DIR / "videogen.brand.json"
    if p.exists():
        return {**DEFAULT_BRAND, **json.loads(p.read_text())}
    return dict(DEFAULT_BRAND)


def extract(scratch: Path) -> dict:
    """Download old videos, grab frames, k-means the palette."""
    import numpy as np
    from PIL import Image

    frames_dir = REPORTS / "brand"
    frames_dir.mkdir(parents=True, exist_ok=True)
    pixels = []
    for vid in BRAND_VIDEOS:
        mp4 = scratch / f"{vid}.mp4"
        if not mp4.exists():
            subprocess.run(
                ["/workspace/.venv/bin/yt-dlp", "-q", "-f", "18/best[height<=360]",
                 "-o", str(mp4), f"https://www.youtube.com/watch?v={vid}"],
                check=True)
        for t in ("2", "20", "40"):
            png = frames_dir / f"{vid}_{t}s.png"
            subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                            "-ss", t, "-i", str(mp4), "-frames:v", "1",
                            str(png)], check=True)
            if png.exists():
                im = Image.open(png).convert("RGB").resize((160, 90))
                pixels.append(np.asarray(im).reshape(-1, 3))
    if not pixels:
        raise RuntimeError("no frames extracted")
    data = np.concatenate(pixels).astype(float)
    # tiny k-means (k=5)
    rng = np.random.default_rng(7)
    cents = data[rng.choice(len(data), 5, replace=False)]
    for _ in range(12):
        d2 = ((data[:, None, :] - cents[None, :, :]) ** 2).sum(-1)
        lab = d2.argmin(1)
        for k in range(5):
            if (lab == k).any():
                cents[k] = data[lab == k].mean(0)
    counts = [(lab == k).sum() for k in range(5)]
    order = sorted(range(5), key=lambda k: -counts[k])
    hexes = ["#%02x%02x%02x" % tuple(int(c) for c in cents[k]) for k in order]

    def lum(h):
        r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
        return 0.299 * r + 0.587 * g + 0.114 * b

    brand = dict(DEFAULT_BRAND)
    darks = [h for h in hexes if lum(h) < 100]
    brights = [h for h in hexes if 100 <= lum(h) < 220]
    if darks:
        brand["bg"] = darks[0]
    if brights:
        brand["accent"] = brights[0]
    brand["palette"] = hexes
    (STATE_DIR / "videogen.brand.json").write_text(
        json.dumps(brand, indent=2))
    print(f"brand: palette {hexes} -> bg {brand['bg']} accent {brand['accent']}; "
          f"frames in {frames_dir} for review")
    return brand
