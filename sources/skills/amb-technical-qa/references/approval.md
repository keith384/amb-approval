# Approval, Experience Review, PR & Commercial

## Contents

- [MSP approval](#msp-approval)
- [Experience Review](#experience-review)
- [Brand approval](#brand-approval)
- [Demo guidance](#demo-guidance)
- [Pre-launch PR](#pre-launch-pr)
- [Commercial](#commercial)
- [Open with Apple](#open-with-apple)

---

## MSP approval

**The checklist is 74 items**, of which 32 are technical. The rest cover capability and go-to-market review, entry-point routing, messaging restrictions, escalation behavior, pre-review UX preconditions, recording production, message history handling, and platform capability gates.

Historically MSP approval has taken 12 to 18 months. Linq completed it in roughly six to seven weeks and is the second agentic-AI MSP Apple has approved.

**After approval** comes a private phase: the MSP can discuss the approval and onboard its first brand. Once that brand is fully live, the final gate clears and the MSP goes public. Brand onboarding can begin roughly a week after approval.

**Post-approval, the MSP is steward of the experience.** Apple has transferred responsibility for enforcing its standards. Practically, the sales team must know the guidelines well enough that no brand is surprised at review — no brand should be rejected for attempting something they were already told not to do. That requires a conversational design document following Apple's guidelines and formal team training.

**Apple's ongoing concern is drift** — brands getting approved for one experience and shipping something different three to twelve months later. Apple mystery-shops for this but it doesn't scale. Monitoring for drift is both what Apple wants and the path to earning pre-approval authority.

## Experience Review

The gate between a restricted test account and public launch, per brand. Results are delivered to the **MSP**, who relays them to the brand — Apple does not go direct.

Plan 2-4 weeks for AMB account approval including Experience Review.

It is a qualitative evaluation of conversation flow, agent etiquette, and use of rich elements — not a technical check. The full process, the pre-submission quality bar, the three required recordings, and Apple's recurring UX feedback are in `experience-review.md`. Read that file for anything about getting an experience approved.

**The non-negotiables**

- A live agent reachable when the customer types "help," at any hour
- Rich Links rather than bare URLs — a plain URL rendering as "Tap to Load Preview" is an explicit rejection criterion and the single most common failure
- Don't re-ask for information the customer already provided
- Working opt-out
- No PII requested in plain conversation
- Unsupported types hidden in the agent console, not merely blocked on the send path

Treat these as hard requirements in QA before booking the review.

## Brand approval

Every brand experience is reviewed individually and personally signed off at Apple. The MSP tells the brand's story from the brand's perspective and shows how the platform safeguards the user experience. A live demo isn't strictly required but helps where nuance needs discussion.

**What Apple asks about each brand:** use case, how each feature will be used, how the agentic model works, recordings of the journeys, and what value the brand brings to society.

**Migration submissions** from iMessage should carry: current volumes, growth expectations, use cases, the current experience, the planned AMB experience, plus screenshots and user stories.

**Migrated experiences must be A-to-A-plus, not like-for-like.** Apple expects the migrated experience to demonstrably use AMB capabilities the brand didn't have on iMessage — Apple Pay, forms, Wallet — and that improvement gets reviewed.

**Screening criteria for migration candidates:** percentage of current volume on iMessage, dependence on group messaging, message volume and growth trajectory, and the societal-value question.

**The consumer AI pause.** Apple has paused consumer-facing AI apps on the channel while it settles its own AI strategy. The distinguishing test: is conversational AI the *product* or the *channel*? A general consumer-facing assistant is in the paused category. AI supporting an existing non-AI business is acceptable.

## Demo guidance

Run roughly three eight-minute chunks with an agenda slide up front, checkpoint questions at each break, and nothing skipped — Apple wants everything shown. 30 to 40 minutes is acceptable and rushing is discouraged. Apple asks questions throughout, so time control matters.

**Do not drive the demo agentically.** Agentic responses are non-deterministic, can be open-ended, and are exposed to prompt injection. A rehearsal where the agent hit a stale state and refused to send delivery windows made the case. Use a scripted spine that walks every required feature deterministically with the AI muted, and turn the agent on at the end as a bonus so reviewers can request elements in natural language.

**Structure it in two parts:** dynamic rendering first — auto-generated list pickers, quick replies, and other elements with no hard-coded flows — to collect immediate feedback. Then full feature coverage with fixed flows and human escalation, showing the platform side and the user experience side by side.

**Roles that worked:** one person opens, frames the session, and takes business and go-to-market questions; one drives the demo and fields technical questions; one keeps time and closes rabbit holes.

**Reframe escalation positively.** Use catering or a compliment rather than a failed order, so the demo never ends on an implied failure.

## Pre-launch PR

Apple treats launch PR as a joint MSP-and-brand reviewed process with fixed lead times, not a self-certification. Apple grants permission to publish rather than issuing PR itself.

**Embargo.** PR is reserved for when the feature is fully available to customers — not at sign-off, soft launch, or go-live, but after the first brand is live. No public reference to the launch or to Apple involvement before that point, across press releases, blog posts, social media, website copy, and sales collateral.

**Lead times**

| Submission | Lead time |
|---|---|
| PR approach, plan, media list | ≥ 6 weeks before outreach |
| Press release | 2–3 weeks for review |
| Blog posts and pitches | 2 weeks for review |
| Press images, videos, detailed pitches | Before distribution |
| Public metrics or numbers | Before publishing |

Content can be fully accurate and still miss the window. A joint release is the default; a separate brand release is approved only case by case.

**The PR plan must contain:** objectives and audience, approach and tactics with where materials will be published, press list with named reporters and timing, execution timeline with key dates, and next steps.

**Prohibited language**

- No claim of an exclusive or Apple-endorsed relationship beyond what Apple approved
- No "first to do X" statements
- No claim, stated or implied, of end-to-end encryption
- No overstatement of automation, identity resolution, or security
- Nobody speaks on Apple's behalf; press inquiries relating to Apple are forwarded to Apple PR
- All materials must make clear that messages come from the brand, not from Apple

**Banned disclaimers in customer-facing copy:** "data rates may apply," "messaging rates may apply," "This chat may be recorded," or any similar phrasing.

**Privacy policy and terms** must be reachable via a rich link presented at first engagement — not inline, and not repeated at the start of every conversation.

**Terminology.** Consumer-facing copy says "Apple Messages." The full formal service name is reserved for technical, registration, and developer materials. "Business Chat" appears nowhere.

**For legal:** Apple may use the brand's name, logos, screenshots, designs, and implementation in its own promotion and marketing. Get legal sign-off on all external claims relating to Apple, privacy, and security.

**Marketing guardrails pre-approval:** invitations may go to an unlimited list as direct communication, but nothing may be posted publicly and nothing goes to analysts or investors. The Apple value proposition page stays private and unlisted until MSP approval. Only the MSP may claim MSP status, once approved.

Source: Apple's Messages for Business PR guidance, [Apple Business Register](https://register.apple.com), and the [AMB Service Terms](https://register.apple.com/tou/bca/latest/en).

## Commercial

**Apple charges nothing per message.** Cost is concentrated in the upfront MSP investment, which is the barrier to entry. Apple also charges no fee for Apple Pay within AMB, including subscriptions.

**How MSPs price.** Three models. Per-message is rarest. Most price by chat window — a session opens, closes at 24 hours or on completion, and is billed. Pricing across the industry is heavily gated and hard to source.

**Linq's model** is contact-based, in tiers. Any inbound or outbound message or window opening counts as a contact, which ties to agent unit economics and allows charging upfront or net-30 rather than post-period true-up. Enterprises want predictable pricing — fixed or projected monthly amounts rather than open-ended usage — and pricing should stay competitive against SMS and RCS benchmarks.

| Tier | Price |
|---|---|
| 200 contacts | $260 |
| 1,000 contacts | $220 |
| 10,000+ contacts | Enterprise, negotiable, around $1.00 per contact |

**Onboarding timeline impact:** a customer can sign and pay, then wait weeks to months for Apple approval before going live.

**Ideal customer profile** (MA): iPhone-heavy audience with strong mobile traffic, high-value customers, three to five repeatable high-volume contact reasons, expensive voice or chat demand, executive sponsorship and accessible APIs, and a measurable revenue or service outcome. Beachhead verticals: travel and hospitality, premium commerce, marketplaces, AI-native startups. Finance, insurance, and telecom enter later, after identity, audit, and data governance controls are proven.

## Open with Apple

Current as of late August 2026. Check whether any have resolved before repeating them as open.

- Under the merchant-managed model, may a merchant register and verify an MSP-controlled subdomain, with the MSP hosting the association file the merchant downloaded?
- Does the no-proxy/no-redirect requirement preclude serving the well-known path through a CDN or reverse proxy, or only HTTP redirects on that path?
- For AMB specifically, where the registered domain authenticates the merchant session rather than hosting a button, is a gateway-only subdomain an acceptable registered merchant domain?
- Does the hosted-payment-pages restriction apply to the AMB payment gateway endpoint, or only to hosted web checkout?
- Multi-device form delivery — the Mac rendering gap, raised as an enhancement.
- App and thread identifier examples above the 2 billion limit, for the ongoing app ID discussion.
- In-place iMessage app updates failing despite the session identifier.
- Form `dynamic.version`: Apple's spec says 1.1, MA guidance says 1.2. Unresolved.
- Whether an MSP may operate a proxy/shell iMessage app for brands without their own — would require App Store approval and is a novel arrangement.
- International brand eligibility — believed workable via a US presence, mechanics unconfirmed.
