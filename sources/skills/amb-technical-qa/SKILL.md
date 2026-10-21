---
name: amb-technical-qa
description: Fact-check and answer technical questions about Apple Messages for Business (AMB) for Linq. Use whenever anyone asks about AMB capabilities, limits, or behavior — message elements (rich links, quick replies, list pickers, time pickers, forms), capability-list and device fallback, Apple Pay, OAuth, tapbacks, entry points and BCRW, attachments, iMessage apps, consent and opt-out, data retention, MSP approval, Experience Review, or Apple's PR rules. Also trigger when verifying an answer already given to a client ("is this right?", "did we tell them the right thing?", "can we say X about AMB?", "does AMB support...?", "what's the limit on...?"), when reviewing collateral or a customer email for AMB accuracy, when a rep needs a sourced answer to send a client, or when someone asks whether AMB is end-to-end encrypted, HIPAA compliant, or reaches Android. Use it even for questions that sound simple — several widely-believed AMB claims are wrong, and this skill carries the corrections.
---

# AMB Technical QA

Verify and answer technical questions about Apple Messages for Business, with the answer traced to a source.

The reason this exists: AMB has a lot of surface area, Apple's documentation sits behind a Business Register login, and several plausible-sounding claims about the channel are false. Answering from memory produces confident wrong answers — which is expensive when the answer is going to a client, into a contract, or into an Experience Review submission.

## Source hierarchy

Rank every claim against these, in order. Say which tier the answer came from.

1. **Apple's REST API documentation** — the specification. Links throughout the reference files. Authoritative on payload shape, field requirements, limits, and OS versions.
2. **Apple's registration, PR, and terms material** — authoritative on process, terminology, and what may be said publicly.
3. **Messaging Advisory guidance** — Apple-derived, but sometimes MA's reading rather than Apple's words. Reference files label these.
4. **Linq's own implementation and measurement** — how Linq built it, and behavior verified against production. Correct for "what do we do," not for "what does Apple require."

When tiers conflict, say so rather than picking silently. A real example: MA's fallback primer says the Form `dynamic.version` must be 1.2; Apple's API spec says 1.1. That conflict is the answer, not a problem to smooth over.

## Answering a fact-check

When someone asks whether a claim is right, open with the verdict, then support it.

Use one of these four:

- **Confirmed** — the claim matches the source.
- **Incorrect** — the source says otherwise. State what's actually true.
- **Partly correct** — the useful case. Name precisely which part holds and which doesn't.
- **Not established** — no source settles it. Say whether it's an open question with Apple or just undocumented, and don't fill the gap with a guess.

Then: the correct statement, the source tier, and a link where one exists. Keep it tight — a rep checking an answer before hitting send does not need an essay.

If the claim is going to a client, add the client-safe phrasing. The gap between "technically true" and "safe to put in writing" is where most of the risk lives, especially on encryption and compliance.

**Example**

> **Q:** A prospect asked if AMB is end-to-end encrypted and our AE said yes. Is that right?
>
> **Incorrect, and this one matters.** AMB is encrypted at rest and in transit within Apple's infrastructure, but Apple acts as an encryption endpoint — messages are decrypted on Apple's servers before being forwarded to us. Apple's PR guidance explicitly prohibits claiming end-to-end encryption, stated or implied. iMessage does have E2EE (quantum-safe), which is where the confusion comes from.
>
> Client-safe phrasing: "Fully encrypted in transit under Apple's infrastructure, with Apple as the encryption endpoint. Nothing is stored at Apple after delivery."
>
> Source: Apple PR guidance (tier 2), consistent with the transport architecture in tier 1.
>
> Worth a correction email if it went out in writing.

## Answering an open question

Same discipline, no verdict line. Answer, cite tier, link. Pull the exact numbers — OS versions, byte limits, timeouts, character caps — rather than approximating, since approximations are what produce the wrong answers this skill exists to catch.

If the question spans several areas, read more than one reference file. Don't answer half from a file and half from memory.

## Reference files

Read the file that covers the question. Each is self-contained.

| File | Covers |
|---|---|
| `references/elements.md` | Capability-list and the fallback cascade; rich links, quick replies, list pickers, time pickers, forms, attachments, Wallet, maps, App Clips, iMessage apps, Apple Music, AR; tapbacks; interactive payload structure and the 10 KB threshold |
| `references/payments-auth.md` | Apple Pay end to end — the three domains, certificates, merchant session fields, endpoints, the merchant-of-record question; OAuth 2.0 / `AUTH2` |
| `references/platform.md` | Channel fundamentals, encryption, identity and Opaque IDs, entry points and BCRW, conversation rules, consent and opt-out, data retention, client landing page, inbound validation |
| `references/experience-review.md` | The Experience Review process end to end — who owns what, the eight steps, the pre-submission quality bar, the three required recordings, resubmission rules, and the UX standards Apple actually flags |
| `references/approval.md` | MSP checklist, brand approval, demo guidance, PR lead times and prohibited language, commercial model |

A "can we do X?" question often has two answers: what the API permits, and what survives Experience Review. They differ more often than people expect — `experience-review.md` closes with a table of exactly where. When a question is about whether something will *launch*, check both files.

## Known-wrong claims

These come up repeatedly and are worth recognizing on sight. Each is expanded in the reference files.

| Claim | Reality |
|---|---|
| "AMB is end-to-end encrypted" | No. Apple is an encryption endpoint. Prohibited claim. |
| "AMB is basically iMessage with an API" | Separate service, separate team, different security model, no group chat, no Android. |
| "It's HIPAA compliant" / "we can BAA it" | Healthcare use cases are not permitted and no HIPAA BAA is published for AMB. |
| "Tapbacks tell you which message was reacted to" | No reference field exists. Reactions to interactive messages collapse to `Liked 1 Business Message` with the prompt text discarded. |
| "There's a sandbox" | There is not. Every call hits production; you use a restricted test Business ID. |
| "List pickers are single-select" | `multipleSelection` is supported per section. |
| "Quick Reply's `summaryText` is the question" | Apple states it is not the intro message. Send a separate text message. |
| "We can pool brands under one Merchant ID" | One Merchant ID per AMB account (reusable across accounts), but you must be merchant of record and `domainName` must match a verified domain. |
| "Apple charges for Apple Pay" | Not within AMB. Subscriptions included. |
| "Apple stores the chat history" | Apple retains nothing after delivery. The MSP is the system of record and the data controller. |
| "Declining a business invitation opts the user out" | It does not. The thread stays open and consent stays intact. Leave Conversation is the opt-out. |
| "Forms just work like a web form" | If the user task-switches out of Messages, the form closes and all responses are lost. Apple documents this and recommends short forms. |
| "The checklist is 76 items" | 74, of which 32 are technical. |
| "We submit one demo recording" | Three: rich features and the main journey, live-agent interaction, and out-of-hours/fallback. |
| "The recording needs to show the agent console" | It does not. Apple reviews the real production journey from the user's point of view on iOS. |
| "We can fix the important feedback items and resubmit" | Partial fixes are treated as a rejection. Address every item and reference each by ID in the resubmission summary. |
| "Apple sends us review feedback directly" | It goes through MA, who is the single point of contact with Apple until MSP status is public. |
| "Experience Review is a technical check" | It's a qualitative evaluation. An experience can pass every technical requirement and still be returned on UX. |

## When the source doesn't cover it

Say so plainly. Three distinct situations, and conflating them misleads people:

- **Undocumented but knowable** — Apple hasn't published it, and testing would settle it. Say what a test would look like.
- **Open with Apple** — already raised, awaiting an answer. `references/approval.md` holds the current list.
- **Interpretation** — MA or Linq has a defensible reading with no Apple statement behind it. Flag it as a reading, especially anything touching compliance, since a reading presented as fact is how a bad commitment gets made.

Never resolve a gap by reasoning from how other messaging channels behave. AMB diverges from SMS, RCS, WhatsApp, and iMessage in ways that are not intuitive, and analogy is the single most common source of wrong answers here.

## Keeping it current

This reflects Apple documentation and Linq's build as of late August 2026, shortly after MSP approval. Apple ships changes to the API and the review process — the Apple Pay API has changed several times, and the reaction set was last expanded in iOS 18. If an answer depends on something that may have moved, or if the person cites behavior that contradicts a reference file, treat the live documentation as authoritative over these notes and say the file may be stale.
