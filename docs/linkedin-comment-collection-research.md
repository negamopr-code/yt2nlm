# LinkedIn comment collection — research & lessons learned (2026-06-02)

**Goal:** do for **LinkedIn** what `yt2nlm` already does for YouTube/Reddit — pull a post's
**comments** into NotebookLM for analysis. (Build deferred by user; this records the research so we
can resume. Full implementation design: `~/.claude/plans/look-to-what-we-jiggly-lagoon.md`.)

## The core finding
**There is no free, ToS-clean, headless path for LinkedIn.** LinkedIn User Agreement §8.2 forbids
*all* automation — scrapers, bots, **and browser extensions/agents**. The only open question is
whether LinkedIn detects it; enforcement is account-level (restriction/ban), and they litigate
commercial scrapers (Proxycurl shut down 2025; HeyReach banned 2026).

## Risk ladder (90-day account-restriction estimates, from 2026 sources)
| Approach | Runs in | Ban risk | Notes |
|---|---|---|---|
| Manual DevTools / JSON copy + **human scroll** | your session | **~5–10%** | lowest; you scroll, harvest the JSON the page loaded |
| **Semi-manual snippet** (Voyager-JSON harvest while you scroll) | your session | ~5–10% | free; mirrors our YouTube extension; **recommended** |
| **Agentic** — Claude for Chrome / Manus Browser Operator (reads post-to-post) | your local browser | ~18–25% | the "Manus behaviour"; convenient; agent's robotic precision is the tell |
| Apify **no-cookies** public actors | Apify cloud | ~5% (public data) | no LinkedIn login of ours → risk on Apify; ~$/record |
| Cloud/headless + your cookies (OpenAI Operator, Playwright/Selenium, Apify-with-cookies, PhantomBuster) | cloud/headless | **~35–40%** | **avoid**; datacenter IP + robotic timing |
| Official LinkedIn API (Marketing/Community Mgmt) | — | none | enterprise-partner-only ($10k+/yr, approval) → **not viable** |

## "Manus behaviour" (agentic browsing) — is it real? Yes.
An agent drives a browser, reads post-to-post like a human, collects insights. Safer variants run in
**your own logged-in browser** (your IP/fingerprint/session): **Claude for Chrome** (most relevant —
you already use Claude; drives real Chrome, pauses for login; token-priced; beta) and **Manus
Browser Operator** (Nov 2025; credit-priced). Cloud ones (OpenAI Operator, Perplexity Comet,
browser-use/Skyvern/Stagehand) = higher ban risk → skip for LinkedIn. **Caveat:** even your-session
agents get flagged at a non-trivial rate; the lowest risk stays the *semi-manual* harvest.

## What we already have here (reuse, don't rebuild)
- **`extensions/add_to_NotebookLM`** — Chrome extension that already harvests YouTube comments (reuses
  the page's InnerTube API) + captures pages as PDF via the CDP debugger API, in your session. The
  **closest foundation** — a LinkedIn module would mirror `lib/youtube-comments-api.js` against
  LinkedIn's **Voyager API**.
- **`docs/claude-tradingview-plan.md`** — a documented-but-unbuilt "MCP server drives a real browser
  over Chrome DevTools Protocol (port 9222)" plan; recorded skeptic verdict **8/10 feasible, 2/10
  reliable**. The agentic-browser foundation, on paper.
- **`glottos-auto/`** — Playwright automation (rendering/recording); navigate/scroll pattern reusable,
  but headless → wrong for logged-in LinkedIn.
- **Prior decision** (memory `multi-platform-comments-research`): chose Reddit (safe API) over
  LinkedIn; documented **Apify as the "generalizable path"** (unbuilt); explicitly **decided against
  headless-login to protected sites** (the glottos lesson: silent Google sign-in, no portable
  session, datacenter cookies get flagged).

## Recommendation (for when we resume — option 4 chosen: research more first)
1. **Default = semi-manual Voyager-JSON harvest:** a console snippet/bookmarklet (then optionally a
   LinkedIn module in the existing extension) captures a post's comment JSON while you scroll your own
   session → a new `yt2nlm/adapters/linkedin_json.py` (mirrors `reddit.py`) → NotebookLM. Free, lowest
   risk, **zero changes to the pipeline core** (matrix/state/nlm/pipeline/render reused).
2. **Convenience upgrade = agentic:** point Claude for Chrome (or Manus) at the same harvest.
3. **Volume/automation = Apify no-cookies** actors (needs `APIFY_TOKEN`; the documented generic
   `adapters/apify.py`, extensible to X/TikTok/IG).

## Key sources
LinkedIn ToS §8.2; hiQ v. LinkedIn (2022) + 2022 settlement; Proxycurl shutdown 2025; Apify
no-cookies LinkedIn actors; Anthropic "Claude for Chrome"; Manus "Browser Operator" (Nov 2025);
Scrapfly / Medium Voyager-API guides. (Full URL list in the session report at localhost:8095.)
