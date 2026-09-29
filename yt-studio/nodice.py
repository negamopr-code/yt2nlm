# Turn off Chromium browser sign-in (DICE) in the yt-studio profile before Chromium starts.
# Incident 2026-09-29: chrome://signin-internals showed Account Consistency=DICE with no refresh token
# ("Missing authorization code due to OAuth outage in Dice" - Debian Chromium has no Google API keys).
# CONFIRMED 2026-09-29 (graceful restart, docker kill, and a real VM reboot all kept the login) cause of "every restart signs the channel out": the DICE AccountReconcilor reconciles the web
# session away at startup (the .google.com SID family vanished, the youtube.com cookies survived).
# signin.allowed=false disables DICE + the reconcilor; plain web sign-in to YouTube Studio is unaffected.
# Chromium must NOT be running (it rewrites Preferences), so entrypoint.sh calls this before every launch.
import json, os, sys
f = os.path.join(sys.argv[1], 'Default', 'Preferences')
try:
    prefs = json.load(open(f))
except FileNotFoundError:
    sys.exit(0)
s = prefs.setdefault('signin', {})
if s.get('allowed') is False and s.get('allowed_on_next_startup') is False:
    sys.exit(0)
s['allowed'] = False
s['allowed_on_next_startup'] = False
tmp = f + '.nodice-tmp'
with open(tmp, 'w') as fh:
    json.dump(prefs, fh)
os.replace(tmp, f)
print('nodice: signin.allowed=false written')
