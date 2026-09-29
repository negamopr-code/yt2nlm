"""Keep the @anotherword8913 Google session alive across VM reboots (incident 2026-09-28).

Why: Chromium commits its cookie DB lazily. A WSL/Docker VM reboot SIGKILLs it, so the DB on disk can hold
an OLDER __Secure-1PSIDTS than the one Google last issued. On the next boot the browser presents that stale
rotating token, and Google ends the whole session. The 16:06 and 17:57 reboots on 2026-09-27 both signed
yt-studio out, and a finished video then sat un-uploaded for 11 h.

What this does, as the ONE writer next to the browser (it never rotates anything itself):
  * every SNAP_SECS it reads the live in-memory cookie jar over CDP and saves the Google/YouTube cookies
    atomically to cookie-guard/snapshot.json (0600) whenever the signed-in set changed;
  * whenever it meets a NEW browser instance (boot, or a relaunch after a crash) it compares the snapshot with
    the jar. The snapshot wins only if it holds a STRICTLY NEWER __Secure-1PSIDTS (Google sets it to expire
    1 year after issue, so the later expiry = the later rotation) or the jar has lost SID. Then it re-injects
    the snapshot BEFORE the browser opens any Google page (the entrypoint starts Chromium on about:blank), and
    navigates to Studio. A snapshot that is older than or equal to the jar is never presented, because
    presenting stale tokens is exactly what kills the session family.
Kill switch: touch cookie-guard/disabled.

RESTORE IS OFF by default (09-28 06:40 test): after a SIGKILL the jar came back without ANY .google.com session
cookie, and re-injecting the snapshot did NOT revive the session (Google showed the account chooser). The keeper's
older lesson says the same: injecting a snapshot can kill the session family. Snapshots are kept for diagnosis;
restore only runs with cookie-guard/restore-enabled present.
"""
import json, os, sys, time, urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright

PROFILE = Path("/home/app/yt-profile")
DIR = PROFILE / "cookie-guard"
SNAP = DIR / "snapshot.json"
LOG = DIR / "log.txt"
CDP = "http://127.0.0.1:9222"
SNAP_SECS = 15
STUDIO = "https://studio.youtube.com/"

def log(msg):
    line = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + msg
    print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def ours(c):
    d = c.get("domain", "").lstrip(".")
    return d == "google.com" or d.endswith(".google.com") or d == "youtube.com" or d.endswith(".youtube.com")

def sid(cookies):
    return next((c for c in cookies if c["name"] == "SID" and c["domain"].lstrip(".") == "google.com"), None)

def psidts_exp(cookies):
    c = next((c for c in cookies if c["name"] == "__Secure-1PSIDTS" and c["domain"].lstrip(".") == "google.com"), None)
    return c["expires"] if c else -1

def browser_id():
    try:
        with urllib.request.urlopen(CDP + "/json/version", timeout=3) as r:
            return json.load(r)["webSocketDebuggerUrl"]
    except Exception:
        return None

def load_snap():
    try: return json.loads(SNAP.read_text())
    except Exception: return None

def save_snap(cookies):
    tmp = SNAP.with_suffix(".tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: json.dump({"saved_at": time.time(), "cookies": cookies}, f)
    os.replace(tmp, SNAP)

def key(cookies):
    return sorted((c["name"], c["domain"], c["path"], c["value"]) for c in cookies)

def on_new_instance(ctx):
    jar = [c for c in ctx.cookies() if ours(c)]
    snap = load_snap()
    if (DIR / "restore-enabled").exists() and snap and sid(snap["cookies"]) and (not sid(jar) or psidts_exp(snap["cookies"]) > psidts_exp(jar)):
        why = "jar lost SID" if not sid(jar) else "snapshot holds a newer PSIDTS"
        ctx.add_cookies([{k: c[k] for k in ("name", "value", "domain", "path", "expires", "httpOnly", "secure", "sameSite") if k in c}
                         for c in snap["cookies"]])
        log(f"restore: {why} (snapshot from {time.strftime('%m-%d %H:%M:%S', time.gmtime(snap['saved_at']))} UTC) → re-injected {len(snap['cookies'])} cookies before any Google page")
    else:
        log("boot: jar " + ("signed in" if sid(jar) else "SIGNED OUT (lost .google.com SID)") + f", snapshot {'has' if snap and sid(snap['cookies']) else 'lacks'} SID; nothing restored")
    pages = [p for c in [ctx] for p in c.pages]
    blank = [p for p in pages if p.url in ("about:blank", "chrome://newtab/", "")]
    if blank or not pages:
        (blank[0] if blank else ctx.new_page()).goto(STUDIO, wait_until="commit")

def main():
    DIR.mkdir(exist_ok=True)
    last_bid, last_key = None, None
    with sync_playwright() as p:
        while True:
            if (DIR / "disabled").exists():
                time.sleep(30); continue
            bid = browser_id()
            if not bid:
                time.sleep(2); continue
            try:
                br = p.chromium.connect_over_cdp(CDP)
                ctx = br.contexts[0]
                if bid != last_bid:
                    on_new_instance(ctx); last_bid = bid
                while browser_id() == bid and not (DIR / "disabled").exists():
                    jar = [c for c in ctx.cookies() if ours(c)]
                    if sid(jar):
                        k = key(jar)
                        if k != last_key:
                            save_snap(jar); last_key = k
                    time.sleep(SNAP_SECS)
                try: br.close()
                except Exception: pass
            except Exception as e:
                log(f"error: {type(e).__name__}: {str(e)[:200]}")
                time.sleep(5)

if __name__ == "__main__":
    main()
