"""YouTube upload: Desktop-client OAuth (loopback via the published port) +
resumable videos.insert. Tokens live in state/videogen.oauth.json."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from .config import STATE_DIR

SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_PATH = STATE_DIR / "videogen.oauth-client.json"
TOKEN_PATH = STATE_DIR / "videogen.oauth.json"


def client_config() -> dict | None:
    if not CLIENT_PATH.exists():
        return None
    raw = json.loads(CLIENT_PATH.read_text())
    return raw if "installed" in raw else {"installed": raw}


def auth_url(redirect_uri: str) -> tuple[str, object]:
    from google_auth_oauthlib.flow import Flow
    flow = Flow.from_client_config(client_config(), scopes=SCOPES,
                                   redirect_uri=redirect_uri)
    url, _state = flow.authorization_url(access_type="offline",
                                         prompt="consent")
    return url, flow


def finish_auth(flow, code: str) -> None:
    flow.fetch_token(code=code)
    creds = flow.credentials
    TOKEN_PATH.write_text(creds.to_json())


def credentials():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    if not TOKEN_PATH.exists():
        return None
    creds = Credentials.from_authorized_user_info(
        json.loads(TOKEN_PATH.read_text()), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN_PATH.write_text(creds.to_json())
    return creds


def upload(item_dir: Path, meta: dict) -> str:
    """Resumable upload; returns the YouTube video id."""
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    creds = credentials()
    if creds is None:
        raise RuntimeError("not authorized — connect YouTube first")
    yt = build("youtube", "v3", credentials=creds)
    body = {"snippet": {"title": meta["title"][:100],
                        "description": meta["description"][:4900],
                        "tags": meta.get("tags", [])[:30],
                        "categoryId": meta.get("categoryId", "27")},
            "status": {"privacyStatus": meta.get("privacyStatus", "private"),
                       "selfDeclaredMadeForKids": False}}
    media = MediaFileUpload(str(item_dir / "final.mp4"),
                            chunksize=8 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        _status, resp = req.next_chunk()
    vid = resp["id"]
    thumb = item_dir / "thumb.jpg"
    if thumb.exists():
        try:
            yt.thumbnails().set(videoId=vid,
                                media_body=str(thumb)).execute()
        except Exception as exc:                     # thumb is non-fatal
            print(f"thumbnail set failed: {exc}")
    return vid


def quota_ok(state: dict, per_day: int) -> bool:
    today = date.today().isoformat()
    if state["uploads"].get("date") != today:
        state["uploads"] = {"date": today, "count": 0}
    return state["uploads"]["count"] < per_day


def count_upload(state: dict) -> None:
    state["uploads"]["count"] = state["uploads"].get("count", 0) + 1
