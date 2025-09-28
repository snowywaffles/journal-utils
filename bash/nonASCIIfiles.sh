#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

DIR="$HOME/Documents/journalEntries"
count=0

echo "Files containing non-ASCII characters:"
echo

for file in "$DIR"/20{24,25,26}*.txt; do
  if LC_ALL=C grep -q "[^ -~]" "$file"; then
    echo "$file"
    ((count++))
  fi
done

echo
echo "Total files with non-ASCII characters: $count"
