#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

DIR="$HOME/Documents/journalEntries"
years=(2024 2025)

days_in_full_year() {
  local y=$1
  if (( y == 2024 || y == 2028 )); then
    echo 366
  else
    echo 365
  fi }

echo
for year in "${years[@]}"; do
  entries=( "$DIR"/${year}.*.txt )
  entry_count=${#entries[@]}

  if [ "$year" -eq 2025 ]; then
    days_in_year=$(date +%j)
  else
    # Full days in that year
    days_in_year=$(days_in_full_year "$year")
  fi

  printf "%d: %d/%d entries/days\n" \
         "$year" "$entry_count" "$days_in_year"
done

echo
echo "latest 7:"
ls -l "$DIR" | tail -n 7

echo
echo "shortest 7:"
ls -lS "$DIR" | tail -n 7
echo
