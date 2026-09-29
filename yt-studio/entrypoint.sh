#!/bin/sh
# yt-studio: one Chromium signed in as the @anotherword8913 channel account (sign in ONCE via noVNC
# http://localhost:8115/vnc.html). The uploader (upload.py) drives it over CDP :9222 and saves every
# video as a PRIVATE draft; the user alone publishes or deletes in YouTube Studio.
#
# Session survival (incident 2026-09-28, two reboots on 09-27 each signed the channel out):
#  * Chromium starts on about:blank, never straight on a Google page. cookie_guard.py first re-injects its
#    live-jar snapshot if (and only if) that holds a NEWER rotating token than the DB a SIGKILL left behind,
#    then opens Studio. It keeps snapshotting every 15 s.
#  * Browser sign-in (DICE) is forced OFF before every launch (nodice.py, incident 2026-09-29).
#  * docker stop / restart → SIGTERM → Chromium is closed with SIGTERM so it flushes its cookie DB.
set -eu
P=/home/app/yt-profile; mkdir -p "$P"; PY=$P/.venv/bin/python
rm -f /tmp/.X99-lock /tmp/.X11-unix/X99 "$P/SingletonLock" "$P/SingletonSocket" "$P/SingletonCookie" /tmp/stopping
Xvfb :99 -screen 0 1600x1000x24 -nolisten tcp &
export DISPLAY=:99; sleep 1
openbox &
x11vnc -display :99 -forever -shared -nopw -localhost -quiet -bg
websockify --web /usr/share/novnc 6080 localhost:5900 &

graceful() {
  touch /tmp/stopping
  pkill -TERM -f cookie_guard.py || true
  pkill -TERM -x chromium || pkill -TERM -f /usr/lib/chromium/chromium || true
  i=0; while pgrep -f /usr/lib/chromium/chromium >/dev/null && [ $i -lt 8 ]; do sleep 1; i=$((i+1)); done
  exit 0
}
trap graceful TERM INT

( while [ ! -f /tmp/stopping ]; do "$PY" /opt/yt/cookie_guard.py || true; sleep 5; done ) &
( while [ ! -f /tmp/stopping ]; do
    "$PY" /opt/yt/nodice.py "$P" || true   # DICE off before every launch (see nodice.py)
    chromium --no-sandbox --disable-gpu --user-data-dir="$P" --remote-debugging-port=9222 --remote-debugging-address=127.0.0.1 \
      --no-first-run --no-default-browser-check --disable-dev-shm-usage --window-size=1580,960 \
      about:blank || true
    sleep 3   # browser closed/crashed -> relaunch (the guard sees the new instance and checks the jar again)
  done ) &
while true; do sleep 3600 & wait $! || true; done
