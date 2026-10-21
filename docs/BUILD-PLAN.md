# AMB Approval Workflow — Build Plan (engineering spec)

Condensed from Keith's plan (20 Oct 2026). The conversation message is the full prose;
this is the executable spec. Four Apple gates; tools cover stages 1–3, Launch gets an SOP.

## Context / guardrails (Apple onboarding, 9 Sep 2026)
- Linq is a **Commercial Non-Public MSP** until first brand is live. All collateral/PR
  goes to Apple before publication. First launch is a showcase.
- **Terminology (enforced by lint):** customer-facing name is **Apple Messages for Business**.
  Forbidden: "iMessage for Business", "Apple Chat", "AMB", "chat"/"text" as a channel name,
  "iMessage app" as a feature label, exclusivity/endorsement claims, speaking for Apple.
- Linq now works the review **directly with Apple** (no MA consultant in the loop going
  forward). MA's Ramp report is kept as the reference example of a good review.
- Use cases → `business-register@apple.com` at qualification; POV recordings → Apple's Box.

## Rule set (foundation — `packages/rules`)
One versioned rule set, all tools read it. A rule record:
`id` (numeric Ref) · `letter_id` (Ramp scheme) · `name` · `check` · `severity`
(Non negotiable | Apple standard | Field) · `source` (Apple | MA (Field)) · `source_anchor`
· `rule_ref` (Standards v2.1 §) · `applies_when` (keyed to scope.json) · `stages`
(doc|storyboard|video) · `machine_checkable`.
Build = extraction/normalization, **not authoring**. Sources & authority in README table.
- **Apple's five non-negotiables:** reachable escalation; honest automation; Leave
  Conversation respected (blocked send shown); capability-aware fallback filmed at send;
  clean language. Plus gate items 0.2 Leave Conversation and 0.3 terminology.
- **Two ID schemes:** 114 cases use numeric Refs (0.1, 5.2); Ramp report uses letter IDs
  (B1, RL1). Carry both; **report in the letter scheme** (what the team reads).
- **10 reasons recordings come back** = first 10 video rules to implement (see plan).

## Tool 1 — Brand Approval Doc generator
Produces the use-case PDF for `business-register@apple.com` + fills Apple's two AcroForms.
- **In:** kick-off transcript (Fireflies/Granola) + AE notes; brand facts; 4 use cases in
  customer's words (one sentence each); entry points.
- **Does:** structured intake (pre-filled from transcript) → classify each use case into
  one of MA's 5 archetypes (find&choose, book&manage, check&resolve, enrol&receive, reach
  a person) → feature fit from Standards 2.5 → flag non-standard use cases needing Apple
  pre-approval + the consumer-AI pause test → terminology lint → render.
- **Out:** `brand-approval-<brand>.pdf` (Walmart-nomination shape: Header; Use Case para;
  At a Glance = Experience/Why It Fits/Value to Users/Value to Society; Features table;
  Company Background), the **two filled Apple PDFs** (pypdf over AcroForms — field names are
  inconsistent, e.g. "GF Authenticaiton", "UC4 Rick Links", so the map lives in one file +
  a test asserts every form field is covered; UseCases has 57 fields, Readiness 25),
  `scope.json` (data every later check reads), internal readiness note (open Qs, pre-approval
  flags, terminology hits).
- **Accept:** every form field present or marked open-question (nothing invented); each use
  case maps to ≥1 enhanced feature or says why text-only; terminology lint passes on PDF
  text + filename; Ramp PDF reads correctly to the AE who ran the call.

## Tool 2 — UX Storyboard tool
Turns approved scope into an iPhone-frame storyboard PDF before anything is built.
- **In:** `scope.json`; a per-use-case conversation script (small authored schema: one line
  per step = actor {customer|bot|human} + element kind + copy + options; YAML/JSON);
  brand assets.
- **Does:** validate each script against storyboard rules (refuse to render blocker-level
  breaks: automated disclosure in opener, QR triage ≤5 real intents, framing bubble before
  every rich element, confirmation after every tap, no bare URL, ≤5 options = Quick Reply not
  List Picker, route-to-person on every menu, "anything else" before close, out-of-hours +
  fallback paths) → render each step as an iPhone frame to Apple's element layout → lay into
  Flows **A** (end to end), **B** (human handoff + console side-by-side), **C** (degraded:
  out of hours, unrecognized input, capability fallback) → emit shot list.
- **Out:** `storyboard-<brand>.pdf` (one page/flow, annotated frames, final page = Standards
  2.18 self-check), `shotlist-<brand>.json` (ordered steps + checklist Refs each should
  evidence; Tool 3 reads this).
- **Accept:** every rich element in scope appears ≥once or storyboard says why not; a Ramp
  expense-support storyboard reproduces the flow and would've flagged ≥ the 6 Fails pre-record;
  renders < 1 min; reviewable in Slack as a PDF.
- **Boundary:** renders what the script says; does not author the brand's bot.

## Tool 3 — Video Review tool (Phase 1, first to build)
Takes the client's iPhone recording → MA-style findings report before Apple sees it.
**Ramp report (9 Oct) is the spec for the output format.**
- **In:** recording (.mov/.mp4), POV; `scope.json` + `shotlist.json`; optional client timestamp index.
- **Pipeline:** (1) frame extract @5fps + OCR → timed transcript of every bubble/chip/row/
  card/label, side-tagged. (2) event detection (message appeared, indicator start/stop,
  element rendered, tap, screen change, cut) → the timings Fail rows need. (3) rule eval:
  deterministic rules first (naming, latency thresholds, indicator presence, bare URL,
  element-kind vs option-count), then an LLM pass for qualitative rules (clear copy, transfer
  announced w/ reason, confirmation after tap, honest automation, clean screen) using frames
  at each timestamp + rule text + Ramp report as examples. (4) coverage: shot-list/scope items
  with no evidence → Not shown (Mandatory|Recommended by severity). (5) render.
- **Out:** `review-<brand>-<date>.pdf` (Ramp 5-bucket format: Fail / Caveat / Not shown
  (Mandatory) / Not shown (Recommended) / Apple will ask — each with timestamp range, test
  ID+name, 1-line issue, 1-line fix; header counts; verdict line), `timestamp-index-<brand>.txt`
  (MA format), `review.json` (findings as data; resubmission diffs against prior run).
- **Accept:** on the Ramp 18-Sep take, reproduces the 6 Fails and ≥15/20 Caveats within 2s of
  MA's; latency within 0.3s of a stopwatch; every in-scope item Ramp didn't show appears in Not
  shown; **no finding cites a rule not in the rule set.**
- **Feedback loop (Phase 4, depends on Phase 0/1 corpus+versioning):** `/amb feedback` →
  split Apple reply into items → AE confirms rule matches → gap classes update the rule set
  (new rule tagged Apple(Review); fix check + regression frame; worked example in prompt; lower
  disputed to Field — never delete). Regression corpus: every Apple'd recording + its final
  findings = a test pair; a new rule-set version ships only if it reproduces all past findings
  with no new false positives. Resubmission summary refuses to generate while any item unresolved.

## Architecture
Three small services + board + bot over one rule set, **separate repo** (not cerebro).
- Rule set: JSON per source → merge → `rules.json`; test every rule cites a source anchor.
- Tools 1&2: CLI first, thin web form second; HTML→PDF (Playwright/WeasyPrint); iPhone frames
  as HTML/CSS to Apple element layouts.
- Tool 3: ffmpeg @5fps; OCR (Apple Vision on Mac, else Tesseract); event detection in Python;
  LLM via Claude API (frames + rule text); shares Tool 2's HTML→PDF path. Runs on Linq Macs
  (Vision OCR, native .mov); container fallback.
- Board: Next.js on Vercel + Linq SSO; one brand/row, stage/col; cells show output+state+date+
  owner; **video upload → blob storage from browser** (Ramp take 17.5MB > Vercel limit); a Mac/
  container **worker** runs Tool 3 and writes back. Board reads the same brand folders the bot writes.
- Slack bot in `#amb-implimenation`: `/amb brand-doc|storyboard|review|feedback|status <brand>`.
- HubSpot (Phase 6, one-way board→HubSpot): deal props AMB approval stage / stage-entered date /
  next-step owner / last-Apple-touch; timeline notes on send/feedback. Phase 0 names props by hand.

## Model placement
Measurement & coverage = code. Judgment = model, constrained to handed rules, frame as
evidence, **required rule ID + timestamp or the finding is dropped.** Measurements are never
the model's.
