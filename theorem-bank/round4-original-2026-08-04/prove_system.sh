#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
python3 "$ROOT/build_round4.py"
python3 "$ROOT/verify_round4.py" > "$ROOT/PROVE-SYSTEM-RECEIPT.txt"
cp "$ROOT/FINAL-VERIFICATION.json" "$ROOT/.first-final.json"
python3 "$ROOT/build_round4.py" >/dev/null
python3 "$ROOT/verify_round4.py" >/dev/null
cmp "$ROOT/.first-final.json" "$ROOT/FINAL-VERIFICATION.json"
rm "$ROOT/.first-final.json"
echo "CLEAN DETERMINISTIC REPLAY: PASS" | tee -a "$ROOT/PROVE-SYSTEM-RECEIPT.txt"
