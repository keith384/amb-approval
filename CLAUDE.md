# AMB Approval Workflow — conventions

## What this is
Internal tooling for Linq's Apple Messages for Business brand-approval pipeline.
See `README.md` (layout) and `docs/BUILD-PLAN.md` (full spec). Separate repo from cerebro.

## Hard rules
1. **Never author Apple rules.** Rules are normalized from `sources/` only; where a source
   is silent, the rule set is silent. Every rule carries a `source_anchor`. No tool may emit
   a finding citing a rule that isn't in `rules.json`.
2. **Terminology lint on every generated artifact** (PDF text + filenames): no "iMessage",
   "AMB", "Apple Chat", "chat"/"text" as a channel name, "iMessage app" as a feature label,
   or exclusivity/endorsement claims. Customer-facing name is "Apple Messages for Business".
3. **Measurement is code, judgment is the model.** Every model finding carries a rule ID +
   timestamp or it is dropped. Measurements (latency, counts, presence) are never the model's.
4. **Rule-set changes are versioned** with a changelog line (brand, date, Apple's wording,
   what changed) and must still reproduce every past finding in the regression corpus.
5. `sources/` is read-only source material — don't edit it; normalize from it.
6. Large recordings (`*.mp4/*.mov`) are git-ignored — reference by path.

## Commands
```bash
cd packages/rules && python3 build_rules.py && python3 test_rules.py
```

## Stack
Rule set: Python → `rules.json`. Tools 1/2: CLI-first, HTML→PDF. Tool 3: ffmpeg+OCR+Python+
Claude API. Board: Next.js/Vercel + SSO. Bot: Slack. Runs on Linq Macs (Vision OCR); container fallback.
