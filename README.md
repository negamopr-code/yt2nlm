# yt2nlm — comments → NotebookLM (notebook matrix)

Собирает комментарии с платформ (**YouTube**, **Reddit**) в Google NotebookLM с
**авто-разбивкой по матрице ноутбуков**. Когда ноутбук упирается в лимит источников
(free = 50), создаётся `_part 2`, `_part 3`… (паттерн из patent-wiki-analyzer, на Python).

Платформы подключаются через **source-адаптеры** (`yt2nlm/adapters/`): адаптер перечисляет
«единицы» (видео/посты) и отдаёт на каждую список источников; ядро (матрица/nlm/manifest)
платформо-агностично.

- **YouTube** (как в референс-видео): на видео **2 источника** — само видео (транскрипт,
  нативный ингест) + комментарии (текст: автор → текст → ветки). Оба в один ноутбук.
- **Reddit** (praw, read-only): на пост **1 источник** — тело поста + дерево комментариев.

## Установка
```bash
cd /workspace && ./scripts/restore.sh
```
- ставит `yt-dlp` в `.venv` (перечисление канала + выкачка комментов, без API-ключа);
- `nlm` берётся из patent-wiki venv по `NLM_BIN` (уже авторизован).

## Запуск

### YouTube
```bash
.venv/bin/python -m yt2nlm youtube '@ChannelHandle' --dry-run        # посчитать
.venv/bin/python -m yt2nlm youtube '@ChannelHandle' --max-videos 2   # обкатать
.venv/bin/python -m yt2nlm youtube '@ChannelHandle'                  # весь канал
```
| Флаг | По умолчанию | Назначение |
|------|--------------|-----------|
| `channel` | — | `@handle`, URL канала, `UC…` id или URL плейлиста |
| `--ingest` | `video+comments` | `video+comments` \| `comments` \| `video` |
| `--comments-mode` | `top` | `top` \| `all` |
| `--max-comments` | `1000` | потолок комментов на видео |
| `--no-replies` | off | не грузить ответы |
| `--max-videos` | все | первые N (последние по дате) |

### Reddit
Нужен бесплатный «script»-app: https://www.reddit.com/prefs/apps →
```bash
export REDDIT_CLIENT_ID=...  REDDIT_CLIENT_SECRET=...
# опц: export REDDIT_USER_AGENT="yt2nlm:comments:0.1 (by /u/you)"

.venv/bin/python -m yt2nlm reddit personalfinance --max-posts 30 --dry-run
.venv/bin/python -m yt2nlm reddit r/personalfinance --listing top --time month
.venv/bin/python -m yt2nlm reddit 'https://www.reddit.com/r/x/comments/.../'   # один пост
```
| Флаг | По умолчанию | Назначение |
|------|--------------|-----------|
| `source` | — | сабреддит (`python` / `r/python`) или URL поста |
| `--listing` | `top` | `top` \| `hot` \| `new` \| `rising` |
| `--time` | `year` | окно для `--listing top` |
| `--max-posts` | все | первые N постов |
| `--max-comments` | `500` | потолок комментов на пост |
| `--comment-sort` | `top` | сортировка комментов |

### Общие флаги
`--limit` (источников/ноутбук, default 50) · `--pace` (пауза между единицами) · `--dry-run`.

## Resume / дедуп
Прогресс пишется в `state/<source>.json` после **каждой** единицы: что в каком
ноутбуке, id источников, статус. Повторный запуск пропускает готовые и продолжает
заполнять последний `_part N`. Ctrl-C безопасен.

## Структура
```
yt2nlm/
  __main__.py        CLI (subcommands: youtube | reddit)
  pipeline.py        оркестрация (платформо-агностичная): adapter → матрица
  matrix.py          ротация ноутбуков (_part N), лимит 50
  nlm.py             обёртка nlm CLI (сериализация, дифф source id, add_*)
  state.py           manifest для resume/дедупа
  render.py          обобщённый рендер вложенных тредов (Reddit)
  comments_fmt.py    рендер YouTube-комментов (2 уровня)
  youtube.py         yt-dlp: список канала + комменты
  adapters/
    base.py          SourceAdapter / Unit / SourceSpec
    youtube.py       видео + комменты (2 источника)
    reddit.py        пост + дерево комментов (praw, 1 источник)
```

## Добавить платформу
Реализуй `enumerate_units()` + `fetch_unit() -> [SourceSpec]` в `adapters/<name>.py`
и подключи сабкоманду в `__main__.py`. Ядро (матрица/nlm/manifest/render) переиспользуется.
LinkedIn/X/TikTok удобнее всего через Apify-actor по API (см. memory `multi-platform-comments-research`).

## Заметки
- `nlm` аккаунт: `bbubu2748@gmail.com` (профиль `~/.notebooklm-mcp-cli`). Если куки протухли —
  `nlm login` на хосте; профиль bind-mounted, переживает рестарт.
- YouTube троттлит headless-выкачку комментов; для больших каналов поднимай `--pace`.
