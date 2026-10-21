# Experience Review — Process & Apple's UX Standards

Source: Messaging Advisory's AMB Experience Review Process document, which mirrors Apple's own Experience Review requirements. This is the operational layer on top of the technical specs — it governs how an experience gets built, validated, recorded, submitted, and approved.

The Experience Review is a **qualitative evaluation, not a technical check**. An experience can be technically flawless and still be returned.

## Contents

- [Who owns what](#who-owns-what)
- [The eight steps](#the-eight-steps)
- [The pre-submission quality bar](#the-pre-submission-quality-bar)
- [The recordings](#the-recordings)
- [Resubmission](#resubmission)
- [Apple's UX feedback patterns](#apples-ux-feedback-patterns)
- [Where this sharpens the technical guidance](#where-this-sharpens-the-technical-guidance)

---

## Who owns what

| Party | Owns |
|---|---|
| Messaging Advisory | Process orchestration, the checklist and guidance, internal validation, and **all Apple communication and submission** |
| Linq (the MSP) | Building the AI agent experience, internal testing, addressing feedback, brand and use-case content |
| Apple | Final experience review, the approval decision, feedback on submitted recordings |

**MA is the single point of contact with Apple for the first brand review, until MSP status becomes public.** Apple's feedback always reaches Linq through MA — never directly, and never brand-direct either.

Two facts shape the whole process: Linq builds the experience with its own tools and content, and most AMB experiences today are AI-generated rather than fixed conversational flows. That second point is why checklist-based validation before submission matters more here than it would for a hard-coded flow — non-deterministic output can't be assumed correct because it was correct once.

This process applies to **every** brand experience, not only the first.

## The eight steps

| # | Step | What happens |
|---|---|---|
| 1 | Use case & scope alignment | Linq prepares brand, use case, and design. MA confirms scope and loops in Apple for pre-approval if the use case is non-standard — flagged here so it doesn't surprise anyone later. |
| 2 | Build & internal testing | Linq builds and tests against the use-case checklist. MA provides the checklist (adapted to agreed scope) and technical guidance. |
| 3 | MA validation | Linq shares the live experience. MA validates against the same checklist and issues feedback until it's clean. |
| 4 | Review prep | MA shares Apple's experience-review guide and recording instructions. Linq reviews so expectations are set before recording. |
| 5 | Recording & feedback | Linq records the required videos. MA reviews against the checklist and Apple's guidelines, and Linq re-records until ready. |
| 6 | Submission | MA submits the videos and any additional materials to Apple on Linq's behalf. |
| 7 | Apple review | Apple approves or returns feedback. MA relays it and coordinates resubmission; Linq fixes. |
| 8 | Go-live | Linq launches and monitors. MA supports go/no-go coordination and post-launch monitoring. |

Step 3 exists so that nothing new surfaces once the experience is in front of Apple. MA validates against the same bar Apple will use.

## The pre-submission quality bar

Apple expects all of this before any review begins:

- The AMB account is connected and message delivery confirmed
- Commercial account access is restricted to authorized Apple IDs used for testing (Account Testing → Advanced)
- The test environment is **fully stable** — all entry points, automated responses, live agent handoffs, and edge cases implemented
- Both automation and live-agent interactions configured, activated, and tested end to end
- Every use case tested from the end user's perspective, with all features and content reviewed and errors fixed
- **Tested on real devices.** Never rely solely on simulators. Every flow tested on a physical supported Apple device using the test environment. iOS is the priority platform.
- Agents prepared and trained to handle AMB traffic and the relevant use cases

## The recordings

The recording is the artifact Apple actually reviews. It must reflect the real production user journey on an iOS device, from the user's point of view. **You do not need to show the agent console or backend bot logs.**

Three recordings are required:

| Video | Must show |
|---|---|
| **#1** | Rich features integrated into the experience, showcasing the main use case(s) — the entire customer journey including success paths. Long journeys can be split into multiple parts for clarity. |
| **#2** | The live-agent interaction — user escalates, agent replies, a short sample conversation happens. |
| **#3** | Out-of-hours messages and fallback. |

MA shares a recording guide at Step 4 before recording begins.

## Resubmission

If Apple identifies issues, MA relays them, Linq addresses them, MA resubmits. The loop can repeat.

Two rules make it shorter:

- **Reference every feedback item by ID or description** in the resubmission summary and explain how it was resolved. Reviewers verify fixes faster when they don't have to hunt.
- **Partial fixes equal rejection.** Address every item. A partial fix usually buys another full review round and delays launch.

## Apple's UX feedback patterns

These are the things Apple actually flags. Treat them as design requirements rather than suggestions.

### Onboarding and triage

- **Automated agent disclosure** must happen within the first interaction — "I'm an automated agent" or equivalent. Transparency is mandatory, not stylistic.
- **Initial triage menu.** When intent is unclear at entry, Apple expects a triage menu immediately. A Quick Reply of up to five options is preferred over making the user type or navigate text prompts.
- **Opt-in must be active.** Notifications cannot be enabled automatically — the user chooses, e.g. a "Subscribe" option. The conversation must explicitly say how to opt out ("Reply 'unsubscribe' at any time").

### Conversational flow

- **End with "anything else?"** Apple prefers closing a use case by asking whether the user needs more help — optionally followed by a triage menu — over just terminating the flow.
- **Fallback is required.** When the bot can't help or doesn't understand, it must not go silent or ignore the message. A clear, polite fallback with options is expected.
- **No dead ends.** Every path needs a next step. Even an unanswerable question must offer a fallback or an escalation route.
- **No repetition.** Never ask the customer for information they already gave earlier in the chat.
- **Concise, QuickType-friendly phrasing.** Keep data prompts short and natural.

### Visual UX and component usage

- **Rich Links for all URLs.** Plain text links and tap-to-load links are not acceptable. **The image must accurately reflect the content of the target page.**
- **Iconography.** Every interactive feature — including text messages and *each individual option in a List Picker* — needs a contextually relevant thumbnail or icon so it reads as tappable.
- **Form context goes in a message bubble before the form**, not buried in the form's subtitle, where it can be cropped and missed.
- **Forms need a splash screen** (best practice), a title, an introductory description, and a final review screen.
- **Long text goes outside feature bubbles.** The first line of a feature bubble should be the title — long text gets cropped and becomes unreadable before the user decides.
- **List Pickers only for genuine category variation.** Five options or fewer should be a Quick Reply: faster and less intrusive.
- **Simple inputs should be conversational, not a Form.** For one or two fields (name, email), Apple discourages a formal Form object and prefers plain-text back-and-forth — "What's your full name?" then "What's your work email address?" — to reduce friction.

### Human escalation

- **Out of hours:** state the operating hours clearly and let the user leave an asynchronous message directly in the thread.
- **Transparent handoff:** when a live agent takes over, say so explicitly ("A live agent will join the chat shortly"), and the agent introduces themselves on joining.
- **Communicate wait time** if an agent isn't immediately available.
- **Contextual escalation:** if an email to support is being drafted, help the user compose it in the channel rather than abruptly pushing them out of the conversation.
- **Prohibited phrasing:** never "This conversation has been closed" or anything similar. It reads as abrupt and dismissive. Use friendly closing language that leaves the door open.

### Satisfaction surveys

CSAT fires **only after the entire experience is complete** — never after each individual FAQ interaction, which saturates the inbox and degrades the experience.

### Copy and style

- **Proper casing.** Messages sent entirely in lowercase get flagged as poor UX.
- **Quick Reply summary text** should be a concise label ("Option selected"), not a repeat of the previous message, which bloats the chat history.

## Where this sharpens the technical guidance

Several of Apple's UX standards narrow what the API technically permits. When answering a "can we?" question, the API answer and the review answer can differ — and the review answer is the one that governs launch.

| Technically | But at review |
|---|---|
| List Picker supports any number of items | Use it only for genuine category variation; five or fewer options should be a Quick Reply |
| Forms support single-field pages | One or two fields should be conversational plain text, not a Form object |
| Forms don't require a splash screen | A splash screen is expected best practice, along with a title, intro description, and final review screen |
| List Picker `imageIdentifier` is optional | Every option needs a contextually relevant image; so does every interactive feature |
| Rich link images can come from a fallback chain | The image must accurately reflect the target page's content |
| Nothing requires the bot to handle unrecognized input | Silence or ignoring a message is a rejection |

**Worth flagging on the fallback image library.** Linq's plan for a curated fallback image library with context-based selection is a real differentiator, but Apple's standard is that the rich link image accurately reflects the target page. A generic library image that doesn't match the destination is the exact failure mode Apple describes. The library needs to be genuinely context-matched, not decorative — and OG-first resolution stays the safest default.
