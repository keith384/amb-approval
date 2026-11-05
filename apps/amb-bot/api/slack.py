"""Slack front door (Vercel). Verifies the request signature, resolves the brand,
enqueues a job, and acks within Slack's 3s window. The worker (api/process.py)
runs the actual build. Configure this URL as the Slack Event Subscriptions request
URL AND the /amb slash command URL."""
import json
import os
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.common import verify_slack, enqueue_job, say  # noqa: E402
import amb  # noqa: E402  (vendored; sys.path set inside lib.common)


class handler(BaseHTTPRequestHandler):
    def _send(self, code, body="", ctype="text/plain"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.end_headers()
        if body:
            self.wfile.write(body.encode() if isinstance(body, str) else body)

    def do_GET(self):
        self._send(200, "amb-bot ok")

    def do_POST(self):
        raw = self.rfile.read(int(self.headers.get("content-length", 0) or 0))
        headers = {k.lower(): v for k, v in self.headers.items()}
        if not verify_slack(headers, raw):
            self._send(401, "bad signature")
            return
        ctype = headers.get("content-type", "")
        try:
            if ctype.startswith("application/json"):
                data = json.loads(raw or b"{}")
                if data.get("type") == "url_verification":
                    self._send(200, data.get("challenge", ""))
                    return
                if data.get("type") == "event_callback" and data.get("event", {}).get("type") == "app_mention":
                    self._mention(data, data["event"])
                self._send(200, "")
                return
            form = {k: v[0] for k, v in urllib.parse.parse_qs(raw.decode()).items()}
            if form.get("command"):
                self._command(form)
                self._send(200, json.dumps({"response_type": "ephemeral",
                                            "text": ":hourglass_flowing_sand: Working on it — I'll post in the thread."}),
                           "application/json")
                return
        except Exception:
            pass
        self._send(200, "")

    def _mention(self, data, ev):
        text = ev.get("text", "")
        files = [{"name": f.get("name"), "url": f.get("url_private_download") or f.get("url_private")}
                 for f in (ev.get("files") or [])
                 if f.get("name", "").lower().endswith((".pdf", ".png", ".jpg", ".jpeg"))]
        channel, thread = ev.get("channel"), ev.get("thread_ts") or ev.get("ts")
        pdf_names = [f["name"] for f in files if f["name"].lower().endswith(".pdf")]
        brand = amb.thread_brand(channel, thread) or amb.parse_request(text, pdf_names)["brand"]
        if brand == "unknown":
            say(channel, thread, "Which brand is this? Mention me with the brand "
                "(e.g. `@AMB build a storyboard for Superpower`) + the PDFs, and I'll remember it for this thread.")
            return
        amb.link_thread(channel, thread, brand)
        rows = enqueue_job(status="queued", action=amb.followup_action(text), brand=brand,
                           channel=channel, thread_ts=thread, user_id=ev.get("user"),
                           files=files, note=text, slack_event_id=data.get("event_id"))
        if rows:  # first delivery (not a Slack retry)
            say(channel, thread, f":hourglass_flowing_sand: *{brand}* — queued, building now…")

    def _command(self, form):
        parts = (form.get("text") or "").strip().split(maxsplit=2)
        sub = parts[0] if parts else "status"
        brand = parts[1] if len(parts) > 1 else ""
        extra = parts[2] if len(parts) > 2 else ""
        if not brand:
            return
        enqueue_job(status="queued", action=sub, brand=brand, channel=form.get("channel_id"),
                    thread_ts=None, user_id=form.get("user_id"), files=[], note=extra,
                    slack_event_id=f"cmd-{form.get('trigger_id')}")
