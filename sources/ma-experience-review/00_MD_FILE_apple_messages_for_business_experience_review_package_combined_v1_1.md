# Apple Messages for Business

# Experience Review, complete document package

**Prepared by Messaging Advisory** Combined edition, version 1.1, 1 September 2026

## About this file

This is the full Messaging Advisory Apple Messages for Business Experience Review package as one machine readable markdown file, for teams loading it into their own AI tooling. It contains all four documents plus the complete list of 114 test cases from the checklist.

Standards content is current to Apple's v3.1 documentation of 21 July 2026, the Apple feedback update of 30 July 2026, and the experience items of the integration checklist update of 25 August 2026\.

## How to cite from this file

Rules carry a source tag in square brackets: \[CDS\], \[MWYC\], \[Journey\], \[Ops\], \[ER\], \[Checklist\], \[Feedback\]. A rule with a tag is Apple's. A statement marked (Field) is a Messaging Advisory observation and carries no Apple authority. A statement marked (Review) is a pattern from real Apple feedback. Never present a (Field) statement to a client as an Apple requirement.

**Anchors.** Section numbering inside Part 2 is stable across versions. Cite as "Standards 2.6" rather than by page or heading text. Test cases are cited by their Ref, for example "5.2".

## Contents

* Part 0\. Package cover note, version 1.0  
* Part 1\. Experience Review Process Overview, version 2.1  
* Part 2\. Conversation Design Standards and Best Practices, version 2.1  
  * Section 2\. Apple's standard, subsections 2.1 to 2.18  
  * Section 3\. What we have seen in reviews, subsections 3.1 to 3.9  
* Part 3\. Experience Review Checklist and Test Cases, version 2.0, all 114 rows  
* Part 4\. Brand Experience Review Recording Guide, version 1.0

Not included here, distributed separately:

* The checklist as a working spreadsheet, with the Summary, Legend and the two Apple appendix tabs  
* Apple, Messages for Business Readiness Review, form  
* Apple, Messages for Business Use Cases, form

\========

# Part 0\. Package cover note

## Apple Messages for Business

### Experience Review: the document package

*Start here*

**Prepared by Messaging Advisory** Version 1.0  |  31 August 2026

### Document metadata

* document: Experience Review package cover note  
* version: 1.0  
* scope: what is in the package, who reads what, and what you owe back at each step  
* audience: everyone involved, once

### What this is

Four documents and two Apple forms that take a brand from kickoff to an approved Apple Messages for Business experience. They are designed to be read in order and used at different moments, and there is deliberately no overlap between them. If you find the same rule stated in two places, tell us, because that is a defect rather than emphasis.

### What each one is for

| \# | Document | What it answers | Who reads it | When |
| :---- | :---- | :---- | :---- | :---- |
| **0** | Package cover note (this document) | Where to start | Everyone, once | First |
| **1** | Experience Review Process Overview | Who does what, in what order, and what Apple's pass and fail criteria are | Sponsor, programme manager, everyone once | Kickoff, before any build |
| **2** | Conversation Design Standards and Best Practices | Every rule Apple documents, source tagged, plus what we have seen in real reviews | Conversation designers, product owners, build team | Throughout design and build |
| **3** | Experience Review Checklist and Test Cases | The evidenced test record you fill in against the live build | Whoever tests, and MA at validation | Steps 2, 3 and 5 |
| **4** | Brand Experience Review Recording Guide | What the videos must show, and how to make them worth watching | Whoever holds the phone | Steps 4 and 5 |

Two Apple forms travel with the package as reference documents. They are Apple's own files, used as issued, and Apple asks brands to complete both at the start of the engagement.

| Reference document | What it is for | When |
| :---- | :---- | :---- |
| **Messages for Business Readiness Review** | Apple's qualification questionnaire: fit, scale, economics and operating model | Step 1, before scope alignment |
| **Messages for Business Use Cases** | Apple's scope form: entry points, features and your top use cases | Step 1 |

Both are also mirrored as fillable tabs inside Document 3, Appendix A and Appendix B, so the answers sit alongside the tests they govern.

A combined markdown file containing Documents 0, 1, 2 and 4 plus the full test case list is provided alongside them, for teams who want to load the package into their own AI tooling.

### The shortest useful path

1. Read Document 1 once, end to end. It is short and it sets every expectation.  
2. Complete Apple's two forms. The Use Cases form is the scope agreement for everything that follows, so answer it carefully. Record the same answers in Appendix A of Document 3\.  
3. Design and build against Document 2\. Use the self check at Section 2.18 as you write.  
4. Test against Document 3, filling in the Evidence column as you go.  
5. Read Document 4 before you film, not after. Pick one primary use case and build the recording around it.  
6. Film, then send the videos and the timestamp index to MA.

### What you owe back, and when

| Step | What we need from you |
| :---- | :---- |
| **1** | Both Apple forms completed, and confirmation of the use cases and entry points in scope |
| **2** | Access to the live experience in your test environment, and confirmation that agents have been briefed |
| **3** | Fixes against MA's feedback, until the checklist is clean |
| **4** | Confirmation that the scope on the Use Cases form is still current |
| **5** | The recordings and the timestamp index |
| **7** | Fixes against Apple's feedback, all of them, plus a summary naming each item and how it was resolved |
| **8** | A go or no go decision, and post launch monitoring on your side |

Ideally we also get access to the test experience before you film, so we can give direct feedback before you commit a day to recording.

### Three things that catch everyone

**Naming.** Apple requires the full name **Apple Messages for Business** and prohibits the abbreviation "AMB". Correct product naming is one of Apple's stated pass criteria, so it applies to conversation copy, interface labels, localisation bundles, marketing, file names you share externally, and anything you say out loud in a recording voiceover. The full table is at Section 2.12 of Document 2\.

**Scope is a decision, not a default.** What you select on Apple's Use Cases form decides which of the 114 test cases apply and what the recordings have to show. Change it after submission and both move with it, so tell us before you film.

**The recording is the artifact.** Apple never opens your build. They watch what you filmed and judge the channel on that. Document 4 exists because a perfect build filmed carelessly comes back, and so does a beautiful film with a rule broken in shot.

### Versions

| Document | Version | Date |
| :---- | :---- | :---- |
| 0\. Package cover note | 1.0 | 31 August 2026 |
| 1\. Experience Review Process Overview | 2.1 | 31 August 2026 |
| 2\. Conversation Design Standards and Best Practices | 2.1 | 31 August 2026 |
| 3\. Experience Review Checklist and Test Cases | 2.0 | 31 August 2026 |
| 4\. Brand Experience Review Recording Guide | 1.0 | 1 September 2026 |

Standards content is current to Apple's v3.1 documentation of 21 July 2026, the Apple feedback update of 30 July 2026, and the experience items of the integration checklist update of 25 August 2026\. Apple's two intake forms predate that documentation, so confirm with your Apple business development contact that you hold the current versions.

Questions on any of this go to Messaging Advisory. We are the single point of contact with Apple for the first brand review.

\========

# Part 1\. Experience Review Process Overview, version 2.1

## Apple Messages for Business

### Experience Review: Process Overview

*How Messaging Advisory leads the design, build and Apple approval of your Apple Messages for Business experience*

**Prepared by Messaging Advisory** Version 2.1  |  31 August 2026

### Document metadata

* document: Experience Review Process Overview  
* version: 2.1  
* scope: process only. Standards, checklists and recording rules live in the companion documents below.  
* audience: brand and provider teams launching an Apple Messages for Business experience

### How to read this

This is one of four documents. It covers the **process**: who does what, in what order, and what has to be true before anything reaches Apple. It deliberately contains no design standards and no test cases. Those live elsewhere.

| Document | What it is for | When you use it |
| :---- | :---- | :---- |
| **1\. Experience Review Process Overview** (this document) | The workstream, roles, the eight steps, Apple's pass and fail criteria | Read first, at kickoff |
| **2\. Conversation Design Standards and Best Practices** | Every rule Apple documents, source tagged, plus what we have seen in real reviews | During design and build |
| **3\. Experience Review Checklist and Test Cases** | The test case template you fill in against the live build | Steps 2, 3 and 5 |
| **4\. Experience Review Recording Guide** | What Apple expects from the submitted videos and how to capture them | Steps 4 and 5 |

Two Apple forms are supplied with the package as reference documents. They are Apple's own files and are used as issued, not reproduced here:

| Reference document | What it is for | When you use it |
| :---- | :---- | :---- |
| **Messages for Business Readiness Review** | Apple's qualification questionnaire: fit, scale, economics and operating model | Step 1, before scope alignment |
| **Messages for Business Use Cases** | Apple's scope form: entry points, features and your top use cases. This is what defines scope for the checklist and the recordings. | Step 1 |

Replace `[BRAND]` and the bracketed examples with your own.

#### A note on naming

Apple requires the full name **Apple Messages for Business** in customer facing and public materials, and explicitly prohibits the abbreviation "AMB" in public communications. Where the short form appears in our internal working files it must not survive into anything you publish, and it should not appear in file names you share externally. Correct product naming is one of Apple's stated pass criteria, so this is a review item and not a style preference. The full naming table is at Section 2.12 of the Standards document.

### 1\. Why this document

This sets expectations for how Messaging Advisory ("MA") will run the Apple Messages for Business experience workstream with you, from day one of the project through to go live. It applies to every brand experience you launch, not only the first one.

Two things shape it:

* You build the experience, the AI agent and the conversational flows, using your own tools and content. MA does not build them for you.  
* Most experiences today are AI generated rather than fixed conversational flows, which makes structured, checklist based validation before submission even more important.

Because of this, MA owns and runs the process below on every engagement. We follow it consistently so that what Apple sees is ready the first time it is submitted, and so you always know what is coming next and who owns it.

We align you to this process at the very start of the project so that roles, hand-offs and the definition of "done" at each stage are clear before any build work begins. If your use case needs Apple's pre approval as a non standard experience, we flag that explicitly at Step 1 so it does not surprise anyone later.

Note: While MA can support you in the future with other brands, the goal is for you to become an autonomous experience builder from beginning to end.

### 2\. Roles and ownership

One rule sits above every step. MA owns this workstream and is the single point of contact with Apple for the **first brand review**, until the provider becomes public. Apple's feedback will always reach you through us.

| Party | Owns | Does not own |
| :---- | :---- | :---- |
| **MA** | Process orchestration, checklist and guidance, internal validation, all Apple communication and submission | Building the experience itself |
| **Client and provider** | Building the AI generated or AI agent experience, internal testing, addressing feedback, brand and use case content | Talking to Apple directly, submitting to Apple |
| **Apple** | Final experience review, approval decision, feedback on submitted recordings | Working with the client directly during review, which always goes via MA |

Two workstreams run in parallel and are easy to conflate. The **experience review** is what this document covers. **Marketing and press** runs on its own Apple approval track with a six week lead time, described at Section 2.17 of the Standards document. If you intend to announce, that clock should start before the experience review finishes.

### 3\. The process, step by step

This is the process we follow for the first brand experience. It mirrors Apple's own Experience Review requirements and the milestones in the project plan. The final column points at the rules each step is validated against, all of which live in the Standards document.

| Step | What happens | Client | MA | Apple | Validated against |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1** | **Use case and scope alignment** | Completes Apple's Readiness Review and Use Cases forms, supplied with this package; defines channel goals and prepares the brand, use case and design to go live with | Confirms use case, experience and scope; loops in Apple for pre approval if the use case is non standard, can predesign mocks if those can help to speed the process up | Pre approves non standard use cases when required | Standards 2.1, 2.5, 2.13; Apple's Readiness Review and Use Cases forms |
| **2** | **Build and internal testing** | Builds the AI agent experience and runs internal testing against the checklist | Provides the checklist adapted to the agreed scope, plus technical guidance; available during the build | — | Standards, all of Sections 2 and 3; Checklist |
| **3** | **MA validation** | Shares the live experience; addresses MA's feedback and fixes | Validates the live experience against the same checklist; issues feedback until it is clean | — | Checklist |
| **4** | **Review prep** | Reviews the Recording Guide and the example video so expectations are clear | Shares the Recording Guide, recording instructions and an example video, generic or from a prior live brand | — | Recording Guide |
| **5** | **Recording and feedback** | Records the required videos; re records after feedback | Reviews the videos against the checklist and Apple's guidelines; gives feedback until ready | — | Recording Guide; Checklist Section 11 |
| **6** | **Submission** | — | Submits the videos and any additional materials to Apple on the client's behalf | Receives the submission | — |
| **7** | **Apple review** | Supports fixes if Apple requests changes | Relays Apple's feedback; coordinates any re submission | Reviews the experience; approves or returns feedback | Sections 6 and 7 of this document |
| **8** | **Go live** | Launches the approved experience; supports post launch monitoring | Supports go and no go coordination and monitoring post launch | — | Standards 2.15, 3.9 |

**A note on the Use Cases form.** What you select on it is the scope for everything that follows. It sets which test cases in Document 3 apply and which are marked not applicable, and it is the shot list for the recordings in Document 4\. If scope changes after you submit it, tell MA before filming.

### 4\. The quality assurance bar before we submit anything

Apple expects a specific quality bar before any experience review begins. We validate against this same bar internally at Step 3, so nothing new surfaces once we are in front of Apple. The review is conducted in your **test environment** and is a qualitative evaluation, not just a technical check.

* Apple Messages for Business account is connected and message delivery is confirmed  
* Commercial account access is restricted to authorized Apple IDs used for testing, under Account Testing then Advanced  
* The test environment is fully stable before submission. All entry points, automated responses, live agent handoffs and edge cases are fully implemented  
* Both automation and live agent interactions are configured, activated and tested end to end  
* Every use case has been tested from the end user's perspective, with all features and content reviewed and any errors fixed  
* Testing happens on real devices. Never rely solely on simulators. Test every flow on a physical, supported Apple device using your test environment. iPhone iOS devices are the priority as the primary platform, and macOS should also be tested  
* Agents are prepared and trained to handle Apple Messages for Business traffic and the relevant use cases  
* Baseline metrics are planned **before** launch, not after

Then run the checklist in full. That is Document 3\.

### 5\. What the screen recording must show

The recording at Step 5 is the artifact Apple actually reviews. The full rules, the capture setup and the pre record checklist are in the Recording Guide, Document 4\. In summary:

* The recording reflects the real production customer journeys on an iOS device, from the **customer's point of view**.  
* You do not need to show the agent console or backend logs, with one exception. Where a live agent is involved, a side by side capture of the console and the device is what demonstrates the handoff properly.  
* Three recordings are required, and they can be separate or in combination:  
  * **Video 1\.** Rich features integrated in the experience, showcasing the main use cases and the entire customer journey including success paths. If the journey is long, split it into multiple parts for clarity.  
  * **Video 2\.** The live agent interaction. The customer escalates, an agent replies, and a short conversation happens.  
  * **Video 3\.** Out of hours messaging and fallback.

Before anything goes to Apple, MA reviews the video and also tests the real device experience as a tester. If the experience is not on par with expectations, we give you feedback and iterate until you are ready for submission.

### 6\. What happens after submission

Apple reviews the submitted recordings and sends feedback to MA. If Apple identifies issues, we relay them, you address them, and we re submit. This loop can repeat until the experience is approved. Once approved, we move to go live and post launch monitoring together.

**Most accounts require one to three rounds of review.** Plan for two. The fastest way to reduce iterations is to design the conversation flows with the platform's capabilities in mind from the start, rather than building a text experience and decorating it afterwards.

### 7\. Feedback management

* When resubmitting, include a summary that explicitly references each feedback item by its ID or description and explains how you resolved it. This helps Apple's reviewers verify your fixes faster.  
* **Partial fixes equal rejection.** Address *all* feedback items. Submitting a partial fix usually leads to another round of review and delays your launch.

### 8\. Apple's own pass and fail criteria

Apple evaluates the full customer journey, from entry point setup through to full conversation resolution, in your test environment, including border situations. It is not just a technical check. Language, tone, flow, clarity and proper use of features are all assessed.

**What passes**

* Clear flows  
* Proper feature usage  
* Correct product naming  
* Automated agent disclosure  
* A complete end to end experience

**What fails**

* **Text only experiences that do not leverage platform features**  
* Dead ends  
* Missing disclosures  
* Incorrect product naming  
* Bare URLs  
* Broken flows  
* Lack of images  
* Slow response times  
* Poor human agent console interactions  
* Missing or broken fallbacks  
* Policy violations

Read that fail list before you read anything in the Standards document. The first is the one that catches AI generated experiences most often. An assistant that answers everything correctly, in prose, with no Quick Reply, no List Picker, no Rich Link, no Forms and no images, fails on that criterion even when every answer is right.

### Reference documents supplied with this package

Two Apple forms travel with this package. They are Apple's own files, used as issued. Do not recreate them.

**Messages for Business Readiness Review.** Apple's qualification questionnaire. It establishes whether the channel fits the business and at what scale: vertical and coverage, the digital priorities you are optimising for, your existing messaging platform and executive sponsorship, expected containment from automation, conversation volumes at launch and at 12 and 24 months, cost per inquiry for voice against digital, and your Apple device share. It is a commercial and operational document. Nothing in it is tested against a build. MA collects it, reviews it with you, and uses it to size the engagement and frame the conversation with Apple. The containment figure and the cost per inquiry bands are the two answers Apple returns to most often, so give real numbers rather than estimates you would not defend.

**Messages for Business Use Cases.** Apple's scope form: brand, definition of success, requested launch date, the entry points you will use, the general features, and your top four use cases each with their enhanced features. This is the most load bearing document in the set and the easiest to underestimate. See the note at Section 3\.

Both forms are Apple issued and predate the July 2026 documentation, so confirm with your Apple business development contact that you have the current versions. One of them labels a feature "iMessage app", which conflicts with the naming rules now in force; that label must not travel into anything customer facing.

### Provenance

* Apple, Pass the Experience Review v3.1, 21 July 2026  
* Apple, Ops and Marketing Preparation v3.1, 21 July 2026  
* Apple, Messages for Business Readiness Review  
* Apple, Messages for Business Use Cases  
* Messaging Advisory, Experience Review Process Overview v1.x  
* Messaging Advisory, Experience Review: Process, Apple's Standard, Field Experience v1.0, 28 August 2026, Section 1

\========

# Part 2\. Conversation Design Standards and Best Practices, version 2.1

## Apple Messages for Business

### Conversation Design Standards and Best Practices

*What Apple documents, what Apple has told us directly, and what we have seen in real reviews* **Prepared by Messaging Advisory** Version 2.1  |  31 August 2026

### Document metadata

* document: Conversation Design Standards and Best Practices  
* version: 2.1  
* scope: design standards only. The process is in Document 1\. The test cases are in Document 3\. The recording rules are in Document 4\.  
* audience: conversation designers, product owners and build teams  
* changes in 2.1: added the fail criteria index; added the live agent console rule at 2.3 \[Feedback\]; indexed the card image rule

### How to read this

This document has two parts. **Section 2\. Apple's standard.** What Apple documents and what Apple has told us directly. A failure here sends the experience back. Every rule carries a source tag. **Section 3\. What we have seen in reviews.** Field observations from Messaging Advisory and patterns that recur in real review feedback. These carry no Apple authority. They are what separates an experience that passes from one that works. **On the numbering.** Section 1 of the previous combined document was the process. It now lives in Document 1, the Experience Review Process Overview. Section numbering here is unchanged from v1.0 so that every cross reference already in circulation still resolves. This document therefore starts at Section 2\. That is deliberate.

#### Source tags used in Section 2

| Tag | Source |
| :---- | :---- |
| **\[CDS\]** | Apple, Conversation Design Standards v3.1, 21 July 2026 |
| **\[MWYC\]** | Apple, Message with Your Customer v3.1, 21 July 2026 |
| **\[Journey\]** | Apple, Plan Your Customer's Journey v3.1, 21 July 2026 |
| **\[Ops\]** | Apple, Ops and Marketing Preparation v3.1, 21 July 2026 |
| **\[ER\]** | Apple, Pass the Experience Review v3.1, 21 July 2026 |
| **\[Checklist\]** | MSP Integration Checklist, Apple Feedback Update, 30 July 2026 |
| **\[Feedback\]** | Direct Apple feedback on live integrations |

#### A note on naming

Apple requires the full name **Apple Messages for Business** in customer facing and public materials, and explicitly prohibits the abbreviation "AMB" in public communications \[Ops\]. Where the short form appears in our internal working files it must not survive into anything a client publishes, and it should not appear in file names shared externally. The full naming table is at Section 2.12. Replace \[BRAND\] and the bracketed examples with your own.

### Apple's fail criteria, and where each is answered

Document 1 lists the criteria Apple passes and fails an experience on. This table maps every fail criterion to the rule in this document that prevents it. Three of them are marked \[Feedback\], meaning Apple has told us directly rather than stating them in the v3.1 written criteria.

| Fail criterion | Answered at |
| :---- | :---- |
| Text only experiences that do not leverage platform features | 2.5, and the audit habit at 3.2 |
| Dead ends | 2.4 |
| Missing disclosures | 2.4 automated disclosure, 2.9 opt out, 2.11 privacy policy and terms of use |
| Incorrect product naming | 2.12 |
| Bare URLs | 2.7, and the "tap to load" variant at 3.7 |
| Broken flows | 2.2 conversation shape, 2.4 recovery and escalation |
| Lack of images \[Feedback\] | 2.6 the card image rule, 2.6 row thumbnails, 2.7 every Rich Link carries an image |
| Slow response times | 2.4 the 5 second rule, 2.3 wait time expectations, 3.9 time to first reply |
| Poor human agent console interactions \[Feedback\] | 2.3, the live agent console |
| Missing or broken fallbacks \[Feedback\] | Not a design rule in this document. Apple wants to see that a fallback exists, and it is on the brand to demonstrate it: Document 4, Video 3, and the corresponding test cases in Document 3\. Keep the fallback decision tree written down as well as built, mapping each interactive type in scope to its supported alternative and the OS floor that triggers the swap. Reviewers may ask to see the tree itself, not only its behaviour on device. |
| Policy violations | 2.9 consent, 2.10 prohibited phrasing, 2.11 privacy and personal information |

### Typical Apple feedback, and where each item is answered

These are the themes that come back most often in real Apple feedback. Each one is a rule somewhere in this document. This table is the index into them, so a team responding to a feedback report can go straight to the relevant rule. It is not a separate list of guidance and it introduces nothing new.

| Feedback theme | Answered at |
| :---- | :---- |
| Automated agent disclosure missing or buried | 2.4 |
| Lack of rich elements in the conversation, becoming pure text | 2.5, 2.18, 3.2 |
| No triage menu when intent is unclear | 2.4 |
| Notifications enabled without an active opt in, or no opt out stated | 2.9, 3.3 |
| Flow ends without offering further help | 2.3 |
| Bot goes silent or ignores an input it cannot classify | 2.4 |
| A formal Form used for one or two fields | 3.4 |
| Dead ends anywhere in the flow | 2.4, and a named Apple failure |
| Prompts that do not trigger QuickType | 2.8 |
| Customer asked to repeat information already given | 2.3 |
| Bare URLs, or "tap to load" text links | 2.7, 3.7 |
| Interactive items with no thumbnail or icon | 2.6 |
| The rich card itself carrying no image, only the rows | 2.6, and the field note at 3.2 |
| A live agent exchange that feels slow or awkward on either side | 2.3 |
| Form missing a splash screen, title, intro or review screen | 2.6, 3.4 |
| Form context buried in the subtitle instead of a preceding bubble | 2.6, 3.4 |
| Long text inside a feature bubble, cropped before the customer decides | 2.6, 3.4 |
| List Picker used where a Quick Reply would do | 2.6 |
| Out of hours handling that offers no way to leave a message | 2.3 |
| Escalation that pushes the customer out of the channel | 2.3, 3.5 |
| Handoff to a person not announced, or no wait time given | 2.3 |
| Prohibited closing phrases | 2.10 |
| Satisfaction survey fired after every interaction | 2.10 |
| Messages sent entirely in lowercase | 3.6 |
| Quick Reply summary text repeating the whole previous message | 2.6 |

## Section 2\. Apple's standard

Everything in this section is drawn from Apple documentation or direct Apple feedback. A failure sends the experience back. Each rule carries its source.

### 2.1 The six design principles \[CDS\]

Apple names six. Every design decision should be traceable to one of them.

| Principle | What Apple says |
| :---- | :---- |
| **Privacy First** | Collect only what is necessary, when it is necessary. Protect customer data at every step of the conversation. |
| **Tap Friendly** | Minimise typing. Use Quick Replies, List Pickers and Time Pickers to let customers navigate with a single tap. |
| **Fast by Default** | Respond within seconds. Use automation to eliminate wait times and get customers to answers without delay. |
| **Smart Automation** | Use bots for triage, FAQs and routine tasks. Escalate to live agents seamlessly when human judgment is needed. |
| **Built to Scale** | Design flows that handle high volume efficiently without sacrificing experience quality for any individual customer. |
| **Rich and Engaging** | Leverage Rich Links, images and interactive features to create experiences that feel native, visual and effortless. |

Our own working translation of these six into design decisions is at Section 3.1. It is ours, not Apple's.

### 2.2 The shape of a conversation \[Checklist\]

A well formed conversation has five moments, in order: a prompt greeting that identifies the automation, a guided opening that establishes what the customer wants, the task itself, resolution, and a close the customer controls. Skipping the guided opening produces a bot that waits to be told what to do. Skipping the resolution moment produces a conversation that ends without confirming anything was achieved.

### 2.3 Agent behaviour, live and automated \[CDS\]

**Agent self introduction.** All agents, live or automated, should self identify when responding to a customer's first message. **Close with an offer to help.** After resolving an issue, always ask if there is anything else you can assist with. Going straight from resolution to close is a named failure \[Checklist\]. **Live support availability.** Outside business hours, let customers know when a live agent will respond, or provide alternative channels together with a way to send and receive the responses inside the channel, for example an email composer with send and receive threaded back. **Live agent handoff, wait time.** If a response is not immediate, set expectations with an estimated wait time. Give a queue position where you have one. Never pretend a person is available, and never silently drop a request \[Checklist\]. **Note: A person must always be available in stated business hours** \[Checklist\]. This is the default. Where availability is limited, that has to be agreed with Apple's regional team case by case, and the alternatives below apply only within that agreement. **Live agent handoff, notification.** Always notify the customer when transferring them, and have the live agent introduce themselves. Give the reason for the transfer, and the customer never repeats information \[Checklist\]. **Offer the in conversation message first when no agent is available** \[Checklist\]. When the team is offline or at capacity, the first and default option is to leave a message in the conversation, with a stated response window such as the next business day. The agent then acknowledges that message and replies to it in the same thread when they are back. Callback and email are alternatives offered afterwards, never the first thing on the menu. The customer chose this channel, so keep the answer inside it. **Email is optional where there is no round the clock cover** \[Checklist\]. Provided the message can be composed in channel and ideally returns to the customer as a message rather than as a separate email thread. **Collect key details before live agent escalation.** Gather essential information before routing a customer to a live agent, reducing repetitive questions and helping agents assist faster. **Do not repeat previously provided information.** Agents have access to the full conversation history. Never ask a customer to repeat information already provided. Acknowledge it and move forward. **Respect asynchronous messaging.** The channel is asynchronous. Never push customers to respond immediately, and never use phrases like "This conversation has been closed" or "Finish conversation". Reassure them they can follow up anytime instead. **Typing indicators.** When an agent, live or automated, starts composing a message, a typing indicator should be displayed. Use a one second typing indicator before each message in a sequence. The 30 July checklist widened this: **every outbound payload** gets its own indicator, not only text, including attachments, Quick Reply, List Picker, Time Picker, Form, Rich Links, the Authentication card and Apple Pay \[Checklist\]. The indicator appears only while something is genuinely being composed. One that is always on is worse than none, because it stops meaning anything \[Feedback\]. **The live agent console** \[Feedback\]. When a customer asks to talk to a person, Apple expects that to be a good experience on both sides of the conversation, not only on the device. The customer should feel the brand is responsive. The agent should find it easy to read the thread and to send, including the rich elements the conversation needs. A console that makes an agent slow, or that makes rich content awkward to send, shows up on the customer's screen as long silences and plain text, and that is what gets reviewed. Treat the console as part of the experience under review, not as internal tooling behind it.

### 2.4 Automated agent requirements \[CDS\]

**Disclose and welcome within 5 seconds.** The bot must immediately disclose that it is automated and send an auto welcome within 5 seconds of the first message. Say it plainly: "This is an automated assistant" or "I am an automated agent." When a customer asks whether they are talking to a bot, answer truthfully and immediately. Reviewers test this with a direct question. **Say what the bot is for, not only that it is a bot** \[Feedback\]. Disclosure on its own leaves the customer no wiser about what they can do. Follow it immediately with the assistant's name and its scope: "I am \[BOT NAME\], here to help you with \[WHAT IT COVERS\]". A bot that discloses it is automated and then jumps straight to "what can we help you with?" does not satisfy this. Note: This is also very important for Business invitations. If user tap “Yes” you must welcome the user and explain what he signed for (eg: We will send you notifications about deliveries and important information about your account) **Respond to actionable keywords.** Keywords contain enough information to act without asking for more input. Matching is case insensitive and tolerates surrounding whitespace \[Checklist\].

| Keyword | Action |
| :---- | :---- |
| **AGENT, REPRESENTATIVE** | Escalate to a person, or to the approved alternative |
| **HELP** | Contextual help for the current step |
| **MENU** | Return the triage menu |
| **STOP, UNSUBSCRIBE, QUIT** | Stop sending immediately, across the brand and not only this thread \[Checklist\] |

**Triage menu.** If the customer's intent is not detected from the entry point or initial message, send a triage menu at the start of the interaction with a Quick Reply covering the top reasons customers contact you, up to five \[CDS, Checklist\]. Two constraints: do not force the menu when the customer has already written a clear intent, answer what they asked; and keep the options current from real demand data rather than from an internal org chart \[Checklist\]. **Confirm the context you already have** \[Checklist\]. If the entry point told you the intent, the store or the order, say so rather than asking again. "I can see you are asking about order \[NUMBER\]" is a better opening than a menu. **Keep triage shallow** \[Checklist\]. Never more than two levels deep. A route to a person appears on every menu. **Never dead end** \[ER\]. Dead ends are a named failure criterion. Every path must have a next step. Even where the automation cannot answer, it provides a fallback or a way to escalate. **Recover, never ignore** \[Checklist\]. When the automation cannot classify a turn, it apologises, says plainly that it did not understand, and puts the options back in front of the customer. The reference wording is "Sorry, I didn't quite understand that. Please select an option below", followed by the options as a Quick Reply. Offer two or three options and make at least one a route to a person, connecting to an agent or requesting a call back. Handing back only the menu that already failed is a loop rather than a recovery. One clarification at most. If the next turn is still unclear, escalate. Looping clarifications are a named failure. **Note**: Do not make yourself repetitive on providing the exact the same message every time the agent is unable to understand the intent **End the use case with a follow up offer.** After resolving a use case, offer a Quick Reply so the customer can respond with a single tap instead of typing. **Language detection, confirm before switching.** For multilingual brands, use device locale for the initial language, then confirm with a Quick Reply before switching if a different language is detected. The locale is read from the device, never asked for. A conversation that opens by asking the customer what language they would like has thrown away information it already had \[Feedback\].

### 2.5 The platform feature inventory \[Journey\]

Apple fails "text only experiences that do not leverage platform features" \[ER\]. This is the inventory you are expected to draw from. Use what the task genuinely needs, and be able to say why you did not use the rest. **Quick Reply.** Single tap responses instead of typing, keeping the conversation moving and reducing drop off.

* 2 to 5 options per menu  
* Design your menu with the most common options first  
* Ideal for triage menus, yes and no confirmations, and simple choices **List Picker.** Options in a structured, scrollable sheet, when each choice benefits from an image or icon, a title and a short description.  
* Best for product catalogues, service selection and location picking  
* Can be organised into sections or categories  
* Supports single or multiple selection **Time Picker.** Available time slots directly in the conversation.  
* Shows available slots from your calendar system  
* Automatically detects and surfaces the customer's calendar conflicts  
* Customer can add the selected time to their calendar  
* Ideal for appointments, deliveries and service bookings **Apple Pay.** Payment completed with Face ID or Touch ID without leaving Messages.  
* No card details entered manually, uses cards already saved in Wallet  
* Payment is processed without leaving the conversation **Forms.** Rich, multi page interactive flows delivered in the conversation.  
* Text fields, dropdowns, checkboxes and date pickers  
* Ideal for triage flows, satisfaction surveys, account creation and service sign ups  
* Strong for hospitality: stay details, check in and check out dates in one flow  
* Supports marking responses as private for sensitive data handling. This is the mechanism to use when a form must take something sensitive. **Authentication.** Secure account access inside the conversation.  
* OAuth 2.0 with password autofill  
* Customers authenticate without leaving Messages  
* Enables access to order history, account details and more **Rich Links.** A preview image, title and source URL when a link is shared.  
* Use for product pages, support articles and self serve resources  
* Builds trust with a branded preview before the customer taps **Rich Links, video.**  
* Video plays inline without leaving Messages  
* Ideal for product demonstrations and tutorials **App Extension.** Your app experience is embedded in the conversation, without switching apps.  
* Custom app interface inside the thread  
* Ideal for complex selection flows such as menus, catalogs and orders  
* Drives app adoption naturally from within Messages **Note**: Do not forget Apple Maps or other type of rich elements like App Clips or Apple Music

### 2.6 Presenting interactive features \[CDS\]

**Introductory text goes before the feature, never inside it.** Send a text bubble immediately before the element, as an agent framing message. Use the first line as a clear title and a short subtitle such as "Tap here to start." Long text placed inside a List Picker may get cropped, and the customer decides without having read it. Eg: For Authentication and payments you can say  "Please log into your account" before the Authentication card and then use the payment method if that is not Apple Pay \[Checklist\]. **Business Invitations.** A "Yes" is followed by an agent message explaining what the customer is signing up for. **Pair it with iconography.** A relevant thumbnail across the **receivedMessage**, the **replyMessage** and **each individual item option**, so the items read as tappable. Icon style imagery is acceptable. Where you use symbols, use Apple's SF Symbols set rather than a third party icon font \[Checklist\]. **Use Quick Reply for five options or fewer.** If your List Picker would have five options or fewer, use a Quick Reply instead. It is faster and better suited to simple, text only selections, including binary confirmations. Do not force open text for a bounded question: "shall I add that to your order?" and "does this look right?" are Quick Replies. Typing is not forbidden and the customer may always type, so this is about what the conversation offers rather than what it permits \[CDS, Feedback\]. **Put an image on the card, not only on the rows** \[Feedback, Checklist\]. The rich card that carries an interactive element needs an image of its own. This is the most commonly missed rule in most reviews. The thumbnails on the individual rows are a separate rule and do not satisfy this one. A Form splash screen needs one too. **Apple Pay and the Authentication card are the exceptions** \[Checklist\]. Both render with Apple's own supplied iconography, so they do not take a brand card image and none should be added. The card image rule applies to List Picker, Time Picker, Form, Quick Reply and Rich Links. **Keep the confirmation small** \[Feedback\]. The reply that comes back after a tap, the summary\_text, carries an image too, and it stays within the icon ceiling of about 150 pixels wide. A confirmation that renders as a large card competes with the element the customer has just answered, and the thread reads as two cards rather than as a question and an acknowledgement. **Eg: a Quick Reply summaryText.** The summaryText should be brief and represent the selected option concisely, for example "Option selected" or a short label. Avoid repeating full message content or using overly long text. Never use it as the introduction to the Quick Reply. The prompt belongs in the introductory text. **Give every item secondary text** \[Checklist\]. A List Picker item showing a title alone forces the customer to guess. Populate the subtitle, and where the choice needs it the second and third subtitle lines, so each row can be told apart at a glance. Include a thumbnail on every row. Each field accepts 512 characters in the payload, but the rendered string is capped near 200\. Keep the visible copy short and put any longer explanation in the introductory text. **Put the location on the Time Picker** \[Checklist\]. When an appointment happens somewhere, populate the location of the event. The venue name and map pin render inside the picker, and the location travels with the calendar entry. Show the variants that apply: single select, multiple select and sections, alongside multiple time slots and icons. State the intended time zone in the payload rather than leaving it to be inferred. **Receive a shared location gracefully** \[Checklist\]. A customer can share their location from the compose bar. Acknowledge it in the next message and reflect back what you understood, the resolved address or the place name, so the customer can correct it before anything is dispatched on it. Never let a shared location land in silence. **Build forms so the review page lands at the end** \[Checklist\]. Where a Form runs to several pages, the Review button sits at the end of the final section to be filled, not in the middle of the flow.

### 2.7 Rich Links \[CDS\]

* **Always use a Rich Link for URLs.** Automatically detect all URLs, including videos, and convert them to Rich Link payloads with a live preview. **Never send a bare URL as plain text.** Bare URLs are a named failure criterion \[ER\]. This applies to what a human agent sends as much as to what the automation sends.  
* **Send locations as Apple Maps links.** Whenever sharing a location, send it as an Apple Maps Rich Link (use the construct payload API) rather than a plain address, so customers get an inline map preview.  
* **Rich Link image size.** When using a logo, including for Terms of Use or Privacy Policy links, use a square or rectangular image **under 150 pixels wide**. This results in a cleaner icon style display. Also elements rich cards should use small icons for better display on screen.  
* **Asset specification** \[Checklist\]. The preview image is a PNG optimised at 240 by 240 pixels, up to 200 kB. This is a different rule from the 150 pixel ceiling: 240 by 240 is the asset specification, 150 pixels is the ceiling for icon style treatment.  
* **Every Rich Link carries an image** \[Checklist\]. The image should reflect the page content rather than being a logo placeholder. If the destination has no Open Graph image, one is generated before sending.  
* **Maps and Apple Music go through Construct Payload**, not through a Rich Link.

### 2.8 Data, identity and payment \[CDS\]

**Use built in Authentication.** Apple Messages for Business supports authentication endpoints that let brands verify a customer's identity **before sharing sensitive information such as order details, account data or balances**, ensuring it reaches only the right person. This is a positive obligation, not only a prohibition. If your flow returns an order status or a balance without authenticating, it does not meet this. **Use Apple Pay.** Apple Pay is native to the platform and offers a seamless, secure payment experience. **Never request credit card details through the channel.** **Never request sensitive data as plain text** \[Checklist\]. No full card numbers, no government ID numbers, no full social security numbers, no account passwords typed into the thread. Use Authentication for identity, Apple Pay for payment, and a Form Message with private responses for structured sensitive intake. **Gate the request** \[Checklist\]. Before requesting personal information, ask a clarifying yes or no question such as "Is your inquiry related to your account with us?" Collect only on a yes. **Use QuickType prompts.** Ask for customer information in a way that triggers QuickType suggestions on the device, so iOS suggests the answer and no typing is required. Use these exact phrasings:

* What is your name?  
* What is your last name?  
* What is your email?  
* What is your phone number?  
* What is your address?  
* What is your zip code?  
* What is your location? / Where are you?

### 2.9 Consent and opt out \[Checklist\]

* **Opt in is an active choice.** A tap, not an inference, and never buried in a longer message. State how to opt out at the same moment, and record the brand, the channel, the purpose, the destination, the source, the timestamp and the disclosure version.  
* **Consent is per brand, per channel, per purpose.** Never infer notification consent from a prior conversation, from an accepted invitation, or from consent given on another channel.  
* **Nothing goes out unsolicited** \[Checklist\]. Outbound is permitted only inside an ongoing conversation the customer started, or through an approved Business Invitation template. No SMS style marketing blasts, no cold sends, and nothing to a customer with no open conversation and no accepted invitation. Approved Invitation templates are the only sanctioned business initiated path; everything else on this channel is reactive, and reviewers look for it directly.  
* **Opt out is immediate and brand wide.** Leave Conversation and the trigger words all stop sending at once, across automation, agents, campaigns, retries and anything scheduled. Not just the current thread.  
* **The enrolment message carries the opt out** \[Feedback\]. The instruction belongs in the enrolment and confirmation template itself, not only in the moment of consent. Apple's own shape: a welcome, the brand name, a statement that the assistant is automated, and the opt out, closing on the pattern "Reply STOP anytime to turn off notifications."  
* **A later conversation does not restore campaign consent.** A customer restarting a conversation restores your permission to reply inside that conversation. It does not restore permission to send notifications. Those are separate states and are reset separately.

### 2.10 Resolution, satisfaction and closing \[CDS\]

**Satisfaction surveys.** Present them on the channel, right after the interaction. Use descriptive labels instead of numbers, and a Quick Reply, or a Form Message for longer surveys. When not to ask \[Checklist\]:

* Not after every FAQ answer  
* Not before the task is resolved  
* Not after a close, a Leave Conversation, or an opt out  
* Never on a schedule that fires after the customer has closed the conversation **No SMS specific language.** Phrases like "Messaging rates may apply" or "Data rates may apply" relate to SMS, not to this channel. Prohibited on screen, and equally prohibited in anything spoken about the channel. **Never say these** \[CDS, Checklist\]:  
* "This conversation has been closed"  
* "Finish conversation"  
* "Messaging rates may apply"  
* "Data rates may apply"  
* Anything implying the customer cannot come back Instead, reassure the customer they can follow up at any time.

### 2.11 Policies: privacy, personal information and Terms of Use \[CDS\]

**Personal information, only when necessary.** Businesses must not request personally identifiable information until it is strictly necessary to resolve the customer's issue. Do not collect it speculatively or at the start of every conversation. **Privacy Policy and Terms of Use, Rich Link only.** These must **never** be pasted as inline text in the conversation. Send them as a Rich Link to the brand's webpage. Send them on **two occasions only**: the customer's first engagement, **or when the policy has been updated**. Never at the start of every conversation.

### 2.12 Naming and terminology \[MWYC\]

Correct product naming is a pass criterion and incorrect naming is a named failure \[ER\]. This is a trademark requirement, not a style preference.

| Use | Term | When to use |
| :---- | :---- | :---- |
| **Yes** | **Apple Messages for Business** | Full name. Headlines, first references and formal copy |
| **Yes** | **Apple Messages** | Acceptable short form in customer facing content and button labels |
| **No** | iMessage | Never. This refers to the personal messaging service, not the business channel |
| **No** | Messages for Business | Never. Always include "Apple" at the start |
| **No** | chat, text | Avoid using these terms to describe Apple Messages for Business buttons or flows |
| **No** | Apple logo in place of the word "Apple" | Never use the Apple logo to replace the word "Apple" in text |
| **No** | AMB | Never in public communications \[Ops\] |
| **No** | iMessage for Business, Apple Chat, Messages Business | Never \[Ops\] |

**Where an interface needs an unknown contact label**, use "Apple Messages contact" rather than "Apple Business Contact", and do not call the channel "Apple Business" \[Checklist\]. **Do not use wording that implies Apple endorses \[BRAND\]** \[Checklist\]. The 30 July update widened naming from a conversation copy rule into a rule covering interface, onboarding, marketing and documentation surfaces as well. Scan localisation bundles and templates, not only the flow \[Checklist\]. **Device and platform references** \[Ops\]. Use iPhone, iPad and Mac. Do not reference specific iOS version numbers in marketing materials without checking with Apple business development for accuracy and currency.

### 2.13 Entry points \[MWYC\]

Every place a customer encounters your brand is a chance to start a conversation. The more visible your entry points, the more conversations you will have. Apple lists ten: **Message Suggest, Apple Maps, Website Button, App Button, Email and SMS, QR Code, NFC Tag, Social Media, Wallet Passes, Augmented Reality.** **Enable native entry points easily.** In Apple Business Register, check **"Show Message buttons for iOS and macOS"** to activate Apple Maps, Business Card and Message Suggest in one step. The phone number in your brand profile, or the location profile when there is only one location, is automatically activated in Message Suggest.

#### Message Suggest

The most powerful call deflection tool on the channel, and it only requires registering your phone numbers. When a customer taps any of your registered business phone numbers, on your website, in search results, or on Apple Maps, they see the option to message instead of call. What it does for the business: reduces call volume by offering messaging as a faster alternative, improves customer satisfaction with asynchronous tap friendly support, and lowers support costs by shifting simple requests away from live phone queues. **How to set it up.** Message Suggest is configured by Apple based on information you provide. Send an email to [**business-register@apple.com**](mailto:business-register@apple.com) with the Message Suggest form, including:

* All primary and high call volume phone numbers  
* Your business phone contact hours  
* Title and subtitle for the interface, up to 120 and 170 characters  
* Translations if you need multi language support  
* Intent and body parameters for each number  
* Current call volume and number of agents **Best practices**  
* Register all high volume numbers, not just the main line  
* Make sure registered numbers are tappable on your website, in E.164 format  
* Set up an automated out of hours response  
* Allow **five to seven days** for propagation before checking visibility Because Message Suggest can start a conversation from a phone tap with no other context, the greeting has to work cold \[Checklist\].

#### Composing your entry point URL

Every entry point, whether a website button, QR code or email link, uses an Apple Messages for Business URL. Parameters let you capture intent, route messages and pre fill context.

```
https://bcrw.apple.com/urn:biz:<your-business-id>?biz-intent-id=order_support&biz-group-id=post_sales&body=Tap%20Send%20to%20start
```

| Parameter | Name | What it does | Example |
| :---- | :---- | :---- | :---- |
| biz-intent-id | Intent ID | Identifies the purpose of the conversation, which entry point or use case triggered it. Lets you track performance by entry point and route appropriately. | order\_support, appointment\_booking, flight\_disruption |
| biz-group-id | Group ID | Routes the conversation to the right team or department within your provider platform. Reduces triage steps when the destination is already known. | post\_sales, reservations, billing\_team |
| body | Pre filled message | Pre populates the customer's message field. All they need to do is tap Send. Reduces friction and increases conversion from entry point to conversation. | Tap%20Send%20to%20start |

**Use a different Intent ID for each entry point.** This lets you measure which entry points drive the most conversations and understand where your customers are coming from. **Important.** Parameters must not contain URI reserved characters: & \# \[ \] ( ) { } /

#### Entry point standards

* **Use a clear call to action.** Tell customers what to expect before they tap. "Style questions? We can help." or "Book an appointment via Apple Messages" performs better than a logo alone.  
* **Keep entry points always on.** Do not disable buttons outside business hours. Customers should always be able to start a conversation. Automation handles the response when agents are not available.  
* **Show buttons on supported devices only.** On websites, the Messages button hides automatically on unsupported devices. If you place buttons manually, use your content management system to detect Apple devices and show accordingly.  
* **Pre fill the message body.** Adding a body parameter means customers only need to tap Send. A small change that meaningfully reduces friction at the start of the conversation.  
* **Add an Intent ID to every entry point.** Even if you do not use routing immediately, Intent IDs let you understand where conversations come from and which entry points are most effective.  
* **Place buttons where customers need help.** The most effective positions are contact pages, support pages, order confirmation pages and product pages, where customers are most likely to have a question.

### 2.14 Buttons and calls to action \[MWYC\]

Apple provides four approved call to action options plus an icon. Use one of them so customers understand what to expect before they tap. **Do not enable buttons until your account is approved to go live.** Button assets provided by Apple must be used as supplied, without modification \[Ops\].

| Button type | Best for |
| :---- | :---- |
| **Message Us** | General support pages and contact pages |
| **Contact an Agent** | When customers expect to reach a live person |
| **Ask a Question** | Product pages and pre purchase support |
| **Get Help** | Troubleshooting flows, order issues and support hubs |
| **Messages for Business icon** | Messages app icon only. Standalone icon in space constrained contexts such as widgets, or inline alongside other icons |

### 2.15 Operational readiness \[Ops\]

Before enabling your account, confirm your team and systems are ready. **Staffing and coverage.** Enough agents available to cover your advertised support hours. Define a clear escalation path for issues an automated agent cannot resolve. **Response time expectations.** Set realistic and honest expectations **in your welcome message**. If live agent wait times vary, communicate this dynamically using automated messages. **Out of hours handling.** Configure an automated out of hours response that informs customers when live agents are available. Do not leave customers without a response when they message outside business hours. **Testing before launch.** Thoroughly test all entry points, automated flows, handoff to live agents and edge cases before going live. Use sandbox environments and real device testing on supported Apple devices. **Analytics and monitoring.** Establish baseline metrics, response times, resolution rates and satisfaction scores, **before launch**. Set up dashboards to monitor performance and identify issues early. Capturing these after launch leaves you nothing to compare against. **Agent training.** Train all live agents on the experience, including tone of voice, feature usage and escalation procedures. Agents should be familiar with asynchronous messaging expectations.

### 2.16 Marketing guidelines \[Ops\]

You may promote your Apple Messages for Business capability, but all activity must follow Apple's naming, branding and messaging guidelines. **Naming and terminology.** Use the correct product name. See Section 2.12. Do not abbreviate "AMB" in public communications. **Apple branding.** Do not use Apple logos, product images or trademarks in your marketing materials without prior written approval. Button assets provided by Apple must be used as supplied, without modification. **Feature availability.** Marketing should only be executed when the feature is fully available to customers. Do not promote the capability before your account is live and approved. **Customer focused messaging.** Focus on the value to the customer and the experience they can expect. Avoid technical jargon. Highlight convenience, speed and ease of use. **Approved description.** Apple Messages for Business allows customers to connect with companies directly from the Messages app on iPhone, iPad and Mac. Customers can get support, make purchases and resolve issues, all in a familiar, trusted messaging experience. **What to avoid.** "iMessage for Business", "Apple Chat", "AMB" in public materials. Claims about Apple's technology, roadmap or strategy. Apple metrics without prior approval.

### 2.17 The partner press announcement process \[Ops\]

**Important.** All public relations plans and press materials must be shared with Apple business development before any outreach. Do not contact media or publish materials before receiving Apple alignment. This runs on its own clock. If you intend to announce, start it before the experience review completes.

| When | What happens |
| :---- | :---- |
| **6+ weeks before announce** | Submit your completed plan template to your Apple business development contact. They share it with Apple public relations and the Apple product lead for review and feedback. |
| **4 to 5 weeks before** | Apple public relations and the product lead provide feedback. Business development communicates it back. Apple may share a press release template. |
| **2 to 3 weeks before** | Once Apple has aligned on your approach, share draft press materials with Apple business development. They review first, then the product lead, then public relations. |
| **Final stage** | Apple public relations routes final materials to Apple leadership for approval. Nothing is published or distributed before this step completes. |

#### Guidelines for press activity

* **Time announcements to feature availability.** Messaging focuses on the value to customers and the customer experience, not on internal milestones or partnerships.  
* **Share your plans at least six weeks in advance**, including your media list, before contacting any press outlet.  
* **Share all press materials with Apple before distribution.** Blog posts, press images, videos and detailed pitches included. Press releases are approved case by case only. Joint releases with Apple are preferred over multiple separate releases.  
* **Allow sufficient review time.** At least two to three weeks for press release reviews, at least two weeks for blog posts and pitches.  
* **Align on any metrics or numbers before sharing publicly.** Customer satisfaction scores, volume figures and any other quantitative claim.  
* **Spokespersons speak only on behalf of their own company.** Do not speak for Apple, make claims about Apple's roadmap or strategy, or represent Apple's position.  
* **Forward Apple press inquiries appropriately.** Do not respond to press inquiries directed at Apple. Forward them to your Apple business development contact. Apple will forward to you any inquiries pertaining to your company.

#### Plan template sections

| Section | What to include |
| :---- | :---- |
| **Objectives** | Goals of the activity, what you are trying to achieve, target audience, what success looks like |
| **Approach and tactics** | What you plan to do (blog post, media pitch, press release), where materials will be published, links to drafts |
| **Press list** | Outlets and reporter names, and when you plan to contact them. Shared at least six weeks before outreach begins |
| **Timeline** | When you will execute, key dates, internal deadlines, embargo dates or dependencies |
| **Next steps** | Open items, dependencies, actions required from Apple, questions for Apple business development or public relations |

Send it to your Apple business development contact, who facilitates all communication with Apple public relations. **Do not contact Apple public relations directly.**

### 2.18 During \- Design self check

This is the writer's quick pass, run at the desk while the flow is still being designed. It is not the test record. The formal, evidenced test record is **Document 3, the Experience Review Checklist and Test Cases**, which is what MA validates against at Step 3 and what accompanies the submission at Step 5\. Every line here has a corresponding test case in Document 3\. **Conversation**

- [ ] Automated greeting arrives within 5 seconds and discloses that it is automated  
- [ ] The opener names the assistant and says what it covers  
- [ ] A one second typing indicator precedes every outbound payload, including back to back sends, and from live agents as well as the bot  
- [ ] No typing indicator appears while nothing is being composed  
- [ ] The opening pairs the greeting with a Quick Reply of up to five real top intents  
- [ ] The Quick Reply menu leads with the most common options  
- [ ] A clear written intent is answered rather than overridden by the menu  
- [ ] A route to a person appears on every menu, and AGENT, HELP and MENU trigger the right behaviour  
- [ ] Triage is never more than two levels deep  
- [ ] No path in the conversation dead ends  
- [ ] Unrecognised input gets a recovery message that re offers the options as a Quick Reply, then escalates  
- [ ] Device locale drives language, and any switch is confirmed first  
- [ ] The conversation never opens by asking the customer which language they want  
- [ ] The conversation offers further help before the close, as a Quick Reply  
- [ ] No information already given is asked for a second time **Features**  
- [ ] The experience uses platform features and is not a text only flow  
- [ ] Introductory text precedes every rich element, including Authentication and Apple Pay  
- [ ] Every card that carries an interactive element has its own image, and the Form splash screen has one  
- [ ] Every interactive item carries a thumbnail on receivedMessage, replyMessage and each item option  
- [ ] Bounded questions are answered by a Quick Reply rather than by typed text  
- [ ] Any List Picker with five options or fewer has been converted to a Quick Reply  
- [ ] At least one List Picker shows subtitles and secondary text, not titles alone  
- [ ] Time Picker events that happen somewhere carry a location, and the time zone is explicit  
- [ ] A location shared by the customer is acknowledged and reflected back before anything acts on it  
- [ ] No brand card image has been forced onto Apple Pay or the Authentication card  
- [ ] Every summaryText reads as a short label, not a sentence  
- [ ] The confirmation image after a tap stays within the icon ceiling of about 150 pixels  
- [ ] The Form review page sits at the end of the final section to be filled  
- [ ] Sensitive form responses are marked private **Rich Links**  
- [ ] Every URL renders as a Rich Link with an image, detected automatically, including video  
- [ ] No bare URL and no "tap to load" text link appears anywhere  
- [ ] Every location renders as a Maps Rich Link  
- [ ] Logo style link images are under 150 pixels wide **Data and policy**  
- [ ] Authentication is used before any order detail, account data or balance is shared  
- [ ] Apple Pay is used for payment and no card details are requested in the thread  
- [ ] No personal information is requested without the clarifying yes or no gate first  
- [ ] No password or card number is ever requested as plain text  
- [ ] Data collection questions use the QuickType phrasings  
- [ ] Privacy Policy and Terms of Use are Rich Links, sent only on first engagement or after a policy update  
- [ ] Opt in is an active choice and states how to opt out  
- [ ] The enrolment and confirmation template carries its own opt out instruction  
- [ ] Opt out keywords stop sending immediately, brand wide  
- [ ] Nothing is sent outside an ongoing customer started conversation or an approved Business Invitation **Live agent**  
- [ ] Business hours logic is configured, and an off hours message states when a live agent will respond  
- [ ] Response time expectations are set in the welcome message  
- [ ] When no agent is available, leaving a message in the conversation is the first option offered  
- [ ] The response window is stated, and an agent replies to that message in the same thread  
- [ ] The handover to a live agent is announced, and the agent introduces themselves on joining  
- [ ] An estimated wait time is given whenever the response is not immediate  
- [ ] Key details are collected before escalation  
- [ ] An agent introduction script is defined and agents are trained **Naming, entry points and readiness**  
- [ ] Naming follows Section 2.12 across the flow, templates, interface labels and localisation bundles  
- [ ] "chat", "text", "iMessage" and "AMB" appear nowhere customer facing  
- [ ] Every entry point carries an Intent ID, and a Group ID where routing applies  
- [ ] Entry point URLs contain no reserved characters  
- [ ] The message body is pre filled where it helps  
- [ ] Buttons use one of Apple's four approved calls to action and are not modified  
- [ ] Buttons are not enabled until the account is approved to go live  
- [ ] Entry points stay on outside business hours  
- [ ] Registered phone numbers are tappable in E.164 format  
- [ ] Staffing covers advertised hours and an escalation path is defined  
- [ ] Baseline metrics are captured before launch  
- [ ] The satisfaction survey uses descriptive labels, fires only after real resolution, and never after a close  
- [ ] None of the prohibited phrases appear anywhere  
- [ ] Every flow tested from the customer side on a real device

## Section 3\. What we have seen in reviews

Nothing here carries Apple authority. **(Field)** is a Messaging Advisory observation. **(Review)** is a pattern drawn from real Apple feedback on live integrations. Three items previously in this section have moved to Section 2, because Apple v3.1 states them directly: dead ends, entry point placement, and the live agent handoff notification and wait time.

### 3.1 Our working translation of Apple's six principles (Field)

Apple's six are at Section 2.1. These are the seven statements we use in workshops, because they translate the principles into decisions a writer can act on. They are ours.

* **Be prompt.** The first automated reply arrives inside 5 seconds. Nothing in this channel justifies a customer waiting for an acknowledgement.  
* **Be honest.** Automation says it is automation. A person is presented as a person. Neither pretends to be the other.  
* **Be clear.** One question at a time, in the customer's words, not in the brand's internal vocabulary.  
* **Be useful.** Every turn moves the task forward or hands it to someone who can.  
* **Be respectful of the customer's control.** They decide when the conversation ends, whether they opt in, and what they share.  
* **Be tappable.** Provide as many tappable options as possible rather than long text that requires a lot of typing. In a large proportion of cases the customer is on a mobile device and on the move.  
* **Be asynchronous.** The customer can walk away and come back. Nothing in the copy pressures an immediate reply, and nothing implies the conversation has been terminated. **Design the close before you design the middle. (Field)** Teams that start from the close write shorter flows.

### 3.2 Build and quality assurance habits

**Treat the card image and the row thumbnails as two different checks. (Field)** Teams that treat them as one thing ship the rows and forget the card, which is the pattern that fails most often. Two lines on your quality assurance list, not one. **Read every summaryText out loud before launch. (Field)** The detail we see failed most often after the card image. If it sounds like a sentence, it is too long. A short label is right. Repeating the question back is not. **Count your bounded questions. (Field)** Read the flow and count the questions ending in a question mark with only two sensible answers. Each one is a Quick Reply you have not built yet. **Audit against the feature inventory, not against your flow. (Field)** Because "text only experiences that do not leverage platform features" is a named Apple failure, walk Section 2.5 top to bottom and write down why each feature is or is not used. An AI generated experience that answers everything correctly in prose still fails.

### 3.3 Openers and triage

**An honest short menu beats a vague AI opener. (Field)** Where an AI layer handles triage rather than a fixed menu, the AI must demonstrably do better than the menu would. If the automation can only really do three things, say so: "I can help with \[A\], \[B\] or \[C\] right now, or I can put you through to someone." **Name the scope in the customer's words, not the department's. (Field)** "Here to help with orders, delivery and returns" lands better than "here to help with order lifecycle management". **Say how to opt out in plain conversational words too. (Review)** Alongside the STOP pattern in the enrolment template, conversations should explicitly tell the customer how to stop, for example "Reply 'unsubscribe' at any time to opt out." **For a single language deployment, say so internally and revisit when a second market opens. (Field)** The locale rule matters the moment it applies, and retrofitting it is more work than designing for it.

### 3.4 Rich elements and forms

**Do not build a Form for one or two fields. (Review)** For an intake with only one or two fields, such as a name and an email, a formal Form object is discouraged. A plain text conversational exchange is preferred: "What's your full name?" then "What's your work email address?" The Form is for structured intake of several fields. **Give the form a splash, a title, an introductory description and a review screen. (Review)** The splash screen is treated as a best practice rather than an optional extra, so the customer knows what they are filling out before they start. **Put the form's "why" in a message bubble before the form. (Review)** Not in the form's subtitle, where it gets cropped and missed. **Long text goes outside the feature bubble. (Review)** The first line of a feature bubble should be the title. Long text gets cropped and becomes unreadable before the customer decides. **Model multi select and multi section properly. (Field)** If the use case genuinely has them, build them rather than flattening everything into single select.

### 3.5 Escalation and human handover

**Keep an email escalation inside the channel. (Review)** If an email is being drafted to support, the automation should help the customer compose it within the conversation rather than abruptly shifting them away from it. Apple expects the conversation keeps in the channel. **Update long waits every five minutes. (Field)** If the wait exceeds what you promised, keep talking rather than going quiet.

### 3.6 Copy and tone

**Use proper casing. (Review)** Messages sent entirely in lowercase are often flagged as a poor customer experience, regardless of how informal the brand voice is elsewhere. **Short bubbles. (Field)** Two or three lines. Long paragraphs read as email, not as messaging. **Match the customer's register. (Field)** If they write in fragments, do not reply in full corporate prose. This does not override the casing point above.

### 3.7 Rich Links

**A black preview fails. (Field)** A video Rich Link with no background image is one of the fastest ways to draw a review finding. **"Tap to load" text links are not acceptable either. (Review)** The rule is not only about bare URLs. Any text style link, including a "tap to load" prompt, fails. And the image inside a Rich Link must accurately reflect the content of the target page.

### 3.8 Shared location handling

**Show it to your agent as a map, not a coordinate pair. (Field)** An agent reading numbers will mistype them. **Treat it as personal data. (Field)** Keep it for as long as the request needs it and no longer, do not copy it into systems that were not disclosed, and do not ask for it where a postcode or a store picker would answer the same question.

### 3.9 Metrics to watch after launch

Baseline these before launch, per Section 2.15. These are the readings we watch afterwards.

| Metric | What good looks like |
| :---- | :---- |
| **Time to first reply** | Under 5 seconds, every time, not on average |
| **Containment without frustration** | Rising, while escalation requests stay flat |
| **Recovery rate** | Most unclassified turns resolved in one clarification |
| **Escalation to resolution time** | Inside the window you promised in the thread |
| **Opt out rate after a notification** | Flat. A spike means the notification was not what the customer consented to |
| **Survey response rate** | Falling response usually means you are asking too often, not that customers are unhappy |
| **Conversations by Intent ID** | Rising on the entry points you invested in. Flat on one you promoted means the button placement is wrong, not the channel |

### Provenance

* Apple, Conversation Design Standards v3.1, 21 July 2026  
* Apple, Message with Your Customer v3.1, 21 July 2026  
* Apple, Plan Your Customer's Journey v3.1, 21 July 2026  
* Apple, Ops and Marketing Preparation v3.1, 21 July 2026  
* Apple, Pass the Experience Review v3.1, 21 July 2026  
* MSP Integration Checklist, Apple Feedback Update, 30 July 2026: items C.6, C.7, C.8, C.12, C.14, E.4, E.5, E.6, E.7, E.8, E.9, E.10, E.11, E.12, F.2, F.5, and the Section C note on introductory text before rich elements  
* Direct Apple feedback on live integrations  
* Messaging Advisory, Experience Review Process Overview v1.x: the feedback examples, distributed through Sections 2 and 3 and indexed at the front of this document  
* Messaging Advisory field observations, marked (Field) in Section 3 Section 2 is drawn from Apple documentation or direct Apple feedback and every rule carries its source. Section 3 carries no Apple authority.

\========

# Part 3\. Experience Review Checklist and Test Cases, version 2.0

## Document 3\. Experience Review Checklist and Test Cases

*Version 2.0. The live template is a spreadsheet with five tabs: Checklist, Summary, Legend, Appendix A Scope, Appendix B Readiness. The 114 test cases are reproduced here so AI tooling can read them. Status, Evidence, Actual result and Comments are filled in the spreadsheet, not here.*

**Severity.** Non negotiable blocks submission. Apple standard is a documented Apple requirement. Field is a Messaging Advisory observation and carries no Apple authority.

**Applies when.** Where the condition is not met for a build, the row is marked N/A in the spreadsheet. Scope comes from Appendix A, which mirrors Apple's Use Cases form.

**Rule ref** points at the section of Document 2 that the row tests. Doc 1 and Doc 4 references point at the Process Overview and the Recording Guide.

### 0\. Final Gate (checked on every Apple review, see the Legend for Apple's five)

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 0.1 | Reachable escalation | Confirm a live agent connection is reachable within stated hours, OR the exempted callback or in conversation message path is offered and works end to end (see Section 9). | Escalation path is reachable and functional. | 2.3 | Always | Non negotiable |
| 0.2 | Leave Conversation respected | End the conversation via Leave Conversation, then attempt to send from both the bot and a live agent. | Both bot and human agent are blocked from sending; the business cannot re-engage until the user restarts. | 2.9 | Always | Non negotiable |
| 0.3 | No forbidden or restricted platform wording | Review every piece of bot copy, template text, interface label, localisation bundle, onboarding copy and spoken narration in the recording. | No use of "iMessage", "AMB", "Apple Chat", "chat" or "text" as a channel name, and no wording implying Apple endorses the brand. Correct product naming throughout. | 2.12 | Always | Non negotiable |
| 0.4 | Opt-out works end to end | Trigger STOP / UNSUBSCRIBE / QUIT from an active, opted-in conversation. | Both bot and live agent stop sending immediately; opt-out applies brand-wide, not just the current thread; re-engagement requires a fresh opt-in. | 2.9 | Always | Non negotiable |

### 1\. Pre-Test and Review Readiness

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1.1 | Apple Messages for Business account connected and delivering | Confirm the account is connected and send a test message. | Message delivery is confirmed end to end. | Doc 1 s4 | Always | Apple standard |
| 1.2 | Commercial account access restricted | Check Account Testing then Advanced settings. | Access is restricted to authorized Apple IDs used for testing. | Doc 1 s4 | Always | Apple standard |
| 1.3 | All registered use cases are testable | Cross-check the approved use case list on Appendix A against scenarios available in the test build. | Every submitted use case has a corresponding, working flow in the test environment. | Doc 1 s4 | Always | Apple standard |
| 1.4 | All entry points are functional | Test each entry point marked in scope on Appendix A (URL button, Message Suggest, Apple Maps, Wallet, QR or App Store link, Business Invitation, IVR deflection, social). | Each entry point opens a Messages conversation with the correct business account and correct routing context. | 2.13 | Always | Apple standard |
| 1.5 | Agents trained, and an introduction script is defined | Confirm with the client that live agent staff have been briefed, and review the written agent introduction script. | Agents are prepared and trained for the channel and the relevant use cases, and a consistent introduction script exists. | 2.3 | Live agent in scope | Apple standard |
| 1.6 | Tested on macOS as well as iPhone | Run the primary use case from the Messages app on a Mac signed in to the same Apple ID. | The experience works on macOS. iPhone is the priority platform, but macOS is also tested before submission. | Doc 1 s4 | Always | Apple standard |
| 1.7 | Baseline metrics planned before launch | Confirm with the client which metrics are captured and from when. | Response times, resolution rates and satisfaction baselines are planned before launch, not after. | 2.15 | Always | Apple standard |

### 2\. Entry Points and Passable Context

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2.1 | Entry point routing lands in the correct flow | Open the conversation from each of the brand's registered entry points (for example two different QR codes for two different stores or intents). | Each entry point routes to the correct, distinct flow, not the same generic flow regardless of source. | 2.13 | Always | Apple standard |
| 2.2 | Bot confirms context received from entry point | Open a conversation from an entry point carrying routing context (store, product or campaign reference). | The opening message reflects the context received, for example "I see you're asking about \[Store or Product X\]", rather than a generic greeting. | 2.4 | Any entry point carrying context | Apple standard |
| 2.3 | Business Invitation opt-in gate and decline handling | Attempt to send a Business Invitation to a number that has not opted in; then send a valid test invite and respond "No" or decline. | Platform requires opt-in coverage before sending; a decline is correctly registered and that user is not messaged again. | 2.9 | Business Invitations in scope | Apple standard |
| 2.4 | Invitation opt-out present in every Business Update | Review every Business Invitation and Business Update message the brand sends. | Opt-out instructions appear in every single Business Update message, not just the first. | 2.9 | Business Invitations in scope | Apple standard |
| 2.5 | A "Yes" on a Business Invitation is followed by a welcome that explains what was accepted | Accept a Business Invitation and read the next message. | An agent message welcomes the customer and states plainly what they signed up for, for example what notifications will be sent and how often. | 2.6 | Business Invitations in scope | Apple standard |

### 3\. Agent Identification, Honesty and Triage

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 3.1 | First response within 5 seconds, with typing indicator | Send the first message of a new conversation and time the automated reply. | A typing indicator appears first, then the automated response arrives within 5 seconds total. | 2.4 | Always | Non negotiable |
| 3.2 | Bot self-identifies as automated on entry | Review the opening automated message. | Message clearly and plainly states it is an automated agent, not implied or buried. | 2.4 | Always | Non negotiable |
| 3.3 | The opener states the assistant's name and what it covers | Read the opening message after the disclosure. | The opener names the assistant and states its scope, for example "I'm \[NAME\], here to help with orders, delivery and returns". Disclosure followed only by "what can we help you with?" does not satisfy this. | 2.4 | Always | Apple standard |
| 3.4 | Bot answers truthfully when asked if it is a bot | At multiple points in the conversation ask directly: "are you a bot?", "am I talking to a real person?", "are you AI?" | Bot always answers truthfully that it is automated. It never claims to be human or dodges the question. | 2.4 | Always | Non negotiable |
| 3.5 | Typing indicator before every outbound message, including rich features | Step through a multi-message bot flow, including back-to-back sequences with no user input between them (enrollment confirmations, status updates, summaries, quick replies, forms). | A typing indicator appears before every single outbound payload, not just the first, including one-off notifications, attachments, rich and interactive bubbles, the Authentication card and Apple Pay. | 2.3 | Always | Non negotiable |
| 3.6 | Typing indicator never hangs or misleads | Have a live agent leave a typing indicator active for an extended period without sending. | Indicator resolves or refreshes sensibly rather than hanging indefinitely and implying an imminent reply that never comes. | 2.3 | Always | Apple standard |
| 3.7 | Live agent messages also carry a typing indicator | During a live agent exchange, watch the customer device while the agent composes. | The typing indicator appears on the customer side for agent messages as well as bot messages. | 2.3 | Live agent in scope | Apple standard |
| 3.8 | Triage menu appears when intent is unclear | Send an ambiguous opening message such as "hi". | Bot offers a Quick Reply triage menu of up to five options instead of guessing or forcing free text. | 2.4 | Always | Apple standard |
| 3.9 | Triage menu leads with the most common options | Compare the order of the menu options against real demand data. | The most common reasons customers make contact appear first, and the list reflects real demand rather than an internal org chart. | 2.5 | Always | Apple standard |
| 3.10 | A clearly written intent is answered rather than overridden by the menu | Open the conversation with a specific, unambiguous request. | The bot answers what was asked. It does not discard the stated intent and present the triage menu instead. | 2.4 | Always | Apple standard |
| 3.11 | A route to a person appears on every menu | Review every triage menu and sub-menu in the experience. | Each menu includes an option to reach a person, or the agreed alternative path. | 2.4 | Always | Apple standard |
| 3.12 | Triage is never more than two levels deep | Walk the deepest menu path in the design. | No path requires more than two menu selections before reaching a task or a person. | 2.4 | Always | Apple standard |
| 3.13 | Actionable keywords trigger the defined behaviour | Send AGENT, REPRESENTATIVE, HELP and MENU, in mixed case and with surrounding whitespace. | Each keyword triggers its defined behaviour. Matching is case insensitive and tolerates whitespace. AGENT and REPRESENTATIVE escalate, HELP gives contextual help, MENU returns the triage menu. | 2.4 | Always | Apple standard |
| 3.14 | Recovery re-offers options and escalates after one clarification | Send an input the bot cannot classify, then send a second unclassifiable input. | The bot apologises, says plainly it did not understand, and re-offers two or three options as a Quick Reply with at least one route to a person. On the second failure it escalates rather than looping. | 2.4 | Always | Apple standard |
| 3.15 | Recovery wording varies rather than repeating identically | Send three consecutive inputs the bot cannot classify. | The recovery message is not the exact same sentence every time. Repetition of an identical failure message reads as a broken loop. | 2.4 | Always | Apple standard |
| 3.16 | Device locale drives language, and any switch is confirmed first | Set the device to a supported non-default locale and open a conversation. Then write in a different supported language. | The conversation opens in the device locale. A detected language change is confirmed with a Quick Reply before switching. | 2.4 | Multilingual in scope | Apple standard |
| 3.17 | The conversation never opens by asking which language the customer wants | Read the opening message. | Language is read from the device, never asked for. | 2.4 | Multilingual in scope | Field |
| 3.18 | Off-hours automated message is accurate and non-deceptive | Message the account, or request a live agent, outside of stated business hours. | Automated message explains the business is closed and states expected response time or business hours, without pretending a person is available. | 2.3 | Always | Apple standard |
| 3.19 | Off-hours notice is triggered at the right moment | Attempt to reach a live agent outside business hours, as distinct from simply messaging the bot outside hours. | The out-of-hours notice fires specifically when the user tries to connect to a live agent outside messaging hours, not generically at the start of any off-hours conversation. | 2.3 | Always | Apple standard |
| 3.20 | Welcome message tone matches brand | Review the welcome and greeting copy against brand voice guidelines. | Tone is warm, on-brand, and not robotic or legalistic. | 3.6 | Always | Field |

### 4\. Core Messaging, Rich Links and Close

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 4.1 | Rich Links used for all URLs | Review every message containing a URL, from the bot and from live agents. | All URLs are sent as Rich Links. Plain-text and "tap-to-load" text links are not used anywhere. | 2.7 | Always | Non negotiable |
| 4.2 | Rich Link logo image is properly sized | Inspect the image used for any Rich Link built from a logo. | Image is square or a rectangle with width under 150px, so it renders as a clean icon rather than a cropped or blurry preview. | 2.7 | Always | Apple standard |
| 4.3 | Rich Link preview asset meets Apple's specification | Inspect the preview asset file for a content Rich Link. | PNG, optimised at 240 by 240 pixels, up to 200 kB. This is separate from the 150 pixel icon ceiling. | 2.7 | Always | Apple standard |
| 4.4 | Every Rich Link image reflects the destination page | Open each Rich Link and compare the preview image to the page it opens. | The image reflects the page content rather than being a generic logo placeholder. Where the destination has no Open Graph image, one is generated before sending. | 2.7 | Always | Apple standard |
| 4.5 | Video Rich Links have a background image | Send every video Rich Link in the experience and view it on device. | The preview renders with a background image. A black preview is a fast route to a review finding. | 3.7 | Video Rich Links in scope | Field |
| 4.6 | Maps and Apple Music are sent through Construct Payload | Trigger any flow that shares a location or a music link. | Maps and Apple Music are sent as Construct Payload, not as a Rich Link. | 2.7 | Maps or Music in scope | Apple standard |
| 4.7 | Rich Link is followed by a message or call to action | Send a Rich Link and observe what follows. | A follow-up message with a clear call to action follows the Rich Link. It is not left to sit on its own. | 2.6 | Always | Apple standard |
| 4.8 | Unclassified input never lands in silence | Send one unclear or unsupported input and observe the immediate response. | The bot never stays silent. It responds with a clear, polite recovery message and a way forward. (Branch-level dead ends are tested separately at 10.7.) | 2.4 | Always | Non negotiable |
| 4.9 | "Anything else?" close prompt | Complete a use case end to end and observe the closing message. | Bot asks if the user needs further assistance, optionally with a follow-up Quick Reply, rather than abruptly ending the flow. | 2.3 | Always | Apple standard |
| 4.10 | No prohibited closing phrases | Review all conversation-ending copy. | Phrases like "This conversation has been closed", "Finish conversation", "Messaging rates may apply" and "Data rates may apply" are not used. Closing language leaves the door open for future contact. | 2.10 | Always | Apple standard |
| 4.11 | No repeated requests for information already given | Provide information such as name or email earlier in the flow, then continue to a step that would normally ask for it again. | The bot does not ask the user to repeat information already captured earlier in the conversation. | 2.3 | Always | Apple standard |
| 4.12 | Proper casing throughout | Review all message copy. | All messages use proper casing. Messages sent entirely in lowercase are flagged as poor customer experience regardless of brand voice. | 3.6 | Always | Field |
| 4.13 | Quick Reply summaryText is a short label | Review the summary text each Quick Reply echoes back into the transcript. | summaryText is short and label-based, for example "Option selected". It does not repeat the full previous message and is never used as the introduction to the Quick Reply. | 2.6 | Quick Reply in scope | Apple standard |

### 5\. Interactive Features

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 5.1 | Every interactive option carries a thumbnail or icon | Review every receivedMessage, replyMessage, and each individual option in a List Picker. | Each includes a thumbnail image or icon making it clearly recognizable as a tappable UI element. SF Symbols where symbols are used. | 2.6 | Any interactive feature in scope | Apple standard |
| 5.2 | The rich card itself carries its own image | Inspect the card that carries each interactive element, separately from the row thumbnails. | The card has an image of its own. Row thumbnails do not satisfy this. A Form splash screen needs one too. This is the single most commonly missed rule. | 2.6 | Any interactive feature in scope | Non negotiable |
| 5.3 | No brand card image forced onto Apple Pay or Authentication | Inspect the Apple Pay sheet and the Authentication card. | Neither carries a brand card image. Both render with Apple's own supplied iconography. | 2.6 | Apple Pay or Authentication in scope | Apple standard |
| 5.4 | List Picker versus Quick Reply used appropriately | Review each menu presented to the user. | List Pickers are used only where there is genuine category variation. Five or fewer flat options use a Quick Reply instead. Bounded questions are answered by a Quick Reply rather than typed text. | 2.6 | List Picker in scope | Apple standard |
| 5.5 | List Picker items carry subtitles and secondary text | Review the rows of every List Picker. | Rows show a subtitle, and second or third subtitle lines where the choice needs them, so each row can be told apart at a glance. Titles alone force the customer to guess. Visible copy stays short; the rendered string caps near 200 characters. | 2.6 | List Picker in scope | Apple standard |
| 5.6 | Forms include splash screen, title, intro and review screen | Step through every Form Message in the experience. | Each form has a splash screen, a title, an introductory description, and a final review screen before submission. | 2.6 | Form in scope | Apple standard |
| 5.7 | The Form review page sits at the end of the final section | Step through a multi-page Form to the end. | The Review button sits at the end of the final section to be filled, not in the middle of the flow. | 2.6 | Multi-page Form in scope | Apple standard |
| 5.8 | Form context set in a conversational bubble first | Review the message immediately preceding each form. | The "why" for the form is stated in a conversational bubble before the form opens, not buried in the form's subtitle where it can be cropped. | 2.6 | Form in scope | Apple standard |
| 5.9 | Simple one or two field forms use plain text conversational flow | Identify any form collecting only one or two fields, such as name and email. | A plain-text conversational exchange is used instead of a formal Form object. | 3.4 | Form in scope | Field |
| 5.10 | Sensitive Form responses are marked private | Inspect the payload for any form field taking sensitive data. | Responses that carry sensitive data are marked private. | 2.5 | Form taking sensitive data | Apple standard |
| 5.11 | Introductory text precedes every rich element | Observe the message immediately before every Time Picker, List Picker, Form, Quick Reply, Rich Link, Authentication card and Apple Pay request. | A brief conversational message sets expectations before the interactive bubble appears. This includes Authentication and Apple Pay, for example "Please log into your account" before the Authentication card. | 2.6 | Any interactive feature in scope | Non negotiable |
| 5.12 | Time Picker confirmation includes a save-to-calendar tip | Complete a booking flow through a Time Picker. | The confirmation message tells the user they can tap their selected time to save it to their Apple Calendar. | 2.6 | Time Picker in scope | Apple standard |
| 5.13 | Time Picker carries a location and an explicit time zone | Inspect the Time Picker payload for an appointment that happens somewhere. | The location is populated so the venue name and map pin render inside the picker and travel with the calendar entry. The intended time zone is stated in the payload rather than inferred. | 2.6 | Time Picker in scope | Apple standard |
| 5.14 | A shared location is acknowledged and reflected back | Share a location from the compose bar mid-conversation. | The next message acknowledges it and reflects back the resolved address or place name so the customer can correct it before anything is dispatched on it. It never lands in silence. | 2.6 | Always | Apple standard |
| 5.15 | The confirmation image after a tap stays within the icon ceiling | Tap an interactive element and inspect the confirmation that comes back. | The user\_confirmation image stays within about 150 pixels wide, so the thread reads as a question and an acknowledgement rather than two competing cards. | 2.6 | Any interactive feature in scope | Apple standard |
| 5.16 | Long text kept outside feature bubbles | Review any feature bubble containing more than a short label. | Long text is sent as a separate message outside the bubble. The first line of any feature bubble is its title, since longer text gets cropped. | 2.6 | Any interactive feature in scope | Apple standard |

### 6\. Attachments and Wallet Passes

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 6.1 | Attachments render correctly and are relevant | Trigger every flow that sends an image, PDF, or other attachment. | Attachment renders correctly on-device and is directly relevant to the step in the flow. | 2.5 | Attachments in scope | Apple standard |
| 6.2 | Wallet passes generate and add correctly | Trigger a flow that issues a Wallet pass and tap to add it. | Pass generates with correct details and adds to Apple Wallet end to end without errors. | 2.5 | Wallet passes in scope | Apple standard |

### 7\. Authentication, Apple Pay and Personal Data

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 7.1 | Authentication used for identity verification | Trigger a flow requiring identity or login verification. | The Authentication message type with inline OAuth 2.0 and password autofill is used, rather than collecting credentials as plain chat text. | 2.8 | Authentication in scope | Apple standard |
| 7.2 | Authentication precedes any account data being shared | Ask for an order status, an account detail or a balance without signing in first. | No order detail, account data or balance is returned until the customer has authenticated. This is a positive obligation, not only a prohibition. | 2.8 | Account data in scope | Apple standard |
| 7.3 | Apple Pay used for payment collection | Trigger a flow that requires payment. | Apple Pay is used to collect payment. Full card numbers are never requested as plain text. | 2.8 | Apple Pay in scope | Apple standard |
| 7.4 | Personal data request is gated by a clarifying question | Trigger a flow that asks for name, email or contact details. | A yes or no clarifying question precedes the request, for example "Is your inquiry related to your account with us?". Details are collected only on a yes. | 2.8 | Always | Apple standard |
| 7.5 | Data collection prompts use the QuickType phrasings | Read the exact wording of every prompt asking for customer data. | Prompts use Apple's phrasings exactly, so iOS surfaces a QuickType suggestion and no typing is required. | 2.8 | Always | Apple standard |
| 7.6 | No health data collected, echoed, or stored | Trigger a flow where a user might disclose a health condition or diagnosis. | The bot declines to engage with the health detail, does not echo it back, and nothing is logged or stored downstream. Confirm this explicitly with the client rather than assuming. | 2.11 | Always | Non negotiable |
| 7.7 | Privacy Policy and Terms of Use are Rich Links, sent only twice | Trigger a first engagement, then a second and third conversation. | Both are sent as Rich Links to the brand's webpage, never pasted inline, and only on first engagement or after a policy update. Never at the start of every conversation. | 2.11 | Always | Apple standard |
| 7.8 | No sensitive data is ever requested as plain text | Walk every flow that collects customer data, and review the agent console templates as well as the bot flows. | No full card number, no government ID number, no full social security number and no account password is requested in the thread. Identity goes through Authentication, payment through Apple Pay, and structured sensitive intake through a Form with private responses. | 2.8 | Where sensitive data is collected | Non negotiable |

### 8\. Device Capability and Fallback

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 8.1 | Fallback happens automatically and live | Run the same use case on an unsupported device or OS version. | The experience swaps live, at send time, to a supported alternative, demonstrated on-device rather than described. | Doc 4 | Always | Non negotiable |
| 8.2 | Fallback path is not a dead end | Reach the fallback path and attempt to continue the use case. | The user can still complete or meaningfully progress the use case through the fallback path. | Doc 4 | Always | Non negotiable |
| 8.3 | Capability data is read on every inbound, not cached once | Send from one device, then send from a second device on the same Apple ID with different capabilities. | The capability list is parsed on every inbound message and the most recent value is stored against the device, so a device switch changes what can be sent. | Doc 4 | Always | Apple standard |
| 8.4 | The console cannot send what the device will not render | In the agent console, open a conversation with a device that lacks a feature in scope. | The unsupported option is hidden or hard disabled for that recipient, so an agent cannot send something the device cannot render. | 2.3 | Live agent in scope | Apple standard |
| 8.5 | The fallback decision tree is documented | Ask to see the written fallback tree, not only its behaviour on device. | A documented tree exists covering every interactive type in scope: the preferred type, the fallback type or sequence, the OS floor that triggers it, and the customer facing copy variant. It is versioned and kept current. Reviewers may ask to see the tree itself. | 2.9 note | Always | Apple standard |

### 9\. Human Escalation and Live Agent Handoff

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 9.1 | Handoff to a live agent is explicitly stated | Trigger escalation to a live agent. | The transition is explicitly communicated, and the agent introduces themselves on joining. The reason for the transfer is given. | 2.3 | Live agent in scope | Non negotiable |
| 9.2 | Wait time is communicated | Trigger escalation when no agent is immediately available. | An estimated wait time is communicated, with queue position where available. | 2.3 | Live agent in scope | Apple standard |
| 9.3 | Key details are collected before escalation | Escalate mid-task and observe what the agent receives. | Essential information is gathered before routing, so the agent can help without re-asking. | 2.3 | Live agent in scope | Apple standard |
| 9.4 | An in conversation message is the first option when no agent is available | Request a person while the team is offline or at capacity. | Leaving a message in the conversation is offered first, with a stated response window. Callback and email are offered afterwards, never as the first option. | 2.3 | Live agent in scope | Apple standard |
| 9.5 | Out-of-hours escalation stays in-thread | Request a live agent outside business hours. | The user can leave a message within the current thread. They are not forced out to an external email system, and an agent replies to that message in the same thread. | 2.3 | Always | Apple standard |
| 9.6 | Contextual escalation stays in-channel | Trigger a flow where an email to support would be drafted on the user's behalf. | The bot helps compose the email within the channel rather than abruptly shifting the user away from the conversation. | 3.5 | Email escalation in scope | Field |
| 9.7 | First response service level is documented | Confirm with the client what the committed first-response time for a live agent is. | A specific figure is documented and available to reference if Apple asks. | 2.15 | Live agent in scope | Apple standard |
| 9.8 | The agent console experience is good on both sides | Sit with an agent through a real escalation and watch both the console and the device. | The customer feels responsiveness. The agent can read the thread easily and send what the conversation needs, including rich elements, without friction. A slow or awkward console shows up on the customer's screen as silence and plain text. | 2.3 | Live agent in scope | Apple standard |
| 9.9 | The escalation acknowledgement states a specific commitment | Escalate, choose the offered path, and read the acknowledgement message. | The confirmation states what happens next and when, with a specific figure, for example "a team member will call you within two business hours". A vague acknowledgement such as "someone will be in touch" is a review finding. | 2.3 | Live agent in scope | Apple standard |

### 10\. Policy, Consent and Conversational Design

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 10.1 | Opt-in captured before non-transactional notifications | Reach any flow that would enroll the customer in ongoing automated notifications. | Explicit opt-in is captured as an active tap before enrollment, and the record persists brand, channel, purpose, destination, source, timestamp and disclosure version. | 2.9 | Notifications in scope | Non negotiable |
| 10.2 | The enrolment template carries its own opt out instruction | Read the enrolment and confirmation message templates. | The opt out instruction sits in the template itself, not only in the moment of consent. Apple's shape: welcome, brand name, automated disclosure, then "Reply STOP anytime to turn off notifications." | 2.9 | Notifications in scope | Apple standard |
| 10.3 | STOP re-entry shows a "Welcome back" message | Opt out via STOP, then message the brand again to re-subscribe. | The bot recognizes the re-entry and responds with a "Welcome back" style message. | 2.9 | Notifications in scope | Apple standard |
| 10.4 | Restarting restores reply permission, not notification consent | Opt out of notifications, then start a fresh conversation and complete a task. | The brand may reply inside that conversation. It may not resume notifications. The two states reset separately. | 2.9 | Notifications in scope | Apple standard |
| 10.5 | Satisfaction survey timing and format | Complete an individual FAQ interaction, then complete a full end-to-end use case, then close a conversation. Review the survey itself. | A survey fires only after a real resolution. Not after every FAQ answer, not before the task is resolved, and never after a close, a Leave Conversation or an opt out. It uses descriptive labels rather than a bare one to five scale, delivered as a Quick Reply, or a Form Message for a multi question survey. | 2.10 | Survey in scope | Apple standard |
| 10.6 | Channel constraints on unsolicited surveys respected | Check whether the brand has a protective agreement affecting unsolicited messages to its end users, for example school districts and parent inboxes. | Where such agreements exist, survey timing is controlled by the brand or institution rather than fired automatically. | 2.10 | Survey in scope | Field |
| 10.7 | No dead ends anywhere in the flow | Walk every branch of the conversation design, including error and edge-case paths. (Single unclassified inputs are tested at 4.8.) | Every path has a clear next step, a fallback, or an escalation route. Never a dead end. | 2.4 | Always | Non negotiable |
| 10.8 | No unsolicited outbound | Review every outbound path the platform can fire: campaigns, scheduled sends, retries, replays, notification jobs and agent console templates. Attempt an outbound to a customer with no open conversation and no accepted invitation. | Outbound is only sent inside an ongoing customer initiated conversation, or through an approved Business Invitation template. No SMS style marketing blasts and no unsolicited sends. Reviewers actively look for this. | 2.9 | Always | Non negotiable |

### 11\. Recording and Submission Prep

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 11.1 | Recorded on a real iPhone, not a simulator | Confirm the recording device before capture. | Recording is captured on a physical, supported iPhone. Simulators are not used for the submitted recording. | Doc 4 | Always | Non negotiable |
| 11.2 | All rehearsal threads deleted before final recording | Review the conversation thread list immediately before recording. | No leftover rehearsal or test threads are visible. Only the clean take is recorded. | Doc 4 | Always | Apple standard |
| 11.3 | Recording shows the customer point of view | Review the recording setup. | The recording captures the customer's device screen. Backend logs are not shown. The one exception is the live agent sequence, which is filmed side by side with the console. | Doc 4 | Always | Apple standard |
| 11.4 | Recording demonstrates all required elements | Review the full recording against Appendix A. | The recording shows the rich features in scope, the live agent interaction, and out of hours messaging and fallback. | Doc 4 | Always | Non negotiable |
| 11.5 | Recording split into multiple parts if long | Assess total recording length against a single-take format. | If the journey is long, the recording is split into clearly labelled parts rather than forced into one continuous take. | Doc 4 | Always | Apple standard |
| 11.6 | Timestamp index submitted alongside the videos | Export the Evidence column of this checklist. | A timestamp list accompanies the videos, one line per demonstrated item: video, time, and what it shows. | Doc 4 | Always | Apple standard |
| 11.7 | Change summary prepared for resubmissions | Before resubmitting after feedback, prepare accompanying documentation. | A summary references each feedback item by its ID or description and explains how it was resolved. | Doc 1 s7 | Resubmission only | Apple standard |
| 11.8 | All feedback items addressed before resubmission | Cross-check every item on Apple's feedback report against the fix log. | Every feedback item is addressed. Partial fixes are not submitted, since they typically trigger another review round and delay launch. | Doc 1 s7 | Resubmission only | Non negotiable |

### 12\. Entry Point Configuration, Buttons and Readiness

| Ref | Test case | Test steps | Expected result | Rule ref | Applies when | Severity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 12.1 | Every entry point carries an Intent ID | Inspect the URL behind each entry point in scope. | Every entry point carries a distinct biz-intent-id, and a biz-group-id where routing applies. | 2.13 | Always | Apple standard |
| 12.2 | Entry point URLs contain no reserved characters | Inspect each entry point URL for the characters & \# \[ \] ( ) { } / | No URI reserved characters appear inside parameter values. | 2.13 | Always | Apple standard |
| 12.3 | The message body is pre filled where it helps | Open each entry point and look at the compose field. | A body parameter pre-populates the message so the customer only has to tap Send. | 2.13 | Always | Field |
| 12.4 | Buttons use one of Apple's four approved calls to action | Review every Messages button placement. | Buttons use Message Us, Contact an Agent, Ask a Question or Get Help, and Apple's assets are used as supplied without modification. | 2.14 | Website or app button in scope | Apple standard |
| 12.5 | Buttons are not enabled before the account is approved to go live | Confirm the launch sequence with the client. | No Messages button is live on any public surface until the account is approved. | 2.14 | Website or app button in scope | Apple standard |
| 12.6 | Entry points stay enabled outside business hours | Load each entry point outside stated hours. | Buttons are not disabled out of hours. Automation handles the response. | 2.13 | Always | Apple standard |
| 12.7 | Registered phone numbers are tappable and in E.164 format | Inspect the phone numbers on the brand's website and profiles. | Numbers are tappable and formatted E.164, so Message Suggest can attach to them. | 2.13 | Message Suggest in scope | Apple standard |
| 12.8 | Response time expectations are set in the welcome message | Read the welcome message. | Realistic and honest expectations are stated up front, and communicated dynamically where live agent wait times vary. | 2.15 | Always | Apple standard |
| 12.9 | Naming scanned beyond the conversation copy | Search interface labels, onboarding copy, templates, marketing surfaces and localisation bundles. | Correct product naming everywhere, not only in the flow. Where an interface needs an unknown contact label, it reads "Apple Messages contact", never "Apple Business Contact". | 2.12 | Always | Apple standard |

\========

# Part 4\. Brand Experience Review Recording Guide, version 1.0

## Apple Messages for Business

### Brand Experience Review: Recording Guide

*What to film, what to leave out, and how to make the recording good enough to be worth watching*

**Prepared by Messaging Advisory** Version 1.0  |  1 September 2026

### Document metadata

* document: Brand Experience Review Recording Guide  
* version: 1.0  
* scope: video capture for a brand experience review. The process is in Document 1, the design standards in Document 2, the test cases in Document 3\.  
* audience: the client and MSP teams who will hold the phone and press record  
* used at: Steps 4 and 5 of the process

## What this document is, and is not

This is a **brand** experience review document. Its audience is Apple, assessing whether **this brand's experience** is good enough for a real customer. It is not the MSP integration review, and the difference is not cosmetic.

The integration review asks whether a platform can do everything, for any brand it onboards. It is answered by breadth: show every feature, show every variant, populate every optional field, because a field the platform cannot fill is a capability gap. In that document an empty field is a failure.

The brand review asks whether **your customer has a good time**. It is answered by depth: pick the journeys that matter to your business, build them properly, and film them as a real person would live them. Here a feature you do not need is not a bonus. It is padding, and it reads on camera as a demonstration rather than an experience, which is the impression you least want to leave.

So the three rules that shape everything below:

1. **You do not need to use every element.** Use what the task genuinely needs.  
2. **You do not need to showcase everything.** Coverage is not the goal.  
3. **Focus on the use case, then demonstrate that use case.** One journey done beautifully beats six done thinly.

There is one boundary on rule one. Apple fails "text only experiences that do not leverage platform features". No single feature is mandatory, but using none of them fails. The mandatory thing is the category, not any item in it. A well built journey with a Quick Reply, a List Picker and a Rich Link is complete. Ideally a form, a time picker or a map would complete the journey, and an App Clip or an App Extension will end it on a high note. The same journey in prose is not.

## Choosing what to film

Almost every Apple Messages for Business brand use case is one of five shapes. Find yours, and the table tells you what the journey is made of and which extension blocks it usually picks up.

| Archetype | The customer wants to | Typically uses but not limited to | Often adds |
| :---- | :---- | :---- | :---- |
| **Find and choose** | Browse options and pick one | Quick Reply triage, List Picker with images, Rich Link | Apple Pay, Wallet pass, App Clip |
| **Book and manage** | Reserve, move or cancel a slot, or deliver something | Quick Reply, Time Picker, Rich Link confirmation | Authentication, Maps payload, Form |
| **Check and resolve** | Find out what happened and fix it | Quick Reply triage, Rich Link, attachments | Authentication, escalation, Form |
| **Enrol and receive** | Sign up and be kept informed | Quick Reply, Form, opt in | Business Invitations, Wallet pass |
| **Reach a person** | Talk to someone who can decide | Quick Reply triage, escalation | Form for details, callback path |

For some brands the real journey is a combination of them, for example find, choose and then manage.

Pick **one primary archetype** for the main recording. If your brand genuinely has two very different journeys, film the second as a short additional take rather than stretching one flow to cover both.

**A test before you commit.** Say your use case out loud in one sentence, from the customer's point of view, with no product names in it. "I want to move my delivery to Saturday." "I want to know why my bill went up." "I want to book a fitting." If you cannot say it in one sentence, you have picked a category rather than a use case, and the recording will wander.

## Demo guidelines

These apply to every brand recording. They mirror how the video is reviewed.

* **Use a real device.** Film on a physical iPhone, not a simulator and not a sandbox, so the experience looks like what a customer would see. iOS 26 as the primary device.  
* **Use QuickTime.** Connect the device and record through QuickTime mirroring, or use direct iOS screen recording. Native resolution, no edits. If you need a second take, submit the second take in full rather than stitching two together.  
* **One continuous take.** Start at the entry point and run through to Leave Conversation. A cut invites the question of what happened in the gap.  
* **Film the customer's screen.** The default point of view is the person holding the phone. Backend logs are not shown. The one exception is Flow B, where the live agent sequence is filmed side by side.  
* **Side by side where a person is involved.** Agent console on one side, customer device on the other, both legible at the size the reviewer will watch, so typing indicators are visible in both directions.  
* **Typing indicators everywhere.** A short indicator before every outbound message, including back to back messages with no customer input between them, from the live agent as well as the automation. About one second for automated messages. This is the single item most often missed on film by builds that do it correctly in production.  
* **Frame every rich element with a preceding agent bubble.** A short text message immediately before every List Picker, Time Picker, Form, Quick Reply, Rich Link, Authentication card and Apple Pay request. First line a clear title, second line a short call to action. Long text never goes inside the element, where it is cropped and the customer decides without reading it.  
* **Confirm back after every tap.** When the customer selects, submits or completes anything, the next message says in plain language what they just chose, before the conversation moves on.  
* **Iconography.** Have brand iconography ready for every rich element you use, with a fallback image where a specific one does not exist. A missing image is more visible on camera than anywhere else.  
* **Gate every personal data request.** Before asking for personal information, a clarifying yes or no question, and collect only on a yes.  
* **Clean the thread before the final take.** Delete every rehearsal conversation. A thread list full of prior attempts is visible in shot and reads as an unstable build.  
* **Check what else is on screen.** Notifications, other conversations, the device name, internal tooling. Anything in frame is submitted.  
* **Timestamps.** Attach a timestamp list of each demonstrated item alongside the video.

#### Prohibited wording

Never on screen and never in the presenter's narration:

* "This conversation has been closed"  
* "Finish conversation"  
* "iMessage" as the name of the channel  
* "Apple Business" as the name of the channel  
* "iMessage app" as the name of an App Extension  
* "Messaging rates may apply"  
* "Data rates may apply"

**Naming convention.** Use "Apple Messages for Business" wherever it fits. "Apple Messages" is the approved alternative where the full name does not fit a label. Where an interface shows an unknown contact, use "Apple Messages contact", never "Apple Business Contact". The naming rule governs the console, the narration and the templates, not only the message copy.

#### Where the recording goes

Send the videos and the timestamp index to Messaging Advisory. We review them against Documents 2 and 3 and test the live experience on real devices ourselves before anything goes forward. Apple reviews the recording, gives feedback, and a live session usually follows.

Ideally, Messaging Advisory has access to the test experience before the video is recorded, so we can give direct and proactive feedback before you commit resources to filming.

## What separates a good recording from a complete one

**Completeness gets you through.** This section is what makes the difference between a reviewer ticking boxes and a reviewer wanting to use your brand. It has no equivalent in the integration review, because nobody cares whether the experience feels real. Here it is the entire point.

**Use real content, not placeholder content.** Real product names, real prices, a plausible order number, photographs rather than grey boxes. "Product 1" and "Lorem ipsum" tell a reviewer the experience has never been used by anyone.

**Give the customer a reason.** Decide before you film who this person is and why they are messaging today. A customer with a motive behaves differently from a hand tapping through a script, and it shows in the pacing.

**Let the customer read.** Pause where a person would pause. Instant taps on a List Picker the moment it renders look like automation testing automation. A beat before the choice is more convincing than any amount of polish.

**Write like a person.** Short bubbles, two or three lines. Proper casing throughout. Match the customer's register without abandoning the brand's. Ask questions and behave in ways that genuinely challenge intent recognition, for example sending several messages at once, so Apple sees how the assistant gets past that rather than only how it handles the easy path.

**Show the thread being useful, not being clever.** A feature that appears because the flow needs it lands well. The same feature appearing because it was on a list lands badly, and reviewers can tell the difference easily.

**Do not narrate the obvious.** If you talk over the video, say what the customer is trying to achieve, not what the reviewer can already see. And remember the naming rules apply to speech.

**End it properly.** The close is the part teams rehearse least and reviewers remember most. Offer further help, confirm the outcome, and let the customer end the conversation.

## How to read the flows

#### Actors

* **User, also called end user on device.** The person on the device. Sends messages, taps interactive elements, and controls when the conversation ends.  
* **Agent (bot).** The automated assistant on the business side. It always identifies itself as automated and never implies a person is present when one is not. It can be an AI or a traditional chatbot.  
* **Human agent.** A live person on the business side, reachable through escalation. From the moment of handoff the User is talking to a real person, and the conversation is presented that way.

#### Notation

* **Step.** A numbered move in the conversation. Steps run in order and form one continuous take.  
* **Side by side.** The conversation is rendered twice, the end user on device on one side and the business side on the other, so both perspectives and both typing indicators are visible at once.  
* **What it shows.** A short note on what each step demonstrates, written so it stays true for any brand.  
* **\[BRACKETS\].** Replace with your own.

## Flow A. The use case, end to end

This is the spine. It holds for all five archetypes. What changes between them is which extension blocks you drop in at Step 5, and nothing else. One continuous take, customer side, from entry point to close.

**Step 1\. Entry point**

**User:** starts the conversation from a real entry point, for example a QR code, a website button, an app or an email link.

**Agent (bot):** receives the routing context carried by the entry point, and the conversation lands in the right flow.

If the entry point carries intent, film a second entry point that carries a different intent and show it landing somewhere visibly different. That is more convincing than any explanation.

*What it shows: the entry point works, and routing is real rather than decorative.*

**Step 2\. Greeting, disclosure and scope**

**Agent (bot):** a short typing indicator, then a greeting inside 5 seconds that states plainly it is automated, gives the assistant's name, and says what kind of experience this is and what it can help the customer with. Not "what can I help you with?" but "I'm an automated agent and I can help you with ...".

**User:** knows who they are talking to and what is on offer before sharing anything.

To be clear: disclosure alone is not enough. "I am `[NAME]`, here to help with `[A]`, `[B]` and `[C]`" is the pattern. A bot that discloses and then asks "what can we help you with?" leaves the customer no wiser.

*What it shows: honest automation, prompt response, and a scope the customer can act on.*

**Step 3\. The opening choice**

**Agent (bot):** where the entry point did not already tell you the intent, offer a Quick Reply of up to five real top intents, most common first.

**User:** taps one, or writes their intent in their own words.

Two things to get right. If the customer has already written a clear intent, answer it rather than overriding it with the menu. And if an AI layer handles triage instead of a fixed menu, show it doing better than a menu would, since that is the only thing that justifies replacing one.

*What it shows: a guided opening drawn from real demand, and an assistant that listens.*

**Step 4\. Confirm what you already know**

**Agent (bot):** reflects back the context it holds, for example the order, the store, the booking, rather than asking for it again.

**User:** is not asked to repeat anything.

*What it shows: the conversation uses what it was given.*

**Step 5\. The task**

This is where the archetype takes over, and where your extension blocks go. Two to four steps, no more. Each rich element is preceded by a framing bubble and followed by a confirmation of what the customer chose.

Whatever the task, it should be visibly the thing the customer came for, and it should complete.

*What it shows: the use case actually working, with platform features used because the task needed them.*

**Step 6\. Resolution**

**Agent (bot):** states the outcome plainly. What has been booked, ordered, changed, answered or sent, and what happens next.

**User:** can see the thing they wanted has happened.

A conversation that stops without confirming an outcome reads as abandoned, even when the task succeeded.

*What it shows: the customer leaves knowing where they stand.*

**Step 7\. Anything else**

**Agent (bot):** asks whether there is anything else, as a Quick Reply so a single tap answers it.

*What it shows: the close is offered rather than imposed.*

**Step 8\. Leave Conversation and the post close block**

**User:** ends the conversation using Leave Conversation.

**Business side:** attempts to send, on camera, and is blocked.

Show the blocked attempt. Do not assert it. This is one of the five points and one of the most common reasons a recording comes back.

*What it shows: the customer controls the end of the conversation, and the block is real.*

## Flow B. When a person is needed

Filmed side by side, console and device. This is a second take, and it can start from the same entry point.

**Step 1\. The customer asks for a person**

**User:** signals it, both ways if you can: once with a trigger word such as AGENT, and once with free text such as "this isn't helping" or "can I talk to someone".

**Agent (bot):** classifies both, and errs toward escalating. A missed escalation is worse than an extra one.

*What it shows: escalation intent is detected from words and from meaning.*

**Step 2\. Collect what the agent will need**

**Agent (bot):** gathers the essentials before routing, so the customer is not asked again on the other side.

*What it shows: the handoff respects the customer's time.*

**Step 3\. Announce the handoff**

**Agent (bot):** says a person is joining, and why. Where the response is not immediate, gives an estimated wait, with queue position if you have one.

*What it shows: nobody is left guessing.*

**Step 4\. The person arrives**

**Human agent:** joins, introduces themselves by name, and picks up the thread without asking the customer to repeat anything.

**User:** sees the typing indicator while the agent composes, and a real exchange follows.

Type it live. A scripted paste looks like a scripted paste.

*What it shows: a real person, presented as a person, on a console that is not slowing them down.*

**Step 5\. Close**

**Human agent:** confirms the outcome and offers further help. The customer ends the conversation, and both bot and agent are blocked from sending afterwards.

*What it shows: the same close discipline applies to people as to automation.*

**Where a live connection is not available.** Film the agreed alternative instead: the in conversation message offered first, with a stated response window, then callback or email after. Collect details in channel. The acknowledgement states specifically what happens next and when. "A team member will call you within two business hours" passes. "Someone will be in touch" does not.

## Flow C. When conditions are not ideal

Short, and it can be one take. This is what proves the experience holds up outside the happy path.

**Part 1\. Out of hours**

**User:** reaches the brand outside stated business hours and asks for a person.

**Agent (bot):** states the hours, says when a reply will come, and offers to take a message **inside the conversation** as the first option.

**User:** leaves the message. Film that.

Never pretend a person is available. Callback and email are alternatives offered after the in conversation message, not instead of it.

*What it shows: honest handling when nobody is there.*

**Part 2\. Capability aware fallback**

**User:** on a second, more limited device, a Mac or an iOS 18 device, runs the same use case.

**Agent (bot):** swaps the unsupported element for a supported alternative at send time, and the journey continues to completion.

Two things must be visible: the swap happening, and the fallback path still finishing the task. Describing this in narration does not count. Apple wants to see that a fallback exists, and it is on the brand to demonstrate it.

*What it shows: a real customer base with mixed devices is safe on this experience.*

## Extension library

Drop these into Flow A, Step 5, only where the use case genuinely uses them. Each is written to stand alone. If your journey does not need one, leaving it out is the correct choice, not a gap.

**Rich Link.** Every URL renders as a Rich Link with an image that reflects the destination page, never a bare URL and never a "tap to load" text link. Preview asset is a PNG at 240 by 240, up to 200 kB. Logo style images stay under 150 pixels wide.

**List Picker.** Frame it, then send it. Rows carry a thumbnail and a subtitle, not a title alone. The card itself carries its own image, which is a separate rule from the row thumbnails and the one most often missed. Show the variants your use case actually has rather than all of them.

**Quick Reply.** Two to five options, most common first. Use it for any bounded question rather than forcing typed text. The summary text left in the transcript afterwards is a short label, not a repeat of the question.

**Time Picker.** Multiple slots, and where the appointment happens somewhere, a populated location so the venue and map pin render inside the picker and travel to the calendar. State the time zone. Show the customer adding it to their calendar.

**Form.** Only for structured intake of several fields. For one or two fields, a plain conversational exchange is preferred. Give it a splash screen with an image, a title, an introductory description and a review page at the end of the final section. Mark sensitive responses private. Have a fallback ready for devices below iOS 18.4.

**Authentication.** A framing message before the card, for example "Please log into your account so I can pull up your order". Inline OAuth 2.0 with Password AutoFill. Use it before returning any order detail, account data or balance. No brand image on the card, since it renders with Apple's own iconography.

**Apple Pay.** Framing message first, then the sheet showing line items, payment methods and delivery options. Confirm back what the customer selected. No brand image on the sheet. Never request card details in the thread.

**Attachments and Wallet pass.** Send and receive the types your use case needs, and make sure they are legible on screen. A Wallet pass is worth showing where the journey naturally produces one, a ticket, a booking or a pass, and the customer adds it on camera.

**Construct Payload, Maps.** Where you share a location, send it as a Maps payload rather than a plain address, so the customer gets a map preview and can navigate.

**Construct Payload, Apple Music.** Build the storefront URL from the locale on the incoming message rather than hardcoding a country.

**Construct Payload, App Clip.** Where a task genuinely continues better outside the thread, an App Clip opens it without an install.

**App Extension.** A custom mini experience inside the thread. Worth it only where the interaction is too complex for the standard elements, for example a rich catalogue or a configurator. Call it an App Extension on camera, never an iMessage app.

**Tapbacks.** If a customer reacts to a message, acknowledge it. Reactions arrive as ordinary messages and cannot be threaded to a specific bubble, so acknowledge in context rather than claiming precision you do not have.

**Shared location.** A customer can share their location from the compose bar. Acknowledge it, reflect back the resolved place, and let them correct it before anything is dispatched on it. Never let it land in silence.

**Business Invitations.** Where the journey starts from an invitation, show the acceptance and then the message that follows it, explaining plainly what the customer signed up for, the category, a realistic frequency, and how to stop.

**Notification enrolment.** Opt in is an active tap, never inferred, and the moment of consent states how to opt out. Film the enrolment message carrying its own opt out instruction.

**Multilingual.** Language follows the device locale. Never open by asking the customer which language they want. If a different language is detected, confirm with a Quick Reply before switching.

## Two proposed walkthroughs

Both are hypothetical and fully generic. They exist to show how the same spine produces two very different recordings.

#### Walkthrough one. Book and manage

`[BRAND]` is a service business. The customer wants to move an existing appointment.

1. **Entry point.** Taps the Messages button on the booking confirmation page. Intent carries "I want to amend a booking".  
2. **Greeting.** "Hi, I'm `[NAME]`, `[BRAND]`'s automated assistant. I can help with bookings, changes and cancellations."  
3. **Opening choice.** Skipped. The entry point already carried the intent.  
4. **Confirm context.** "I can see your appointment on `[DATE]` at `[LOCATION]`. Is that the one you'd like to change?" Quick Reply, yes or no.  
5. **The task.** Authentication before showing booking detail. Framing bubble, then a Time Picker with the real available slots and the venue location populated. Customer picks one, adds it to their calendar. Confirmation states the new time.  
6. **Resolution.** "You're moved to `[NEW TIME]` at `[LOCATION]`. I've sent the updated confirmation." Rich Link to the booking page. Maps payload for the venue.  
7. **Anything else.** Quick Reply.  
8. **Close.** Customer leaves the conversation. Send attempt blocked on camera.

Extensions used: Authentication, Time Picker, Rich Link, Maps. Extensions deliberately not used: Apple Pay, Form, App Extension, Wallet pass. Nothing is lost by their absence.

Nice to have: locale detection, so the language follows the device.

#### Walkthrough two. Check and resolve

`[BRAND]` is a consumer business. The customer has a problem with something they received.

1. **Entry point.** Scans a QR code on the packaging. Intent carries "order issue".  
2. **Greeting.** Discloses automation, names its scope.  
3. **Opening choice.** Quick Reply: damaged, wrong item, missing item, something else.  
4. **Confirm context.** "I can see order `[NUMBER]`, delivered `[DATE]`."  
5. **The task.** Customer sends a photograph of the problem. The assistant acknowledges what it received. Framing bubble, then a List Picker of resolution options with images, replacement, refund or a call back. Customer chooses. Confirmation states the choice.  
6. **Resolution.** "A replacement is on its way, arriving `[DATE]`." Rich Link to tracking.  
7. **Anything else.** Quick Reply. Customer says yes, and asks something the assistant cannot classify. It apologises, re offers options including a route to a person, and the customer declines.  
8. **Close.** Customer leaves the conversation. Send attempt blocked on camera.

Extensions used: attachments, List Picker, Rich Link. Extensions deliberately not used: Authentication, Apple Pay, Time Picker, Form. This journey is shorter than walkthrough one and is not worse for it.

## The five points checked every time

Whatever the brand, these five are the most common reasons a recording is sent back. All five must be visible somewhere across the three flows.

* **Reachable escalation.** A live agent connection is reached, or the agreed alternative is offered and acknowledged with a specific commitment.  
* **Honest automation.** The automation identifies itself as automated and never implies a person is present when one is not.  
* **Leave Conversation respected.** The close is honoured, and a send attempt afterwards is shown being blocked.  
* **Capability aware fallback.** The swap to a supported alternative happens at send time, on device, and the journey still completes.  
* **Clean language.** None of the prohibited wording appears on screen or in narration.

## The timestamp index

Submit a timestamp list alongside the videos. One line per demonstrated item: the video, the time, and what it shows.

```
V1  00:04   Entry point, QR code, intent carried into the flow
V1  00:11   Greeting, automated disclosure, assistant scope
V1  00:20   Quick Reply, four real top intents
V1  00:48   Context confirmed, no repeat question
V1  01:15   Framing bubble, then List Picker with row thumbnails and card image
V1  01:44   Choice confirmed back in plain language
V1  02:30   Resolution stated, Rich Link with page image
V1  02:52   Anything else, as a Quick Reply
V1  03:10   Leave Conversation, blocked send attempt shown
V2  00:34   Escalation by free text
V2  00:51   Handoff announced, wait time given
V2  01:20   Agent joins, introduces themselves, types live
V3  00:08   Out of hours notice, message left in conversation
V3  01:02   Fallback swap at send time on a limited device
V3  01:30   Fallback path completes the task
```

If you filled in the Evidence column of Document 3 while testing, this list already exists. Export it.

## Why recordings come back

In rough order of how often we see each one.

1. A typing indicator missing on a back to back sequence  
2. The rich card filmed without its own image, showing only the row thumbnails  
3. Leave Conversation asserted rather than demonstrated, with no blocked send on screen  
4. A bare URL or a "tap to load" link visible in the thread  
5. Capability fallback described in narration instead of filmed  
6. Placeholder content, grey boxes and "Product 1" in shot  
7. Rehearsal threads visible in the conversation list  
8. Restricted platform wording spoken in the voiceover  
9. Out of hours filmed as a generic greeting rather than as a live agent request outside hours  
10. Features included because they were on a list, making the whole thing read as a demo

## Before you press record

- [ ] The use case is one sentence, from the customer's point of view  
- [ ] Document 3 has been run in full and the in scope rows pass  
- [ ] Content is real: real products, real prices, plausible names and numbers  
- [ ] Brand iconography is in place for every rich element used, with fallbacks  
- [ ] Filming on a physical iPhone through QuickTime, native resolution  
- [ ] A second, more limited device is on hand for Flow C  
- [ ] Out of hours can be triggered, or the schedule has been adjusted for the take  
- [ ] Rehearsal and test threads deleted  
- [ ] Notifications silenced and nothing unintended is in frame  
- [ ] Side by side capture set up and both panes legible for Flow B  
- [ ] Typing indicators confirmed on every outbound payload, both directions  
- [ ] Every rich element has its framing bubble and its confirmation reply  
- [ ] Narration script checked against the naming rules  
- [ ] The timestamp index is open and ready to fill as you film

### Provenance

* Apple, Pass the Experience Review v3.1, 21 July 2026  
* Apple, Conversation Design Standards v3.1, 21 July 2026  
* Apple, Messages for Business Use Cases form  
* Messaging Advisory, Video Review Flow Instructions generic v6.6, adapted from platform scope to brand scope  
* Messaging Advisory, Conversation Design Standards and Best Practices v2.1  
* Messaging Advisory field observations from prior brand submissions

