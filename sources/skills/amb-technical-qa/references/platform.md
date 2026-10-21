# Channel Fundamentals, Entry Points, Consent & Platform

## Contents

- [Channel fundamentals](#channel-fundamentals)
- [Encryption and what may be claimed](#encryption-and-what-may-be-claimed)
- [Compliance boundaries](#compliance-boundaries)
- [Identity and addressing](#identity-and-addressing)
- [Entry points and BCRW](#entry-points-and-bcrw)
- [Conversation rules](#conversation-rules)
- [Consent and opt-out](#consent-and-opt-out)
- [Data retention](#data-retention)
- [Client landing page](#client-landing-page)
- [Inbound validation](#inbound-validation)
- [Platform capabilities and the sandbox question](#platform-capabilities-and-the-sandbox-question)

---

## Channel fundamentals

AMB messages appear inside the Messages app but are a separate service from iMessage — separate API, separate team at Apple, different security properties. Apple enforces the distinction in language.

**Terminology.** "Apple Messages for Business" in technical, registration, and developer material. "Apple Messages" in consumer-facing copy. "Business Chat" is deprecated and must not appear anywhere public or customer-facing. Apple supplies its Messages logo in SVG and PNG for use on the client landing page and BCRW buttons.

**No Android.** Apple devices only.

**No group chat.** This is the substantive capability loss versus iMessage and there is no direct equivalent.

**No cold outbound.** The customer must initiate through an entry point, or accept a business invitation — which itself requires a prior opt-in collected at the brand's point of sale.

**Threads persist.** Conversation history stays alive, which is what makes the human-escalation requirement workable.

**Apple's liability** for the service is contractually capped at $50, provided as-is, with no uptime guarantee. Relevant when setting expectations for payment or other business-critical flows. See the [AMB Service Terms](https://register.apple.com/tou/bca/latest/en).

## Encryption and what may be claimed

iMessage is peer-to-peer with end-to-end encryption — quantum-safe, per Apple.

AMB is different. Messages are encrypted at rest and in transit within Apple's infrastructure, but **Apple acts as an encryption endpoint** — content is decrypted on Apple's servers before being forwarded to the MSP. Apple→MSP transport is TLS 1.2. Apple decrypts for content review against prohibited terms.

**The claim "AMB is end-to-end encrypted" is prohibited**, stated or implied, in press releases, blog posts, social media, website copy, and sales collateral. It is also simply false.

What can be said accurately: fully encrypted in transit under Apple's infrastructure, with Apple as the encryption endpoint. Supporting points that hold up: nothing is stored at Apple after delivery, conversations are scoped to opaque per-brand identifiers, and there has been no breach of Apple Messages in the eight years it has existed.

Public privacy and security statements must be consistent with this — transport encryption with data decrypted on Apple servers before forwarding.

## Compliance boundaries

**HIPAA.** Healthcare use cases are not currently permitted and no HIPAA BAA is published for AMB. If a brand is in healthcare, raise it before building rather than after.

**PII.** Do not request highly sensitive PII in plain conversation. The platform must prevent it. Authentication is the sanctioned path for anything requiring verified identity; forms are the path for structured collection.

**Prohibited industries.** Sex and adult content, drugs, and alcohol, plus the standard prohibited categories. Health is a gray zone.

**GDPR.** Apple's own security and compliance position: the MSP is the data controller, the brand–MSP arrangement governs, and everything beyond blocking further messages is outside Apple's scope.

## Identity and addressing

A conversation is identified by the pair of **Opaque ID** (the customer) and **Business ID** (the brand). Messages arrive at the MSP's `/message` endpoint keyed only by those two values, never by brand name — which is why the client landing page exists.

The Opaque ID is the fixed pairing of one customer's Apple Account with one brand's Business ID. It does not change when the customer upgrades or switches device. A customer contacting two brands has a separate Opaque ID and separate thread for each.

On inbound, `sourceId` is the customer's Opaque ID and `destinationId` is your Business ID. They reverse on outbound.

**Phone numbers** are not used for normal conversations. Business invitations are the exception — addressed to a phone number, which is why they carry their own consent rules and namespace. Accepting an invitation creates the Opaque ID; the mapping runs through the sender ID field.

## Entry points and BCRW

**BCRW** is Apple's entry-point domain for starting a conversation from a URL:

```
https://bcrw.apple.com/urn:biz:<business-id>?biz-intent-id=account_question&biz-group-id=credit_card_department&body=Order%20additional%20credit%20card
```

- `biz-intent-id` — purpose of the chat
- `biz-group-id` — routing target, e.g. a department
- `body` — pre-populated message text the user can edit

On the first inbound message the MSP reads intent and group from the payload to route. **Parameter values must not contain reserved URI characters** such as `& # [ ] ( ) { }` and `/`. Links can be shortened; redirects are fine.

Why Apple cares: the conversation shouldn't open with "how can I help you" when the entry point already says the user scanned a specific code in a specific place. It also powers IVR deflection. Apple provides no reporting of its own here, so MSP-built reporting on entry point, group, and intent is a genuine differentiator (MA guidance).

**Capture once or every click?** Both are defensible; expose the choice to the brand. Most users click once and thereafter use the thread; some repeatedly scan different codes. Track every intent ID, store first-touch separately from subsequent state, and let the brand decide whether a new intent ID changes context.

**The entry points**

| # | Entry point | Notes |
|---|---|---|
| 1 | Business invitations | Business-initiated to a phone number previously provided. Yes/No prompt; Yes opens the conversation and creates the Opaque ID |
| 2 | Email, SMS, social | BCRW string as a tappable link; opens Messages on Apple devices |
| 3 | Website button | Apple's button markup; does not render on non-Apple devices |
| 4 | In-app | BCRW via `UIApplication.open()` or a deep link; iOS apps only |
| 5 | Message Suggest | Tapping an AMB-registered phone number surfaces "Message Us" instead of calling. Works from corporate sites, Apple and Google Maps, and search engines |
| 6 | Apple Maps card | Message button on the place card. **No intent signal is passed** and there is no accompanying context. Per AMB brand activation |
| 7 | QR code | Static QR encoding a BCRW string; camera launches Messages, user sends the first message. Different codes can drive different bot flows |
| — | NFC | Supported |
| — | Wallet | Passes act as entry points |
| — | Voice / IVR | Invitation triggerable from a voice experience |

**Fallback page.** Configured at brand level alongside OAuth and Apple Pay. It should deflect non-Apple users into an alternate channel — SMS, RCS, WhatsApp, or email — so Android users land somewhere useful rather than a dead end. Brands need it standing before launch.

**For review:** Apple wants every *element* demonstrated, not every entry point. Two or three entry points suffice; what's checked is handling of intent ID, group ID, and body.

## Conversation rules

1. Automated first response within **5000 ms** of the conversation opening
2. The agent must identify itself as automated — no opt-out from this
3. An escalation path to a live agent within the conversation, with history available to that agent
4. No promotional or SMS-style marketing
5. Explicit opt-in capture, MSP-handled or verifiably brand-handled
6. Business hours specified and communicated on escalation
7. Typing indicators in both directions

**Typing indicators** are bidirectional, persist 60 seconds, with a one-second minimum enforced and API consumers advised to manage their own timing.

**Escalation.** Requesting a human puts the conversation into handoff-requested: neither AI nor human can respond without a force override. It queues with an SLA; claiming it moves to handoff-accepted with typing indicators inserted on behalf of the human and templated messages available. Handing back re-enables automation. Marketing consent is tracked separately from willingness to talk to a human.

**Out of hours:** Apple's demo feedback was that leaving an asynchronous message in the chat should be the **primary** option, ahead of callbacks or external email.

**Unrecognized intent:** present a clarifying Quick Reply rather than guessing. Ambiguous stop words get their own clarification — all messages, automated replies only, or never mind.

**Closed conversations:** sending into one returns `409 conversation closed`.

**Symbols:** disallowed symbols are rejected at the API. Raw rejection errors need humanizing before an end user sees them.

**Bot disclosure** works best through persona rather than compliance language — tie it to the agent's character and move on.

## Consent and opt-out

This describes Linq's implementation against Apple's rules, not Apple specification.

**Capture.** At the brand's own point of sale — website, app, customer service line, or physical location — applying only to the transaction it was collected for. The brand attests it to the MSP via API, recording the number in E.164, which POS surface it came from, and when. Owning the record doesn't mean you can send: enforcement is always the MSP's.

**Keywords.** Only marketing can be granted by keyword, via `subscribe`, which is Apple's own rule. Account notifications and invitations can never be granted by keyword — deliberately, so nothing routes around the required disclosure or POS collection. Sending `subscribe` on a phone-number thread records nothing at all, which means someone who previously opted out cannot be re-consented by a stray keyword. Invitation consent has exactly one door: the attestation.

**Granularity.** Per brand, per category, per customer. Four categories: transactional, account notification, marketing, invitation. Transactional is exempt inside an active chat; the other three each need their own opt-in. A marketing opt-in cannot satisfy an account-notification send.

**Expiry.** Hard two-year ceiling from grant — Apple's ceiling. Longer requests are clamped. Evaluated at send time rather than by a background job, so a stalled sweep can't let a stale grant through.

**Enforcement.** Gated at accept time and re-checked at delivery. No opt-in returns 403, no overrides, force flags don't bypass. Batches add two more passes — every recipient screened at submit, then re-evaluated at fan-out — because a consent read at submit is a screen rather than a license. The decision that counts is always the last one before the message leaves. Anything already queued when someone opts out stays suppressed permanently.

**Opt-out.** STOP / UNSUBSCRIBE / QUIT plus phrase variants ("stop texting me", "take me off your list"), case-insensitive. A stop is **total and brand-scoped**, not thread-scoped, and it silences transactional replies too. Leave Conversation is a hard stop at every send path. Both honored immediately, AI agent and human alike.

**Declining an invitation is not opting out.** Measured against production Apple rather than inferred: the thread stays open and consent stays intact. The real opt-out is Leave Conversation, which causes Apple to send a `CloseSession` carrying the phone number; that revokes invitation consent for the number automatically and notifies the brand. Continuing to invite after a CloseSession is a terms-of-service violation on Apple's side. (Apple's own entry-point material describes a declined invitation as blocking further invitations until re-subscribe — Linq's measured behavior is the more precise account.)

**After an opt-out**, nothing reaches that number until a fresh opt-in is collected at the POS and attested. There is no in-channel path back, by design.

**Partial opt-outs.** Apple defines none. Phrases like "stop the bot" or "no more AI" are intercepted with a Quick Reply confirming intent before acting — automation pauses before the question renders. Choosing "stop all messages" writes the same total opt-out a bare STOP does.

**Re-engagement.** If the customer writes back, that lifts the blanket suppression and only that. Marketing still needs an express subscribe; account notifications still need the disclosure opt-in. Never retroactive.

**Audit.** Every grant, revoke, and expiry is an append-only event carrying source and timestamp, surfaced to brand operators in the chat view and to AI agents via webhooks.

## Data retention

Apple sets no retention period, no deletion deadline, and no erasure requirement anywhere in its terms or policies. Nor does Apple specify any encryption-at-rest requirement. Retention is the MSP's to define and defend.

**Apple stores nothing after delivery.** Brand-facing material must never claim or imply Apple stores, backs up, or can recover chat history — there is no Apple-side copy to request, subpoena, or restore from.

A chat exists in two places: the customer's devices and the MSP platform. Every journalable inbound and outbound event is appended to a per-chat, gapless, append-only journal. Typing indicators are deliberately never written down — they have no durable meaning and are wrong the moment they're stale.

**Linq's operational windows**

| Data | Window |
|---|---|
| Idempotency keys | 24 hours |
| Inbound duplicate-detection records | 24 hours |
| Completed background job rows | 24 hours |
| Sign-in sessions | 12 hours |
| Delivered webhook records | 30 days |
| Delivery records | 90 days |
| Connect link attempts and hits | 90 days |
| Customer attachments | 30 days |
| Chat history | No expiry today |

Windows are swept on a schedule and compared against the database clock rather than any single host's.

**Attachment deletion is enforced twice over:** the application sweep removes the database row and the stored object, and an independent storage lifecycle rule expires the bytes regardless of whether that sweep ran. A test reads the infrastructure configuration and fails if the two disagree, because a retention rule that silently matches nothing reads exactly like one that is working.

**Partner reads are honest about it.** Timeline responses carry the retention horizons they were computed against, plus a marker distinguishing "this was swept" from "this never happened." A reference to an aged-out attachment answers 404 rather than pretending the bytes are still there.

**Brand-level deletion is a crypto-shred.** Archive objects and stored attachments are encrypted under a per-brand customer-managed key; destroying the key renders that brand's archived history and attachment objects unreadable whether or not every object has been collected.

**Cold tier rule: archive before drop, never the reverse.** No data is dropped before a verified cold copy exists. Exports run as explicit operator commands with an explicit window and no defaults — a bare run is a preview that writes nothing. An export is counted independently of the rows it streams, and written objects are read back and hashed before the ledger records the partition as verified. A partition that fails verification is not eligible to be dropped. A window must have been closed at least an hour before export so a long-running read can't contend with live traffic.

## Client landing page

A single HTTPS page the MSP hosts. When a brand finishes selecting you as its MSP in Apple Business Register, Apple sends them here so the Apple-issued Business ID can be tied to a client record in your system — their tenant, agent routing, and channel settings. Hosting one with account linking is a required MSP capability Apple checks for approval, alongside centrally hosting per-brand channel settings.

Without it you have a Business ID with nothing to map it to, and no way to route a brand's traffic to the right configuration, agents, and back-end integrations.

**What Apple sends:**

```
https://<YourSiteHost>/<YourSitePath>?id=<BusinessChatID>&name=<BusinessName>&logo=<LogoURL>
```

| Parameter | Notes |
|---|---|
| `id` | The Business ID (UUID). Store as the key for this brand's channel and settings |
| `name` | Display name, URL-encoded |
| `logo` | URL to the brand's logo, URL-encoded — decode and validate before fetching |

Read with a **GET** handler — you are rendering a page for a person. Field names are case-sensitive. Validate and safe-encode each value exactly once.

**On a valid request:** authenticate the brand into your platform or create their tenant and client record; link the Business ID to a client ID associated with the brand's name and logo; save the brand's channel settings against that record.

**Hosting requirements.** Publicly reachable over HTTPS with a valid SSL certificate whose issued name matches the hostname, including the entire trust chain with intermediate CAs and root, present in the Oracle Java 8+ default trust store. **No tunneling** — Ngrok and other firewall-defeating technologies may result in declined requests for messaging, the landing page, or authentication endpoints.

**Registering the URL:** Apple Business Register → Connected Services → Messaging Service Providers → your Commercial MSP → Server Configuration → Client Landing Page URL → Edit → Save → Submit.

**Gotchas to build for:**

- Internal test accounts return only the Business ID, no name or logo. The handler must tolerate their absence rather than erroring.
- The "Connect to <platform>" link appears only after Apple approves the account, and never shows for private MSPs. If it's missing or grayed out, the account is still under review.
- Apple cannot assist with MSP account linking, so handle failures your side and give brands a clear retry path.

## Inbound validation

Validate every inbound message:

1. `destination-id` matches a valid Business ID in your system
2. The `Authorization` header (JWT) validates against your MSP secret
3. Required HTTP headers are present, including reading and storing `capability-list`
4. The body is valid GZIP — gunzip it
5. The result is valid JSON

**Network gotcha:** if you front your messaging endpoint with an HA proxy, allow Apple's address block **17.0.0.0/8** or inbound AMB messages are silently dropped at the proxy.

## Platform capabilities and the sandbox question

Being an MSP means providing a platform brands configure and deploy, not just exposing an API — for quality-control reasons. Ship an API alone and brands hack against it, then ask you to get Apple to approve whatever they built. You are judged on the quality of every brand deployment, so direct brands are the priority and MSP-of-an-MSP arrangements are a possible later bridge, not a starting point. Providing the API to an ISV that generates experiences at arm's length is not permitted.

**Required platform capabilities:** no-code bot builder (brands must be able to build every component themselves, with the same capability the human agent has), message template library, attachment handling, device capability gating, agent console, opt-in/opt-out handling, centrally hosted per-brand channel settings, client landing page with account linking, and Apple Pay.

**The agent console** must take over mid-conversation, build and send every element type including images on list pickers, complete transactions such as refunds, hand back to the agent, run an SLA queue with defined out-of-hours behavior, show tapback reactions, and hide unsupported types rather than merely blocking them on send.

**There is no sandbox.** Every call hits production. The approach is a dedicated test Business ID, configured identically to production and restricted to a whitelist of authorized internal Apple Accounts so real customers can't reach it. Until MSP approval, staging brands can only be created under the MSP's own organization; after approval, brands self-register and select the MSP from the dropdown. The Business ID, not an API key, is the core primitive, linked via the landing page.
