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
        # Long-running tools: ack now, run + upload artifacts, post when done.
        if sub in ("brand-doc", "storyboard", "review"):
            ack(f":hourglass_flowing_sand: running *{sub}* for *{brand}*…")
            channel_id = command.get("channel_id")

            def work():
                res = amb.dispatch(sub, brand, extra)
                uploaded = 0
                for it in res.get("artifacts", []):
                    try:
                        up = app.client.files_upload_v2(channel=channel_id, file=it["path"], title=it["label"])
                        f = up.get("file") or (up.get("files") or [{}])[0]
                        perma = f.get("permalink")
                        if perma:
                            amb.set_artifact_link(brand, it["label"], perma)
                            uploaded += 1
                    except Exception:
                        pass  # posting results still works even if an upload fails
                tail = f"\n_{uploaded} artifact(s) posted; links are on the board._" if uploaded else ""
                respond(res["text"] + tail)
            threading.Thread(target=work, daemon=True).start()
        else:
            res = amb.dispatch(sub, brand, extra)
            ack(res["text"])

    @app.event("app_mention")
    def on_mention(event, say):
        text = event.get("text", "")
        files = event.get("files", []) or []
        channel = event.get("channel")
        thread = event.get("thread_ts") or event.get("ts")
        attach = [f for f in files if f.get("name", "").lower().endswith((".pdf", ".png", ".jpg", ".jpeg"))]
        pdf_names = [f.get("name", "") for f in attach if f.get("name", "").lower().endswith(".pdf")]
        # Resolve the project: an explicit "for <brand>", else the brand this thread remembers.
        brand = amb.parse_request(text, pdf_names)["brand"]
        if brand == "unknown":
            brand = amb.thread_brand(channel, thread) or "unknown"
        if brand == "unknown":
            say(text="Which brand is this? Mention me with the brand (e.g. "
                     "`@AMB build a storyboard for Superpower` + the PDFs) and I'll remember it for this thread.",
                thread_ts=thread)
            return
        amb.link_thread(channel, thread, brand)        # thread is now persistent for this project
        action = amb.followup_action(text)
        doing = {"storyboard": "re-doing the storyboard", "brand-doc": "updating the brand doc",
                 "review": "running the experience review", "feedback": "logging Apple's feedback",
                 "status": "checking status"}.get(action, "on it")
        say(text=f":hourglass_flowing_sand: *{brand}* — {doing}…", thread_ts=thread)

        def work():
            d = amb._brand_dir(brand)
            pdfs = []
            for f in attach:
                dest = d / "inputs" / f["name"]
                try:
                    amb.download(f.get("url_private_download") or f["url_private"], str(dest), os.environ["SLACK_BOT_TOKEN"])
                    if f["name"].lower().endswith(".pdf"):
                        pdfs.append(str(dest))
                except Exception:
                    pass
            res = amb.apply_followup(brand, action, note=text, pdf_paths=pdfs)
            for it in res.get("artifacts", []):
                try:
                    up = app.client.files_upload_v2(channel=channel, thread_ts=thread, file=it["path"], title=it["label"])
                    f = up.get("file") or (up.get("files") or [{}])[0]
                    if f.get("permalink"):
                        amb.set_artifact_link(brand, it["label"], f["permalink"])
                except Exception:
                    pass
            say(text=res["text"], thread_ts=thread)
        threading.Thread(target=work, daemon=True).start()

    # No-op: we read attachments from the app_mention payload, not these events.
    @app.event("file_shared")
    def _ignore_file_shared():
        pass

    @app.event("file_created")
    def _ignore_file_created():
        pass

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    main()
