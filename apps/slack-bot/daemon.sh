#!/bin/bash
# Start/stop/status the AMB Slack bot as a detached daemon that survives the
# terminal/session closing (reparented to init via a Python double-fork).
#
# macOS note: a launchd LaunchAgent is the "proper" way to also survive reboot,
# but launchd is blocked by TCC from executing under ~/Documents ("Operation not
# permitted"). Until the repo is moved out of ~/Documents (or Full Disk Access is
# granted to /bin/bash), this daemon is the reliable option. Re-run after reboot.
#
#   ./daemon.sh start | stop | status | restart
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG=/tmp/amb_bot.log
PAT="apps/slack-bot.*bot.py|bot\.py$"

pids() { ps -eo pid,command | grep -iE "$PAT" | grep -v grep | grep -vi claude | awk '{print $1}'; }

case "${1:-status}" in
  start)
    if [ -n "$(pids)" ]; then echo "already running: $(pids)"; exit 0; fi
    : > "$LOG"
    python3 -c "
import os
os.chdir('$DIR')
if os.fork()>0: os._exit(0)
os.setsid()
if os.fork()>0: os._exit(0)
f=open('$LOG','a'); os.dup2(f.fileno(),1); os.dup2(f.fileno(),2)
os.execvp('bash',['bash','run.sh'])
"
    sleep 5; echo "started: $(pids)"; tail -4 "$LOG" ;;
  stop)
    P="$(pids)"; [ -z "$P" ] && { echo "not running"; exit 0; }
    echo "$P" | xargs kill; echo "stopped: $P" ;;
  restart) "$0" stop || true; sleep 1; "$0" start ;;
  status)
    P="$(pids)"; [ -z "$P" ] && echo "not running" || { echo "running: $P"; tail -3 "$LOG"; } ;;
esac
