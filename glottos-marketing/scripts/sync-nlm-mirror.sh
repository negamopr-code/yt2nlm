#!/bin/sh
# Mirror docs/nlm-mirror/*.md into the "Glottos — go-to-market" NotebookLM notebook,
# replace-by-title (NLM sources are immutable: delete the old one, add the new one).
# Run after every substantive exchange (user rule 2026-09-27, universal for all projects).
set -eu
cd "$(dirname "$0")/.."
N=${NLM_BIN:-$PWD/.nlmvenv/bin/nlm}; P=drawnformula; NB=8306c0a9-1418-41e2-a988-1c0459eafc89
export NLM_PROFILE=$P
sync_one() {  # file title
  old=$($N source list $NB --profile $P | python3 -c "import json,sys;t=sys.argv[1];print(' '.join(s['id'] for s in json.load(sys.stdin) if s.get('title')==t))" "$2")
  $N source add $NB --file "$1" --title "$2" --wait --profile $P >/dev/null
  for id in $old; do $N source delete $id --confirm --profile $P >/dev/null; done   # delete AFTER the new one is in
  echo "synced: $2"
}
sync_one docs/nlm-mirror/discussion-journal.md "MIRROR — discussion journal (verbatim)"
sync_one docs/nlm-mirror/status.md "MIRROR — status"
