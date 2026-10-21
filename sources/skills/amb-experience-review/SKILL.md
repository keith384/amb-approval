---
name: amb-experience-review
description: Run Linq's Apple Messages for Business (AMB) Experience Review workstream — getting a brand experience validated, recorded, and approved by Apple via Messaging Advisory (MA). Use whenever anyone is preparing, auditing, or troubleshooting an AMB experience ahead of Apple submission. Trigger on "review this experience", "will this pass Apple", "experience review", "Apple submission", "pre-submission checklist", "we got Apple feedback", "Apple rejected us", "resubmission", "what videos does Apple need", "what does MA need from us", "walk the client through the process", "quick reply or list picker", "does this flow dead-end", or anything about Apple's UX bar for bots, escalation, forms, rich links, out-of-hours, or CSAT timing. Also trigger when reviewing a customer's conversational flow, script, or bot design even if Apple isn't mentioned — every brand experience goes through this review, and catching issues before MA sees them is the point. For what AMB can technically do, use amb-technical-qa instead.
---

# AMB Experience Review

Get a brand's AMB experience through Apple's Experience Review on the first submission.

The reason this exists: Apple's Experience Review is a **qualitative** evaluation, not a technical conformance check. An experience can be fully functional, pass every API validation, and still be returned because the bot didn't disclose it was automated, or a URL was sent as plain text, or a flow dead-ended. Each rejection round costs a re-record and another wait on Apple. The failure modes are known and repetitive, so nearly all of them can be caught before submission — which is what this skill is for.

## The setup you're operating in

Linq is the **MSP**. Messaging Advisory (**MA**) owns the Experience Review workstream and is the single point of contact with Apple for the first brand review, until MSP status becomes public. Apple's feedback always arrives through MA — never directly.

That means Linq's job is: build the experience, test it internally, fix what MA flags, record the videos, and address Apple's feedback. MA's job is: supply the checklist, validate before Apple sees it, submit, and relay feedback. Never suggest contacting Apple directly, and don't promise a client an Apple timeline Linq doesn't control.

This process applies to **every** brand experience launched, not just the first one.

## Pick the mode

Four things people actually need. Identify which before answering.

| Mode | Trigger | What to produce |
|---|---|---|
| **Audit** | "review this", "will this pass", a flow/script/transcript/screenshots dropped in | Findings report — see below |
| **Process brief** | "what's the process", "what does MA need", client asking about timeline | Step walkthrough with owners, from `references/process-and-roles.md` |
| **Recording prep** | "what do we record", "is this video enough" | The three-video spec and QA gate, from `references/process-and-roles.md` |
| **Feedback response** | "Apple came back with...", "how do we resubmit" | Item-by-item resolution summary — see below |

When it's ambiguous, audit. It's the highest-value default.

## Mode 1: Audit

Read `references/apple-ux-standards.md` before auditing. It carries the full standard, organized as reviewable checks with the failure mode for each. Don't audit from memory — the list is long and the misses are specific.

Also confirm the QA bar in `references/process-and-roles.md` is met. A beautiful flow submitted from an unstable test environment still fails.

Grade every finding into one of three buckets. The severity is what makes the report actionable, so don't hedge:

- **Blocker** — Apple will return the submission for this. Automated-agent disclosure missing, plain-text URLs, dead ends, auto-enabled notifications, silent fallback.
- **Fix before submission** — likely to draw feedback and cheap to fix. Missing icons, form without a splash screen, List Picker used for four options, all-lowercase copy.
- **Polish** — won't fail review, will make the experience better.

### Findings report format

```
# AMB Experience Review — [Brand] — [date]

**Verdict:** Ready to submit / Fix blockers first / Not close yet
**Blockers:** N  |  **Fix before submission:** N  |  **Polish:** N

## Blockers
### [Short title]
**Standard:** [which section of the Apple UX standard]
**What's happening:** [the specific place in the flow]
**Why Apple returns this:** [one line]
**Fix:** [concrete change, with the replacement copy or component where useful]

## Fix before submission
[same shape]

## Polish
[one line each]

## Not verifiable from what I was given
[what still needs checking on a physical device — be explicit rather than assuming it passes]
```

That last section matters. Most of what gets shared is a script or a screenshot, and half the standard is about runtime behavior — live agent handoff, out-of-hours, fallback on unrecognized input. Say plainly what wasn't testable rather than implying a clean bill of health.

When the fix is copy, write the replacement copy. "Add a fallback message" is less useful than the actual line the bot should send.

## Mode 2: Process brief

Walk the eight steps with owners from `references/process-and-roles.md`. Adjust the register to the audience — an internal Linq rep needs the hand-offs and what's blocking, a brand contact needs what's expected of them and when.

Two things to state up front every time, because they are the most common source of surprise:
1. If the use case is non-standard, Apple pre-approval is needed at Step 1 — flag it then, not later.
2. Apple's review turnaround isn't controlled by Linq or MA. Don't quote one.

## Mode 3: Recording prep

The recording is the artifact Apple actually reviews — the build is only seen through it. Pull the three-video spec from `references/process-and-roles.md`, and check the proposed recording against it before anyone spends time filming.

Note that MA shares a recording guide at Step 4. If someone is about to record without it, tell them to get it first.

## Mode 4: Feedback response

Apple's feedback comes through MA. Two rules govern the resubmission, and both come straight from the process:

- Reference each feedback item by its ID or description and explain how it was resolved. Reviewers verify faster when they can match fixes to items.
- **Partial fixes get rejected.** Address every item. Shipping a partial fix buys another full review round.

### Resolution summary format

```
## Resubmission summary — [Brand]

| # | Apple's feedback | How we resolved it | Where to see it |
|---|---|---|---|
| 1 | [item as Apple worded it] | [the change made] | [Video 1, 0:42] |
```

If an item can't be resolved as asked — a product constraint, a conflict with another requirement — say so in the summary with the reasoning and what was done instead. Silently skipping it reads as a partial fix.

## Working with the other AMB skill

`amb-technical-qa` answers what AMB supports and where the limits are, with sourcing. This skill answers whether a built experience will be approved. Audits routinely surface capability questions — "can a Quick Reply hold six options?" — and those should be resolved against `amb-technical-qa` rather than guessed at, since a wrong capability answer inside an audit produces a fix that itself fails review.

## Where the source material lives

- `references/apple-ux-standards.md` — the six categories of Apple design feedback, as a review checklist. Read this for any audit.
- `references/process-and-roles.md` — roles, the eight steps, the pre-submission QA bar, recording spec, and post-submission loop. Read this for process, recording, and feedback modes.

Both are derived from MA's *AMB Experience Review Process* overview and reflect the feedback patterns Apple has actually returned. Where something isn't covered there, say it isn't rather than extrapolating — a fabricated Apple requirement sends a client to fix a non-problem and costs credibility when MA contradicts it.
