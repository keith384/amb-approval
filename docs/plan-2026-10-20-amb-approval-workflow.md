# AMB Approval Workflow — Build Plan for Zed
Oct 20, 2026 · @Keith

> Source planning document, reproduced verbatim as the repo's reference. The executable
> condensed spec is in `BUILD-PLAN.md`; this is the original narrative.

## Why this exists
Every brand Linq launches on Apple Messages for Business goes through a four-stage Apple approval pipeline, and today each stage is hand-built, slow, and dependent on Messaging Advisory (MA) catching what we miss. The Ramp review came back with 6 Fails, 20 Caveats, 17 things not shown in the recording, and 5 open questions Apple will ask. Most of those were catchable before anyone recorded a video. This build turns the pipeline into three tools that generate the artifacts Apple actually reviews and grade them against Apple's bar before Apple sees them.

What Apple's onboarding email (9 Sep 2026) locks in for us:
- Linq is a Commercial Non-Public MSP until the first brand is live. Nothing about Apple Messages for Business gets published, and all collateral, landing pages, and PR (ours or the brand's) go to Apple for review before publication.
- The first brand launch is a showcase. Use cases and interaction flows go to Apple early for review against platform experience guidelines.
- Terminology is enforced: the channel is Apple Messages for Business in anything customer-facing. No "iMessage for Business", no "Apple Chat", no "AMB" abbreviation, no exclusivity claims ("first MSP", "selected by Apple"), no speaking for Apple. Press goes to media.help@apple.com.
- Two internal aliases are needed (general MSP comms, experience review and mystery shopper) and an MSP account in Apple Business Register using the production URL.

Since September Linq works the review directly with Apple as the MSP: use cases go to business-register@apple.com at qualification, the UX design is shared for alignment, and iPhone POV recordings are uploaded to Apple's Box link (never shared with clients). No consultant sits in the loop going forward: Linq runs every stage internally, and MA's Ramp report is kept only as the reference example of a good review. The existing amb-experience-review skill still describes the older MA-as-gatekeeper flow and needs updating as part of this build.

The three deliverables:
1. **Brand Approval Doc generator**: produces the use-case PDF Apple requires at the Brand Approval stage.
2. **UX Storyboard tool**: turns an approved use-case doc into a storyboard PDF of the conversation layout for UX approval.
3. **Video Review tool**: takes the client-recorded experience video and returns a Messaging Advisory-style findings report before submission.

## The workflow end to end
Four gates, one per stage, each with a hard output Apple reviews. The whiteboard session on 20 Oct mapped each stage across customer, people and process, systems, issues, output and needs; the tools in this plan cover the first three stages, and Launch gets an SOP rather than software.

Each stage is a self-contained loop: build the output, review it internally against Apple's bar, send it, address feedback, resend. Apple reviews the output, never the build.

| Stage | Customer does | Linq does | Tool | Output | Known issues today |
|---|---|---|---|---|---|
| 1. Brand Approval (Explain) | Describes 4 use cases and which features each uses | Kick-off call, follow-up call (brand and UX design) | Brand Approval Doc generator; Claude team space as centralized knowledge | PDF submitted to Apple | Client unprepared; iMessage vs Apple Messages for Business conflict; unclear ownership and AE handoff |
| 2. UX Approval (Show) | Reviews outline and storyboard | Works async in Slack with brand on approval | UX Storyboard tool (today: Figma by hand) | Storyboard PDF | We don't know Apple's expectations in detail; we lack expertise owning this for clients |
| 3. Experience Review (Build) | Records the production experience on iPhone | Reviews video, meets if needed, fixes with brand | Video Review tool (today: MA consultant, trial and error) | Video of production experience, timestamp index, one-pager on full approval | Trial and error; no internal tooling to produce or review videos |
| 4. Launch (Production) | Sets launch volume, timeline, PR approval | Post-launch follow-up: secret shop, account moved to commercial | Launch SOP (no software) | One-pager on launch plans | No SOP exists |

## Tool 1: Brand Approval Doc generator
Produces the use-case PDF Linq sends to business-register@apple.com at qualification. The content is Apple's own Messages for Business Use Cases form (brand, definition of success, requested launch date, entry points in scope, general features, enhanced features, top four use cases each with the enhanced features it uses), plus the narrative Apple asks for on every brand: the use case, how each feature will be used, how the agentic model works, and what value the brand brings to society. Apple's two intake PDFs (Use Cases and Readiness) go with it; both are fillable forms, so the tool fills them from the same answers rather than asking anyone to type into Acrobat.

**Why it matters.** What the brand selects on the Use Cases form is the scope for everything after it. It decides which of MA's 114 test cases apply and what the video has to show. A weak Stage 1 doc is why Ramp's recording came back with 17 items not shown.

**Input**
- Kick-off call transcript (Fireflies or Granola) and the AE's notes from the consultation call
- Brand facts: name, vertical, website, app, support hours, existing bot or agent vendor, live-agent setup
- The four use cases in the customer's words, one sentence each from the customer's point of view (MA's test: "I want to move my delivery to Saturday"; if it cannot be said in one sentence it is a category, not a use case)
- Entry points the brand will actually deploy

**What it does**
1. Interviews for anything missing with a short structured intake (the form's fields, in order), pre-filled from the transcript.
2. Classifies each use case into one of MA's five archetypes (find and choose, book and manage, check and resolve, enrol and receive, reach a person) and proposes the feature fit per archetype from the Standards 2.5 feature inventory.
3. Flags non-standard use cases that need Apple pre-approval at this stage, and flags the consumer-AI pause test (is AI the product or the channel).
4. Runs the terminology lint: no "iMessage", "AMB", "Apple Chat", "chat" or "text" as a channel name, no exclusivity or Apple-endorsement claims, no feature labelled "iMessage app".
5. Renders a PDF in a fixed Linq template and a JSON scope record that Tool 2 and Tool 3 read.

**Output**
- `brand-approval-<brand>.pdf`: cover, company information, scope (entry points, general features, enhanced features as yes/no), four use cases with archetype and feature list, agentic model description, live-agent and out-of-hours model, societal value statement
- `scope.json`: the same answers as data. Every later check reads its "applies when" condition from this file.
- An internal readiness note the AE sees before the client does: open questions, pre-approval flags, terminology hits

**Acceptance**
- Every field on Apple's Use Cases form is present or marked as an open question; nothing invented
- Each use case maps to at least one enhanced feature, or the doc says why the experience is not text-only
- Terminology lint passes on the PDF text and the file name
- A PDF for a known brand (Ramp) reads correctly to the AE who ran the call

The template is settled. The Walmart brand nomination is the format Apple receives, so Tool 1 generates exactly that shape: (1) Header: company, submitted by Linq; (2) Use Case: one paragraph on who the customers are, what they do today, what the brand's assistant already does, and why Messages is where it belongs; (3) At a Glance: The Experience, Why It Fits (naming the feature for each step), Value to Users, Value to Society; (4) Features table: Apple feature and how the brand would use it, one row per feature in scope; (5) Company Background: founded, headquarters, headcount, financials with the latest quarter.

Two things the generator adds: an explicit Entry Points list (Apple's form asks for it), and the terminology lint on the output (the Walmart draft says "an iMessage app brings the Walmart app's product gallery into the chat", the exact label Apple now prohibits; the lint replaces it with the App Extension / embedded app experience wording and flags that the feature is also missing from the Features table). The two Apple PDFs are blank AcroForms with stable field names, filled with pypdf from scope.json. Use Cases has 57 fields; Readiness has 25. Field names are inconsistent ("GF Authenticaiton", "UC4 Rick Links"), so the mapping lives in one file and a test asserts every field is covered. Tool 1 ships three files per brand: the narrative doc, and the two filled forms.

## Tool 2: UX Storyboard tool
Turns the approved scope into a storyboard PDF that shows Apple the conversation layout before anything is built: every bubble, every rich element, every branch, rendered as it will look on an iPhone. Today this is done by hand in Figma.

**Why it matters.** Apple's biggest fail criterion is a text-only experience that does not use platform features. The storyboard is where that gets caught, because it forces every step to declare which element it uses. It's also the cheapest place to apply the Standards 2.18 self-check.

**Input**
- `scope.json` from Tool 1
- A conversation script per use case in a simple authored format: one line per step with the actor (customer, bot, human agent), the element kind, the copy, and the options (YAML or JSON flow file with a kind field per step)
- Brand assets: logo, element thumbnails, a fallback image, brand colors

**What it does**
1. Validates each script against the storyboard rules before rendering, and refuses to render a step that breaks a blocker-level rule: automated disclosure in the opener, a Quick Reply triage of up to 5 real intents, a framing bubble before every rich element, a confirmation after every tap, no bare URL, five-or-fewer options as Quick Reply not List Picker, a route to a person on every menu, an "anything else" before close, and an out-of-hours and fallback path present.
2. Renders each step as an iPhone frame with the element drawn to Apple's layout, labelled with the step number and the test case Refs it evidences.
3. Lays the frames into the three flows the recording guide requires: Flow A the use case end to end, Flow B the human handoff side by side with the console, Flow C degraded conditions.
4. Emits a shot list: the same steps as a numbered table, which becomes the recording script and the timestamp index skeleton for Stage 3.

**Output**
- `storyboard-<brand>.pdf`: cover, scope summary, one page per flow, each step an annotated iPhone frame, a final page with the Standards 2.18 self-check results
- `shotlist-<brand>.json`: ordered steps with the element and the checklist Refs each step is expected to evidence

**Acceptance**
- Every rich element in scope.json appears at least once in the storyboard, or the storyboard says why not
- A storyboard for Ramp's expense-support use case reproduces the Ramp flow and would have flagged at least the six Fails before recording
- Renders in under a minute; reviewable in Slack as a PDF

**Scope boundary.** The tool renders what the script says; it does not author the brand's bot. Keep the authored format simple enough that an AE or the brand's product owner can edit it.

## Tool 3: Video Review tool
Takes the client's iPhone recording and returns the kind of report MA produced for Ramp, before Apple sees the video. The Ramp report (9 Oct 2026) is the reference output.

**What the Ramp report does that the tool must reproduce**
- Five buckets: Fail, Caveat, Not shown (Mandatory), Not shown (Recommended), Apple will ask
- Every finding has a timestamp range, a test ID and name, the issue in one line, and the fix in one line
- Timings are measured, not eyeballed
- "Not shown" is derived from the feature list and the archetype: features in scope that never appear on screen are listed as gaps, not passed by default
- "Apple will ask" captures what the recording cannot answer and the brand must state in writing
- A header count: 6 Fail, 20 Caveat, 8 Not shown Mandatory, 9 Not shown Recommended, 5 Apple will ask

**Input**
- The recording (.mov or .mp4), one or more takes, iPhone POV; for Flow B a side-by-side capture. Ramp's submitted video is 7 min 34 s, 592 by 1280, 30 fps, 17.5 MB. MA's report was written against the 18 Sep take.
- scope.json and shotlist-<brand>.json from Tools 1 and 2
- Optional: the brand's feature list and the timestamp index if the client supplied one

**Pipeline**
1. Frame extraction at 5 fps and an OCR pass over every frame, producing a timed transcript of every bubble, chip, picker row, card and system label on screen, tagged customer or business side.
2. Event detection on that transcript: message appeared, typing indicator started and stopped, element rendered, tap occurred, screen changed, cut detected.
3. Rule evaluation. Each rule is a function over the event stream plus scope, returning pass, fail, caveat, not shown, or a question. Deterministic rules run first; an LLM pass then judges the qualitative rules using the frames at each timestamp, with the rule text and the Ramp report as examples.
4. Coverage check: everything in the shot list and every feature in scope that has no evidence row becomes a Not shown item, split Mandatory or Recommended by the rule's severity.
5. Report render: the Ramp layout as PDF plus a Markdown version for Slack, and the timestamp index.

**Output**
- `review-<brand>-<date>.pdf` in the Ramp format, with a verdict line
- `timestamp-index-<brand>.txt` in MA's format
- `review.json`: findings as data so a resubmission summary can be generated later

**Acceptance**
- Run on the Ramp recording of 18 Sep, the tool reproduces the six Fails and at least 15 of the 20 Caveats with timestamps within 2 seconds of MA's
- Latency measurements agree with a stopwatch to within 0.3 s
- Every item in scope that Ramp did not show appears in Not shown
- No finding cites a rule that does not exist in the knowledge base

**Where the LLM sits.** Measurement and coverage are code. Judgment is the model, constrained to rules it is handed, with the frame as evidence and a required timestamp.

## The feedback loop from Apple
Apple's verdict is the ground truth; MA's report and our tool are proxies. Every time Apple returns an item the tool did not flag, that gap is a defect in the rule set, fixed before the next brand.

- The AE pastes Apple's feedback into `/amb feedback` with the brand and the recording it refers to. The model splits it into items, each with Apple's wording, the timestamp if given, and a proposed match to a rule ID. The AE confirms the matches; nothing is learned from an unconfirmed item.
- MA's Ramp report is loaded once as a seed, labelled MA, as a (Review) pattern one tier below Apple's own words.

Gap classes → rule-set changes: Matched (nothing); Missed no rule (new rule, source Apple (Review)); Missed rule exists check failed (fix the check + regression frame); Missed rule exists judgment failed (worked example in the prompt, re-run corpus); Disputed (lower severity to Field, never delete); Apple-will-ask answered (nothing); Apple-will-ask unpredicted (add to Apple-will-ask rules).

**Regression corpus.** Every recording that has been through Apple is stored with its final Apple findings as a test pair. A new rule-set version ships only when it reproduces every Apple finding and does not add false positives on approved recordings.

**Resubmission summary.** The reconcile step generates the summary Apple expects (item, how resolved, video + timestamp), and refuses while any item is unresolved.

**Versioning.** The rule set carries a version and a changelog line per change. Each review states the rule-set version it ran on. The two Claude skills are regenerated from the rule set on each version.

**Open question.** The format Apple's feedback arrives in now that Linq submits directly decides how much the ingest step can parse automatically. Keith to share the first Apple reply once there is one.

## Shared knowledge base: the rules engine
All three tools read one rule set. A rule is a record: ID, name, the check in plain words, severity (Non negotiable, Apple standard, Field), source tag and anchor, applies-when condition keyed to scope.json, which stage it applies to (doc, storyboard, video), and whether it is machine-checkable or needs the model. The build is extraction and normalization, not authoring. Where a source is silent, the rule set is silent.

Sources: MA combined package v1.1 (process, Standards 2.1–2.18, 114 test cases, recording guide, the 10 reasons recordings come back); MA checklist workbook v2.0 (114 cases as rows + Appendix A/B); MA Ramp report (9 Oct 2026; the video-review test IDs A1–I5, X0, RL/AT/LP/TP/FM/AP/AU/IA, the five-bucket format); Apple onboarding email (9 Sep 2026); amb-experience-review skill; amb-technical-qa skill; MA AMB kit (Apple's docs as canonical, 49 JSON schemas); cerebro Experience Review readiness.

**One ID scheme.** The 114 test cases use numeric Refs; the Ramp report uses letter IDs. The rule set carries both where they map, and the tool reports in the letter scheme.

**The five Apple checks every time.** Reachable escalation, honest automation, Leave Conversation respected with a blocked send shown, capability-aware fallback filmed at send time, clean language. Non negotiable tier; block submission regardless of score.

**The ten reasons recordings come back** (first ten video rules): typing indicator missing on a back-to-back sequence; rich card filmed without its own image; Leave Conversation asserted not demonstrated; bare URL or tap-to-load link; fallback described in narration not filmed; placeholder content; rehearsal threads visible; restricted wording in voiceover; out of hours filmed as a generic greeting; features included because they were on a list.

## Architecture and stack
Three small services over one rule set, kept out of the cerebro repo (a new repo `amb-approval` with the rule set as a versioned JSON package).

- Rule set: one JSON file per source, a build script that merges them into rules.json; a test that every rule cites a source anchor
- Tool 1 and Tool 2: a CLI first, a thin web form second; PDF rendering from HTML (Playwright or WeasyPrint)
- Tool 3: ffmpeg for frame extraction at 5 fps; OCR per frame (Apple Vision on a Mac, or Tesseract); event detection in Python; the LLM pass through the Claude API; report rendering shares Tool 2's HTML-to-PDF path
- Model use: Claude for intake interviewing, script validation, qualitative judgment. Every model finding must carry a rule ID and a timestamp or it is dropped
- Where it runs: Linq Macs (Vision OCR, QuickTime-native .mov); container fallback

**Integration points.** Transcripts (Fireflies/Granola); Slack bot; Claude team space (skills become the human-readable layer over the rule set); HubSpot (later phase); Apple (email + Box upload stay manual, Linq-only).

**Slack bot** in #amb-implimenation: `/amb brand-doc <brand>`, `/amb storyboard <brand>`, `/amb review <brand>`, `/amb feedback <brand>`, `/amb status <brand>`. Long runs acknowledge immediately and post when done. Every artifact is written to the brand's folder.

**Pipeline board.** A simple internal web app on Vercel behind Linq SSO. Rows are brands; columns are the four stages. Each cell shows the stage's output, its state, the date it last moved, and who owns the next step. Video upload inside the board goes straight to blob storage from the browser (Ramp take is 17.5 MB); a worker outside Vercel runs Tool 3 and writes back.

**HubSpot sync, later phase.** One direction, board to HubSpot, on: stage moved, output sent to Apple, Apple feedback received, approved, launched. Writes four deal properties and a timeline note. Phase 0 names the properties by hand; the sync itself is Phase 5/6.

## Build sequence
Five phases in dependency order, HubSpot sync a sixth (scoped, unscheduled). The rule set is the foundation and ships first; the video reviewer goes next because Ramp's recording and MA's report give a complete test pair, and Stage 3 is where trial and error is most expensive today. Phase 1 (frame extraction, OCR, event detection, typing-indicator timing at 5 fps) is the one to size carefully. Phases 2 and 3 are mostly templating once the rule set exists. Phase 4 is the handoff to sales + the feedback-ingest/reconcile step. The regression corpus and rule-set versioning are built in Phases 0 and 1.
