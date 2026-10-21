# AMB Slack bot (`#amb-implimenation`)

One slash command, `/amb <sub> <brand> [text]`, that runs the three tools and
reports back. `amb.py` is the dispatcher (no Slack deps — CLI-testable);
`bot.py` is the Socket-Mode wrapper.

## Commands
- `/amb brand-doc <brand>` — Tool 1: intake → Walmart doc + filled Apple forms + scope + readiness note
- `/amb storyboard <brand>` — Tool 2: validate flow → iPhone-frame storyboard + shotlist
- `/amb review <brand>` — Tool 3: recording → Ramp-format findings report
- `/amb feedback <brand> <paste Apple's reply>` — split into rule-matched items (AE confirms)
- `/amb status <brand>` — pipeline stage, artifacts, next step

## Brand folders (shared with the pipeline board)
```
brands/<brand>/
  inputs/   intake.json (Tool 1), flow.json (Tool 2), <recording>.mp4 (Tool 3)
  output/   generated artifacts (the board reads these)
  state.json  stage + event log
```
Uploads in a Slack thread are saved to `inputs/` before the matching command runs.

## Run it
```bash
pip install slack_bolt
export SLACK_BOT_TOKEN=xoxb-…  SLACK_APP_TOKEN=xapp-…  ANTHROPIC_API_KEY=…
python bot.py
```
Slack app: create an app, enable Socket Mode, add a `/amb` slash command, scopes
`commands` + `chat:write` + `files:read/write`, install to the workspace, and put the
bot/app tokens in the env above.

## CLI (no Slack)
```bash
python amb.py status ramp
python amb.py storyboard ramp        # runs Tool 2 against brands/ramp/inputs/flow.json
python amb.py review ramp            # runs Tool 3 against the recording in inputs/
```
Long-running tools (brand-doc/storyboard/review) ack immediately in Slack and post when done.
