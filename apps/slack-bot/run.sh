#!/bin/bash
# Launch the AMB Slack bot with its env. Used by the launchd agent.
cd "$(dirname "$0")"
set -a; source .env.local; set +a
exec ./.venv/bin/python bot.py
