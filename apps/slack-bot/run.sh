#!/bin/bash
# Launch the AMB Slack bot with its env. Used by the launchd agent / daemon.sh.
# Wrap in `caffeinate -is` so the Mac doesn't sleep while the bot runs — on this
# laptop, sleep freezes the process, drops the Socket Mode connection, and makes
# the bot miss @mentions (Slack does not replay events received while asleep).
# -i prevents idle sleep, -s prevents system sleep on AC power.
cd "$(dirname "$0")"
set -a; source .env.local; set +a
exec caffeinate -is ./.venv/bin/python bot.py
