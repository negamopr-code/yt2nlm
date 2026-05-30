# yt2nlm — YouTube channel → NotebookLM (notebook matrix)

Загружает видео целого канала YouTube в Google NotebookLM **как в референс-видео**:
на каждое видео создаётся **2 источника** — само видео (транскрипт, нативный YouTube-ингест
NotebookLM) и его **комментарии** (структурированный текст: автор → текст → ветки ответов).
Оба источника кладутся в **один** ноутбук, чтобы NotebookLM сопоставлял видео с комментами.

Когда ноутбук упирается в лимит источников (free = 50), создаётся `_part 2`, `_part 3`… —
это **матрица ноутбуков** (паттерн из patent-wiki-analyzer, портирован на Python).

## Установка
```bash
cd /workspace && ./scripts/restore.sh
```
- ставит `yt-dlp` в `.venv` (перечисление канала + выкачка комментов, без API-ключа);
- `nlm` берётся из patent-wiki venv по `NLM_BIN` (уже авторизован).

## Запуск
```bash
# посчитать масштаб без записи:
.venv/bin/python -m yt2nlm '@ChannelHandle' --dry-run

# обкатать на 2 видео:
.venv/bin/python -m yt2nlm '@ChannelHandle' --max-videos 2

# полный прогон канала:
.venv/bin/python -m yt2nlm '@ChannelHandle'
```

### Опции
| Флаг | По умолчанию | Назначение |
|------|--------------|-----------|
| `channel` | — | `@handle`, URL канала, `UC…` id или URL плейлиста |
| `--ingest` | `video+comments` | `video+comments` \| `comments` \| `video` |
| `--comments-mode` | `top` | `top` (популярные) \| `all` (все до лимита) |
| `--max-comments` | `1000` | потолок комментов на видео |
| `--no-replies` | off | не грузить ответы |
| `--limit` | `50` | источников на ноутбук (plus = 300) |
| `--max-videos` | все | взять первые N (тест) |
| `--pace` | `2.0` | пауза между видео, сек (анти-троттлинг) |
| `--dry-run` | off | только перечислить и посчитать |

## Resume / дедуп
Прогресс пишется в `state/<channel>.json` после **каждого** видео: какое видео в каком
ноутбуке, id источников, статус. Повторный запуск пропускает уже готовые видео и
продолжает заполнять последний `_part N`. Ctrl-C безопасен.

## Структура
```
yt2nlm/
  __main__.py     CLI (python -m yt2nlm)
  pipeline.py     оркестрация: канал → видео → матрица
  youtube.py      yt-dlp: список видео канала + комменты с ветками
  comments_fmt.py рендер комментов в Markdown-источник
  nlm.py          обёртка nlm CLI (сериализация, дифф source id)
  matrix.py       ротация ноутбуков (_part N), лимит 50
  state.py        manifest для resume/дедупа
```

## Заметки
- `nlm` аккаунт: `bbubu2748@gmail.com` (профиль `~/.notebooklm-mcp-cli`). Если куки протухли —
  `nlm login` на хосте; профиль bind-mounted, переживает рестарт.
- YouTube троттлит headless-выкачку комментов; для больших каналов поднимай `--pace`.
