# Connecting any project to a NotebookLM knowledge base

This repo (`yt2nlm`) builds NotebookLM notebooks from YouTube/Reddit/URL sources.
Once a notebook exists, **any other project on this host can read it as a
queryable knowledge base** — with zero install and zero re-auth. This document
is the contract for doing that.

## The mental model: the notebook ID *is* the connection string

There is no per-project database to provision. The whole system is account-global:

| Thing | Where it lives | Shared? |
|---|---|---|
| NotebookLM account | Google `bbubu2748@gmail.com` | one account holds **all** notebooks |
| Auth profile | `~/.notebooklm-mcp-cli/auth.json` | **persistent bind mount** (`persistent/nlm-profile`), shared by every project in the container, survives rebuilds |
| `nlm` CLI binary (v0.6.10) | `/home/node/patent-wiki-analyzer/.venv/bin/nlm` | persistent bind mount, callable from anywhere |
| A specific knowledge base | a notebook **UUID** | the *only* thing a consuming project needs to know |

So "connect project X to NotebookLM database Y" reduces to: **give project X the
notebook UUID.** Everything else (binary, auth, account) is already there.

## Three steps for a consuming project

```bash
# 1. Point at the shared, already-authenticated binary
export NLM_BIN=/home/node/patent-wiki-analyzer/.venv/bin/nlm

# 2. Record the notebook UUID you want to read (commit this to the project)
export NLM_NOTEBOOK=<notebook-uuid>      # e.g. in the project's .env or a .nlm file

# 3. Query it (RAG over that notebook's sources — grounded answer + citations)
"$NLM_BIN" query notebook "$NLM_NOTEBOOK" "your question here" --json
```

That's the entire integration. The notebook answers from its sources only
(the videos + comments we ingested), with citations back to them.

## Token hygiene — query through a Haiku subagent

`nlm query notebook --json` returns a large blob (~95 KB: answer + every
citation + chunk metadata). **Do not pour that into a main (Opus) context.**
Per the project rule [[feedback-nlm-query-via-haiku]]: run the query inside a
cheap Haiku subagent whose only job is to call `nlm ... --json` and return
`.value.answer` (plus citation titles if needed). The expensive model never
sees the raw JSON.

Minimal extractor (what the subagent runs):

```bash
"$NLM_BIN" query notebook "$NLM_NOTEBOOK" "Q" --json \
  | python -c 'import sys,json; d=json.load(sys.stdin); print(d.get("value",{}).get("answer") or d.get("answer",""))'
```

## Reading several KBs at once

```bash
"$NLM_BIN" cross query --help     # query multiple notebooks, aggregated answer
```

Use this when a project wants to consult more than one corpus (e.g. a
"Claude × TradingView" notebook plus a future "broker execution venues" one).

## Writing back (optional, makes the KB bidirectional)

A consuming project isn't limited to reading. It can append its own findings to
the same notebook so the KB compounds over time:

```bash
"$NLM_BIN" source add "$NLM_NOTEBOOK" --file ./my-findings.md --title "Project X notes"
```

Or build a sibling notebook with this repo's pipeline and keep them as a matrix.
Mind the free-tier ceiling: **50 sources / notebook** (`--limit 50`). yt2nlm's
matrix auto-spills into `_part 2`, `_part 3`, … when a base notebook fills.

## Copy-paste helper for a new project

Drop this `kb.sh` into any project; it hard-codes the binary and takes the
notebook + question as args:

```bash
#!/usr/bin/env bash
# kb.sh — ask a NotebookLM knowledge base. Usage: ./kb.sh "<notebook-uuid>" "<question>"
set -euo pipefail
NLM_BIN="${NLM_BIN:-/home/node/patent-wiki-analyzer/.venv/bin/nlm}"
"$NLM_BIN" query notebook "$1" "$2" --json \
  | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("value",{}).get("answer") or d.get("answer",""))'
```

## Discovering notebook IDs

You don't have to remember UUIDs by hand:

```bash
"$NLM_BIN" notebook list                       # all notebooks: id + title
"$NLM_BIN" notebook list | grep -i tradingview # find one by title
"$NLM_BIN" notebook describe "$NLM_NOTEBOOK"    # AI summary + suggested topics
"$NLM_BIN" source list "$NLM_NOTEBOOK"          # what's actually inside it
```

## Known knowledge bases on this account

| Topic | Title (search `notebook list`) | UUID |
|---|---|---|
| Claude × TradingView integration | `Claude × TradingView — integration` | `a86ba710-142d-475f-afcd-49f251ae7080` |

> The yt2nlm manifest `state/<key>.json` records the notebook UUID(s) for every
> corpus this repo builds — it is the source of truth for IDs. For the
> TradingView corpus the key is `claude_tradingview`.
