# AMB bot — serverless (Vercel Events API)

Always-on replacement for the Mac Socket Mode daemon. Anyone can `@AMB …` or use
`/amb …` in Slack at any time — no laptop required.

## Architecture
```
Slack  ──POST──▶  api/slack.py   (verify signature, resolve brand, enqueue, ack <3s)
                        │  writes amb_job (Supabase)
                        ▼
              api/process.py  ◀── Vercel cron (every minute)
                        │  claims a job → runs brand-doc + storyboard via the
                        │  vendored tools (amb.py) → uploads artifacts to the thread
                        ▼
                     Slack thread
```
- **Front door** (`api/slack.py`): handles the Events API URL-verification handshake,
  `app_mention` events, and the `/amb` slash command. Verifies the Slack signature,
  resolves the project from the thread (or an explicit "for <brand>"), enqueues an
  `amb_job`, and acks immediately.
- **Worker** (`api/process.py`): a cron-triggered function that drains one queued job,
  runs the build, and posts back. `maxDuration` 300s covers a full build.
- **Tools** are vendored at build time by `scripts/vendor.sh` (brand-doc + storyboard +
  the 12 AMB element frames the compositor uses — ~19 MB, not the full 116 MB mirror).
  They run under this function's Python (one `requirements.txt`), so no per-tool venvs.
- **Video review (Tool 3)** is NOT here — Apple Vision is macOS-only; it stays a Mac worker.

## Deploy (one-time)
1. **Vercel → Add New Project → import this repo**, set **Root Directory = `apps/amb-bot`**.
   Framework preset: **Other**. (Build command is in `vercel.json`.)
2. **Environment variables** (from `.env.example`): `SLACK_SIGNING_SECRET`, `SLACK_BOT_TOKEN`,
   `NEXT_PUBLIC_SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `ANTHROPIC_API_KEY`, `CRON_SECRET`
   (any random string). Deploy → note the URL, e.g. `https://amb-bot.vercel.app`.
3. **Cron** needs a Vercel plan with sub-daily crons (Pro). The `* * * * *` schedule in
   `vercel.json` drains the queue every minute.

## Slack app reconfig (one-time) — https://api.slack.com/apps → your app
1. **Event Subscriptions** → turn **On** → Request URL: `https://<deploy>/api/slack`
   (it must echo the `challenge`; the handler does). Subscribe to bot event **`app_mention`**.
2. **Slash Commands** → edit `/amb` → Request URL: `https://<deploy>/api/slack`.
3. **Socket Mode** → turn **Off** (Events API replaces it). You can delete the app-level token.
4. Scopes are unchanged (`app_mentions:read, chat:write, files:read, files:write, commands`).
5. Reinstall the app if Slack prompts.

## Cut over
Once the Vercel bot responds to a test mention, stop the Mac daemon:
`apps/slack-bot/daemon.sh stop`.

## Local checks (already pass)
- `bash scripts/vendor.sh` → vendors tools + 12 frames.
- Signature verify, Supabase thread map, and a full build through the vendored tools
  have been verified locally.
