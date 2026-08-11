# Backlog — платформы и фичи на потом

## Платформы (source-адаптеры)
- [x] **YouTube** — видео + комменты (2 источника/видео). Готово.
- [x] **Reddit** — пост + дерево комментов через praw (1 источник/пост). Готово, ждёт live-теста (нужны `REDDIT_CLIENT_ID/SECRET`).
- [ ] **LinkedIn** — headless только через **Apify-actor по API** (части нужны экспортир. куки). Альтернатива — браузерное расширение/«Claude in Chrome» (не headless, риск бана).
- [ ] **X / Twitter** — Apify-actor по API (офиц. API платный).
- [ ] **TikTok / Instagram** — Apify-actor по API (агрессивный антибот).
- [ ] **Generic `apify` адаптер** — один Apify API-ключ → каталог actors; Claude/код выбирает actor под платформу. Самый универсальный путь для всего, кроме Reddit. См. memory `multi-platform-comments-research`.

## Market monitor (2026-08-11, `yt2nlm monitor`) — SHIPPED, follow-ups
- [x] Комментный дедуп по cid + re-check старых видео — решено монитором (`yt2nlm/monitor.py`).
- [x] Аналитика-артефакты — SCOREBOARD/LEDGER/QUESTIONS/COMPETITORS/PROPOSALS + дашборд http://localhost:8091/monitor.
- [ ] Reddit-lane live-тест (нужны `REDDIT_CLIENT_ID/SECRET` в окружении CLI-запуска).
- [ ] Apple App Store reviews (сейчас только Google Play).
- [ ] Cron-обёртка (сейчас ручной запуск; exit 75 = quota-pause, cron-friendly).
- [ ] Кнопка "run" на дашборде (монитор должен бежать вне web-контейнера — state там :ro).
- [ ] state JSON → SQLite, если файл вырастет >10 MB.
- [ ] Удалить throwaway-ноутбук `MONITOR-TEST` (2896e387…) + state/monitor-test.* + reports/monitor-test/ после первого реального батча (беречь 100-notebook cap).

## Фичи
- [ ] Аналитика-артефакты: `reports/<source>.md` и/или studio-артефакт в NotebookLM (report/mindmap/audio).
- [ ] `--since/--until` фильтр по дате для каналов/сабреддитов.
- [ ] Параллельная выкачка комментов (сейчас последовательно ради анти-троттлинга).

## LinkedIn research (2026-06-02) — build deferred
Researched LinkedIn comment collection. No free/ToS-clean headless path. Risk ladder: manual/semi-manual Voyager-JSON harvest (~5-10%) < your-session agent Claude-for-Chrome/Manus (~18-25%) < cloud/headless (~35-40%). Recommended default = semi-manual snippet -> `adapters/linkedin_json.py` (mirrors reddit.py, zero core changes); agentic = convenience upgrade; Apify no-cookies = automation. Full notes: `docs/linkedin-comment-collection-research.md`; design: `~/.claude/plans/look-to-what-we-jiggly-lagoon.md`. **Status: deferred (continue later).**
