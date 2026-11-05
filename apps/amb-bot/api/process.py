"""Queue worker (Vercel cron, every minute). Claims the oldest queued job, runs the
build via the vendored amb dispatcher, uploads artifacts to the Slack thread, and
marks the job done/failed. maxDuration 300s covers a brand-doc + storyboard build."""
import json
import os
import sys
import traceback
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.common import claim_next_job, finish_job, run_job, say  # noqa: E402

CRON_SECRET = os.environ.get("CRON_SECRET", "")


class handler(BaseHTTPRequestHandler):
    def _ok(self, obj):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())

    def do_GET(self):
        # Vercel injects `Authorization: Bearer $CRON_SECRET` when CRON_SECRET is set.
        if CRON_SECRET and self.headers.get("authorization", "") != f"Bearer {CRON_SECRET}":
            self.send_response(401)
            self.end_headers()
            return
        job = claim_next_job()
        if not job:
            self._ok({"drained": 0})
            return
        try:
            run_job(job)
            finish_job(job["id"], "done")
            self._ok({"job": job["id"], "status": "done"})
        except Exception as e:
            finish_job(job["id"], "failed", error=traceback.format_exc())
            say(job.get("channel"), job.get("thread_ts"),
                f":warning: *{job.get('brand')}* build failed — {e}")
            self._ok({"job": job["id"], "status": "failed"})
