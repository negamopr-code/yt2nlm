"""edge-tts narration: one call per slide (per-slide WAV = natural sync)."""

from __future__ import annotations

import asyncio
import subprocess
import sys
import time
import wave
from pathlib import Path

from .config import FFMPEG, REPORTS

SAMPLE_VOICES = ["en-US-ChristopherNeural", "en-US-JennyNeural",
                 "en-GB-RyanNeural"]


def _tts_once(text: str, voice: str, rate: str, mp3_path: Path) -> None:
    import edge_tts

    async def go():
        await edge_tts.Communicate(text, voice, rate=rate).save(str(mp3_path))
    asyncio.run(go())


def synth(text: str, voice: str, rate: str, out_wav: Path) -> float:
    """TTS -> 44.1kHz stereo WAV. Returns duration in seconds."""
    mp3 = out_wav.with_suffix(".mp3")
    for attempt in range(3):
        try:
            _tts_once(text, voice, rate, mp3)
            break
        except Exception as exc:
            if attempt == 2:
                raise
            print(f"  tts retry ({exc})", file=sys.stderr)
            time.sleep(3)
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                    "-i", str(mp3), "-ar", "44100", "-ac", "2",
                    "-c:a", "pcm_s16le", str(out_wav)], check=True)
    mp3.unlink(missing_ok=True)
    with wave.open(str(out_wav)) as w:
        return w.getnframes() / w.getframerate()


def synth_slides(slides: list[dict], voice: str, rate: str,
                 audio_dir: Path) -> list[float]:
    audio_dir.mkdir(parents=True, exist_ok=True)
    durs = []
    for i, sl in enumerate(slides):
        out = audio_dir / f"slide{i:02d}.wav"
        if out.exists():                       # resume-safe
            with wave.open(str(out)) as w:
                durs.append(w.getnframes() / w.getframerate())
            continue
        durs.append(synth(sl["speech"], voice, rate, out))
        print(f"  tts {i + 1}/{len(slides)}: {durs[-1]:.1f}s")
    return durs


def make_samples(script: dict, rate: str = "+0%") -> list[Path]:
    """Same script through the sample voices -> reports/videogen/samples/."""
    d = REPORTS / "samples"
    d.mkdir(parents=True, exist_ok=True)
    text = " ... ".join(sl["speech"] for sl in script["slides"][:5])
    out = []
    for v in SAMPLE_VOICES:
        wav = d / f"{v}.wav"
        dur = synth(text, v, rate, wav)
        mp3 = d / f"{v}.mp3"
        subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y",
                        "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "128k",
                        str(mp3)], check=True)
        wav.unlink()
        print(f"  sample {v}: {dur:.0f}s -> {mp3}")
        out.append(mp3)
    return out
