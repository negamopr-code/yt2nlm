# Backlog — платформы и фичи на потом

## Платформы (source-адаптеры)
- [x] **YouTube** — видео + комменты (2 источника/видео). Готово.
- [x] **Reddit** — пост + дерево комментов через praw (1 источник/пост). Готово, ждёт live-теста (нужны `REDDIT_CLIENT_ID/SECRET`).
- [ ] **LinkedIn** — headless только через **Apify-actor по API** (части нужны экспортир. куки). Альтернатива — браузерное расширение/«Claude in Chrome» (не headless, риск бана).
- [ ] **X / Twitter** — Apify-actor по API (офиц. API платный).
- [ ] **TikTok / Instagram** — Apify-actor по API (агрессивный антибот).
- [ ] **Generic `apify` адаптер** — один Apify API-ключ → каталог actors; Claude/код выбирает actor под платформу. Самый универсальный путь для всего, кроме Reddit. См. memory `multi-platform-comments-research`.

## Фичи
- [ ] Аналитика-артефакты: `reports/<source>.md` и/или studio-артефакт в NotebookLM (report/mindmap/audio).
- [ ] `--since/--until` фильтр по дате для каналов/сабреддитов.
- [ ] Дедуп комментов между видео (сейчас дедуп только на уровне единиц).
- [ ] Параллельная выкачка комментов (сейчас последовательно ради анти-троттлинга).

## LinkedIn research (2026-06-02) — build deferred
Researched LinkedIn comment collection. No free/ToS-clean headless path. Risk ladder: manual/semi-manual Voyager-JSON harvest (~5-10%) < your-session agent Claude-for-Chrome/Manus (~18-25%) < cloud/headless (~35-40%). Recommended default = semi-manual snippet -> `adapters/linkedin_json.py` (mirrors reddit.py, zero core changes); agentic = convenience upgrade; Apify no-cookies = automation. Full notes: `docs/linkedin-comment-collection-research.md`; design: `~/.claude/plans/look-to-what-we-jiggly-lagoon.md`. **Status: deferred (continue later).**
