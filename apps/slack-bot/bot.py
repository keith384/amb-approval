#!/usr/bin/env python3
"""
Slack front door for the AMB tools (channel #amb-implimenation). Thin wrapper over
amb.dispatch — one slash command `/amb <sub> <brand> [text]`. Long runs ack
immediately and post when done. Requires a Slack app (Socket Mode):

    pip install slack_bolt
    export SLACK_BOT_TOKEN=xoxb-...   SLACK_APP_TOKEN=xapp-...   ANTHROPIC_API_KEY=...
    python bot.py

Slash command config: Command `/amb`, Socket Mode on, scopes commands/chat:write/
files:write. Uploaded files (intake.json / flow.json / recording) are saved to the
brand's inputs/ folder by the file_shared handler before the matching command runs.
"""
from __future__ import annotations
import os
import threading

import amb


def _parse(text: str):
    parts = (text or "").strip().split(maxsplit=2)
    sub = parts[0] if parts else "status"
    brand = parts[1] if len(parts) > 1 else ""
    extra = parts[2] if len(parts) > 2 else ""
    return sub, brand, extra


def main():
    try:
        from slack_bolt import App
        from slack_bolt.adapter.socket_mode import SocketModeHandler
    except ImportError:
        raise SystemExit("pip install slack_bolt  (and set SLACK_BOT_TOKEN / SLACK_APP_TOKEN)")

    app = App(token=os.environ["SLACK_BOT_TOKEN"])

    @app.command("/amb")
    def handle(ack, respond, command):
        sub, brand, extra = _parse(command.get("text", ""))
        if not brand and sub != "status":
            ack("usage: `/amb <brand-doc|storyboard|review|feedback|status> <brand> [text]`")
            return
        # Long-running tools: ack now, post when done.
        if sub in ("brand-doc", "storyboard", "review"):
            ack(f":hourglass_flowing_sand: running *{sub}* for *{brand}*…")
            def work():
                res = amb.dispatch(sub, brand, extra)
                respond(res["text"])
            threading.Thread(target=work, daemon=True).start()
        else:
            res = amb.dispatch(sub, brand, extra)
            ack(res["text"])

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


if __name__ == "__main__":
    main()
