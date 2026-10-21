# AMB Approval Workflow

Internal tooling for Linq's Apple Messages for Business brand-approval pipeline.
Turns the four-stage Apple approval process into tools that **generate the artifacts
Apple reviews and grade them against Apple's bar before Apple sees them**.

> Note: "AMB" is an internal abbreviation only. Apple prohibits it (and "iMessage for
> Business", "Apple Chat", exclusivity claims, etc.) in anything customer-facing. The
> terminology lint enforces this on every generated artifact.

## The three tools (+ one SOP)

| Stage | Tool | Output |
|---|---|---|
| 1. Brand Approval (Explain) | **Brand Approval Doc generator** | use-case PDF + 2 filled Apple forms + `scope.json` |
| 2. UX Approval (Show) | **UX Storyboard tool** | storyboard PDF (iPhone frames) + `shotlist.json` |
| 3. Experience Review (Build) | **Video Review tool** | MA-style findings report (Ramp format) + timestamp index |
| 4. Launch (Production) | Launch SOP (no software) | one-pager |

All three tools read **one versioned rule set** (`packages/rules`). Tool 1's `scope.json`
and Tool 2's `shotlist.json` are what let Tool 3 say what was *not* shown.

## Repo layout
```
packages/rules/      Rule set: build_rules.py → rules.json (+ test). THE foundation.
sources/             Read-only source material (MA package, checklists, Apple forms,
                     AMB kit, Ramp example). Rules are normalized from here only.
tools/brand-doc/     Tool 1 (CLI-first, HTML→PDF)
tools/storyboard/    Tool 2 (CLI-first, HTML→PDF iPhone frames)
tools/video-review/  Tool 3 (ffmpeg + OCR + event detection + LLM judgment)
apps/board/          Pipeline board (Next.js on Vercel, SSO) — one brand/row, stage/col
apps/slack-bot/      Slack bot (#amb-implimenation) — /amb brand-doc|storyboard|review|feedback|status
schemas/             JSON Schemas: rule, scope, shotlist, flow-file
docs/                BUILD-PLAN.md (spec), STATUS.md (sources + phase tracker)
```

## Core principle
**Do not author Apple rules.** Every rule traces to a source anchor; where a source is
silent, the rule set is silent. No finding may cite a rule that isn't in the rule set.
Measurement & coverage are code; qualitative judgment is the model, constrained to rules
it is handed, always carrying a rule ID + timestamp (mirrors the Deal Predictability
Engine's LLM-extraction / rule-based-scoring split).

## Rule set
```bash
cd packages/rules
python3 build_rules.py     # sources → rules.json (114 rules today)
python3 test_rules.py      # invariants (count, source anchors, severity, gate items)
```
`rules.json` carries: id (numeric Ref), letter_id (Ramp scheme, layered later), name,
check, severity (Non negotiable | Apple standard | Field), source (Apple | MA (Field)),
source_anchor, rule_ref (Standards v2.1 §), applies_when (scope.json key), stages, and
machine_checkable.

## Status
See `docs/STATUS.md`. Phase 0 (rule set) foundation is in place; Tool 3 (video review)
is next per the build sequence.
