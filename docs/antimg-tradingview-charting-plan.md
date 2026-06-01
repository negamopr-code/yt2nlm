# Antimartingale × TradingView charts — backtest replay plan (copy into antimartingale-studio)

**Goal:** feed real OHLC into the coin-flip/options backtest and **render the
result on a TradingView chart with trade markers** (cycle entry / pyramid step /
loss-reset / target-win) + an equity (bank) curve.

**Key decision (read first):** TradingView has *no headless data API*, and the
"Claude-drives-TradingView-Desktop over CDP" path needs a GUI desktop the
antimg container doesn't have. So we **do not** use TradingView for data. We use:
- **Data:** `ccxt` (crypto, no key) or `stooq` (equities, no key) — headless, free.
- **Chart:** **TradingView Lightweight Charts** (their free open-source JS lib) —
  renders *our* candles + *our* markers. (The current TV widget iframe shows TV's
  own data and cannot overlay our trades; this replaces it for backtest views.)

```
ccxt/stooq ──▶ fetch_ohlc() ──▶ run_call_coinflip(prices) ──▶ events
                   │                                              │
        GET /api/backtest/chart  ◀──── markers_from_events() ◀────┘
                   │  returns { candles, markers, bank, summary }
                   ▼
        Lightweight Charts (candles + setMarkers + bank line)
```

### Assumptions to verify against your tree (adjust paths if different)
- Engine lives in `src/antimg/` (e.g. `options.py: run_call_coinflip`).
- FastAPI app object is importable (e.g. `src/antimg/web/app.py: app` or
  `src/antimg/api/app.py`). The web frontend is static HTML/JS served by FastAPI.
- The engine can emit a **per-cycle event log** with bar indices. If it currently
  returns only `final_bank`, Step 2 adds a tiny recording wrapper — no rewrite.

---

## Step 0 — deps

`requirements.txt` (or pyproject): add
```
ccxt>=4.0
```
`stooq` needs nothing (plain CSV over HTTP via stdlib). Reinstall into the
**persisted** venv and add to `scripts/restore.sh` so a rebuild restores it:
```bash
.venv/bin/pip install ccxt
```
Frontend lib is loaded from CDN (Step 4) — no npm needed. Cache dir (Step 1) must
be gitignored: add `data/cache/` to `.gitignore`.

---

## Step 1 — data adapter  `src/antimg/data/ohlc.py`

```python
"""Headless OHLC fetch for backtests. ccxt (crypto) or stooq (equities), no keys.
Returns candles as dicts with UNIX-second `time` (Lightweight Charts native)."""
from __future__ import annotations

import csv
import io
import json
import os
import time
import urllib.request
from dataclasses import dataclass, asdict

CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "cache")
CACHE_TTL = 3600  # seconds; backtests don't need fresher than this


@dataclass
class Candle:
    time: int          # UNIX seconds, UTC
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


def _cache_path(key: str) -> str:
    os.makedirs(CACHE_DIR, exist_ok=True)
    safe = "".join(c if c.isalnum() else "_" for c in key)
    return os.path.join(CACHE_DIR, f"{safe}.json")


def _cached(key: str):
    p = _cache_path(key)
    if os.path.exists(p) and (time.time() - os.path.getmtime(p)) < CACHE_TTL:
        with open(p, encoding="utf-8") as fh:
            return [Candle(**c) for c in json.load(fh)]
    return None


def _store(key: str, candles: list[Candle]):
    with open(_cache_path(key), "w", encoding="utf-8") as fh:
        json.dump([asdict(c) for c in candles], fh)


def _from_ccxt(symbol: str, timeframe: str, limit: int) -> list[Candle]:
    import ccxt
    ex = ccxt.binance({"enableRateLimit": True})
    rows = ex.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)  # [[ms,o,h,l,c,v],...]
    return [Candle(int(ms // 1000), o, h, l, c, v) for ms, o, h, l, c, v in rows]


def _from_stooq(symbol: str, limit: int) -> list[Candle]:
    # daily only; symbol e.g. "aapl.us", "spy.us", "^spx"
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
    with urllib.request.urlopen(url, timeout=30) as r:
        text = r.read().decode("utf-8")
    out: list[Candle] = []
    for row in csv.DictReader(io.StringIO(text)):
        if not row.get("Close"):
            continue
        t = int(time.mktime(time.strptime(row["Date"], "%Y-%m-%d")))
        out.append(Candle(t, float(row["Open"]), float(row["High"]),
                          float(row["Low"]), float(row["Close"]),
                          float(row.get("Volume") or 0)))
    return out[-limit:] if limit else out


def fetch_ohlc(symbol: str, timeframe: str = "1d", limit: int = 500,
               source: str = "ccxt") -> list[Candle]:
    key = f"{source}-{symbol}-{timeframe}-{limit}"
    hit = _cached(key)
    if hit is not None:
        return hit
    if source == "ccxt":
        candles = _from_ccxt(symbol, timeframe, limit)
    elif source == "stooq":
        candles = _from_stooq(symbol, limit)
    else:
        raise ValueError(f"unknown source {source!r}")
    candles.sort(key=lambda c: c.time)
    _store(key, candles)
    return candles
```

> **Yahoo note:** do *not* default to yfinance — Yahoo 429s this host's server IP
> (known incident). ccxt/stooq avoid it.

---

## Step 2 — backtest → markers  `src/antimg/charting/markers.py`

Lightweight Charts marker shape:
`{ time, position: 'aboveBar'|'belowBar'|'inBar', color, shape:
'arrowUp'|'arrowDown'|'circle'|'square', text }`, **sorted ascending by time**.

Map the coin-flip pyramid lifecycle to markers:

| Event | position | shape | color | text |
|---|---|---|---|---|
| cycle entry | belowBar | arrowUp | `#2962FF` | `C{n} b={b}` |
| pyramid step (win in-cycle) | aboveBar | circle | `#26a69a` | `×2 s{k}` |
| loss / reset | belowBar | arrowDown | `#ef5350` | `loss −b` |
| target streak hit (win) | aboveBar | square | `#f0b90b` | `WIN +{payout}` |

```python
"""Turn a backtest event log into Lightweight-Charts markers + a bank curve.

The engine must yield events as dicts: {bar, kind, ...} where
  kind ∈ {"entry","step","loss","win"} and `bar` is the candle index.
If run_call_coinflip already returns a trade/cycle log, adapt `simulate_with_events`
to read it. Otherwise pass a `record` callback into the engine (see note)."""
from __future__ import annotations

_STYLE = {
    "entry": ("belowBar", "arrowUp", "#2962FF"),
    "step":  ("aboveBar", "circle", "#26a69a"),
    "loss":  ("belowBar", "arrowDown", "#ef5350"),
    "win":   ("aboveBar", "square", "#f0b90b"),
}


def markers_from_events(events: list[dict], candles: list) -> list[dict]:
    out = []
    n = len(candles)
    for e in events:
        i = max(0, min(e["bar"], n - 1))
        pos, shape, color = _STYLE[e["kind"]]
        out.append({
            "time": candles[i].time,
            "position": pos, "shape": shape, "color": color,
            "text": e.get("text", e["kind"]),
        })
    out.sort(key=lambda m: m["time"])
    return out


def simulate_with_events(candles: list, *, b: float, target_streak: int,
                         p: float | None = None, **engine_kw) -> dict:
    """Wrap the existing engine and collect events + bank curve.

    ADAPT THIS to your real engine. Two ways:
    A) If run_call_coinflip already returns a list of cycles/trades with bar
       indices, translate each into {bar, kind, text} here.
    B) If it only returns final_bank, add a `record=events.append` hook in the
       engine at: cycle-open, each win (step), each loss (reset), each target-win.
    The bank curve is bank value sampled at each event's bar.
    """
    from antimg.options import run_call_coinflip  # ADAPT import/name

    events: list[dict] = []
    closes = [c.close for c in candles]

    # --- EXAMPLE shape; replace body with your engine's real call/return ---
    result = run_call_coinflip(closes, base_bet=b, target_streak=target_streak,
                               p=p, record=events.append, **engine_kw)
    # result expected to carry .final_bank and a bank-by-bar series; adapt:
    bank_series = getattr(result, "bank_curve", None) or []
    bank = [{"time": candles[min(i, len(candles) - 1)].time, "value": v}
            for i, v in bank_series]

    markers = markers_from_events(events, candles)
    summary = {
        "final_bank": getattr(result, "final_bank", None),
        "cycles": sum(1 for e in events if e["kind"] == "entry"),
        "wins": sum(1 for e in events if e["kind"] == "win"),
        "losses": sum(1 for e in events if e["kind"] == "loss"),
    }
    return {"markers": markers, "bank": bank, "summary": summary}
```

> **If the engine returns only a number today:** add a `record=None` kwarg and, at
> the four lifecycle points, call `if record: record({"bar": i, "kind": "...",
> "text": "..."})`. That's the whole change — no logic rewrite, fully backward
> compatible (default `record=None` ⇒ old behaviour, tests stay green).

---

## Step 3 — FastAPI endpoint  `src/antimg/web/routes_chart.py`

```python
from dataclasses import asdict
from fastapi import APIRouter, HTTPException

from antimg.data.ohlc import fetch_ohlc
from antimg.charting.markers import simulate_with_events

router = APIRouter(prefix="/api/backtest", tags=["backtest-chart"])


@router.get("/chart")
def backtest_chart(symbol: str = "BTC/USDT", timeframe: str = "1d",
                   limit: int = 500, source: str = "ccxt",
                   b: float = 1.0, target_streak: int = 3, p: float = 0.5):
    try:
        candles = fetch_ohlc(symbol, timeframe, limit, source)
    except Exception as exc:  # network/source failure → 502, not 500
        raise HTTPException(502, f"data fetch failed: {exc}")
    if not candles:
        raise HTTPException(404, "no candles for symbol")
    sim = simulate_with_events(candles, b=b, target_streak=target_streak, p=p)
    return {
        "candles": [asdict(c) for c in candles],
        "markers": sim["markers"],
        "bank": sim["bank"],
        "summary": sim["summary"],
    }
```

Wire it in your app factory (next to existing routers):
```python
from antimg.web.routes_chart import router as chart_router
app.include_router(chart_router)
```

---

## Step 4 — frontend  (Lightweight Charts v4, pinned)

Add a panel to the existing web page (vanilla JS — works regardless of framework).
**Pin v4**: v5 renamed the series/marker API.

```html
<!-- in your <head> or before your script -->
<script src="https://unpkg.com/lightweight-charts@4.2.3/dist/lightweight-charts.standalone.production.js"></script>

<div id="bt-controls">
  <input id="bt-symbol" value="BTC/USDT">
  <select id="bt-source"><option value="ccxt">ccxt</option><option value="stooq">stooq</option></select>
  <input id="bt-tf" value="1d"><input id="bt-N" type="number" value="3" min="1">
  <button id="bt-run">Run backtest</button>
  <span id="bt-summary"></span>
</div>
<div id="bt-chart" style="height:460px"></div>

<script>
const el = document.getElementById('bt-chart');
const chart = LightweightCharts.createChart(el, {
  height: 460, autoSize: true,
  layout: { background: { color: '#0e1117' }, textColor: '#d1d4dc' },
  grid: { vertLines: { color: '#1c1f26' }, horzLines: { color: '#1c1f26' } },
  rightPriceScale: { borderColor: '#2a2e39' },
  timeScale: { borderColor: '#2a2e39', timeVisible: true },
});
const candleSeries = chart.addCandlestickSeries({
  upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
  wickUpColor: '#26a69a', wickDownColor: '#ef5350',
});
const bankSeries = chart.addLineSeries({
  priceScaleId: 'left', color: '#f0b90b', lineWidth: 2, title: 'bank',
});
chart.priceScale('left').applyOptions({ visible: true, borderColor: '#2a2e39' });

async function run() {
  const symbol = encodeURIComponent(document.getElementById('bt-symbol').value);
  const source = document.getElementById('bt-source').value;
  const tf = encodeURIComponent(document.getElementById('bt-tf').value);
  const N = document.getElementById('bt-N').value;
  const r = await fetch(`/api/backtest/chart?symbol=${symbol}&source=${source}&timeframe=${tf}&target_streak=${N}`);
  if (!r.ok) { document.getElementById('bt-summary').textContent = 'error ' + r.status; return; }
  const d = await r.json();
  candleSeries.setData(d.candles);     // {time,open,high,low,close}
  candleSeries.setMarkers(d.markers);  // sorted ascending by time (backend guarantees)
  bankSeries.setData(d.bank);          // [{time,value}]
  chart.timeScale().fitContent();
  const s = d.summary;
  document.getElementById('bt-summary').textContent =
    `final bank ${s.final_bank} · ${s.cycles} cycles · ${s.wins}W/${s.losses}L`;
}
document.getElementById('bt-run').addEventListener('click', run);
run();
</script>
```

**React variant (if the frontend is React):** create the chart in a
`useEffect(() => { ... return () => chart.remove(); }, [])`, keep
`candleSeries`/`bankSeries` in refs, and call `setData`/`setMarkers` when the
fetch resolves. Same v4 API.

> Keep the existing TradingView **widget iframe** if you want a live TV view; this
> Lightweight-Charts panel is the *backtest replay* (your data + your markers).
> They coexist — different jobs.

---

## Step 5 — tests  `tests/test_chart.py`

```python
from antimg.data.ohlc import Candle
from antimg.charting.markers import markers_from_events


def _candles(n=5):
    return [Candle(time=1700000000 + i * 86400, open=1, high=2, low=0.5,
                   close=1 + i, volume=0) for i in range(n)]


def test_markers_shape_and_sorted():
    c = _candles()
    ev = [{"bar": 0, "kind": "entry", "text": "C1"},
          {"bar": 2, "kind": "step"}, {"bar": 3, "kind": "loss"},
          {"bar": 4, "kind": "win", "text": "WIN"}]
    m = markers_from_events(ev, c)
    assert [x["time"] for x in m] == sorted(x["time"] for x in m)
    assert m[0]["shape"] == "arrowUp" and m[0]["position"] == "belowBar"
    assert {x["shape"] for x in m} == {"arrowUp", "circle", "arrowDown", "square"}


def test_markers_clamp_out_of_range_bar():
    c = _candles(3)
    m = markers_from_events([{"bar": 99, "kind": "win"}], c)
    assert m[0]["time"] == c[-1].time  # clamped, no IndexError


def test_endpoint_shape(monkeypatch):
    from fastapi.testclient import TestClient
    from antimg.web.app import app          # ADAPT import
    import antimg.web.routes_chart as rc
    monkeypatch.setattr(rc, "fetch_ohlc", lambda *a, **k: _candles())
    monkeypatch.setattr(rc, "simulate_with_events",
                        lambda *a, **k: {"markers": [], "bank": [],
                                         "summary": {"final_bank": 0, "cycles": 0,
                                                     "wins": 0, "losses": 0}})
    r = TestClient(app).get("/api/backtest/chart?symbol=BTC/USDT")
    assert r.status_code == 200
    body = r.json()
    assert {"candles", "markers", "bank", "summary"} <= body.keys()
    assert len(body["candles"]) == 5
```

---

## Step 6 — verify & ship (antimg autonomous loop)

```bash
.venv/bin/pip install ccxt
.venv/bin/python -c "from antimg.data.ohlc import fetch_ohlc; print(len(fetch_ohlc('BTC/USDT','1d',50)))"
.venv/bin/pytest -q                          # existing 51 + 3 new = green
# rebuild/redeploy antimg-web (8090) so the panel is live; do NOT bind 8080
```
- Add to `scripts/restore.sh`: `pip install ccxt`.
- `.gitignore`: `data/cache/`.
- Commit + push to `github.com/negamopr-code/antimartingale-studio`; log + DECISIONS entry; update `antimartingal_next_session_entrypoint.md`.

---

## Caveats (carry these into the build)
- **No TradingView data dependency** — by design (headless container can't run TV
  Desktop/CDP). If you ever *must* have TV's exact series, `tvdatafeed` (websocket
  login) works headless but is unofficial/fragile/ToS-gray — not the foundation.
- **Pin Lightweight Charts v4** (`@4.2.3`). On v5, `addCandlestickSeries()` →
  `addSeries(LightweightCharts.CandlestickSeries, …)` and `series.setMarkers()` →
  `createSeriesMarkers(series, …)`. Don't float the version.
- **Marker time type must match candle time type** and be **sorted ascending**
  (backend guarantees both).
- **ccxt symbols** use `BASE/QUOTE` (`BTC/USDT`); **stooq** uses `aapl.us`,
  `spy.us`, `^spx` and is **daily only**.
- Engine change is additive (`record=None` default) — backward compatible, keeps
  the 51 tests green.
- Optional cross-project assist: from the antimg session you can query the KB
  notebook `a86ba710-142d-475f-afcd-49f251ae7080` for any TV-charting specifics
  (see `nlm-cross-project.md`).
```
