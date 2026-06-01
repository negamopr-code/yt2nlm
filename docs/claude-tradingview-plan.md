# Lean Claude × TradingView integration — implementation plan

> Knowledge base backing this plan:
> notebook **`a86ba710-142d-475f-afcd-49f251ae7080`** ("Claude × TradingView — integration"),
> 20 curated YouTube videos + their comment threads. Query it from the executing
> project per [`nlm-cross-project.md`](./nlm-cross-project.md).
>
> Status: **Validated against the full 20-video corpus** (40 sources). The
> "Corpus says" callouts are distilled from notebook queries, not invented.

## What the corpus actually recommends as "leanest" (headline)

The community's *leanest agentic* connection is **not** scraping or a custom data
API — it's an **MCP server that drives TradingView *Desktop* over the Chrome
DevTools Protocol (CDP, debug port 9222)**, set up via a **"one-shot setup
prompt"** in Claude Code (≈5 min) rather than hand-written JSON config. It streams
live chart data into Claude and injects Pine Script back. Requirement: Claude
Desktop + TradingView **Desktop** (not browser) + a Claude Pro/Max plan for token
budget. If you don't want the Desktop apps, the leanest *non-agentic* path is
still Job A below (Claude Code + Pine files). Pick by whether you want Claude
*in the live loop* (CDP/MCP) or just *authoring* (Pine files).

## The core fact that makes "lean" non-obvious

TradingView has **no official public order/data API**. Every integration is one of
three bridges, and "leanest" depends entirely on which job you're doing. Don't
pick a stack first — pick the *job*, then the thinnest bridge for it.

```
   ┌─────────────┐   author/refine    ┌──────────────┐
   │  Claude     │ ─── Pine Script ──▶ │ TradingView  │   (Job A: strategy authoring)
   │  (Code/API/ │ ◀── backtest pics ─ │  charts      │
   │   Desktop)  │                     └──────┬───────┘
   │             │                            │ alert() webhook (only TOS-clean egress)
   │             │ ◀── signal JSON ──── ┌─────▼───────┐
   │             │ ──── place order ──▶ │  broker API │   (Job B: signal→execution)
   └─────┬───────┘                      │ Alpaca/CCXT │
         │ MCP tools (get_quote/place_order)  └────────┘
         ▼
   (Job C: agentic — Claude in the live loop via an MCP server)
```

## Three jobs, leanest bridge for each

### Job A — Strategy authoring (no live money, leanest overall)
**Use when:** you want Claude to write/refine Pine Script and you backtest in TV.
**Leanest wiring:** Claude Code in a repo of `.pine` files. You paste backtest
results (or screenshots) back; Claude iterates. **Zero infrastructure, zero API
keys, zero standing process.** This is the lean default and where most of the
corpus's "insane results" actually live.
- Optional upgrade: a tiny MCP/CLI that pulls TV backtest data so Claude reads
  results without manual paste.
- **Corpus says:** creators push a **"one-shot setup prompt"** to configure the
  whole loop in ~5 min instead of manual JSON. Even the authoring flow trends
  toward driving TradingView Desktop via CDP so Claude can read indicators and
  inject Pine directly. Common friction from comments: token burn from
  high-frequency monitoring, and Claude **safety refusals** on anything framed as
  a live financial trade.

### Job B — Signal → execution (live, still lean)
**Use when:** a TV strategy should fire real (paper first) orders.
**Leanest wiring:** TradingView Pine `alert()` → **webhook** → a small always-on
receiver → broker API.
- Receiver: ~40-line FastAPI/Flask endpoint validating a shared secret, mapping
  the alert JSON to an order. Runs as its own container on this host (pattern:
  the existing `*-serve` containers) on a free port (8094/8095/8096), or a
  serverless function (Lambda) per the Part Time Larry video.
- Broker: **Alpaca** (paper+live, simplest REST) for US equities/crypto; **CCXT**
  for crypto exchanges; IBKR if you must.
- Claude's role: generate + maintain the receiver and the Pine alert payload.
- **Pitfalls to encode (from comments):** webhook auth/secret, idempotency on
  duplicate alerts, paper-trade first, TV alert payload size limits.
- **Corpus says:** brokers used are **Alpaca, BitGet, or Bybit**; hosting is
  **Railway** (24/7) or **AWS Lambda** (serverless); webhooks secured by a
  **randomized secret string validated server-side**, keys in `.env`. Documented
  breakages: Windows **MSIX TradingView blocks the remote debug port (9222)**,
  network sandboxing blocking outbound API calls, **LLM latency causing missed
  entry prices**, Lambda auth/permission errors, and **local cron jobs dying on
  laptop restart** (→ use an always-on host, not a laptop).

### Job C — Agentic, Claude in the live loop (most powerful, least lean)
**Use when:** you want Claude to *decide*, not just relay a Pine signal.
**Leanest wiring:** a **trading MCP server** exposing tools
(`get_quote`, `get_indicators`, `place_order`, `get_positions`); register it with
Claude Code / Claude Desktop. Claude reasons over tool outputs and acts.
- Data source behind the MCP server: a real data API (Alpaca/Polygon/yfinance) —
  *not* scraped TV — because TV has no clean read API. "TradingView" here means
  the indicators/strategy concept, computed server-side.
- Build vs borrow: Nicholas Renotte's "MCP server in 10 minutes for stock trading
  agents" is the canonical build; some community MCP servers exist to borrow.
- **Corpus says:** multiple creators ship MCP servers exposing **~78 tools**
  (Trades Don't Lie; Nicholas Renotte's **FastMCP SDK** example; Peter Müller's
  **MetaTrader 5** server; DaviddTech's Chrome-extension bridge). Tool surface:
  market data (`get_symbol_price` via Yahoo Finance or exchange APIs), execution
  (`open_buy_trade` / `open_sell_trade` / `close_position`), charting (switch
  symbol/timeframe, inject Pine, draw zones), reporting (`morning_brief` watchlist
  scans). Data comes from **live TradingView Desktop via CDP**, Yahoo Finance,
  broker APIs (Alpaca/BitGet/Bybit), or MT5 — i.e. confirmed: TradingView itself
  is driven through the Desktop app, not a data API.

## Recommended path (lean-first)

1. **Start at Job A** in a fresh repo: Claude Code + Pine files, backtest loop.
   Proves value with zero infra.
2. **Graduate to Job B** only once a strategy backtests well: add the webhook
   receiver container + Alpaca **paper** keys. Keep it ≤1 small service.
3. **Reach for Job C** only if you need Claude making live judgment calls — it's
   the heaviest (standing MCP server + live data + execution auth) and the corpus's
   skeptics (Algovibes) suggest "autonomous and profitable" is the hard part.

## Reality check (why the skeptical video is in the corpus)

The comment threads are the real signal here. Distilled corpus verdict:
**technical feasibility ≈ 8/10, investment reliability ≈ 2/10** — "treat Claude as
a junior analyst, not a portfolio manager." Specific warnings the corpus raises:

- **Grid/parameter overfitting** (Algovibes): viral strategies brute-force
  parameters to fit past data → great backtest, fails live.
- **LLM latency** is too slow for 1-minute candles; **hallucinations** are
  dangerous on options.
- **Copy-trading lag (30–45 days)** makes it useless.
- **API keys pasted into chat** expose accounts — never do it.
- **Paper trading hides slippage/fees/liquidity**, so even paper success is soft.
- Cynical-but-useful: "the real money is in selling courses, not the strategies."

Encode this honesty in whatever the executing project builds — **paper-trade gate
before any live key, forward-test before trusting any backtest, keep credentials
in `.env` (never in a prompt), and run on an always-on host (not a laptop cron).**

## How the executing project consumes this

The other project doesn't re-read these videos. It queries the notebook live:

```bash
export NLM_BIN=/home/node/patent-wiki-analyzer/.venv/bin/nlm
export NLM_NOTEBOOK=a86ba710-142d-475f-afcd-49f251ae7080
"$NLM_BIN" query notebook "$NLM_NOTEBOOK" \
  "What is the leanest way to send a TradingView alert to a broker for execution, and what do people say breaks?" --json
```

…ideally via a Haiku subagent returning only `.value.answer`. See
[`nlm-cross-project.md`](./nlm-cross-project.md).

## Execution checklist for the other project

- [ ] Record `NLM_NOTEBOOK=a86ba710-…` + `NLM_BIN=…` in that project's env/.nlm.
- [ ] Add a `kb.sh` (from the cross-project doc) for ad-hoc KB queries.
- [ ] Pick the Job — default A; choose C (CDP/MCP) only if you have Claude Desktop
      + TradingView **Desktop** and want Claude in the live loop.
- [ ] Job A: repo of Pine files + Claude Code loop (zero infra).
- [ ] Job B: webhook receiver on an **always-on host** (own container, free port
      8094+) or Railway/Lambda; **Alpaca paper** first; secret-string auth; keys in `.env`.
- [ ] Job C: MCP trading server — borrow an existing ~78-tool one (Trades Don't
      Lie) or build with **FastMCP** (Renotte); drive TradingView Desktop over CDP
      (debug port 9222); register with Claude. Watch the Windows MSIX port-9222 block.
- [ ] Try the **one-shot setup prompt** before hand-writing MCP JSON config.
- [ ] **Paper-trade gate** before any live credential; **never paste API keys into a prompt**.
