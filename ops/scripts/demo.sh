#!/usr/bin/env bash
set -euo pipefail

API_URL=${API_URL:-http://localhost:8000}

echo "Seeding demo user and data via API flow..."
curl -s -X POST "$API_URL/flow/demo" | jq '.'

echo "Submitting sample feedback..."
curl -s -X POST "$API_URL/feedback" \
  -H 'Content-Type: application/json' \
  -d '{"user_id":"demo-user","symbol":"TCS","signal_id":"signal-001","rating":"up","comment":"Great explanation"}' | jq '.'

echo "Demo seed complete."
