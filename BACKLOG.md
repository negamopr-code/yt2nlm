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
