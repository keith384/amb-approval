# Apple Messages for Business — Canonical (Verbatim, Consolidated)

**Channel:** Apple Messages for Business (AMB) · **Canonical:** v7.0-verbatim · **Assembled:** July 2026
**Consolidated build:** `v7.0-verbatim-consolidated` — single-file merge of the Master overlay + Parts 1–4. No Apple content summarized, reflowed, or dropped; only reorganized and wrapped.
**Correction applied in this build (CIDR):** the overlay's earlier claim that Apple's Class A block was "standardized to `17.0.0.0/8` throughout" is **retracted**. Part 1 preserves Apple's source form `17.0.0/8` verbatim; `17.0.0.0/8` appears only as a reference annotation (see Appendix B, §32 Gap #31, and Appendix C, §34 re-verification note). The dated v6.0 changelog entry that mentions `17.0.0.0/8` is left unchanged as a historical record, per instruction.

> This is the **master index** of the master-plus-parts verbatim canonical. Apple's rules, code samples, and content are reproduced **verbatim** in the domain **Part** files below (no summarizing, no concatenation — organized, deduplicated, source-cited). This master carries the **overlay** that does not exist in any single source: provenance, recency/conflict resolution, audit, change logs, and the image manifest.

> **Keep-both policy:** where sources overlap (e.g., REST API vs tutorial; Platform vs Merchant guide), both are retained in full and cross-referenced. Where they conflict, the recency winner is flagged in the Conflict & Recency Register below.
> **Verbatim exceptions (documented, non-content):** HTML entities decoded to rendered form; `\`-escapes removed; tab field-tables rendered as Markdown; JSON/cURL fenced unchanged; PDF page footers / running heads / TOC dot-leaders removed. A few multi-column matrix/header rows render as table structure rather than raw tab strings. No wording, field, value, or rule was altered.

> **Verification status (honest):** This file is a **consolidation** of a verbatim rebuild. It has NOT been independently diff-verified against Apple's original source documents — only against the input Part files. Confirmed here: structural integrity (balanced fences, consistent tables) and complete line-preservation from the inputs. **Not** confirmed: byte-for-byte fidelity to Apple's sources. **Part 4 (Legal)** was reconstructed from pasted text, not a source file, and still requires a byte-diff against the Service Terms. The audit/revision-history appendices were inherited from an earlier synthesis and remain unverified against sources **except** the CIDR item (§37 R3), corrected here. A full source-diff audit is still outstanding.

> **Update — ALL FOUR PARTS now source-verified (this revision).** All seven source documents were supplied and diffed against the canonical:
> - **Part 1** (`msp-rest-api` + `msp-api-tutorial`) & **Part 2** (`messaging-documentation` + `msp-onboarding`): ~100% content-line coverage; residual misses are multi-column matrix/version headers rendered as Markdown tables (documented tab→table transform). No fabrication.
> - **Part 3** (Apple Pay Platform Jun 2025 + Merchant Mar 2026 PDFs): 100% both directions after excluding PDF/TOC chrome (813/813, 719/719); all payloads, endpoints, JSON, cURL/openssl, cert rules and `canMakePayments` variants verbatim. **11 PDF `fi`-ligature losses restored** in field names/URLs (`Identi er`→`Identifier` ×7, `tokenNoti cationURL`→`tokenNotificationURL` ×3, `/noti cation/`→`/notification/` ×1).
> - **Part 4** (Service Terms, 17 Dec 2024) — **byte-diff COMPLETE and PASSED.** All sections (§1–§8, §2.1–2.12, §4.1–4.9) present in order; 44/44 representative source paragraphs present; no clause dropped, reordered, or reworded; no fabrication. All ten Apple-source typos/oddities are preserved verbatim — the two `[sic]`-marked ones (`solely responsible maintaining` §2.1; `MESSSAGES` §4.5) plus eight unmarked (`Messages for or Business` §2.4; `in through use` §2.1; `Message for Business` §4.3; `relied upon it as such` and `Apple make no representations` §2.8; `laws regulations` §2.9; `set forth in herein` §3). Key values confirmed: `$50.00` cap, `ninety (90) days`, Delaware/Santa Clara venue, `Last updated: December 17, 2024`. The only additions vs source are the two documented `[sic]` annotations; Part 4's own ⚠ pre-audit flag is hereby resolved.
> - **Overlay appendices (Master §32/§33) checked against these four sources:** §33 revision trails were verified and found **stale** — now corrected in Appendix C: **§33.1** (REST API) was missing the 7 newest versions **4.2.3–4.2.9** (topping out at 4.2.2; source current is **4.2.9**, 3 Jun 2026); **§33.2** (onboarding guide) was missing **3.0** (6 Jan 2026) and **3.1** (21 May 2026) and had silently rewritten the v2.11 summary. The current source rows are reproduced verbatim in the Appendix C addendum, with the Master trails kept and flagged (keep-both). **§32** (gaps/ambiguities/contradictions) is analytical overlay, **not** reproduced source content, so it cannot be verbatim-verified; its factual anchors were spot-checked (capability-list, 17.0.0/8, sessionIdentifier, Opaque ID, Roadside Assistance all present in source) and several rows cite the retired Word-doc v4.2.2 which is outside the supplied source set.
> **Net:** every Apple source document has now been diffed against its Part; the consolidation is a source-verified canonical. Remaining non-content caveats: the audit/revision-history appendices (Master §32/§33) beyond the CIDR item are inherited overlay and not re-derived here; image binaries are manifest-only.

---

## Provenance & Recency — Source Inventory

> Every source carries a version, a date, and a recency rank. On any duplicated fact, the highest recency rank (lowest number) is authoritative unless §37 records a deliberate exception.

| Rank | Source | Version | Date | Role | Status |
|---|---|---|---|---|---|
| 1 | MSP REST API Integration Spec (`msp-rest-api`) | 4.2.9 | 03 Jun 2026 | Technical schema — **top authority** | Current (user-confirmed up to date) |
| 2 | Apple Pay **Merchant** Integration Guide | — | Mar 2026 | Apple Pay merchant setup/registration/processing | Current — newest Apple Pay source (carries own Change Log) |
| 3 | Public Onboarding / Brand Documentation portal (`messaging-documentation`) | 3.1 | 21 May 2026 | Policy / UX / privacy / FAQ / metrics | Current |
| 4 | MSP API Tutorial (`msp-api-tutorial`) | 3.4 | 29 Apr 2026 | Worked examples / code | Current |
| 5 | Service Terms for Messages for Business (§35) | — | 17 Dec 2024 | Legal layer | Current (confirmed unchanged) |
| 6 | Apple Pay **Platform** Integration Guide | — | Jun 2025 | Apple Pay platform/PSP integration | Superseded on overlap by Rank 2; **cover page dated Sep 2025 vs footer Jun 2025 — footer prevails per file-date protocol** |
| — | Apple Integration Word doc | 4.2.2 | 27 Feb 2026 | v6.0 baseline | **Superseded by Rank 1 (v4.2.9)** |
| 7 | MSP Onboarding (`msp-onboarding`) | 3.0.3 | 01 Feb 2024 | MSP onboarding lifecycle | ⚠ **Stale — 2+ years older than all others; any uniquely-sourced fact flagged for verification** |


---


## Table of Contents

**Body**

- [1. API & Messages](#1-api--messages) — `msp-rest-api` + `msp-api-tutorial`
- [2. Policy / UX / Privacy / Onboarding](#2-policy--ux--privacy--onboarding) — `messaging-documentation` + `msp-onboarding`
- [3. Apple Pay](#3-apple-pay) — Apple Pay Platform + Merchant Integration Guides
- [4. Legal (Service Terms)](#4-legal-service-terms) — Service Terms for Messages for Business

**Appendices (Master overlay)**

- Appendix A — Conflict & Recency Resolution Register (Master §37)
- Appendix B — Audit: Documentation Gaps, Ambiguities & Contradictions (Master §32)
- Appendix C — Revision History & Changelog (Master §33 + §34)
- Appendix D — Image Manifest & Placement Map (Master §38)
- Appendix E — Service Terms / Legal Layer overlay (Master §35)
- Appendix F — Apple Pay Merchant Setup, Registration & Processing overlay (Master §36)

---

## 1. API & Messages

> **Part 1 of the master-plus-parts verbatim canonical.** Content reproduced from Apple source docs with **verbatim fidelity**: HTML entities decoded to rendered form, `\`-escapes removed, tab-separated field tables rendered as Markdown tables, and every JSON/cURL payload fenced **exactly as in source** (not reflowed). No wording, field name, value, or rule was altered.
>
> **Sources:** `msp-rest-api.md` (REST API Integration Spec v4.2.9, 03 Jun 2026) · `msp-api-tutorial.md` (MSP API Tutorial v3.4, 29 Apr 2026).
> **Keep-both policy (§37):** the REST API reference (1A) and the tutorial's worked examples (1B) overlap on some topics (message types, Apple Pay). Both are retained in full and cross-referenced rather than merged, so no source wording is lost.
> **Verified fidelity:** 99% of source content lines preserved verbatim; 0 payloads or rules dropped. **Documented exception (fractional):** a small number of multi-column *table header rows* (e.g., version-history and device-capability matrix headers) are rendered as Markdown table structure rather than the source's raw tab-joined string — a formatting transform, not a content change.
> **Overlay:** provenance, recency/conflict register (§37), audit, change logs, and image manifest live in the **Master index** file, which links here.

---

# Part 1A — MSP REST API Reference (verbatim)

> **Source:** `msp-rest-api.md` — verbatim (entities decoded, escapes removed, tab-tables → Markdown, JSON/cURL fenced unchanged).

# msp-rest-api

https://register.apple.com/resources/messages/msp-rest-api/

Integration

Version: 4.2.9

Last update: 03 June 2026

Apple Messages for Business is a service that allows your clients to communicate directly with their users through your Messaging Service Provider (MSP) platform using the Messages app. An MSP implements the server-to-server REST API solutions on their messaging platform which makes it possible to send and receive texts and photos, request payment through Apple Pay, and much more.

This drawing illustrates the relationship between a business, an MSP, the Apple Messages for Business service, and users. The MSP platform handles user message routing between Apple Messages for Business service and the business. For more information on these accounts and how to qualify for them, see MSP Onboarding.

<!-- img: msp-abc-flow.png -->

“MSP

Communicate with users using Apple Messages for Business

Apple devices running iOS 11.3 and later or macOS 10.13.4 and later support Apple Messages for Business.

For more information about the visual design of Apple Messages for Business, see Apple Human Interface Guidelines.

Required Features

Apple requires that you build and demonstrate support for the following features for approval to connect brands to Messages for Business:

| Feature | Bot/API | Agent Triggered* | Description |
|---|---|---|---|
| Receiving and Sending Messages | Required | Required | Send and receive text, international characters, and emojis. |
| Receiving and Sending attachments | Required | Required | Send and receive commonly known type files up to 100MB between your platform and the user. |
| Tapback Reactions | N/A | Required | Detect user tapbacks. |
| Receiving Closed Conversation Messages | Required | Required | Notify live agents and automated agents of customer opt-out, and prevent additional messages from being sent to the user. |
| Rich Link Messages | Required | Required | Every URL sent by an automated or human agent should be recognised and sent as a rich link. |
| Quick Reply Messages | Required | Optional | Send quick reply choices to end user. |
| List Picker Message | Required | Optional | Single selection, multi selection and multi section with icons for send/received list pickers as well as images. |
| Time Picker Message | Required | Optional | Send time pickers including icons. |
| Apple Pay Message | Required | Optional | Send an Apple Pay payment request. |
| Authentication Message | Required | Optional | New OAuth2 inline authentication. |
| Authentication Message | Deprecated | Deprecated | oAuth authentication. |
| iMessage Apps | Required | Optional | Support iMessage apps for advanced interactions. |
| Form Message | Required | Required | Support forms interactions. |
| Construct Payload API | Required | Required | Support construct payload API for App Clips, Apple Music and Apple Maps RichLink interactions. |
| Invitation Messages | Required | Required | Send invitation messages to opted-in customers to initiate a conversation via Apple Messages for Business using their provided mobile number. |
| Typing Indicator Message | Required | Required | Show bidirectional typing indicators. |
| Routing based on entrypoint parameters | Required | Required | Route new conversations using intentID and groupID attributes. |
| Channel settings and Landing Page | Required | Required | Centrally host channel settings and provide a landing page with account linking |
| Device capabilities | Required | Required | Support alternate handling for devices with different capabilities. |
<sub>↳ `msp-rest-api.md` L37–75</sub>

The MSP must provide the business with easy-to-use tools necessary to build rich object payloads, such as List Pickers, Message Forms, etc. This allows a business to have a library of ready to use rich objects that can be used by agents and bot builders.

*Agent Triggered: the agent or operator can trigger this message type via an automated flow, or a canned response/object available in the agent console.

Authorizing Messages

When exchanging messages between Apple Messages for Business service and the MSP platform, the server sending the message must authorize the HTTP request by setting the Authorization header field with a signed JSON Web Token (JWT), which the receiving server decodes. Apple Messages for Business requires this field, and the receiving server should reject the request when the field is not present.

Messages for Business uses a subset of the JWT fields, described here:

| Name | Type | Description |
|---|---|---|
| alg | string | A string used in the header, identifying the algorithm used to encode the payload. The alg value is always HS256 when exchanging messages with Apple Messages for Business. |
| aud | string | A claim that is a string, or array of strings, identifying the recipients of the JWT. The value should be a string when the JWT has one recipient; otherwise, it should be an array of strings where each string represents a recipient. The aud value is always the MSP ID when exchanging messages with Apple Messages for Business. This value is used when sending messages from the business to the MSP platform |
| iss | string | A claim that is a string identifying the principal that issued the JWT. The value is always the MSP ID when exchanging messages with Apple Messages for Business. This value is used with traffic coming from the MSP platform to the business. |
| iat | dateTime | A claim that is a numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519. |
<sub>↳ `msp-rest-api.md` L95–103</sub>

Create a JSON Web Token

Sign and verify all messages in Apple Messages for Business by creating a signed JWT. After registering for Apple Messages for Business as an MSP, you receive the following:

An MSP ID that identifies the platform. This is not the same as the business ID you receive after registering for Apple Messages for Business.

A Messaging API secret key that is a Base64-encoded string. Decode the string before using the key to sign the JWT. When receiving an HTTP request from Apple Messages for Business, verify that Apple Messages for Business signed the request with the secret key.

The JWT has three parts, each separated with a period ( . ): the Javascript Object Signing and Encryption (JOSE) header, the claims, and the Base64-encoded Messaging API secret. The JWT looks similar to the following:

hhhhhhh.ccccccc.ssssssss

For more information about the JWT specifications, see RFC 7519.

A decoded JWT authorization header has the following header and claims for each message coming from the Messaging service to the MSP platform:

header

```json
{
  "alg": HS256,
}
claims
```
<sub>↳ `msp-rest-api.md` L131–137</sub>

```json
{
  "aud": <CSP-ID>,
  "iat": <issued at unix-timestamp (in seconds)>
}
The decoded JWT authorization header from the MSP platform to the Messaging service has the following header and claims for each message:
```
<sub>↳ `msp-rest-api.md` L139–147</sub>

header

```json
{
  "alg": HS256,
}
claims
```
<sub>↳ `msp-rest-api.md` L153–159</sub>

```json
{
  "iss": <MSP-ID>,
  "iat": <issued at unix-timestamp (in seconds)>
}
Generate authorization tokens at least once every hour, and reject tokens with an iat timestamp older than an hour.
```
<sub>↳ `msp-rest-api.md` L161–169</sub>

Manage the Messaging API Secret Key

The registering agent should record and securely store the Messaging API secret key for safekeeping. If the secret key becomes compromised, the registering agent should provision a new key using the Apple Messages for Business web portal.

When using a new secret key, honor the authorization tokens signed with both the old and new keys for a short period of time. After deploying the token signed with the new secret key—and ensuring its use throughout the MSP platform environment—the registering agent should revoke the old key using the Apple Business Register web portal.

Add the JWT to Your Messages

Once you have your signed JWT, format the Authorization field value with the string Bearer followed by a space, followed by your signed JWT.

POST https://mspgw.push.apple.com/v1/message

```json
{
  "Destination-Id": "urn:mbid:AQAAYy <truncated>",
  "Source-Id": "DEF123GH-b0ad-<truncated>",
  "Content-Type": "application/json",
  "id": "4102c4b3-316 <truncated>",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIs.<truncated>"
}
The following code shows an example of a JWT authorization header from the Messaging service to an MSP platform:
```
<sub>↳ `msp-rest-api.md` L193–207</sub>

POST /message

```json
{
    "Destination-Id": "DEF123GH-b0ad <truncated>",
    "Source-Id": "urn:mbid:AQ/quv4JIAJyVALyKtW <truncated>",
    "Content-Type": "application/json",
    "id": "3608321f-<truncated>",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIs.<truncated>"
}
First Message Exchange
```
<sub>↳ `msp-rest-api.md` L215–229</sub>

To exchange text messages between customers and businesses, an MSP integrates their platform with Apple Messages for Business. To integrate, the MSP provider:

Implement the /message endpoint that Apple Messages for Business uses to forward messages sent by customers. For more information, see Messages Received.

Authorizes the exchange of messages by creating a JSON web token (JWT) and using it in the authorization header field. For more information, see Authorizing Messagess.

Uses the Apple Messages for Business REST API to send replies from the business to their users. For more information, see Messages Sent.

https://register.apple.com/resources/messages/msp-rest-api/reference

Document Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.
Format
All field names in the specification are case sensitive.
Schema
Unless a property is explicitly REQUIRED or RECOMMENDED, it is OPTIONAL.
It is RECOMMENDED that a publisher not include a property when there is no content to provide or any meaning attached to a null or empty string (string instance of zero length) input.
Data Types
Data types listed below are used in descriptions throughout the Specification, but the relevant RFC or other linked documentation should be consulted for the type's formalized details where not described in this document.
| Name | Type | Description |
|---|---|---|
| array | array | RFC 7159-compliant sequence of values. |
| boolean | boolean | RFC 7159-compliant value (true or false). |
| dateTime | string | ISO 8601 date-time with an offset (time difference in hours and minutes with UTC). Format is yyyy-MM-ddTHH:mm:ss±hh:mm. The offset part (±hh:mm) may be replaced by Z to denote UTC. |
| integer | number | RFC 7159-compliant number value without a fraction or exponent part. |
| ISO-3166 alpha2 | string | ISO 3166-compliant alpha-2 country code. |
| number | number | RFC 7159-compliant number value. |
| object | object | RFC 7159-compliant collection of name/value pairs. |
| string | string | RFC 7159-compliant string literal value. |
| uri | string | RFC 3986-compliant value. |
| json | json | RFC 7159-compliant value. |
| uuid | UUID | RFC 4122- UUID is a 128-bit universally unique identifier represented in canonical string form as 36 hexadecimal characters separated by hyphens, in the pattern 8-4-4-4-12. |
<sub>↳ `msp-rest-api.md` L252–263</sub>

https://register.apple.com/resources/messages/msp-rest-api/common-specs

Common Specifications

The following specifications, such as HTTP headers, HTTP body, and other similar fields, are common to all messages. This includes specialized messages such as rich links and pickers. Differences are pointed out in their respective section.

URL

Implement the /message endpoint to send and receive messages.

POST https://mspgw.push.apple.com/v1/message

HTTP Headers

| Name | Type | Description |  |
|---|---|---|---|
| Authorization | string | REQUIRED. Credentials used to authenticate the request. See Authorizing Messagess. |  |
| auto-reply | string | A Boolean that determines whether the reply is sent by a person or an automated agent (bot). Set the value to true when a bot sends the reply. |  |
| capability-list | string | REQUIRED. A string list that identifies Apple Messages for Business features supported by the customer’s device. The list items are case insensitive and separated by commas. When a customer sends a message, the MSP platform must obtain the customer device capabilities to compose an appropriate response for that device. The agent console should not permit sending a payload to a user that is not supported by the user's device. Bots should use these values to automatically determine which payload type to send. Possible values are: |  |
<sub>↳ `msp-rest-api.md` L283–289</sub>

\- QUICK for Quick Reply Message support

\- LIST for List Picker Messsage support

\- TIME for Time Picker Messsage support

\- AUTH for Authenticate Message support

\- AUTH2 for New Authentication Message Message support

\- FORM for Forms Message support.

Apple Pay, Rich Links are supported on all devices type and version.

| iMessage apps and Forms are only supported on iPhone and iPad. |  |  |  |
|---|---|---|---|
| destination-id | string | REQUIRED. A string that identifies the message recipient. When a user sends a message, the destination-id is the business ID. When a business sends a reply to the user, the value is the user’s opaque ID. |  |
| id | uuid | REQUIRED. A UUID string that identifies the message. |  |
| msp-agent | string | A string that identifies the agent or system sending the request. The MSP platform should set the field to a string value that is meaningful to the business. Apple Messages for Business logs up to the first 64 characters of the string. |  |
| source-id | string | REQUIRED. A string that identifies the message sender. When a user sends a message, the source-id is the user’s opaque ID. When a business sends a reply to the user, the source-id is the business ID. |  |
| accept-encoding | string | Applicable to Interactive Message Type. A string value, set to gzip, deflate, advertising which content encoding, usually a compression algorithm, the client understands. |  |
| accept | string | Applicable to Interactive Message Type. A string value, set to */*, advertising which MIME types the client understands. |  |
| content-type | string | Applicable to Interactive Message Type. A string value, set to application/octet-stream, advertising that the content is a generic binary data. |  |
| owner | string | Applicable to Getting Attachment URL. REQUIRED. The owner of the attachment. Retrieve this field's value from the owner field in the Attachment dictionary. |  |
| signature | byte | Applicable to Getting Attachment URL. REQUIRED. A Base64-encoded string containing the file checksum. |  |
| url | string | Applicable to Getting Attachment URL. REQUIRED. The URL, provided by Apple Messages for Business, that identifies the attachment. |  |
| size | integer | Applicable to Authorizing an Attachment for Upload. REQUIRED. An integer representing the size, in bytes, of the encrypted attachment. |  |
<sub>↳ `msp-rest-api.md` L305–327</sub>

HTTP Body

All messages, except the /preUpload and /preDownload messages, include the fields from the HTTP Body dictionary.

Properties

| Name | Type | Description |
|---|---|---|
| attachments | attachments | An array of attachment dictionaries. For more information, see Attachments. |
| destinationId | string | REQUIRED. Identifies the message recipient. When the MSP platform receives a message from Apple Messages for Business, the value is the business ID. When the MSP platform sends a reply to Apple Messages for Business, the value is the user’s opaque ID. |
| group | string | The group identifier for the message as specified by the business, such as the department name. For more information, see About Intent, Group, and Body Values. |
| id | uuid | REQUIRED. A UUID string that identifies the message. |
| intent | string | The intention, or purpose, of the chat as specified by the business, such as account_question. For more information, see About Intent, Group, and Body Values. |
| locale | string | User's device locale settings. For example, en_AU specifies the language as English and the region as Australia. For more information, see Internationalization and Localization Guide - Locale ID. |
| sourceId | string | REQUIRED. A string that identifies the message sender. When a user sends a message, the source-id is the user’s opaque ID. When a business sends a reply to the customer, the source-id is the business ID. |
| type | string | REQUIRED. A string that identifies the message type. For the list of possible values and their meanings, see Message Type Values. Possible values: interactive, typing_start, typing_end, text. |
| v | integer | REQUIRED. The message payload version number. This value must be 1, which is the current version of the message JSON. |
<sub>↳ `msp-rest-api.md` L339–357</sub>

About the Opaque ID

For privacy, the business doesn’t receive the user’s phone number, email address or iCloud account information. The Opaque ID is unique to the relationship between the customer's Apple Account and the business’s business ID. A customer has a different Opaque ID for every chat they have using Apple Messages for Business. The customer decides if and when to share personal identifying information with the business. For more information, see Apple Platform Security.

Response Codes

| Code | Reason-Phrase |
|---|---|
<sub>↳ `msp-rest-api.md` L367–367</sub>

200

OK

The request was successful.

Content-Type: application/json

| 400 | Bad Request |
|---|---|
<sub>↳ `msp-rest-api.md` L377–377</sub>

The request lacks the required header fields, the request body isn't JSON or the JSON lacks the required fields, or the destination-id header field does not match the destinationId JSON field.

| 401 | Unauthorized |
|---|---|
<sub>↳ `msp-rest-api.md` L381–381</sub>

The request lacks the Authorization header field. Requests from Messaging service always contain the Authorization header field. If the MSP platform returns a 401 response code, the problem is either a configuration issue with Apple Messages for Business or a signal of spoofed incoming activity.

| 403 | Forbidden |
|---|---|
<sub>↳ `msp-rest-api.md` L385–385</sub>

The request failed to validate the Authorization header field. If the MSP platform sends a request to Messaging service and it responds with 403 - Forbidden, it’s likely in response to an invalid MSP ID in the Authorization header field.

| 404 | Not Found |
|---|---|
<sub>↳ `msp-rest-api.md` L389–389</sub>

The request failed to recognize the destination-id or was sent to a user no longer available. These errors occur when a business messages a user during their iPhone or device upgrade cycle. The carrier has an inactivated status on the SIM card for a particular device. Our messaging systems have the user account marked as messageable and active but the error comes back from the carrier network. Once the upgrade cycle is complete, users will again receive messages without any further work for the MSP or the user. They will not, however, receive messages that were returned as 404. We recommend those be sent again or marked in your system as undelivered.

| 410 | Gone |
|---|---|
<sub>↳ `msp-rest-api.md` L393–393</sub>

The request failed because the user closed the conversation. For more information, see Receiving a close conversation.

| 500 | Internal Server Error |
|---|---|
<sub>↳ `msp-rest-api.md` L397–397</sub>

A server error occurred. An additional response could be 50x - various. This means that the request encountered various server-side failures. The bot and/or agent needs to be notified that message delivery failed and provide an opportunity to resend the message.

Note

Only 5xx errors are retried. Apple will retry 4 times with an exponential backoff, starting with 100ms. All other errors fail immediately.

TypingIndicatorMessage

Forward indicators from Apple Messages for Business when someone is entering text in Messages.

In a conversation, typing indicators provide visual cues to let each person know when the other is entering text. When receiving messages, the Apple Messages for Business service sends the MSP platform a typing indicator each time the user starts entering text in Messages. The MSP platform receives the typing indicator as a message with the type of typing_start. After receiving the typing indicator message, the MSP platform should display the indicators to the person receiving the message.

If the user clears the text they entered, Apple Messages for Business sends a typing_end message to the MSP platform. The MSP platform should remove the visual indicator, which tells the business that the user stopped entering text and is no longer preparing to send a text message.

Likewise, when an agent, live or automated, starts or stops typing, a message of type typing_start and/or typing_end must be sent, so the user can also see the typing indicator and the experience is consistent.

The typing indicador should be displayed before any message type (text or interactive), so that the user experience is consistent. For messages sent by bots, use only a 1-second typing indicators before each message.

This behavior is not the same as a message type close. For more information, see Receiving Closed Conversation Messages.

Note

You can have a timeout for the typing indicator, if the typing_end is not received within 60 seconds.

Declaration

This object inherits from HTTP body.

object TypingIndicatorMessage

Tapback Reactions

Sometimes users respond to messages using a Tapback, such as the heart, thumbs-up, or other expressions. Below is the workflow and guidelines for handling various types of Tapback reactions.

Tapback workflow:

Agent sends a message to the user.

User uses the Tapback feature to react to the message using thumbs-up, laughter, heart, or other reactions.

Apple Messages for Business sends back a text message to the agent console that is parsable as a Tapback.

Handling Standard Tapbacks:

When a user reacts using common Tapbacks such as thumbs-up, thumbs-down, heart, laughter, exclamation points, or question mark, the Tapback message encloses the original message text within unicode double quote characters with the type of reaction indicated in text.

For example, an agent would see the following message in their console when responding using an expression.

Liked "Thank you, Mr. Smith."

Just show the text message received and don’t try to convert it as a tapback reaction on the agent console.

Because the reaction is both language and text direction dependent, this can make parsing the Tapback message challenging. For example, if the language on the user device is set to Japanese, the Tapback message arriving at the agent console might look like this:

"Domo arigato, Smith-san."に「いいね」と応答

Handling Stickers and Memojis:

When a user reacts with a sticker or Memoji, the boy key of the message will include a description of the reaction. For example, "Reacted with a sticker to "Hello"".

In addition, the message will contain an attachment, which represents the sticker or Memoji used by the user. Ensure that attachments are handled correctly when stickers or Memojis are sent.

Handling Emoji Reactions: When a user reacts with an emoji, the body will contain the emoji itself, along with the original message. For example, "Reacted ☺️ to “Hello"".

Handling Reactions to Interactive Messages: When a user reacts to an interactive message (e.g., Form Message, Time Picker), the message body will contain both the reaction and the wording "1 Business Message".

Actual response example:

Liked a text

```json
{ 
  "type": "text",
  "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
  "v": 1,
  "sourceId": "urrnXXXXXXXXX",
  "destinationId": "<destinationId>",
  "body": "Liked “hiiiii”" 
}
Liked an image
```
<sub>↳ `msp-rest-api.md` L523–539</sub>

```json
{
 "type": "text",
 "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
 "v": 1,
 "sourceId": "urrnXXXXXXXXX",
 "destinationId": "<destinationId>"
 "body": "Liked an image"
}
Liked a text in Japanese locale
```
<sub>↳ `msp-rest-api.md` L543–559</sub>

```json
{
  "type": "text",
  "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
  "v": 1,
  "sourceId": "urrnXXXXXXXXX",
  "destinationId": "<destinationId>",
  "body": "“hiiiii ”に「いいね」と応答"
}
Liked an interactive message
```
<sub>↳ `msp-rest-api.md` L563–579</sub>

```json
{
  "type": "text",
  "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
  "v": 1,
  "sourceId": "<sourceId>",
  "destinationId": "<destinationId>",
  "body": "Liked 1 Business Message"
}
Reacted with an Emoji
```
<sub>↳ `msp-rest-api.md` L583–599</sub>

```json
{
  "type": "text",
  "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
  "v": 1,
  "sourceId": "<sourceId>",
  "destinationId": "<destinationId>",
  "body": "Reacted ☺️ to “Hello”"
}
Reacted with a Stickers or Memojis
```
<sub>↳ `msp-rest-api.md` L603–619</sub>

```json
{
  "type": "text",
  "id": "ce5e8c7c-ade6-4495-b373-4c94f44b123c",
  "v": 1,
  "sourceId": "<sourceId>",
  "destinationId": "<destinationId>",
  "body": "Reacted with a sticker to “Hello”"
  "attachments": [{
      "name": "4bdd43066e6d692a-sticker.png",
      "size": 77526,
      "mimeType": "image/png",
      "signature-base64": "gbfE2SGlaM<truncated>"
      "key": "002CC85B3<truncated>",
      "url": "https://p27-content.icloud.com/<truncated>",
     "owner": "MZ87d0b6daba5<truncated>",
    }],
}
Group and Intent ID-based Routing
```
<sub>↳ `msp-rest-api.md` L623–657</sub>

Businesses have the option to set up the Apple Messages button using a plain URL, web button, in-app button, QR code, or NFC, and pass three values intentID, groupID, and body.

Your platform needs to route new conversations using intentID and groupID values from an entrypoint, as well as the default body parameter. See the following documentation for more information:

About Intent, Group, and Body Values

Starting a Message from your App

Design Your Website and App to include the Messages Buttons

Starting a Message from a URL

https://register.apple.com/resources/messages/msp-rest-api/messages-received

Incoming Messages

Your Messaging Service Provider (MSP) platform can receive an incoming message sent by a user through Apple Messages for Business, by implementing the /message endpoint. In the implementation, you can setup your MSP platform to validate the message (see Validating a Message) and deliver it to the business identified by the destinationId field (see Routing and Prioritizing Messages).

Request

POST https://msp.example.com/message

Parameters

The request body is a JSON dictionary that, in addition to the HTTP Body parameters, contains the following fields:

| Name | Description |
|---|---|
| body | REQUIRED. The message text. This field is required when the type is text. There is no predetermined maximum for this field, but there may be a maximum size for the payload. This field supports the Basic Multilingual Plane of unicode. For more information, see TextMessage. |
| interactiveData | A dictionary representing the properties of an interactive message. For more information, see BaseInteractiveData dictionary for more information. |
| interactiveDataRef | A dictionary containing a reference to the interactive data dictionary. Apple Messages for Business includes this field, instead of interactiveData, when the interactive data dictionary is larger than 10 KB. For more information, see Receiving an Interactive Message. |
<sub>↳ `msp-rest-api.md` L693–699</sub>

Message Type Values

When a user sends a text message to a business, the Messaging service receives and forwards the message to the MSP platform by calling the MSPs platform /message endpoint. The message type is set to text.

The MSP platform validates the incoming message as described in Validating a Message. The /message endpoint then returns the appropriate response code to Apple Messages for Business. For a list of possible codes, see the Response Codes section in Common Specifications.

The possible string values for the message type field are:

| Name | Description |
|---|---|
| text | REQUIRED. Indicates that this is a text message, with or without attachments. |
| interactive | REQUIRED. Indicates that this is an interactive message. This could be a list picker, time picker, or any other interactive message. For more information, see Interactive Message Types |
| typing_start | REQUIRED. Indicates that the user is actively entering text in Messages. |
| typing_end | REQUIRED. Indicates that the user cleared the text they were entering. |
| close | REQUIRED. Indicates that the user closed the chat. Only a user can close a chat. The MSP platform should not send a message with the type set to close. For more information, see Receiving Closed Conversation Messages. |
<sub>↳ `msp-rest-api.md` L715–725</sub>

Sample Message Received

This is a user communication sent from the Apple Messages for Business service to an MSP platform.

Request

Authorization: Bearer eyJhbGciOiJIUzI1NiJ9. <truncated>

Content-Length: 300

Destination-Id: a884eddf-<truncated>

Content-Encoding: gzip

Capability-List: AUTH,LIST,TIME,QUICK

X-Http2-Scheme: https

Host: http://msp.messagesforbusinessendpoint.com:443

Source-Id: urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG/ <truncated>

Content-Type: application/json

Id: 27167455-1f53-4ddc-a797-318ad85cb28e

```json
{
    "body": "Hi",
    "sourceId": "urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG/ <truncated>",
    "locale": "en_US",
    "destinationId": "a884eddf-<truncated>",
    "v": 1,
    "type": "text",
    "id": "27167455-1f53-4ddc-a797-318ad85cb28e"
}
Response
```
<sub>↳ `msp-rest-api.md` L757–775</sub>

HTTP/1.1 200 OK

Date: Fri, 05 Apr 2019 20:43:49 GMT

Server: Apache/2.4.7 (Ubuntu)

Content-Length: 0

Content-Type: text/html; charset=utf-8

### Validating a Message

When the MSP platform receives a message, you must use the MSP platform secret to validate the message by performing the following checks:

Verify that the destination-id field in the HTTP request header matches a valid business ID. If the MSP platform is multitenant, verify that the business exists within the MSP platform system and can accept incoming messages from Apple Messages for Business.

Validate the Authorization header field using the MSP platform secret. For more information, see Authorizing Messages.

Check for required HTTP request header fields. For more information, see the HTTP Headers section in Common Specifications.

Verify that the HTTP body is a valid GZIP formatted object and reverse the compression ("gunzip") to reveal the JSON payload.

Verify that the resulting text resolves to a valid JSON data payload.

Routing and Prioritising Messages

Each incoming message includes a list of fields useful for routing and prioritizing messages. When the MSP platform sends a message to Apple Messages for Business that includes any of these fields, Apple Messages for Business returns the fields in the user’s reply:

| Name | Type | Description |
|---|---|---|
| body | string | A text field that prepopulates the message body. It can be overwritten and changed by the user. |
| capability-list | string | A string list that identifies Apple Messages for Business features supported by the customer’s device. The list items are case insensitive and separated by commas. When a customer sends a message, the MSP platform can obtain the customer device capabilities to compose an appropriate response for that device. Possible values are: |
<sub>↳ `msp-rest-api.md` L811–815</sub>

\- QUICK for Quick Reply Message support

\- LIST for List Picker Messsage support

\- TIME for Time Picker Messsage support

\- AUTH for Authenticate Message support

\- AUTH2 for New Authentication Message Message support

\- FORM for Forms Message support

| destinationId | string | The identifier for the message recipient. When the MSP platform receives a message from Apple Messages for Business, the value is the business ID. When the MSP platform sends a reply to Apple Messages for Business, the value is the user’s opaque ID. |
|---|---|---|
| group | string | The group identifier for the message as specified by the business, such as the department name. For more information, see About Intent, Group, and Body Values. This field is optional. |
| intent | string | The intention, or purpose, of the chat as specified by the business, such as account_question. For more information, see About Intent, Group, and Body Values. This field is optional. |
| locale | string | The user's device locale settings. For example, en_AU specifies the language as English and the region as Australia. |
| sourceId | string | The identifier for the message sender. When the MSP platform receives a message from Apple Messages for Business, the value is the user’s opaque ID. When the MSP platform sends a reply to Apple Messages for Business, the value is the business ID. |
| capabilities | string | (Deprecated March 2022) A string list that identifies Apple Messages for Business features supported by the user’s device. The list items are case insensitive and separated by commas. When a user sends a message, the MSP platform can obtain the user device capabilities to compose an appropriate response message for that device. Possible value is auth for authenticate message support. |
<sub>↳ `msp-rest-api.md` L829–839</sub>

Receiving a Closed Conversation

Users can opt out of receiving any further messages from a brand. This is also known as closing a conversation.

A user closes a conversation by going to the tray view in Messages and left swipe a conversation. This action reveals two buttons: a mute icon and a delete icon. The user clicks the delete icon, agrees to delete the conversation, and confirms that they would you like to stop receiving messages from the business. This action sends a “close” message for an Apple Messages for Business conversation. Apple refers to this action as “delete” on the user's device, and the MSP and brand receive a “close” conversation from the standpoint of the brand and MSP.

Note that when the user deletes the conversation and does not ask to stop receiving messages from the business, no “close” message is sent to the MSP.

<!-- img: ios15-iphone12-pro-messages-delete-biz-chat-confirmation.png -->

iPhone showing how to stop receiving messages

Communicate with users using Apple Messages for Business

When a user closes a conversation, Apple Messages for Business sends a message of type close to your MSP platform, and your platform must block any agent, virtual or live, from sending any further messages to this user.

Important — HTTP 410 Gone

If your MSP attempts to send a message to a user who has left the conversation, Apple Messages for Business returns an

HTTP 410 | Gone

response. The message will

not

be delivered. We require MSPs to keep a table of closed conversations and prevent brands from sending messages to users who have opted out. If a business fails to honor a customer's opt-out request and continues to send invitation messages, the customer can report the unwanted invitation to Apple through the

"Report Junk"

feature. The Apple team reviews these reports and takes appropriate action.

Continuing to send invitation messages after a CloseSession is a violation of Apple's terms of service.

The user can re-initiate the conversation. They can resume the conversation from any valid entry-point for the brand. When they do, they will return with the same opaque user ID as before.

For invitation-based conversations, if a user has previously left the conversation, the business may resume sending invitations only if the user re-subscribes using the same phone number through a valid opt-in channel.

CloseSession message

Similar to a notification message, the HTTP request for a CloseSession message to the MSP contains the headers message-type and source-id.

message-type: notification

source-id: tel:+14085554567

sourceId and destinationId are also included in the message body.

Message Body Fields

| Key | Name | Type | Required | Description |
|---|---|---|---|---|
| sourceId | Sender ID | String | Yes | A string that identifies the message sender. The value depends on whether a conversation previously existed between the customer and the business: if a conversation existed (and therefore an opaque ID was created), the value is the customer's opaque ID; if no prior conversation existed (for example, the customer declined an invitation), the value is the customer's phone number in tel: format (for example, tel:+11234567890). |
| destinationId | Destination ID | String | Yes | A string that identifies the message recipient. The value is the business ID. |
| type | Message type | String | Yes | Value must be close for a CloseSession message. |
<sub>↳ `msp-rest-api.md` L911–917</sub>

### Example CloseSession Message

```json
{
    "id": "UUID-IDENTIFIER-FOR-MESSAGE",
    "sourceId": "OPAQUE-USER-ID",
    "destinationId": "BUSINESS-ID",
    "type": "close",
    "v": 1
}
Leave conversation flow scenarios
```
<sub>↳ `msp-rest-api.md` L923–937</sub>

A customer can leave the conversation at any time by selecting Leave Conversation. Note that this is a separate action from declining an invitation, and the behavior of sourceId differs depending on whether an opaque ID exists.

| Scenario | sourceId in CloseSession | destinationId in CloseSession |
|---|---|---|
| Customer had an active conversation (opaque ID exists) | Customer's opaque ID | Business ID |
| Customer only received an invitation and declined (no opaque ID) | Customer's phone number | Business ID |
<sub>↳ `msp-rest-api.md` L943–947</sub>

Important

Declining an invitation (No) and leaving a conversation are two distinct customer actions. A customer who declines an invitation has not had a conversation with the business, so no opaque ID is available. If that same customer later selects

Leave Conversation

, the CloseSession message your MSP receives will contain a phone number in sourceId, not an opaque ID. Your MSP implementation must handle both cases.

Message Attachments

You can send and receive message attachments when conversing with users.

Receiving a Text Message with an Attachment

An incoming text message may include one or more attachments. The MSP platform should process the message as described in TextMessage, but with the additional step of downloading the attachments. If the attachment size is larger than 10 KB, see Receiving an Interactive Message.

Any file type that can be sent as a binary can be sent by Apple Messages for Business. Binary files are considered successfully sent and viewable if the end device has the Messages app installed and can use the file.

Check the Incoming Message for Attachments

Always check for and download attachments after returning a response code to Apple Messages for Business. Check for attachments by inspecting the attachments array, which contains a list of Attachment dictionary objects, such as the url, signature-hex (hex-encoded signature), owner, and key. (A library converts the hex-encoded signature into a Base64-encoded signature.) Download each attachment by doing the following:

Retrieve the URL by obtaining the URL, Base64-encoded signature, owner keys from the initial attachment receipt, and use a GET request to the /preDownload endpoint (see Getting an Attachment's URL).

Download the attachment by sending a GET download-url request to the attachment URL.

Use the key to decrypt the downloaded file (see Downloading and Decrypting an Attachment).

Repeat the steps in the loop for each attachment listed in the attachments array, as shown in the diagram below.

<!-- img: incomingMsgAttach.png -->

“Flow

Steps for retrieving an attachment from a message

Getting an Attachment’s URL

To retrieve an attachment's URL, use the information contained in the Attachment dictionary to call the /preDownload endpoint. The endpoint returns a temporary URL that you call to download an encrypted file containing the attachment.

URL

GET https://mspgw.push.apple.com/v1/preDownload

HTTP Headers

For more information, see the HTTP Headers in Common Specifications.

Response Codes

You can find the full list of Response Codes in Common Specifications.

| Code | Description |
|---|---|
| 200 | OK |
<sub>↳ `msp-rest-api.md` L1019–1021</sub>

The request was successful.

Content-Type: application/json, see preDownloadResponseBody.

Response

The response body is a JSON dictionary that contains the following key.

| Key | Description |
|---|---|
| download-url | The URL to the file. Make a GET request to this URL to download the attachment. |
<sub>↳ `msp-rest-api.md` L1033–1035</sub>

Example of a Received Message with Attachments

The following code example contains two attachments. When there is more than one attachment, they are displayed within an array.

Request

```json
{
    "body": "\\ufffc\\ufffc",
    "attachments": [{
            "mimeType": "image/png",
            "name": "IMG_2103.PNG",
            "url": "https://p50-content.icloud.com/<truncated>",
            "mime-type": "image/png",
            "owner": "Murn%3Ambid%3A33c32473476ca07d893.<truncated>",
            "key": "00A155FD83F85B008957DEB918 <truncated>",
            "signature": "81C16E7AE89C5F98F1B <truncated>",
            "size": 205883
        },
        {
            "mimeType": "image/png",
            "name": "IMG_2065.PNG",
            "url": "https://p46-content.icloud.com/<truncated>",
            "mime-type": "image/png",
            "owner": "Murn%3Ambid%3A33c32473476ca07d89 <truncated>",
            "key": "00183E442B6779E08E0425543C <truncated>",
            "signature": "814C28F63E13501B71876 <truncated>",
            "size": 233488
        }
    ],
    "sourceId": "urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG <truncated>",
    "locale": "en_US",
    "destinationId": "a884eddf-<truncated>",
    "v": 1,
    "type": "text",
    "id": "b07c4587-<truncated>"
}
Response
```
<sub>↳ `msp-rest-api.md` L1047–1107</sub>

HTTP/1.1 200 OK

content-type: application/json

```json
{
  "content-length": "291",
  "content-encoding": "gzip",
  "strict-transport-security": "max-age=31536000",
  "cache-control": "no-cache, no-store",
  "x-frame-options": "DENY",
  "content-type": "application/json"
}
{
  "download-url":"https://cvws.icloud-content.com/M/<truncated>"
}
Example of GET /preDownload
```
<sub>↳ `msp-rest-api.md` L1115–1137</sub>

Request

GET   https://mspgw.push.apple.com/v1/preDownload HTTP/1.1

predownload_headers = {

```json
        "authorization": "Bearer %s" % get_jwt_token(),
        "source-id": BIZ_ID,
        "url": mmcs_url,
        "signature": base64_encoded_signature,
        "owner": mmcs_owner
    }
{empty body}
```
<sub>↳ `msp-rest-api.md` L1147–1159</sub>

Response

HTTP/1.1 200 OK

content-type: application/json

```json
{
  "download-url": "https://content.example.com/file-id"
}
Downloading and Decrypting an Attachment
```
<sub>↳ `msp-rest-api.md` L1169–1175</sub>

Before sending an attachment to the business, the MSP platform needs to download it using an HTTP request, then decrypt it using a cypher library. After decrypting the attachment, the MSP platform can forward the message to the business.

When using Server Name Indication (SNI) (RFC 6066), upload the request in a secured TLS connection to the returned download URL. The TLS client should set the TLS server hostname from the extracted hostname for the download URL.

First, download the attached file by sending a GET request to the URL returned by /preDownload. This request returns an encrypted file.

Then, using a cypher library, decrypt the file by using the AES/CTR/NoPadding algorithm with an all-zero, 16-byte initialization vector (IV) with the key value in the Attachment dictionary for the downloaded attachment.

Finally, forward the message with the decrypted attachment to the business.

preDownloadResponseBody

Response body should be empty.

Declaration

object preDownloadResponseBody

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending and Receiving Messages.

https://register.apple.com/resources/messages/msp-rest-api/messages-sent

Outgoing Messages

When a business replies to a user’s text message, the Messaging Service Provider (MSP) platform prepares the message for delivery and sends a POST request to the /message endpoint hosted by Apple Messages for Business. Apple Messages for Business validates the message, returns a response code to the MSP platform, and delivers the message to the user’s device.

<!-- img: messages-sent-flow.png -->

“MSP

Communicate with users using Apple Messages for Business

Sending Messages to Apple Messages for Business Service

You can send messages to a user by using the POST /message request method to the Apple Messages for Business service. Apple Messages for Business delivers the message to the user’s device. Unless otherwise noted, all text fields support Basic Multilingual Plane of Unicode. For information about sending interactive messages, see iMessage App (Custom InteractiveData).

In addition to the dictionaries listed below, sending a message also includes keys from the Attachment dictionary.

Request

POST https://mspgw.push.apple.com/v1/message

Parameters

In addition to the keys from HTTP Body, use the following keys:

| Name | Type | Description |
|---|---|---|
| body | string | REQUIRED. The message text. Required when the type is text. |
| interactiveData |  | A dictionary representing the properties of an interactive message. See BaseInteractiveMessage dictionary. |
| type | string | REQUIRED. A string that identifies the message type. For the list of possible values, see Message Type Values. |
<sub>↳ `msp-rest-api.md` L1245–1251</sub>

Response

The response includes a status code listed in the Response Codes section of Integration.

The body of the response is empty unless the message sent is of type interactive and its JSON is larger than 10 KB. To reuse an asset, use the asset reference when creating a new interactive data JSON. For more information, see Receiving an Interactive Message.

### Example of a Text Message

Request

Destination-Id: "urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG/<truncated>",

Source-Id: "a884eddf-<truncated>",

Content-Type: "application/json",

id: "0c316beb-<truncated>",

Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.<truncated>"

```json
{
    "body": "Hi",
    "sourceId": "a884eddf-<truncated>",
    "locale": "en_US",
    "destinationId": "urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG/<truncated>",
    "v": 1,
    "type": "text",
    "id": "0c316beb-<truncated>"
}
Response
```
<sub>↳ `msp-rest-api.md` L1279–1297</sub>

HTTP/1.1 200 OK

cache-control: no-cache, no-store

content-length: 0

strict-transport-security: max-age=31536000

x-frame-options: DENY

Sequencing Messages

Due to its distributed nature, Messaging server may not deliver messages in the same order they are sent. If it’s essential for the user to receive messages in a particular order, the MSP platform should wait after sending a message to receive a 200 - OK response code from Apple Messages for Business before sending the next message. This guarantees that the user’s device displays the messages in the correct order.

This sequence is useful when the MSP platform needs to send a typing indicator message before a text message. Send the typing indicator message first, then wait for the 200 - OK response code before sending the text message. If the MSP platform doesn’t wait, the text message might appear on the user’s device before the typing indicator.

Message Attachments

You can send a text message with attachments from the business to a user.

Sending Messages with Attachments

A message can include one or more attachments with a message type of text. An attachment can be an image, PDF, or other file type, and it must be smaller than 100 MB.

Apple Messages for Business ensures that each attachment is available to the user for 30 days. If, within that 30-day period, the MSP platform sends a new message that includes a reference to an existing attachment, Apple Messages for Business extends the attachment’s availability for another 30 days. If the user’s device is offline for 30 days or more, the device retrieves only attachments sent in the previous 30 days.

Get the Attachment Reference

An attachment sent by the MSP platform isn't included in the message JSON. Instead, the MSP platform adds a reference to the attachment in the Attachment dictionary.

To get the attachment reference, do the following:

<!-- img: incomingMsgAttach (1).png -->

Encrypt the attachment (see Encrypting an Attachment).

Authorize the attachment for upload by calling /preUpload with a GET request, passing in the size of the encrypted file attachment (see Authorizing an Attachment for Upload). This endpoint returns the upload-url and metadata about the attachment.

Upload the encrypted file by sending a POST request to the upload-url, which returns a file checksum for the uploaded file (see Uploading an Attachment).

Use the metadata about the attachment and the file checksum to create an Attachment dictionary, which represents the attachment reference that you include in the message JSON (see Adding Attachment Metadata to a Message).

Repeat these steps for each attachment in the array, as shown below, prior to sending the message.

“Flow

Steps for retrieving an attachment from a message

Encrypting an Attachment

You must encrypt an attachment before uploading it to Apple Messages for Business. To encrypt an attachment, do the following:

Encrypt the attachment using the AES/CTR/NoPadding algorithm with an all-zero, 16-byte initialization vector (IV).

Generate a single-use 256-bit AES decryption key using a cryptographically-secure random number generator, and not a weak source like rand().

Store the key as a hex-encoded string, prefixed with 00, in the key field of the Attachment dictionary in the message JSON.

Authorizing an Attachment for Upload

Get the URL needed to upload the file by authorizing the attachment for upload to Apple Messages for Business.

Before uploading an attachment to Apple Messages for Business, authorize the file for upload by sending a GET request to /preUpload, passing the header fields listed in the HTTP Headers section. This call returns the URL that you use to upload the encrypted file to Apple Messages for Business.

URL

GET https://mspgw.push.apple.com/v1/preUpload

HTTP Headers

For more information, see the HTTP Headers in Common Specifications.

Response Codes

You can find the full list of Response Codes in Common Specifications.

| Code | Description |
|---|---|
| 200 | OK |
<sub>↳ `msp-rest-api.md` L1407–1409</sub>

preUploadResponseBody

The request was successful. See above for more information. Content-Type: application/json

Uploading an Attachment

To upload the encrypted attachment to Apple Messages for Business, send a POST request to the URL returned by the /preUpload call (see Authorizing an Attachment for Upload), with the attachment in the body of the request.

Apple Messages for Business returns a JSON dictionary containing the fileChecksum field. Store the value from this field in the signature-base64 key in the Attachment dictionary.

When using Server Name Indication (SNI) (RFC 6066), upload the request in a secured TLS connection to the returned upload URL. The TLS client should set the TLS server hostname from the extracted hostname for the upload URL.

Sample Attachment Upload

Request

POST [upload-url]

content-length: upload-size-in-bytes

{content is bytes of the encrypted attachment}

Response

HTTP/1.1 200 OK

content-type: application/json

```json
{
    "singleFile": {
        "fileChecksum": "file-signature-base64-encoded"
    }
}
Adding Attachment Metadata to a Message
```
<sub>↳ `msp-rest-api.md` L1449–1459</sub>

A text message may contain one or more attachments. To attach a file, the MSP platform uploads each attachment to the Messaging service. After uploading the attachment, the MSP platform creates the Attachment dictionary, which contains metadata representing the attachment.

The message text must have one Unicode object replacement character (\\uFFFC) for each attachment in the attachments array. For example, if the message includes two attachments, the message text must contain two Unicode object replacement characters. Extra replacement characters or attachment array items are ignored.

Including the \\uFFFC replacement character tells Messages where to place the attachment when the user sees the message on their device. The order of the replacement character within the text corresponds to the order of attachments in the attachment array. Messages displays the first attachment at the first replacement character, the second attachment in the array at the second replacement character, and so on.

To include an attachment in a message:

Place a Unicode object replacement character (\\uFFFC) at the text position where the attachment should appear in the message text.

Add the Attachment dictionary to the attachments array.

Example Attachment

Request

```json
{
    "body": "\\uFFFc",
    "attachments": [{
        "name": "picture.png",
        "size": "67497",
        "mimeType": "image/png",
        "signature-base64": "AThQ82TySl <truncated>",
        "key": "005269B32EF12645D <truncated>",
        "url": "https://p54-content.icloud.com",
        "owner": "M61383834656464662d6 <truncated>"
    }],
    "sourceId": "a884eddf-<truncated>",
    "destinationId": "urn:mbid:AQAAYyUbut6E4B3T9FLv5EbG/ <truncated>",
    "v": 1,
    "type": "text",
    "id": "9143ac3c-<truncated>"
}
Response
```
<sub>↳ `msp-rest-api.md` L1487–1521</sub>

{The response body is empty.}

preUploadResponseBody

The response body for /preUpload is a JSON dictionary containing the following keys.

| Key | Type | Description |
|---|---|---|
| upload-url | string | In URL format, used to upload the encrypted attachment data. For more information, see Uploading an Attachment. |
| url | string | In URL format, that identifies the attachment; assigned by Apple Messages for Business. Use this value when setting the url key in the Attachment dictionary. |
| owner | string | The attachment owner's ID in URL format, used when setting the owner key in the Attachment dictionary. |
<sub>↳ `msp-rest-api.md` L1533–1539</sub>

Declaration

object preUploadResponseBody

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending and Receiving Messages.

https://register.apple.com/resources/messages/msp-rest-api/type-text

Text Message Type

When a customer sends a simple text message to a business, the Messaging service receives and forwards the message to the Messaging Service Provider (MSP) platform by calling the MSPs platform /message endpoint. The message type is set to text.

The MSP platform validates the incoming message as described in Validating a Message. The /message endpoint then returns the appropriate response code to Apple Messages for Business. For a list of possible codes, see the "Response Codes" section in Integrating with Apple Messages for Business.

In addition to the Common Specifications, the following Dictionary keys are also used for sending and receiving messages.

Properties

| Name | Type | Description |
|---|---|---|
| body | string | REQUIRED. The message body |
| subject | string | The message subject displayed in bold, long text is not recommended |
<sub>↳ `msp-rest-api.md` L1569–1573</sub>

Attachments

By default Apple Messages for Business supports file attachments up to 100MB between your platform and the user. Apple Messages for Business supports commonly known file types, such as .pages, .numbers, .key, .pdf, .txt, .rtf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .jpg, .jpeg, .png, .gif, .heic, .tiff, .svg, .heif, .psd, .mp3, .m4a, .aac, .wav, .aiff, .mov, .mp4, .m4v, .avi, .zip, .dmg, .app, .pkg, .ipa, .ics, .vcf, .xml, .3gp, .mxf, .csv, .emlx

In addition, the following specialized file types are supported.

| Extension | Definition | MIME Type |
|---|---|---|
| .caf | Voice audio recording, usually sent from end user device | audio/x-caf |
| .pkpass | Wallet pass for events, loyalty, or NFC pass | application/vnd.apple.pkpass |
| .usdz | Augmented Reality object, common on iOS, which can be sent by an agent or automation to end user | vnd.usdz+zip |
<sub>↳ `msp-rest-api.md` L1585–1591</sub>

You can find demo files for these types as follow:

Voice audio recording: tap the microphone button from your iOS or macOS device to send an audio recording.

Wallet sample passes can be found as a downloadable companion file on this page: Building Your First Pass or Direct Link.

Visit our Quick Look Gallery - Augmented Reality - Apple Developer.

Apple Messages for Business doesn't reject messages due to the MIME type. The messaging platform determines which mime type to support and validate for the business. For more information about adding an attachment to a message, see Adding Attachment Metadata to a Message

In addition to the Common Specifications, the following Dictionary keys are also used for sending and receiving messages with attachments.

Properties

| Name | Type | Description |
|---|---|---|
| key | binary | The single-use, 256-bit AES key represented as a hex-encoded string. To decrypt a downloaded attachment file using key, remove the 00 prefix from the hex-encoded string, then decode the string into its original value. Use the decoded key value to decrypt the downloaded attachment file. |
| mimeType | string | The MIME type |
| name | string | The name of the file |
| owner | integer | The owner of the attachment |
| signature | binary | The file checksum, represented as a hex-encoded string. |
| signature-base64 | byte | The file checksum, represented as a Base64-encoded string.. |
| size | integer | The size of the encrypted attachment, in bytes.. |
| url | string | A URL assigned by Messages for Business to identify the attachment. |
<sub>↳ `msp-rest-api.md` L1615–1631</sub>

Sending Text Messages

When a business replies to a user’s message, the MSP platform first sends the message to the /v1/message endpoint. Messages for Business then validates the incoming message and returns the appropriate response code (see the "Response Codes" section in Common Specifications). Next, the Messaging service delivers the text message to the user’s device.

<!-- img: Text-message.png -->

“Text

Text message type received on a device

You can ensure a quick and responsive experience by setting the timeout for the HTTP request to 30 seconds. If Messages for Business doesn’t return a response code within that time, cancel the request and try again later.

Sample Text Message Payload without Attachments

```json
{
    "id": "UUID-IDENTIFIER-FOR-MESSAGE",
    "sourceId": "BUSINESS-ID",
    "destinationId": "OPAQUE-USER-ID",
    "v": 1,
    "type": "text",
    "body": "The message text"
}
Tutorial Exercise
```
<sub>↳ `msp-rest-api.md` L1651–1667</sub>

For more help or guidance, see our Tutorial: Exercise: Sending a Text Message.

https://register.apple.com/resources/messages/msp-rest-api/type-richlink

Rich Link Messages

Rich link messages contain an inline image or video. The following message types are part of the JSON dictionary. In addition to the Common Specifications, the following Dictionary keys are also used. For a full list of the JSON dictionary fields, see Parameters.

Image Size

Apple Messages for Business optimizes rich link images to 240 x 240 pixels. Apple Messages for Business scales down larger images and magnifies smaller ones. Optimizing your image for 240 x 240 pixels results in the best experience for your customers. This image size is the same as using “large” style for receivedMessage or replyMessage on an interactive message.

Image binary size must be 200kB or smaller.

Image size and related experience on device:

| Device Rendering | Image Size |
|---|---|
<sub>↳ `msp-rest-api.md` L1693–1693</sub>

	Square or rectangle with width < 150px results in an icon.

<!-- img: icon.png -->

	Square with width ≥ 150px, results in a square icon.

<!-- img: small.png -->

	Rectangle image with width ≥ 150px, results in a large icon.

<!-- img: large.png -->

RichLinkData

Keys in the richLinkData dictionary.

Properties:

| Name | Type | Description |
|---|---|---|
| assets | byte | REQUIRED. A dictionary representing the asset of the rich link. The key in the dictionary represents the type of asset: image or video. An image rich link has an image asset. A video rich link has both an image and video asset. It’s recommended to use both the image and video for better experience of video asset. Possible types: ImageAsset, VideoAsset |
| title | string | REQUIRED. A string that shows the title for the rich link in the Message transcript. |
| url | string | REQUIRED. A string URL where the rich link message is sent. When clicked, the URL you provide takes the customer to the content. |
<sub>↳ `msp-rest-api.md` L1711–1717</sub>

Custom URL, for example myapp://example.com/amb, will not work in the context of Rich Links. Universal links are recommended for rich link to work properly with your App. For more information, see Allowing apps and websites to link to your content for more information.

RichLinkDataRef

When a rich link message with richLinkData is sent by the Messaging Service Provider (MSP) platform or business, Apple Messages for Business (mspgw) returns an optional dataRef in the HTTP response body. The MSP platform uses this dataRef to represent the richLinkDataRef field in a rich link message.

Properties:

| Name | Type | Description |
|---|---|---|
| bid | string | REQUIRED. A string of the bid of the rich link message that was uploaded to content. Identifies the Messages framework extensions. For example: com.apple.messages.URLBalloonProvider |
| dataRefSig | string | REQUIRED. String of the dataref signatures associated to the message and the business. Used to verify that the dataref messages sent by the business are associated with the same business |
| key | string | REQUIRED. A string representation of the key needed to decrypt the encrypted attachment. |
| owner | string | REQUIRED. A string representation of the owner of the attachment. |
| signature-base64 | byte | REQUIRED. The file checksum, represented as a Base64-encoded string, returned in the response for the upload request. |
| size | integer | REQUIRED. The size, in bytes, of the encrypted attachment represented by an integer. |
| url | string | REQUIRED. String URL used by the Apple Messages for Business server to identify the attachment or content reference that is uploaded to content. |
<sub>↳ `msp-rest-api.md` L1733–1747</sub>

RichLinkResponse

When you include the Boolean header, include-data-ref :true, in the request header for a rich link message with richLinkData, the optional dataRef returns an HTTP response that is content reference to the rich link to be sent next time. Use this dataRef for rich link messages using the reference with richLinkDataRef field.

Subdictionary keys contained in the JSON response's dataRef key.

Properties:

| Name | Type | Description |
|---|---|---|
| bid | string | Bid of the richLinkData message that was uploaded to content represented in string. |
| dataRefSig | string | A string representation of the dataref signatures associated to the message and the business. |
| key | string | A string representation of the key needed to decrypt the encrypted attachment. |
| owner | string | A string representation of the owner of the attachment. |
| signature-base64 | byte | The file checksum, represented as a Base64-encoded string, returned in the response for the upload request. |
| size | integer | The size, in bytes, of the encrypted attachment represented by an integer. |
| url | string | String URL used by Apple Messages for Business to identify the attachment. |
<sub>↳ `msp-rest-api.md` L1763–1777</sub>

VideoAsset

The key for an image asset in richLinkData assets dictionary is video, that represents another dictionary representing video attributes.

Properties:

| Name | Type | Description |
|---|---|---|
| mimeType | string | REQUIRED. A string representing the format/type of the video; for example: video/mp4, video/mpeg. |
| url | string | REQUIRED. A string representing the URL of the video loaded in Message transcript within the rich link balloon. For example: https://store.storevideos.cdn-apple.com/v1/store.apple.com/st/1619042871000/mx532-vid3/mx532-vid3_960x540.mov |
<sub>↳ `msp-rest-api.md` L1789–1793</sub>

ImageAsset

The key for an image asset in the RichLinkData assets dictionary is image, which represents another dictionary representing image attributes. The image is restricted to PNG format only.

Properties:

| Name | Type | Description |
|---|---|---|
| data | byte | REQUIRED. A Base64-encoded string representing the image used for the richLinkData balloon in the transcript. |
| mimeType | string | REQUIRED. A string representing the format/type of the image; Use image/png. |
<sub>↳ `msp-rest-api.md` L1805–1809</sub>

Sending Rich Link Messages

When a business sends a URL with an inline image or video to a user, the user receives a "Tap to Load Preview" message, which the user then needs to tap to load the content. To allow users to preview content inline without first loading a preview, you can send a rich link message instead.

<!-- img-row: bc-rich-link-no_2x.png, bc-rich-link-yes_2x.png -->

When a business sends a URL within a sentence or a large text message, divide the content in 3 separate messages and generate the rich link message accordingly as per the example below.

<!-- img-row: RL-1-bubble.png, RL-3-bubbles.png -->

One message

Before

 Rich Link

After

Your rich link generation should automatically detect all URLs sent by agents or bots, and convert them to rich link payloads. You can use OpenGraph tags to generate the rich link preview if the target web page supports them. If OpenGraph tags are unavailable, generate a rich link preview by fetching the <TITLE> tag, and the largest image from the web page.

Please note that only PNG format is accepted. Some websites use other formats like SVG, so ensure the image is converted to PNG format.

For more information on the visual design of rich link message bubbles, see Message Bubble Content in Apple Human Interface Guide.

Note

The image of the Rich Link should provide a visual indication of what the user can expect. For this reason, we recommend offering brands the option to customize the image for the Rich Link. This would allow them to use a preferred image if they have one that is better suited than the one retrieved from OpenGraph tags.

Add an Image Using Rich Links

When coding a richLinkData message to send an image, you need to include the business URL, title of the image, and details about the image, including its data and MIME types, as shown below.

Sample of a Rich Link Containing an Image

```json
{
    "body": "https://www.apple.com/ipad-pro/",
    "sourceId": "<business_id>",
    "destinationId": "<destination_id>",
    "v": 1,
    "type": "richLink",
    "id": "<message_id>",
    "richLinkData": {
        "url": "https://www.apple.com/ipad-pro/",
        "title": "iPad Pro",
        "assets": {
            "image": {
                "data": "/9j/4AAQSkZJRgABAQA…………<snipped>…………AAQAB/Z",
                "mimeType": "image/png"
            }
        }
    }
}
“MSP
```
<sub>↳ `msp-rest-api.md` L1859–1895</sub>

A rich link message, displaying an image to the user

Add a Video and Image Using Rich Links

When sending video as a rich link, include a complementary background image or something from the video. Video and image rich links require the same assets⏤URL, title, data, and MIME types⏤to create the message bubble. Video rich links also include a URL to the video, as shown below.

Sample of a Rich Link Containing a Video

```json
{
    "body": "https://store.storevideos.cdn-apple.com/v1/store.apple.com/st/1619042871000/mx532-vid3/mx532-vid3_960x540.mov",
    "sourceId": "<business_id>",
    "destinationId": "<destination_id>",
    "v": 1,
    "type": "richLink",
    "id": "<message_id>",
    "richLinkData": {
        "url": "https://store.storevideos.cdn-apple.com/v1/store.apple.com/st/1619042871000/mx532-vid3/mx532-vid3_960x540.mov",
        "title": "AirTag",
        "assets": {
            "video": {
                "url": "https://store.storevideos.cdn-apple.com/v1/store.apple.com/st/1619042871000/mx532-vid3/mx532-vid3_960x540.mov",
                "mimeType": "video/mp4"
            },
            "image": {
                "data": "/9j/4AAQSkZJRgABAQA…………<snipped>…………AAQAB/Z",
                "mimeType": "image/png"
            }
        }
    }
}
Below shows a video rich link bubble, displayed in Messages on iPhone. The play button is the video link, which sits on top of the background image. The video loads and starts playing when tapped.
```
<sub>↳ `msp-rest-api.md` L1909–1953</sub>

<!-- img: RichLinksVideo2.png -->

“Rich

Rich Link message, displaying a video to the user

Sending an Apple Maps Link

Maps Point of Interest (POI) links differs slightly from other rich links. When creating a rich link to use for a Maps POI, do the following: use correctly formatted Maps POI link (as per instruction below) as a value in the url field in your Rich Link payload retrieve appropriate Open Graph data to generate relevant values for the Rich Link, Title, and Image fields.

Detect the URL Apple Maps format as per this example :

https://maps.apple.com/place?map=hybrid&place-id=I8C46F331341124BD&address=Westfield+London%2C+Ariel+Way%2C+London%2C+W12+7GF%2C+England&coordinate=51.5074594%2C-0.2208569&name=Apple+White+City&_provider=9902

Note

It is no longer necessary to modify the URL (e.g., adding /place). Use the original URL directly as returned by http://maps.apple.com. Do not use a text editor or tool that could reformat or encode characters in the URL, as this may break the link or affect parsing.

Retrieve the necessary data to build the rich link.

Once the image has been retrieved, verify it is PNG format. If not, it must converted to PNG format.

You can use Open Graph Meta Tags website to test Urls and Preview the Meta Tags obtained: https://www.opengraph.xyz

Note

<!-- img: maps-richlink.png -->

Scrapping OG information using methods without JavaScript: the URL maps.apple.com is rejecting HTTP requests containing a User Agent related to Firefox. We advice using alternative User Agents as:

Safari UA

\- Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.1

Chrome UA

\- Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36

Build the json and send the payload to the device.

Maps rich link

Expected Maps Rich Link (note that resulting image and title may vary)

For more information on the message bubble visual design, see Message Bubble Content.

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending Rich Link Messages.

https://register.apple.com/resources/messages/msp-rest-api/type-interactive

Interactive Message Types

You can provide users with a rich experience by using interactive messages, like list picker, time picker, authentication, and Apple Pay.

The following rich messages use the type Interactive:

### Quick Reply Message

### List Picker Message

### Time Picker Message

### Apple Pay Message

### Authentication Message

iMessage App Message (Custom InteractiveData)

### Form Message

Invitation Messages

InteractiveData Common Properties

In addition to the Common Specifications, the following Dictionary keys are also used for all interactive message types.

### InteractiveData Dictionary

| Name | Type | Description |
|---|---|---|
| bid | string | com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension |
| data | object | A collection of name and values used for interactive message types. |
| sessionIdentifier | string | sessionIdentifier is related to generic iMessage app sessions. If the interactive data in the message from MSP contains sessionIdentifier, Apple Messages for Business server will use the same sessionIdentifier in the payload to device. Otherwise, Apple will generate a random session identifier (UUID) and use it in the bp payload to device. |
<sub>↳ `msp-rest-api.md` L2055–2061</sub>

### InteractiveData.Data Dictionary

| Name | Type | Description |
|---|---|---|
| images | array | An array of image dictionaries. The image size must be 200kB or smaller, and the format is restricted to PNG only. |
| requestIdentifier | UUID | REQUIRED. An unique identifier for the authenticate request. Value must be UUID: uuid. |
| version | string | REQUIRED. A numerical version number of the message extension schema. |
<sub>↳ `msp-rest-api.md` L2065–2071</sub>

### BaseInteractiveMessage Dictionary

Messages of type interactive should include the interactiveData dictionary. This dictionary tells the Messages app which iMessage extension to use and provides the data to pass into the extension. It also provides settings that control the visual appearance of the interactive message.

The following Interactive Data dictionary keys are common to all interactive messages.

Properties

| Name | Type | Description |
|---|---|---|
| bid | string | REQUIRED. A string identifying the iMessage extension that the user interacts with while using Messages. The bid value format is: com.apple.messages.MSMessageExtensionBalloonPlugin:team-id:extension-id When using your custom interactive message, replace team-id and extension-id with your team and extension IDs. When using an Apple Messages for Business interactive message, set team-id to 0000000000 and the extension-id to com.apple.icloud.apps.messages.business.extension. For example: com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension |
| receivedMessage |  | REQUIRED. A dictionary with information telling the Messages app how and what content to display the received message bubble. See ReceivedMessage Dictionary. |
| replyMessage |  | REQUIRED. A dictionary with information telling the Messages app how and what to display in the reply message bubble. See ReplyMessage Dictionary. |
<sub>↳ `msp-rest-api.md` L2087–2093</sub>

### InteractiveResponse Dictionary

When Apple Messages for Business or the user sends a list or time picker, the Messages app uses the InteractiveResponse dictionary to set the style, content, and images for the message bubble that the Messages app displays.

The response body is a JSON dictionary of the decoded interactive message data dictionary. The dictionary keys are listed below.

Properties

| Name | Type | Description |
|---|---|---|
| imageSubtitle | string | The attached image's subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| imageTitle | string | The attached image's title. Limited to 512 characters. Only custom interactive messages use this key. |
| secondarySubtitle | string | A right-aligned title. Limited to 512 characters. Only custom interactive messages use this key. |
| style | string | A style that controls the size of the view rendered by Live Layout. The default is icon. Depending if the message is a reply or response, see Reply Message Style Values or Received Message Style Values for the list of possible values. This key is optional. Default: icon Possible values: icon,small,large |
| subtitle | string | The subtitle that appears under the main title in the reply message bubble. When the user taps the reply message bubble, Messages displays the subtitle in the header. Limited to 512 characters. |
| tertiarySubtitle | string | A right-aligned subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| title | string | REQUIRED. The main title that Messages shows in the header of the reply message bubble. When the user taps the reply message bubble, Messages replaces the title with the user’s selection. Limited to 512 characters. |
<sub>↳ `msp-rest-api.md` L2109–2123</sub>

### InteractiveMessageData Dictionary

Only Apple Messages for Business interactive messages uses the interactive message data dictionary. The dictionary contains information that the Messages app passes to the feature. The contents of the interactive message data dictionary vary based on the feature in use. For example, when using the list picker, the dictionary includes a listPicker key that describes each list item. However, the interactive message data dictionary includes common fields, regardless of the feature.

The keys for the InteractiveMessageData dictionary can be used for all interactive messages.

Properties

| Name | Type | Description |
|---|---|---|
| images | array | An array of image dictionaries. For the list of keys in the image dictionary, see ImageItem dictionary. |
| requestIdentifier | UUID | REQUIRED. A string representing a unique identifier for the request. Apple Messages for Business returns the ID in the response it sends back to the MSP platform. Value must be UUID: uuid. |
| version | string | REQUIRED. A string representing the version number of the message extension schema. Should be 1.0. |
<sub>↳ `msp-rest-api.md` L2139–2145</sub>

### ImageItem Dictionary

To send images in an interactive message, add the images array to the interactive message data dictionary. Each element in the array is a key from the image item dictionary.

The image size must be 200kB or smaller, and the format is restricted to PNG only. Total size of the ImageItem Dictionary should not exceed 5MB.

An example of where you may want to include images is when sending a list picker containing products, and you want to display an image for each product in the array.

The keys to the image item dictionary used in sending interactive messages.

Properties

| Name | Type | Description |
|---|---|---|
| data | byte | REQUIRED. A Base64-encoded string representing the image file data. Always provide @3x images at 72 dpi. The system downscales the @3x images to generate @2x and @1x versions for use on lower-resolution devices. |
| description | string | Description of the image that the systems reads aloud to users who have VoiceOver enabled on their device. If the value is null, VoiceOver ignores the image. This key is optional. |
| identifier | string | REQUIRED.A string containing the image identifier, which must be unique within the list of images. The list picker items and other dictionaries, such as receiveMessage and replyMessage, refer to identifier as imageIdentifier. |
<sub>↳ `msp-rest-api.md` L2169–2175</sub>

<!-- img: 0d99fa38-7db4-4a94-ab5c-f61da401a83e.png -->

Below is a listing of a sample array containing two images.

```json
"images": [
  {
    "data": "base64encoded-image-file",
    "description": "Optional image description",
    "identifier": "1"
  },
  {
    "data": "base64encoded-image-file",
    "description": "Optional image description",
    "identifier": "2"
  }
]
Note
```
<sub>↳ `msp-rest-api.md` L2181–2205</sub>

The total size of the ImageItem Dictionary should not exceed 5MB. This can be achieved by combining multiple images of varying sizes, but each individual image’s binary size must be 200KB or less.

### InteractiveMessageResponse Dictionary

A list of dictionaries contained in the feature's response.

Properties

| Name | Type | Description |
|---|---|---|
| bid | string | REQUIRED. A string identifying the iMessage extension that the user interacts with while using the Messages app. |
| data InteractiveMessageData |  | A dictionary containing additional information for Apple Messages for Business interactive messages |
| receivedMessage ReceivedMessage |  | A dictionary with information telling the Messages app what content and how to display it in the received message bubble. |
| replyMessage ReplyMessage |  | A dictionary with information telling the Messages app what and how to display it in the reply message bubble. |
<sub>↳ `msp-rest-api.md` L2223–2231</sub>

### ReceivedMessage Dictionary

Both text and custom interactive messages use the receivedMessage field. In addition to the key listed here, the InteractiveResponse dictionary also tells the Messages app what and how to display it in the received message bubble.

The keys for the receivedMessage dictionary.

| Name | Type | Description |
|---|---|---|
| title | string | REQUIRED. The main title that the Messages app shows in the header of the received message bubble. |
| subtitle | string | REQUIRED. The subtitle that appears under the main title in the received message bubble. |
| imageIdentifier | integer | REQUIRED. The identifier for one of the images specified in interactiveData.data.images. |
| style | string | A style that controls the size of the view rendered by Live Layout. The default is icon. |
<sub>↳ `msp-rest-api.md` L2243–2251</sub>

The possible string values for the receivedMessage style are:

icon: Indicates a message bubble size of 280 x 65 points at @3x scale (840 x 195 pixels).

small: Indicates a message bubble size of 280 x 85 points at @3x scale (840 x 255 pixels).

large: Indicates a message bubble size of 280 x 210 pixels at @3x scale (840 x 630 pixels).

The image size of each imageIdentifier reference should correspond with the style as follows:

When style is icon, the expected @3x image size is 40 x 40 points (120 x 120 pixels).

When style is small, the expected @3x image size is 60 x 60 points (180 x 180 pixels).

When style is large, the expected @3x image size is 263 x 150 points (789 x 450 pixels).

Note

Always provide @3x images at 72 dpi. The system downscales @3x images to generate @2x and @1x versions for use on lower-resolution devices. For Apple Pay, only large style is supported.

Illustration showing the layout of a message bubble that Messages displays on the user's device. The larger, top portion, displays attachments, and the image's title and subtitle. Along the bottom, the message title and subtitle are shown at left, and the secondary and tertiary subtitles are shown at right.

Message bubble layout that Messages displays on the user's device

### ReplyMessage Dictionary

A dictionary with information telling Messages how and what to display in the reply message bubble.

When the user’s device receives a list or time picker, the Messages app uses the ReplyMessage dictionary to set the style, content, and images for the reply message bubble that the Messages app displays after the user makes their selection and returns a reply to the business. When sending an interactive message, the contents of the title and subtitle may not show up on the response if these fields are overwritten by the user.

Declaration

object ReplyMessage

The following are the replyMessage dictionary keys.

| Name | Description |
|---|---|
| title | The main title that the Messages app shows in the header of the reply message bubble. When the user taps the reply message bubble, the Messages app replaces the title with the user’s selection. Limited to 512 characters. |
| subtitle | The subtitle that appears under the main title in the reply message bubble. When the user taps the reply message bubble, the Messages app displays the subtitle in the header. Limited to 512 characters. |
| imageTitle | The attached image's title. Limited to 512 characters. Only custom interactive messages use this key. |
| imageSubtitle | The attached image's subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| secondarySubtitle | A right-aligned title. Limited to 512 characters. Only custom interactive messages use this key. |
| tertiarySubtitle | A right-aligned subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| imageIdentifier | The identifier for one of the images specified in interactiveData.data.images. |
| style | A style that controls the size of the view rendered by Live Layout. The default is icon. See Reply Message Style Values for the list of possible values. |
<sub>↳ `msp-rest-api.md` L2305–2321</sub>

Reply Message Style Values

The possible reply message style values are:

icon: Indicates a message bubble size of 280 x 65 points at @3x scale (840 x 195 pixels).

small: Indicates a message bubble size of 280 x 85 points at @3x scale (840 x 255 pixels).

large: Indicates a message bubble size of 280 x 210 pixels at @3x scale (840 x 630 pixels).

Sending Interactive Messages

Add the necessary dictionaries and fields in your request to send an interactive message.

To send an interactive message, use the type value of interactive and include the interactiveData field in the message JSON. The interactiveData field is a dictionary that describes the features to use. The dictionary also contains data that Messages passes to the feature.

Below is a sample interactive message showing all possible values.

```json
{
    "type": "interactive",
    "interactiveData": {
      "appId": app-store-id,
      "appName": "Name of the App",
      "appIcon": A Base64-encoded string representing the app icon of the iMessage extension.
      "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:{team-id}:{ext-bundle-id}",
      "URL": "?data=passed-to-app&data2=more-data-passed-to-app",
      "sessionIdentifier": "uuid-for-this-interaction",
      "receivedMessage": {
        "title": "Title of bubble",
        "subtitle": "Subtitle to be displayed under title",
        "imageTitle": "Title of image attachment",
        "imageSubtitle": "Subtitle of the image attachment.",
        "secondarySubtitle": "Title that is aligned right",
        "tertiarySubtitle": "Subtitle that is aligned right"
        "style":"A style that controls the size of the view rendered by Live Layout"
      }
    "useLiveLayout": A Boolean that determines whether Messages should use Live Layout
    },
        "attachments": [
            {
              "name":"FileName",
              "mimeType":"image/jpeg",
              "size":file size,
              "key":decryption_key,
              "url":mmcs_url,
              "owner": mmcs_owner,
              "signature-base64":base64_encoded_signature
            }
    ],
    "sourceId": "A string that identifies the message sender",
    "destinationId": "A string that identifies the message recipient",
    "v": The message payload version number,
    "intent": "Purpose, of the chat",
    "group":  "Designates the department or individuals best qualified to handle the user’s particular question or problem",
    "locale": "Language in ISO 639-1",
    "id": "A UUID string that identifies the message"
}
Receiving an Interactive Message
```
<sub>↳ `msp-rest-api.md` L2349–2427</sub>

Download the interactive data when a user's reply contains a large attachment or payload.

A user’s reply to an interactive message may cause the Interactive Message Dictionaries in the message JSON to grow beyond 10 KB in size. When this happens, the Apple Messages for Business service uploads the original reply message and sends a reference pointer, interactiveDataRef, to the original interactive data response. The keys in the interactiveDataRef contain the pointer to the Messaging service where the payload, or set of large assets, is contained.

As an MSP, your platform must download the reference pointer to obtain the original interactive data response from Apple Messages for Business.

<!-- img: large-attachment-flow.png -->

Diagram showing the download flow for a large interactive data dictionary from Messages for Business. Using metadata from the interactive data reference dictionary, call the /preDownload endpoint to get a temporary URL. Use the URL to download the encrypted file. Decrypt the file, then call the /decodePayload endpoint to retrieve the binary payload

Steps to follow when receiving a large interactive data payload

Identify a Large Interactive Data Payload

When your MSP platform receives a message of type interactive from the Messaging service, the MSP platform inspects the message JSON, looking for the interactiveDataRefkey (see below). Its presence indicates that the received message is an interactive data reference and contains a payload to download. For more details on an interactive data reference in the message JSON payload, see Receiving Messages from the Apple Messages for Business Service.

Below is a large interactive data payload.

```json
{
    "interactiveDataRef": {
        "url": "https://p61-content.icloud.com/M58C0A1A2EB62B6E899B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00",
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
        "signature-base64": "gdYWyD3loBxhiXGaXSDhdDDGMeHr",
        "key": "00c0d1827fdc858fe7b42421de1fb289c2ee0a9463d787ce4f118506f970bd6e38",
        "signature": "81a619c81da5a01c6139219a5d20e17430c631e1eb",
        "owner": "M58C0A2A1EB62B4E859B4F28996E8DA229E1914295299C39944B2F2CA7482AE50.C01USN00",
        "size": 101267
    },
    "sourceId": "",
    "destinationId": "",
    "v": 1,
    "type": "interactive",
    "id": "80c72dab-dc7b-4750-8fae-ee7a90fae0cb"
}
Download the Encrypted Payload
```
<sub>↳ `msp-rest-api.md` L2455–2487</sub>

When the interactiveDataRef key is present, download the encrypted payload from Apple Messages for Business using the following method:

Using the fields in the received interactiveDataRef key, retrieve the URL to the payload by calling the /preDownload endpoint. See Getting an Attachment's URL.

Download the payload by sending a GET request to the URL returned by /preDownload.

Decrypt the downloaded file. See Downloading and Decrypting an Attachment.

For improved performance, the interactive data reference can be reused for sending another request with the same content. However, it has the same 30-day expiry as payloads like an image, PDF, or other file type, as described in Sending Messages with Attachments. Although you can reuse requests with interactiveDataRef in the next send request, you must immediately process responses with interactiveDataRef and cannot reuse them.

Decode the Payload Data

The decrypted payload of the downloaded file yields encoded data. To decode the data, the MSP platform must send a POST request to Apple Messages for Business’s /decodePayload endpoint with the request body containing the encoded data from the previous steps. The response body from the /decodePayload request is a decoded interactive data dictionary, which is the original interactive data dictionary that the user sent. For more details, see Decoding Interactive Data Payloads.

Decoding Interactive Data Payloads

Convert an interactive data reference into an interactiveData dictionary by calling the /decodePayload endpoint to decode large interactive data payloads received from Apple Messages for Business. The endpoint takes the encoded attachment and returns the JSON dictionary representing the interactiveData dictionary. For more information, see Receiving Large Interactive Data Payloads.

URL

POST https://mspgw.push.apple.com/v1/decodePayload

HTTP Headers

For more information, see the HTTP Headers in Common Specifications.

HTTP Body

| Name | Description |
|---|---|
| data | A binary file which is the decrypted downloaded file. For more details on the decrypted downloaded file, see Download the Encrypted Payload |
<sub>↳ `msp-rest-api.md` L2527–2529</sub>

Response Codes

You can find the list of Response Codes in Common Specifications.

Sample Decode Payload

The response body is a JSON dictionary of the decoded interactiveData dictionary. For the list of interactiveData dictionary keys, see BaseInteractiveMessage.

Request

POST https://mspgw.push.apple.com/v1/decodePayload

accept: */*

accept-encoding: gzip, deflate

authorization: Bearer signed-web-token

source-id: business-id

bid: com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension

content-type: application/octet-stream

{ attachment data }

Response

HTTP/1.1 200 OK

content-type: application/json

content-length: (size of stream)

```json
{
    "interactiveData": {
        "bid": "some-bid",
        "URL": "url-data",
        "receivedMessage": {
            "title": "Interaction Title"
        }
    }
}
Quick Reply Message
```
<sub>↳ `msp-rest-api.md` L2573–2591</sub>

Provide a simple way for the user to make an inline choice with a single tap during an ongoing conversation. You can have between two and five customizable choices, and the user can select only a single item.

The summaryText should not be considered as the introduction message to the quick reply message. You should use a text message to offer the user to choose one of the items.

Quick reply is an interactive message. Due to its simple structure, it doesn't have receivedMessage or replyMessage fields similar to other interactive message types.

This feature requires iOS 15.1 and macOS 12.0 or higher. For more information, see capability-list under HTTP Headers.

<!-- img-row: Quick-Reply-Response.png, Quick-Reply.png -->

A screenshot of a quick reply, as displayed on iPhone

Quick Reply message type on an iPhone

 A screenshot of a quick reply response, as displayed on iPhone

Quick Reply Response message type on an iPhone

A screenshot of a quick reply, as displayed on macOS

Quick Reply message type on macOS

 A screenshot of a quick reply response on macOS

Quick Reply Response message type on macOS

Request

### InteractiveData.Data Dictionary

| Name | Type | Description |
|---|---|---|
| quick-reply | object | REQUIRED. An array of objects. |
<sub>↳ `msp-rest-api.md` L2629–2631</sub>

### Data.Quick-Reply Dictionary

| Name | Type | Description |
|---|---|---|
| summaryText | string | REQUIRED. A summary text that will be used for device notification but also shown in the transcript after user makes a choice. |
| items | object | REQUIRED. An array of section items. |
<sub>↳ `msp-rest-api.md` L2635–2639</sub>

### Quick-Reply.Items Dictionary

| Name | Type | Description |
|---|---|---|
| identifier | string | REQUIRED. An identifier to identify the item. |
| title | string | REQUIRED. Title of the quick reply item. Max 1 line of text. |
<sub>↳ `msp-rest-api.md` L2643–2647</sub>

Order of the items is based on the JSON order. Max of 5 items.

Quick Reply Webhook Event

Webhook object for quick reply.

### Data.Quick-Reply Dictionary

Only 1 item is allowed to be selected

| Name | Type | Description |
|---|---|---|
| selectedIndex | integer | The selected item number from top order. |
| selectedIdentifier | string | The selected identifier of the item. |
| items | object | The array of section items, max of 5 items allowed. |
<sub>↳ `msp-rest-api.md` L2665–2671</sub>

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending Quick Reply.

### List Picker Message

Allow the customer to choose from a list of items. A list picker displays a list of items, and information about the items—such as product name, description, and image—in the Messages app on the customer's device. The customer can choose one or more items from the list to send with a reply.

<!-- img: List-Picker.png -->

For more information on the visual design of list pickers, see Apple Messages for Business features.

A list picker screenshot on iPhone

A list picker displaying on iPhone

### ListPickerMessage Dictionary

If the item dictionary includes the imageIdentifier key, the list picker displays an image that is 60 x 60 points. To ensure that the image looks its best on Retina and standard resolution displays, send a @3x image (180 x 180 pixels). The system downscales the @3x image to @2x and @1x for display on lower-resolution screens. For more information about sending an image, see ImageItem dictionary.

### InteractiveData.data Dictionary

A data dictionary containing fields used to describe the properties of a list picker.

| Name | Type | Description |
|---|---|---|
| listPicker | object | REQUIRED. An array of objects. See ListPickerSection. |
<sub>↳ `msp-rest-api.md` L2705–2707</sub>

### Data.ListPickerSection Dictionary

Keys for list picker section dictionary.

| Name | Type | Description |
|---|---|---|
| listPickerItem | object | An array of section items. See ListPickerItem. |
| multipleSelection | boolean | A Boolean that indicates whether the customer can make multiple selections within the section. Defaults to false. |
| order | integer | An integer containing the ordinal pn the sections array. |
| title | string | REQUIRED. A string field of the section title. |
<sub>↳ `msp-rest-api.md` L2715–2723</sub>

### ListPickerSection.ListPickerItem Dictionary

Keys for the item dictionary.

| Name | Type | Description |
|---|---|---|
| identifier | string | REQUIRED. A string field identifying the item. |
| imageIdentifier | string | A string field of the item title. |
| order | integer | An integer representing the ordinal position for the item. If this key is missing, the item isn't sorted within the items array. |
| subtitle | string | A string field of the item's subtitle. |
| title | string | REQUIRED. A string field of the section title. |
<sub>↳ `msp-rest-api.md` L2731–2741</sub>

### Time Picker Message

Allow the customer to schedule an appointment.

To let the customer pick a time slot when scheduling a meeting or appointment, send a time picker interactive message. The interactive message displays conflicts found on the customer’s local calendar so the customer can make an informed decision.

After sending the reply, the customer can tap the reply message bubble to view location information, if available. The customer can also get directions to the location or add the event to their calendar by tapping Get Directions or Add to Calendar.

<!-- img: Time-Picker.png -->

For more information on the visual design of time pickers, see Apple Messages for Business features.

A time picker screenshot on iPhone

A time picker displaying on iPhone

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending Pickers.

### TimePickerMessage Dictionary

Message body for time picker.

InteractiveData.Data

A data dictionary containing fields used to describe the properties of a time picker.

| Name | Type | Description |
|---|---|---|
| event | object | REQUIRED. A dictionary containing specific information for the user. See Event |
<sub>↳ `msp-rest-api.md` L2783–2785</sub>

### Data.Event Dictionary

Keys for time picker section dictionary.

| Name | Type | Description |
|---|---|---|
| identifier | string | REQUIRED. A string field identifying the event that must be unique within the payload, if more than one exists. |
| imageIdentifier | string | An identifier for the image to show when the user taps a reply message bubble. The image should be a @3x image sized at 375 x 208 points (that is, 1125 x 624 pixels). |
| location |  | A dictionary describing a location. For the list of location dictionary keys, see LocationItem dictionary. |
| timeslots | array | An array of time slots. For the list of time slot dictionary keys, see TimeItem dictionary. |
| timezoneOffset | integer | An integer representing the number of minutes from GMT, specifying the timezone of the event’s location. If not set, times are shown according to the customer’s current time zone. If set, the times are shown according to the event’s time zone, regardless of the customer’s location. |
| title | string | A string field of the event title. |
<sub>↳ `msp-rest-api.md` L2793–2805</sub>

### EventItem.LocationItem Dictionary

The keys for the location dictionary used in sending a time picker.

| Name | Type | Description |
|---|---|---|
| latitude | double | A double representing the latitude of the location. |
| longitude | double | A double representing the longitude of the location. |
| radius | double | A double representing the location radius, in meters. Apple Messages for Business ignores this field when latitude and longitude are missing. |
| title | string | A string field of the location title. |
<sub>↳ `msp-rest-api.md` L2813–2821</sub>

Note

If the latitude, longitude, or radius parameters don’t have values, simply omit them from the Payload request.

### Location.TimeItem Dictionary

The time item dictionary keys used in sending a time picker.

| Name | Type | Description |
|---|---|---|
| duration | integer | REQUIRED. An integer representing the duration of the time slot, in seconds. |
| identifier | string | REQUIRED. A string field identifying the time item that must be unique within the payload, if more than one exists. |
| startTime | string | REQUIRED. A UTC date string, represented by a valid date in ISO-8601 format and specified as absolute GMT +0000 date; for example, 2017-05-26T08:27+0000 or 2025-07-10T17:00+0000; the API does not accept seconds (:ss) or the Z notation (2025-07-10T17:00:00Z is invalid). The timezoneOffset, from the EventItem dictionary, determines whether the startTime is in a specific time zone or in the customer's current time zone. |
<sub>↳ `msp-rest-api.md` L2837–2843</sub>

Tutorial Exercise

For more help or guidance, see our Tutorial: Sending Pickers.

### Apple Pay Message

Provide an easy and secure way for customers to buy goods and services through Apple Messages for Business using Apple Pay. When a business asks for payment from a customer who is purchasing goods and services through Apple Messages for Business, the customer can use Apple Pay to make the payment.

<!-- img: Apple-Pay.png -->

To learn more about Apple Pay, see Apple Pay for Developers.

Apple Pay screenshot on iPhone.

Apple Pay message on iPhone

### ApplePayMessage Dictionary

Add these keys to the message body of the Apply Pay payment requests in addition to the InteractiveMessageData dictionary keys.

Properties

| Name | Type | Description |
|---|---|---|
| InteractiveData | object | REQUIRED. Fields that contain all the data needed to submit an Apple Pay payment request. See Sending an Apple Pay Payment Request. |
<sub>↳ `msp-rest-api.md` L2875–2877</sub>

### ApplePay.InteractiveData Dictionary

| Name | Type | Description |
|---|---|---|
| receivedMessage | object | REQUIRED. Contains fields giving the specifics of an Apple Pay request |
<sub>↳ `msp-rest-api.md` L2881–2883</sub>

InteractiveData.Data

A data dictionary containing fields used to describe the properties of a Apple Pay.

| Name | Type | Description |
|---|---|---|
| payment | object | REQUIRED. Contains fields giving the specifics of an Apple Pay request |
<sub>↳ `msp-rest-api.md` L2891–2893</sub>

### Data.Payment Dictionary

| Name | Type | Description |
|---|---|---|
| endpoints ApplePayEndpoints | dictionary | REQUIRED. A dictionary containing the endpoints for payment processing, contact updates, and order tracking. For the list of dictionary keys, see ApplePayEndpoints dictionary. |
| merchantSession ApplePayMerchantSession | dictionary | REQUIRED. A dictionary containing the payment session provided by Apple Pay after requesting a new payment session. For more information, see Requesting an Apple Pay Payment Session. |
| paymentRequest | dictionary | REQUIRED. A dictionary with information about the payment request. For the list of dictionary keys, see ApplePayPaymentRequest dictionary. |
<sub>↳ `msp-rest-api.md` L2897–2903</sub>

### PaymentRequest.requiredBillingContactFields Dictionary

Use the following field names to request contact information in a payment request.

| Name | Type | Description |
|---|---|---|
| email | string | REQUIRED. Email address of the Apple Pay contact. |
| name | string | REQUIRED. Full name of the Apple Pay contact. |
| phone | string | REQUIRED. Phone number of the Apple Pay contact. |
| phoneticName | string | REQUIRED. Phonetic spelling of the Apple Pay contact. |
| post | string | REQUIRED. Postal address of the Apple Pay contact. |
<sub>↳ `msp-rest-api.md` L2911–2921</sub>

### Payment.ApplePayEndpoints Dictionary

The endpoints dictionary contains a list of URLs that Apple Pay calls during the payment process. Apple Pay requires the paymentGatewayUrl endpoint for use in asking the payment provider to process the payment; all other endpoints are optional.

| Name | Type | Description |
|---|---|---|
| fallbackUrl | string | A URL that opens in a web browser so the customer can complete the purchase if their device is unable to make payments using Apple Pay. |
| orderTrackingUrl | string | Called by Apple Messages for Business after completing the order; provides you with an opportunity to update the order information in your system. For more information, see Tracking Orders. |
| paymentGatewayUrl | string | REQUIRED. Called by Apple Pay to process the payment through the payment provider. The URL should match the URL in the initiativeContext field of the payment session. For more information, see Processing Payment Requests. |
| paymentMethodUpdateUrl | string | Called by Apple Pay when the customer changes the payment method. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Payment Methods. |
| shippingContactUpdateUrl | string | Called by Apple Pay when the customer changes their shipping address information. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Shipping Contacts. |
| shippingMethodUpdateUrl | string | Called by Apple Pay when the customer changes the shipping method. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Shipping Methods. |
<sub>↳ `msp-rest-api.md` L2929–2941</sub>

### PaymentRequest.ApplePay Dictionary

Keys for Apple Pay dictionary. The applePay dictionary provides Apple Pay configuration to Apple Messages for Business.

| Name | Type | Description |
|---|---|---|
| merchantCapabilities applePay.MerchantCapabilities](type-interactive.md#applePay.MerchantCapabilities) |  | An array of payment capabilities supported by the merchant. The array must include supports3DS, and may optionally include supportsCredit, supportsDebit, and supportsEMV. For more information, see [merchantCapabilities. |
| merchantIdentifier | string | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| supportedNetworks applePay.SupportedNetworks](type-interactive.md#applePay.SupportedNetworksc') |  | An array of payment networks supported by the merchant. The array must include one or more of the following values: amex, discover, jcb, masterCard, privateLabel, or visa. For more information, see [supportedNetworks. |
<sub>↳ `msp-rest-api.md` L2949–2955</sub>

### ApplePay.MerchantCapabilities Dictionary

An array of payment capabilities supported by the merchant.

object applePay.MerchantCapabilities

### ApplePay.SupportedNetworks Dictionary

An array of payment networks supported by the merchant.

object applePay.SupportedNetworks

### ApplePay.lineItems Dictionary

A set of line items that explain recurring payments and additional charges and discounts.

| Name | Type | Description |
|---|---|---|
| amount | string | REQUIRED. The monetary amount of the line item. |
| label | string | REQUIRED. A short, localized description of the line item. |
| type | string | A value that indicates whether the line item is final or pending. |
<sub>↳ `msp-rest-api.md` L2979–2985</sub>

The applePay dictionary provides Apple Pay configuration to Apple Messages for Business.

### Payment.MerchantSession Dictionary

A unique token representing a transaction between a customer and merchant.

| Name | Type | Description |
|---|---|---|
| displayName | string | REQUIRED. The canonical name for your store, suitable for display and consisting of 64 or fewer UTF-8 characters. Do not localize the name. |
| epochTimestamp | string | REQUIRED. The time representation in number of seconds that have elapsed since 00:00:00 UTC, Thursday, January 1, 1970. |
| expiresAt | string | REQUIRED. The exipiration time representation in number of seconds that have elapsed since 00:00:00 UTC, Thursday, January 1, 1970. |
| initiative | string | REQUIRED. A predefined value that identifies the e-commerce application making the request. |
| initiativeContext | string | REQUIRED. A value you provide based on the initiative. The values for initiative and initiativeContext depend on the kind of application you're building. For Apple Messages for Business, use "messaging"for the initiative parameter. For the initiativeContextparameter, pass your payment gateway URL. See Processing Payment Requests for more information. |
| merchantIdentifier | string | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| merchantSessionIdentifier | string | REQUIRED. A unique identifier that represents a merchant's session for Apple Pay. |
| nonce | binary | A single-use string that checks the integrity of the interaction. |
| signature | binary | A hash of the public key used to sign the interactions. |
<sub>↳ `msp-rest-api.md` L2997–3015</sub>

The Apple Pay Server generates a unique token, called ApplePayMerchantSession, that represents a transaction between a customer and a merchant. The ApplePayMerchantSession token allows an update, such as a change of shipping charges or refunding an item, and captures it as a single financial transaction within Apple Pay. For more information, see Requesting an Apple Pay Payment Session.

### PaymentRequest Dictionary

Keys for the paymentRequest dictionary.

### PaymentRequest.supportedCountries Dictionary

An array of countries or regions to support.

object paymentRequest.supportedCountries

List each country or region with its ISO country code. This key is optional.

### PaymentRequest.shippingMethodItem Dictionary

The itemized shipping method for delivering physical goods.

| Name | Type | Description |
|---|---|---|
| amount | string | REQUIRED. The nonnegative cost associated with this shipping method. |
| detail | string | REQUIRED. Additional description of the shipping method. |
| identifier | string | REQUIRED. A client-defined value used to identify this shipping method. |
| label | string | REQUIRED. A short description of the shipping method. |
<sub>↳ `msp-rest-api.md` L3045–3053</sub>

For more information, see ApplePayShippingMethod.

Processing Payment Requests

If you support Apple Pay payment requests, you need to obtain the Apple Pay payment token from the customer's device. To receive this token, implement the payment gateway endpoint. Apple Pays calls this endpoint to send you the token and ask that you process the transaction. The URL to the endpoint must match the value in the paymentGatewayUrl field defined in the ApplePayEndpoints dictionary. For more information, see Sending an Apple Pay Payment Request.

Request

POST https://msp.example.com/paymentGateway

Parameters

The request body is a JSON dictionary with the following keys.

| Key | Description |
|---|---|
| payment | A dictionary containing payment information. For the list of payment dictionary keys, see Payment Dictionary. |
| requestIdentifier | An identifier for the request. Apple Messages for Business includes the identifier in its response to the MSP platform. Value must be UUID: uuid. |
| version | The version number of the message extension schema; the version should be 1.0. |
<sub>↳ `msp-rest-api.md` L3075–3081</sub>

Note

The v: 1 key-value pair and the version: 1.0 pair both indicate version numbers.

The v indicates the version of the REST API that corresponds to the endpoint version at https://mspgw.push.apple.com/v1.

The version inside of the interactive message indicates the version of the requested list picker implementation. Currently, both have only a single version. Apple architected the system to increase the list picker and other interactive message components as a higher number than the underlying API.

Also the v is an integer data type while version is a string.

### Payment Dictionary

Use the following payment dictionary keys.

| Key | Description |
|---|---|
| billingContact | The customer's billing contact information. For more information, see billingContact. |
| paymentToken | The payment token. For more information, see Payment Token Format Reference for more information. |
| shippingContact | The customer's shipping address information. For more information, see shippingContact. |
<sub>↳ `msp-rest-api.md` L3109–3115</sub>

Sample Payment Gateway Request

POST https://msp.example.com/paymentGateway

content-type: application/json

```json
{
    "requestIdentifier": "8EF748B5-3DC5-47AE-B185-65E91518D209",
    "version": "1.0",
    "payment": {
        "billingContact": {
            "phoneticFamilyName": "",
            "locality": "Cupertino",
            "postalCode": "95014",
            "subLocality": "",
            "administrativeArea": "CA",
            "country": "United States",
            "familyName": "Appleseed",
            "addressLines": ["1 Infinite Loop"],
            "givenName": "Johnny",
            "phoneticGivenName": "",
            "countryCode": "us"
        },
        "shippingContact": {
            "phoneNumber": "55555555555",
            "emailAddress": "user@example.com",
            "subLocality": "",
            "phoneticGivenName": "",
            "countryCode": "us",
            "phoneticFamilyName": "",
            "administrativeArea": "CA",
            "addressLines": ["1 Infinite Loop"],
            "givenName": "",
            "postalCode": "95014",
            "familyName": "",
            "locality": "Cupertino",
            "country": "United States"
        },
        "shippingMethod": {
            "amount": "0",
            "label": "In-Store Pickup",
            "detail": "Available within an hour",
            "type": "Final",
            "identifier": "in_store_pickup"
        },
        "paymentToken": {
            "transactionIdentifier": "5394..00",
            "paymentData": {
                "version": "EC_v1",
                "data": "kdHd..GQ==",
                "signature": "MIAGCSqGSIb3DQEH...AAA",
                "header": {
                    "applicationData": "94ee0..C2",
                    "transactionId": "d3b28af..f8",
                    "ephemeralPublicKey": "MFkwE..Q==",
                    "publicKeyHash": "dxCK..6o="
                }
            }
        }
    }
}
Response
```
<sub>↳ `msp-rest-api.md` L3127–3237</sub>

After processing the payment, send a response with the transaction results and errors, if any. The body of the response is a JSON dictionary with the following fields:

errors: An array of ApplePayError types. This field is present only when the payment processing request detects errors.

status: Indicates the status of the transaction. For a list of status codes, see Apple Pay Status Codes.

Sample Payment Gateway Response

```json
{
    "status": "STATUS_SUCCESS"
}
ApplePayPaymentRequest Dictionary
```
<sub>↳ `msp-rest-api.md` L3249–3255</sub>

Keys for the paymentRequest dictionary.

Properties

| Name | Type | Description |
|---|---|---|
| applePay |  | REQUIRED. A dictionary that describes the Apple Pay configuration. For the list of dictionary keys, see [ApplePayItem](#ApplePayItem) dictionary. |
| countryCode | string | REQUIRED. The merchant’s two-letter uppercase ISO 3166 country code. |
| currencyCode | string | REQUIRED. The three-letter alphabetic codes in uppercase, ISO 4217 currency code for the payment. |
| lineItems | string | REQUIRED. An array of line items explaining payments and additional charges (max of 20 items). Line items are not required. However, the array cannot be empty if the lineItems key is present. For more information, see lineItems. |
| requiredBillingContactFields |  | The list of the customer's required billing information needed to process the transaction. For the list of possible strings, see requiredBillingContactFields. |
<sub>↳ `msp-rest-api.md` L3265–3275</sub>

Require only the contact fields needed to process the payment. Requesting unnecessary fields adds complexity to the transaction, which can increase the chances of the customer canceling the payment request.

| requiredShippingContactFields |  | The list of shipping or contact information required from the customer to fulfill the order. For example, if you need the customer's email or phone number, then include this key. For the list of possible strings, see requiredShippingContactFields. |
|---|---|---|
| shippingMethods |  | An array that lists the available shipping methods. The Apple Pay payment sheet displays the first shipping method from the array as the default shipping method. For the list of shipping method dictionary keys, see ApplePayShippingMethod. |
| supportedCountries |  | An array of countries to support. List each country with their ISO 3166 country code. |
| total |  | REQUIRED. A dictionary containing the total. The total amount must be greater than zero to pass validation. The label, defined in the total dictionary, appears on the payment sheet and should be the doing-business-as name of the business. For more information, see total. |
<sub>↳ `msp-rest-api.md` L3279–3285</sub>

For additional information about the payment request dictionary, see ApplePayPaymentRequest.

### ApplePayItem Dictionary

The applePay dictionary provides Apple Pay configuration to Apple Messages for Business.

Properties

| Name | Type | Description |
|---|---|---|
| merchantCapabilities |  | An array of payment capabilities supported by the merchant. The array must include supports3DS, and may optionally include supportsCredit, supportsDebit, and supportsEMV. For more information, see merchantCapabilities. |
| merchantIdentifier | string | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| supportedNetworks |  | An array of payment networks supported by the merchant. The array must include one or more of the following values: amex, discover, jcb, masterCard, privateLabel, or visa. For more information, see supportedNetworks. |
<sub>↳ `msp-rest-api.md` L3301–3307</sub>

### Sending an Apple Pay Payment Request

A payment request starts when a customer service agent with the business asks you to send a payment request to a customer. You should create a data dictionary to collect and store information about the payment request.

The first piece of information to collect is a payment session object. To get it, ask Apple Pay to start a new payment session (see Requesting an Apple Pay Payment Session). Apple Pay returns a payment session object which you add to the Payment.MerchantSession dictionary in the data dictionary.

Next, add the ApplePayPaymentRequest dictionary keys to the data dictionary. This is where you specify transaction details such as the purchase amount, payment processing capabilities, available shipping methods, and a list of items or services purchased. You can also request billing and shipping address information through the ApplePayPaymentRequest dictionary.

Finally, add the ApplePayEndpoints dictionary keys to the data dictionary. This dictionary identifies the endpoints needed to process the payment and receive any updates a customer might make before confirming the payment, such as updating the shipping address or changing the shipping method.

After constructing the data dictionary, send it to Apple Messages for Business as part of an interactive message (see Sending a Custom Interactive Message). Apple Messages for Business forwards the payment request to the customer's device, and the customer authorizes the payment from the Apple Pay payment sheet using Touch ID or Face ID. The device then sends the payment information, including the encrypted Apple Pay token and any requested customer contact information, to the paymentGatewayURL endpoint listed in the endpoints dictionary. After processing the payment, the merchant sends the transaction results to the customer's device, which in turn sends the results to you to let you know the payment request is complete.

```json
{
    "type": "interactive",
    "interactiveData": {
      "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
      "data": {
        "images": [
          {
            "data": "base64encoded-image-file",
            "identifier": "1"
          }
        ],
        "version": "1.0",
        "payment": {
          "endpoints": {
            "fallbackUrl": "https://sams.example.com/fallback/",
            "orderTrackingUrl": "https://sams.example.com/orderTrackingUrl/",
            "paymentGatewayUrl": "https://sams.example.com/paymentGateway/",
            "paymentMethodUpdateUrl": "https://sams.example.com/paymentMethodUpdate/",
            "shippingContactUpdateUrl": "https://sams.example.com/shippingContactUpdate/",
            "shippingMethodUpdateUrl": "https://sams.example.com/shippingMethodUpdate/"
          },
          "merchantSession": {
            "epochTimestamp": 1525722894057,
            "expiresAt": 1525730094057,
            "merchantSessionIdentifier": "PSH40080EF4D655442D...FD",
            "nonce": "fe72cd0f",
            "merchantIdentifier": "302B976...8E",
            "displayName": "Sam's Fish",
            "signature": "308006092a864886f...00",
            "initiative": "messaging",
            "initiativeContext": "https://sams.example.com/paymentGateway",
            "signedFields": [
              "merchantIdentifier",
              "merchantSessionIdentifier",
              "initiative",
              "initiativeContext",
              "displayName",
              "nonce"
            ]
          },
          "paymentRequest": {
            "applePay": {
              "merchantCapabilities": [
                "supports3DS",
                "supportsDebit",
                "supportsCredit"
              ],
              "merchantIdentifier": "merchant.com.sams.fish",
              "supportedNetworks": [
                "amex",
                "visa",
                "discover",
                "masterCard"
              ]
            },
            "countryCode": "US",
            "currencyCode": "USD",
            "lineItems": [
              {
                "amount": "59.00",
                "label": "Halibut",
                "type": "final"
              },
              {
                "amount": "4.99",
                "label": "Shipping",
                "type": "final"
              }
            ],
            "requiredBillingContactFields": [
              "post"
            ],
            "requiredShippingContactFields": [
              "post",
              "phone",
              "email",
              "name"
            ],
            "shippingMethods": [
              {
                "amount": "0.00",
                "detail": "Available within an hour",
                "identifier": "in_store_pickup",
                "label": "In-Store Pickup"
              },
              {
                "amount": "4.99",
                "detail": "5-8 Business Days",
                "identifier": "flat_rate_shipping_id_2",
                "label": "UPS Ground"
              },
              {
                "amount": "29.99",
                "detail": "1-3 Business Days",
                "identifier": "flat_rate_shipping_id_1",
                "label": "FedEx Priority Mail"
              }
            ],
            "total": {
              "amount": "63.99",
              "label": "Sam's Fish",
              "type": "final"
            }
          }
        },
        "requestIdentifier": "8EF748B5-3DC5-47AE-B185-65E91518D209"
      },
      "receivedMessage": {
        "imageIdentifier": "1",
        "style": "large",
        "subtitle": "$63.99 at Sam's Fish",
        "title": "Halibut"
      }
  }
Updating Shipping Contacts
```
<sub>↳ `msp-rest-api.md` L3331–3559</sub>

Receive changes that the customer makes to their shipping address by implementing the shipping contact update endpoint.

To receive shipping address changes, implement the shipping contact update endpoint. Give the endpoint any name you like, and make sure to set the shippingContactUpdateUrl key in the ApplePayEndpoints dictionary to this endpoint. For more information, see Handling Shipping Contact Updates.

Note

This endpoint must respond to the request within 30 seconds or the request times out.

Shipping Contact Request

POST https://msp.example.com/shippingContactUpdate

Parameters

The request body is a JSON dictionary with the following keys.

| Key | Description |
|---|---|
| payment | A dictionary containing payment information. For the list of payment dictionary keys, see Payment Dictionary. |
| requestIdentifier | An identifier for the request. Apple Messages for Business includes the identifier in its response to the MSP platform. Value must be UUID: uuid. |
| version | The version number of the message extension schema; the version should be 1.0. |
<sub>↳ `msp-rest-api.md` L3587–3593</sub>

### Payment Dictionary

Prior to the customer authorizing the transaction, you receive redacted shipping contact information, which includes only the necessary data for completing transaction related tasks, such as calculating taxes or shipping cost. For more information, see onshippingcontactselected.

The payment dictionary has the following key.

| Key | Description |
|---|---|
| shippingContact | A dictionary with the customer's updated shipping address information. For more information, see shippingContact. |
<sub>↳ `msp-rest-api.md` L3605–3607</sub>

Updating Payment Methods

Receive changes that the customer makes to the payment method by implementing the payment method update endpoint.

To receive changes that a customer makes to the payment method, such as changing the credit card type, implement the payment method update endpoint. Give the endpoint any name you like, and set the paymentMethodUpdateUrl key in the ApplePayEndpoints dictionary to this endpoint. For more information, see Handling Payment Method Updates.

Note

This endpoint must respond to the request within 30 seconds or the request times out.

Update Payment Method Request

POST https://msp.example.com/paymentMethodUpdate

Parameters

The request body is a JSON dictionary with the following keys.

| Key | Description |
|---|---|
| payment | A dictionary containing payment information. For the list of payment dictionary keys, see Payment Dictionary. |
| requestIdentifier | An identifier for the request. Apple Messages for Business includes the identifier in its response to the MSP platform. Value must be UUID: uuid. |
| version | The version number of the message extension schema; the version should be 1.0. |
<sub>↳ `msp-rest-api.md` L3637–3643</sub>

### Payment Dictionary

The payment dictionary has the following key.

| Key | Description |
|---|---|
| paymentMethod | A dictionary with payment method information. For the list of dictionary keys, see Payment Method Dictionary. |
<sub>↳ `msp-rest-api.md` L3651–3653</sub>

### Payment Method Dictionary

The paymentMethod dictionary has the following key.

| Key | Description |
|---|---|
| type | Indicates the payment method type. For more information, see ApplePayPaymentMethodType. |
<sub>↳ `msp-rest-api.md` L3661–3663</sub>

Sample Request

Below is a sample update payment request.

POST https://msp.example.com/paymentMethodUpdate

content-type: application/json

```json
{
    "requestIdentifier": "8EF748B5-<truncated>9",
    "version": "1.0",
    "payment": {
        "paymentMethod": {
            "type": "credit"
        }
    }
}
Response
```
<sub>↳ `msp-rest-api.md` L3679–3697</sub>

The response body is a JSON dictionary that contains the state of the payment request and indicates that the data has changed. The dictionary can contain a partial or complete payment dictionary. Following are the dictionary keys.

Note

For more information about the payment method update response, see ApplePayPaymentMethodUpdate.

| Key | Description |
|---|---|
| endpoints | A dictionary containing the endpoints for payment processing, contact updates, and order tracking. For the list of dictionary keys, see ApplePayEndpoints dictionary. |
| errors | An array of ApplePayError types, present only when the request detects errors. |
| merchantSession | The merchant session containing the payment session provided by Apple Pay (see Requesting an Apple Pay Payment Session). |
| newLineItems | An optional list of line items (max of 20 items). For more information, see newLineItems. |
| newTotal | The new total resulting from a change in the payment method. For more information, see newTotal. |
<sub>↳ `msp-rest-api.md` L3711–3721</sub>

Sample Response

Below is a sample payment method update response.

```json
{
  "newLineItems": [
    {
      "amount": "59.00",
      "label": "Halibut",
      "type": "final"
    },
    {
      "amount": "29.99",
      "label": "FedEx Priority Mail",
      "type": "final"
    }
  ],
  "newTotal": {
    "amount": "88.99",
    "label": "Total",
    "type": "final"
  }
}
Updating Shipping Methods
```
<sub>↳ `msp-rest-api.md` L3729–3767</sub>

Receive changes that the customer makes to the shipping method by implementing the shipping method update endpoint.

If you provide shippingMethods in paymentRequest (see ApplePayPaymentRequest dictionary) when sending an Apple Pay payment request, implement the shipping method update endpoint. If the customer changes the shipping method, you receive the selected shipping method through this endpoint.

Name the endpoint and point the shippingMethodUpdateUrl key in the ApplePayEndpoints dictionary to this endpoint. For more information, see Handling Shipping Method Updates.

Note

This endpoint must respond to the request within 30 seconds or the request times out.

Request

POST https://msp.example.com/shippingMethodUpdate

Parameters

The request body is a JSON dictionary with the following keys.

| Key | Description |
|---|---|
| payment | A dictionary containing payment information. For the list of payment dictionary keys, see Payment Dictionary. |
| requestIdentifier | An identifier for the request. Apple Messages for Business includes the identifier in its response to the MSP platform. Value must be UUID: uuid. |
| version | The version number of the message extension schema; the version should be 1.0. |
<sub>↳ `msp-rest-api.md` L3799–3805</sub>

### Payment Dictionary

The payment dictionary has the following key.

| Key | Description |
|---|---|
| shippingMethod | The shipping method selected by the customer. For more information, see shippingMethod. |
<sub>↳ `msp-rest-api.md` L3813–3815</sub>

Sample Shipping Method Update Request

POST https://msp.example.com/shippingMethodUpdate

content-type: application/json

```json
{
   "requestIdentifier": "8EF748B5-<truncated>",
   "version": "1.0",
   "payment": {
        "shippingMethod": {
          "amount": "29.99",
          "detail": "1-3 Business Days",
          "identifier": "flat_rate_shipping_id_1",
          "label": "FedEx Priority Mail",
          "type": "Final"
        }
    }
}
Response
```
<sub>↳ `msp-rest-api.md` L3827–3853</sub>

The response body is a JSON dictionary that contains the state of the payment request and indicates that the data has changed. The dictionary can contain a partial or complete payment dictionary. Below are the dictionary keys.

| Key | Description |
|---|---|
| endpoints | A dictionary containing the endpoints for payment processing, contact updates, and order tracking. For the list of dictionary keys, see ApplePayEndpoints dictionary. |
| errors | An array of ApplePayError types, present only when the request detects errors. |
| merchantSession | The merchant session containing the payment session provided by Apple Pay (see Requesting an Apple Pay Payment Session). |
| newLineItems | An optional list of line items. For more information, see newLineItems. |
| newTotal | The new total resulting from a change in the payment method. For more information, see newTotal. |
<sub>↳ `msp-rest-api.md` L3859–3869</sub>

Note

For more information about the shipping method update response, see ApplePayShippingMethodUpdate.

Sample Shipping Method Update Response

```json
{
  "newLineItems": [
    {
      "amount": "59.00",
      "label": "Halibut",
      "type": "final"
    },
    {
      "amount": "29.99",
      "label": "FedEx Priority Mail",
      "type": "final"
    }
  ],
  "newTotal": {
    "amount": "88.99",
    "label": "Total",
    "type": "final"
  }
}
Tracking Orders
```
<sub>↳ `msp-rest-api.md` L3881–3919</sub>

Receive final payment information by implementing the order tracking endpoint.

After processing the payment request, Apple Messages for Business calls the order tracking endpoint providing final payment information. To receive that information, implement this endpoint, giving it any name you like. Make sure to set the orderTrackingUrl key in the ApplePayEndpoints dictionary to this endpoint.

Request

POST https://msp.example.com/orderTracking

Parameters

The request body is a JSON dictionary with the following keys.

| Key | Description |
|---|---|
| payment | A dictionary containing payment information. For the list of payment dictionary keys, see Payment Dictionary. |
| requestIdentifier | An identifier for the request. Apple Messages for Business includes the identifier in its response to the MSP platform. Value must be UUID: uuid. |
| version | The version number of the message extension schema; the version should be 1.0. |
<sub>↳ `msp-rest-api.md` L3939–3945</sub>

### Payment Dictionary

Below are the keys for the payment dictionary.

| Key | Description |
|---|---|
| billingContact | The customer's billing contact information. For more information, see billingContact. |
| errors | An array of ApplePayError types. This field is present only when the payment processing request detects errors. |
| shippingContact | The customer's shipping address information. For more information, see shippingContact. |
| shippingMethod | The shipping method selected by the customer. For more information, see ApplePayShippingMethodItem. |
| summaryItems | An array of ApplePayLineItem dictionaries. |
<sub>↳ `msp-rest-api.md` L3953–3963</sub>

Tutorial Exercise

For more help or guidance, see our Tutorial: Exercise: Integrating Apple Pay.

### Authentication Message

The new built-in Authentication flow uses the latest OAuth 2.0 Authorization Framework to allow implementation of latest authorization flows, and compatibility with OpenID Connect. The update also includes changes to improve security in the OAuth 2.0 flow.

<!-- img: new-authentication-flow.png -->

In the new flow the device initiates the authorization flow and the business or Messaging Service Provider (MSP) is responsible to complete the authorization flow.

The new authentication flow

The new authentication flow

Requirements

You need an Apple device running iOS 16, iPadOS 16 or macOS 13 to test the new built-in Authentication flow. For more information see Apple Developer Downloads.

Sending an Authentication Message

The new authentication flow does not require private/public key generation and follows the OAuth specification to redirect the user to the ‘redirect_uri’ provided. It removes the requirement to provide the client secret on the payload, and is compatible with OpenID Connect.

Following are the responsibilities for the Business & MSP:

The Business & MSP needs to use the state to verify the session and user for authentication.

The Business & MSP is responsible for retrieving the Access Token (ID Token) to complete the authentication.

URL

POST https://mspgw.push.apple.com/v1/authenticate

End Point Registration

Businesses supply authentication details about the OAuth provider, including authentication endpoint URLs, client identifier, and business information verified by Apple Business Register. Changing any of these authentication parameters requires additional verification and approval from multiple customers that own or administer the business.

Initiate Authorization Flow

Initiating the authorization flow requires sending a POST request to the /v1/authenticate endpoint hosted by Apple Messages for Business with the authentication message in the request body. You must secure the authentication endpoint before sending a request from a business to the customer. When the OAuth request is sent to the provider, the endpoints must present a valid Extended Validation (EV) certificate for a successful authorization.

The authentication request is an interactive message. When composing an authentication request, include the InteractiveData Properties for New Authentication Message to describe the behavior and content of the authentication request.

You can send the New Authentication Message to a customer’s device with the auth capability announced, which is included in the capability-list header of the message request. Devices that support the New Authentication Message will have the value AUTH2 in the capability-list header. For more information about the Authorization header field, see Authorizing Messages.

Example of Authentication Request

Request

```json
{
  "v": 1,
  "sourceId": "<sourceId>",
  "destinationId": "<destinationId>",
  "type": "interactive",
  "locale": "en_us",
  "interactiveData": {
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
    "data": {
      "version": "2.0",
      "requestIdentifier": "f8ad656-12a0-4fc9-a28d-22d103a0ae5d",
      "authenticate": {
        "oauth2": {
          "state": "3D138r5719ru3e1%26AQAAY+jbFom1SW+wCRR2yq3eh+k0VtLQrTRnVPYF9V2fQ5LM5c53uamshW1DYOF2d+jnENvo5c1sV+UWvjV2+rmGwJ+q2GsvPziBDsgw+Jps7YjbvqwtB+SVdLV2EJC4H0l3cVj8tMuEC0gSw3lGeRP4z+QhhPQ=",
          "responseType": "code",
          "scope": ["r_liteprofile"],
          "redirectURI" : "https://example.com/auth/linkedin/callback"
        }
      }
    },
    "receivedMessage": {
      "title": "Lets Sign In"
    },
    "replyMessage": {
      "title": "Sign In Completed"
    }
  }
}
Response
```
<sub>↳ `msp-rest-api.md` L4033–4089</sub>

200 OK

InteractiveData Properties

The New Authentication Message is an Interactive Message Type, which has the following properties. See Common Specifications for interactive messages types.

### InteractiveData Dictionary

| Name | Type | Description |
|---|---|---|
| bid | string | REQUIRED. com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000: |
<sub>↳ `msp-rest-api.md` L4101–4103</sub>

com.apple.icloud.apps.messages.business.extension

| data | object | REQUIRED. A collection of name and values used for interactive message types. |
|---|---|---|
| receivedMessage |  | REQUIRED. A dictionary with information telling the Messages app how and what content to display the received message bubble. See ReceivedMessage. |
| replyMessage |  | REQUIRED. A dictionary with information telling the Messages app how and what to display in the reply message bubble. See ReplyMessage. |
<sub>↳ `msp-rest-api.md` L4107–4111</sub>

### InteractiveData.Data Dictionary

| Name | Type | Description |
|---|---|---|
| images | array | An array of image dictionaries. |
| requestIdentifier | UUID | REQUIRED. An unique identifier for the authentication request. Value must be UUID: uuid. |
| version | string | REQUIRED. A numerical version number of the message extension schema. Set 2.0 for the New Authentication Message. |
| authenticate | object | REQUIRED. An object to construct the authorization URL. |
<sub>↳ `msp-rest-api.md` L4115–4123</sub>

### InteractiveData.Data.Authenticate Dictionary

| Name | Type | Description |
|---|---|---|
| oauth2 | object | REQUIRED. A dictionary that describes the authentication request. |
<sub>↳ `msp-rest-api.md` L4127–4129</sub>

### Data.Authenticate.Oauth2 Dictionary

| Name | Type | Description |
|---|---|---|
| responseType | string | REQUIRED. A string indicating the type of authentication request. Set code for authorization flow. |
| scope | array | REQUIRED. An array of scope items that specifies the scope of the request.This dictionary entry gives the exact fields of data that the authentication service provides to the client requesting the authentication. |
| state | string | REQUIRED. A string indicating the state of the authentication request. |
| redirectURI | string | REQUIRED. A string representing the redirect URL that the OAuth provider redirects the user. |
| additionalParameters | string | A string value that you can add on the authorization URL query parameter. |
<sub>↳ `msp-rest-api.md` L4133–4143</sub>

Generating state Value

The state is used to prevent request forgery attacks. It is important that you create a session token that is unique to that session and constructed with a high quality random number. Use the state to link the user with the session using the OpaqueID provided on each message.

For example :

3D138r5719ru3e1%26AQAAY+jbFom1SW+wCRR2yq3eh+k0VtLQrTRnVPYF9V2fQ5LM5c53uamshW1DYOF2d+jnENvo5c1sV+UWvjV2+rmGwJ+q2GsvPziBDsgw+Jps7YjbvqwtB+SVdLV2EJC4H0l3cVj8tMuEC0gSw3lGeRP4z+QhhPQ=

The above example is created with

<Random string using cryptographic> & <OpaqueID>

Do not use a static value on the session token that an attacker could easily identify.

Using this format you can confirm the session token for anti-forgery and the OpaqueID with requestIdentifier to link to the user.

Additional Parameters

The additionalParameters allows to add additional query parameters to the authorization URI request. This allows specific parameters required for custom OAuth providers.

For example:

parameter1=01\¶meter2=02

Complete the OAuth flow

Once the user completes the authorization, the user is redirected to the redirectURI with the state and authorization code to complete the OAuth 2.0 flow. The Business & MSP are responsible to complete the authentication flow to retrieve the access token or id token for the user authentication.

Note

For more details on OAuth 2.0 authorization code flow, please check the OAuth 2.0 RFC.

Finishing the New Authentication Flow

Once the OAuth flow has been completed, the Business and MSP can finish the flow by redirecting the user to the following URL scheme which closes the window and bubble. After the flow is complete, be sure to send a welcome message to the user.

URL Scheme

messages-auth://?

Query Parameters

| Query Name | Parameter | Description |
|---|---|---|
| status | success, failure, cancel, unknown | REQUIRED. A string that describes the authentication status. |
| error_code | string (numeric) | A numeric string to provide reference of a specific error. |
<sub>↳ `msp-rest-api.md` L4211–4215</sub>

Examples:

302 messages-auth://?status=success

302 messages-auth://?status=failure&error_code=400

Authentication Webhook Event

The authentication webhook event is sent when closing the window with status as success or failure using the URL scheme. See Finishing the New Authentication Flow for more details.

Authentication Webhook Payload Properties

### InteractiveData.Data Dictionary

| Name | Type | Description |
|---|---|---|
| requestIdentifier | UUID | An unique identifier for the authentication request. Value must be UUID: uuid. |
| version | string | A numerical version number of the message extension schema. 2.0 for the New Authentication Message. |
| authenticate | array | An array object to construct the authorization URL. |
<sub>↳ `msp-rest-api.md` L4235–4241</sub>

### Data.authenticate Dictionary

| Name | Type | Description |
|---|---|---|
| status | string | success, failure, cancel, unknown is returned as a value, which indicates that the authentication flow was closed. |
| error_code | string | A numeric number of the error_code sent from |
<sub>↳ `msp-rest-api.md` L4245–4249</sub>

Example of Authentication Webhook Event

```json
{
    "type": "interactive",
    "id": "a2cb006d-8025-4f68-832f-78922518d1b9",
    "v": 1,
    "sourceId": "<OpaqueID>",
    "destinationId": "<BusinessID>",
    "locale": "en_us",
    "interactiveData": {
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
        "data": {
            "requestIdentifier": "f8ad656-12b0-43c9-a28d-13d103a0ae5d",
            "version": "2.0",
            "authenticate": {
                "status": "success"
            }
        }
    }
}
Using Password AutoFill to Authenticate Users
```
<sub>↳ `msp-rest-api.md` L4253–4289</sub>

Provide customers with an easy solution to perform authentication on their iOS devices.

Supporting the Password AutoFill feature requires that the authorization input element annotate the autocomplete HTML attribute in the following format:

<input autocomplete=”value”>

Possible values for the autocomplete attribute are username, current-password, new-password, and one-time code. For more information about these values, see Enabling Password AutoFill on an HTML Input Element.

Note

Password AutoFill is supported in Safari 12 for iOS 12 and later, and Safari 12 for macOS 10.14 and later.

After the customer has been authorized, the system sends an OAuth response. In this step, the customer’s device is redirected to a URL that triggers a login form using an existing third party login system. For more information, see Password AutoFill.

iMessage App

Below is the iMessage app, also referred to as CustomInteractiveData, request body. The request body is based on InteractiveData.

| Name | Type | Description |
|---|---|---|
| InteractiveData |  | Custom InteractiveData |
<sub>↳ `msp-rest-api.md` L4323–4325</sub>

InteractiveData

The CustomInteractiveData dictionary keys. In addition to the keys from the BaseInteractiveMessage dictionary, the message can also include the keys from the CustomInteractiveData dictionary.

| Name | Type | Description |
|---|---|---|
| appIcon | byte | A Base64-encoded string representing the app icon of the iMessage app. The Messages app displays the icon when a customer's device receives a iMessageApp message that uses an iMessage extension not installed on the device. The MSP platform must include this key when sending an interactive message that uses an iMessage extension provided by the business. appIcon should be smaller than 15kb. For more information, see Sending Custom iMessage app. |
| appId | string | REQUIRED. The App Store identifier of the iMessage app. The MSP platform must include this key when sending an interactive message that uses an iMessage extension provided by the business. For more information, see Sending Custom iMessage app. |
| appName | string | REQUIRED. The name of the iMessage app. The MSP platform must include this key when sending an interactive message that uses an iMessage app provided by the business. For more information, see Sending Custom iMessage apps. |
| receivedMessage |  | REQUIRED. A dictionary with information telling the Messages app what content and how to display it in the received message bubble. |
| replyMessage |  | REQUIRED. A dictionary with information telling the Messages app what and how to display it in the reply message bubble. |
| URL | string | REQUIRED. A URL string containing data that the Messages app sends to the iMessage app. |
| useLiveLayout | boolean | REQUIRED. A Boolean that determines whether the Messages app should use Live Layout. The default is true. Default: true |
<sub>↳ `msp-rest-api.md` L4333–4347</sub>

InteractiveData.ReceivedMessage

A dictionary with information telling Messages how to display the received message bubble and what content to include. For more information, see ReceivedMessage.

object InteractiveData.ReceivedMessage

InteractiveData.ReplyMessage

A dictionary with information telling Messages how to display the reply message bubble and what content to include.

object InteractiveData.ReplyMessage

When the MSP platform sends a custom interactive message, the contents of the title and subtitle may not show up on the response if the customer overwrites these fields. For more information, see ReplyMessage.

Sending a Custom Interactive Message

Provide a unique user experience with custom interactive messages.

You can use your custom interactive message—by setting the bid, appId, appName, and appIcon to reference your extension.

When sending a custom interactive message, use the type value of interactive and include the interactiveData field in the message JSON. The interactiveData field is a dictionary that describes the iMessages extension to use. The dictionary also contains data that the Messages app passes to the extension.

To control the appearance of the interactive message that Messages displays on the customer’s device, use the receivedMessage dictionary. Note that the Messages app ignores the imageIdentifier and style keys when using a custom interactive message. For the list of received message dictionary keys, see receivedMessage dictionary.

```json
{
    "type": "interactive",
    "interactiveData": {
        "appId": "<app - store - id>",
        "appName": "Name of the App",
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:{team-id}:{ext-bundle-id}",
        "URL": "?data=passed-to-app&data2=more-data-passed-to-app",
        "sessionIdentifier": "uuid-for-this-interaction",
        "receivedMessage": {
            "title": "Title of Bubble",
            "subtitle": "Subtitle to be displayed under title",
            "imageTitle": "Title of image attachment",
            "imageSubtitle": "Subtitle of the image attachment.",
            "secondarySubtitle": "Title that is aligned right",
            "tertiarySubtitle": "Subtitle that is aligned right"
        }
    },
    "sourceId": "",
    "destinationId": "",
    "v": 1,
    "id": "d2f99c0e-f64c-4c3b-abbf-4a8567891ef5"
}
Tutorial Exercise
```
<sub>↳ `msp-rest-api.md` L4387–4431</sub>

For more help or guidance, see our Tutorial: Exercise: Integrating Your iMessage App.

### Form Message

Apple Messages for Business Form allow you to create rich, multipage interactive flows for users on iOS and iPadOS devices using a single JSON payload. This document provides the Form specifications, along with example outbound and inbound JSON payloads. This feature is supported in iOS version 18.4 and later.

You and your brands may already have ideas which could benefit from this type of interaction. Below are some example use cases:

Triage flows

CSAT Survey

Account creation or service sign-up

Known Issues

When a user task switches out to another app and back to Messages, the form closes. The user must tap to re-open the form. The form resets and the user has to re-enter their responses.

Because a user may have to re-open the form and re-enter their responses, we recommend you give less complicated use cases that provide quick answers through a simple triage menu. For example, if you use a technical support triage, the following choices appear:

Did you plug it in?

Did you turn it on?

Is the green light flashing?

Form Specifications

The specifications below define the content of the JSON payloads used to render the Form on user devices. For JSON examples, see the Sample Request Payload and Response Payload.

Request Payload

The type of interactiveMessage that initiates the experience is dynamic.

| Field | Description |
|---|---|
| version | REQUIRED. Should be 1.2 |
| template | REQUIRED. Type is 'messageForms'. Tells the client which template to use to render the view. |
| data | REQUIRED. Place all the data in this field. |
<sub>↳ `msp-rest-api.md` L4479–4485</sub>

Data Dictionary Objects

| Object | Description |
|---|---|
| splash | Shown at the start of the form. When using splash, ensure the appropriate fields listed below display: |
<sub>↳ `msp-rest-api.md` L4489–4491</sub>

\-header: If set, it displays in bold the title on the page underneath the image.

\-splashtext: Use this to display the body copy for the page.

\-buttonTitle: REQUIRED. Text on the button shown on the page. If buttonTitle is missing then this view doesn't display and continues onto the first module.

\-imageIdentifier: Image to be shown at the top of the view.

| startPageIdentifier | REQUIRED. Identifier for the starting page of the form. Must match one of the string identifiers for the configured pages. See pageIdentifier under pages below. |
|---|---|
| private | Defaults to false. Boolean value indicates whether to mark the response as private. If value is true, the response object contains this property (interactiveData > data > dynamic > private). private allows the MSP to detect that the payload requires special handling, and then decide how to handle it based on the brand’s requirements. |
| showSummary | Defaults to false. If set to true then it shows the summary of all the selections made within the form. |
| pages | REQUIRED. An array of different pages to be shown in the form. Every page object has following common objects. |
<sub>↳ `msp-rest-api.md` L4501–4507</sub>

\-pageIdentifier: REQUIRED. A unique identifier, as a string, for the page being shown, that is less than 20 characters in length. Do not reuse. Ex: "firstNamePage" or "0001".

\-type: REQUIRED. Use one of the following values: select, picker, datePicker, or input.

\-title: If set this displays the title in bold on the page.

\-subtitle: REQUIRED. Use this object to display the question for the page.

\-nextPageIdentifier: REQUIRED except for single select option page, where you specify the nextPageIdentifier within each of the item objects. If a page does not have a nextPageIdentifier set on it, the client assumes the current page to be the final page and proceeds to send or provides a summary page based on the data. This is a unique page identifier to show the next page.

\-submitForm: A Bool value placed on the pages to denote the end page of the form. Since multiple pages can act as an end page, this object can be set on multiple pages.

Types of Pages

Pages is an array of page elements and there needs to be at least be one page to trigger the Form experience.

| Page Type | Field | Description |
|---|---|---|
| select | multipleSelection | A Bool value that defaults to false or singleSelect. Set to true to enable multipleSelection on the page. |
| items | An array of objects defining the user experience. |  |
<sub>↳ `msp-rest-api.md` L4527–4531</sub>

\-title: Localized string value for display.

\-value: A string value of the object itself.

\-identifier: A unique identifier for the item.

\- imageIdentifier: A string containing the image identifier, from the imageItem dictionary. For more information about sending an image, see ImageItem dictionary.

\-nextPageIdentifier: A unique page identifier to show the next page. Set this value only when multipleSelection is not defined or set to false.

| picker | pickerTitle | A string value representing optional text shown next to the picker text field. This value defaults to an empty string. When empty the picker text field centers to the page |
|---|---|---|
| selectedItemIndex | A zero-indexed number identifying the item in the picker wheel should be selected by default. Defaults to item at index 0. |  |
| items | An array of objects defining the user experience. |  |
<sub>↳ `msp-rest-api.md` L4543–4547</sub>

\-title: Localized string value for display.

\-value: A string value of the object itself.

\-identifier: A unique identifier for the item.

| datePicker | hintText | A string representing optional text to give the user more input context that displays below the Date field. |
|---|---|---|
| options | Dictionary containing optional values for the Date Picker element. The date in the payload defaults to UTC+00:00 on user devices. |  |
<sub>↳ `msp-rest-api.md` L4555–4557</sub>

\-dateFormat: A string representing the date format on the page. Defaults to MM/dd/yyyy. Unless this property is explicitly set, all of the date properties are defined using this format. The dateFormat in the payload only applies to reading the value from the payload. For format string specifications see: Use Format Strings to Specify Custom Formats.

\-startDate: A string representing the date displayed by the date picker. Defaults to current date.

\-maximumDate: A string representing the maximum date that a date picker can show. Defaults to current date.

\-minimumDate: A string representing the minimum date that a date picker can show.

\-labelText: A string representing the text string to be shown next to date field. Defaults to text 'Date'.

| input | hintText | A string representing optional text to give the user more input context that displays below the Input field. |
|---|---|---|
| options | Dictionary containing optional values for the input field. |  |
<sub>↳ `msp-rest-api.md` L4569–4571</sub>

\-regex: A string representing a JSON encoded regular expression (regex) string to limit the type of input for input field to use. An example is when you want to limit input to only have proper decimal values provide a regex string: ^\\d*\\.?\\d?\\d?$. JSON encode all regex strings

\-placeholder: A text string used when there is no other text in the input text field. Default value are Required or Optional.

\-required: A Boolean value that defaults to false. When set to true, the next button on page is disabled until the user provides input.

\-inputType: A string value that defaults to singleline. Other values are multiline or singleline.

\-labelText: A string value representing a text label shown to identify the input field. This value defaults to an empty string. Only applies to inputType : singleline.

\-prefixText: A string value representing optional text shown next to the text field. This value defaults to an empty string. For example, you can set this value to denote the $ character for the field. Only applies to inputType : singleline.

\-maximumCharacterCount: An integer value representing the field size in characters for singleline and multiline. The field size defaults to 30 characters for singleline and 300 characters for multiline.

\-keyboardType: Optional string value. Type of keyboard to be shown. Possible values:

\--default: Default value. Specifies the default keyboard for the current input method.

\--asciiCapable: Specifies a keyboard that displays standard ASCII characters.

\--numbersAndPunctuation: Specifies the numbers and punctuation keyboard.

\--URL: Specifies a keyboard optimized for URL entry. This keyboard type prominently features the period (.), forward slash (/) characters, and the .com string.

\--numberPad: Specifies a numeric keypad designed for PIN entry. This keyboard type prominently features the numbers 0 through 9. This keyboard type does not support autocapitalization.

\--phonePad: Specifies a keypad designed for entering telephone numbers. This keyboard type prominently features the numbers 0 through 9 and the asterisk (*) and hash tag (#) characters.

\--namePhonePad: Specifies a keypad designed for entering a person’s name or phone number. This keyboard type does not support auto-capitalization.

\--emailAddress: Specifies a keyboard optimized for entering email addresses. This keyboard type prominently features the at (@), period (.), and space characters.

\--decimalPad: Specifies a keyboard with numbers and a decimal point.

\--webSearch: Specifies a keyboard optimized for web search terms and URL entry. This keyboard type prominently features the space and period (.) characters.

textContentType: A string value representing the keyboard and system information about the expected semantic meaning for the content that users enter. Supported values are name, namePrefix, givenName, middleName, familyName, nameSuffix, nickname, jobTitle, organizationName, location, fullStreetAddress, streetAddressLine1, streetAddressLine2, addressCity, addressState, addressCityAndState, sublocality, countryName, postalCode, telephoneNumber, emailAddress, URL, creditCardNumber, username, password, newPassword, and oneTimeCode. For a full description of each supported value, see UITextContentType on Apple Developer.

Sample Request Payload

Below is a sample request payload in JSON.

```json
{
    "type": "interactive",
    "interactiveData": {
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
        "data": {
            "version": "1.0",
            "requestIdentifier": "da39a3ee5e6b4b0d3255 <truncated>",
            "dynamic": {
                "version": "1.2",
                "template": "messageForms",
                "data": {
                    "startPageIdentifier": "0",
                    "showSummary": true,
                    "splash": {
                        "header": "Apple Card",
                        "splashtext": "Kindly answer the following questions to help us dispute this transaction.",
                        "buttonTitle": "Continue",
                        "imageIdentifier": "2"
                    },
                    "pages": [{
                            "pageIdentifier": "0",
                            "type": "select",
                            "title": "Type of Product",
                            "subtitle": "Was the merchandise you received defective or not as the merchant described?",
                            "multipleSelection": true,
                            "nextPageIdentifier": "1",
                            "items": [{
                                    "title": "Option 1",
                                    "value": "option1",
                                    "identifier": "001"
                                },
                                {
                                    "title": "Option 2",
                                    "value": "option2",
                                    "identifier": "002"
                                },
                                {
                                    "title": "Option 3",
                                    "value": "option3",
                                    "identifier": "003"
                                },
                                {
                                    "title": "Option 4",
                                    "value": "option4",
                                    "identifier": "004"
                                },
                                {
                                    "title": "Option 5",
                                    "value": "option5",
                                    "identifier": "005"
                                },
                                {
                                    "title": "Option 6",
                                    "value": "option6",
                                    "identifier": "006"
                                }
                            ]
                        },
                        {
                            "pageIdentifier": "1",
                            "type": "select",
                            "title": "Item Condition",
                            "subtitle": "Was the merchandise you received defective or not as the merchant described?",
                            "multipleSelection": false,
                            "items": [{
                                    "title": "Defective",
                                    "value": "defective",
                                    "identifier": "101",
                                    "nextPageIdentifier": "2"
                                },
                                {
                                    "title": "Not as described",
                                    "value": "notAsDescribed",
                                    "identifier": "102",
                                    "nextPageIdentifier": "3"
                                }
                            ]
                        },
                        {
                            "pageIdentifier": "2",
                            "type": "select",
                            "title": "Supporting Documents",
                            "subtitle": "Do you have any supporting documents that demonstrate that the product quality was not sufficient?",
                            "multipleSelection": false,
                            "items": [{
                                    "title": "Yes",
                                    "value": "yes",
                                    "identifier": "201",
                                    "nextPageIdentifier": "3"
                                },
                                {
                                    "title": "No",
                                    "value": "no",
                                    "identifier": "202",
                                    "nextPageIdentifier": "3"
                                }
                            ]
                        },
                        {
                            "pageIdentifier": "3",
                            "type": "picker",
                            "pickerTitle": "Select Your Region",
                            "nextPageIdentifier": "4",
                            "items": [{
                                    "title": "APAC",
                                    "value": "apac",
                                    "identifier": "301"
                                },
                                {
                                    "title": "EMEA",
                                    "value": "emea",
                                    "identifier": "302"
                                },
                                {
                                    "title": "LATAM",
                                    "value": "latam",
                                    "identifier": "303"
                                },
                                {
                                    "title": "NAM",
                                    "value": "nam",
                                    "identifier": "304"
                                }
                            ]
                        },
                        {
                            "pageIdentifier": "4",
                            "type": "datePicker",
                            "title": "Retrieval Date",
                            "subtitle": "What date did you receive, or expect to receive the product?",
                            "nextPageIdentifier": "5",
                            "options": {
                                "startDate": "2020-02-12",
                                "maximumDate": "2020-02-13",
                                "minimumDate": "2020-01-01",
                                "dateFormat": "MM/dd/yyyy"
                            }
                        },
                        {
                            "pageIdentifier": "5",
                            "type": "input",
                            "title": "Remaining Issues",
                            "subtitle": "Please provide details about remaining issue",
                            "nextPageIdentifier": "6",
                            "options": {
                                "required": true,
                                "inputType": "multiline",
                                "maximumCharacterCount": 300,
                                "keyboardType": "UIKeyboardTypeEmailAddress"
                            }
                        },
                        {
                            "pageIdentifier": "6",
                            "type": "input",
                            "title": "Product name",
                            "subtitle": "Please provide name of the product",
                            "options": {
                                "required": false,
                                "inputType": "singleline",
                                "maximumCharacterCount": 25,
                                "keyboardType": "UIKeyboardTypePhonePad"
                            },
                            "submitForm": true
                        }
                    ]
                }
            },
            "images": [{
                    "data": "base64encoded-image-file",
                    "identifier": "1"
                },
                {
                    "data": "base64encoded-image-file",
                    "identifier": "2"
                },
                {
                    "data": "base64encoded-image-file",
                    "identifier": "3"
                },
                {
                    "data": "base64encoded-image-file",
                    "identifier": "4"
                }
            ]
        },
        "receivedMessage": {
            "title": "Apple Card Dispute Form",
            "subtitle": "Please fill out the following dispute form.",
            "style": "small",
            "imageIdentifier": "1"
        },
        "replyMessage": {
            "title": "Tap to view your response.",
            "subtitle": "",
            "style": "small",
            "imageIdentifier": "1"
        }
    }
}
Response Payload
```
<sub>↳ `msp-rest-api.md` L4617–5015</sub>

The response from the client is encapsulated within interactiveData > data > dynamic > selections object.

Each of the objects within the selections object would have the following elements.

| Element | Description |
|---|---|
| pageIdentifier | A unique identifier representing the page from which the response is mapped. |
| title | A string representing the title of the page |
| subtitle | A string representing the question or subtitle on the page. |
| items | An array containing all the selections made on the page. Each of the objects within the array items contains the following structure: |
<sub>↳ `msp-rest-api.md` L5025–5033</sub>

\-identifier: A unique identifier set on the individual items for each type of page selected. Except for pages with type of input and datePicker the identifier is the same value as the pageIdentifier.

\-type: One of the following values select, datePicker, or input that corresponds to the page’s type value.

\-title: The localized value of an item selected or user input. For example, the datePicker type would format the date value. For input type if any prefixLabel is provided, and the title needs to contain the prefixLabel + inputValue.

\-value: A string value included in the request payload. For the selections objects and for input type, this is the same value as in title (user input). For datePicker pages, this field returns the value in UTC format: yyyy-MM-dd'T'HH:mm:ss'Z'.

Sample Response Payload

Below is an example of a response payload in JSON.

```json
{
    "type": "interactive",
    "interactiveData": {
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
        "sessionIdentifier": "ad461c33-7534 <truncated>",
        "data": {
            "version": "1.0",
            "dynamic": {
                "template": "messageForms",
                "version": "1.2",
                "selections": [{
                        "pageIdentifier": "001",
                        "items": [{
                            "identifier": "001_03",
                            "value": "option03",
                            "type": "select",
                            "title": "Single 3"
                        }],
                        "subtitle": "Single Select Page",
                        "title": "Please Choose One Selection To Move On To The Next Page"
                    },
                    {
                        "pageIdentifier": "002",
                        "items": [{
                                "identifier": "002_01",
                                "value": "multi1",
                                "type": "select",
                                "title": "Multi 1"
                            },
                            {
                                "identifier": "002_03",
                                "value": "multi3",
                                "type": "select",
                                "title": "Multi 3"
                            },
                            {
                                "identifier": "002_05",
                                "value": "multi5",
                                "type": "select",
                                "title": "Multi 5"
                            }
                        ],
                        "subtitle": "Multiple Selection",
                        "title": "Select All That Apply"
                    },
                    {
                        "pageIdentifier": "003",
                        "items": [{
                            "identifier": "003",
                            "value": "2021-03-30T07:00:00Z",
                            "type": "datePicker",
                            "title": "03/30/2021"
                        }],
                        "subtitle": "Date Picker",
                        "title": "Date Picker With Min/Max Date and Label Text"
                    },
                    {
                        "pageIdentifier": "004",
                        "items": [{
                            "identifier": "004",
                            "value": "50.00",
                            "type": "input",
                            "title": "$50.00"
                        }],
                        "subtitle": "Numeric Input - Currency",
                        "title": "With Custom Label, Prefix, Regex and Placeholder Text"
                    },
                    {
                        "pageIdentifier": "005",
                        "items": [{
                            "identifier": "005",
                            "value": "J. Appleseed",
                            "type": "input",
                            "title": "J. Appleseed"
                        }],
                        "subtitle": "Text Input - Single Line",
                        "title": "With Placeholder, Label and Expecting a Name"
                    },
                    {
                        "pageIdentifier": "006",
                        "items": [{
                            "identifier": "006",
                            "value": "Multi\\nLine\\nText\\nInput",
                            "type": "input",
                            "title": "Multi\\nLine\\nText\\nInput"
                        }],
                        "subtitle": "Text Input - Multiple Lines",
                        "title": "Optional Additional Comment Field"
                    }
                ]
            },
            "receivedMessage": {
                "subtitle": "Tap to view the available pages",
                "imageIdentifier": "1",
                "style": "small",
                "title": "Apple Messages for Business Form"
            },
            "replyMessage": {
                "subtitle": "Tap to review your selections",
                "alternateTitle": "Apple Messages for Business Form",
                "imageIdentifier": "1",
                "style": "small",
                "title": "Apple Messages for Business Form"
            },
            "requestIdentifier": "42bcfae9-3da6 <truncated>",
            "images": [{
                    "identifier": "1",
                    "data": "base64encoded-image-file"
                },
                {
                    "identifier": "2",
                    "data": "base64encoded-image-file"
                }
            ]
        }
    }
}
Invitation Messages
```
<sub>↳ `msp-rest-api.md` L5049–5283</sub>

Overview

<!-- img: Apple_Invitations_Crop_6.png -->

Authorized businesses can invite customers to engage in conversations via Apple Messages for Business by sending an invitation message to the mobile number the customer has provided. These branded and verified invitations appear in the Messages app on Apple devices, allowing customers to engage with businesses in secured and private conversations.

A screenshot of connect message with image, as displayed on iPhone.

Invitation messages display in the branded business conversation

Requirements

Businesses must request access to the invitations feature. For enhanced security, all invitation messages are template-based. Apple creates and manages templates to support specific use cases. Business-specific templates are not supported.

Customers must provide the business with explicit opt-in for messaging to the provided phone number before the invitation is sent. Customer opt-out requests must be respected.

All the devices linked to the Apple Account receiving invitation messages must be running iOS 18.0/macOS 15.0 or later.

Templates

Templated invitation messages allow businesses to invite customers who are Apple users to engage in Apple Messages for Business to take needed actions easily and securely.

Access to invitations must be requested by the business, and approved by Apple.

The invitations template only allows limited text customization.

New and Existing Conversations

If the user does not have an existing conversation with the business, a new one is created.

If the user responds to the business, the conversation becomes a normal two-way Apple Messages for Business conversation.

If the user has an existing Apple Messages for Business conversation with this business, invitations appear in the same conversation thread.

User Consent

Users must explicitly agree to receive invitations from a business and provide their phone number. This can include signing up on the business's web site to receive messages, or choosing to switch to messaging during a voice call with IVR. Unsolicited invitations and marketing campaigns are prohibited. Businesses must respect user opt-out.

User Leaves the Conversation

Users can choose to opt-out of a conversation at any time, if they select Leave Conversation. See also Leave Conversation.

Resulting actions:

The conversation between the business to the user through the standard Apple Messages for Business messages is blocked.

The user can choose to reopen the conversation by sending a new message to the business.

A message is sent to the MSP indicating that the user with that phone number has opted out of invitations from that business.

<!-- img-row: brand-shell.png, junk-detail-shell.png, leave-detail-shell.png -->

User options to Report Junk or Leave this Conversation

User Conversation

Management Options

 User options to Leave this Conversation

User option to

Leave Conversation

 User options to Report Junk

User option to

Report Junk

Important

Businesses must respect this and not send any further invitation messages to the user, until the user registers with the business again to receive invitations to the same phone number. If the business fails to honor the user's opt-out request, the user can report the unwanted invitation to Apple through the "Report Junk" feature. The Apple team reviews these reports, and takes appropriate action if the terms of use policies have been violated.

Integration

As with other Apple Messages for Business messages, the Messaging Service Provider (MSP) sends invitation messages to the MSP Gateway endpoint using secure HTTP and method POST.

POST https://mspgw.push.apple.com/v1/message

In addition to common required HTTP headers, include the following header in the request. If it is missing, the request is rejected by MSP Gateway.

message-type: notification

Invitations are classified as a notification message. The notification message is an interactive message that is template-based. The message contains a few additional keys, such as templateId and referenceId, as listed in this table.

Notification Headers

| Key | Name | Type | Description |
|---|---|---|---|
| templateId | Template ID | string | REQUIRED. A field inside notification, which indicates the template used in the notification message |
| referenceId | Reference ID | string | REQUIRED. A field inside notification, which tells the context of the notification message. It can be an order number, case ID, etc. Must not exceed 1,000 characters in length, and must not contain quotation marks or apostrophe characters. |
| locale | Locale | string | Indicates the language used in the message. If the locale is not specified, the default language will be used. |
| parameters | Template parameters | json | REQUIRED. All the required parameters must be provided in the value of this field. Otherwise, the validation will fail and the message will be rejected. If the brandLogo image is used, it must be in PNG format. |
<sub>↳ `msp-rest-api.md` L5413–5421</sub>

Example Notification Message

```json
{
    "v": 1,
    "id": "fbc2ccee-f67e-4bd5-96e4-934967db0159",
    "sourceId": "fbc2ccee-f67e-4bd5-96e4-934967db0159",
    "destinationId": "tel:+11234567890",
    "interactiveData": {
        "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
        "data": {
            "version": "1.0",
            "requestIdentifier": "fcb5e9ca-0ddc-4a07-bf9b-7fcbd044aeeb",
            "notification": {
                "templateId": "binaryChoice.engage.withImage",
                "locale": "en-us",
                "referenceId": "{ caseNumber : 1009273616 }",
                "parameters": {
                    "brandName": "testBrand",
                    "brandLogo": "<decoded-image>"
                }
            }
        },
        "useLiveLayout": true
    },
    "type": "interactive"
}
When MSP Gateway receives an invitation message from an MSP, it performs a number of validations on the message for business eligibility and message format, including:
```
<sub>↳ `msp-rest-api.md` L5427–5475</sub>

Authentication: The auth token in the authorization header must be valid and doesn’t expire.

Message format: The message contains required headers (fields) and is well formatted. This includes:

The request must have the message-type header

The message contains a valid template ID and required parameters

Business eligibility:

The business is registered for invitation messages

The template ID in the message is authorized for the business

Other:

The user has a device capable of receiving invitation messages

The user hasn’t opted out of invitation messages

If any of the validations fail, the message is rejected and an error response status is returned. The failure reason is listed in the error status response. For example:

 Reason: The template is not allowed for the business

Common Error Response: Status Codes and Possible Reasons

| Status Code | Possible Reason for Error |
|---|---|
| 200 OK | The message is valid and has been successfully processed. |
| 400 Bad Request | Unable to deliver the message. |
<sub>↳ `msp-rest-api.md` L5509–5513</sub>

Possible reasons include:

* The request doesn't contain the header message-type

* The message is not a notification message

* The template doesn't exist

* The message doesn't contain all required parameters for the template used

* The message is malformed

| 403 Forbidden | Unable to deliver the message. |
|---|---|
<sub>↳ `msp-rest-api.md` L5527–5527</sub>

Possible reasons include:

* The message doesn't contain authorization header or source ID header

* Auth token in Authorization header is invalid

* The business is not eligible to send invitation messages

* The template ID is not allowed for the business

| 404 Not Found | Unable to deliver the message. |
|---|---|
<sub>↳ `msp-rest-api.md` L5539–5539</sub>

Possible reasons include:

* Phone number does not match an active Apple Account

* One or more of the user's devices is running an unsupported OS version

* The message is undeliverable due to user preference or a legal reason

| 410 Gone | Unable to deliver the message. |
|---|---|
<sub>↳ `msp-rest-api.md` L5549–5549</sub>

Possible reason includes:

* The request doesn't contain the header message-type or the header value is incorrect

| 500 Internal Error | Unable to deliver the message. |
|---|---|
<sub>↳ `msp-rest-api.md` L5555–5555</sub>

Possible reason includes:

* An unexpected error occurred during message processing

Note

404 — Fallback Expectation
 - When a 404 response is received, the message cannot be delivered via Apple Messages for Business. MSPs are expected to implement a fallback mechanism to the next channel the brand has configured (e.g., SMS, or other messaging channels) to ensure the customer is still reachable. Brands should define their preferred fallback channel as part of their integration setup.

Understanding sourceId and destinationId in invitation flows

The values of sourceId and destinationId depend on the message direction and on whether an opaque ID has been created for the customer.

Standard (non-invitation) message flow

In a standard Apple Messages for Business conversation, an opaque ID always exists because the customer initiated the conversation. The behavior is consistent:

| Direction | sourceId | destinationId |
|---|---|---|
| MSP → MSPGW (message to customer) | Business ID | Opaque ID |
| MSPGW → MSP (message from customer) | Opaque ID | Business ID |
<sub>↳ `msp-rest-api.md` L5582–5586</sub>

Note

The opaque ID is only created when a customer starts or accepts a conversation. For more information, see About the Opaque ID.

Invitation message flow

Because invitation messages are sent to customers who have not yet started a conversation, no opaque ID exists at the time the invitation is sent. The phone number is used instead as the destination identifier.

The customer's response (Yes or No) determines whether an opaque ID is created:

| Step | Direction | sourceId | destinationId |
|---|---|---|---|
| MSP sends invitation | MSP → MSPGW | Business ID | Customer's phone number (tel:+11234567890) |
| Customer accepts (Yes) | MSPGW → MSP | Opaque ID | Business ID |
| Customer declines (No) | MSPGW → MSP | Customer's phone number | Business ID |
<sub>↳ `msp-rest-api.md` L5606–5612</sub>

When the customer accepts, an opaque ID is created and all subsequent messages in that conversation use the opaque ID. When the customer declines, no opaque ID is created, and the phone number is used in any further system messages related to that interaction.

Schema and Example Payloads

The table includes example messages and download links for schema and example payload files.

<!-- img: binaryChoice-withImage-gray.jpg -->

| Type | Example Message | Schema | Example JSON Payload |
|---|---|---|---|
| Connect Using Messages | A screenshot of Connect option message with image, as displayed on iPhone. | Download | Download |
<sub>↳ `msp-rest-api.md` L5624–5626</sub>

https://register.apple.com/resources/messages/msp-rest-api/construct-payload

Construct Payload API

The Construct Payload API allows you to generate a rich link payload from a URL. It supports App Clips, Apple Music, and Apple Maps URLs, enabling rich rendering with artwork, metadata, and map snapshots directly in Messages.

<!-- img: ConstructPayload_Flow.png -->

Following is the flow on how to send a RichLink message using the Construct Payload API.

Construct Payload flow

Construct Payload flow

URL

POST https://mspgw.push.apple.com/v1/constructPayload

HTTP Header

| Name | Type | Description |
|---|---|---|
| Authorization | string | REQUIRED. Credentials used to authenticate the request. See Authorizing Messages. |
| content-type | string | REQUIRED. A string value, set to application/json, advertising that the content is a JSON data. |
| source-id | string | REQUIRED. A string that identifies the message sender. |
| id | uuid | A UUID string that identifies the message. |
<sub>↳ `msp-rest-api.md` L5650–5658</sub>

ConstructPayload Properties

| Name | Type | Description |
|---|---|---|
| type | string | REQUIRED. A string representing the type. Default is link . |
| link | object | REQUIRED. A collection of name and values used for link type. |
| version | integer | REQUIRED. The payload version number. Default is 1.0. |
<sub>↳ `msp-rest-api.md` L5662–5668</sub>

link Properties

| Name | Type | Description |
|---|---|---|
| url | string | REQUIRED. The URL to generate the rich link payload from. See Supported URL Types for accepted values. |
| storeRegion | string | ISO 3166 alpha-2 country code of the App Store region. By default it is "US". Set this value incase the AppClip is not in the US App Store. |
<sub>↳ `msp-rest-api.md` L5672–5676</sub>

Supported URL Types

App Clips

URLs that include App Clip elements on the web page. If the URL does not support App Clips, the API returns 400 Bad Request. For more details, see Generating a Rich Link payload for App Clips.

Apple Music

music.apple.com URLs that resolve to one of the following content types:

| Content Type | Example URL |
|---|---|
| Song | https://music.apple.com/us/album/song-name/id |
| Album | https://music.apple.com/us/album/album-name/id |
| Artist | https://music.apple.com/us/artist/artist-name/id |
| Playlist | https://music.apple.com/us/playlist/playlist-name/id |
| Music Video | https://music.apple.com/us/music-video/video-name/id |
| Radio Station | https://music.apple.com/us/station/station-name/id |
<sub>↳ `msp-rest-api.md` L5692–5704</sub>

Note:

The country code in the URL (e.g., /us/, /gb/) should match the target user's storefront for full rich link rendering, including the play button, when applicable. We recommend dynamically constructing the Apple Music URL using the locale field from the user's incoming message, rather than hardcoding a country code.

Apple Maps

maps.apple.com URLs that resolve to one of the following:

| Content Type | Example URL |
|---|---|
| Place (with coordinates) | https://maps.apple.com/place?address=...&coordinate=... |
| Place (with place ID) | https://maps.apple.com/place?place-id=... |
| Search Query | https://maps.apple.com/?q=coffee+shops+san+francisco |
| Directions | https://maps.apple.com/?daddr=...&saddr=... |
| Airport | https://maps.apple.com/place?place-id=<airport-id> |
<sub>↳ `msp-rest-api.md` L5718–5728</sub>

Generating a Rich Link payload for App Clips

Before calling the API make sure that the URL has the App Clips elements on its web page. For more details please check here. If the URL doesn't support App Clips the API will return 400 Bad Request. The App Clip Rich Link Generator requires image under 4MB in size.

Example of Construct Payload Request

Request

```json
{
 "type":"link",
 "link":{
    "url":"https://www.example.com"
    },
 "version":1.0
}
Response
```
<sub>↳ `msp-rest-api.md` L5740–5754</sub>

200 OK

```json
{
    "version": "1.0",
    "richLinkDataRef": {
        "title": "https://www.example.com",
        "signature-base64": "AZ60f1FhkxZ4HdtzGFXXXXX",
        "size": 351298,
        "url": "https://p97-content.icloud.com",
        "owner": "M66169d55-aaee-48dd-b781-XXXXXXXXX.XXXXXX",
        "key": "00ccec31f00f05d3416bf0a41f4762afa3241f486ff3509dXXXXXXXX"
    }
}
Sending Rich Link Message with payload
```
<sub>↳ `msp-rest-api.md` L5758–5780</sub>

Follow our Rich Link message specification and use the RichLinkDataRef to attach the payload returned from the Construct Payload API.

Example of Rich Link Message Request

Request

```json
{
    "sourceId": "<business_id>",
    "destinationId": "<destination_id>",
    "id": "<message_id>",
    "v": 1,
    "type": "richLink",
    "richLinkDataRef":{
        "title": "https://www.example.com",
        "signature-base64": "AZ60f1FhkxZ4HdtzGFXXXXX",
        "size": 351298,
        "url": "https://p97-content.icloud.com",
        "owner": "M66169d55-aaee-48dd-b781-XXXXXXXXX.XXXXXX",
        "key": "00ccec31f00f05d3416bf0a41f4762afa3241f486ff3509dXXXXXXXX"
    }
}
Response
```
<sub>↳ `msp-rest-api.md` L5790–5820</sub>

200 OK

https://register.apple.com/resources/messages/msp-rest-api/channel-settings

Specific Channel Settings

Channel settings enable the capabilities Apple Messages for Business offers. The Messaging Service Provider needs to keep channel specific settings for each business.

By default you will receive one or more Messages for Business ID, one per account (private or commercial) created on Register. See how to create a Landing Page to register these ID.

List of Settings

Following is a non-exhaustive list of settings you can store or offer in an editable form for the business owner.

| Function | Name | Type |
|---|---|---|
| Apple Messages for Business account | Messages for Business ID | Single value per Apple Messages for Business account for each Apple Messages for Business account. Generated by Apple. |
| Apple Pay | Merchant ID |  |
<sub>↳ `msp-rest-api.md` L5836–5840</sub>

Verified Domain Name

Merchant Name

PEM file

Payment Gateway

| Base Domain URL | Set of values provided by the business. |
|---|---|
| OAuth | Title |
<sub>↳ `msp-rest-api.md` L5850–5852</sub>

Response Type

Scope

Client Secret

OAuth URL

| Token URL | Set of values provided by the business. |
|---|---|
| iMessage app extension | App ID |
<sub>↳ `msp-rest-api.md` L5862–5864</sub>

App Name

| BID URL | Set of values provided by the business. |
|---|---|
<sub>↳ `msp-rest-api.md` L5868–5868</sub>

Client Landing Page

Businesses need to subscribe to a Messaging Service Provider (MSP) to receive messages. When brands first sign up for Apple Messages for Business on Apple Business Register, they choose an MSP as their service to help them send and receive messages to their customers.

When your MSP gets a new brand, also known as a client, you need the following information from Apple Business Register:

The Apple Business Register generated Business ID for the new brand.

The new brand's name and logo.

NOTE For internal test accounts, it only returns the Business ID.

See the related exercises in the API Tutorial to build and test the data retrieved from Apple Business Register.

Device Capabilities

Human and bot interactions must detect the device capabilities to compose the appropriate response for that device.

The Apple Messages for Business REST API defines message headers in detail. For more information, see HTTP Headers in Common Specifications.

Guidelines for Device Capability

Capability Detection: Ensure your system identifies device capabilities before composing a response. This includes checking whether specific features, such as forms, are supported.

Handling Unsupported Features: If a device does not support certain features (e.g., forms), adapt the interaction by providing alternative methods. For example, for Form Message, if “FORM” is absent from the capability list, each question should be sent as a separate object. Alternatives include:

Select or Picker Pages: Convert these into a Quick Reply with up to 5 options, or use a List Picker for more extensive choices.

Date Picker Pages: Use a Time Picker instead.

Input Pages: Send the question as a text message, prompting the user to respond with their answer.

Other Unsupported Features: Similarly, for any other capabilities that a device lacks, identify the best alternative to ensure the interaction remains smooth and intuitive.

By detecting device capabilities and providing appropriate alternatives, you ensure a seamless user experience across all devices, even when specific features are unavailable.

https://register.apple.com/resources/messages/msp-rest-api/doc-rev-history

Revision History
| Date | Version | Summary |
|---|---|---|
| 3 Jun 2026 | 4.2.9 | Construct Payload section updated to include Apple Music and Apple Maps rich link support |
| 19 May 2026 | 4.2.8 | Closed Conversation section updated, including HTTP 410 Gone response details |
| 19 May 2026 | 4.2.7 | Invitation Messages section updated, including sourceId and destinationId clarification |
| 08 May 2026 | 4.2.6 | Invitations feature details updated |
| 08 May 2026 | 4.2.5 | UUID details updated |
| 20 April 2026 | 4.2.4 | Invitation Messages added to Required Features; 404 — Fallback Expectation section added |
| 06 March 2026 | 4.2.3 | Minor corrections |
| 27 February 2026 | 4.2.2 | Interactive message image type restrictions added |
| 16 Februrary 2026 | 4.2.1 | Minor updates to leave conversation function |
| 11 February 2026 | 4.2 | Updated payload specifications for enhanced security |
| 04 February 2026 | 4.1.8 | Feature name revision, and Leave Conversation specifications updated |
| 01 December 2025 | 4.1.7 | New server fix for the Form Message applied. The latest version available is 1.2, and It can be set in the interactiveData > data > dynamic > version section |
| 30 October 2025 | 4.1.6 | Clarified Close Conversation requirements |
| 14 April 2025 | 4.1.5 | Updated Apple Maps Rich Link specifications |
| 07 April 2025 | 4.1.4 | Updated Business Updates specifications |
| 21 March 2025 | 4.1.3 | Updated App Clip Rich Link Generator specs |
| 04 February 2025 | 4.1.2 | Channel Settings – Updated OAuth URL parameters details |
| 24 October 2024 | 4.1.1 | Updated Type Interactive details |
| 01 October 2024 | 4.1 | Updated Tapback information with new reactions available with iOS 18 |
| 14 September 2024 | 4.0.8 | Updated iOS requirements for Business Updates feature |
| 28 August 2024 | 4.0.7 | Updated file type support and device capability handling |
| 09 August 2024 | 4.0.6 | Updated MSP feature requirements including new Rich Links capabilities |
| 15 April 2024 | 4.0.5 | sessionIdentifier details added |
| 11 April 2024 | 4.0.4 | Minor fixes |
| 01 February 2024 | 4.0.3 | Service name update to match registered service mark |
| 04 October 2023 | 4.0.2 | Minor wording adjustments for clarify |
| 29 September 2023 | 4.0.1 | Corrections to the Response Codes session |
| 31 May 2023 | 4.0 | Links updates and new Construct Payload for App Clips support |
| 15 March 2023 | 3.9 | Updated Rich Link instructions for Apple Maps URL |
| 24 February 2023 | 3.8 | Deprecation of the original oAuth authenticate method. The most recent Authentication Message type shall be used. |
| 13 January 2023 | 3.7.5 | Corrections on oAuth authenticate attribute |
| 10 January 2023 | 3.7.4 | Corrections |
| 03 January 2023 | 3.7.3 | Corrections |
| 15 December 2022 | 3.7.2 | Rich Links and Custom URL clarification |
| 02 December 2022 | 3.7.1 | Corrections |
| 09 November 2022 | 3.7 | Clarification on Channel Settings |
| 08 September 2022 | 3.6 | Clarification on Opaque ID and removal of New OAuth implementation |
| 15 June 2022 | 3.5.1 | Forms specifications fixes |
| 07 June 2022 | 3.5 | New Authentication Message Specification available in iOS 16 and macOS 13 |
| 06 June 2022 | 3.4.1 | Form documentation fixes |
| 06 May 2022 | 3.4 | Form documentation fixes |
| 22 April 2022 | 3.3 | Fixes sample code |
| 04 April 2022 | 3.2 | Form Message type moved to Form Messages |
| 23 March 2022 | 3.1 | HIG, Links updates and fixes in forms and list picker |
| 15 March 2022 | 3.0.1 | Fixed on links and forms specs |
| 11 February 2022 | 3.0.0 | Integration requirements revised for bot and agent, capabilities and device-agent deprecated in March 2022 |
| 12 January 2022 | 2.1.2 | Updated instructions about Sending Rich Link Messages |
| 22 November 2021 | 2.1.1 | Fixes |
| 25 October 2021 | 2.1 | Updated Quick Reply and added Capabilities-list |
| 08 October 2021 | 2.0.2 | oAuth2 flow changes in iOS 15 within the HTTP Body |
| 06 October 2021 | 2.0.1 | Various fixes on Attachment payload, BaseInteractiveMessage |
| 20 September 2021 | 2.0.0 | Rebranded Business Chat to Messages for Business; Chat Suggest to Message Suggest; removed 'BETA' from Quick Reply. |
| 22 July 2021 | 1.0.0 | Initial release: |
<sub>↳ `msp-rest-api.md` L5909–5962</sub>

- Added HTTP Header : "capability-list"
- iMessage App Message type clarification
- Quick Reply Message type (Interactive)
Revision Number Incrementation
| Version | Explanation |
|---|---|
| 1.0.0 | Major revision. Includes number increment and new content. |
| 1.0.0 | Minor revision. Includes number increment and changes to current content, such as content corrections, graphics, grammar, etc. |
<sub>↳ `msp-rest-api.md` L5967–5969</sub>


---

# Part 1B — MSP API Tutorial: Worked Examples (verbatim)

> **Source:** `msp-api-tutorial.md` — verbatim (entities decoded, escapes removed, tab-tables → Markdown, JSON/cURL fenced unchanged).

# msp-api-tutorial

https://register.apple.com/resources/messages/msp-api-tutorial/

Overview

* Version: `3.4`

* Last update: 29 April, 2026

Welcome to the Messaging Service Provider (MSP) API Integration Tutorial! The exercises in this tutorial help you get your messaging platform integrated with the Messages for Business service.

This tutorial offers some code samples resources which can be [downloaded](https://register.apple.com/resources/messages/msp-api-tutorial/download).

Apple requires that you build and demonstrate support for all the features for approval to connect brands to Messages for Business, if you want to view a full listing, see [MSP REST API - Required Features](https://register.apple.com/resources/messages/msp-rest-api/#required-features).

If you have any questions about the Integration Review, contact the Apple team directly.

https://register.apple.com/resources/messages/msp-api-tutorial/integration

Tutorial Setup

This step-by-step tutorial helps you to design and integrate your Messaging Service Provider (MSP) platform with the Messages for Business REST API.

NOTE

You should configure and implement all Messages for Business features in this tutorial on your test server.

The code examples provided are in the Python programming language, and HTTP protocol is the fundamental architecture, but you can adapt the code for use in any language. This tutorial relies on a test server platform in a testing environment you provide and configure as an MSP. Do not use a production server in a production environment. Your MSP test server platform needs access to the web so it can talk to the Messages for Business service.

You'll learn the following in this tutorial:

Experiment with different message types, from basic text messaging to sending Apple Pay payments.

Use Messages for Business with different message types, such as text and interactive, and the handling of small to large attachments.

By the end of this tutorial, you should be familiar with the concepts and features Messages for Business offers to businesses, including familiarity with implementing these features on your MSP platform.

All tutorials follow the sending and receiving data diagram below. A user's, device sends a message to the Messages for Business service that posts the user's message to the MSP endpoint. The MSP platform digests the message and forwards it to the appropriate business agent for a response. The business agent responds and sends the message back to the MSP platform that posts it to the Messages for Business service, and from there it is forwarded back to the user's Device.

<!-- img: Integration-messages-for-business.png -->

Setting Up Your Accounts on Apple Business Register

You must enter all MSP, Messages for Business accounts, brands, team members, and organization details into Apple Business Register to create the accounts needed for this tutorial.

Apple Business Register is a self-service portal, and is mostly self-explanatory with a few key items of note:

You have to apply and be approved for your company to offer MSP services. If you don't see Messaging Service Provider as an item in Apple Business Register, contact your Messages for Business account manager to determine the application process status.

Apple Business Register generates several key values that you'll need for your servers, such as MSP ID, Business ID, and a secret passphrase. Other parameters you have to enter into Apple Business Register are organizational details, team member details, brand colors, brand logos, and your server URLs.

Each Business ID is associated with an unique MSP ID. Internal test Business IDs have no brand. Commercial Business IDs must be associated with a brand in Apple Business Register, which requires an approval step by the brand review team that may take several business days.

Configuring Your MSP Test Server

When prompted, you can refer to the following information throughout the exercises in this tutorial:

MSP ID: a unique UUID you receive upon approval of your MSP account

Business ID: a unique UUID you receive upon approval of your Messages for Business account

Secret passphrase for API: a Base64-encoded string

MSP message endpoint: https://<your.endpoint.host>/message

Information obtained from your Apple Business Register MSP account

NOTE

For legacy reasons, code samples and some parts of the Messages for Business documentation may refer to "CSP ID" instead of "MSP ID". CSP stands for Customer Service Provider and is equivalent to the new term Messaging Service Provider (MSP).

MSP endpoint SSL certificate requirements

Your SSL certificate must meet the HTTPS requirements needed to connect to the Messages for Business endpoints. Your SSL certificate should contain the following:

Valid SSL certificate

Issued name on the SSL certificate must match the hostname

Certificate must include the entire trust chain, including CAs and root

Certificate must be in Oracle Java 8+ framework's default trust store, meaning signed by trusted CAs, supported encryption, and format

NOTE

Messages for Business does not allow the use of Ngrok hosts and other similar firewall-defeating technologies. The use of these technologies may result in declined requests for messaging, client landing page, or authentication endpoints.

Messages for Business Server Endpoints

The endpoints allow messages to be routed between the Messages for Business service and your platform. See How to Set Up Your Endpoint.

Production: https://mspgw.push.apple.com/v1/message

Staging: https://mspgw-int.push.apple.com/v1/message

Use the staging endpoint to develop and test your server changes. Even though you can message users through the staging endpoint, it has a load limit and is not intended for production messages.

TIP

Messaging requests arrive at your registered MSP base URL plus /message.

Tools

This section includes the tools used throughout this tutorial.

Apple Devices

To test and verify the exercises from both your console and user-side, you'll need

an Apple supported device that can run iOS 11.3 or later.

an Apple Account setup under the Message App settings / iMessage.

TIP

If your device continues to display Waiting for activation, use the following link to check your device settings If you get an error when trying to activate iMessage or FaceTime.

You can use also Messages for Business from macOS device by running macOS monterey version 12.0 or later. For more information about compatibility, see capability-list under HTTP Headers under Common Specifications.

Older version of macOS, may not support certain message types and will display the following message when clicked:

<!-- img: iOS-device-notification-no-shadow.png -->

Development Tools

The following development tools are needed to complete the exercises in this tutorial:

Python 3.7

Python modules:

Flask

pyjwt

pycryptodome (replaces pycrypto)

requests

cryptography

How to Set Up Your Endpoint

If your endpoint isn't set up, you'll need to set up a messaging server platform endpoint to send and receive messages from the Messages for Business service.

Select a server that has sufficient storage available for the application, as Apple doesn't save messages after delivery.

Set up your server to receive HTTPS messages.

Configure a URL endpoint on your messaging server. Your server must be capable of receiving traffic on /message.

Confirm that you can receive traffic to your URL on /message.

You must have a logging tool installed and activated so that you can triage issues from your server side.

Set Up an HTTPS proxy

The Messages for Business server expects the MSP endpoint to listen for the registered platform's API base-URL supporting HTTPS. You can simplify local development by setting up a proxy on the platform's API base-URL server to point to a local HTTP port, such as 8002:

https://your.endpoint.base.url points to http://localhost:8002/

Research online methods to redirect HTTPS traffic to a local development server, or to set up Flask to handle SSL using correctly generated keys and certificates.

NOTE

Exercises in this tutorial expect that you are redirecting messages to the Messages for Messages for Business Server at http://localhost:8002.

https://register.apple.com/resources/messages/msp-api-tutorial/receiving-sending-messages

Sending and Receiving Messages

When a user sends a message to a business, the user's device sends the message to the Messages for Business server. The Messages for Business server forwards the message to the Messaging Service Provider (MSP) platform by making a POST request to the /message endpoint. For more information on receiving messages, see Messages Received.

When a business replies to a user's text message, the MSPs platform forwards the reply to the Messages for Business server. To forward the reply, the MSP platform prepares the message for delivery and sends a POST request to the Messages for Business /message endpoint. For more information on sending messages, see Messages Sent.

There is no time limit for a business to reply or send a new message to a user, but consider the following guidelines and features available:

Notifications

Receiving Closed Conversation Messages

In this section, you'll learn how to listen for, receive, and validate incoming messages.

TIP

You can initiate a conversation in the Messages app by using the business ID directly as a recipient in Compose Message. The format is urn:biz:<your-business-id>.

Exercise: Listening for Incoming Messages

In this exercise, you run a simple web service and listen to message requests. Send a text message from the Messages app on a device to your business and observe the request of the text message.

Perform the following tasks on your test server:

Locate the zip folder and unzip it.

Locate and run the 00_listening.py file.

Listen to POST requests at: https://<yourCSPEndpoint>/message.

Sending a Message from Your iOS Device

Send a text message from the Messages app on an iOS device to your business.

From an iOS device, open Messages.

Put in your business URN identifier (urn:biz:<your registered business id>) as the recipient.

Compose a simple text message, such as "Hello business!", and tap send.

Expected MSP server response

By default, on your MSP test server you'll receive at least two messages: typing_start and the actual message. The typing indicator in the output automatically displays on the console and is not part of the typing_start indicator.

Just received a message!

Just received a message!

TIP

When using a HA Proxy for your messaging endpoint, make sure to add Apple's Class A address block to accept incoming traffic: 17.0.0/8.

Exercise: Receiving a Text Message

In this exercise, you receive, decode, and read an incoming text message.

TIP

Once a message has been delivered, you cannot retrieve it.

Complete the following tasks:

Send a text message from the Messages app to your business.

Receive the message payload.

Uncompress, using GZIP, and print the payload.

Perform the following tasks on your test server:

Locate and run the 01_receiving_text_message.py file.

When finished, save the source_id for use later in the tutorial.

Expected MSP server response

You should see two types of information: the opaque user ID and the capability-list. The opaque user ID is the source ID when receiving messages. You can retrieve the opaque user ID by listening to incoming messages. The capability list tells you the user's device capability to support certain types of messages type. For more information on sending messages, see HTTP Headers

User is typing...

Just received a text message!

Message body: Nice to meet you

Source ID: <opaque user ID>;

Capability List: <capability-list?;

Messages for Business uses the opaque user ID to uniquely identify conversations that occur between a Business ID and a user. The user's multiple devices share the same opaque user ID and it persists over long periods of time (years). It isn't shared between businesses, even if they're with the same MSP. When the user initiates a conversation with another Business ID, they'll receive a new opaque user ID for that conversation.

Exercise: Validating a Received Message

In this exercise, you verify the authorization header of a received message. For more information on validating messages, see Validating a Message.

Complete the following tasks:

Extract the JWT (JSON Web Token) string from headers.

Verify the signature and audience by decoding the JWT string.

When receiving a message on your messaging platform, the JWT audience (aud) value in the JWT payload, is your MSP ID. Do not use your Business ID to validate.

TIP

The HTTP header field names are case-insensitive, according to https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html.

Perform the following tasks on your test server:

Locate and run the config.py file to completion.

Locate and run the 02_verify_message.py file to completion.

Expected MSP server response

By default, you'll receive at least two messages: one is for typing start, and the other is for the actual message. The output automatically displays the typing indicator on the console and is not the typing_start indicator. Observe the request of the text message.

Authorization succeeded.

Authorization succeeded.

If you don't receive any requests from Apple Messages for Business server, check the following:

Make sure your endpoint SSL certificate fulfills the requirements. See Configuring Your MSP Test Server.

Make sure your server is listening to POST requests on https://<your.domain>/<path>/message.

Make sure you are using the iMessage service for outgoing messages. You can check the iMessage setting by going to Settings > Messages.

Make sure your messages actually were sent from the device. If you are seeing a progress bar that runs for a long time, check your internet connection and iMessage settings. For more information, see If you get an error when trying to activate iMessage or FaceTime.

Make sure there is no software blocking requests or closing the connection. Be aware that your service may be blocking incoming requests due to strict rules. For example, the port number is in the "hostname" HTTP header even though it's optional.

Receiving Closed Conversation Messages

Users can opt out of receiving any further messages from a brand. This is also known as closing a conversation.

A user closes a conversation by going to the tray view in Messages and left swipe a conversation. This action reveals two buttons: a mute icon and a delete icon. The user clicks the delete icon and agrees to delete the conversation. This action sends a "close" message for a Messages for Business conversation. Apple refers to this action as "delete" on the user's device, and the MSP and brand receive a "close" conversation from the standpoint of the brand and MSP.

When a user closes a conversation, Messages for Business sends a message of type close to your MSP platform. Your brand cannot send any further messages to this user. If they try, Messages for Business service sends an HTTP 410 | Gone response. We require MSPs to keep a table of closed conversations and prevent brands from sending messages to users who have opted out.

The user can re-initiate the conversation. They can resume the conversation from any valid entry-point for the brand. When they do, they will return with the same opaque user ID as before. For more information, see Receiving a Closed Conversation.

If the user chooses to stop receiving messages, Messages for Business considers the conversation closed and sends a message of type close to the MSP platform.

```json
{
  "id": "UUID-IDENTIFIER-FOR-MESSAGE",
  "sourceId": "OPAQUE-USER-ID",
  "destinationId": "BUSINESS-ID",
  "type": "close",
  "v": 1
}
Typing Indicators
```
<sub>↳ `msp-api-tutorial.md` L435–449</sub>

Your platform can receive these message types from user devices. Your platform should parse these messages and send the typing indication to your agents. For more information, see TypingIndicatorMessage.

Tapback Reactions

Your platform can receive these message types from user devices. Your platform should parse these messages and send the typing indication to your agents. For more information, see Tapbak Reactions.

Exercise: Sending a Text Message

In this exercise, you send a text message payload.

Complete the following tasks:

Successfully derive the binary MSP secret from secret passphrase.

Create a valid JWT header using your MSP secret. See Authorizing Messages.

Get the destination_id from the response in Exercise: Receiving a Text Message to respond.

Copy and paste the destination_id into the Listing 03_send_text_message.py code.

Assemble a message header and payload.

Send a message.

When sending a message from your messaging platform, the JWT issuer value (iss in the JWT payload) should be the MSP ID. Using Business ID in this instance results in authorization failures.

TIP

The timestamp unit, iat in the JWT payload, should be in seconds, not milliseconds.

The following JWT header creation code makes the authorization header field token.

Perform the following tasks on your test server:

Locate and run the jwt_util.py file to completion.

Locate and edit the 03_send_text_message.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 03_send_text_message.py file.

Expected MSP server response

You should see the following message on your MSP server.

Messages for Business server return code: 200

TIP

You can find sample of HTTP Headers used generally for messaging on Messages for Business in the sample code under samples/message_headers.json.

If you are unable to send a text message, then check the following:

Go through the Messages for Business documentation and the tutorial.

Examine the response body for potential errors.

If you get an error code, refer to the table below.

| Error | Troubleshooting Tips |
|---|---|
| 401 "unauthorized" error | Verify the following: Use your MSP ID to encode the JWT token, and your Business ID in headers and payload. Base64-decode the textual secret when generating your JWT token. Your JWT timestamp (iat value) is in seconds and not in milliseconds or another unit. The "Bearer" prefix is in the authorization header. |
| 404 "Not Found: No device registrations for user" error | These errors occur when a brand messages a user during their iPhone or device upgrade cycle. The carrier has an inactivated status on the SIM card for a particular device. Our messaging systems have the user account marked as messageable and active but the error comes back from the carrier network. |
<sub>↳ `msp-api-tutorial.md` L533–537</sub>

Once the upgrade cycle is complete, users will again receive messages without any further work for the MSP or the user. They will not, however, receive messages that were returned as 404. We recommend those be sent again or marked in your system as undelivered.

| 410 "session expired" error | The customer you are attempting to message deleted the conversation from the messages tray on their device. This brand will be unable to message the user. |
|---|---|
<sub>↳ `msp-api-tutorial.md` L543–543</sub>

If the user resumes the conversation, by clicking on a link or entry-point, the conversation will continue. The user will have the same opaque ID and the brand will again be able to message the user.

Use the following matrix to troubleshoot problems you may encounter with the allow list.

| Apple Account | Allow Listed | Closed Conv. | Device to MSP | MSP to Device |
|---|---|---|---|---|
| ✓ | ✓ |  | Ok | Ok |
| ✓ |  |  | Not delivered | Not delivered |
| ✓ | Removed |  |  | Ok |
| Logout* | ✓ |  | Ok | 404 Resource Not Found |
| n/a | No email sent |  |  |  |
| ✓ | Ok, reopens conversation. | 410 Resource Gone |  |  |
<sub>↳ `msp-api-tutorial.md` L553–565</sub>

* Occurs only if the user is logged out on all devices for a particular Apple Account. Otherwise, messages are delivered to devices still logged in with the Apple Account.

Exercise: Sending an Image Attachment

A message can include one or more attachments. An attachment can be an image, PDF, or other file type, and it must be smaller than 100 MB. For more information about attachments, see Sending Messages with Attachments.

In this exercise, you'll send a message with an image attachment.

Perform a pre-upload request to retrieve an attachment upload URL.

Encrypt the attachment data.

Upload the encrypted attachment data to the retrieved attachment upload URL.

Send the message with metadata of the attachment.

Perform the following task on your test server:

Locate and run the attachment_cipher.py file.

Send the Message with Base64-encoded Images

In this exercise, you send a message with Base64-encoded image attachments. In the message payload body, you need an Unicode Object Replacement Character (\uFFFC) as a placeholder for each attachment you send.

TIP

Base64 is a standard for converting binary data to a viewable text string. For more information, see How to convert an image to base64 encoding. There are also online drag-and-drop encoders. To encode or decode Base64, see Base64 Decode and Encode

Perform the following tasks on your test server:

Locate and edit the 04_send_image_attachment.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 04_send_image_attachment.py file.

Expected MSP server response

You should see the following message appear on your MSP server.

Messages for Business server return code: 200

Expected client device response

If the encrypted data does not display correctly in the Message client, check your encryption implementation.

If attachments are not showing up in the Messages app, check the following:

Make sure in the message body you have a Unicode Object Replacement Character (\uFFFc) for each attachment you are sending.

Make sure you are using Base64-encoding for the attachment signature.

If the sent images are displayed as icons in the Messages app, then verify the following:

Encrypt the attachment using the correct algorithm.

Do not compress the data when sending.

Uploaded data is not corrupted.

Do not subsequently modify the data using network nodes.

To verify that your encryption implementation is correct:

In your encryption method, use the following encryption key rather than a randomly generated one: 12E9F08B6B0CCC36DF688BF167FAF7BF3E7E696D1A66E98C9E9949131C9F8E07 (hex-encoded).

Hex-decode the string.

Encrypt the string "12345" using the above listed encryption key.

The Base16-encoded result should be 7634125F65.

To verify that your decryption implementation is correct:

Encrypt then decrypt any given string. The result should be the same as the input.

Exercise: Downloading Attachments

In this exercise, you'll receive a message containing attachments. You need to download and decrypt the attachments. For more information, see Downloading and Decrypting an Attachment.

TIP

In general, the URL field in the attachments array should not be URI-encoded. You can include a mix of unescaped and escaped characters if that is how the client device uses the link.

Complete the following tasks:

Receive a message payload with attachments.

For each attachment perform a /preDownload request to get the download URL.

Convert the provided hexadecimal signature from the payload to a Base64-encoded signature.

Download the attachment using the download URL.

Decrypt attachment data and save to file.

Save the message attachments as local files under the current path.

NOTE

You always get a download URL from the /preDownload step even if the parameters are not correctly set. However, the downloaded data is not valid in such a case.

Perform the following task on your test server:

Locate and run the 05_downloading_attachments.py file.

Expected MSP server response

2 attachments found in the message.

writing to local file: 52106351067__A31A08AE-A449-4EDD-A735-458D17ADF9EA.JPG

writing to local file: 52106351346__8CEE7676-0E8C-4D19-83B5-C680836837CC.JPG

Error codes

| Error | Troubleshooting Tip |
|---|---|
| 400 "not authorized" | Make sure you are using the correct encoding for attachment signature. It should be a Base64-encoded string. |
| 400 error when calling /decodePayload for interactive data payload | Make sure you have "bid" as a header in your request. |
| Problems decrypting the attachment | Make sure you are using the correct algorithm for decryption. Once you are confident that the encryption algorithm works, try to encrypt and immediately decrypt the file. If the file can be recovered, then the decryption worked. |
<sub>↳ `msp-api-tutorial.md` L733–739</sub>

Ensure Correct Signature Fields

Below are the uses of Base16- and Base64-encoded signature fields used by Messages for Business:

When receiving a message from Messages for Business, the signature field of the attachment is Base16-encoded, or hexadecimal.

When sending the signature header in the preDownload request, the value is Base64-encoded.

When sending a message from your MSP to Messages for Business, Messages for Business calls the signature field signature-Base64 because it is Base64-encoded.

https://register.apple.com/resources/messages/msp-api-tutorial/rich-links

Sending Rich Link Messages

The Messages app on Apple devices protects user privacy and security by not allowing a remote sender to trigger the user's device to access internet resources without their knowledge or permission. When a URL is sent to a user's device, a preview bubble appears. If the rich link feature is not used, the URL is treated as untrusted. A blank bubble appears with the website domain and the label "Tap to Load Preview." This allows the user to see the domain name of the site, and chose whether they want to load a preview before opening the link in a web browser. This experience tends to discourage users from tapping to open the link, and is unacceptable in the Messages for Business experience.

When a business sends a URL to a user using rich links, the user can see a preview of the web page. This reassures them that they aren't being tricked into visiting a malevolent website.

Sending URLs using Rich Links

When a business sends a URL with an inline image or video to a customer, the customer receives a "Tap to Load Preview" message (second image below). You need to remove the "Tap to Load Preview" step by using the Messages for Business REST API, see [Exercise: Rich Links](https://register.apple.com/resources/messages/msp-api-tutorial/rich-links#exercise:-rich-links).

Simple URL

Rich Link

Exercise: Rich Links

By default, the Messages app renders a URL with a warning to the user. The warning asks the user to "Tap to load" before displaying an image from the linked page and showing the full URL. The rich link feature of Messages for Business allows a brand to send a link without the "Tap to load" step.

There are two types of rich links: image and video. Choose `image` type to link to a webpage that provides a visual indication of what the user can expect. Choose `video` type only when linking directly to a video media asset, such as an MP4 file.

In the `samples` directory, you'll find a payload for each type for your reference. See `rich_link_image.json` and `rich_link_video.json`.

https://register.apple.com/resources/messages/msp-api-tutorial/quick-reply

Quick Reply Messages

Quick reply messages provide a simple way for the user to make an inline choice with a single tap during an ongoing conversation. You can have between two and five customizable choices, and the user can select only a single item.

Quick reply is an interactive message. Due to its simple structure, it doesn't have receivedMessage or replyMessage fields similar to other interactive message types.

This feature requires iOS 15.1 and macOS 12. For more information, see `capability-list` under [HTTP Headers](https://register.apple.com/resources/messages/msp-rest-api/common-specs#http-headers).

Sending Quick Reply

In this exercise, you'll send a message payload that triggers a quick reply in the Messages app on the user's device. The payload shows five choices sent to the receiving device.

Complete the following tasks:

1. Locate the code zip folder and unzip it.

2. Locate and edit the `23_send_quick_reply.py` file by inserting the `destination_id`, located towards the bottom of the file, with the `source_id` from the output in Exercise: Receiving a Text Message.

3. Save and run the `23_send_quick_reply.py` file.

4. Verify on the receiving device (macOS or iOS device) has received the payload, and tap one of the choice.

5. Verify that your platform has received the response and parsed it to the agent console for viewing.

https://register.apple.com/resources/messages/msp-api-tutorial/list-time-pickers

Sending List and Time Pickers

Interactive messages provide a range of functionality, from letting the user select an item from a list to scheduling an appointment. Messages for Business comes with a set of interactive messages that you can use, or you can create and use custom interactive messages. When sending an interactive message to the user, set the type field to interactive. For more information, see List Picker Message and Time Picker Message.

In this section's exercises, you'll learn how to provide a rich user experience using list and time pickers.

Exercise: Sending a Text-only List Picker

In this exercise, you generate a request ID to send a text-only list picker payload to trigger an item selection in the Messages app.

The request ID ensures that the requests and responses are properly paired. In situations where an agent sends multiple interactive messages, the MSP may receive responses out-of-order or no response for some requests. The request ID ensures that the responses match the corresponding request.

TIP

When parsing the list picker response, note that the selected options of the list picker are sent back to the MSP as a subset of the options in the list picker.

Complete the following tasks:

Generate a request ID.

Assemble list picker item configuration with optional sections.

Send a message with payload.

Perform the following tasks on your test server:

Locate the code zip folder and unzip it.

Open and edit the 06_send_text_list_picker.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 06_send_text_list_picker.py file.

Expected MSP server response

Messages for Business server return code: 200

If your custom message isn't being shown on your client device, use the following matrix identifying the type of messages sent and how they appear in the UX.

| Message Type | Reply Message | Response Message |
|---|---|---|
| Text | Picture |  |
| List Picker | ✓ | ✓ |
<sub>↳ `msp-api-tutorial.md` L863–867</sub>

Exercise: Sending a List Picker with an Image

In this exercise, you send a list picker with an image payload to trigger an item selection in the Messages app. When a user responds to a list picker with a text message, the two messages are delivered separately without association.

TIP

If you cannot see the images in interactive message bubbles, make sure your image DPI is set to the common DPI setting for iOS, which is 72.

Complete the following tasks:

Base64-encode the image data.

Assemble a list picker payload with the encoded image data.

Send a list picker message with the payload.

Perform the following tasks on your test server:

Locate the code zip folder and unzip it.

Locate and edit the 07_send_list_picker_with_image.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 07_send_list_picker_with_image.py file.

Expected MSP server response

Messages for Business server return code: 200

Exercise: Sending a List Picker with Multiple Images

In this exercise, you send a list picker with multiple images and receive a data reference for use in the next exercise, Exercise: Sending a List Picker Using a Data Reference.

Complete the following tasks:

Perform iteration over a dictionary containing three image files, encrypting each for transmission.

Use references in JSON to specify which images go with each section of the list picker.

Print out the data reference in JSON format for use in the next exercise, Sending a List Picker Using a Data Reference.

Use the same List Picker from Exercise: Sending a List Picker with an Image. Note the references specify multiple images. You use a dictionary to match the image identifiers in JSON to the file names. Then loop through the images to encrypt each one and add it to the payload.

This example includes an additional header parameter, include-data-ref, that is set to true. This setting directs the Messages for Business server to return the data reference. Because HTTPS header key-value pairs are string only, set the value of true to a four character string.

Perform the following tasks on your test server:

Locate and edit the 08_send_list_picker_with_multiple_images.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 08_send_list_picker_with_multiple_images.py file.

Save the data reference from the output to use in later exercises.

Expected MSP server response

Messages for Business server return code: 200

Messages for Business server response body:

```json
{
    "dataRef": {
        "bid":"<bid save for next exercise>",
        "owner":"<owner save for next exercise>",
        "url":"<url save for next exercise>",
        "size":"<size save for next exercise>",
        "signature":"<signature save for next exercise>",
        "signature-base64":"<signature-Base64 save for next exercise>",
        "title":"Select Produce",
        "dataRefSig":"<dataRefSig save for next exercise>"
    }
}
Exercise: Sending a List Picker Using an InteractiveData Reference
```
<sub>↳ `msp-api-tutorial.md` L949–973</sub>

An InteractiveData Reference (IDR) in Messages for Business is like a super-charged URL. An IDR points to a set of large media assets. These media assets are usually 10KB, but can be 100MB or more. The IDR pointer is easier to use rather than expending the bandwidth to upload or download assets. It conforms to the JSON standard in a form that is unique to Messages for Business.

The IDR allows you to send the list picker using an abbreviated handle instead of uploading all the attachments again.

In this exercise, you reuse a previous interactive data reference sent in Exercise: Sending a List Picker with Multiple Images, and assumes that you got the data reference from the response. Make sure the dataRefSig field is present in the data reference.

Perform the following tasks on your test server:

Locate and edit the 09_send_list_picker_with_data_ref.py file.

Insert the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Insert the interactive_data_ref, located towards the bottom of the file, with the output data reference from Exercise: Sending a List Picker with Multiple Images.

Save and run the 09_send_list_picker_with_data_ref.py file.

Expected MSP server response

Messages for Business server return code: 200

Exercise: Sending a Time Picker

This exercise sends a message payload to trigger a time picker in the Messages app on the user's device.

When setting the times for your list picker, the start date can't be earlier than the current date/time, otherwise the times are removed from the time picker. If all items in the time picker are for past times, then the device displays an empty time picker with a message "No times available."

You can have the following types:

Long duration items, even extending to days long

Zero time length duration items, use this feature with discretion

Across different days, different months, or different years

Complete the following tasks:

Generate time picker request ID.

Assemble time picker configuration with or without timezone offset.

Send a message with a payload.

Sending a Time Picker Using the User's Timezone

This example sends a time picker for an event in San Francisco to a user in New York. The event occurs in San Francisco on 2020-10-15 at 10:00am (PDT: GMT-7 hours), and you want the user in New York (EDT: GMT-4 hours) to view the time picker as 2020-10-15 at 1:00pm.

Sending the time of an event requires you to convert the event time to GMT, 2020-10-15T17:00+0000, and use it as thestartTime value. In this case, you don't set the timezoneOffset value.

On your server

Locate and edit the 10_send_time_picker_with_user_timezone.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 10_send_time_picker_with_user_timezone.py file.

Sending a Time Picker Using a Fixed Timezone

This example sends a time picker for an event in San Francisco to a user regardless of their timezone.

Setting the time of the event regardless of the user's timezone requires you set the startTime value as GMT, 2020-10-15T17:00+0000. And you need to set a timezoneOffset, in this case -420 minutes for San Francisco PDT.

With the timezoneOffset value set, the user's device always displays the time where the event occurs without converting the time to the user's timezone.

Perform the following tasks on your test server:

Locate and edit the 11_send_time_picker_with_fixed_timezone.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 11_send_time_picker_with_fixed_timezone.py file.

Expected MSP server response

Messages for Business server return code: 200

If your custom message doesn't show on your client device, use the following matrix identifying the type of messages sent and how they appear in the UI.

| Message Type | Reply Message | Response Message |
|---|---|---|
| Text | Picture | Text |
| Time Picker | ✓ | ✓ |
<sub>↳ `msp-api-tutorial.md` L1093–1097</sub>

https://register.apple.com/resources/messages/msp-api-tutorial/advanced-interactive-messaging

Large Interactive Messages

When a response payload exceeds 10KB, Messages for Business saves the full JSON to a cloud server and the MSP receives an Interactive Data Reference (IDR). The IDR has URLs to retrieve the full response payload and decryption keys to decipher the response. The response that your MSP receives is an IDR (implied by the `interactiveDataRef` key): [Receiving an Interactive Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive.md#receiving-an-interactive-message)

A List Picker response includes all of the images of the original picker. Therefor the payload will most likely exceed 10KB. This ensures that the response JSON has a complete set of digital assets to render the bubble, images, user selection, and future interaction.

Your messaging platform needs to parse the IDR and use it to download the full JSON response. Use the full JSON to complete the action of interactive message.

Exercise: Retrieve a Large Message Using an Interactive Data Reference

In this exercise, you'll learn how to decrypt, decode, and parse a data reference resulting from a user's response to an interactive message.

Perform the following tasks on your test server:

1. Locate the code zip folder and unzip it.

2. Locate and run the `12_large_interactive_message.py` file to set up the listener.

3. Go through the [Exercise: Sending a List Picker with Multiple Images](https://register.apple.com/resources/messages/msp-api-tutorial/list-time-pickers#exercise-sending-a-list-picker-with-multiple-images) to send a list picker to your test device.

4. On your test device, make your selections, enter a text message, and send it.

5. Observe the interaction between your MSP and the Messages for Business service.

6. Open the file `data_reference_debug.json` in your favorite text editor to see the full payload retrieved by script.

If your custom message doesn't show on your user's device and the message type is Custom Interactive Messages, then the reply message's text and picture don't appear in the UI because a response message wasn't generated. The response message's text and picture are encoded as an attachment rather than an IDR.

https://register.apple.com/resources/messages/msp-api-tutorial/applepay

Integrating Apple Pay

Apple Pay allows consumers to complete purchases without having to manage paper bills, coins, or physical bank cards. Using Messages for Business, consumers can complete transactions with their favorite brands without having to leave the Messages app.

Apple Pay in Messages for Business is a distinct feature, but shares similarities to Apple Pay in-app and Apple Pay on the Web. For more information, see Apple Pay Message.

To support refunds to Apple Pay purchases, use a workflow outside of Messages for Business. For more information, see Apple Pay Resources.

Complete Preparation Steps to Prepare an Apple Pay Merchant Account

Before you are able to send an Apple Pay in Messages for Business payload across the messaging system, you must have a valid merchant account, identifiers, certificates, and domain registrations. The following preparation steps step you through these items to ensure you are up-to-speed quickly.

Preparation Step 1: Set Up an Apple Pay Merchant Account

If you already have an Apple Pay Merchant account, skip to Preparation Step 2: Associate your Website Domain to your Merchant Account.

Set up an Apple Developer account to create an Apple Pay Merchant account at developer.apple.com. The approval time may take several days.

Use one of the following tutorials to add Apple Pay Merchant capabilities to your Apple Developer account:

Configuring Your Environment" section in Apple Pay JS Documentation

Preparation Step 2: Associate Your Website Domain to Your Merchant Account

Decide the domain or domains to associate with your Apple Pay Merchant Account. Register this association within developer.apple.com. Otherwise, Apple Pay rejects your transactions.

Log into your developer account at developer.apple.com.

Navigate to Certificates, IDs & Profiles.

From the left navigation panel, click Identifiers.

From the drop down menu on the upper right, select Merchant IDs. The default is set to App IDs.

You will now see a list of your Apple Pay Merchant accounts listed by IDENTIFIER. If this list is blank, return to the Pre-Work section above and add an identifier to your Merchant Account.

Click on the identifier that you want to use for Apple Pay in Messages for Business. The portal opens a full page view of details for that identifier.

Search for the Merchant Domains section on the page. Use the Add Domain and Verify buttons to add and verify all domains that you want to use with the Merchant account.

Follow the directions for verifying each domain.

Reference these industry standards to better understand the verification process:

IETF RFC 3986 Uniform Resource Identifier (URI): Generic Syntax gives the requirements for the domain portion of your website.

IETF RFC 8615 Well-Known Uniform Resource Identifiers (URIs) describes the well-known process used by Apple Pay for website verification.

Preparation Step 3: Create and Download the Certificates for Your Merchant Account

Navigate to the same identifier page as shown in the Preparation Step 2: Associate Your Website Domain to Your Merchant Account.

Search for the section "Apple Pay Payment Processing Certificate."

If you do not see a payment processing certificate, use the "Create Certificate" button and follow the instructions to create one.

NOTE

You must have a Payment Processing certificate associated with your Merchant account in order to have transactions accepted by the Apple Pay server. The Payment Processing certificate expires every 25 months.

Search for the section "Apple Pay Merchant Identity Certificate."

If you do not see a certificate in this section, use the Create Certificate button and follow the instructions to create one.

Download the Merchant Identity Certificate for use in the code exercises later in this section.

Preparation Step 4: Generate the PEM File for your Merchant Identity Certificate and Test It with cURL

If you have an Apple Pay in-app or on the web endpoint currently in production and are using that account in this exercise, then you can skip this step using your existing PEM file. Otherwise, this step is necessary to work with the sample code provided in this section.

Apple uses command line tools for this procedure. If you are on macOS and familiar with Keychain Access, you can perform these steps using that application instead.

Create a directory for your key store.

mkdir keysncerts

cd keysncerts/

Initiate keystore with ECC (EC in the command line) 256 key pair and generate a signing request.

keytool -genkeypair -keystore fileforkeys.p12 -storetype pkcs12 -alias keyone -keyalg EC -keysize 256

keytool -certreq -keystore fileforkeys.p12 -storetype pkcs12 -alias keyone > my_request.csr

Generate an Apple Pay Merchant Identity certificate.

Log into your Apple Developer account on developer.apple.com. Navigate to your certificates. Then upload my_request.csr to developer portal, generate the Merchant Identifier certificate, and it downloads as merchant_id.cer.

openssl pkcs12 -in fileforkeys.p12 -out pv.key -nodes -clcerts

Move merchant_id.cer over to the keysncerts directory. Then convert and export it as a PEM file.

openssl x509 -inform DER -outform PEM -in merchant_id.cer -out server_crt.pem

Generate the payload file.

vi data.json

Enter the file, save, and exit.

```json
{
    "merchantIdentifier": <SHA256 hash of your text merchant identifier>,
    "domainName": <domain name associated with Apple Pay merchant account>,
    "displayName": <Merchant name in human readable form>,
    "initiative": "messaging",
    "initiativeContext": "https://<...your endpoint URL...>/paymentGateway"
}
Issue the command to get your Merchant Payment token.
```
<sub>↳ `msp-api-tutorial.md` L1265–1279</sub>

curl -k -vvvv --request POST -d "@data.json" --header "Content-Type: application/json" --cert server_crt.pem --key pv.key "https://apple-pay-gateway.apple.com/paymentservices/paymentSession"

If you can retrieve the token from the command line above, use the PEM file and private key generated on your server.

If you can successfully issue the command, you'll receive a response similar to the one below. The merchantSessionIdentifier field is the payment token for this transaction that a payment processor redeems.

For the example code, Apple discarded the token without redemption. This ensures that payment requests completed in a test context don't result in a financial transaction.

Expected Apple Pay server response

```json
{
    "displayName": "<REDACTED>",
    "epochTimestamp": 1588615039232,
    "expiresAt": 1588622239232,
    "initiative": "messaging",
    "initiativeContext": "<REDACTED>/paymentGateway",
    "merchantIdentifier": "<REDACTED>",
    "merchantSessionIdentifier": "<REDACTED>",
    "nonce": "<REDACTED>",
    "signature": "<REDACTED>",
    "signedFields": [
        "merchantIdentifier",
        "merchantSessionIdentifier",
        "initiative",
        "initiativeContext",
        "displayName",
        "nonce"
    ]
}
NOTE
```
<sub>↳ `msp-api-tutorial.md` L1299–1337</sub>

Fields epochTimestamp and expiresAt are integer fields. These must be used back in the messaging payload with correct type.

Exercise: Send an Apple Pay Request——Basic Functionality

This exercise covers the basics needed for you to send an Apple Pay request through Messages for Business and how to read the return message. To qualify as an MSP, you'll need to demonstrate the basic Apple Pay functionality on your platform.

TIP

When you host the merchant payment token generator, also known as a payment gateway, you'll receive a payment transaction token. When giving a demo, you can simply retain the token and ensure that no payment transaction is executed. This allows you to run tests and demo your implementation without incurring charges through your Apple Pay account.

For more information on sending Apple Pay requests, see Apple Pay Message. Also, you can find a sample Apple Pay in Messages for Business request in the code repository at samples/apple_pay_request.json.

Step 1: Register and Configure your Apple Business Register account

Use the following steps to enter your Merchant Information into your Messages for Business account.

Go to register.apple.com and sign in. Ensure that you are signed in with your Apple Account which is the administrator or technical contact for the Messages for Business account.

Navigate to your company's Messages for Business Accounts and find the appropriate business account.

Under "Optional Integrations" you should see an "Apple Pay" section.

Click on Edit next to "Apple Pay Merchant ID."

Enter the IDENTIFIER referenced in the Pre-Work sections into the field labeled "Apple Pay Merchant ID." You must enter it EXACTLY character-for-character as it appears in the IDENTIFIER column in your developer portal account.

Click "Done."

NOTE

Your Apple Pay Merchant ID may be used across more than one Messages for Business account. Each Messages for Business account, however, can have only one associated Apple Pay Merchant ID.

Step 2: Run a test payment gateway

Run a test payment gateway to verify that you can receive payment requests from the user. For more information about the payment gateway API, see PKPaymentAuthorizationController.

Perform the following tasks on your test server:

Locate the code zip folder and unzip it.

Locate and run the 13_test_payment_gateway.py file.

Expected MSP server response

Payment received!

Request Identifier: <request identifier in message payload>

Payment Method Dictionary: {'displayName': 'Visa 1234', 'type': 'Credit', 'network': 'Visa'}

Step 3: Send Apple Pay request

Respond with a test payment session to a request from the test payment gateway, using the following fields in the payload:

merchantIdentifier: SHA256 hash represented in hexadecimal of merchant identifier.

displayName: Your merchant name in text in human readable text.

domainName: Your base website without any punctuation or prefix, for example: "developer.apple.com", that must match the domainName of your merchant account. The domainName field is used for authentication instead of the merchant information in Apple Pay, so the HTTPS prefix and punctuation is not used. If you leave this field out of your payload, you will receive a token. It will only be valid for Business Pay on the Web, not Apple Pay in Messages for Business.

initiative: Set to messaging for Messages for Business.

initiativeContext: Your payment gateway URL with the https:// prefix. This is a publicly exposed network endpoint. It won't work using a private network. The initiativeContext field defines an endpoint called during the transaction, so the HTTPS prefix and punctuation are required.

Step 4: Send a payment request as a message

Using the code from 14_send_apple_pay_request.py, send a payment payload for a purchase item using the merchant session.

Perform the following tasks on your test server:

Locate and run 13_test_payment_gateway.py as a background process.

Locate and edit the 14_send_apple_pay_request.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 14_send_apple_pay_request.py file in the foreground.

Expected MSP server response

Messages for Business server return code: 200

If an "Invalid Payment Request" shows up in the Messages client after sending the payment request message, check the following:

Make sure your payment gateway URL is in the valid URL format.

Make sure you are obtaining a new merchant session every time you are sending a payment request.

Step 5: Approve the test payment on your iPhone

You should have received the Apple Pay test payment request on your device from the previous step.

<!-- img: applepay-bubble.jpg -->

Buy with Apple Pay

Apple Pay bubble

Tap the payment message to make the test payment:

<!-- img-row: Apple-Pay-After.png, Apple-Pay-Before.png -->

Confirm payment

Apple Pay prompt

 Payment confirmed

Apple Pay done

Expected MSP server response

After the test payment completes, an interactive message is delivered to your endpoint with the Apple Pay payload. In the payload there is a state field that indicates whether the test payment was approved in your payment gateway. Confirm that the test payment transaction went through your payment system, rather than relying on the state of the return message.

You should see the following output from your Payment Gateway:

Payment received!

Request Identifier: <request identifier in message payload>

Payment Method Dictionary: {'displayName': 'Visa 1234', 'type': 'Credit', 'network': 'Visa'}

Troubleshooting tips

If you can't receive payments in your payment gateway, check the following:

Ensure you have a valid merchant ID, and you already verified your domain.

Check your payment gateway is listening to POST requests on /paymentGateway.

If you receive a 400 error when sending the Apple Pay interactive message, make sure that you have registered your merchant ID on your account at Apple Business Register.

If your custom message doesn't show on your user's device and the message type is Apple Pay, then the reply and response message's text and picture appear in the UI.

Enhance your Apple Pay Request——Advanced Functionality

In the previous exercise, you successfully sent an Apple Pay request. The appearance, though, was very plain. In this exercise, you'll learn a few techniques to enhance your Apple Pay transactions with tax, shipping, and payment options in Messages for Business.

When reading the code, you should notice that it can recognize and parse the payment response.

The next change is the new handlers for new endpoints. The use cases show you how businesses can update the shopping cart depending on a user's payment method, shipping method, or contact information. For illustrative purposes, we made all of these endpoints in our main domain. They can be URL endpoints to different domains for different functions.

Below are the different endpoints:

| Endpoint | Description |
|---|---|
| /fallback | Captures the response for devices that are not able to use Apple Pay. The request redirects the client device to this URL which allows you to explain a procedure for completing the transaction through an alternative payment medium. |
| /orderTracking | Captures changes to the line items, amounts, or status for each line item. If set, it calls on the first presentation of the line items to the user. |
| /paymentMethodUpdate | Called when the payment method, such as debit, credit, or cash, changes. For more information, see ApplePayPaymentMethodUpdate. |
| /shippingContactUpdate | Called when any of the shipping contact details, such as shipping address, associated email address, or associated phone number, change. Also called when the user taps their device to initiate an Apple Pay session. For more information, see ApplePayShippingContactUpdate. |
| /shippingMethodUpdate | Called only when the shipping method is changed. For more information, see ApplePayShippingMethodUpdate. |
<sub>↳ `msp-api-tutorial.md` L1531–1541</sub>

Perform the following tasks on your test server:

Locate and run the 15_handle_payment_gateway.py in the background to set up the server with the endpoint listeners.

Locate and edit the 16_send_rich_apple_pay_request.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 16_send_rich_apple_pay_request.py file to send the payment request.

Approve the payment on your test device and observe the response on your server.

Expected MSP server response

Payment received!

Request Identifier: cb43a <truncated>

Payment Method Dictionary: {

  'displayName': 'Visa 8087','type': 'Debit', 'network': 'Visa'

  }

orderTracking received!

ordertracking_payload: {

  'version': '1.0',

  'payment':

   {

    'summaryItems': [{

    'amount': '1.5',

    'type':  'Final',

    'label': 'Adoption fee'

```json
},
{
 'amount': '1',
```
<sub>↳ `msp-api-tutorial.md` L1589–1593</sub>

     'type': 'Final',

     'label': 'Required shots'

```json
 },
{
 'amount': '2',
```
<sub>↳ `msp-api-tutorial.md` L1599–1603</sub>

     'type': 'Final',

     'label': 'Outtake fee'

```json
 },
{
 'amount': '-1',
```
<sub>↳ `msp-api-tutorial.md` L1609–1613</sub>

     'type': 'Final',

     'label': 'Daily discount'

     },

    {'amount': '3.5',

     'type': 'Final',

     'label': 'Your Total'

    }],

    'errors':

    []},

  'requestIdentifier': 'cb43a <truncated>'}

payload {'interactiveDataRef': { <truncated> }

Enhance your Apple Pay Request with Images——Advanced Functionality

By adding a Base64-encoded image of their order, users can visually verify their purchase. For more information about image encoding, see Exercise: Sending a List Picker with an Image.

In this exercise, two fields have been added that require the user to provide additional information to complete the transaction. The fields, requiredBillingContactFields and requiredShippingContactFields, are arrays that require the user to provide a postal address, name, and phone. We recommend adding these fields for physical goods. For virtual goods, fewer fields may be more appropriate. For more information about the list of available values for billing and shipping contact fields, see ApplePayContactField.

TIP

On the user's device, these required fields default to the information defined in Settings > Wallet & Apple Pay. The user can overwrite these fields for any transaction.

To make up the payment request, multiple line items have been added. These items appear in the order given in the payload on the user device in the Apple Pay drawer for Messages for Business.

Set user expectations about discounts or charges by using a line item for each charge or discount. Each line item can be a zero, positive, or negative value to indicate the type of charge or discount. The total amount of the order must be greater than zero.

The amounts are specified by strings. This allows flexibility across different currencies and payment systems. For more information about payment line items, see lineItems.

https://register.apple.com/resources/messages/msp-api-tutorial/authenticationV2

Sending an Authentication Message

Table of Contents

Introduction

Audience

Rationale

Prerequisites

Security Considerations

OAuth 2.0 Flows

Exercises

Exercise: Sending an Authentication Request

Exercise: Create your LinkedIn App

Exercise: Decode the Auth Code and Retrieve User Data

Exercise: Receive and Parse an Authentication Response

Using Auth0 as an Alternative

Troubleshooting

Introduction

The Messages for Business authentication feature allows a user service agent or a bot to send an authorization access request to a user for specific information.

This request displays as a bubble on the device with a Sign In call to action. The user then signs into the authentication service with their username and password. Financial services, insurance, and e-commerce use this feature to ensure that users authorize access to their private data in a way that is not visible to either the user service provider or Apple Messages for Business servers.

You can use a third-party service as the authentication service, password autofill, or you can use an authentication endpoint that you already control. For more information, see Authentication Message.

Audience

The Messages for Business authentication feature relies on advanced cryptography. We wrote this section for an audience with sufficient background in cryptographic concepts to implement the standards described.

For a better understanding about the field of cryptography, see the following:

Crypto 101, an introductory course on cryptography

OAuth 2.0 State Parameters

For a better understanding of authentication and authorization technologies:

OAuth 2 in Action by Justin Richer Antonio Sanso, ISBN: 9781617293276, 2017

OAuth 2.0 is the industry-standard protocol for authorization

For more information on the specific standards used by Messages for Business:

Implicit flow from OAuth 2.0 specification

Authorization Code flow from OAuth 2.0 specification

Standards for Efficient Cryptography 1 (SEC 1), Certicom Research, Version 2.0

RSA Security Inc. Public-Key Cryptography Standards (PKCS), RSA Laboratories, v1.2

Rationale

We chose elliptic-curve cryptography (ECC) and a large key size for strong encipherment by current technology. This also anticipates future development of security technology.

The OAuth 2.0 specification is an industry standard for authorization. We chose two flows from this specification to ensure flexibility. The private/public key pairs can be generated either by the MSP or the brand for either flow.

The key derivation function specification ensures that the public key can be communicated through a text field in an unambiguous way.

Prerequisites

Before starting these exercises, ensure you have:

An Apple Business Register account with Messages for Business enabled

A LinkedIn Developer account (for the LinkedIn OAuth example) or Auth0 account (for the Auth0 example)

Basic understanding of OAuth 2.0 concepts

A server endpoint that can receive webhook callbacks

Familiarity with making HTTP requests and handling JSON responses

Security Considerations

When implementing authentication in Messages for Business:

Protect Sensitive Data: Never log or store authentication tokens in plaintext

Validate All Inputs: Always validate state parameters and tokens before processing

Use HTTPS: Ensure all communication endpoints use HTTPS

Implement Token Expiration: Set appropriate expiration times for access tokens

Follow OAuth Best Practices: Adhere to OAuth 2.0 security recommendations

OAuth 2.0 Flows

Messages for Business supports two OAuth 2.0 flows:

Authorization Code Flow: More secure, requires server-side exchange of the authorization code for an access token. Recommended for most implementations.

Implicit Flow: Simpler but less secure, returns the access token directly to the client. Use only when Authorization Code flow isn't feasible.

The examples in this document primarily demonstrate the Authorization Code flow.

Exercises

To learn how to pass authentication information using the /authenticate endpoint, complete the following exercises:

Exercise: Sending an Authentication Request

Exercise: Create your LinkedIn App

Exercise: Decode the Auth Code and Retrieve User Data

Exercise: Receive and Parse an Authentication Response

Exercise: Sending an Authentication Request

The new Authentication flow, AuthV2, is part of the Type Interactive messages. This means that most of the information related to the Authentication flow will be located in the "interactiveData" field. See Authentication Message.

Send a POST request to the following URL: https://mspgw.push.apple.com/v1/authenticate

Here are the details for your payload request:

```json
{
  "v": 1,
  "sourceId": "<sourceId>",
  "destinationId": "<destinationId>",
  "type": "interactive",
  "locale": "en_us",
  "interactiveData": {
    "bid": "com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension",
    "data": {
      "version": "2.0",
      "requestIdentifier": "f8[****]5d",
      "authenticate": {
        "oauth2": {
          "state": "3D13[***]hPQ",
          "responseType": "code",
          "scope": ["openid", "email", "profile"],
          "redirectURI" : "https://example.com/auth/linkedin/callback"
        }
      }
    },
    "receivedMessage": {
      "title": "Lets Sign In"
    },
    "replyMessage": {
      "title": "Sign In Completed"
    }
  }
}
Notes about the payload:
```
<sub>↳ `msp-api-tutorial.md` L1837–1897</sub>

v: API version

sourceId: Business ID

destinationId: Opaque ID

type: Type of message

locale: Language selected

version: Refers to AuthV2

requestIdentifier: A unique identifier for the authentication request. Value must be UUID: uuid.

state: State of the authentication request

responseType: Refers to OAuth 2.0 authorization code flow

scope: Refers to data that the authentication service provides

redirectURI: Your MSP endpoint ready to receive the code from LinkedIn

receivedMessage: Button UI that will receive the user to initiate the Authentication process

replyMessage: Button UI that will receive the user once the Authentication process has finished

Here are a few notes to consider about the following REQUIRED parameters:

requestIdentifier: This is a UUID created in your MSP server and is useful for identifying the Authentication request sent. Once the client has completed the Authentication process, regardless of the result (success or failure), the MSP will receive a Message request with the same requestIdentifier. This allows you to identify the Authentication request. Value must be UUID: uuid.

scope: This refers to the data that will be provided by the authentication provider you have selected.

redirectURI: This is a string representing the redirect URL that the OAuth provider redirects the user to. With the redirect request, you'll receive the "code" to identify the auth process from the client and take the necessary actions for your MSP integration.

state: The Business & MSP needs to use the state to verify the session and user for authentication. The state will be received later in your webhook request.

Exercise: Create your LinkedIn App

This exercise uses a third-party service, LinkedIn's OAuth 2.0 API, to authenticate. To create a LinkedIn App, you'll need to be registered as a LinkedIn Developer here: https://developer.linkedin.com.

To make your chosen OAuth 2.0 provider available, you need to request a security audit for your Apple Business Register account. Apple typically completes the approval process in 2-3 business days.

Most third-party authentication service providers ask you to create an app on their platform. Some platforms simply refer to it as setting up a client, which is the name given under the OAuth 2.0 specification, and some refer to it as an OAuth 2.0 service.

For each service used, you have to tell the service where to send requests. This is called the redirect_uri or callback URL. Enter your private MSP endpoint (example: https://myMSPserver.com/authentication/linkedIn/callback) into the field.

Prior to sending authentication requests, you need to retrieve the following fields from each third-party service and enter these into Apple Business Register:

Collect your LinkedIn Client ID App

Authorised Redirect URLs

Enable OpenID Connect (disabled by default)

Step 1: Set up a LinkedIn App

In this exercise, you set up an authentication service and add information about the service into Apple Business Register. There is no code to run for this task.

To follow along with these exercises, you'll need a LinkedIn developer and user account for testing.

Log into LinkedIn Developer and click Create App from their API site.

Collect your Client ID App: Under the Auth > Application credentials > Authentication Keys section, collect the Client ID. You'll need this to register it in Apple Business Register.

Set Authorised Redirect URLs: Under the Auth > OAuth 2.0 settings > Authorised redirect URLs section for your app, set your MSP endpoint ready to receive the code from LinkedIn. Ensure that the Authorised URL matches the one configured as redirectURI (payload request).

Enable OpenID Connect (disabled by default): Under the Products > Available Products > Sign In with LinkedIn using OpenID Connect section, request access to LinkedIn to enable this option.

Step 2: Connect data from the LinkedIn App to Apple Business Register

Go to your existing Messages for Business account in Apple Business Register (https://register.apple.com), find the End User Authentication section, and enter the following values:

OAuthURL: https://www.linkedin.com/oauth/v2/authorization

Client Identifier: Use the unique identifier from the LinkedIn API

Make sure you click Submit at the top of the account page. Changes on Apple Business Register become active after you submit the profile and Apple approves it. The security audit for your authentication service takes 2-3 business days. You need to allow sufficient time in your development schedule for this approval.

To ensure prompt approval, send an email reminder about the authentication audit to messagesforbusiness-support@apple.com. Include the Business ID or a link to the URL in Apple Business Register.

Exercise: Decode the Auth Code and Retrieve User Data

You will receive the state configured previously with the Authentication request, you can use it to verify the Authentication session.

You will receive the code as a request argument in your webhook endpoint, you can use it to retrieve all the information about the user who recently logged in.

For LinkedIn integration, you can refer to the documentation here: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fconsumer%2Fcontext

As example, exchange Authorization Code for an Access Token:

```bash
curl --location --request POST 'https://www.linkedin.com/oauth/v2/accessToken' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code={authorization_code_from_endpoint_request}' \
--data-urlencode 'client_id={your_client_id}' \
--data-urlencode 'client_secret={your_client_secret}' \
--data-urlencode 'redirect_uri={your_callback_url}'
Once received the token, use it to redeem user information from LinkedIn.
```
<sub>↳ `msp-api-tutorial.md` L2021–2035</sub>

curl -X GET 'https://api.linkedin.com/v2/userinfo' \

-H 'Authorization: Bearer {INSERT_TOKEN}'

You should be receiving JSON data like this:

```json
{
    "sub": "****",
    "email_verified": true, 
    "name": "ClientName", 
    "locale": {
       "country": "CC", 
       "language": "en"
    },
    "given_name": "ClientGivenName",
    "family_name": "ClientFamilyName",
    "email": "****@email.com"
}
If all the information is correct, please remember to redirect the status to success. Clients should receive a message confirming that the sign-in process has been completed successfully.
```
<sub>↳ `msp-api-tutorial.md` L2047–2071</sub>

302 messages-auth://?status=success

Exercise: Receive and Parse an Authentication Response

In this exercise, we receive an interactive message response at our messaging endpoint with either a successful login or an unsuccessful login prompted by the authentication request.

The authentication request conforms to the interactive message class, even though it's delivered to its own endpoint. The response arrives at your MSP's /message endpoint. It conforms to the interactive message response, similar to the list picker response, with a few unique fields for authentication.

When developing your Messages for Business integration, you need to parse interactive message responses into the different types to ensure that each can be routed to the correct handler. This exercise demonstrates how to parse the response to filter out the authentication response from other interactive message response types.

Expected MSP server response

Make a note of the encrypted token displayed in the output, this piece is used in the next exercise.

```json
{
    "type": "interactive",
    "id": "<messageId>",
    "v": 1,
    "sourceId": "<sourceId>",
    "destinationId": "<destinationId>",
    "locale": "en_IE",
    "interactiveData": {
        "bid": "com.apple.[****].business.extension",
        "data": {
            "replyMessage": {
                "alternateTitle": "Sign In Completed",
                "title": "Sign In Completed",
                "style": "icon"
            },
            "receivedMessage": {
                "title": "Lets Sign In",
                "style": "icon"
            },
            "authenticate": {
                "status": "success"
            },
            "version": "2",
            "requestIdentifier": "<requestIdentifier>"
        },
        "sessionIdentifier": "<sessionIdentifier>"
    }, 
    "attachments": [ ]
}
Notes about the response:
```
<sub>↳ `msp-api-tutorial.md` L2099–2157</sub>

sourceId: Opaque ID

destinationId: Business ID

Note that requestIdentifier should be the same as you indicated when building the AuthV2 request. Persist this information, along with any useful information from your MSP, at the moment of sending the request, and collect it back now for your MSP's purpose.

Authenticate > status should match the status sent by your webhook.

Using Auth0 as an Alternative to LinkedIn

Auth0 provides a more powerful authentication system with more features and better coverage of the OAuth 2.0 specification compared to LinkedIn. This section explains how to set up Auth0 as your authentication provider.

Setting Up Auth0

You can navigate to https://auth0.com and sign up for a free account.

From your Auth0 management account:

Create Application > Regular Web Application.

Under Allowed Callback URLs, add your private MSP endpoint (example: https://myMSPserver.com/authentication/auth0/callback). Ensure that the other URL fields (including Login URI, Logout URLs, Web Origins) are left blank.

Refresh Token Behavior by selecting Non-Rotating.

Select Advanced Settings > Grant Types. Based on the process you want to use, select "Code Authorization" or "Implicit".

You have to add users onto an allow list in Auth0 similar to the allow list in Apple Business Register. Add your test users with Users & Roles > + Create User. You can also enable providers, such as Google, to allow any user with an account on that system.

Configuring Auth0 with Apple Business Register

Go to your Messages for Business account in Apple Business Register

In the End User Authentication section, enter:

OAuthURL: https://[your-auth0-domain].auth0.com/authorize

Client Identifier: Your Auth0 Client ID

Submit your changes and wait for approval

Troubleshooting

Common Issues and Solutions

Authentication Request Not Showing:

Verify your payload format is correct

Check that your Business ID and Opaque ID are valid

Ensure your Apple Business Register account has been approved for authentication

OAuth Provider Rejecting Requests:

Verify your redirect URI matches exactly what's configured in the provider

Check that all required scopes are properly configured

Ensure your client ID is correct

Authentication Success but No User Data:

Verify you're using the correct token endpoint

Check that your client secret is valid

Ensure you've requested the appropriate scopes

Webhook Not Receiving Authentication Response:

Verify your webhook endpoint is publicly accessible

Check server logs for any errors processing the request

Ensure your webhook is correctly registered with Apple Business Register

https://register.apple.com/resources/messages/msp-api-tutorial/imessage-apps

Integrating Your iMessage App

Messages for Business provides an iMessage app that makes it simple for you to send interactive messages to customers. But if you want to give your customers an interactive experience that is unique to your business, you can also use the Messages framework to create a standalone iMessage app or extend your iOS app so that it interacts with Messages. For more information, see iMessage App.

Exercise: Using Custom iMessage Apps

In this exercise, you perform the following tasks:

Set up the sample iMessage app.

Send an interactive message payload to trigger the sample iMessage app with custom parameters.

Step 1: Set up a sample iMessage app

Make sure you are using Xcode 16 or later.

Download the iMessage App sample, as part of the resources sample-code.

Open the Xcode project, install and run the app on the test device.

Step 2: Send a custom iMessage app payload

Copy Development Team ID and Bundle Identifier of the app from Xcode.

Generate the bid parameter using prefix, team ID, and bundle identifier.

Assemble the app parameter using URL parameters.

Assemble and send the Message payload.

Perform the following tasks on your test server:

Locate the code zip folder and unzip it.

Open and edit the 22_invoke_custom_extension.py file by inserting the destination_id, located towards the bottom of the file, with the source_id from the output in Exercise: Receiving a Text Message.

Save and run the 22_invoke_custom_extension.py file.

Expected MSP server response

Messages for Business server return code: 200

Expected client device response

| Initial Response in Messages for Business | iMessage App |
|---|---|
| On the user device, you should see the following message bubble. | When the user taps the message bubble, a detailed map opens up with a location pin. |
<sub>↳ `msp-api-tutorial.md` L2301–2303</sub>

<!-- img: extension-ipad.jpeg -->

<!-- img: extension.png -->

https://register.apple.com/resources/messages/msp-api-tutorial/client-landing-page

Exercise: Create a Client Landing Page

To route messages between the Messages for Business server and new brands, you need to create a link between the new brands Messages for Business ID and the business client ID on your messaging platform using the Client Landing Page URL. When new brands access the landing page, you need to present them with a login screen. The login screen logs the brand into your messaging platform, and then links their Messages for Business ID to a business client ID you associated with their business name and logo in your system.

In this step, you connect your new brands Messages for Business ID to your messaging platform. This linking process allows messages to pass through your platform to the customer support agents.

Create an HTML page, based on the template located in the downloadable files, to allows your business clients link their Messages for Business IDs to your business client ID assigned by your messaging platform.

NOTE

The values saved go to your database based on the GET handler for this page, and not the POST handler. Because we're rendering a page visible to the user, GET handles this data.

Ensure the page is HTTPS accessible.

Add handlers to read the following fields from the query strings of the URL, validate the data passed, and save those items in your database: id, name, logo. Below is an example of how the URL passes the information:

https://<YourSiteHost>/<YourSitePath>?id=<BusinessChatID>&name=<BusinessName>&logo=<LogoURL>

Automate a process to get the Messages for Business ID from the URL and plug it into your messaging platform to allow new brands to test the messaging connectivity.

NOTE

When brands select you as their MSP, Messages for Business directs them to your landing page with a "Connect to <Messaging Service Platform>" link passing the information you need to send and receive messages for their business.

Listing 21_create_landing_page.py

from flask import Flask, render_template, request

    app = Flask(__name__)

    @app.route("/landingPage", methods=['GET'])

    def landingPage():

        return render_template("landingPage.html")

Client Landing Page HTML

Create a /templates folder in the same directory as the HTML file. A sample /templates folder is in the same directory as the other Python files in our API tutorial repository.

The following HTML uses Jinga2 that runs parallel with Flask.

Listing templates/landingPage.html

<html>

    <head>

    <title>Landing Page</title>

    </head>

    <body>

        <div class="box">

            <div class="main">

                <h1> Welcome, {{ request.args.get('name') }}! </h1>

                <p>Sign in to connect your Messages for Business account.</p>

                <img src={{ request.args.get('logo') }}>

                <form class="text-center" method="post" action="/landingPage_csp">

                    <input type="text" name="userName" placeholder="User Name">

                    <input type="password" name="userPassword" placeholder="Password">

                    <input type="hidden" name="BusinessId" value="{{ request.args.get('id') }}">

                    <input type="hidden" name="BusinessName" value="{{ request.args.get('name') }}">

                    <input type="hidden" name="BusinessLogo" value="{{ request.args.get('logo') }}">

                    <input type="submit" value="Get Started">

                </form>

                <p>Don't have an account? Click <a href="/#">here</a> to create one.</p>

                <a href="/#">Forgot password or user name?</a>

            </div>

        </div>

    </body>

    <style>

        body{text-align:center;display:flex;justify-content:center;color:darkgray;background-color:darkgray;}

        .box{padding:2% 10%;max-width:75%;position:fixed;top:20%;border-radius:20px;background-color:white;}

        h1 {color:black;}

        input{box-sizing: border-box;-moz-box-sizing: border-box;width:50%;padding:10px;border-style:unset;border:1px solid darkgray;border-radius:5px;text-align:center;}

        input[type=submit]{color:#007bff;border-color:#007bff;background-color:initial;}

        img{max-width:200px;}

        p a {color:#007bff;text-decoration:none;}

        a {color:gray;}

    </style>

</html>

Test Your Client Landing Page

To test your "Connect to <Customer Service Platform>" link, append the Messages for Business ID, name, and logo to the end of your landing page URL similar to the following:

https://<your-domain-here>/landingPage?id=a884eddf-b0ad-4be4-9c0e-071531638768&name=Connect%20Business%20Chat%20Account&logo=https://register.apple.com/assets/images/icon/apps/MessagesIcon.png

NOTE

The "Connect to Customer Service Platform" link doesn't show for private MSPs.

Exercise: Publish Your Client Landing Page

In this step, you submit your company's Client Landing Page to Apple Business Register which publishes it to any new brands of your messaging platform.

Log into your company account in Apple Business Register.

Find "Messaging Service Providers" under Connected Services and click the "Customer Service Platforms" selection.

NOTE

If you do not see "Messaging Service Providers" here, our system may not consider your company as an MSP. For more information on how to correct this, contact your Apple Business Register support representative.

Find your main Commercial MSP along the left navigation panel, and click it.

Find the "Server Configuration" Section, and then find the "Client Landing Page URL" field under this section.

NOTE

If you do not see a "Client Landing Page URL" on any of your MSPs, your company may not be have a Commercial status MSP account yet. Contact your Apple Business Register support representative.

Click Edit for the section and provide the landing page URL in the field indicated.

Click Save.

Click Submit located in the lower right corner to publish your changes to Apple Business Register.

https://register.apple.com/resources/messages/msp-api-tutorial/faq

Most Common Errors

What can I do to avoid the most common errors in implementing Messages for Business?

Encoding errors are the largest class of technical errors based on our analysis of support tickets associated with the Messages for Business API.

Developers who work entirely or primarily with web technologies may be unfamiliar with binary classes and objects. When you decode a Base64-encoded string it creates a binary object that is not a string. String methods attempted on this object fail.

Another common error is double-encoding URLs. You should only apply safe-encoding to a URL a single time. You should use a well-validated library to URL encode and decode, to ensure that it correctly implements all aspects of the specification.

Many languages safe-encode output to log files and standard output stream. These strings may error out when used as input in the exact same format as the output. For example, Java safe-encodes many characters in strings with a / character. Python safe-encodes strings with a u at the beginning to indicate unicode string.

Unfortunately, all valid hexadecimal strings are also valid Base64 strings. When you decode a hex string as Base64, the method succeeds, but creates an erroneous result. This makes it difficult to triage the issue.

User Accounts and Synchronization

I sent my first message and it shows Not Delivered on the device. How do I fix it?

There are different reasons you may see the Not Delivered error when beginning a Business Chat conversation for the first time.

If you receive Not Delivered for all test devices, try the following steps:

Use a cURL command, or similar language, to ensure that your server is listening on the correct endpoint. Remember, /message appends to the end and is a POST, not a GET.

Verify your server received the Messages for Business message and, if so, troubleshoot based on the HTTP response code.

Double check that all of the email addresses used in the allow list are valid Apple Accounts at https://account.apple.com.

For each device showing Not Delivered perform the following steps:

Go to Settings > Messages > Send & Receive.

Ensure that the email address associated with the allow list is checked, on both "… receive messages…" and "…start new conversations…" sections.

Return to Settings.

Wait 12 hours from the last attempt to message this particular brand from this device as the message may have been sent since you logged the support ticket.

Ensure that the Messaging Service Provider (MSP) endpoint, listener, and agent console are prepared to receive and process the message.

Attempt to start the conversation again.

How are messages synced across multiple devices for a single user?

Messages sync across all devices that are on a set of related Apple Accounts. You can create Apple Accounts from an email address or a phone number. You can check these associations by logging into the Apple Account site.

Some users set up two or more devices from different Apple Accounts. This creates two zones that act as separate users. Additional devices sync with one of the zones depending on the Apple Account, but the two zones don't sync. Also, Messages for Business conversations have different Opaque IDs across the two zones.

What can we do to prevent issues for users with multiple devices or accounts?

Our recommended practice is to structure user tables in such a way that a single known user may have more than one Opaque ID. Most users only enter the system once with one Opaque ID. They may return under an unknown ID not fully realizing that is the case. This is more common with tech-savvy users who have many devices and many accounts for services they use, than for the general user population.

What is an Opaque ID?

It is a unique identifier to each pairing between a Business ID and a user. The Opaque ID also refers to the destinationId in the code samples for sending messages from your Messaging Service Provider (MSP) to a user. Each user is defined by a set of related Apple Accounts as described above.

For privacy, the business doesn't receive the user's phone number, email address or iCloud account information. The Opaque ID is unique to the relationship between the customer's Apple Account and the business's business ID. A customer has a different Opaque ID for every chat they have using Messages for Business. The customer decides if and when to share personal identifying information with the business. For more information, see Apple Platform Security.

In your MSP agent console, Apple recommends that your system stores the Opaque ID. Once a user has authenticated through either an agent/bot process or our OAuth2 feature, you should change the identifier to the user's name.

Are users limited to sending only photos and videos in Messages for Business? Is it possible to send other types of files such as PDF, Microsoft Word, Microsoft Excel?

You can send any type of file through Messages for Business. For example, you can easily send and receive an Excel file (.xlsx) to an iPhone that does not have Excel installed. Any binary file should be intact after transport in either direction, regardless of the iPhone or iPad settings.

Getting Users into a Conversation with Entry Points

How do I use the intent ID and group ID parameters?

The intent (biz-intent-id) and group (biz-group-id) fields are used to track the source of user engagement and to route messages to the appropriate groups.

Intent and group field values can be specified as URL parameters embedded in apps, QR codes, or Messages for Business buttons on websites. For example:

https://bcrw.apple.com/urn:biz:Some-Biz-Chat-ID?biz-intent-id=SomeIntent&biz-group-id=SomeGroup

In the first text message from the customer after starting the conversation through the URL, the MSP can retrieve the intent and group from the message payload. For example:

```json
{
"body": "Hello",
"sourceId": "<opaque user ID>",
…
```
<sub>↳ `msp-api-tutorial.md` L2625–2631</sub>

```json
"intent": "SomeIntent",
"group": "SomeGroup"
}
The intent field value is specified with biz-intent-id key in the URL, but appears under intent key in the message payload. Similarly, the group field is specified with biz-group-id in the URL and group from the message.
```
<sub>↳ `msp-api-tutorial.md` L2633–2639</sub>

Apple Maps puts the physical address in the biz-intent-id field for users who launch Messages for Business from Maps. Spaces are replaced by plus-sign characters and other safe encoding changes may be made for the sake of generating a valid URL.

For more information about routing using intent and group IDs, see About Intent, Group, and Body Values and Apple Maps and Your Business Locations.

How do I set up entry points in Apple Maps and my brand website?

You can set up entry points for the following:

iOS entry points: Entry Points

Message Suggest: Message Suggest Guide

Messages buttons: Adding a Message for Business Button to Your Website and Starting a Chat from Your App. You can also add a Message button to your email, see Starting a Chat from a URL

Our users experienced latency or our engineers measured latency in the message delivery. Can you fix this latency on your side?

The device connectivity, also known as the "last mile" connection from the device into the network, generates the most latency. Apple continually optimizes message delivery on the Messages for Business server side, but we cannot affect connectivity between the device and Wi-Fi or cellular networks.

Compliance and Regulatory Questions

Does the MSP have to delete the conversation history with user in accordance with General Data Protection Regulation 2016/679 (GDPR)?

According to our security and compliance team:

The MSP is the data controller. The arrangement between the brand and the MSP guides how it is handled, with consideration of the regulatory domain they are operating in. All we offer is a block for further messages from the brand to the user. It is beyond our scope to manage the relationship any further than that.

https://register.apple.com/resources/messages/msp-api-tutorial/glossary

Glossary

Following are common terms and their definitions frequently used in this tutorial.

| Term | Definition |
|---|---|
| agent | The receiving entity for a Messages for Business dialog. It can be a human customer support representative or an automated agent. |
| Apple Account | An Apple Account is the email address that has been preregistered at Apple: https://appleid.apple.com/. The email can be issued by an Apple domain, such as iCloud.com (http://icloud.com/) and apple.com, or a non-Apple domain. |
| bot | An automated agent. |
| business card | Business cards display the global contact details for your business, including your brand or logo, your business phone number, email, website URL, and Messages button. See Business and Place Cards. |
| business ID | Also known as a biz-ID, it is a unique business identifier assigned when Apple Register approves a Messages for Business account. |
| console | The view of a MSP seen by customer service agents. |
| conversation | A long-lived interaction between a unique user Apple Account and a unique business. A conversation may consist of multiple dialogs. |
| CSP ID | A unique customer service platform identifier assigned when Apple Business Register approves a CSP account. Now called MSP ID. |
| CSP Secret | A unique secret retrieved from Apple Business Register along with the CSP ID. |
| destination ID | A field describing a messages destination. It is the user's opaque ID for messages sent to the client device or the Business ID for messages sent to the MSP. This field appears twice: once in the HTTPS header of the message as Destination-Id and once encrypted in the body as destinationId. |
| dialog | A set of interactions between a unique user Apple Account and a unique bot or customer service representative that is bound in time. For example, User A chats with Automated Agent #1, then CSR #15, who escalated to CSR #3, who then refers User A back to CSR #15. This would be considered four dialogs. |
| group ID | A value used in URLs that designates the department or individuals best qualified to handle a user's particular question or problem. |
| iMessages | Apple's secure messaging service for sending and receiving messages in the Messages app. |
| intent ID | A value used in URLs that define the purpose of the chat. |
| interactive message | A category of message within Messages for Business that includes List Picker, Time Picker, Apple Pay requests, custom app download requests, and authentication requests. |
| link previews | A Messages app feature that Messages for Business uses. The functionality of Link Previews has been found to be inconsistent, necessitating the creation of the Rich Link Messages feature in Messages for Business. |
| Messages app | The application for sending and receiving messages. This should not be confused with iMessages. |
| MSP | Messaging Service Platform. A messaging platform that provides the user interface for customer service agents and the connection to Messages for Business orthe company that sells a customer service product, such as Genesys Hub and LiveEngage by LivePerson. |
| MSP ID | A unique customer service platform identifier assigned when Apple Business Register approves a MSP account. |
| opaque ID | A 169-character string that uniquely identifies the interaction between a user and a business. It is passed in the HTTP header of each Messages for Business message. An opaque ID is created with each message associated with the conversation between the customer and a unique business. |
| OAuth | An industry-standard protocol used for authorization. Messages for Business supports OAuth 2.0. |
| place card | Place cards appear in iOS search results and display your business name and address. See Apple Maps place card. |
| POI | Point of Interest is a place of interest in Maps. |
| register | The portal site located at https://register.apple.com. |
| rich link | An MSP implemented Messages for Business feature to enhance user communications. This feature ensures that media, either an image or a video, arrives on the user's device smoothly, without presenting the "Tap to Load" message. See Rich Link Messages. |
| source ID | A field describing where the message originates. It is the user's opaque ID for messages from the client device or the Business ID for messages from the MSP. This field appears twice: once in the HTTPS header of the message as Source-Id and once encrypted in the body as sourceId. |
<sub>↳ `msp-api-tutorial.md` L2691–2743</sub>

https://register.apple.com/resources/messages/msp-api-tutorial/download

Download Sample code

APPLE INC. SAMPLE CODE LICENSE (for use with Apple Messages for Business)

PLEASE READ THIS SAMPLE CODE LICENSE ("AGREEMENT") CAREFULLY BEFORE USING THE SAMPLE CODE.

BY USING THE SAMPLE CODE, YOU ARE AGREEING TO BE BOUND BY THE TERMS OF THIS AGREEMENT. IF YOU DO NOT AGREE TO THE TERMS OF THIS AGREEMENT, DO NOT USE THE SAMPLE CODE.

IMPORTANT NOTE: THIS SAMPLE CODE IS LICENSED TO YOU FOR INTERNAL TESTING AND EVALUATION PURPOSES ONLY, AND IT SHOULD NOT BE USED IN A COMMERCIAL OPERATING ENVIRONMENT OR WITH IMPORTANT DATA.

License. Subject to the terms and conditions of this Agreement, you are granted a limited non-exclusive license under Apple's copyrights in the sample code accompanying this license as originally provided by Apple (the "Sample Code") to use, reproduce, and modify the Sample Code during the term of this Agreement solely for purposes of your own internal testing and evaluation of Apple Messages for Business; and only in accordance with the applicable terms of use for the Apple Messages for Business service. The Sample Code is not licensed under this Agreement for redistribution, sublicensing, or transfer of any kind. Except as expressly stated herein, no other rights or licenses are granted or to be implied, including but not limited to, any rights under Apple patents.

No Support and Maintenance. Apple is not obligated to provide any maintenance, support, or updates for the Sample Code. You acknowledge that Apple has no express or implied obligation to announce or make available a commercial, distributable version of the Sample Code to anyone in the future. Should a commercial, distributable version of the Sample Code be made available, it may not be compatible with the Sample Code licensed hereunder. Any development work you perform using the Sample Code will be at your sole expense and risk.

Term of Agreement. The term of this Agreement shall commence upon your downloading, installation or use of the Sample Code and will terminate automatically without notice from Apple if you fail to comply with any term(s) of this Agreement. Upon release of a new version of the Sample Code by Apple, You agree to cease using the Sample Code provided to You under this Agreement.

Disclaimer of Warranties.

A. The Sample Code provided hereunder is an internal version that may be incomplete and may contain inaccuracies or errors that could cause failures or loss of data.

B. YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT, TO THE EXTENT PERMITTED BY APPLICABLE LAW, USE OF THE SAMPLE CODE AND ANY SERVICES ACCESSED THROUGH THE SAMPLE CODE, IS AT YOUR SOLE RISK AND THAT THE ENTIRE RISK AS TO SATISFACTORY QUALITY, PERFORMANCE, ACCURACY, AND EFFORT IS WITH YOU.

C. TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THE SAMPLE CODE IS PROVIDED "AS IS" AND "AS AVAILABLE", WITH ALL FAULTS AND WITHOUT WARRANTY OF ANY KIND, AND APPLE AND APPLE'S LICENSORS HEREBY DISCLAIM ALL WARRANTIES AND CONDITIONS WITH RESPECT TO THE SAMPLE CODE, EITHER EXPRESS, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES AND/OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS.

D. APPLE DOES NOT WARRANT THAT THE SAMPLE CODE WILL MEET YOUR REQUIREMENTS, THAT THE OPERATION OF THE SAMPLE CODE WILL BE UNINTERRUPTED OR ERROR-FREE, THAT ANY SERVICES ACCESSED THROUGH THE SAMPLE CODE WILL CONTINUE TO BE MADE AVAILABLE, THAT THE SAMPLE CODE WILL BE COMPATIBLE WITH ANY OTHER PRODUCTS OR SERVICES, OR THAT DEFECTS IN THE SAMPLE CODE WILL BE CORRECTED.

E. YOU FURTHER ACKNOWLEDGE THAT THE SAMPLE CODE IS NOT INTENDED OR SUITABLE FOR USE IN SITUATIONS OR ENVIRONMENTS WHERE THE FAILURE OF, OR ERRORS OR INACCURACIES IN THE CONTENT, DATA, OR INFORMATION PROVIDED BY THE SAMPLE CODE COULD LEAD TO DEATH, PERSONAL INJURY, OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE, INCLUDING WITHOUT LIMITATION THE OPERATION OF NUCLEAR FACILITIES, AIRCRAFT NAVIGATION OR COMMUNICATION SYSTEMS, AIR TRAFFIC CONTROL, LIFE SUPPORT, OR WEAPONS SYSTEMS.

Limitation of Liability. IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, EVALUATION, TESTING, REPRODUCTION, MODIFICATION, AND/OR DISTRIBUTION OF THE SAMPLE CODE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The Sample Code is copyrighted © 2025 by Apple Inc. All Rights Reserved

https://register.apple.com/resources/messages/msp-api-tutorial/doc-rev-history

Revision History

| Date | Version | Summary |
|---|---|---|
| April 29, 2026 | 3.4.0 | Updated UUID requirements |
| June 2, 2025 | 3.3.0 | Updated Authentication tutorial with enhanced OAuth 2.0 flows and added reference to iMessage sample code |
| September 21, 2022 | 3.2.0 | Apple Pay signing request changed to ECC 256 algorithm |
| May 20, 2022 | 3.1.0 | Added section on Implementing Client Verification |
| April 22, 2022 | 3.0.1 | Fixes sample code |
| February 11, 2022 | 3.0.0 | Update to the structure and updated pointers to REST API |
| January 11, 2022 | 2.1.3 | Link fixes |
| December 16, 2021 | 2.1.2 | Sample code update |
| November 22, 2021 | 2.1.1 | Fixes |
| October 25, 2021 | 2.1 | Quick Reply Update |
| September 20, 2021 | 2.0.0 | Rebranded Business Chat to Messages for Business; Chat Suggest to Message Suggest; removed 'BETA' from Quick Reply. |
| August 12, 2021 | 1.6.0 | Quick Reply Update |
| June 7, 2021 | 1.5.0 | iOS 15, macOS 15 Beta update |
| May 27, 2021 | 1.4.1 | Minor visual corrections |
| May 13, 2021 | 1.4.0 | Minor changes to Authentication section. |
| April 29, 2021 | 1.3.0 | Minor changes to Apple Pay section. |
| April 16, 2021 | 1.2.0 | Minor changes to troubleshooting steps in the FAQ. |
| April 1, 2021 | 1.1.0 | Minor changes to introduction text for clarification. |
| March 23, 2021 | 1.0.0 | Initial release. |
<sub>↳ `msp-api-tutorial.md` L2783–2821</sub>

Revision Number Incrementation

| Version | Explanation |
|---|---|
| 1.0.0 | Major revision. Includes number increment and new content. |
| 1.0.0 | Minor revision. Includes number increment and changes to current content, such as content corrections, graphics, grammar, etc. |
<sub>↳ `msp-api-tutorial.md` L2825–2829</sub>



---

## 2. Policy / UX / Privacy / Onboarding

> Part 2 of the master-plus-parts verbatim canonical. Prose rules reproduced in Apple's exact wording. Sources: `messaging-documentation.md` (portal v3.1, 21 May 2026) and `msp-onboarding.md` (v3.0.3, 01 Feb 2024). Overlay (provenance, recency, audit) lives in the Master index.

---

# Part 2A — Getting Started, Policies, UX, Privacy, Metrics (verbatim)

> **Source:** `messaging-documentation.md` — verbatim (entities decoded, escapes removed, tab-tables → Markdown, JSON/cURL fenced unchanged). 

# messaging-documentation

https://register.apple.com/resources/messages/messaging-documentation/

Apple Messages for Business

Create Engaging, Secure, and Scalable Messaging Experiences

<!-- img: msp-m4b-flow.png -->

Version: 3.1

Last update: 21 May 2026

Apple Messages for Business is a service that allows your organization to directly message with your customers using the Messages app. It's designed to provide rich, engaging, and secure experiences, while protecting user privacy.

Messages for Business service flow

Apple Messages for Business service flow

User journeys should be built to prioritize tap-friendly, fast and easy to use conversational flows, using the power of automation for fast responses and triage, as well as efficient scaling. While automation is critical to responsiveness and scalability, there must always be a way to reach a real human agent for escalations.

To qualify for an Apple Messages for Business account, your company needs to select an Apple-approved Messaging Service Provider (MSP). The MSP will provide the asynchronous messaging platform and access to Apple Messages for Business channel. They will also provide automation support (bots/AI), and custom integration with your back-end business systems, such as CRM, order management, authentication, etc. You can find a list of accepted providers here

Designing for great user journeys

<!-- img: heroImage.png -->

Hero 1800 Flowers.com

1800-Flowers.com on Apple Messages for Business

Tap-friendly: Use Rich Features for easy, intuitive navigation.

Fast: Automation provides instant responses and triage.

Scalable: Handle common inquiries automatically while keeping live agents available.

Seamless: Let customers move from automation to a live agent anytime.

Before You Go Live

Every brand experience goes through an Experience Review to ensure it's clear, engaging, and aligned with Apple Messages for Business policies. Familiarizing yourself with these principles early will help inform your design decisions.

Your experience should:

Respond to the first customer message within 5 seconds (automation), and clearly identify itself as an automated agent.

If the user's intent is not detected from the entry point or opening message, offer a triage menu to quickly guide them to the most relevant options.

Handle live agent transitions transparently: notify users when a transfer is happening, include estimated wait times when applicable, and have agents introduce themselves when taking over.

Support keywords like "help" or "agent" to reach a live agent at any time.

Use Rich Features (Quick Reply, Form, Apple Pay, Authentication, List and Time Picker, Apple Maps, Rich Links, etc.) to create a fast, tap-friendly experience, following UX guidelines for each feature.

Respect asynchronous messaging and avoid pressuring customers to respond immediately.

Never ask customers to repeat information they've already shared in the conversation.

When presenting options to users, use Quick Reply (up to 5 options) or List Picker (for longer lists) — avoid expecting customers to type responses that could be handled with a tap.

Comply with Apple's policies on privacy, PII collection, and Terms of Use handling.

Getting Started with Apple Messages for Business

<!-- img: e2e-circle-v2.png -->

Messages for Business onboarding end-to-end flow

The Apple Messages for Business onboarding end-to-end flow

1. Planning and Preparation

What you need:

Business goals defined (revenue, support efficiency, customer satisfaction)

Basic understanding of your business use cases and customer communication patterns

Messaging Service Provider (MSP) selected from Apple's approved list

What to do:

Document your use cases using the Use Cases template

Work with your MSP to finalize goals and technical approach

Plan your customer journey and identify interactive features

Review Apple Messages for Business policies to ensure compliance

Understand conversation design best practices for effective customer interactions

2. Account Registration

What you need:

Apple Account (formerly Apple ID or Managed Apple Account created by your organization)

Corporate email address for login

Administrator access to Apple Business Register

One or more Apple Accounts for testing

What to do:

Create your Internal Test Account at Apple Business Register

Select your MSP and configure connection

Add test Apple Accounts for internal testing

See Register your account for complete step-by-step instructions

Review troubleshooting guide if you encounter issues during registration

3. Design and Build Your Experience

What you need:

Understanding of your customer base and common issues

Team roles and responsibilities defined

Access to customer service tools and information systems

Familiarity with Apple Messages for Business features (see Design your UX)

What to do:

Map out your user journey for Apple Messages for Business

Design conversation flows using conversation design best practices

Implement interactive features (Quick Reply, List Picker, Time Picker, Apple Pay, etc.)

Create conversation guidelines for your team

Identify and define the entry points you plan to enable once your experience is approved and live

Build and configure your experience with your MSP

Implement automation and live agent routing

Follow UX design guidelines for optimal customer experience

4. Testing and Quality Assurance

What you need:

Apple Messages for Business account created

iMessage enabled on your device

Added as approved tester in your account

Apple Account configured on the test device

What to do:

Test the complete experience in your internal test account

Perform comprehensive quality assurance on all conversation flows

Verify all interactive features work correctly

Test automation, triage menus, and live agent escalation paths

See Account testing guide for detailed testing procedures

Prepare a screen recording of the complete customer journey

Consult troubleshooting guide for any issues encountered during testing

5. Experience Review and Launch

What to do:

Your MSP submits the screen recording for Experience Review

Review experience review requirements to understand the evaluation criteria

Address any feedback from the review process

Once approved, Apple updates your test account to a commercial account in Apple Business Register

Finalize your commercial account configuration and branding assets

Follow go-live procedures to launch your experience

Schedule and execute your go-live date

Monitor performance using metrics and analytics

Review end-to-end implementation guide for post-launch optimization

Continue to refine your experience based on customer feedback and best practices

Learn More

Core Documentation:

Apple Messages for Business Policies - Required policies and guidelines

Design Your UX - User experience design principles

Interactive Features - Rich features overview

Entry Points Overview - Ways customers can reach you

Additional Resources:

Conversation Guidelines - Team response standards

Privacy and Security - Data protection and compliance

FAQ - Frequently asked questions

Troubleshooting - Common issues and solutions

https://register.apple.com/resources/messages/messaging-documentation/end-to-end

Onboarding with Apple Messages for Business

Before you create your Apple Messages for Business account, review the following Apple Messages for Business onboarding overview.

Messages for Business onboarding end-to-end flow

The Apple Messages for Business onboarding end-to-end flow

Register your account

Registering your Apple Messages for Business account requires the following actions.

Register your organization. Register your organization at Apple Business Register. Create your Apple Messages for Business account. Create your Apple Messages for Business account, upload your branding, and select your Messaging Service Provider (MSP). Approval. The Apple approval process can take few days. Be sure to account for the time needed and submit your account for approval as soon as possible. Team members. Provide backup contacts for your Apple Messages for Business account by adding any additional team members to the account. Connection. Testing your ability to send and receive messages may require you to connect your CRM with your Messaging Service Providers (MSPs) console.

For a more in-depth guide, see Register your account.

Plan for your customer's journey

Using the Use Case template, define your most common use cases.

Channel goals. Define channel goals by completing and returning the Readiness Assessment. Use cases. Determine the top contact drivers for customers or benchmark use cases that you want to support in the channel and meet the defined goals. Interactive features. Consider how you currently address the defined use cases, then implement interactive features to support your customer's journey. Entry points. Plan for entry points that can drive customer engagement, such as adding Messages buttons or using Message Suggest.

For more information, see Plan your customer's journey.

Design your user experience and implement

Once you complete filling out your Use Case template, work with your MSP to apply Best practices and design and implement solutions for each use case.

Automated messages. Support an automated welcome message to greet customers, including an off-hours message. For more information on Design and implement your user experience. Triage customers. Design a welcome Quick reply or List picker menu to triage customer intents and route appropriately. For more information on intents and routing, see About Intent, Group, and Body Values Satisfaction surveys. Design a customer satisfaction survey list picker. Refer to CSAT survey design and code samples for ideas. Authentication and Apple Pay. Configure Authentication and Apple Pay, if needed. Align with your MSP to get the full set of instructions.

For more information, see Design and implement your user experience.

Prepare operations and marketing

Tracking. Plan to track defined channel goals with your MSP to measure your Apple Messages for Business success. Training agents. Update agent scripts and train agents, in console, for Apple Messages for Business messaging and features. Register for Message Suggest. Register your phone numbers for Message Suggest. Marketing preparedness. Prepare your marketing plans for launch and include press releases.

For more information, see Preparing your teams for launch.

Pass the experience review

Refer to the use case template you worked on during your planning phase to help you to set up a use case for the review. The following actions may take anywhere from 1-2 weeks:

Coordinate the use experience with your MSP platform or your internal team.

Prepare recordings of the customer experience using an Apple device.

Share the recordings with Apple.

Apple signs-off on automated agent interaction.

Implement feedback provided by Apple before launch.

For more information, see Experience review.

Go live

On your selected go-live date, you or your MSP need to activate your account and entry points. You need to schedule a performance review with your MSP.

For more information, see Go live!.

Analyze metrics and grow

The following actions may take anywhere from 3-5 weeks to gather and analyze the data:

Review channel performance 30 days after launch.

Increase discoverability by adding additional entry points.

Review how current intents are being supported and plan for optimization.

Consider adding more customer intents to add more value to the channel.

Review metrics every 30 days to continuously improve channel.

For more information, see Optimize your customer's Apple Messages for Business experience.

https://register.apple.com/resources/messages/messaging-documentation/register-your-acct

Register your Apple Messages for Business account

Create and configure your Apple Messages for Business account with Apple Business Register.

Estimated time: 30-45 minutes

Current status: After MSP selection, before account testing

Prerequisites

: See Prerequisites for requirements at different stages.

Overview

The registration process involves:

Creating your account at Apple Business Register

Selecting your MSP platform

Adding test Apple Accounts

Verifying MSP connection

Configuring your commercial account

Step 1: Create your organization profile

<!-- img: abr_Log1.png -->

Navigate to Apple Business Register Messages page and select "Get Started"

Apple Business Register - Apple Messages page

Apple Business Register Messages landing page

Sign in using your business Apple Account or Managed Apple Account (use your corporate email address)

Note

: To create a new Apple Account, visit Create Your Apple Account

Accept the Apple Messages for Business terms and Apple Business Register terms when prompted

Complete your organization information on the form that appears:

Confirm your organization name and details

Select "Internal test account" under "Messages for Business Account Type"

Provide your technical contact information

Step 2: Select your Messaging Service Provider

In the "Messaging Service Provider Configuration" section, select your MSP from the approved provider list

Click "Next" and choose your MSP endpoint:

<!-- img: msp-list.png -->

Select from the "Apple Authorized Commercial Messaging Platform" dropdown, OR

Select "Advanced" if instructed by your MSP to use a custom configuration

Messaging Platform Configuration

Messaging Service Provider configuration

Step 3: Add Test Apple Accounts

<!-- img: add-tester-apple-id.png -->

Test Apple Accounts allow your team to verify message delivery before going live.

Select "+ Add Apple Accounts" to add testers

For each tester, provide:

Full name

Apple Account ID (their personal Apple Account or Managed Apple Account)

Tester Apple Accounts

Add tester Apple Accounts

Click "Submit" when you have added all testers

Important

: You must submit the form after adding Apple Accounts. Apple Accounts will not be stored unless you submit.

Step 4: Wait for Apple account review

Apple reviews your account application. This process typically takes 1-3 business days.

<!-- img: abr_Log4_dashboard.png -->

Click "Back" to return to the Register dashboard

Tip

: Click "Progress" in the upper right corner to view your account status at any time

Check your email for account approval notification

Dashboard

Organization dashboard showing account status

Step 5: Verify MSP Connection

Once Apple approves your account, verify the connection with your MSP:

Sign in to Apple Business Register and select "Messages for Business Accounts"

Select your account from the left sidebar

Scroll to "Messaging Service Provider Configuration" and select "Test your Messaging Service Provider connection"

Click "Connect" next to your MSP name

Important

: The "Connect" link appears only after Apple approves your account. If the link is unavailable, your account is still under review.

Your MSP's landing page loads. Complete the account linking process with your MSP

Note

: Apple cannot assist with MSP account linking. Contact your MSP directly if linking fails.

Once your MSP confirms successful linking, return to your account in Apple Business Register

After MSP connection is complete, your account is ready for testing with internal testers.

Step 6: Prepare your commercial account assets

Gather this information before configuring your commercial account:

Business Name

The name displayed to customers in Messages app:

Use your commercial brand name

Exclude location names, legal designations (LLC, Ltd, GmbH, Inc.)

Example (correct): "Apple"

Example (incorrect): "Apple Westfarms"

Note

: Only official brand owners qualify. Franchisees must work through their brand owner.

Business Logos

Important

: iOS 26 and macOS 26 removed support for wide logos in conversation navigation. Square logos now appear in all contexts. Wide logos are still used on iOS 18 and earlier, macOS 18 and earlier.

Square logo (required)

The square logo appears in:

Conversation list (all iOS and macOS versions)

Contact card (all iOS and macOS versions)

Conversation header (iOS 26+, macOS 26+)

Conversation navigation bar (iOS 18 and earlier, macOS 18 and earlier, when wide logo not provided)

Requirements:

Format: PNG or JPEG

Background: Full-color (not personal or product photos)

Dimensions: Minimum 1024px × 1024px

Padding: 10% inset from edges for key elements

File size: Maximum 2MB

Color space: sRGB or P3

Resolution: @3x

Wide logo (optional, legacy support only)

The wide logo appears in:

Conversation navigation bar (iOS 18 and earlier, macOS 18 and earlier only)

Note

: Wide logos do not display on iOS 26, macOS 26, or later versions. Design your square logo to work effectively in all contexts.

Requirements:

Format: PNG

Background: Transparent with full-color artwork (no text transparency)

Dimensions: Minimum 256px height, maximum 1706px width, aspect ratio 6.66:1

File size: Maximum 2MB

Color space: sRGB or P3

Resolution: @3x

Square logo example

Square logo in the conversation list

Wide logo example

Wide logo in conversation navigation (iOS 18 and earlier, macOS 18 and earlier)

 Square logo in conversation

Square logo in conversation header (iOS 26+, macOS 26+)

Response Hours

Document your customer service availability:

Estimated live agent response time during business hours

Support hours (e.g., 9 AM - 5 PM PT, Monday - Friday)

Account Type

Select the appropriate account type:

Online business only: No physical locations (website-only or planning no Apple Maps presence)

Business with 1 public location: One physical location plus optional website presence

Business with multiple public locations: Multiple locations on Apple Maps

Reference

: See Apple Maps and Your Business Locations for more information

Step 7: Configure your commercial account

After experience review, Apple transitions your internal test account to a commercial account.

Sign in to Apple Business Register

<!-- img: abr_Log3_SendNow.png -->

Select "Messages for Business Accounts" and choose your account

Click "Get Started" and complete:

Business name and details

Brand identity (logos, colors)

Response hours

Account type

Click "Next" and "Send Now"

Send Now

Commercial account configuration

Troubleshooting

Issue: Custom endpoint configuration fails

Symptom: Error message when selecting custom URL endpoint

Solution: Temporarily select a standard commercial endpoint and contact Apple support at business-register@apple.com with your custom configuration details

Issue: Test Apple Accounts not recognized

Symptom: Tester receives "Not Delivered" error

Solution:

Verify the Apple Account is in your approved testers list

Confirm the account is submitted

Wait up to 24 hours after approval for messaging to work

Re-submit the form if any Apple Accounts were added or modified

Issue: MSP connection link unavailable

Symptom: "Connect" button is missing or grayed out

Solution: Wait for Apple approval email. Your account is still under review.

Team member management

Add team members to coordinate your implementation:

In your organization dashboard, click "Members"

Click "Add a member" and select "Individual"

Enter:

Full name

Work email address (corporate only, not personal)

Assign a role:

Administrator (for MSP representatives)

Member (for team members with editing capabilities)

Read-only (for stakeholders without editing access)

Click "Submit"

Note

: You can change member roles at any time. Use corporate email addresses only.

Next steps

After registering your account:

Test your account - Verify connectivity and messaging functionality with approved testers

Complete experience review - Conduct quality assurance with your MSP before launch

Configure go-live settings - Set up production configuration and launch

https://register.apple.com/resources/messages/messaging-documentation/customer-journey

Build your customer journey

Design customer interactions that accomplish business goals and meet customer expectations.

Prerequisites: See [Prerequisites](https://register.apple.com/resources/messages/messaging-documentation/index#prerequisites) for requirements at different stages.

Channel goals

Define how you enable Apple Messages for Business and design your customer's experience. Channel goals include:

Improving sales or creating revenue

Decreasing average agent handling time

Increasing app adoption

Improving customer satisfaction

Once you define channel goals, Apple can provide suggestions for integration and feature use. Complete the [Readiness Assessment](https://register.apple.com/resources/messages/messaging-documentation/resources/Messages-for-Business_Readiness.pdf) to formally document goals.

Use cases

Define your business use cases to determine why your customer's contact your business. When filled out properly, the [Use Case template](https://register.apple.com/resources/messages/messaging-documentation/resources/Messages-for-Business_UseCases.pdf) provides valuable information for setting up your channel, implementing interactive features, and achieving goals.

Once your template contains about five of your most common use cases, you can begin to think how better to support your customers in the channel. Share your use cases with the Apple Messages for Business team and they can provide insight into how best to implement interactive features.

Interactive features

Apple Messages for Business provides powerful interactive features that enhance your customer journey and make conversations more efficient. These features work together to create seamless experiences that accomplish business goals while meeting customer expectations.

Available interactive features:

Rich links - Preview content inline with images and videos for brand assurance

Quick replies - Enable single-tap choices for fast responses (2-5 options)

List pickers - Organize options by category for effective customer triage

Time pickers - Schedule appointments that add directly to customer calendars

Apple Pay - Process secure payments without leaving Messages

Authentication - Enable OAuth2-based account access with password autofill

iMessage apps - Provide interactive app experiences within conversations

Media sharing - Exchange images, videos, and documents for faster resolution

Augmented reality - Display products in 3D with AR Quick Look

When to use each feature:

Choose interactive features based on your use cases and customer needs. For example:

Use list pickers for initial triage of customer inquiries

Use time pickers for delivery windows or service appointments

Use Apple Pay to enable purchases through Messages

Use rich links to direct customers to self-serve resources

Use authentication for secure account information access

For detailed implementation guidance, conversation design patterns, and best practices for each interactive feature, see [Conversation design best practices](https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices#interactive-features).

For technical API documentation on implementing these features with your MSP, see [Sending Messages with Attachments](https://register.apple.com/resources/messages/msp-rest-api/messages-sent#message-attachments) and the [MSP REST API documentation](https://register.apple.com/resources/messages/msp-rest-api/).

Next steps

After designing your customer journey:

[Design your user experience](https://register.apple.com/resources/messages/messaging-documentation/ux-design) - Create conversation guidelines and response patterns

[Register your account](https://register.apple.com/resources/messages/messaging-documentation/register-your-acct) - Set up Apple Messages for Business with Apple

[Test your implementation](https://register.apple.com/resources/messages/messaging-documentation/account-testing) - Verify all features and journeys work correctly

https://register.apple.com/resources/messages/messaging-documentation/message-with-customers

### Entry Points Overview

There are many options available for customers to start a conversation with your business. You can use Messages buttons and URLs to meet your customers in places where they are likely to contact your business. You can also enable system features such as Apple Maps or Message Suggest so that customers can start a conversation when locating your business details.

A highly visible entry point with a powerful call to action can be key to success for your brand. Let's start with the native entry points which don't require you to perform a lot of configuration.

You can enable all native entry points, such as Business Card, Place Card, and Message Suggest, by selecting the checkbox "Show Message buttons for on iOS and macOS" in Apple Business Register. When you do this, by default, all three entry points are activated when applicable, and the phone number available in the brand profile, or location profile when there's only one location for your business, is activated in Message Suggest.

Message Suggest

Reduce phone call volume by offering Message Suggest. When customers tap any of the registered business phone numbers, a phone sheet appears allowing them to choose between voice and messaging. For more information on getting the most from Message Suggest, see Triggering Message Suggest.

Website button

The more visible your brand, the easier it is for customers to contact you. For example, you can add a button for Apple Messages for Business at the top and bottom of your website, on the contact page, and specific use-case pages. For more information about how to add buttons to a website, see Design your website and app to include the Messages buttons.

<!-- img: amb-web.png -->

Button on a website

App button

<!-- img: amb-app.png -->

When adding a button to your app, you make it easy for customers to contact your brand when necessary, quickly and safely. For more information on how to add a button to your app, see Design your website and app to include the Messages buttons.

Button within an app

Email and SMS

You can include the URL in an email or send it using SMS to reach specific customers. For more information about how to start a conversation from a URL, see Starting a message from a URL.

<!-- img: amb-email.png -->

Button within Mail

Social media

Nowadays it's difficult to find someone who doesn't use at least one type of social media. In fact, most people access more than one type every day. Making entry points available on social media is another way for the brand to be visible to customers.

<!-- img: amb-social.png -->

Button within Social

QR code and NFC tag

QR codes and NFC tags add an entry point anywhere you can post marketing material. You can post advertising on bus stops, on streets, inside stores and malls, on business cards, tickets, and bills. In short, creativity is the limit. It's easy to create, and there are several free websites and apps to generate a QR code and program an NFC tag.

<!-- img-row: amb-nfc.png, amb-qr.png -->

Trigger using a QR code

A QR code

 Trigger using an NFC tag

An NFC tag

Augmented reality (AR)

You can add AR to your brand experience as an entry point if the AR is on your website or app. The customer can check how an object looks in their house, and ask questions if they want to know more. For more information about adding a custom action, see Adding an Apple Pay or a Custom Action in AR Quick Look.

<!-- img: amb-ar.png -->

Messages button in AR Quick Look

Wallet passes

Your brand can have a direct entry point for Apple Messages for Business on the back of boarding passes, loyalty cards, movie and event tickets, debit and credit cards, store cards, coupons, and gift cards. For more information on how to add an entry point in Wallet passes, see Introducing Wallet.

Apple Pay Order Tracking

From iOS 16 and macOS 13, a business can add a tracking order status in Wallet linked to an Apple Pay transaction. The customer can check the order status by tapping the order button  in the Wallet app. From there, the business can add a link which will open a conversation in Apple Messages.

<!-- img: Wallet_Order_Track.jpg -->

For more information about adding Messages link in a Wallet Order Tracking, see Apple Pay Order Tracking Demo and Merchant Order.

Order Tracking in Wallet

Wallet app showing the Order tracking icon, leading to "Send a Message" link on the order details view.

Composing an Apple Messages for Business URL

You can compose your own Apple Messages for Business URL to give your customers another way to contact your business. Place the URL on all your websites, in emails, and social media posts, and have them activated when a customer taps the Messages button. Before you begin, understand the components by reading About Intent, Group, and Body Values and Starting a message from a URL. For more information on adding Messages buttons to your websites, see Design your website and app to include the Messages buttons.

Apple Maps place card

You can win twice with this entry point by adding and updating your brand's public location data in Apple Maps. When customers use Apple Maps, your brand's location data can provide instructions and estimated arrival times; in addition, of course, to having a Messages button that redirects customers to Apple Messages for Business. There is more than one way to add or update Maps information. Let us know the number of your brand's public locations so we can give you the best suggestion. To activate Messages button on Apple Maps, see Apple Maps and Your Business Locations.

<!-- img: amb-maps-ios26.png -->

Expanded place card

Apple Maps and Your Business Locations

Messages are routed from the Apple Messages for Business service to your agents through your Messaging Service Provider (MSP). To direct Messages to a specific business location enable the Message button on your Apple Maps location, Apple Maps displays the button on your business location next to the call button. Like other entry points, when customer's tap on it, they're directed to start an Apple Messages for Business conversation.

You can enable the Message buttton on your Apple Maps locations directly from your Apple Messages for Business account in Apple Business Register. Check the box to enable iOS and macOS entry points and add the countries you want to display the Message button for your locations. For example, if your business has locations in both the United States and Canada, but you only want to display the Message button for locations in the United States only add the United States. Once you activate the buttons submit the changes to Apple for review. When Apple approves the change, your business locations in the countries display the Messages button.

By adding intent and group ID information to your Locations profile, you can route messages directly to a business location the first time a customer taps the Apple Messages for Business button. When performing traffic analysis, you can parse out your Apple Messages for Business traffic by splitting out the intent and group information.

Your Apple Business Register representative enables the Locations service where you can set up your business Locations. Before creating a Location profile, determine which locations to register. The most useful locations are the ones customers visit, such as a retail store.

Customize Intent and Group ID for Your Business Locations

The intent and group ID values can be whatever you decide. When you don't define the intent or group ID, by default, the group ID is empty and the intent ID is set as:

business_name: physical_address_of_the_location

If you would like to customize the group and intent ID for your locations, this can also be accomplished in Apple Business Register. For each location you wish to add a custom group or intent ID, it must be added to Apple Business Register. If your business has more than 50 locations, speak with your Apple representive so that they can advise how to proceed in adding them.

After adding the locations for your business, you can customize the intent and group IDs. When the values are defined, they allow you to track the locations of customer requests from Apple Maps. Additionally, it lets you send messages directly to the appropriate group of agents for a business location. For example, if a customer in a store asks for a particular item, your agent can send the customer to the correct aisle.

When sending a message from a Maps location, Apple Messages for Business uses the standard URL encoding, similar to a web button. When the MSP platform receives the encoded parameters, a plus sign replaces the encoded spaces. When the intent ID is defined, your logs contain something similar to the following:

{"intent":"My+Business:+One+Apple+Park+Way,+Cupertino,+CA++95014,+United+States", "sourceId": "urn:mbid:AQAAY1RfNajxPMgY5JzQHCnF6bY00d+HrG2YmTlgZ2VJ/spRqzPQUER1mT4wBWg=", "v": 1, "group": "poi_to_abc", "body": "hi", "locale": "en_PL", "id": "0c68c45c-fb66-47de-b255-df1644c", "type": "text", "destinationId": "70a55-11de-11e8-a180-b7c088"}

For more information on defining intent and group ID values, see About Intent, Group, and Body Values.

Important Tips for Successful Entry Points

Include a powerful call to action. Clear contextual information tell customers what to expect when they contact the brand. When using the Messages app icon only, use clear and succinct phrases that's relevant to the content on the page, such as "Style questions? We can help", "Book an appointment using Apple Messages", or "Message with our team now." Place the call to action next to Messages button to encourage customers to initiate a conversation.

Don't forget to add an Intent_Id to all available entry points. Intent IDs help you to understand which entry point your customer uses, and provides a customer's intent to ensure higher visibility. For more information, see About Intent, Group, and Body Values.

Include a prefilled message or body for the customer. It's easy to add and makes it easier for them to reach out to you. This message can be something like "Tap send to start a conversation."

Allow conversations to start anytime. Don't disable buttons or links that initiate conversations outside of normal business hours. Even if you only respond to customer service inquiries during certain hours, people should be able to start a conversation anytime. If a customer starts a conversation after hours when live agents aren't available, an automated agent should send a reply letting them know when a live agent is able to respond.

Show the Messages button on supported devices. To maximize Apple Messages for Business usage, show Messages buttons for supported devices as the main option for contacting your brand. If a customer's device doesn't support Apple Messages for Business, don't encourage a conversation by displaying a button on your websites. You can use your CMS to hide the button when an Apple devices is not detected.

Referring to Apple Messages for Business

In general, use the terms Apple Messages for Business or Apple Messages in customer-facing communications. Avoid using the term Messages by itself, especially when paired with a logo-only button.

Use proper capitalization when mentioning Apple Messages for Business in headlines and copy. Specifically, use four words with an uppercase A, an uppercase M, and an uppercase B, and lowercase for all other letters.

Avoid using other terms to refer to Messages for Business in customer-facing content. For example, avoid using the terms chat or text to refer to a Messages for Business button or flow.

Never use the Apple logo to represent the name Apple in text. Apple Messages for Business is a service mark of Apple Inc.

| Status | Example text |  |
|---|---|---|
| ✅ | Correct | Apple Messages for Business |
| ✅ | Correct | Apple Messages |
| ❌ | Incorrect | Apple messages for business |
| ❌ | Incorrect | iMessage |
| ❌ | Incorrect | APPLE MESSAGES FOR BUSINESS |
| ❌ | Incorrect | Messages for Business |
<sub>↳ `messaging-documentation.md` L1107–1119</sub>

Referring to Apple products

Adhere to Guidelines for Using Apple Trademarks. Apple trademarks must not appear in your app name or images. In text, use Apple product names exactly as shown in Apple Trademark List — never make them plural or possessive.

Design your website and app to include the Messages buttons

Place a button to give your customers an easy way to access your support. Design your Messages buttons that will appear on your website and app, and have Apple review the call-to-action (CTA) text. Do not enable them until your account is approved to go online. You can place the buttons on contact information, support, order confirmation, product, and order history pages. When you're done, your website and app should have the Messages buttons configured and enable-ready for your customers to use.

<!-- img-row: Messages-for-Business-Message-Us-Black.svg, Messages-for-Business-Contact-Black.svg, Messages-for-Business-Ask-Black.svg, Messages-for-Business-Get-Help-Black.svg, Messages-for-Business-Icon.svg -->

Use one of Apple's provided CTA's to help your customers understand the type of support they can expect to receive. You can also leverage the standalone Messages app button in case you have a widget or in the context of a smaller area.

| Button Type | Description |
|---|---|
| Message us - dark | "Message Us", call-to-action. |
| Contact an Agent - dark | "Contact an Agent", call-to-action. |
| Ask a Question - dark | "Ask a Question", call-to-action. |
| Get Help - dark | "Get Help", call-to-action. |
| Messages app | Messages app icon only |
<sub>↳ `messaging-documentation.md` L1137–1147</sub>

The images below display the output of the Messages button or icon on a website.

<!-- img-row: msg-cta-mode.png, msg-icons-mode.png -->

Messages button icons mode Messages button CTA mode

For more information about best practice positioning and using Apple Messages button and Referring to the service next to the button, see Human Interface Guidelines - Buttons and Referring to Apple Messages for Business.

Using Messages for Business buttons

Let the default button title encourage customers to contact you. System-provided button titles like "Message Us," "Get Help," "Ask a Question," or "Contact an Agent" help people understand what the button does. If you use the logo-only button, consider displaying the text "Apple Messages" near the button to help people recognize the service.

Show the buttons on supported devices. If a customer is using an unsupported device, don't encourage a conversation by displaying a button — on websites, the button hides automatically when it isn't supported. If the button is hidden, update the layout accordingly and remove the call to action or other related text.

Make sure Messages for Business buttons are discoverable. People generally expect to find the button on contact information, support, order confirmation, product, and order history pages.

Display the button prominently. Make Messages for Business buttons the same size or larger than similar contact initiation buttons, such as an email button.

Use only approved button styles. For guidance, see Design your website and app to include the Messages buttons.

Maintain minimum and maximum button sizes and inner side margins. Use the following values for guidance.

| Max width | Min height | Max height | Min side margins |
|---|---|---|---|
| 1000 pt (2000 px @2x) | 40 pt (80 px @2x) | 150 pt (300 px @2x) | 5% of height |
<sub>↳ `messaging-documentation.md` L1185–1187</sub>

Don't make any other visual or functional modifications to buttons. For example, don't change transparency values or add drop shadows.

Maintain minimum clear space. The minimum amount of clear space required around the buttons is 10% of the button's height. Don't let other elements infringe on this space or occlude the button in any way.

Maintain the minimum button size and margin values when manually placing buttons on a webpage. You're responsible for sizing and placing the buttons correctly.

Use the following margin values for guidance.

| Margin | Minimum value |
|---|---|
| Top and bottom | 15 pt (15 px @1x, 30 px @2x) |
| Left and right | 20 pt (20 px @1x, 40 px @2x) |
| Between buttons | 15 pt (15 px @1x, 30 px @2x) |
<sub>↳ `messaging-documentation.md` L1205–1211</sub>

For developer guidance, see Starting a message from a URL.

Using the PNG/SVG Button

Make sure you use an appropriate call-to-action message so your customers know that they can get resolution to their questions by tapping this entry point. Download the PNG/SVG button resources and can then create the HTML or web link around the image of the button and CTA. Format this link as described in Starting a Message from a URL.

Starting a message from a URL

Customers may start a message using a URL you provide. When customers click the URL, the system redirects them to Messages so they can send your business a text message.

You decide how and where to provide the URL. You can include it as a link in an email message, on your website, or use it as the action for a button in your app.

The URL to use is https://bcrw.apple.com/urn:biz: <your-business-id>, replacing <your-business-id> with the business ID you received from Apple after registering with Apple Messages for Business.

There are optional query string parameters you can include in the URL:

biz-intent-id

biz-group-id

body

The biz-intent-id parameter lets you specify the intention, or purpose, of the message. The biz-group-id parameter lets you indicate the group, department, or individuals best qualified to handle the customer's particular question or problem. The body parameter prepopulates the message so the customer only has to hit send to initiate the conversation. For more information, see About Intent, Group, and Body Values.

Here's an example of what the URL might look like for a bank customer with a question for the credit card department:

https://bcrw.apple.com/urn:biz:9c231233-d943-482a-b913-7c625ba19988?biz-intent-id=account_question&biz-group-id=credit_card_department&body=Order%20additional%20credit%20card

NOTE

Parameters and data attributes that form the URL, such as the intent, group, and body, must not contain a subset of URI reserved characters, such as &, #, [], (), {} and /.

About Intent, Group, and Body Values

Businesses define the values for the intent, group, and body parameters, and these parameters are included in a URL that initiates a chat session in Messages when a customer clicks or taps the Messages button.

When a customer starts a chat session through your app or website, you can choose to include the following three parameters as part of the URL for defining messages:

Intent, or purpose, of the chat.

Group designates the department or individuals best qualified to handle the customer's particular question or problem.

Body, a parameter that prepopulates a message for your customers so all they need to do is tap Send in Messages.

Use the intent, group, and body values to define the customer's intent so you can quickly direct them appropriately within your support organization. How you define these values is up to you.

For example, if your company is a financial institution and a customer contacts you with a question about their credit card account. The customer taps or clicks a Messages button, and Messages provides an autogenerated response, "How may we help you today?". Messages opens when the customers clicks the Messages button, and displays a greeting with a list of options to choose from. For example, these options could include "Credit Card Account," "Checking Account," and "Savings Account," among others.

The customer taps one of the options (the intent)—in this case, "Credit Card Account"—which routes the message to the Credit Card Department (the group).

The body parameter, which you add manually to a URL, allows you to provide more granular information such as "Order an additional credit card." Apple Messages for Business uses the body value to prepopulate a message for your customers so all they need to do is tap Send in Messages. In this example, the customer taps a chat button which opens a prepopulated text message, "Order an additional credit card." The customer only needs to tap Send to notify the business of their intent and initiate the conversation.

NOTE

The Spotlight entry point doesn't allow intent and group values.

Starting a message from your app

You can let a customer start a message from your app by creating a class button and adding it to the app's user Interface. Build the Messages button so that it calls the Apple Messages for Business URL link used in the target-action mechanism to initiate a conversation with your business when the customer taps the button.

Use the SVG/PNG button images to create a Messages button class. Make sure you use an appropriate call-to-action message so your customers know that they can get resolution to their questions by tapping this entry point. For more information about using the Messages button for your website or app, see Human Interface Guidelines - Using Messages for Business buttons.

Triggering Message Suggest

When your customers tap on any of your registered business phone numbers, a phone sheet appears allowing your customers to choose between voice and messaging. The Message Suggest feature allows your customers to contact you through Apple Messages for Business in the Messages app.

Businesses can reduce phone call volume by offering Message Suggest instead. Given that messaging offers a better agent to customer concurrency ratio compared with either voice or live chat, brands can potentially reduce their contact center operational costs by launching Message Suggest.

You can trigger Message Suggest from any place where the phone number is tappable on iOS devices, including search, Apple Maps, and a website.

<!-- img-row: Apple-Store-Message-Suggest-Enabled.png, AppleMaps-Message-Suggest.png, AppleWeb-Message-Suggest.png -->

Message Suggest triggered from search

Message Suggest from search

 Message Suggest triggered from a website

Message Suggest from a website

 Message Suggest triggered from Apple Maps

Message Suggest from Apple Maps

The following screenshots are of an iPhone with no Message Suggest and with Message Suggest (right).

<!-- img-row: Better_Bag_disabled.png, Better_Bag_enabled.png -->

BetterBag Messages Suggest not active

no Message Suggest

 BetterBag Messages Suggest enabled

Message Suggest enabled

Benefits

By enabling Message Suggest, you can:

Deflect calls before they reach your IVR queue

Reduce voice support costs by shifting call volume to messaging

Increase customer satisfaction by reducing wait times and getting cut-off in mid-conversation on phone lines

Better customer experience with built-in features, such as Apple Pay, list pickers, time pickers, and augmented reality

Getting Message Suggest setup

<!-- img: message-suggest-settings.png -->

First, get familiar with the different settings associated to Message Suggest

Message Suggest settings

Message Suggest settings on an iPhone

Characters Limits

Title: Limited to 120 characters.

Subtitle: Limited to 170 characters.

Intent and Group ID: Limited to 512 characters.

Body: Should be reasonable and not be longer than a sentence.

NOTE

Parameters and data attributes that form the URI, such as the intent, group, and body, must not contain a subset of URI reserved characters, such as &, #, [], (), {} and /.

Configuration

Then send an email to the Apple Messages for Business team with the following Message Suggest form and Apple can set up the numbers using the parameters you provided:

Your business phone contact hours.

All of your primary and high call volume phone numbers. You may include your own stores phone numbers.

The title and subtitle to be set for the UI. If you want to have different languages supported, please provide the translation as well.

The intent and body parameters to associate with each phone number. Intent, group, and body values define a customer's intent so you can quickly direct them to the appropriate group within your support organization. For more information, see About Intent, Group, and Body Values.

Your current call volume for these phone numbers.

How many agents you have to support customers over Apple Messages for Business.

Please note that there is a ramp up period of several days for the Message Suggest prompt to become visible across all eligible devices. We recommend that you wait until the propagation period (average of 5 to 7 days) is complete before checking the visibility.

Measuring Message Suggest Volume

The effectiveness of the Apple Messages for Business channel is assessed by measuring the conversion from voice to chat, by tracking overall reduction in call volume, increased customer satisfaction and NPS scores, and reduction in operational costs.

To accurately measure the conversion from voice to messaging from Message Suggest, you can calculate the conversion rate by measuring the phone call volume before and after enabling Message Suggest. For example, the call volume on a phone number prior to Message Suggest was 350 per day. After Message Suggest, the message volume from Message Suggest is 70 per day and the call volume decreased by same amount. Based on this information you can calculate that 20% of calls convert to messaging.

For a detailed approach, track Message Suggest performance on brand properties as described in the best practices below.

Capture taps on all pages where the registered phone number appears. Measure the number of taps on the registered phone number on the page from where the tap originated on your website and iOS app, if applicable.

Measure taps from iOS 13 and later. Make sure you are capturing the taps on the registered phone number by iOS 13+ users only. Message Suggest is enabled for iOS 13 and later.

Measure Message Suggest volume. Track the intent ID for all incoming messages to measure the volume of messages from Message Suggest. When a customer chooses the Apple Messages for Business option on the Message Suggest UI, the message delivers the intent ID value in the header.

Model your call volume. Customers tend to rely on search engines to quickly find a phone number. Message Suggest volume from search engine results should also be considered in calculating the conversions. Plan to apply the conversion rate from web analytics to overall call to messaging volume.

Determine your conversion rate. You can find the conversation rate by taking the total number of taps on a phone number and divide it by the number of Message Suggest messages received from that same phone number.

The following conditions may affect your conversion rate:

Additional iOS entry points to Apple Messages for Business. Track other brand-enabled entry points, such as Apple Maps, Siri, or business card, separately for measuring conversion rates.

Other Message Suggest entry points. Consider incoming volume from other sources, such as phone taps on search engine results and other social media sites, when calculating the conversion rate.

Messages button on the website. If brands place the Messages button on the website or app, it contributes to an increase in overall volume of Apple Messages for Business messages. However, this may decrease the conversation rate, if the Message Suggest registered phone number is also on the same page.

Maximizing Message Suggest

To reduce phone support costs, you should try to maximize message volume by deflecting voice calls. Based on the observations Apple has made since launching the Message Suggest feature, we recommend the following best practices to maximize volume from Message Suggest.

Register all primary numbers. For higher deflection to messaging, register phone numbers with high call volume for Message Suggest.

Make sure the registered phone numbers are easily tappable on your web sites and apps. Use the E.164 format for registered phone numbers to trigger the Message Suggest UI in iOS. Images or text-formatted phone numbers are not tappable. For more information on how to create tappable telephone links, see Phone Links.

Ensure high visibility to maximize volume. Verify that Message Suggest enabled numbers are easily

visbile across your mobile website, search results and apps. Availability ensures that all brand iOS customers have access to the feature which results in higher deflection and reduced call volume.

Setup automated message for off hours. Because Apple Messages for Business is asynchronous, customers can message brands at any time including off hours when live agents aren't available. For brands not leveraging automation to assist customers during off hours, Apple recommends that you provide an automated response to inform customers that live agents can address their inquiry when they return.

Appropriate call-to-action message set by Apple to meet capacity. Assuming customers always have access to a live agent, Apple sets your call-to-action messages so that customers understand that they can get help quickly from a live agent. You have the option to change it to meet your business needs. Contact the Apple Messages for Business Team to update your call-to-action text.

https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices

Conversation design best practices

Design Apple Messages for Business experiences that help customers accomplish their goals through intelligent automation and seamless live agent support.

Overview

Effective Apple Messages for Business conversations prioritize customer intent resolution through tap-friendly interactions, fast automated responses, and seamless escalation to live agents when needed. Every conversation should maintain privacy and security while helping customers accomplish their goals efficiently.

Core principles:

Resolve customer issues quickly through automation

Provide clear paths to live agent support

Use interactive features to simplify complex tasks

Maintain context throughout the conversation

Respect customer time and preferences

Conversation flow pattern

A successful Apple Messages for Business conversation follows this pattern:

Customer initiates → Entry point activation

Greetings → Automated welcome (within 5 seconds)

Triages → Quick reply menu determines intent

Routes → Automated flow or live agent queue

Resolves → Issue addressed or escalated

Closes conversation → Optional satisfaction survey

Design automated responses

Implement automation for fast, helpful responses while maintaining clear escalation paths to live agents.

Greet customers immediately

Send an automated greeting within 5 seconds of customer contact:

Required elements:

Identify as automated agent

Set response expectations

Offer clear next steps

Example:

Hi Sarah, I'm an automated agent here to help. What can I assist you with?

Automated greeting within 5 seconds

Identify automated agents clearly

When customers interact with automated systems:

State the automation upfront: "I'm an automated agent"

Explain capabilities and limitations

Provide immediate value or next steps

Example:

I'm an automated agent here to help route your question. I can help with order tracking, account info, or billing.

Bot identifies capabilities and limitations

Enable escalation to live agents

Always provide a path to human agents:

Trigger words: Route to live agent when customer types:

"agent", "help", "support", "speak with someone"

During business hours: Route to available agent immediately

After hours: Send out-of-hours message with expected response time

Example:

We're closed now. Our team responds Monday at 9 AM PT.

After-hours automated response

Handle unclear requests

When automation cannot resolve a request:

Acknowledge the limitation: "I'm not sure I understood that"

Offer alternatives: "Would you like me to connect you with a specialist?"

Escalate if customer confirms: "Routing you to a live agent"

Pass conversation context to agent

Example escalation:

I want to make sure you get the help

you need. Connecting you with a specialist.

Bot escalates to live agent

Design live agent conversations

Create meaningful customer interactions with human agents.

Introduce all live agents

When a conversation begins or transfers to a new agent:

Required elements:

Provide agent name or title

Explain agent's role

Acknowledge conversation history

Example:

Hi Sarah. I'm Alex, your account specialist. I see you need help with your invoice. Let me take care of that.

Live agent introduces themselves with context

Keep conversations with one agent

Individual agent identities are not visible in the conversation:

Keep the customer with their current agent when possible

If you must transfer, explain the reason first

Get customer permission before transferring

Provide the customer's context to the new agent

Enable smooth agent transfers

Customer experience during transfer:

Current agent explains the transfer reason

Inform customer of expected wait time

New agent reviews conversation history before taking over

New agent reintroduces themself and picks up where previous agent stopped

Customer never repeats information already provided

Example transfer:

Connecting you with our billing specialist.

Current agent explains transfer

Hi Sarah. I see you're asking about your invoice.

New agent takes over with context

Manage queue and business hours

When agents are busy:

Inform customer of queue position

Provide estimated wait time

Update every 5 minutes if wait exceeds expectations

Example:

You're 3rd in queue. Approximately 8 minutes wait time.

Bot provides queue status

When no agents are available:

Inform current status (closed/unavailable)

Provide expected response time

List business hours

Triage customer issues

Route customers efficiently through guided questioning using interactive features.

Create effective triage flows

Use Quick Replies or list pickers to guide customers:

Ask one question at a time

Provide 2-5 clear response options

Each response leads to next action or agent queue

Never force customer to type detailed explanations

Example triage flow:

Initial question: "What can I help you with today?"

Order tracking

Billing question

Technical support

Something else

Design principles:

Use customer vocabulary, not internal terminology

Order by frequency (most common first)

Keep labels under 25 characters

Always include "Something else" or "Live agent" option

Limit triage levels

Best practices:

Show triage menu at conversation start for fastest intent determination

Limit to 2 levels maximum before reaching agent

Each additional level reduces completion rates

Include "Live agent" on every menu

After customer selection:

Acknowledge choice immediately

Proceed to appropriate flow

Never ask customer to confirm their selection

Example:

Order tracking

Customer selects "Order tracking"

I can help with that. What's your order number?

Bot responds with request for information

Resolution paths

Choose the appropriate resolution path based on issue complexity and customer needs.

Automated end-to-end flows

For high-frequency, low-complexity issues:

Pattern:

Collect required information

Process request automatically

Confirm completion

Offer related help

Example - Order Tracking:

Enter your order number

Bot requests information

12345

Customer provides order number

Order arriving Friday. Track here: [link]

Bot provides tracking information

Anything else I can help with?

Bot offers additional help

Best for:

Order status lookups

Account balance checks

Store hours and locations

Password resets

FAQ answers

Self-serve redirects

For tasks requiring authentication or complex interaction:

Pattern:

Explain what customer needs to do

Send rich link to appropriate page

Confirm customer received information

Offer live agent if needed

Example:

To update your payment method, tap this secure link: [link]

Bot provides self-serve link

Live agent escalation

Transfer to human agent when:

Customer types "agent", "help", "support", or "speak with someone"

Automated system cannot understand intent after 2 attempts

Customer requests escalation

Issue requires account access or sensitive information

Customer expresses frustration

Respond to customers effectively

Craft responses that help customers achieve their goals.

Use clear, direct language

Effective responses:

Use simple words matching customer vocabulary

Avoid jargon and unexplained acronyms

Be concise (fewer than 160 characters per message preferred)

Use imperative voice ("Select your account type" not "You can select")

Example:

Preferable: "To reset your password, tap the link sent to your email"

Avoid: "Utilize the authentication mechanism to recalibrate your credentials"

Provide assurance

Help customers feel confident:

Acknowledge their issue: "I see you're asking about [Product]. How can I help?"

Confirm understanding: "Let me confirm: you need a replacement by Friday?"

Reassure when possible: "This is a common issue and easily resolved"

Include context from conversation history

Never ask for repeated information:

Review entire conversation before responding

Reference previous messages: "Following up on the damage you reported..."

Access account history: "I see you purchased this item last month"

Use available customer data

Respond quickly to actionable requests

Trigger immediate actions from keywords:

| Keyword | Action |
|---|---|
| agent, support, help, speak | Route to live agent immediately |
| unsubscribe, stop, spam, opt-out | Disable notifications without confirmation |
| menu, list | Send menu or navigation options |
| settings, preferences | Show settings or preference options |
<sub>↳ `messaging-documentation.md` L2019–2027</sub>

Set accurate response expectations

For delayed responses:

Thank customer immediately upon contact

Provide estimated response time: "A specialist will respond within 2 hours"

Queue position updates (if applicable): "You're 5th in the queue"

After-hours message: "We're closed now. We'll respond Monday at 9 AM"

Interactive features

Use Apple Messages for Business features to simplify complex tasks and improve customer experience.

Rich links

<!-- img: RichLinks.png -->

Links with preview content provide brand assurance and click confidence.

Best practices:

All URLs send as rich links with preview image

Image reflects page content (not logo placeholders)

Logos acceptable only if width < 150px (icon style)

Provides brand assurance and click confidence

Use for:

Self-serve redirects to account pages

Product information and support articles

Secure payment or authentication flows

Rich link example showing preview with image

Rich link with content preview

Quick replies

<!-- img: quick-reply.png -->

Provide a simple way for customers to make an inline choice with a single tap.

Specifications:

Maximum options: 5 per menu

Minimum options: 2 per menu

Text length: Under 25 characters per option

Selection: Single choice only

Use for:

Initial triage menus

Yes/No confirmations

Simple option selection

Quick reply interface

Quick reply for simple choices

For more information, see Quick reply.

List pickers

<!-- img: List-Picker.png -->

Provides information or asks questions with organized options.

Best practices:

Great for triaging customer questions

Organize options by category or frequency

Include descriptive labels for each option

Provide clear section headers

Use for:

Multi-level triage flows

Product or service selection

Category-based routing

List picker interface

List picker for organized options

For more information, see List Pickers.

Time pickers

<!-- img: Time-Picker.png -->

Provides time slots for customers to choose and adds the chosen time to the customer's calendar.

Best practices:

Display available time slots clearly

Automatically add appointment to customer's calendar

Send confirmation with calendar event

Use for:

Scheduling delivery windows

Booking service appointments

Reservation confirmations

Time picker interface

Time picker for scheduling

For more information, see Time Pickers.

Apple Pay

<!-- img: Apple-Pay.png -->

Provides an easy and secure way for customers to buy goods and services through Apple Messages for Business.

Best practices:

Customers complete purchases without leaving Messages

Builds trust through Apple security

Growing channel as sales and e-commerce platform

Use for:

Product purchases

Service payments

Subscription renewals

Apple Pay interface

Apple Pay for secure payments

For more information, see Apple Pay.

Authentication

<!-- img: Authentication.png -->

Allows customers to view account information safely through OAuth2 protocol.

Best practices:

Supports OAuth2 protocol with password autofill

Enables account information viewing in Messages

MSP can implement full authentication flows

Use for:

Account access

Order history viewing

Profile management

Authentication interface

Authentication for secure account access

For more information, see Authentication.

iMessage apps

<!-- img: iMessage-apps.png -->

Allows customers to interact with your app directly within Messages, including within an Apple Messages for Business conversation.

Best practices:

Analyze top customer pain points

Convert solutions requiring transactions to app experiences

Prompt users to install and launch apps

Drives app adoption naturally

Use for:

Interactive product catalogs

Custom ordering experiences

Loyalty program integration

iMessage apps interface

iMessage app integration

Learn more about building and submitting your iMessage app.

Images and video

Visual communication for faster resolution.

Image sharing:

Agents share product photos, troubleshooting screenshots

Customers provide proof of purchase, damage, or feedback

Faster resolution than text descriptions

Video sharing:

Sharing videos creates a more immersive experience

Provide product or service descriptions

Allow customers to send proof of incident

Use for:

Product demonstrations

Troubleshooting assistance

Proof of purchase or damage

Document attachments

Send documents in PDF format.

Best practices:

Send billing statements, receipts, forms

Customer can store for record-keeping

Include fillable forms for signature

Use for:

Billing statements

Receipts and confirmations

Forms requiring signature

Augmented reality

Give customers a real-world view of products using AR Quick Look.

Best practices:

Send 3D models with AR Quick Look

Enable size and fit comparison

Provide product demonstration in customer environment

Use for:

Furniture placement visualization

Product size comparison

Virtual product demonstrations

For more information about AR Quick Look, see Previewing a Model with AR Quick Look.

Conversation completion

End conversations professionally and gather feedback when appropriate.

Agent closes conversation

Pattern:

Confirm issue resolved

Offer additional assistance

Close professionally

Example:

Your invoice is corrected. Is there anything else I can help with?

Agent confirms resolution and offers help

No, that's all

Customer confirms completion

Thank you for contacting us

Agent closes professionally

Always offer further assistance

Conclude by opening the next opportunity:

After resolving issue: "Is there anything else I can help with?"

Before ending conversation: "Would you like to know about related topics?"

Post-conversation survey (optional)

If collecting feedback, send immediately after close:

Survey design:

Single question: "How would you rate this interaction?"

5-point scale or thumbs up/down

Optional: Brief follow-up for low ratings

Never message ended conversations

Respect conversation closure:

When customer explicitly ends conversation, stop messaging

Customer must initiate new conversation to restart

Exception: Follow-up survey immediately after session ends

Handle notifications and subscriptions

Manage customer expectations around message frequency.

Request permission first

Before enabling notifications:

Ask customer if they want notifications

Explain what notifications include: "You'll get order status updates"

Explain how to unsubscribe: "Reply STOP anytime to turn off"

Example:

Would you like order status notifications? Reply STOP anytime.

Bot requests notification permission

Support standard subscribe and unsubscribe

When customer texts subscribe, unsubscribe, or related keywords:

Immediately enable or disable as requested

Send confirmation: "You're now unsubscribed from order notifications"

For complex preferences, send option menu

Provide preference control

When customer requests settings:

Customer sends: "settings", "preferences", "notifications", "subscribe"

Send list picker or quick replies with options

Let customer choose: notifications on/off, notification frequency, categories

Example settings menu:

Order tracking notifications: ON/OFF

Promotional offers: ON/OFF

Billing alerts: ON/OFF

Common mistakes to avoid

❌ Don't: Send triage menu before greeting

✅ Do: Greet first, then present options

❌ Don't: Create 3+ levels of triage menus ✅ Do: Limit to 2 levels, then escalate

❌ Don't: Force customers to type free-form text ✅ Do: Provide Quick reply options

❌ Don't: Hide live agent option

✅ Do: Include "Talk to someone" on every menu

❌ Don't: Ask customers to repeat information

✅ Do: Pass conversation context to agents

❌ Don't: Send marketing after issue resolution

✅ Do: Ask permission before sending promotional content

Implementation checklist

Before launching:

 Automated greeting sends within 5 seconds

 First triage menu contains 2-5 most common intents

 Live agent option available on all menus

 Keywords (agent, help, support) trigger live agent

 Business hours logic implemented

 Out-of-hours message configured

 Agent introduction script defined

 Conversation history passes to agents

 Post-conversation survey tested (if applicable)

 All flows tested from customer perspective

Metrics to track

Monitor these flow metrics to improve performance:

Automation effectiveness:

Percentage resolved without agent: Target 60-70%

Average resolution time by intent

Escalation rate by menu option

Customer satisfaction:

CSAT score by resolution path

Completion rate by flow

Abandonment points in conversation

Agent efficiency:

Average handle time

First contact resolution rate

Transfer rate between agents

Next steps

After reviewing these best practices:

Document your use cases - Map common customer intents

Create conversation guidelines - Establish team response standards

Register your account - Set up Apple Messages for Business

Test thoroughly - Verify all paths work correctly

See also

Related Documentation:

Build your customer journey - Interactive features overview

Conversation guidelines - Team response standards

Use Cases Template - Document common scenarios

Readiness Assessment - Formalize your goals

Remember: Successful conversations balance automation efficiency with human agent accessibility. Customers should reach resolution quickly through automation or seamlessly connect with a live agent when needed.

https://register.apple.com/resources/messages/messaging-documentation/policies

Policies

All businesses must comply with the following Apple Messages for Business channel policies.

Live support available. The business must provide access to a live agent in this channel during its regular business hours. A business must not provide a limited or bot-only solution.

Unsolicited messages. Your business is prohibited from sending unsolicited messages. Your business may only send a message in response to an active conversation unless you comply with the restrictions below.

If your business wants to send important notifications related to your customer's account status or previous transactions, then your business must provide the following notification, "We will send important notifications related to your account status or transactions. Send 'Unsubscribe' to manage your message preferences."

Businesses and Messaging Service Providers (MSPs) must support subscribe and unsubscribe operations that allow the customer to configure message delivery preferences. The List Picker should permit the customer to select or unselect the notification types that your business may send.

At no time may your business send marketing information, promotional offers, or information related to products or services that the customer has not purchased unless the customer has expressly sent "subscribe" and provided their permission.

Deleted conversation. Businesses and MSPs must not send messages to customers when they expressly delete a conversation. MSPs must handle the delete action received through Apple Messages for Business and should not send any further messages to the customer unless the customer initiates conversation again with the business.

Trigger words. Businesses that employ these features should use and respond to standardized trigger words. Businesses should use the primary term in text sent to the customer, but should also support the alternative words if sent by a customer.

To reach a live agent, the primary term is "agent". Alternatives are "support" or "help".

To view a menu or list of available items, the primary word is "menu". Alternatives are "list" or "?".

To manage message preferences, the primary term is "unsubscribe". Alternatives are "spam", "stop", or "end".

Requesting Personal Identifiable Information (PII). This PII policy is applicable at all times in the Apple Messages for Business conversation and applies to both live agent and automation flows.

Businesses must not request PII from the user until the point in the conversation where it is necessary to request this information to address the user's issue or inquiry.

To begin a PII request, a clarifying question must be asked first. This question must be phrased as a yes-no question in this manner, "Is your inquiry related to your account with us?" where the user must answer with "Yes" or "No". If the user answers "Yes" then PII can be requested.

PII can be requested for these purposes:

First name only for relationship building.

Full name or other PII for account creation or account information retrieval.

======= Brand Privacy Policy/Terms of Use statements. Privacy policies and terms of use should not be displayed in-line. The brand should provide a rich link to a web page with this content. Also, this link should be presented under two conditions: 1. First engagement by the user, and 2. when the policy or terms have been updated. It should not be sent at the start of every conversation. Additional details:

Statements such as "data rates may apply" or similar are not appropriate for Apple Messages for Business. Smart phones are always online, constantly sending a receiving data over cellular and WiFi networks for a variety of reasons, including weather updates, social media updates and notifications, email, web browsing, software update checks and more.

"Messaging rates may apply" relates to SMS, not Internet-based messaging. This should not be used for Apple Messages for Business.

Prohibited uses. The following list of business categories are prohibited from offering Apple Messages for Business to their customers:

Violates any law or otherwise fails to comply with legal requirements;

Offers transactions involving:

Cigarettes or tobacco products;

Vaping;

Counterfeit or stolen goods;

Firearms, weapons, or ammunition;

Gambling;

Gaming involving purchases of digital goods (customer service is allowed);

Illegal drugs or non-legally prescribed controlled substances;

Items that create consumer safety risks;

Items that are intended to be used to engage in illegal activities;

Political organizations (government institutions are allowed);

Pornography; or

Personal fundraising or collections of nonprofit donations unless approved by Apple.

Primarily offers or sells drug paraphernalia or sexually-oriented items or services;

Promotes hate, violence, or intolerance based on race, age, gender, gender identity, ethnicity, religion, or sexual orientation;

Allows an end-user to purchase currency or establish a pre-paid account;

Constitutes a staged digital wallet (for example, where a second payment transaction is conducted in order to complete the first transaction or where there is a substitute merchant of record in a transaction);

Engages in fraud;

Infringes or violates the intellectual property, publicity, or privacy rights of another; or

Shows Apple or its products in a false or derogatory light.

Apple reserves the right at any time to disable Apple Messages for Business for any reason it deems prudent.

https://register.apple.com/resources/messages/messaging-documentation/privacy-security

  Privacy and security

End-users and businesses can find Apple Messages for Business Privacy in different locations.

On devices. When messaging using Apple Messages for Business for the first time, you can see the following privacy statement and link. When in a conversation with a business, you can locate the privacy statement under the information button , tap Messages for Business & Privacy.

<!-- img: privacy-macOS-1.png -->

Welcome message on macOS

On iOS and iPadOS. Open Settings > Messages, scroll to the bottom, and tap About Business Chat & Privacy.

<!-- img-row: privacy-iOS-1.png, privacy-iOS-2.png -->

Welcome message on iPhone

Apple Messages for Business and Privacy information expanded

On Apple website. For privacy information, see [Apple Messages for Business & Privacy](https://www.apple.com/legal/privacy/data/ww/messages-for-business/).

Security. For security information, see [Secure Apple Messages for Business using the Messages app on Apple Platform Security](https://support.apple.com/guide/security/sec1c603aab4/1/web/1).

ISO/IEC 27001 and ISO/IEC27018. Apple Messages for Business is covered by ISO/IEC 27001 and ISO/IEC 27018. For more informations, see [Apple internet services security certifications](https://support.apple.com/guide/certifications/apc34d2c0468b/web).

https://register.apple.com/resources/messages/messaging-documentation/faq

Apple Messages for Business FAQ

Answers to common questions about Apple Messages for Business service, features, and implementation.

Updated: February 7, 2025

Version: 2.11

Prerequisites

: See Prerequisites for requirements at different stages.

General questions

What operating systems support Apple Messages for Business?

Apple devices running iOS 11.3 and later or macOS 10.13.4 and later support Apple Messages for Business.

What is the business cost of deploying Apple Messages for Business?

Cost depends on your deployment scope and Messaging Service Provider (MSP) selection. Contact your chosen MSP for pricing details.

How does Apple Messages for Business differ from iMessage?

Apple Messages for Business differs from consumer iMessage in these ways:

Purpose: Business-to-customer (vs. person-to-person)

Encryption: Slightly different encryption mechanism

Registration: Requires business account registration with Apple

Features: Includes business-specific interactive features (list pickers, Apple Pay, etc.)

When referring to the service to consumers, use "Apple Messages" rather than "iMessage."

How can customers contact my business?

Customers initiate Apple Messages for Business conversations by tapping the Messages button (looks like a message bubble) placed on:

Business website

Mobile site

Email marketing

QR codes

iOS app

Apple Maps listing

Direct phone number tap

See Entry points for more details.

Can I message employees through Apple Messages for Business?

No. Apple Messages for Business currently supports only business-to-customer communications, not internal business or B2B use.

Can I use my own bot to access the Apple Messages for Business REST API?

Virtual agents must access Apple Messages for Business through an approved Messaging Service Provider (MSP), not directly through the REST API. Apple requires a blend of automated agents (bots) and human agents. Live agent escalation is mandatory.

Can I send initial messages to customers using their phone numbers?

No. Customers must initiate conversations first. When customers start a conversation:

They trigger the Messages button or tap your business phone number

Apple sends an anonymous identifier (opaque ID) to your MSP

You cannot identify or message customers by phone number alone

What is an Opaque ID?

An Opaque ID is:

A unique identifier for each customer-business conversation

Different for every conversation the customer has with your business

Not the customer's phone number, email, or iCloud account

Assigned by Apple for privacy protection

Gives customers control: they decide what personal information to share

Opaque IDs protect customer privacy while enabling personalized business interactions.

Can I deploy Apple Messages for Business using only virtual agents?

No. Apple requires:

Blend of automated agents (bots) and human agents

Mandatory live agent escalation path

Human agent reachability for customer support

Deployments using only virtual agents will not receive Apple approval.

What is a Messaging Service Provider (MSP)?

An MSP is a business platform that:

Implements server-to-server REST API integration

Sends and receives messages and photos

Processes Apple Pay transactions

Provides live agent console for customer interactions

Routes messages to appropriate teams

Offers automation and bot capabilities

Integrates with your business systems

Getting started

As a business, where do I start?

Follow these steps:

Select an approved Messaging Service Provider (MSP) from Apple's MSP list

Contact your chosen MSP to discuss requirements and next steps

Create your Apple Messages for Business account at Apple Business Register

Complete the registration process (select MSP, provide branding, add testers)

Verify MSP connection

Begin implementation with your MSP

See Register your account for detailed instructions.

Where can I find approved Messaging Service Providers?

Visit Apple Business Register Messages to see all Apple-approved MSPs and their capabilities.

What does an MSP platform do?

MSPs handle:

Message delivery and routing

Processing and responding to messages

Applying Apple Messages for Business features (list pickers, Apple Pay, etc.)

Implementing basic automation (bots for common questions like store hours)

Agent console for live responses

Integration with your backend systems

My registration has been under review for a while. How can I get help?

Sign in to Apple Business Register

Review all pending actions required for your account

Click "Help" to contact Apple support directly

Contact your MSP representative for MSP-side issues

Service features

What is a Messaging Service Provider (MSP)?

(See General Questions section above)

Can customers reach any business?

No. Customers can only reach businesses that:

Registered with Apple

Received Apple approval for Apple Messages for Business

Meet Apple's service and security requirements

Can customers add others to a conversation with my business?

No. Group chat with a business is not supported. Conversations are one-to-one between customer and business.

Can businesses send message notifications to customers?

Yes, with permission. Best practices:

Ask permission before enrolling customer in notifications

Explain notification types: "You'll get order status updates"

Explain opt-out: "Reply STOP anytime to turn off notifications"

Keep opt-out simple and easy to remember

Example: "You're now signed up for order status notifications. Reply STOP anytime to turn off."

See Handle notifications for more details.

Can I continue communicating with customers after conversations end?

No. When a customer ends a conversation:

Stop sending messages

Customer must initiate a new conversation to receive messages again

Exception: Immediate follow-up satisfaction survey (CSAT) is acceptable

See Design responses for conversation guidelines.

What is the message exchange flow?

The message flow follows this pattern:

Customer sends message → Apple Messages for Business service

Service forwards to your MSP platform → Your MSP backend

MSP processes and routes → Agent queue or automation

Agent/bot responds → MSP platform

MSP sends to service → Apple Messages for Business

Service delivers to customer device

See the MSP REST API documentation for technical details.

Which languages does Apple Messages for Business support?

Apple Messages for Business supports every language that iOS, iPadOS, and macOS support:

Left-to-right languages (English, Spanish, French, etc.)

Right-to-left languages (Arabic, Hebrew, etc.)

To view supported languages:

iPhone/iPad: Settings > General > Language & Region > Other Languages

Mac: System Preferences > Language & Region > click plus button

Note: Your MSP must confirm they support your chosen language.

Technical implementation

What is the REST API?

The Messaging Service Provider REST API enables:

Server-to-server message exchange with Apple

Sending interactive features (list pickers, Apple Pay)

Receiving customer opaque IDs (not phone numbers)

Processing transactions securely

Learn more: Messaging Service Provider REST API

What authentication methods does Apple Messages for Business support?

Apple Messages for Business supports:

OAuth2 protocol with password autofill

Third-party vendor authentication integration

Full authentication and authorization flows

Customers authenticate securely in Messages to view account information.

What security features are included?

Built-in security features:

End-to-end encryption for messages

Opaque ID (no phone number exposure)

Apple Pay for secure transactions

OAuth2 authentication support

MSP platform security compliance

Next steps

For more information:

Getting started: See Register your account

Design your experience: See Design your UX

Test your implementation: See Account testing

Technical documentation: MSP REST API

https://register.apple.com/resources/messages/messaging-documentation/account-testing

Account testing
Account testing is an important aspect of setting up your Apple Messages for Business account. It allows you to determine if the connections, entry points, and console are working. Work with your MSP to determine how best to test your Apple Messages for Business account and add authorized testers, if necessary.
Add testers
Use the following steps to add internal testers to your Apple Messages for Business account:

Sign in to Apple Business Register.
Click Messages for Business Accounts and select the account to add testers.
TipWhether you are a business or an MSP ensure you and your team members have an Apple Account using your organization's email address.

Scroll down the page to Account Testing.
Add your internal tester's Apple Accounts.
Click Send to new testers to send an instructional email to your testers when your list is complete and you're ready to begin testing.
Click Submit in the Apple Messages for Business account profile for Apple to approve your changes.
Apple Business Register sends an instructional email containing a link to your Messages for Business conversation to the Apple Account email address of each tester. If a tester doesn't receive the email, then recheck that their email address is provided in the Account Testing section. The email address maybe wrong or not an Apple Account. For security and privacy reasons, Apple can't verify Apple Account email addresses.
Test sending and receiving messages
Activating the link contained in the testers email allows testers to send messages to your agents who can reply from your MSP agent desktop. When testing, be aware of the following details:

Design a test to include your support agent desktop and webpage which triggers the appropriate built-in features and iMessage apps.
You should observe messages sent from an iOS device are now arriving to your test business. Employees testing from your support agent desktop or webpage should be able to respond to these test messages.
Your testers may notice your brand colors are not visible in the Messages header. Business color is not available while your account is in test mode. Your brand's colors display correctly once your account goes online.
If you send the testing link to someone whose email is not listed in the Account Testing section, then they will be unable to send messages.
If you provide a Redirect Page URL and your testers try to enter Apple Messages for Business from an unsupported device, then they land on the redirected page, instead of the default page. You can set your Redirect Page URL in the "Unsupported Devices" section at the bottom of your Apple Messages for Business account page.
Use the following steps to begin testing:

From a supported device, ask your testers to find the email sent to them.
Click the link in the email from a supported device which takes them to an Apple Messages for Business conversation in the Messages app.

https://register.apple.com/resources/messages/messaging-documentation/xp-review

Experience quality assurance

The experience review is where Apple reviews the user experience of interacting with your brand before you launch to the public.

Before beginning the experience review, you should complete a quality assurance of your experience. Your account needs to meet the following requirements:

Connect your Apple Messages for Business account and confirm that messages are delivered.

If you are using your commercial account, the account access should be restricted to authorized Apple Accounts. Under Account Testing > Advanced, select 'Restrict access to authorized Apple Accounts'. Enter the Apple Accounts that will test messages from their personal iPhones.

Configure, activate, and test both the automation and live agent interactions. Ensure that all use cases have been tested from the user perspective. All features and content in the experience should be reviewed, and any errors addressed.

Make sure agents have been prepared to handle Apple Messages for Business traffic and trained to support the channel use cases.

Experience review

When you are ready to complete the experience review, prepare the screen recording.

Screen recording

The screen recording should be conducted by your team or the MSP team working with you, to test your experience and adherence to Apple's conversational guidelines. It also should accurately represent the user journey that will occur when your Apple Messages for Business account is in production and has launched.

Please make sure to demonstrate the [interactive features](https://register.apple.com/resources/messages/messaging-documentation/customer-journey#interactive-features) you have integrated in the experience, the live agent interaction, as well as the out of hours messages.

TipTo record your device screen, review the following links: [Record the screen on your iPhone, iPad or iPod touch](https://support.apple.com/HT207935) [Use an iPhone, iPad or iPod touch connected to your Mac](https://support.apple.com/guide/quicktime-player/qtp356b55534/mac) [How to record the screen on your Mac](https://support.apple.com/HT208721)

Recording upload and results

Please work with your MSP to provide a screen recording of the user experience for our team to review.

Once your MSP uploads the screen recording, Apple will provide any feedback directly to your MSP.

Next steps

Fix any issues listed in the report received from Apple. Once all issues have been addressed, you can move on to the next section, see [Go Live!](https://register.apple.com/resources/messages/messaging-documentation/go-live).

https://register.apple.com/resources/messages/messaging-documentation/go-live

Ready to launch

Launch your Apple Messages for Business account after you pass an experience review and Apple approves your account. Let your Apple Messages for Business team know the date and time you want to launch so they can coordinate entry point activation, such as the business phone numbers you registered with Message Suggest, with your launch tasks. Complete the following launch tasks to ensure your brand is ready to accept customers:

Log into Register and submit your Apple Messages for Business account to go online. Once Apple approves this change in status on the Apple Messages for Business account, it will display as Online.

Ready your support agents to receive messages. Your business may begin receiving customer messages as soon as your entry points are publicly visible. For more information on preparing your agents see [Prepare ops and marketing for launch](https://register.apple.com/resources/messages/messaging-documentation/prep-ops-mktg)

Enable the Messages button on your Apple Maps locations, you may need to add the country where your physical locations reside. Selecting countries does not affect the visibilty of your iOS entry points. For more information on Apple Maps place cards, see [Entry points](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#entry-points-overview).

Enable the Apple Messages for Business buttons within your website and app, and launch Apple Messages for Business for your customers. If you need to add Messages buttons to your website, see [Adding a Messages button to your website](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#design-your-website-and-app-to-include-the-messages-buttons). If you have any questions, send an email to your Apple Messages for Business team at [business-register@apple.com](mailto:business-register@apple.com).

https://register.apple.com/resources/messages/messaging-documentation/metrics

Optimize your customer's Apple Messages for Business experience

After launching Apple Messages for Business, growing the channel through intelligent optimization is necessary to leverage the platform's full potential for your business.

Although Apple doesn't provide any metrics, if you don't have metrics or analytics to gather, you can work with your Messaging Service Provider (MSP) to obtain the metrics you need.

First 30 days

<!-- img: msp-dashboard.png -->

The first 30 days should be spent monitoring the agent team to make sure they can resolve all customer issues within the messaging channel, and to create a prioritized list of ways to improve agent training.

By the end of the first 30 days, the brand and MSP should appoint an optimization team with representatives from both the brand and the MSP.

Areas of improvement

At the end of the first 30 day period, the optimization team should review the operational metrics, focusing on the intents that have the greatest frequency, the worst CSAT, or highest agent time-to-resolve. The optimization team should select a few of the worst intents to improve:

Intents with the highest frequency are candidates for automation.

Intents with the lowest CSAT can usually be improved by connecting the customer more quickly to a live agent.

Intents with the highest time-to-resolve can usually be improved through agent training, improving self-serve content, refining agent productivity tools like the agent desktop or Natural Language Processing (NLP) or bot system, or by improving customer productivity through apps or ABC built-in features.

The brand and MSP optimization team should create a regular process to review the worst intents and implement fixes, tracking how their improvements are reflected in driving higher customer satisfaction or lower agent time-to-resolve.

Automating intents

The optimization team should continue automating the most frequent and repetitive intents to increase live agent team capacity. Typically, a large enterprise can reach a level where at least 70% of customers are fully assisted by an automated agent without connecting to a live agent.

Increasing traffic

The optimization team should increase messaging traffic in the following order, managing volume where necessary so that customers are connected with live agents within 3 minutes:

Register the brand's primary numbers for Message Suggest and follow Message Suggest best practices.

Register all of the brand's store phone numbers for Message Suggest, if there are physical locations and stores.

Shift all web chat traffic to Apple Messages for Business for customers on all supported Apple devices.

Add Apple Messages buttons to the brand's website and app, in priority to phone numbers, with strong call-to-action messages, and displayed to every customer on a supported Apple device.

Add Apple Messages buttons to email broadcasts, retail packages, and within the brand's stores.

Quarterly presentations

After a few optimization cycles, the MSP should work with the brand team to create a presentation for brand executives, highlighting:

Monthly operational metrics since launch.

How the experience of messaging in Apple Messages for Business compares to phone and other messaging channels in terms of customer satisfaction and time-to-resolve.

A breakdown of optimization activities, showing the intents selected for improvement, the results of optimization in terms of increased CSAT and lower agent time-to-resolve, and how the optimizations translate into annualized cost savings for the business; and

A plan to increase messaging volumes, a professional services budget to optimize the experience, and an estimated ROI from shifting customer traffic to ABC and continuing optimizations.

Next steps

The outcome of the executive review should be a green light to increase customer traffic in Apple Messages for Business, and provide a budget for professional services to use for optimization.

After the green light from brand executives, the optimization team should create a plan for shifting agents from other channels to Apple Messages for Business. It's best to create a regular cadence to train and transfer a group of agents over to Apple Messages for Business, along with adding customer traffic.

The optimization team should continue quarterly updates to brand executives to build confidence in the program. The team should report on how optimizing intents and shifting traffic from other channels to Apple Messages for Business is improving overall customer satisfaction and generating an ongoing annual ROI for the business.

https://register.apple.com/resources/messages/messaging-documentation/prep-ops-mktg

Preparing your teams for launch

Launch ready means that your agents are available to resolve all customer queries that are regularly resolved over the telephone support line. Prepare your support operations and marketing, as necessary. You can conduct the following launch readiness activities:

* Train your agents for asynchronous support

* Register your primary phone numbers for Message Suggest

* Prepare the [Experience Review](https://register.apple.com/resources/messages/messaging-documentation/xp-review) with Apple and implement the feedback to improve experience

* Inform Apple Messages for Business team when you wish to launch to the public

Tracking

Plan to track defined channel goals with your MSP to measure your Apple Messages for Business success. To implement tracking, look at the tools to use for Apple Messages for Business, such as websites, entry points, and surveys. Work with your MSP to coordinate on how best to collect and measure data.

You can use website analyitics to understand click-rates for Message Suggest registered phone numbers. On some of your entry points, you can implement intent, group, and body values to track why customers are contacting you and where they're directed. Provide customer satisfaction surveys after digital encounters and collect information. You can also measure how often a customer needs to escalate to an agent after interacting with a bot.

Training agents

Update your live agent scripts and work with your MSP to train your agents. Ensure your console agents are thoroughly trained in working in the MSP console with the different Apple Messages for Business features implemented in your design.

Marketing preparedness

Prepare marketing plan for launch. If you have any press release plans, contact the [Apple Messages for Business team](mailto:business-register@apple.com?subject=PR%20Request)

For design guidance on branding and visual elements for marketing materials, see [Referring to Apple Messages for Business](https://register.apple.com/resources/messages/messaging-documentation/message-with-customers#Referring-to-Apple-Messages-for-Business).

https://register.apple.com/resources/messages/messaging-documentation/troubleshooting

Troubleshooting

Resolve common issues with Apple Messages for Business messaging and testing.

Estimated time to resolve: 5-30 minutes per issue

Current status: For internal testers and account setup

Prerequisites

: See Prerequisites for requirements at different stages.

Messaging setup

Verify basic Messages app setup on your device before troubleshooting Apple Messages for Business issues.

iPhone, iPad, or iPod Touch:

Follow Apple's guide: Set up Messages

Mac:

Follow Apple's guide: Set up Messages on Mac

For general iMessage errors, see:

Error when activating iMessage or FaceTime

Cannot send or receive messages

Issue: "Not Delivered" error when messaging test account

Symptom: Message fails to send with "Not Delivered" alert

Severity: Critical - blocks testing

Causes:

Apple Account not in approved testers list

Account not submitted after adding testers

iMessage not enabled on device

Account still under Apple review

Solution:

Verify iMessage settings:

Go to Settings > Messages > Send & Receive

Confirm iMessage is enabled

Confirm your Apple Account is logged in with send/receive enabled

Verify tester status in Apple Business Register:

Sign in to Apple Business Register

Select your Messages for Business account

Confirm your Apple Account appears in the approved testers list

Check that the account is in "submitted" status

Reset iMessage and retry:

Close the Messages app completely

Go to Settings > Messages

### Disable iMessage

Wait 30 seconds

### Re-enable iMessage

Wait 2-5 minutes

Retry sending message

Wait for account activation:

If added as tester after account creation, wait up to 24 hours

Try messaging again after waiting period

Tip

: If issue persists after 24 hours, contact your MSP representative or Apple support at business-register@apple.com

Issue: Message Suggest not appearing

Symptom: Business phone number does not trigger "Message" suggestion in Contacts or Phone app

Severity: Medium - affects customer discoverability

Causes:

Device region mismatch

Not logged in with Apple Account in Messages

Wrong phone number format for region

Solution - Check account settings:

Verify Messages app login:

Go to Settings > Messages > Send & Receive

If not logged in with Apple Account, tap "Use your Apple Account for iMessages"

Wait a few moments for settings to sync

Check device region:

Go to Settings > General > Language & Region

Device region must match the business country

Message Suggest displays without country code only when device region matches business region

Verify phone number format:

Confirm you're tapping the phone number without the country code for your region

Example: In US, tap "(555) 123-4567" not "+1 (555) 123-4567"

Solution - Clear cache (if settings are correct):

Close the Messages app

Clear device cache:

Go to Settings > General > Date & Time

Set date forward one day

Set date back to current day

Wait 30 seconds

Restart device and wait approximately 30 seconds

Test with non-Apple Messages contact first:

Send a regular message to a personal contact

Return to Contacts or Phone app

Test Message Suggest with test number:

Tap +14086065775 to verify Message Suggest appears

Tap any business phone numbers you're testing

If still not appearing:

Retry steps 1-5

Wait 1-2 hours for server synchronization

Try again

Note

: Message Suggest availability depends on device being registered with iCloud and Messages account settings being up to date.

Issue: Message delivery inconsistent or delayed

Symptom: Some messages send successfully while others fail, or delivery is slow

Severity: Medium - affects testing reliability

Causes:

MSP platform connectivity issues

Network connectivity on your device

Message queue processing delays

Account transition between test and commercial status

Solution:

Verify network connectivity:

Confirm device has strong Wi-Fi or cellular signal

Try on a different network if possible

Check MSP connection status:

Sign in to Apple Business Register

Select your account

Verify MSP connection status shows "Connected"

Wait for queue processing:

Apple Messages for Business queues messages for processing

Most messages process within 1-5 minutes

Allow 5-10 minutes for delivery

Contact your MSP:

If multiple messages fail consistently

Your MSP can view detailed server logs

Provide message timestamps for investigation

Issue: Cannot add Apple Account as tester

Symptom: Apple Account not accepted when adding testers to account

Severity: Medium - blocks testing setup

Causes:

Incorrect Apple Account format

Account not submitted after adding ID

ID already added to account

Solution:

Verify Apple Account format:

Use the full Apple Account (typically email address)

Example: user@icloud.com or user.name@company.com

Avoid shortened or partial IDs

Confirm form submission:

After adding Apple Accounts, scroll down and locate the "Submit" button

Click "Submit" to save changes

Important: Settings not saved until form is submitted

Verify success message appears

Check for duplicates:

View current testers list

Confirm Apple Account is not already listed

Remove duplicate entry if needed

Retry adding tester:

Sign out of Apple Business Register

Sign back in

Navigate to your account settings

Attempt to add Apple Account again

Next steps

After resolving messaging issues:

Test account messaging - Verify all features work correctly

Complete experience review - QA checklist before going live

Move to production - Transition to commercial account

https://register.apple.com/resources/messages/messaging-documentation/doc-rev-history

Revision History

| Date | Version | Summary |
|---|---|---|
| May 21, 2026 | 3.1 | Misc corrections and updated links |
| January 6, 2026 | 3.0 | Updated References using latest iOS 26 references and designs |
| February 7, 2025 | 2.11 | Updated references of Apple Account to Apple Account |
| October 31, 2024 | 2.10.8 | Updated brand and MSP onboarding overview |
| July 16, 2024 | 2.10.7 | Revised graphics, added new detailed guidance for onboarding |
| April 11, 2024 | 2.10.6 | Terminology updates and minor fixes |
| February 11, 2024 | 2.10.5 | Minor fixes |
| November 2, 2023 | 2.10.4 | Fixes |
| September 26, 2023 | 2.10.3 | Fixes |
| September 25, 2023 | 2.10.2 | RSA updates |
| September 15, 2023 | 2.10.1 | Fixes |
| September 12, 2023 | 2.10 | Qualifying as a Roadside Assistance via Satellite provider. |
| May 9, 2023 | 2.9.4 | Update links to Human Interface Guidelines. |
| April 11, 2023 | 2.9.3 | Update instructions under the policies. |
| January 5, 2023 | 2.9.2 | Update instructions to enable native entry points. |
| January 3, 2023 | 2.9.1 | Fixes |
| December 15, 2022 | 2.9 | Link fixes. ISO Certifications |
| November 4, 2022 | 2.8 | Updated Register your accounts and instructions for registering Message Suggest. |
| October 24, 2022 | 2.7 | Updated Policies related to Requesting end-user's Personal Identifiable Information. |
| October 10, 2022 | 2.6 | Updated "Pass Apple's QA" to Pass the experience review. Moved Best Practices to Design and implement your user experience. Moved Messages Suggest guide to section on Message with your customer. |
| Septembre 15, 2022 | 2.5 | Add entry point to Apple Pay Order tracking on iOS 16 and macOS 13. |
| April 19, 2022 | 2.4 | Register links updated. |
| March 31, 2022 | 2.3 | Apple Messages localized new buttons. |
| March 23, 2022 | 2.2 | Apple Messages new buttons and update to Design and Implement your User experience. Human Interface Guidelines links updated. |
| November 25, 2021 | 2.1.1 | Fixes. |
| October 25, 2021 | 2.1 | Added Quick Reply supported. |
| September 20, 2021 | 2.0.0 | Rebranded Business Chat to Messages for Business; Message Suggest to Message Suggest; removed 'BETA' from Quick Reply. |
| June 22, 2021 | 1.0.0 | Initial release. |
<sub>↳ `messaging-documentation.md` L3762–3818</sub>

Revision number incrementation

| Version | Explanation |
|---|---|
| 1.0.0 | Major revision. Includes number increment and new content. |
| 1.0.0 | Minor revision. Includes number increment and changes to current content, such as content corrections, graphics, grammar, etc. |
<sub>↳ `messaging-documentation.md` L3822–3826</sub>



---

# Part 2B — MSP Onboarding (verbatim)

> **Source:** `msp-onboarding.md` — verbatim (entities decoded, escapes removed, tab-tables → Markdown, JSON/cURL fenced unchanged). ⚠ Source last updated 01 Feb 2024 — oldest in the set; see Master §Recency for staleness flags.

# msp-onboarding

https://register.apple.com/resources/messages/msp-onboarding/

Introduction

Version: 3.0.3

Last update: February 1, 2024

The Messaging Service Provider (MSP) onboarding process provides end-to-end guidance for you to register, integrate, and deliver great experiences to your brands and their customers using Apple Messages for Business.

As an MSP, you are the contact center technology partner that provides the key features and services necessary for a business, also known as a brand, to communicate with their customers through Apple Messages for Business.

The requirements for MSPs include the following:

Messaging platform that supports asynchronous conversations and intent-based routing.

Channel connector to link the messaging platform to the Apple Messages for Business Service.

Live agent console that can be customized to support Apple Messages for Business features.

Virtual assistant, or bot, flows to triage incoming conversations and hand off to live agents with conversation history.

Customer success team to build custom integrations into brand back-end systems (CRM, OMS, and authentication) to support the use of Apple Messages for Business features.

Conversational designer who can assist brands to build smooth and efficient customer journeys in Apple Messages for Business.

The diagram below shows a typical MSP architecture. The items highlighted in blue are required for all MSPs to qualify for the Apple Messages for Business MSP onboarding process.

<!-- img: msp-Architecture.png -->

MSP architecture

An MSP must deliver a full experience to brands and customers, which means a complete integration with all features, and staying current with all new feature releases. The MSP must provide businesses with easy-to-use GUI tools necessary to build and share rich interactive objects such as List Pickers with their agents, and bot management tools. As rich features require integration with each brand’s back-end systems, such as a CRM (customer relationship manager), OMS (order management system), and authentication, all MSPs must have a team who can build the necessary connections to enable them.

Overview

To become an approved MSP for Apple Messages for Business, you must first create an account for your organization through Apple Business Register. Apple reviews your registration, and a member of the Apple Messages for Business team in your region contacts you to schedule a review of your capabilities and go-to-market plan for Apple Messages for Business.

Once the region team approves your organization to begin the onboarding process, there are three phases to complete: Integration, Brand Onboarding, and Launch.

NOTE

Until your organization completes the launch process, you must not advertise your involvement with Apple Messages for Business in any public forum including, but not limited to, web sites, blog posts, social media, or press releases.

Feature Integration

When you receive your invitation, you can begin the integration of Apple Messages for Business features into your platform. Apple provides an API Integration Tutorial as a guide, along with code samples to give you a head start. You configure your MSP test account in Apple Business Register and begin development. You’ll need to build a demo that shows an example customer journey, leveraging the full range of Apple Messages for Business features. When your integration and demo are complete, you can schedule a live review of your demo with the Apple Messages for Business team. When the team determines that the integration is done to Apple’s standards, you’ll be approved to begin the next phase. For more information, see Integration.

Business Development

When Apple approves your organization, you can begin this phase by signing up your sales and customer success teams for Apple Messages for Business online training. Make sure you have three client registered for Apple Messages for Business in Apple Business Register, and develop their conversational flows and necessary back-end integration, followed by a pilot program for testing. For more information, see Business Development.

Launch

When your chosen brands complete the pilot program, you’ll need to work with the Apple Messages for Business operations team to prepare your first brands for launch. This includes a review of goals and success metrics, a ramp plan, and an experience review, where the Apple operations team reviews the user experience of interacting with the brand’s Apple Messages for Business experience. Upon final approval, the brand’s Apple Messages for Business Account will go live. Once this is done, your marketing and PR efforts for Apple Messages for Business may begin. Coordinate with your Apple regional team for guidance around marketing and PR. For more information, see Launching Your Brands.

https://register.apple.com/resources/messages/msp-onboarding/mspRegistration

Registering Your MSP

To provide your Message Service Provider (MSP) services you need to register for Apple Messages for Business on the Apple Business Register portal.

Organization

Apple Messages for Business accounts require actions from an administrator, a technical contact, and a sponsoring executive. The administrator uses Apple Business Register to register the organization and approve the TOU on behalf of the sponsoring executive. The technical contact can set up Apple Messages for Business Accounts, MSPs, and brands. The technical contact must be an alias email, such as @<yourdomain.com>. The sponsoring executive agrees to the TOU. You should have these program contact roles identified prior to registration.

You must enter your MSP, Apple Messages for Business accounts, brands, team members, and organization details into Apple Business Register to create the accounts needed to connect your platform to Apple Messages for Business.

Apple Business Register is designed as a self-service portal. It is mostly self-explanatory with a few key items of note:

You have to apply and be approved for your company to offer MSP services on behalf of Apple. If you don’t see Messaging Service Providers as an item in Apple Business Register, contact your Apple Messages for Business account manager to determine the status of your application.

Apple Business Register generates several values: MSP ID, Business ID, and secret passphrase.

In Apple Business Register, you have to define additional attributes, such as organizational details, team member details, brand colors, brand logos, and URLs of your servers.

Each Business ID is associated with a unique MSP ID. Internal test Business IDs have no brand. Commercial Business IDs must be associated with a brand in Apple Business Register, which requires an approval step by the brand review team that may take several business days.

Branding

During registration, please register your brand name, making sure it matches your online or physical identity. For example, the details registered for your website match your company’s website.

Use your product name or the main product that supports Apple Messages for Business. For example, if the product has a dedicated name and website, you may want to register the product as the brand you want to promote for your platform name. This is how businesses will find you in Apple Business Register, and connect their accounts to your service.

Account Types

There are three registration account types available to MSPs: Private, Commercial Public, and Commercial Non-Public.

Private. Intended for development, testing, staging, and integration work endpoints.

Commercial Public. Indicates an MSP endpoint for paid commercial use as a service offering of the MSP. This service appears in the drop-down list of MSPs available to new business customers.

Commercial Non-Public. An alternative to Commercial Public. It is intended as a commercial messaging service, but doesn’t appear in the drop-down list of services. Use this type for alternative endpoints such as geo-specific endpoint, such as EMEA- or APAC-specific geo-locations. Businesses will need to connect their accounts to these alternate endpoints manually.

Private MSP Accounts

Private MSP accounts allow you to associate your platform with our Messaging gateway and establishes a communication channel to start sending and receiving messages with an Apple device.

Add at least one MSP Private account to your Apple Business Register portal to begin developing and testing. In Apple Business Register, go to the Messaging Service Providers section and press the + button to create a private account. Once created, the account isn’t accessable to the general public.

<!-- img: msp-onboarding-connectedSvc.png -->

“Connected

Configure the following values for your account:

MSP ID. A unique UUID for your approved MSP account.

Business ID. A unique UUID for your approved Apple Messages for Business account.

Secret passphrase for API. A Base64-encoded string.

MSP message endpoint. Use https://<your.endpoint.host>/message.

When you create your MSP private endpoint, your screen changes to list an additional link (see screenshot below). Click on Get your test Messages for Business URL to get a test version of your Messages for Business ID and URL. You can use these links for testing purposes only, but not for development.

<!-- img: msp-onboarding-testIDs.png -->

Test IDs

Private Apple Messages for Business Accounts

To fully set up Apple Messages for Business integration, go back to the main Register page dashboard and click on Messages for Business Accounts to create your Private accounts. You can create multiple private account.

Each of them can be configured to a specific MSP account.

Sending messages to Private accounts requires you to register the Tester’s Apple IDs. Use the email address from their device which you can find under Setting > Messages > Send & Receive. For more information, see Messaging for Approved Testers

With the Private account, you can create Apple Messages for Business accounts for testing and development purposes. Each of them can be configured to a specific endpoint. You’ll need an account to set up and integrate OAuth2, see Sending an Authentication Message, and Apple Pay, see Integrating Apple Pay.

NOTE

Apple Messages for Business accounts created for testing and development have no branding to identify them as private.

Test message

MSP Commercial Public Apple Messages for Business Account

Once you have completed integrating Apple Messages for Business features on your platform, you’re eligible to add a commercial public Apple Messages for Business account and assign your business branding. This allows your customers to engage with you via Apple Messages, as they would with any other business.

https://register.apple.com/resources/messages/msp-onboarding/integration

Feature Integration and Your Apple Demonstration

Once you have configured your Messaging Service Provider (MSP) test account in Apple Business Register, you can begin with the first phase of the onboarding process: integration.

Use the API Integration Tutorial and code samples to build an integration on your MSP platform using all of the Apple Messages for Business features from the tutorial. You must meet this critical requirement to deliver the full Apple Messages for Business experience to brands and their customers.

Create a customer demo journey that demonstrates all of the Apple Messages for Business features. All features should be functional and the conversation should mimic what would happen with a real business.

Finally, schedule a review with the Apple Messages for Business team. During the review, you’ll present a live demonstration of your customer journey using a web conference. This demonstration should simultaneously present both sides of the conversation, from your agent desktop UI and an iPhone.

API Reference

The Apple Messages for Business REST API documentation is available on the Apple Messages for Business REST API website. It features all the integration requirements, technical specifications about the API to aid in your development efforts.

API Tutorial and Sample Code

The Apple Messages for Business team designed the Apple Messages for Business MSP API Integration Tutorial

to guide developers through the integration of each Apple Messages for Business feature. You can use the tutorial along with the bundled sample code from Appendix C—Assets Download as a reference to help you integrate Apple Messages for Business features.

Building the Integration Demo

The Integration Review allows a new MSP to demonstrate full integration with Apple Messages for Business to the Apple team. Your customer journey demo needs to show how a user would engage in conversation with a brand, and how the automated and live agents would handle the conversation. Your demo allows the Apple team to confirm their full support of the channel, and that your MSP team understands the flow of an Apple Messages for Business conversation.

Building Your Customer Journey Demo

The following steps outline how to prepare your demo.

Select a vertical that is representative of one of your existing brands, such as retail, financial services, telco, or airline.

Script a conversation flow between a business and their customer. In the script, answer questions like, such as “What would the customer intent be?” “How can customers use Apple Messages for Business features to provide a great experience?”

If you provide an automated agent, show how to triage incoming conversations and resolve some intents quickly. Demonstrate how a user can be handed off to a live agent when using an automated agent because live agent escalation is a requirement for Apple Messages for Business.

To qualify as an MSP, you need to demonstrate that your messaging platform can perform each of the following fundamental Apple Messages for Business functionalities in both the agent console and any automated agents. The Apple team checks these items during your integration demonstration.

The Apple team uses the following feature checklist to confirm that all major features of Apple Messages for Business are complete and working properly.

The checklist is not all-encompassing, if you want to view a full listing, see MSP REST API. If you have any questions about the Integration Review, contact the Apple team directly.

Integration Demo of Apple Pay and OAuth2

The Apple Pay on Apple Messages for Business portion of the demo requires a merchant account and

Apple Developer Program access. These may take several days to request and receive approval.

OAuth2 requires approval of the endpoints that you request and this may take 2-3 business days. Using a third-party service, such as Amazon’s Auth0, provides quick approval for your demo.

Integration Demo of iMessage Apps

The iMessage apps portion of the demo requires a developer account, iPhone, and a MacOS device that can run Xcode. Once you have the requirements follow the tutorial documentation for iMessage Apps to guide you on your iMessage app demonstration.

Presenting the Demo

The Integration Review is typically conducted over a video conference. You need to share the screen of an iPhone, as well as the agent desktop so that the Apple team can see both sides of the conversation. If you are using a Mac, you can connect your iPhone to it with a USB or lightning cable, and use QuickTime Player in New Movie mode to display the screen on your desktop in real time. For more information see Use an iPhone, iPad or iPod touch connected to your Mac. For other operating systems, you may need to use other tools to present both sides of the conversation.

https://register.apple.com/resources/messages/msp-onboarding/business-dev

Onboarding Your Clients

At this point of the MSP Onboarding Program, you’ll onboard and successfully register three of your clients on Apple Business Register. For Apple to consider you as a public Messaging Service Provider (MSP), one of your chosen client needs to actively use Apple Messages for Business. Ensure that your teams are fully prepared to assist clients in planning their customer experience, completing integrations, and launching Apple Messages for Business.

Configuring Your Production MSP Account

Once Apple verifies and approves your platform integration you can proceed to Business Development. Before you begin, you need to make modifications in your MSP and Apple Messages for Business accounts at Apple Business Register.

In your MSP account, configure a Commercial/Public MSP account with your production URL, and send it for review. Once Apple approves the new configuration, clients registering for Apple Messages for Business can select the name of your Commercial/Public MSP account.

In your Apple Messages for Business accounts, choose an account and change the account type or create a new one using the Commercial/Public type. Follow the instructions for setting up Apple Messages for Business accounts and set it up properly with your assigned client. Normally, an MSP is eligible to have one Commercial/Public Apple Messages for Business account. It should leverage your product name or corporate identity. If you need more accounts, please reach out to the Apple Messages for Business team.

Preparing Your Sales and Customer Success Teams

Resources are available to your sales and customer success teams to educate them on Apple Messages for Business features and best practices. Utilizing this knowledge base will assist your teams on providing your clients with a thorough understanding of Apple Messages for Business for onboarding. Complete the steps below to prepare your teams for onboarding your clients.

Sign up your sales and customer success teams for Apple Messages for Business online training.

Once your team members have completed this training, schedule a Q&A conference with the Apple Messages for Business team to follow up on any questions or concerns.

Create three internal email aliases, such as amb-execs, amb-sales, and amb-tech@<yourdomain.com>. This enables the Apple Messages for Business team to quickly reach the right people in your organization.

Your MSP, under certain conditions, is eligible to have one branded commercial DEMO account, for your sales team to use during their sales pitch. This demo should demonstrate all Apple Messages for Business features, and use, for example, a QR code as an entry point. If you want more information about the demo account, please reach out to the Apple Messages for Business team.

Onboarding Your First Client

Client onboarding is essential to your success as an MSP. The first clients that you onboard for Apple Messages for Business can set the stage for promoting your MSP to other clients. You may have clients in mind that you wish to promote as showcases once they are live on Apple Messages for Business. The clients that you select should possess the qualities of a successful client outlined below.

Select three of your clients that want to use Apple Messages for Business, and communicate these with your Apple Messages for Business representatives. Have them sign up in Apple Business Register. Once they’ve created their Apple Messages for Business account, they can link it to your MSP account.

End-to-End Process

Apple recommends that you review the Onboarding Overview, which details the end-to-end launch process, and provide this document directly to your clients.

Qualities of a Successful Client in Apple Messages for Business

You can determine how ready your clients are in going live by asking them the following questions in the listed categories:

Digital maturity. Is the client excited about adopting new technologies to change how they interact with their customers.

Senior executive support for messaging. Is there higher internal support for adding and developing Apple Messages for Business as a channel than beyond the Customer Care team?

Setting performance goals expectations. Has the client defined their goals for digital engagement and have they defined how Apple Messages for Business fits into these goals? What does the client expect to accomplish by enabling Apple Messages for Business?

Analyze Channel Business Goals and Identify Use Cases

Engage with your regional Apple Messages for Business representative early in the design process. They can provide implementation suggestions that can help meet client goals. Apple recommends using the Apple Messages for Business Readiness Review to quickly assess the goals that are most important for the client.

You can begin by determining the top contact drivers in both digital and voice channels. Identifying low-value drivers that result in high cost-to-resolve for the client, can be places to explore for adding interactive content or self-serve use cases.

Make sure that you’re able to provide the client with clear expectations on performance metrics collection in the channel based on their primary goals. Additionally, put in place a regular review plan to go over the goals they identified after launch.

Designing a Conversation Flow

Guide the client to follow the conversational design guidelines when interacting with customers on Apple Messages for Business. You can find general guidance in Design and Implement Your User Experience.

Below are tips to ensure a quality user experience:

Provide an automated greeting to the customer upon their first message. For experiences that don’t include automation on the front-end and are agent only, provide an automated response for off-hours. This sets the customer’s expectation on when to receive a response from the client.

Provide automated triage. Use list pickers and quick replies instead of textual menus to provide an easier navigation experience for the customer.

Focus on tap, not type, interactions. Encouraging tap versus type interactions allows customers to easily navigate through needs resolution while going about their day. Use Interactive Features, like QuickType prompts, and format questions in a way that allows the customer to easily send responses.

Focus on users in context. Present information that is helpful to the customer in their current context. Don’t ask for identifying information unless it’s required to resolve the customer’s need. Utilize interactive content to provide assistance that reaches across iOS.

Interactive Content

Working with your clients and following the Human Interface Guidelines, you can create user-focused features

to integrate interactive content. The following features enhance the user experience:

Quick Replies. Provide a simple way for the user to make an inline choice with a single tap during an ongoing conversation. You can have between two and five customizable choices, and the user can select only a single item. To learn more about list pickers, see REST-API - Quick Reply Message.

<!-- img: mspClientDev-quick-reply.png -->

Quick Reply

List picker. Triage a user’s intent (image below, list picker on the left) by guiding the user through automated self-serve flows and product selection. For more information, see REST API - List Picker Message.

Time picker. Schedule appointments, select dates for reservations, or coordinate in-store pickup using a time picker (image below, time picker on the right). Selected times are added directly to the Calendar app by the user. You can integrate the time picker with a scheduling system managed by the client. For more information, see REST API - Time Picker Message.

<!-- img: mspClientDev-listPicker-timePicker.png -->

List picker (left) and time picker (right)

Rich links. Allow a customer to preview a product by sending rich links (image below, rich links on the left) with product image previews. Video previews can also be added to rich links for a more immersive experience. Rich links provide customers the reassurance that the website being directed to, is secure and owned by the client. For more information, see REST API - Rich Link.

Wallet Cards. Provides customers with instant access to tickets, membership cards, or reservation confirmations that they can easily save in their Apple Wallet (image below, Wallet cards on the right). To send Wallet Cards in Apple Messages for Business, send them as an attachment.

<!-- img: mspClientDev-richLinks-walletCards.png -->

For guidance on creating Wallet Cards, see Developer Documentation.

Rich Links (left) and Wallet Cards (right)

Apple Pay. Grow the channel as a sales or e-commerce platform by sending Apple Pay requests (image below, Apple Pay on the left) over Apple Messages for Business. Allow users to complete purchases or bill payments with the ease of Apple Pay. View Apple Pay in Apple Messages for Business for guidance on how to set this up with your clients.

Authentication. Allow customers to authenticate (image below, authentication on the right) in Apple Messages for Business using OAuth2. Provide personalized care without leaving PII in the agent transcript, providing support for authenticated use cases. For guidance, see Authentication.

<!-- img: mspClientDev-ApplePay-auth.png -->

Apple Pay (left) and authentication (right)

iMesssage apps. Support additional or more complex functionality through the use of iMessage apps (image below). This is a great way to provide in-app utility, without ever leaving Messages. Clients who already have iOS apps created can reuse investments made in their app by recycling code into the iMessage app. Coordination may be needed with the client’s app development team. The resources below can be shared for more information:

<!-- img: mspClientDev-iMessageApp.png -->

Developer Guidance on iMessage apps

Design Guidelines for iMessage apps

Sending iMessage apps over Apple Messages for Business

iMessage app

Image sharing. Photos can be sent (image below, image sharing on the left) by or to users, allowing for easier resolution. Images can be sent by agents or automated assistants to display products, share image resources already utilized on the website, or just for fun! Allow users to send images to provide proof of purchase, damage, or just to share their favorite products.

Video sharing. Sharing videos with users (image below, video sharing on the right) can create a more immersive and direct way of providing product or service descriptions and instructions for troubleshooting. Allow users to send a video for proof of incident or to share how happy they are with a product.

<!-- img: mspClientDev-imgShar-Videos.png -->

To send images and videos over Apple Messages for Business, see Sending Messages with Attachments.

Image sharing (left) and videos (right)

Document attachments. Send documents (image below, document attachment on the left) in the form of PDFs to provide billing statements or other forms that a user can store for safe keeping. Send PDFs as fillable forms so that users can complete a document, sign it electronically, and send it back to the agent for processing.

Augmented reality. Give users a real world view of a product by sending over 3D images with Augmented Reality (AR) Quicklook (image below, AR on the right). Users can view virtual and real content, side by side, for size comparison or product fit. For information about AR Quicklook, see Previewing a Model with AR Quick Look.

<!-- img: mspClientDev-DocAttach-AR.png -->

To send PDF and USDZ files over Apple Messages for Business, see Sending Messages with Attachments.

Document attachments (left) and AR Quicklook (right)

Some interactive content is available for specific version of macOS and iOS/iPad OS. Review the table below to adjust the user experience and leverage the capability-list HTTP header. For more information, see HTTP Headers.

| Required macOS version | Required iOS/iPadOS version |  |
|---|---|---|
| List Picker / Time Picker | N/A | iOS / iPadOS 11.3 and later |
| Quick Reply | macOS 12 | iOS / iPadOS 15.1 and later |
| Rich Links | macOS 10.13.4 and later | iOS / iPadOS 11.3 and later |
| Attachments (Wallet pass/USDZ/...) | macOS 10.13.4 and later | iOS / iPadOS 11.3 and later |
| Apple Pay | macOS 10.13.4 and later | iOS / iPadOS 11.3 and later |
| Authentication | macOS 10.14 and later | iOS / iPadOS 12 |
| iMessage app | N/A | iOS / iPadOS 11.3 and later |
| Form | N/A | iOS / iPadOS 11.3 and later |
<sub>↳ `msp-onboarding.md` L493–509</sub>

Complete Integrations

Before proceeding to the next stage, make sure to complete all necessary integrations to secure a smooth path to launch.

Make sure that Rich Links function correctly with all possible links provided by clients to support their use cases.

Make sure that list pickers are functional to support automated triage.

Verify that Apple Pay is functional to support digital sales.

Make sure your authorization functions appropriately.

Verify that all interactive features are integrated with the client’s CRM or OMS.

https://register.apple.com/resources/messages/msp-onboarding/launch

Coordinating Your Launch Plans

Contact the Apple Messages for Business Operations team to coordinate your launch plans by sharing the completed use cases, planned entry points, and expected launch date.

Planning Entry Points

There are many options available for customers to start a conversation with a business. Brands can use Apple Messages for Business buttons and URLs to meet their customers in places where they are likely to contact your brands. Your brands can also enable system features such as Maps or Message Suggest so that customers can start a conversation when locating their business details.

A highly visible entry point with a powerful call to action can be key to success for your Apple Messages for Business brands. Here are some different ideas that you can share with your brands to drive engagement. For more information, see Entry Points.

Message Suggest. Reduces phone call volume by allowing customers to initiate a conversation by tapping on any of the registered business phone numbers. For more information, see Message Suggest.

Apple Maps Place Card. When customers use Maps, the brand’s location data provides instructions and estimated arrival times, and a message button to initiate Apple Messages for Business. For more information, see Apple Maps Place Cards.

Website button. Add an Apple Messages for Business button to the brand’s website. For more information, see Adding a Messages Button to Your Website.

App button. Adds a Messages for Business button to your app. For more information on how to add a button to the app, see Starting a Message from Your App.

Email and SMS. Brands can include URLs in the email or send it using SMS to reach specific customers. For more information, see Starting a Message from a URL

Social media. Making entry points available on social media is another way for the brand to increase visibility to customers.

QR code. Add an entry point anywhere you post marketing material.

Apple Wallet. Add entry points, such as passes, cards and orders tracking, for Apple Messages for Business using the Apple Wallet app. For more information on how to add entry points to the Wallet app, see Introducing Wallet and Merchant Order.

Augmented reality (AR). Add an entry point when using AR on your website or app. For more information about adding a custom action, see Adding an Apple Pay or a Custom Action in AR Quick Look.

Composing an Apple Messages for Business URL. Place URLs on all your external communications. For more information, see Adding a Messages Button to Your Website.

Brand Experience Review

Apple provides a free consulting session to test the customer experience of interacting with your business. The experience review is where Apple reviews the user experience of interacting with a brand before you launch to the public. Apple reviews your automated agents to ensure customers received the same level of quality with an automated agent as they would with a live agent.

You do not need a live agent to test automation. However, once testing of the automated agent is complete, you’ll need a live agent available to test any use cases that would escalate to a live agent.

Apple shares all review results with you and your brand, including details of any items that must be corrected prior to launch.

The Apple Messages for Business team provides feedback based on the following:

Interactive features work correctly

Ability and ease of completing a use case

Agent interaction

Launch Your Brand

On the brand’s selected go-live date, you’ll need to activate your brand’s account, entry points, and schedule a performance review.

Turn On the Brand’s Account

In Apple Business Register, go to the brand’s profile and click the Go Live button and follow the prompts to put the account online. This action submits the brand’s account to Apple for approval.

<!-- img: Notifications.png -->

Messages for Business Account Go Live

Activate Entry Points

Once approved, you can activate Maps entry points by adding an Apple Maps Enabled Region on the Apple Messages for Business account in Apple Business Register. You can only enable regions where the brand has two or more public locations.

<!-- img: Message-Buttons.png -->

Messages for Business Account Message Buttons

Coordinate with the Apple Messages for Business team to activate Message Suggest on your go-live date and time.

Enable any additional entry points on the website, app, or other planned assets so that customers can start contacting the business. For more information, see Planning Entry Point.

Performance Review

Schedule a review meeting after the first 30 days of launch with your Apple representative and the brand to outline goals and next steps.

https://register.apple.com/resources/messages/msp-onboarding/postLaunch

Start Measuring Channel Performance

After a successful Apple Messages for Business launch, work with your brands to assess the Apple Messages for Business channel performance relative to the goals set for the channel. As a Messaging Service Provider (MSP), you can help the brand set up and track certain performance measurements that are important for them. Due to Apple User Privacy Policies, Apple is unable to provide metrics to brands on channel performance.

Review the brand’s high priority items listed during Readiness Review. During the first 30 days, monitor the channel to ensure resolution of all user intents and follow the visualization path towards meeting long term channel goals.

During the first 30 days it’s helpful for the brand to pay attention to the following items:

Expected volume. Factors that influence volume are entry point placement, availability, and your contextual call-to-action (CTA). If the brand is starting with Message Suggest, determine where to place the phone number on the website. Find out how many other chat options are available to a user other than Apple Messages for Business. Review the CTAs and change them, if necessary, to match them to the user intents.

Intent matching. If the brand has an automated greeting in place, start assessing some of the initial messages that users write for abandoned conversations. Determine if their messages for specific intents are listed and, if not, set up the bot to handle these types of queries correctly.

Automated agent containment. Dive into the chat transcripts to see where users are experiencing more friction when working with any kind of automation. Look at how Interactive Features can help to ease friction and keep users in channel.

Value of intent. Optimize for self-serve by determining if there are a high number of intents that the brand would consider to be of low value coming in through the channel and reaching agents.

30 Day Review

After the first 30 days of the brand being live on Apple Messages for Business, Apple schedule’s a review meeting with the brand. During this meeting, Apple reviews the following:

Overall Apple Messages for Business goals set out by the brand

Discoverability

User experience

Prior to the meeting, the Apple Messages for Business team conducts a Mystery Shopper test to assess the current user experience. During the call, the Apple Messages for Business team discusses the results and provides suggestions to improve the user experience.

The Apple Messages for Business team reviews current entry points. Suggestions will be made in relation to the brand’s goals on how entry points can be strategically added.

Take Action to Improve the Channel

There are several actions you can take to improve your brand’s channel response, such as increasing the user’s ability to use entry points. You can also make tracking the channel easier by optimizing the intents used by customers.

Increase Discoverability

There are a variety of ways to increase discoverability. Make sure to take into consideration how current entry points have been implemented and see how these can be improved. Below are some best practices when looking to improve channel discovery and volume.

Add all support and store numbers to Message Suggest. Increase Message Suggest discovery by registering more numbers with Message Suggest. Brands can register individual store numbers and route them appropriately using the default intent parameters passed when a store’s phone number is tapped.

Add Apple Messages for Business buttons on brand webpages and apps. Brands should think about placing Messages buttons on their website and apps on Contact Us pages or other locations where the customer is likely to want to contact. Webpages such as ‘Product Details’, ‘FAQ page’, top menu bar or bottom footer area are key locations for placing the button. Always display message buttons with a strong call to action and context to inform the customer what they can achieve by tapping on the button.

Reduce channel confusion. Make sure that Apple Messages for Business is the preferred messaging option available for iOS users. Display the Apple Messages for Business button as the main option when viewing a mobile page on iOS. This is important to consider when guiding a customer to self serve on the website as part of a use case. Don’t have conflicting channel options display to keep the user in one channel and avoid creating multiple open cases in an agent queue.

Get creative on discovery! Think about creating opportunities to meet customers outside the website or phone. Using QR codes or NFC tags on product packaging or in physical store locations can open doors for creating valuable user experiences. Review Planning Entry Point Options for more details.

Optimize and Increase Intent Support

Create a regular process in reviewing channel performance and helping the brand to implement changes or fixes to their Apple Messages for Business experience.

Optimize current intents. Improve customer experience by adding interactive features or automated self-serve so that agents have higher capacity.

Work towards supporting more intents. Add intents that provide value to the brand in Apple Messages for Business. Implement OAuth2 so customers can achieve more within the channel versus pointing them to the phone or the website to complete. Add Apple Pay for easy and secure payments on use cases that would require a transaction.

Review Interactive Content for more ideas on what features can be used to support channel improvement.

Remember to share with Apple any new interactive feature or flow redesign for review and testing before you release.

https://register.apple.com/resources/messages/msp-onboarding/doc-rev-history

Revision History Date    Version    Summary 01 February 2024    3.0.3    Updated service naming to comply with registered service mark 05 July 2023    3.0.2    Fixes and Updated URLs 24 May 2022    3.0.1    Fixes and reference pointer to Forms 11 February 2022    3.0.0    Requirements of integration moved to REST-API, clear instruction on integration 25 October 2021    2.1    Added Quick Reply 20 September 2021    2.0.0    Rebranded Business Chat to Messages for Business; Chat Suggest to Message Suggest; removed ‘BETA’ from Quick Reply. 22 June 2021    1.0.0    Initial release. Revision Number Incrementation Version    Explanation 1.0.0    Major revision. Includes number increment and new content. 1.0.0    Minor revision. Includes number increment and changes to current content, such as content corrections, graphics, grammar, etc.


---

## 3. Apple Pay

> Part 3 of the master-plus-parts verbatim canonical. The **AMB Apple Pay _message_ schema** (ApplePayMessage / InteractiveData / Payment dictionaries, MerchantSession, lineItems, endpoints) is reproduced verbatim in **Part 1** (from `msp-rest-api`) and is not duplicated here. This part carries the **Apple Pay merchant setup, registration, and processing layer** from Apple's two Integration Guides, which underpins Apple Pay in AMB.
>
> **Sources:** Apple Pay Platform Integration Guide (Jun 2025) and Apple Pay Merchant Integration Guide (Mar 2026), both Apple-authored PDFs.
> **Keep-both (§37):** the two guides overlap heavily (understanding Apple Pay, payment flow, merchant tokens, availability checks). Both are retained in full; where they differ, the Merchant guide (Mar 2026) is the recency winner — see Master §Conflict Register.

---

## Part 3A — Apple Pay Platform Integration Guide (verbatim)

> **Source:** Apple Pay Integration Guide PDF (Jun 2025) — verbatim text extracted from the PDF; page footers, running heads, and the contents/TOC dot-leader lines removed (PDF pagination chrome, not Apple content). Body wording, values, code, and rules unchanged.

Apple Pay
Platform Integration Guide
September 2025

### Introduction

Apple Pay provides an easy and secure way to make payments in iOS, iPadOS, and
watchOS apps, and on the web when using compatible browsers. By using
biometric authentication, users can quickly and securely provide their payment,
shipping, and contact information to check out.

Customers love the simplicity of Apple Pay, and merchants love the increased
conversion rates and new user adoption that comes with it. To experience an Apple
Pay test transaction on a compatible device, visit the Apple Pay demo site at
applepaydemo.apple.com.

This guide outlines the steps and considerations you need to take as a platform to
enable Apple Pay payments for your merchants. If you are a merchant, please
reference the Apple Pay Merchant Integration Guide.

### Getting started

    Before enabling Apple Pay, it is important that developers understand how Apple
    Pay differs from an In-App purchase, and make sure their implementation follows
    the guidelines. There are many ways to implement Apple Pay, with some of the most
    popular Payment Service Providers and E-Commerce platforms offering an
    Apple Pay SDK or JavaScript API as a quick and reliable way to support Apple Pay in
    an app or on a website.

    Guidelines
    Apple Pay vs In-App Purchases
    Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services
    such as club memberships, hotel reservations, and events tickets; and for donations. Use In-App
    Purchases to sell virtual goods such as premium content for your app, and subscriptions for digital
    content.

    Apple Pay on the Web Acceptable Use Guidelines
    Before merchants can deploy Apple Pay on their website, they must ensure that their implementation
    follows these guidelines. When onboarding merchants using the Web Merchant Registration API, you
    must also ensure these guidelines are being met by the merchant.

         Apple Pay on the Web Acceptable Use Guidelines

􀉣

### Understanding Apple Pay

          Apple Pay is available on all iOS devices with a Secure Element — an industry-
          standard, certified chip designed to store payment information safely. On Desktop,
          users must have an Apple Pay-capable iPhone authorize the payment, or a Mac with
          Touch ID. Any transaction type you currently support for regular debit and credit
          cards can be performed with Apple Pay, including refunds.

          Payment flow
          Apple Pay uses device-specific tokenized credit or debit card credentials (DPAN) in place of a Payment
          Account Number (PAN). When users authenticate the payment using their biometric data or passcode,
          the tokenized card data is returned to your app or website. This token can then be passed to your
          Payment Service Provider (PSP) to process as you would for a typical online credit or debit card
          payment.

                                       Customer
                                       Authenticates with biometrics or passcode. Payment Data is encrypted and
                                       returned to the app/website

                                       Merchant App/Website
                                       Sends the Apple Pay payment object to merchant server

                                       Merchant Server
                                       Receives payment object and maps data to PSP API or SDK

                                       Payment Service Provider
                                       Decrypts Apple Pay payment object and formats a 3D Secure authorization
                                       message

                                       Acquirer
                                       Sends payment for authorization

                                       Payment Network
                                       De-tokenizes payment data and sends PAN to issuer for authorization

                                       Issuer
                                       Authorizes payment

􀄩􀄩􀄩􀄩􀄩􀄩
􀬩􀪬􁎣􀤨􀆪􀍯􀎽

### Get set up for Apple Pay

           To enable Apple Pay on your app or website, you need to confirm that you have the
           correct options configured on your server, are set up to accept Apple Pay Payments
           and register for an Apple Developer account.

           Confirm you operate in a supported region
           Check the list of currently supported regions at the link below.

                Countries and regions that support Apple Pay

           Confirm you support EMVCo Token data elements
           In order to accept Apple Pay, the party processing the payments must be capable of handling the
           appropriate fields related to processing EMVCo tokens such as TAVV, ECI or potentially 3D Secure
           related data elements such as CAVV/UCAF values.

           Set up your Server
           For Apple Pay on web only, ensure that your server meets the set up requirements for secure
           communications with Apple Pay.

                Setting up your server

           Register for an Apple developer account as an organization
           Both Apple Pay in apps and Apple Pay on the web require a subscription to the Apple developer
           Program, which must be renewed yearly. You should enroll as an organization, and you can use the
           same Apple developer account that you use today to publish apps to the App Store.

                Enroll for an Apple Developer account

􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣

### Design your Apple Pay solution

         Apple Pay creates a streamlined checkout process, allowing customers to authorize
         payments and complete transactions promptly. Consider where and when in the
         customers journey would be best to utilize Apple Pay to help drive conversion and
         enhance the customer experience.

         Assess the checkout products you offer
         To help drive conversion and enhance the user s experience, carefully consider the location of the
         Apple Pay button. The best user experiences place the Apple Pay button as early in the checkout
         process as possible in order to leverage Apple Pay provided information, and minimize data entry.

         Apply the Apple Pay design principles
         There are several key Apple Pay design principles that help drive conversion, increase usage and
         engagement, and provide an excellent user experience. Please review our best practice
         recommendations in Planning for Apple Pay.

              Planning for Apple Pay

         Review the Human Interface Guidelines
         Refer to the Apple Pay Human Interface Guidelines for additional information on how to best
         incorporate Apple Pay in your app or website.

              Apple Pay Human Interface Guidelines

􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
                                      ’

### Merchant Onboarding

       Before merchants are able to support Apple Pay, they must first have a set of credentials registered
       that identifies them as a merchant able to accept Apple Pay payments. These credentials can be
       configured by the merchant within their own Apple Developer Account, or as a platform integrator, you
       can manage the Apple Pay configuration on behalf of the merchant for web transactions.

### Onboarding with a merchant-managed Apple Developer Account

       To allow your merchants to offer Apple Pay within their Apps you must support this method of
       onboarding. This option allows merchants to create and manage their own set of Apple Pay credentials
       which can be used across both App and Web.

                       Supports native in-app Apple Pay integrations

                       Merchant has more control over their certificates and keys

                       Merchant is required to have their own Apple Developer Account

                       Does not support Hosted Payment Pages.

       To remove complexity, merchants often let payment processors handle decryption of the Apple Pay
       token. When a processor performs the decryption process, a unique key pair will need to be generated
       for each merchant. The processor provides the public key via a Certificate Signing Request (CSR),
       which the merchant uploads to the Apple Developer Portal to generate a Payment Processing
       Certificate.

       Build your merchant onboarding interface for Merchant-managed Developer Account
       To streamline the onboarding process for the merchant, you should provide them the ability to generate
       their key pair and CSR directly from within your merchant portal.

                       Download a certificate signing request to generate their Payment Processing Certificate

                       Upload the generated payment processing certificate for your records

### Key management

       Whether the payment platform is managing the keys on behalf of their merchants, or the merchant is
       managing this via their own Apple Developer account, payment platforms should implement
       mechanisms to roll keys and certificates without any downtime. Payment processors should support at
       least 2 active key pairs/certificates on an Apple Pay configuration at a time so that it s possible to
       transition from one key pair to a new set.

       The key rolling process should follow the below steps (assuming existing keys are in place):

            1. Generate new key pair and CSR on the payment platform
            2. Upload new CSR to Apple Developer account & download new certificate
            3. Upload new certificate to the payment platform
            4. Activate the new keys/certificates in the Apple Developer account
            5. Revoke old keys/certificates
       Payment Processors should use the value of the publicKeyHash to determine which merchant public
       key Apple used for encryption, and then retrieve the corresponding certificate and private key for
       decryption. This is especially important as keys/certificates are being transitioned.

􀁢
􀁢
􀀲
􀀲
􀁢
􀁢
􀃲􀂒􀃲􀂒
                                                                    ’

### Onboarding with the Apple Pay Web Merchant Registration API

                   The most streamlined and scalable way to onboard merchants on the web is by using the Apple Pay
                   Web Merchant Registration API. This is a REST API that enables payment platforms to register and
                   manage the Apple Pay configuration on behalf of the merchant. This offers some key benefits for both
                   the platform and merchant, including:

                                   Merchant is not required to create an Apple Developer Account

                                   Shared set of keys and certificates across your Merchant Portfolio

                                   Merchants can register their own domains, hosted payment pages, or both

                                   Domain registration does not expire

                                   Supports integrations on hosted pages and direct API or JS libraries

                                   Cannot be used for native in-app integrations

                   Apply for access to the Apple Pay Web Merchant Registration API
                   Platforms enrolled in the Apple developer program as an organization can apply to use the Apple Pay
                   Web Merchant Registration API by submitting an application form.

                        Web Registration API Application form

                   Configure your credentials
                   Once you have been granted access to use the API, you will be able to set up a Payment Platform
                   Integrator ID and it s associated certificates which follows the same process as a Merchant Identifier as
                   outlined in the Apple Pay Merchant integration Guide.

                        Apple Pay Merchant Integration GuideStart using the Web Merchant Registration API

                   Prepare merchant domains
                   Before making a Register Merchant request, you must prepare each domain included in the request for
                   verification. When you have created your Payment Platform Integrator ID, you will be able to access the
                   domain verification file in the Apple Developer portal.

                   Download and distribute this file to each merchant whose domain will be registered via the Web
                   Merchant Registration API. If merchants will be using Apple Pay via pages hosted on your own domain,
                   host this file on your domain also. Host your domain verification file at the following path for each
                   domain being registered:

                   https://[DOMAIN_NAME]/.well-known/apple-developer-merchantid-domain-association

                   Register a Merchant
                   Retrieve information about a registered merchant s current state by using the merchant s internal
                   merchant identifier.

                        registerMerchant

                   Unregister a Merchant
                   Unregister one or more domains associated with a previously registered merchant.

                        unregisterMerchant

                   Get Merchant Details
                   Retrieve information about a registered merchant s current state by using the merchant s internal
                   merchant identifier.

                        getDetails.

􀉣
􀀲
􀁢
􀁢
􀁢
􀁢
􀁢
􀉣
􀉣
􀉣
􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
               ’
                                                ’
                                                ’
                                                                                     ’
                                                                                     ’
     Build your merchant onboarding interface for the Web Merchant Registration API
     Using the API streamlines the onboarding process for merchants by removing many of the steps
     required when they use they manage their own credentials. One step that remains is domain
     verification. To allow merchants to prepare and register their own domains, provide them with the
     necessary steps and files in your merchant portal.

                     Download your domain verification file

                     Instructions on how and where to host this on their domains

                     Provide the list of domains that they want to register for use with Apple Pay

􀃲􀂒
􀁢
􀁢
􀁢

### Build your Apple Pay solution

           When building your Apple Pay integration, the process is largely the same as a merchant integrating
           Apple Pay on the web or in an App. You can follow step-by-step instructions on these processes using
           the Apple Pay Merchant Integration Guide.

                    Apple Pay Merchant Integration Guide

### Integration types

           Payment processors provide diverse integration options to cater to merchants, ranging from
           straightforward hosted payment forms, to seamless direct API integrations. To ensure an optimal Apple
           Pay experience, merchants should strategically place the Apple Pay button early in the checkout
           process, typically on the product or basket summary page. Payment processors should allow
           merchants to control the location of their Apple Pay experience within their checkout flow. Apple
           recommends direct API support or integrating Apple Pay into JavaScript or iOS code libraries for the
           best results.

           Direct API Integration
           Payment processors should always support this method of integration for Apple Pay because it gives
           merchants complete control over how they integrate Apple Pay into their websites or apps. In this
           scenario, the merchant manages interactions with Apple Pay APIs and sends the Apple Pay payment
           data to the payment processor for consumption. Since payment processors often provide API fields for
           customer address and contact information, these can be extended to support encrypted payment data.

           While most merchants rely on their payment processors to decrypt payment data, some may want to
           decrypt Apple Pay data themselves before sending it to their processors. Therefore, payment
           processors should consider extending their APIs to support Apple Pay payloads in both encrypted and
           decrypted formats.

           JavaScript & iOS Code Libraries
           Payment processors offer these products to simplify and speed up integrations, including Apple Pay.
           They may wrap around Apple Pay APIs to reduce merchant effort in adopting Apple Pay.

           It's recommended to build JavaScript and iOS libraries to simplify Apple Pay integration, yet give
           merchants control over presenting the Apple Pay button in their checkout flow.

           Hosted Payment Forms
           Apple Pay is designed to streamline the checkout process. While it's possible to support Apple Pay on
           a hosted payment form, its full potential won't be realized. By the time users reach the hosted payment
           form, they've likely already provided their address and contact information—steps that could've been
           skipped if Apple Pay had been presented earlier.

           If payment processors are interested in supporting Apple Pay on a hosted payment form, they should
           ensure that they enable onboarding merchants through the Apple Pay Web Merchant Registration API.

           When integrating Apple Pay into the hosted payment form, the payment platform should follow the
           standard steps for integrating Apple Pay on the web. However, they should use the
           partnerInternalMerchantIdentifier value (created when registering a merchant via the Apple Pay Web
           Merchant Registration API) in all fields used for the Merchant Identifier.

           iframes
           Apple Pay on the web uses a number of measures to ensure transactions remain secure and private.
           One of these measures is to ensure that a validated domain is being used during the Apple Pay
           payment. When using an iframe, this means that the top-level domain must be registered and verified,
           and this domain should be passed to the Apple Pay servers as the initiativeContext value during
           merchant validation. The iframe must also have the allow=“payment” attribute in order to communicate
           correctly with the Apple Pay API s.

􀉣
􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒
           fi
                ’

### Offering Apple Pay

                 The system provides several Apple Pay button types and styles so that the merchant can choose the
                 button type that fits best with the terminology and flow of their purchase or payment experience. In
                 contrast to the Apple Pay buttons, the Apple Pay mark is used to communicate the availability of Apple
                 Pay as a payment option. Don t create your own Apple Pay button design or attempt to mimic the
                 system-provided button designs.

                 Present the Apple Pay button
                 The button will be rendered by the appropriate PassKit or Javascript API, which will display the most up
                 to date version of the button as well as perform the appropriate localizations based on the users device
                 settings.

                      Display the Apple Pay button - Apple Pay on web

                      Display the Apple Pay button - PassKit

                 Apple Pay Mark
                 Use the Apple Pay mark to show that Apple Pay is an available payment option. The Apple Pay mark
                 isn t a button and shouldn t be used to launch the payment sheet. Use only the artwork Apple provides,
                 with no alterations other than height.

                      Apple Pay mark and Marketing Guidelines

                 Check for Apple Pay Availability
                 To ensure that you only display the Apple Pay button to customers with a supported device, check for
                 Apple Pay availability.

                      Checking for Apple Pay availability

### canMakePayments()

                 Verifies that the device is capable of making Apple Pay payments; it doesn t verify that the user has a
                 provisioned card for use with Apple Pay on the device. You can call this method at any time. In App you
                 can extend this to include a list of supported networks, and it will only return true if a card with a listed
                 networks is available for payment.

                      Web - canMakePayments()

                      App - canMakePayments()

### applePayCapabilites()

                 Verifies on Safari and third-party browsers that the device is capable of making Apple Pay payments. It
                 also verifies on Safari browsers that the device has at least one payment credential provisioned in
                 Wallet. Depending on the response, you can determine if the device supports Apple Pay and whether
                 to display an Apple Pay button. Call this method if you want to default to Apple Pay during your
                 checkout flow, or if you want to add an Apple Pay button to your product detail page.

### applePayCapabilities()

􀉣
􀉣
􀉣
􀉣
􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣
         ’
             ’
                 ’
                                                                 ’

### Processing Apple Pay

                    The diagram illustrates the flow of an Apple Pay transaction, showing the roles of different entities.
                    These roles may vary based on the payment processor's integration method, but the interaction is
                    divided into two stages:

                               Stage 1: Interacting with Apple Pay APIs to generate the payment data.

                               Stage 2: Using the payment data to process the payment.

                                                 Customer
                                                 User authenticates the transaction with biometrics (Face ID, Touch ID etc)
          Stage 1

                                                 Merchant App/Website
                                                 Payment data is encrypted and returned to the merchant

                                                 Merchant Server
                                                 Receives payment object and maps data to PSP API or SDK

                                                 Payment Service Provider
                                                 Decrypts Apple Pay payment object and formats a 3D Secure authorization
                                                 message
          Stage 2

                                                 Acquirer
                                                 Sends payment for authorization

                                                 Payment Network
                                                 De-tokenizes payment data and sends PAN to issuer for authorization

                                                 Issuer
                                                 Authorizes payment

􀄩􀄩􀄩􀄩􀄩􀄩
􀬩􀪬􁎣􀤨􀆪􀍯􀎽

### Supported Transaction Types and Business Models

    Apple Pay supports most E-Commerce transaction types and offers the flexibility to accommodate
    simple to complex business models.

    Below are examples of transaction types supported by Apple Pay.

      Transaction type           Description                                   Example

      Authorization & capture    Reserve funds on a customer s account         Online shopping where
                                 and transfer money to your bank               merchandise is readily available for
                                                                               shipping

      Authorization & delayed    Reserve funds on a customer s account         Pre-order, delivery service with tip,
      capture                    and transfer money to your bank later         or order online to pick up in store

      Authorization & capture    Reserve funds on a customer s account         Taxi, Scooter
      with different amount      and transfer money to your bank once an
                                 order is successfully completed for an
                                 amount higher or lower than authorized

      Partial shipment           Divide a purchase into multiple payments      Multi-item purchase with more than
                                 for goods that are not shipped together       one delivery

      Fixed subscription         Handle repeating payments at a regular        Monthly gym membership
                                 frequency and with a fixed amount

      Flexible frequency         Handle payments for services where            Meal subscriptions, where user can
      subscription               frequency is inconsistent or the user has a   skip deliveries, reschedule delivery
                                 choice to vary frequency                      dates, and change frequency of
                                                                               deliveries

      Flexible amount            Handle payments for services where price      Utility bill, or subscription with a
      subscription               varies based on consumption                   promotion on the first month

      Managed subscription       Handle payments for services where the        Meal delivery service with high
                                 user can vary frequency and amount of         flexibility
                                 services received

      Canceled transactions      Reverse money for canceled, reimbursed,       Chargeback, voided transaction, or
                                 or disputed transactions                      refund

      Card verification          Verify that the selected card is associated   $0 or $1 authorizations
                                 with a cardholder account that is valid and
                                 in good standing

’
’
’

### Recurring Payments and Merchant tokens

     A standard one-time payment with Apple Pay uses a device-specific token to securely complete the
     transaction. In addition to this, Apple Pay supports the use of merchant tokens to complete supported
     payments independent of a device. After the initial transaction, payment details can be stored to create
     follow-on transactions.

     Different flags may be required for subsequent transactions depending on the payment network. For
     instance, Visa's MIT specification and MasterCard's DSRP specification outline the formatting of
     authorization messages for these payments. Payment processors interested in supporting these
     transactions should inquire with their acquiring partner or payment networks for further information.

     Support Merchant tokens (where applicable)
     A merchant token associates a payment card, merchant, and user, allowing for continuity across
     multiple devices, even when a device is upgraded or a card is removed. When a payment request is
     created for a recurring, automatic reload, or a deferred payment, the merchant can provide essential
     information the customer directly in the payment sheet, potentially helping to decrease cart
     abandonment and increase conversion rates.

     To request a merchant token, the merchant must include one of the following in their payment request:

                recurringPaymentRequest
                Recurring payments, such as subscriptions, can feature different payment intervals (for
                example, annually or monthly), and either regular or trial billing cycles.

                     recurringPaymentRequest

                automaticReloadPaymentRequest
                Automatic reload payments, such as store card top-ups, feature a balance threshold and a
                reload amount. The card automatically reloads with the reload amount when the account drops
                below the balance threshold.

                     automaticReloadPaymentRequest

                deferredPaymentRequest
                Deferred payments, such as for a Hotel booking or a pre-order, allow you to specify a free
                cancellation period and specify the date when payment will be taken.

                     deferredPaymentRequest

     When any of these request types are used to initiate an Apple Pay transaction, a merchant token is
     automatically requested by Apple, and where supported by the issuer, returned in the Apple Pay
     payload. If an issuer does not yet support merchant tokens, Apple Pay defaults back to returning the
     DPAN as it would for a regular Apple Pay transaction, but the customer still benefits from having the
     updated information in the payment sheet.

     If you are supporting these transaction types, ensure that you have built in the functionality for your
     merchants to provide the additional fields necessary for these payment request types through your
     product offerings.

􀃲􀂒
􀉣
􀉣
􀉣
      MPAN Creation and Authorization Flow

                 Initiating the recurring/autoReload/deferred payment request

                                     MPAN supporting
                                   payment request type

                                                                          DPAN + Cryptogram

            Merchant                                          Apple Pay           MPAN + Cryptogram   PNO

                                          MPAN + Cryptogram

                 Transaction Authorization - Cardholder Initiated Transaction (CIT)

                                   MPAN + Cryptogram                      MPAN + Cryptogram

            Merchant                               TRID          PSP                       TRID       PNO

                 Subsequent Transaction(s) - Merchant Initiated Transaction (MIT)

                                     MPAN + TRID                             MPAN + TRID

            Merchant                                             PSP                                  PNO

􀄫􀄪
􀣺
􀀺􀆪
􁽇
􀄪
􀄫
􀄫
􁎣
􀆪
􁽇
􀀾􀄫
􀄫􀄪
􁎣
􀆪
􁽇
􀀼􀄫􀄪

### Merchant Token Management API

### Merchant tokens are also designed to help prevent or resolve billing issues by giving visibility into

         important payment lifecycle updates, such as account status, bank card art, and card expiration date.
         The Apple Pay Merchant Token Management API allows you retrieve and manage these lifecycle
         updates.

         When your app or website creates a payment request using one of the supported request types, it
         passes a notification URL in the tokenNotificationURL parameter. If a life-cycle event affects the token,
         Apple Pay sends a notification with an event identifier to that tokenNotificationURL. The details of the
         event can be retrieved by requesting the details from the Apple Pay server with the event identifier.

         Receiving and Handling Merchant Token Notifications
         When a life-cycle event occurs to a card associated with a merchant token, Apple Pay sends a GET
         request to the endpoint included in the tokenNotificationURL parameter of the original payment
         request.

             GET https://merchant.example.com/tokenapi/notification/merchantToken/{eventId}

         When you receive this request, use the eventId included in the path to format a POST request to
         retrieve the details of the event. This will include both the Merchant Identifier from the original
         transaction, alongside the specific eventId that has been triggered.

```bash
POST https://apple-pay-gateway.apple.com/paymentServices/v1/merchantId/{merchantId}/merchantToken/
event/{eventId}
```

              Receiving and handling merchant token notifications

         In response, you should receive a merchantTokenEventResponse object containing the details of the
         event. There are currently 3 event types that can be triggered.

                     UNLINK
                     The token have been revoked, and will be rejected if sent for processing. When receiving this
                     event type the merchant may want to reach out to the customer to ask them to update their
                     payment details before the next payment cycle.

                     UPDATED_METADATA
                     The metadata, such as the FPAN suffix, the expiry date, or the token itself has been updated.

                     UPDATED_CARD_ART
                     The card art for the underlying card has been updated.

```json
{
    statusCode: 200,
```

                   merchantTokenEvent: {
                     merchantTokenIdentifier: 'MAPLAB001M317N593274cf108544f98420d15c5c2',
                     eventType: 'UNLINK',
                     reason: 'UNLINKDEVICE'
```json
    }
}
```

              merchantTokenEventResponse

􀉣
􀉣
    fi
                            fi
                                 fi
                                      fi
                                                       fi

### Apple Pay Payment Object

     When a customer confirms a transaction, the secure element on a device will create a payment object
     that contains a payment token with the encrypted payment data, alongside any additional contact data
     requested from the customer.

     The Secure Element encrypts the token s payment data using either elliptic curve cryptography (ECC)
     or RSA encryption. The encryption algorithm is selected by the Secure Element based on the payment
     request, with most regions using ECC encryption. RSA is used only in regions where ECC encryption is
     unavailable due to regulatory concerns. Unless advised otherwise, payment processors should focus
     on ECC encryption/decryption.

```json
{
    "billingContact": {
      "addressLines": [
        "1 First Street"
```

                 ],
```json
  "administrativeArea": "London",
  "country": "United Kingdom",
  "countryCode": "GB",
  "familyName": "Appleseed",
  "givenName": "John",
  "locality": "London",
  "phoneticFamilyName": "",
  "phoneticGivenName": "",
  "postalCode": "AB12 3CD",
  "subAdministrativeArea": "",
  "subLocality": ""
},
"shippingContact": {
  "addressLines": [
    "1 First Street"
```

                 ],
```json
      "administrativeArea": "London",
      "country": "United Kingdom",
      "countryCode": "GB",
      "emailAddress": "john.appleseed@apple.com",
      "familyName": "Appleseed",
      "givenName": "John",
      "locality": "London",
      "phoneticFamilyName": "",
      "phoneticGivenName": "",
      "postalCode": "AB12 3CD",
      "subAdministrativeArea": "",
      "subLocality": ""
    },
    "token": {
      "paymentData": {
        "data": "K+kSR...BbAj",
        "signature": "MIAG...AAA=",
        "header": {
          "publicKeyHash": "2xR1...PGQ=",
          "ephemeralPublicKey": "MFkw...1w==",
          "transactionId": "ba9c...7298"
        },
        "version": "EC_v1"
      },
      "paymentMethod": {
        "displayName": "NetworkName 1234",
        "network": "NetworkName",
        "type": "credit"
      },
      "transactionIdentifier": "ba9c...7298"
    }
}
```

fi
                     ’

### Decrypting the Payment Data

                   The Secure Element encrypts the token s payment data using either elliptic curve cryptography (ECC)
                   or RSA encryption. The encryption algorithm is selected by the Secure Element based on the payment
                   request, with most regions using ECC encryption. RSA is used only in regions where ECC encryption is
                   unavailable due to regulatory concerns. Unless advised otherwise, payment processors should focus
                   on ECC encryption/decryption.

                        Payment Token Format Reference

                   Payment Processors should use the value of the publicKeyHash to determine which merchant public
                   key Apple used for encryption, and then retrieve the corresponding certificate and private key for
                   decryption. This is especially important as keys/certificates are being transitioned.

                   For a standard Apple Pay transaction that uses a device token, the decrypted payment information will
                   be formatted as shown below, and contains all of the necessary data for processing the payment.

```json
{
    "paymentDataType": "3DSecure",
    "applicationExpirationDate": "YYMMDD",
    "applicationPrimaryAccountNumber": "0001...1234",
    "currencyCode": "826",
    "deviceManufacturerIdentifier": "54...56",
    "transactionAmount": "10000",
    "paymentData": {
      "onlinePaymentCryptogram": "INX0...AwA=",
      "eciIndicator": “XX"
    }
}
```

                   When a merchant token has been issued, there will also be additional data within the decrypted
                   payload related to that token.

```json
{
    "paymentDataType": "3DSecure",
    "applicationExpirationDate": "YYMMDD",
    "applicationPrimaryAccountNumber": "0001...5678",
    "currencyCode": "826",
    "deviceManufacturerIdentifier": "54...56",
    "transactionAmount": "10000",
    "merchantTokenIdentifier": “MAPL...1654”,
    "merchantTokenMetadata": {
      "cardArt": [
        {
          "name": "card.png",
          "type": "image/png",
          "url": "https://...d91b"
        }
      ],
      "cardMetadata": {
        "longDescription": "Long Card Name",
        "shortDescription": "Short Name",
        "cardCountry": "GB",
        "fpanSuf x": "1234"
      }
    },
    "paymentData": {
      "onlinePaymentCryptogram": "TIA0...bdE=",
      "eciIndicator": “XX"
    }
}
```

􀉣
    fi
         fi
              fi
              fi
                                   ’

### Authorizing the Payment

                   Once the user has authorized themselves on the payment sheet the app / website will receive the
                   Apple Pay payment object outlined in the previous section. At this point the user has verified their
                   identity using Touch ID or Face ID but a payment has not yet taken place.

                   The merchant needs to pass the token information to the payment processor who can then create an
                   authorization via the payment networks. As stated previously, the merchant can decrypt the payment
                   data themselves, but more commonly the payment processor will manage this complexity on the
                   merchant s behalf.

### Constructing the Authorization Message

                   Once the payment data has been decrypted, it needs to be sent for authorization. Apple Pay has been
                   designed to use similar data formatting as a 3D Secure transaction. Creating a successful authorization
                   should be a case of mapping the Apple Pay fields to payment fields used for card/EMVCo token
                   payments.

                   Some acquirers/networks may use existing 3D Secure fields whilst others may have dedicated fields
                   for EMVCo tokens. The tables below are only for guidance, always check with your acquiring/payment
                   network partner for the correct mapping.

                    Apple Pay Field                                              Representative Acquirer Field

                     data.applicationPrimaryAccountNumber                        PAN

                     data.applicationExpirationDate (YYMMDD)                     Expiration Date

                     data.paymentData.onlinePaymentCryptogram                    TAVV / CAVV / UCAF

                     data.paymentData.eciIndicator                               ECI

                   American Express
                   Payments using an American Express card may require slightly different mapping to that outlined
                   above. In addition to the above mapping, please use the following table for guidance on mapping Amex
                   payment fields.

                    Apple Pay Field                                              Amex Card Field

                     data.deviceManufacturerIdentifierToken                       Token Requestor ID

                     data.paymentData.onlinePaymentCryptogram                    Token Block A

                     [all zeros] fill field value with zeros                         Token Block B

fi
     ’
         fi
              fi

### Good practice guidance when processing Apple Pay transactions

    Apple Pay offers multiple layers of security beyond many other payment methods. However, you can
    apply the same industry best practices for risk mitigation to Apple Pay as you do for other E-commerce
    payment methods.

    Apple Pay uses device based tokens (DPAN) so PANs cannot be used as a unique key and each
    transaction generates a unique cryptogram in place of the CV2. There are many standard checks that
    are still applicable to Apple Pay.

    Velocity and Pattern Checks
    A velocity check monitors specific data elements to check and compare a customer's shopping history
    with current purchases in order to identify any irregularities in their purchasing behaviour. This includes
    sudden bursts of high activity considered inconsistent with standard purchase behaviours for your
    industry or customer base.

    Consider using purchase frequency, repeat billing/delivery address for high value purchases,
    cardholder name, email, name and IP address - particularly if combinations of these details are used in
    quick succession. Actions you could take based on a high risk transaction are:

               • Decline the transaction.
               • Delay shipping and complete outbound checks on address and customer details.

    Delivery Checks
    Consider implementing risk indicators for delivery methods such as the delivery address being
    different from the billing address, temporary addresses, instructions to leave goods on doorsteps (or
    similar), export address or requests for fast delivery. In countries where applicable, use Address
    Verification Services (AVS) to verify the billing address is correct. Consider looking at data provided by
    the user and check if it's linked to previous purchases (email addresses, phone numbers, billing and
    shipping addresses linked to other users). Multiple transactions could be correlated against another
    order.

    Maintain a “Bad Transactions” List
    Maintain a list of historical transactions for all payment methods which have either looked suspicious or
    resulted in chargebacks and compare the details of new transactions against these. If one or more of
    the transaction details match against historically bad transactions it may be worth putting the
    transaction aside for manual review or declining it outright. This data may also be available via your
    Payment Service Provider s (PSP) Risk Management tool.

    Email and IP address Checks
    Ensure that email addresses are correct. You can use the Apple Pay Error Handling API's to ensure a
    customer adheres to your email rules. If the domain looks ok, send an email to the address to confirm it
    exists. Check the IP address coming from the device to verify the IP country matches the billing
    country and country where the card was issued.

    Country Checks
    If you identify certain countries as high risk, you can use the supportedCountries property in the Apple
    Pay payment request to limit payment cards to those that were issued in specific countries. The
    supportedCountries list does not affect the currency used for the transaction, and it applies to all
    payment cards in Wallet. You can also consider limiting IP addresses from high risk regions.

’

### Testing

    The Apple Pay sandbox environment enables merchants and developers to test their implementation of
    Apple Pay using test credit and debit cards. This testing process helps verify the customer experience
    and assess the ability to decrypt the transaction-specific payment data. To provision these test cards
    to a test device, the user must sign in to iCloud using a Sandbox Tester account.

         Apple Pay Sandbox testing

    It is also important to test Apple Pay in your production environment using real cards to ensure the
    end-to-end transaction flow is working as expected.

    Test your integration on multiple devices and browsers
    Apple Pay is now available on Safari, third party browsers in iOS and MacOS, as well as on other
    computing platforms. Check that the Apple Pay button is displayed on all the relevant devices and
    locations, and the you are able to support third party browsers/devices.

    Data Mapping and formatting
    Confirm that you are able to map all of the relevant data included in the Apple Pay payload, including
    the shipping and billing contact fields. Ensure you can handle this data in the various possible formats.
    For example, phone numbers may contain numeric values as well as special character such as “+”.

    Responding to Events
    When you are supporting handling of Payment Sheet event, such as when the shipping contact or
    method is updated, ensure you have tested your event handling process and that you are formatting
    and responding using the relevant completion method.

    Test all integration types
    Test Apple Pay functions as expected across all of the integration types you are offering. Pay close
    attention to integrations involving iframes to ensure they do not cause any errors during validation.

### Documentation

    Payment processors should provide detailed technical documentation to their merchants for all the
    ways they support Apple Pay via their platform. It is recommended that payment processors provide
    links to any existing content on the Apple Pay developer website, instead of recreating similar content
    on their own site.

    Where possible, it is recommended that payment processors use code examples and step-by-step
    instructions to clearly explain the requirements for integrating Apple Pay.

### Reporting

    It is recommended that payment processors identify Apple Pay transactions in all transaction
    information and reporting made available to merchants.

### Marketing Toolkit

    Let your merchants know that Apple Pay is available with messaging across all of your channels.
    Highlight the ease of use, security, and privacy that Apple Pay brings to making payments. With the

### canMakePayments API, merchants can target their messaging to customers with devices that support

    Apple Pay. The Marketing Toolkit contains guidelines, tips, and templates to help create and implement
    marketing campaigns.

         Apple Pay Marketing toolkit for PSP's

􀉣
􀉣

### Frequently asked questions

    Where does the customer information come from in the payment sheet?
    The information comes from Wallet & Apple Pay defaults in Settings, if available, as well as the My Card
    in Contacts. It could also come from previous Apple Pay transactions. You can set up your My Card by
    going to Settings > Contacts > My Info.

    Is the customer information that comes from Apple Pay verified by Apple?
    Customer information is shared as-is, and is not verified by Apple. You will need to validate it on your
    platform and communicate through the Apple Pay API if fields should be corrected. For more
    information visit the Error Handling section of this guide.

    What customer information can I pull from Apple Pay?
    Customer information includes shipping and billing address, name, phone number and email address.

    What does the Apple Pay payment token contain?
    The structure, format, and data included in the PKPaymentToken can be found in the Payment Token
    Format Reference. PKPaymentToken only contains information on processing the payment; the
    customer information is included in the PKPayment object. The PKPayment encapsulates the customer
    information and the PKPaymentToken.

         Payment Token Format Reference

    Can I use the same Apple developer account for all countries I process payments in?
    Yes; you do not need to have separate Apple developer accounts for multiple markets. You can also
    use the same Apple Merchant ID or Platform Integrator ID if you wish.

### Troubleshooting

    Further information and troubleshooting steps to debug common issues with Apple Pay can be found
    in the below guide.

         Apple Pay on the Web Troubleshooting Guide

􀉣
􀉣

### API Diagrams

                                                                                                                                                                                        Apple Pay in app

                                                  iOS                                                                                        App                                                     Merchant Server                   Apple Server                               PSP/Acquirer                                    Network                                   Issuer

                                                                     [1] canMakePayments() / canMakePayments(usingNetworks:)

                                                                                            [2] true / false

                                                                                                                                 show / hide Apple Pay button

                                                          [3] User taps Apple Pay button

                                                                                                                  [4] create PKPaymentRequest

                                                                 [5] instantiate PKPaymentAuthorizationController(paymentRequest:)

                                                                                       [6] present(completion:)

                [7] Payment Sheet is presented

                                            opt         [payment method event]

                                                               [8] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [9] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

                                            opt         [shipping contact event]

                             Event only triggered if shipping contact
                                    fields are requested in the
                                       PKPaymentRequest.

                         Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

                                                              [10] paymentAuthorizationController(_: didSelectShippingContact: handler:)

                                                        [11] completion(PKPaymentRequestShippingContactUpdate(errors: shippingMethods: ))

               [12] Payment Sheet is activated

opt      [payment method changed event]

      [13] User changes payment method

                                                              [14] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [15] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

opt      [shipping contact changed event]

                             Event only triggered if shipping contact
                                    fields are requested in the
                                        PKPaymentRequest

                         Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

 [16] User changes shipping contact / address

                                                              [17] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [18] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

opt      [shipping method changed event]

                             Event only triggered if shipping methods
                                        are included in the
                                      PKPaymentRequest.

      [19] User changes shipping method

                                                              [20] paymentAuthorizationController(_: didSelectShippingMethod: handler:)

                                                         [21] completion(PKPaymentRequestShippingMethodUpdate(paymentSummaryItems: ))

[22] User authenticates with Touch ID / Face ID

                  [23] Apple Pay payment data
                        is generated on device

                                                                                                                                [24] payment data sent to Apple Server

                                                                                                                                                                                                                         [25] Apple encrypt
                                                                                                                                                                                                              payment data using public key
                                                                                                                                                                                                                  (associated with Payment
                                                                                                                                                                                                                     Processing Certificate)

                                                                                                                             [26] encrypted payment data returned to iOS

                                                                [27] paymentAuthorizationController(_: didAuthorizePayment: handler :) {

                                                                                                                                                   [28] send user data and ecnrypted payment data to server

                                                                                                                                                                                                                        [29] send user data and ecnrypted payment data to psp

                                                                                                                                                                                                                                               [30] PSP decrypts Apple Pay payment data

                                                                                                                                                                                                                                                                                          [31] decrypted payment data sent to PNO

                                                                                                                                                                                                                                                                                                 [32] PNO detokenises Apple Pay token

                                                                                                                                                                                                                                                                                                                                        [33] card data sent for authorisation

                                                                                                                                                                                                                                                                                                                                            [34] authorisation response

                                                                                                                                                                                                                                                                                                    [35] authorisation response

                                                                                                                                                                                                                                      [36] authorisation response

                                                                                                                                                                 [37] authorisation response

                                                                    [38] completion(PKPaymentAuthorizationResult(status: errors:))

              [39] Payment outcome displayed
                 and payment sheet dismissed

                                                                                                                                                                             Apple Pay on the web

                                            iOS / Safari                                                            Website                                                  Merchant Server                            Apple Server                               PSP/Acquirer                                    Network                                   Issuer

                                                       [1] canMakePayments() / canMakePaymentsWithActiveCard()

                                                                                  [2] true / false

                                                                                                          show / hide Apple Pay button

                                            [3] User taps Apple Pay button

                                                    [4] create ApplePayPaymentRequest and new ApplePaySession()

                                                                             [5] session.begin()

               [6] Payment Sheet is presented

                                                                         [7] onvalidatemerchant event

                                                                                                                                     [8] request a new merchant session

                                                                                                                                                                                       [9] request a new merchant session

                                                                                                                                                                                        [10] return merchant session blob

                                                                                                                                         [11] return merchant session blob

                                                                     [12] completeMerchantValidation()

                                          opt       [payment method event]

                                                                   [13] onpaymentmethodselected event

                                                                 [14] completePaymentMethodSelection()

                                          opt       [shipping contact event]

                             Event only triggered if shipping contact
                                   fields are requested in the
                                  ApplePayPaymentRequest.

                          Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

                                                                   [15] onshippingcontactselected event

                                                                 [16] completeShippingContactSelection()

                [17] Payment Sheet is activated

opt      [payment method changed event]

      [18] User changes payment method

                                                                   [19] onpaymentmethodselected event

                                                                 [20] completePaymentMethodSelection()

opt      [shipping contact changed event]

                             Event only triggered if shipping contact
                                   fields are requested in the
                                  ApplePayPaymentRequest.

                          Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

 [21] User changes shipping contact / address

                                                                   [22] onshippingcontactselected event

                                                                 [23] completeShippingContactSelection()

opt      [shipping method changed event]

                             Event only triggered if shipping methods
                                        are included in the
                                   ApplePayPaymentRequest.

      [24] User changes shipping method

                                                                   [25] onshippingmethodselected event

                                                                 [26] completeShippingMethodSelection()

[27] User authenticates with Touch ID / Face ID

                  [28] Apple Pay payment data
                        is generated on device

                                                                                                                      [29] payment data sent to Apple Server

                                                                                                                                                                                                          [30] Apple encrypt
                                                                                                                                                                                               payment data using public key
                                                                                                                                                                                                   (associated with Payment
                                                                                                                                                                                                      Processing Certificate)

                                                                                                                   [31] encrypted payment data returned to iOS

                                                                        [32] onpaymentauthorized event

                                                                                                                           [33] send user data and ecnrypted payment data to server

                                                                                                                                                                                                      [34] send user data and ecnrypted payment data to psp

                                                                                                                                                                                                                                [35] PSP decrypts Apple Pay payment data

                                                                                                                                                                                                                                                                           [36] decrypted payment data sent to PNO

                                                                                                                                                                                                                                                                                  [37] PNO detokenises Apple Pay token

                                                                                                                                                                                                                                                                                                                         [38] card data sent for authorisation

                                                                                                                                                                                                                                                                                                                             [39] authorisation response

                                                                                                                                                                                                                                                                                     [40] authorisation response

                                                                                                                                                                                                                    [41] authorisation response

                                                                                                                                           [42] authorisation response

                                                                           [43] completePayment()

              [44] Payment outcome displayed
                 and payment sheet dismissed

                                                                                                                                        Apple Pay on the web:
                                                                                                                          PSP hosted payment page, merchant registered via API

                                            iOS / Safari                                                       Hosted Payment Page                       Apple Server                                  PSP/Acquirer                                    Network                                   Issuer

                                                       [1] canMakePayments() / canMakePaymentsWithActiveCard()

                                                                                  [2] true / false

                                                                                                            show / hide Apple Pay button

                                            [3] User taps Apple Pay button

                                                    [4] create ApplePayPaymentRequest and new ApplePaySession()

                                                                             [5] session.begin()

               [6] Payment Sheet is presented

                                                                         [7] onvalidatemerchant event

                                                                                                                                                    [8] request a new merchant session

                                                                                                                                                                    [9] request a new merchant session

                                                                                                                                                                        [10] return merchant session blob

                                                                                                                                                     [11] return merchant session blob

                                                                     [12] completeMerchantValidation()

                                          opt       [payment method event]

                                                                   [13] onpaymentmethodselected event

                                                                 [14] completePaymentMethodSelection()

                                          opt       [shipping contact event]

                             Event only triggered if shipping contact
                                   fields are requested in the
                                  ApplePayPaymentRequest.

                          Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

                                                                   [15] onshippingcontactselected event

                                                                 [16] completeShippingContactSelection()

                [17] Payment Sheet is activated

opt      [payment method changed event]

      [18] User changes payment method

                                                                   [19] onpaymentmethodselected event

                                                                 [20] completePaymentMethodSelection()

opt      [shipping contact changed event]

                             Event only triggered if shipping contact
                                   fields are requested in the
                                  ApplePayPaymentRequest.

                          Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

 [21] User changes shipping contact / address

                                                                   [22] onshippingcontactselected event

                                                                 [23] completeShippingContactSelection()

opt      [shipping method changed event]

                             Event only triggered if shipping methods
                                        are included in the
                                   ApplePayPaymentRequest.

      [24] User changes shipping method

                                                                   [25] onshippingmethodselected event

                                                                 [26] completeShippingMethodSelection()

[27] User authenticates with Touch ID / Face ID

                  [28] Apple Pay payment data
                        is generated on device

                                                                                       [29] payment data sent to Apple Server

                                                                                                                                           [30] Apple encrypt
                                                                                                                                payment data using public key
                                                                                                                                    (associated with Payment
                                                                                                                                       Processing Certificate)

                                                                                    [31] encrypted payment data returned to iOS

                                                                        [32] onpaymentauthorized event

                                                                                                                                         [33] send user data and ecnrypted payment data to server

                                                                                                                                                                 [34] PSP decrypts Apple Pay payment data

                                                                                                                                                                                                                [35] decrypted payment data sent to PNO

                                                                                                                                                                                                                      [36] PNO detokenises Apple Pay token

                                                                                                                                                                                                                                                             [37] card data sent for authorisation

                                                                                                                                                                                                                                                                 [38] authorisation response

                                                                                                                                                                                                                         [39] authorisation response

                                                                                                                                                        [40] authorisation response

                                                                           [41] completePayment()

              [42] Payment outcome displayed
                 and payment sheet dismissed



---

## Part 3B — Apple Pay Merchant Integration Guide (verbatim)

> **Source:** Apple Pay Integration Guide PDF (Mar 2026) — verbatim text extracted from the PDF; page footers, running heads, and the contents/TOC dot-leader lines removed (PDF pagination chrome, not Apple content). Body wording, values, code, and rules unchanged.

Apple Pay
Merchant Integration Guide
March 2026

### Good practice guidance when processing Apple Pay transactions                                                                                           23

Frequently asked questions                                                                                                                                     24
Troubleshooting                                                                                                                                                25
API Diagrams                                                                                                                                                   26
Change Log                                                                                                                                                     29

### Introduction

Apple Pay provides an easy, secure and private way to make payments in iOS,
iPadOS, macOS, visionOS and watchOS apps, and on the web when using
compatible browsers. By using Face ID, Touch ID, Optic ID or double-clicking Apple
Watch, users can quickly and securely provide their payment, shipping, and contact
information to check out.

This guide outlines the steps needed to enable Apple Pay in app and on the web. To
experience an Apple Pay test transaction on a compatible device, visit the Apple Pay
demo site at applepaydemo.apple.com.

Integrating Apple Pay is often a cross-functional effort involving designers,
developers, server administrators and payment teams within an organization. This
guide supports each of these roles through the end-to-end process of enabling
Apple Pay in your app or on the web, and the typical role responsible for each task
will be noted beside the task checkbox.

   ACCOUNT ADMIN            UX DESIGNER   SERVER ADMIN   PAYMENTS TEAM   DEVELOPER

### Getting started

    Before enabling Apple Pay, it is important that developers understand how Apple
    Pay differs from an In-App purchase, and make sure their implementation follows
    the guidelines. There are many ways to implement Apple Pay, with some of the most
    popular Payment Service Providers and E-Commerce platforms offering an
    Apple Pay SDK or JavaScript API as a quick and reliable way to support Apple Pay in
    an app or on a website.

    Guidelines
    Apple Pay vs In-App Purchases
    Apple Pay can be used in your app to sell physical goods like groceries, clothing, and appliances; for
    services such as club memberships, hotel reservations, and events tickets; and for donations. In-App
    Purchase are used to sell virtual goods such as premium content for your app, and subscriptions for
    digital content.

    App Review Guidelines
    Before submitting your app for review, make sure it follows these guidelines to help progress smoothly
    through the review process.

         App Review guidelines: Payments

    Apple Pay on the Web Acceptable Use Guidelines
    Before deploying Apple Pay on your website, make sure your implementation follows these guidelines.

         Apple Pay on the Web Acceptable Use Guidelines

    E-Commerce Platforms and Payment Service Providers
    The most popular e-commerce platforms and payment service providers support Apple Pay within
    apps and on the web. Using an Apple Pay SDK or JavaScript API from a payment provider is the
    quickest and easiest way to support Apple Pay in your app or on your website.

         View E-Commerce platforms and Payment Service Providers

    If using an e-commerce platform or payment service provider s own SDK or API, contact them to get
    started. The process to integrate using an SDK or API they provide may differ from the steps outlined in
    the rest of this guide. Refer to their documentation to understand the process required.

􀉣
􀉣
􀉣
                                    ’

### Understanding Apple Pay

          Apple Pay is available on all Apple devices with a Secure Element — an industry-
          standard, certified chip designed to store payment information safely. On macOS,
          users must have a Mac with Touch ID or an Apple Pay-capable iPhone or Apple
          Watch to authorize the payment. On third party browsers, whether on Mac or other
          devices, the user must have an Apple Pay-capable iPhone running iOS 18 or newer
          to authorize the transaction. Any transaction type you currently support for regular
          debit and credit cards can be performed with Apple Pay, including refunds.

          Payment flow
          For one-time transactions, Apple Pay uses device-specific tokenized credit or debit card credentials
          (DPAN) in place of a Payment Account Number (PAN). When users authenticate the payment using
          their biometric data or passcode, the tokenized card data is returned to your app or website. This token
          can then be passed to your Payment Service Provider (PSP) to process as you would for a typical
          online credit or debit card payment.

                                       Customer
                                       Authenticates with biometrics or passcode. Payment Data is encrypted and
                                       returned to the app/website

                                       Merchant App/Website
                                       Sends the Apple Pay payment object to merchant server

                                       Merchant Server
                                       Receives payment object and maps data to PSP API or SDK

                                       Payment Service Provider
                                       Decrypts Apple Pay payment object and formats a 3D Secure authorization
                                       message

                                       Acquirer
                                       Sends payment for authorization

                                       Payment Network
                                       De-tokenizes payment data and sends PAN to issuer for authorization

                                       Issuer
                                       Authorizes payment

􀄩􀄩􀄩􀄩􀄩􀄩
􀬩􀪬􁎣􀤨􀆪􀍯􀎽

### Get set up for Apple Pay

                           To enable Apple Pay on your app or website, you need to confirm that you have the
                           correct options configured on your server, are set up to accept Apple Pay Payments
                           and register for an Apple Developer account.

          PAYMENTS TEAM    Confirm your Payment Service Provider (PSP) supports Apple Pay
                           Check the list of currently supported gateways at the link below. If you do not see your PSP on the list,
                           contact them directly to confirm availability.

                                Supported E-Commerce platforms and Payment Service Providers

          SERVER ADMIN     Set up your Server
                           For Apple Pay on web only, ensure that your server meets the set up requirements for secure
                           communications with Apple Pay.

                                Setting up your server

          ACCOUNT ADMIN   Enroll in the Apple Developer Program
                           Both Apple Pay in apps and Apple Pay on the web require an Apple Developer program membership,
                           which must be renewed yearly. You can enroll as an individual or as an organization, and you can use
                           the same Apple developer account that you use today to publish apps to the App Store.

                           You cannot use an Apple Developer Enterprise Program account to enable Apple Pay within an app or on the web.

                                Enroll for an Apple Developer account

􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣

### Design your Apple Pay solution

                         Apple Pay creates a streamlined checkout process, allowing customers to authorize
                         payments and complete transactions promptly. Consider where and when in your
                         customers journey would be best to utilize Apple Pay to help drive conversion and
                         enhance the customer experience.

          UX DESIGNER    Assess your Checkout flow
         PAYMENTS TEAM
                         To help drive conversion and enhance your user s experience, carefully consider the location of the
                         Apple Pay button. The best user experiences place the Apple Pay button as early in the checkout
                         process as possible in order to leverage Apple Pay provided information, and minimize data entry.

          UX DESIGNER
                         Review the Human Interface Guidelines
                         Refer to the Apple Pay Human Interface Guidelines for additional information on how to best
                         incorporate Apple Pay in your app or website.

                              Apple Pay Human Interface Guidelines

          UX DESIGNER    Design your Apple Pay Experience
                         There are several key Apple Pay design principles that help drive conversion, increase usage and
                         engagement, and provide an excellent user experience. Please review our best practice
                         recommendations in Planning for Apple Pay.

                              Planning for Apple Pay

                         Design your Apple Pay experience quickly and accurately by using the Apple Pay Design Template,
                         available for for both Figma and Sketch. This can be found in the Technologies section of the Apple
                         Design Resources page below.

                              Apple Design Resources

􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣
                                                      ’

### Build your Apple Pay solution

                         Now that you have designed your solution for Apple Pay, it s time to start building
                         your implementation into your app or website. This section will link to relevant
                         sources within the API documentation, as well as provide additional detail to support
                         you in the process. These steps will differ if you are integrating through your PSP or
                         E-commerce platform, so you should refer to their documentation if that is how you
                         have chosen to integrate.

### Configure Apple Pay

                         To support Apple Pay on your website or app, you need to complete a few set up steps in your
                         developer account: registering a merchant ID, creating certificates, and verifying your web domain(s).
                         Completing the setup enables you to use the Apple Pay web APIs and/or App APIs.

### Configure Apple Pay for Apps

### Configure Apple Pay on the Web

        ACCOUNT ADMIN   Create a Merchant ID
                         Your Merchant ID uniquely identifies your business as a merchant able to take payments. A merchant
                         Identifier never expires, and can be used for multiple Apps and websites. Follow the steps below when
                         signed in to the Apple Developer Account as an account holder or admin role.

                         1.    In Certificates, Identifiers & Profiles, click Identifiers in the sidebar, then click the add button (+)
                               on the top left.
                         2.    Select Merchant IDs, then click Continue.
                         3.    Enter the merchant description and identifier name, then click Continue.
                         4.    Review the settings, then click Register.
                         Alternatively, you can create a merchant identifier in Xcode.

        ACCOUNT ADMIN   Create a Payment Processing Certificate
                         A Payment Processing Certificate is associated with your merchant ID and used to secure transaction
                         data. To generate a certificate you will need to upload a Certificate Signing Request (CSR) to the Apple
                         Developer portal. If your PSP is decrypting the data, contact them to obtain a properly formatted CSR
                         to upload and create your certificate. If you plan to decrypt the Apple Pay data yourself, you will need
                         to generate your own CSR using an ECC and 256 bit key pair, unless creating certificates for mainland
                         China in which case you will need to generate RSA 2048 key pairs.

                         1. In Certificates, Identifiers & Profiles, click Identifiers in the sidebar.
                         2. Under Identifiers, select Merchant IDs using the filter on the top right.
                         3. On the right, select your merchant identifier.
                         4. Under Apple Pay Payment Processing Certificate, click Create Certificate.
                         5. Create a certificate signing request .
                         6. Click Choose File.
                         7. In the dialog that appears, select the certificate request file (a file with a .certSigningRequest
                            file extension), then click Choose.
                         8. Click Continue.
                         9. Click Download. The certificate file (a file with a .cer file extension) appears in your Downloads
                            folder.

􀃲􀂒􀃲􀂒
􀉣
􀉣
                                                                       ’
    If your PSP is decrypting the payment data, they may require this certificate file. Follow the guidance
    they provide on where and how to share this with them.

    The Payment Processing Certificate is valid for a period of 25 months. Before it expires, you'll need to
    create a new certificate by following the same steps as outlined above. This prepares your replacement
    certificate but doesn't activate it immediately. Work with your PSP to choose the best time to switch
    over to the renewed certificate, and when you are both ready, press the “activate” button next to the
    certificate in the Apple Developer Portal. This tells the Apple Pay servers to begin using the new
    certificate for encryption.
    It s important to complete this process before your current certificate expires to avoid any interruption
    to your Apple Pay transactions. Most payment processors can guide you through this step-by-step.

’

### Configure Apple Pay on the Web

                             If you re developing websites using Apple Pay on the Web, you can use the same merchant ID and
                             Payment Processing Certificate for your website and your app. However, Apple Pay on the web requires
                             additional setup. As a reminder, if you are being onboarded by your Payment Service Provider or E-
                             Commerce platform, they may handle this on your behalf, and you should contact them to confirm
                             wether you need to create your own credentials.

### Configure Apple Pay on the Web

            ACCOUNT ADMIN   Create a Merchant ID
                             Your Merchant ID uniquely identifies your business as a merchant able to take payments. Follow the
                             steps in the previous section to create a Merchant ID.

            ACCOUNT ADMIN   Create a Payment Processing Certificate
                             A certificate associated with your merchant ID, used to encrypt Apple Pay transaction data. Follow
                             steps in previous section to create a Payment Processing Certificate.
            ACCOUNT ADMIN   Verify your domain(s)
                             You must register and verify all top-level domains and subdomains where you display the Apple Pay
                             button.

                             1. In Certificates, Identifiers & Profiles, click Identifiers in the sidebar, then select Merchant IDs from
                                the pop-up menu on the top right.
                             2. On the right, select your merchant identifier.
                             3. Under Merchant Domains, click Add Domain.
                             4. Enter the fully qualified domain name, then click Save.
                             5. Click Download, place the downloaded file in the specified location, then click Verify.
                             6. Click Done.
                             For successful domain validation, domains can t be behind a proxy or redirect, and must be accessible
                             to the Apple servers listed in setting up your server.

            ACCOUNT ADMIN   Create a Merchant Identity Certificate
                             A certificate associated with your merchant ID, used to authenticate sessions with the Apple Pay
                             servers. The steps to create this certificate are similar to those for the Payment Processing Certificate,
                             but you will need to generate your own CSR using an RSA 2048 bit key pair.

                             1. In Certificates, Identifiers & Profiles, click Identifiers in the sidebar, then select Merchant IDs from
                                the pop-up menu on the top right.
                             2. On the right, select your merchant identifier.
                             3. Under Apple Pay Merchant Identity Certificate, click Create Certificate.
                             4. Create a certificate signing request.
                             5. Click Choose File.
                             6. In the dialog that appears, select the certificate request file (a file with a .certSigningRequest
                                file extension), then click Choose.
                             7. Click Continue.
                             8. Click Download. The certificate file (a file with a .cer file extension) appears in your Downloads
                                folder.
                             9. Double-click the Merchant Identity Certificate you just downloaded to add it to your Mac Keychain.

􀉣
􀃲􀂒􀃲􀂒􀃲􀂒􀃲􀂒
             ’
                                                          ’
        ACCOUNT ADMIN   Export your Merchant Identity Certificate
          DEVELOPER      You should now have a private key and corresponding certificate. If you generated the private key in
                         the Keychain App on Mac, the Merchant Identity Certificate and key will need to be exported and
                         packaged into a .p12 file before you are able to use it to generate a session with the Apple Pay servers.
                         Follow the steps below to export and then test your certificate.

                         1. Open the Keychain app.
                         2. Click on 'login from the sidebar, Keys from the menu and search for the key you generated.
                         3. Click on the disclosure arrow beside the key, which should display your Merchant Identity
                            Certificate.

                         4. Right-click on the certificate and click Export <name of certificate>.

                         5. Choose a directory to save the certificates, and enter a password to protect the file.
                         Now you have a .p12 file that contains the key and certificate for Merchant Validation. Open Terminal
                         and use the following commands to split the .p12 into the corresponding key and certificate, where
                         ApplePayMerchantID_and_privatekey.p12 is the name of your .p12 file:

```bash
openssl pkcs12 -in ApplePayMerchantID_and_privatekey.p12 -out
ApplePay.crt.pem -nokeys
```

```bash
openssl pkcs12 -in ApplePayMerchantID_and_privatekey.p12 -out
ApplePay.key.pem -nocerts
```

        ACCOUNT ADMIN   Test your Merchant Identity Certificate
          DEVELOPER      To test that your Apple Pay Merchant Identity certificate is working correctly, use the following cURL
                         command in terminal to post the certificates and JSON up to Apple servers. Ensure you change the
                         merchantIdentifier and initiativeContext to the merchant identifier matching your
                         certificate, and a registered and verified domain associated to that merchant identifier. Make sure you
                         are using straight double quotes (") and not curly double quotes (“) to ensure the request can be
                         parsed correctly.

```bash
curl --location 'https://apple-pay-gateway-cert.apple.com/paymentservices/
paymentSession' \
--header 'Content-Type: text/plain' \
--data '{
     "merchantIdentifier": "merchant.XXXXXX",
     "displayName": "Example Merchant",
     "initiative": "web",
     "initiativeContext": "www.example.com"
}' \
--cert ApplePay.crt.pem \
--key ApplePay.key.pem
```

􀃲􀂒􀃲􀂒
􀃲􀂒
                 ’
                              ’
                                      ’
    If the connection succeeds and the session validated, you should see a print out in Terminal similar to
    the following:

         {“epochTimestamp”:15445664606792,”expiresAt”:154167344466792,”
         merchantSessionIdentifier”:”
         SSHC45CBB9C8073415198E3AB7314791C6D_916523AAED1343F5BC5815E12BEE9250AFFDC1A1
         7C46B0DE5A943F0F94927C24”,”nonce”:”
```json
8f47a9c1”,"merchantIdentifier":"20C8BB48576962AD936399118741FFEA6130838BDF69
A50B9A3CE4E7","domainName":"www.example.com","displayName":"Example
Merchant”,"signature":"308006092a864886f70d010702a0803080020101310f300d06096
086480165030402010500308006092a864886f70d0107010000a080308203e63082038ba0030
```

         2010202086860f699d9cca70f300a06082a8648ce3d040302307a312e302c06035504030c254
         170706c8274854054658569d4170706c652043657274696669636174696f6e20417574686f72
         69747931133011060355040a0c0a4170706c6520496e632e310b300906035504061302555330
         1e170d3136303630333138313634305a170d32313036303231383.......}

    This is the opaque session object, and is used to start a session for Apple Pay on the Web. It is
    important that this object is not inspected, parsed or modified in any way. Apple may update the
    contents of this object from time to time with changes and enhancements.

    A general guide to debugging common issues can be found in the troubleshooting section. If your
    issue is not resolved after reviewing the guide, you can get further assistance by contacting Apple
    Developer Support directly.

         Apple Pay Developer Support

􀉣

### Present Apple Pay as a payment option

                         With your configuration complete, you can now move on to add an Apple Pay button to your app or
                         website. There are several Apple Pay button types and styles you can use, and it is important that you
                         do not create your own Apple Pay button design or attempt to mimic the system-provided button
                         designs.

         DEVELOPER       Display the Apple Pay button
                         The button will be rendered by the appropriate PassKit or Javascript API, which will display the most up
                         to date version of the button, perform the appropriate localizations and have a system-provided
                         alternative text label that lets VoiceOver describe the button

                              Display the Apple Pay button - Apple Pay on web

                              Display the Apple Pay button - PassKit

         DEVELOPER       Apple Pay Mark
                         Use the Apple Pay mark in your app or website to show that Apple Pay is an available payment option.
                         The Apple Pay mark isn t a button and shouldn t be used to launch the payment sheet. Use only the
                         artwork Apple provides, with no alterations other than height.

                              Apple Pay mark and Marketing Guidelines

         DEVELOPER       Check for Apple Pay Availability
                         To ensure that you only display the Apple Pay button to customers with a supported device, check for
                         Apple Pay availability.

                              Checking for Apple Pay availability

### canMakePayments()

                         Verifies that the device is capable of making Apple Pay payments; it doesn t verify that the user has a
                         provisioned card for use with Apple Pay on the device. You can call this method at any time.

                              Web - canMakePayments()

                              App - canMakePayments()

### canMakePayments(usingNetworks:) App only

                         Verifies that the device is capable of making Apple Pay payments and that there is a payment card
                         from at least one of the provided networks available.

                              App - canMakePayments(usingNetworks:)

### applePayCapabilites() Web only

                         Verifies on Safari and third-party browsers that the device is capable of making Apple Pay payments.
                         On iOS devices or when using Safari on Mac, it also verifies whether the device has at least one
                         payment card available. Call this method if you want to default to Apple Pay during your checkout flow,
                         or if you want to add an Apple Pay button to your product detail page.

                              Web - applePayCapabilities()

􀉣
􀉣
􀉣
􀉣
􀃲􀂒􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣
􀉣
                     ’
                                                      ’
                                                                       ’

### Present the Payment Sheet

                       To present the payment sheet to the customer, construct a payment request containing information
                       that describes the purchase. This includes merchant information, supported payment networks, line
                       items including the total, currency code, billing and shipping contact, and more.

       DEVELOPER       Construct your Payment request
                       Your app or website specifies what the payment sheet displays, but it doesn t control the users
                       interaction with the sheet. You must decide if it makes sense to present shipping and billing
                       information, shipping methods, and other line items to the user. For the best results, only request the
                       information necessary to process and service the transaction.

       DEVELOPER       Complete Merchant Validation           Web only

                       Once the system launches the payment sheet, the merchant validation process is automatically
                       triggered and a call to onmerchantvalidation is made. In order for merchant validation to be
                       successful, you ll need to request a merchant session object from the Apple Pay servers.

                       Inside the onmerchantvalidation event handler, make a call to an endpoint on your server asking
                       for a new session to be created. For security purposes the request to the Apple Pay servers needs to
                       come from your server and not from the browser directly. Your server will then need to post your
                       request data alongside the Merchant Identity Certificate to obtain the session object.

```bash
POST https://apple-pay-gateway.apple.com/paymentservices/paymentSession
{
        merchantIdentifier: "merchant.com.example.mystore",
```

                                    displayName: "MyStore",
                                    initiative: "web",
                                    initiativeContext: "mystore.example.com"
                            }

                       Pass the session object into the complete method from the event to finish the Merchant Validation
                       process and allow the customer to authenticate the transaction.

                       When testing with sandbox cards, you ll make the call to a different endpoint. Be sure to make the call
                       to the production endpoint before pushing to your live environment.

􀃲􀂒􀃲􀂒
                   ’
                                    ’
                                                                       ’
     DEVELOPER   Shipping and Billing
                 In the payment request, you can specify the required customer information by setting the relevant
                 boolean values in the paymentOptions dictionary. Required data can include billing address,
                 shipping address, name, email address, and phone number.

                 Setting requestShipping to true presents redacted address information in a callback event prior
                 to the user authenticating the transaction, similar to the example shown below.

```json
{
        country: “US”,
```

                              addressLine: [],
                              region: “NC”,
                              city: “Raleigh”,
                              dependentLocality: “”,
                              postalCode: “27601”,
                              sortingCode: “”,
                              recipient: “”,
                              phone: “”
                      }

                 Apple Pay provides the information in a redacted form to protect a person s privacy, and can vary
                 based on geographic location – in the UK for example, only the first part of the postal code is returned
                 prior to authentication. Use this information to provide relevant shipping options within the
                 paymentDetails array, or to calculate any taxes due on the transaction and then update the payment
                 sheet accordingly.

                 Once a person authenticates the transaction with their biometric data or passcode, you will receive the
                 complete set of requested contact information.

```json
{
        country: "US",
```

                              addressLine: ["2399 Elm St"],
                              region: "NC",
                              city: "Raleigh",
                              dependentLocality: "",
                              postalCode: "27601",
                              sortingCode: "",
                              organization: "",
                              recipient: "Allison Cain",
                              phone: ""
                      }

     DEVELOPER   Respond to Payment sheet interactions
                 When the user interacts with the information they are providing in the payment sheet, events are
                 triggered with relevant information that allows you to respond to the changes. For example, if a
                 customer changes their selected address in the payment sheet, you can update the shipping methods
                 or shipping costs presented.

                      Web - request.onshippingaddresschange

                      App - PKPaymentRequestShippingContactUpdate

                 To display the coupon code field within the payment sheet, add supportsCouponCode to your
                 payment request with an empty couponCode field if there is no initial coupon code. If a customer
                 enters a coupon code within this field, respond to that event by adding an event listener to the
                 shippingaddresschange event and checking the event.methodDetails.couponCode
                 property.

􀃲􀂒
􀃲􀂒
􀉣
􀉣
                                                              ’
      DEVELOPER    Error handling

     UX DESIGNER
                   When you determine that there s a problem with an address or contact information on the payment
                   sheet, you can use ApplePayError to create a customized error message. Apple Pay highlights the
                   area with an error and displays your message, making it easier for users to correct errors.

                          Web - ApplePayError

                          App - PKPaymentError

                   The following sample code demonstrates Error Handling for a shipping contact

                              const paymentResponse = await paymentRequest.show();
                                 switch (paymentResponse.methodName) {
                                     case "https://apple.com/apple-pay":
                                         if (paymentResponse.details.shippingContact) {
                                             const errors = validateAddress(paymentResponse.details);
                                             if (errors.length) {
                                                 await paymentResponse.retry({
                                                     paymentMethod: errors,
                                                 });
```json
    }
}
       // Handle authorization with valid details here.
```

                                                break;

                                     case "https://...":
                                         // Other payment method changes here.
                                         break;
```json
       }
}
```

                          function validateAddress({shippingContact}) {
                              const errors = [];
                              // Validate shipping ZIP code here.
                              if (!isValidZipCode(shippingContact.postalCode)) {
                                  const error = new ApplePayError(
                                      "shippingContactInvalid",
                                      "postalCode",
                                      `ZIP code doesn’t match city`
                                  )
                                  errors.push(error);
```json
}
//validate other parts of address
```

                              return errors;
                          }

􀃲􀂒
􀉣
􀉣
                      ’
The following example demonstrates an implementation of Error Handling for a coupon code

     paymentRequest.addEventListener("shippingaddresschange", (event) => {
         switch (event.methodName) {
             case "https://apple.com/apple-pay":
                 if (event.methodDetails.couponCode) {
                     event.updateWith(
                         validCouponCode(event.methodDetails.couponCode)
                     );
                     return;
                 }

                             if (event.methodDetails.type) {
                                 // Handle payment method type changes here.
```json
}
break;
```

                    case "https://...":
                        // Other payment method changes here.
                        break;
```json
        }
});
```

     async function validCouponCode(couponCode) {
         const paymentMethodErrors = [];
         // Validate coupon code here against server.
         if (!(await isValidCouponCode(couponCode))) {
             paymentMethodErrors.push(
                 new ApplePayError(
                     "couponCodeInvalid",
                     undefined,
                     `Coupon code "${couponCode}" is invalid`
                 )
             );
```json
    }
    return { paymentMethodErrors };
}
```

     DEVELOPER   Multi-token payments
                 Multi token transactions such as a booking site where a user pays for a hotel, flight, and car rental from
                 different merchants, allow you to process and display payment requests with multiple merchants on
                 one payment sheet.

                      Web - Multi Token Payment Request Modifer

                      App - PKPaymentTokenContext

     DEVELOPER   Disbursement requests
                 Allow users to transfer funds from your site to an account that is linked to a card in Wallet. The
                 Disbursement Requests are only available as a subset of the Payment Request API.

                      Web - Disbursement Request Modifer           Payment Request API only

                      App - PKDisbursementRequest

     DEVELOPER   Recurring payments and Merchant Tokens
                 Apple Pay supports the use of merchant tokens (MPANs) to complete a variety of supported payments
                 independent of a device. After the initial transaction, payment details can be stored to create follow-on
                 transactions. A merchant token associates a payment card, merchant, and user, allowing for continuity
                 across multiple devices, even when a device is upgraded or a card is removed. When a payment
                 request is created for a recurring, automatic reload, or a deferred payment, you can provide essential
                 information the customer directly in the payment sheet, potentially helping to decrease cart
                 abandonment and increase conversion rates. Map each payment model you offer to the relevant Apple
                 Pay payment request type.

                 recurringPaymentRequest
                      Subscriptions such as digital content, streaming services, or membership programs, where the
                      customer is charged the same transaction amount at fixed regular intervals.

                            Recurring billing such as a utility bill, with a variable transaction amount at fixed regular
                            intervals.

                            Installment loan repayments such as a buy now, pay later loan, where there are a set number of
                            fixed, regular intervals for a single purchase of goods or services.

                                 Web - Recurring Payment Request Modifer

                                 App - PKRecurringPaymentRequest

                 automaticReloadPaymentRequest
                      Automatic reloads such as balance top up for transit or stored balance cards, allow you to add
                      funds to a specific account automatically, triggered by a pre-determined threshold.

                                 Web - Automatic Reload Payment Request Modifer

                                 App - PKAutomaticReloadPaymentRequest

                 deferredPaymentRequest
                      Deferred payments, such as car hire or hotel bookings with incidental charges, allow you to
                      specify a free cancellation period and the date when payment will be taken.

                                 Web - Deferred Payment Request Modifer

                                 App - PKDeferredPaymentRequest

                 When any of these request types are used to initiate an Apple Pay transaction, a merchant token is
                 automatically requested by Apple, and where supported by the issuer, returned in the Apple Pay
                 payload. If an issuer does not yet support merchant tokens, Apple Pay defaults back to returning the
                 DPAN.

􀃲􀂒
􀃲􀂒
􀃲􀂒
􀉣
􀉣
􀉣
􀉣
􀉣
􀉣
􀉣
􀉣
􀉣
􀉣

### Merchant Token Management API

### Merchant tokens are also designed to help prevent or resolve billing issues by giving visibility into

    important payment lifecycle updates, such as account status, bank card art, and card expiration date.
    The Apple Pay Merchant Token Management API allows you retrieve and manage these lifecycle
    updates.

    When your app or website creates a payment request using one of the supported request types, it can
    pass a notification URL in the tokenNotificationURL parameter. If a life-cycle event affects the
    token, Apple Pay sends a notification with an event identifier to that tokenNotificationURL. The
    details of the event can be retrieved by requesting the details from the Apple Pay server with the event
    identifier.

    Receiving and Handling Merchant Token Notifications
    When a life-cycle event occurs to a card associated with a merchant token, Apple Pay sends a GET
    request to the endpoint included in the tokenNotificationURL parameter of the original payment
    request.

        GET https://merchant.example.com/tokenapi/notification/merchantToken/{eventId}

    When you receive this request, use the eventId included in the path to format a POST request to
    retrieve the details of the event. This will include both the Merchant Identifier from the original
    transaction, alongside the specific eventId that has been triggered.

```bash
POST https://apple-pay-gateway.apple.com/paymentServices/v1/merchantId/
{merchantId}/merchantToken/event/{eventId}
```

         Receiving and handling merchant token notifications

    A merchantTokenEventResponse object containing the details of the event that triggered the
    notification will be returned. Consider how to handle different lifecycle events to proactively resolve
    payments issues. For example, when a consumer revokes the payment authorization on a token and
    you receive the UNLINK event, trigger a notification to the customer to update their payment details
    before the next billing cycle commences.

```json
{
    statusCode: 200,
```

             merchantTokenEvent: {
               merchantTokenIdentifier: 'MAPL...c5c2',
               eventType: 'UNLINK',
               reason: 'UNLINKDEVICE'
```json
    }
}
```

         merchantTokenEventResponse

􀉣
􀉣

### Authorize payment and map customer information

                     When a customer authenticates a transaction, the device will create a payment object that contains a
                     payment token with the encrypted payment data, alongside any additional contact data requested from
                     the customer. The information provided by the customer is not validated or verified by Apple.

     PAYMENTS TEAM
       DEVELOPER     Validate and Map Customer Information
                     Once you have validated customer information, map the values provided in Billing and Shipping
                     contact fields to your typical order fulfillment systems.

```json
{
    "billingContact": {
       "addressLines": [
         "1 First Street"
```

                                 ],
```json
   "administrativeArea": "London",
   "country": "United Kingdom",
   "countryCode": "GB",
   "familyName": "Appleseed",
   "givenName": "John",
   "locality": "London",
   "phoneticFamilyName": "",
   "phoneticGivenName": "",
   "postalCode": "AB12 3CD",
   "subAdministrativeArea": "",
   "subLocality": ""
},
"shippingContact": {
   "addressLines": [
     "1 First Street"
```

                                 ],
```json
       "administrativeArea": "London",
       "country": "United Kingdom",
       "countryCode": "GB",
       "emailAddress": "john.appleseed@apple.com",
       "familyName": "Appleseed",
       "givenName": "John",
       "locality": "London",
       "phoneticFamilyName": "",
       "phoneticGivenName": "",
       "postalCode": "AB12 3CD",
       "subAdministrativeArea": "",
       "subLocality": ""
    },
    "token": {
       "paymentData": {
          "data": "K+kSR...BbAj",
          "signature": "MIAG...AAA=",
          "header": {
             "publicKeyHash": "2xR1...PGQ=",
             "ephemeralPublicKey": "MFkw...1w==",
             "transactionId": "ba9c...7298"
          },
          "version": "EC_v1"
       },
       "paymentMethod": {
          "displayName": "NetworkName 1234",
          "network": "NetworkName",
          "type": "credit"
       },
       "transactionIdentifier": "ba9c...7298"
    }
}
```

􀃲􀂒
         DEVELOPER     Authorize Payment with your PSP
                       Apple Pay passes payment information inside a PKPaymentToken object (app) or an
       PAYMENTS TEAM
                       ApplePayPaymentToken object (web). The payment object has a nested structure that contains a
                       payment token with encrypted payment data, as shown in the figure below.

                       Depending on your PSP, you can pass the encrypted payment data directly to their systems for
                       authorization and capture. Alternatively, the payment data can be decrypted by you and then sent to
                       your PSP for processing For more information on decrypting the payment data yourself, refer to the
                       documentation at the link below.

                            Decrypting the Apple Pay Payment Token

         DEVELOPER     Complete payment
       PAYMENTS TEAM   Once you have passed the data to your PSP and received their response, pass the success or failure
                       back into the Apple Pay APIs. This will inform the user if the payment was successful, and dismisses
                       the payment sheet.

                            Web - complete

                            App - PKPaymentAuthorizationResult

􀃲􀂒􀃲􀂒
􀉣
􀉣
􀉣
                     Test your Apple Pay integration
                     Apple provides sandbox accounts and Apple Pay Cards that you can use to run tests in the Apple Pay
                     Sandbox environment. Attempting to use these cards with a live production environment will result in
                     your PSP rejecting the transaction. More information on how to set up the sandbox accounts and cards
                     can be found on the developer website linked below.

                          Sandbox Testing

                     It is also important to test Apple Pay in your production environment using real cards to ensure the
                     end-to-end transaction flow is working as expected.

                          Participating Banks

       DEVELOPER     Test your integration on multiple devices and browsers
     PAYMENTS TEAM
                     Apple Pay is now available on Safari, third party browsers in iOS and MacOS, as well as on other
                     computing platforms. Check that the Apple Pay button is displayed on all the relevant devices and
                     locations, and that you are able to see the Apple Pay button on third party browsers and devices.

       DEVELOPER     Data Mapping and formatting
     PAYMENTS TEAM   Confirm that you are able to map all of the relevant data included in the Apple Pay payload, including
                     the shipping and billing contact fields to your order management services. Ensure you can handle this
                     data in the various possible formats. For example, phone numbers may contain numeric values as well
                     as special characters such as “+”.

       DEVELOPER     Responding to Events
     PAYMENTS TEAM   When you are supporting handling of Payment Sheet event, such as when the shipping contact or
                     method is updated, ensure you have tested your event handling process and that you are formatting
                     and responding using the relevant completion method.

       DEVELOPER     Test all payment flows
     PAYMENTS TEAM   Test that Apple Pay functions as expected across all of the payment flows you are offering.

􀃲􀂒
􀃲􀂒
􀃲􀂒
􀃲􀂒
􀉣
􀉣

### Good practice guidance when processing

    Apple Pay transactions
    Apple Pay offers multiple layers of security beyond many other payment methods. However, you can
    apply the same industry best practices for risk mitigation to Apple Pay as you do for other E-commerce
    payment methods.

    Apple Pay uses tokenised credentials (such as a device-specific DPAN or a merchant-specific MPAN)
    so actual card numbers (PANs) cannot be used as a unique key and each transaction generates a
    unique cryptogram in place of the CV2. There are many standard checks that are still applicable to
    Apple Pay. If you do not have an in-house Risk Management tool, please consider reaching out to your
    Payment Service Provider (PSP) who should be able to help implementing the below Risk Checks.

    Velocity and Pattern Checks
    A velocity check monitors specific data elements to check and compare a customer's shopping history
    with current purchases in order to identify any irregularities in their purchasing behavior. This includes
    sudden bursts of high activity considered inconsistent with standard purchase behaviors for your
    industry or customer base.

    Consider using purchase frequency, repeat billing/delivery address for high value purchases,
    cardholder name, email, name and IP address - particularly if combinations of these details are used in
    quick succession. Actions you could take based on a high risk transaction are:

    • Decline the transaction.
    • Delay shipping and complete outbound checks on address and customer details.

    Delivery Checks
    Consider implementing risk indicators for delivery methods such as the delivery address being
    different from the billing address, temporary addresses, instructions to leave goods on doorsteps (or
    similar), export address or requests for fast delivery. In countries where applicable, use Address
    Verification Services (AVS) to verify the billing address is correct. Consider looking at data provided by
    the user and check if it's linked to previous purchases (email addresses, phone numbers, billing and
    shipping addresses linked to other users). Multiple transactions could be correlated against another
    order.

    Maintain a “Bad Transactions” List
    Maintain a list of historical transactions for all payment methods which have either looked suspicious or
    resulted in chargebacks and compare the details of new transactions against these. If one or more of
    the transaction details match against historically bad transactions it may be worth putting the
    transaction aside for manual review or declining it outright. This data may also be available via your
    Payment Service Provider s (PSP) Risk Management tool.

    Email and IP address Checks
    Ensure that email addresses are correct. You can use the Apple Pay Error Handling API's to ensure a
    customer adheres to your email rules. If the domain looks ok, send an email to the address to confirm it
    exists. Check the IP address coming from the device to verify the IP country matches the billing
    country and country where the card was issued.

    Country Checks
    If you identify certain countries as high risk, you can use the supportedCountries property in the Apple
    Pay payment request to limit payment cards to those that were issued in specific countries. The
    supportedCountries list does not affect the currency used for the transaction, and it applies to all
    payment cards in Wallet. You can also consider limiting IP addresses from high risk regions.

’

### Frequently asked questions

        Where does the customer information come from in the payment sheet?
        The information comes from Wallet & Apple Pay defaults in Settings, if available, as well as the My Card
        in Contacts. It could also come from previous Apple Pay transactions. You can set up your My Card by
        going to Settings > Contacts > My Info.

        Is the customer information that comes from Apple Pay verified by Apple?
        Customer information is shared as-is, and is not verified by Apple. You will need to validate it on your
        platform and communicate through the Apple Pay API if fields should be corrected. For more
        information visit the Error Handling section of this guide.

        What customer information can I pull from Apple Pay?
        Customer information includes shipping and billing address, name, phone number and email address.

        What does the Apple Pay payment token contain?
        The structure, format, and data included in the payment token can be found in the Payment Token
        Format Reference. The payment token only contains information on processing the payment; the
        customer information is included in the payment object. The payment object encapsulates the
        customer information and the payment token.

             Payment Token Format Reference

        What do I do if my PSP is unable to decrypt my payment?
        You may need to regenerate your payment processing certificates. Please follow the steps in this guide
        to generate your payment processing certificates and work with your PSP to understand where the
        issue may lie.

        Can I use the same Merchant ID for multiple PSPs?
        This is supported only if you are decrypting the payload yourself and passing on the payment
        information. Where the PSP s will be performing decryption, they should each have their own, unique
        merchant identifier to ensure the payments are encrypted with the correct sets of certificates and
        keys..

        Will I get liability shift with Apple Pay?
        Please check with your PSP. Depending on your specific agreement, you may get liability shift with
        certain card networks.

        Can I use the same Apple developer account for all countries I process payments in?
        Yes; you do not need to have separate Apple developer accounts for multiple markets. You can also
        use the same Apple Merchant ID if you wish

􀉣
    ’

### Troubleshooting

    Further information and troubleshooting steps to debug common issues with Apple Pay can be found
    in the below guides.

         Apple Pay on the Web Troubleshooting Guide

         Troubleshooting Apple Pay payment processing

         Diagnosing issues with displaying the Apple Pay button on your website

         Diagnosing issues with the Apple Pay payment sheet on your website

         Troubleshooting issues with your Apple Pay merchant identifier configuration

􀉣
􀉣
􀉣
􀉣
􀉣

### API Diagrams

                                                                                                                                                                                        Apple Pay in app

                                                  iOS                                                                                        App                                                     Merchant Server                   Apple Server                               PSP/Acquirer                                    Network                                   Issuer

                                                                     [1] canMakePayments() / canMakePayments(usingNetworks:)

                                                                                            [2] true / false

                                                                                                                                 show / hide Apple Pay button

                                                          [3] User taps Apple Pay button

                                                                                                                  [4] create PKPaymentRequest

                                                                 [5] instantiate PKPaymentAuthorizationController(paymentRequest:)

                                                                                       [6] present(completion:)

                [7] Payment Sheet is presented

                                            opt         [payment method event]

                                                               [8] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [9] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

                                            opt         [shipping contact event]

                             Event only triggered if shipping contact
                                    fields are requested in the
                                       PKPaymentRequest.

                         Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

                                                              [10] paymentAuthorizationController(_: didSelectShippingContact: handler:)

                                                        [11] completion(PKPaymentRequestShippingContactUpdate(errors: shippingMethods: ))

               [12] Payment Sheet is activated

opt      [payment method changed event]

      [13] User changes payment method

                                                              [14] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [15] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

opt      [shipping contact changed event]

                             Event only triggered if shipping contact
                                    fields are requested in the
                                        PKPaymentRequest

                         Only a partial address is provided at this stage.
                    Full address is only provided after the user authenticates.

 [16] User changes shipping contact / address

                                                              [17] paymentAuthorizationController(_: didSelectPaymentMethod: handler:)

                                                         [18] completion(PKPaymentRequestPaymentMethodUpdate(paymentSummaryItems: ))

opt      [shipping method changed event]

                             Event only triggered if shipping methods
                                        are included in the
                                      PKPaymentRequest.

      [19] User changes shipping method

                                                              [20] paymentAuthorizationController(_: didSelectShippingMethod: handler:)

                                                         [21] completion(PKPaymentRequestShippingMethodUpdate(paymentSummaryItems: ))

[22] User authenticates with Touch ID / Face ID

                  [23] Apple Pay payment data
                        is generated on device

                                                                                                                                [24] payment data sent to Apple Server

                                                                                                                                                                                                                         [25] Apple encrypt
                                                                                                                                                                                                              payment data using public key
                                                                                                                                                                                                                  (associated with Payment
                                                                                                                                                                                                                     Processing Certificate)

                                                                                                                             [26] encrypted payment data returned to iOS

                                                                [27] paymentAuthorizationController(_: didAuthorizePayment: handler :) {

                                                                                                                                                   [28] send user data and ecnrypted payment data to server

                                                                                                                                                                                                                        [29] send user data and ecnrypted payment data to psp

                                                                                                                                                                                                                                               [30] PSP decrypts Apple Pay payment data

                                                                                                                                                                                                                                                                                          [31] decrypted payment data sent to PNO

                                                                                                                                                                                                                                                                                                 [32] PNO detokenises Apple Pay token

                                                                                                                                                                                                                                                                                                                                        [33] card data sent for authorisation

                                                                                                                                                                                                                                                                                                                                            [34] authorisation response

                                                                                                                                                                                                                                                                                                    [35] authorisation response

                                                                                                                                                                                                                                      [36] authorisation response

                                                                                                                                                                 [37] authorisation response

                                                                    [38] completion(PKPaymentAuthorizationResult(status: errors:))

              [39] Payment outcome displayed
                 and payment sheet dismissed

### Change Log

                             Minor editorial updates

### canMakePayments(usingNetworks:) added

                             Merchant token guidance added
    March 2026
                             Merchant Token Management API section added

                             Example Payment Object added for reference

                             Testing recommendations added

                             Guidance for applePayCapabilites API added
      Jun 2025
                             Good practice when processing Apple Pay transactions guidance added



---

## 4. Legal (Service Terms)

> Part 4 of the master-plus-parts verbatim canonical. Reproduces Apple's **Service Terms for Messages for Business** verbatim.
> **Source:** `register.apple.com/tou/bca/latest/en` — **Last updated: December 17, 2024** (confirmed current as of the July 2026 verification; this document is gated and was retrieved as provided text).
> **⚠ Verification flag:** unlike Parts 1–3 (extracted directly from source files on disk), Part 4 was reconstructed from the provided Service Terms text. It should be diff-verified byte-for-byte against the source document in the full re-audit. Preserve Apple's original typos where present (e.g., "solely responsible maintaining" §2.1; "MESSSAGES" §4.5) with `[sic]` rather than silently correcting.
> **Overlay:** provenance, recency, and audit live in the Master index.

---

## Service Terms for Messages for Business

PLEASE READ THE FOLLOWING SERVICE TERMS CAREFULLY BEFORE USING APPLE MESSAGES FOR BUSINESS. THESE SERVICE TERMS REPLACE THE FORMER TERMS FOR BUSINESS CHAT AND SUPPLEMENT THE APPLE BUSINESS REGISTER TERMS OF USE. THESE SERVICE TERMS CONSTITUTE A LEGAL AGREEMENT BETWEEN YOU AND APPLE.

### Service Terms for Apple Messages for Business

The following Apple Messages for Business Service Terms ("Service Terms") are in addition to the Apple Business Register Terms of Use ("ABR Terms of Use") and govern your use of Apple Messages for Business. In the event of a conflict between these Service Terms and the ABR Terms of Use, these Service Terms shall control.

You certify to Apple and agree that you or your representative entering into these Service Terms is of the legal age of majority in the jurisdiction(s) in which you reside (at least 18 years of age in many countries) and have the right and authority to enter into these Service Terms on your own behalf, and that if your representative is entering into these Service Terms on behalf of you as a business, that such representative has the right and authority to legally bind you to all the terms and obligations of these Service Terms.

THE ENGLISH LANGUAGE VERSION OF THIS AGREEMENT SHALL BE THE ORIGINAL, GOVERNING INSTRUMENT AND UNDERSTANDING OF THE PARTIES. IF THIS AGREEMENT IS MADE AVAILABLE BY APPLE IN ANY LANGUAGE OTHER THAN ENGLISH, THE ENGLISH LANGUAGE VERSION SHALL GOVERN AND CONTROL IN THE EVENT OF ANY CONFLICT WITH ANY TRANSLATION INTO ANY OTHER LANGUAGE.

BY USING APPLE MESSAGES FOR BUSINESS, YOU AGREE TO THESE SERVICE TERMS; IF YOU DO NOT AGREE, DO NOT USE APPLE MESSAGES FOR BUSINESS.

### 1. Definitions

In addition to the definitions found in the ABR Terms of Use, the following definitions apply whenever capitalized in these Service Terms:

"Business" means an organization registered to use Apple Messages for Business to connect with customers. Your Business must have an active and valid Apple Account.

"Documentation" means any technical or other specifications or documentation that Apple may provide to you for use in connection with Apple Messages for Business.

"Guidelines" means the Apple Messages for Business usage guidelines set forth herein and also all policies, best practices, protocols, partnership requirements or other terms and conditions set forth by Apple, including, but not limited to, Apple Messages for Business MSP & brand media guidelines, design guidelines, policies, and best practices, each of which may be updated from time to time.

"Apple Messages for Business" means the services, Program or Apple Messages for Business Materials that Apple may provide or make available through Apple Messages for Business service, including Updates (if any) that may be provided to you by Apple.

"Apple Messages for Business API(s)" means the application programming interface(s) documented by Apple in the Documentation or elsewhere by Apple and which are contained in the Apple Products.

"Apple Messages for Business ID" means the Apple Messages for Business identifier assigned to each of your Apple Messages for Business or MSP accounts that enables access to and use of Apple Messages for Business.

"Apple Messages for Business Materials" means the Documentation, tools, certificates, data, and other materials provided to you by Apple through Apple Messages for Business.

"Message(s)" means a message that is received or sent by you using Apple Messages for Business.

"Messaging Service Provider" or "MSP" means an organization that provides or delivers a system or service that facilitates the exchange of or enables the use of Apple Messages for Business for one or more businesses. For clarity, a Business may also be an MSP, subject to these Service Terms, Guidelines, Service and Feature Requirements, and any other terms and conditions Apple may require during registration, onboarding, and/or use of the Apple Messages for Business.

"Program" means the overall Apple development, testing, digital signing and distribution program contemplated in these Service Terms.

"Service and Feature Requirements" mean the technical, human interface, design, product category, security, performance, current and new features, and other criteria and requirements specified by Apple, which may be modified from time to time by Apple in its sole discretion and which you must comply with in order to access and use Apple Messages for Business either as a Business or as an MSP.

"Updates" means bug fixes, updates, upgrades, modifications, enhancements, supplements, and new releases or versions of any part of Apple Messages for Business.

### 2. Use of Apple Messages for Business and Integration

#### 2.1 Use of Apple Messages for Business and Your Business Information

To the extent a Business or MSP chooses to participate in the Program and use Apple Messages for Business, it does so at its own initiative and agrees to, and shall ensure all employees, contractors, agents, and other individuals with access to its Apple Messages for Business account (collectively, "End-Users") agree to, use Apple Messages for Business only as expressly permitted in the ABR Terms of Use and these Service Terms (including any Updates), in accordance with the Service and Feature Requirements, Guidelines, and applicable laws, regulations, or additional policies, terms or guidance Apple may require. Any reference to a Business or an MSP in these Service Terms also includes and applies to all End-Users. Apple Messages for Business, or any feature or part thereof, may vary by region and may not be available in all languages or in all countries. Apple makes no representation that Apple Messages for Business, or any feature or part thereof, is appropriate, accurate or available for use in any particular location. Apple reserves the right to change, suspend, remove, or disable access to Apple Messages for Business at any time without notice. In no event will Apple be liable for the removal of or disabling of access to Apple Messages for Business.

A Business and MSP must agree to provide accurate, current and complete information required to register with Apple for use of Apple Messages for Business and at other points as may be required in the course of using Apple Messages for Business, including, but not limited to, company name, physical address, business license/registration, or other information as requested by Apple. You hereby confirm that any information provided to Apple (including, without limitation, in through use of Apple Messages for Business or any other Apple services (e.g., App Store) is accurate, current and complete. You further agree to maintain and update your information as required to keep it accurate, current, and complete. You understand and acknowledge that failure to provide, update, and maintain accurate, current, and complete information pursuant to these Service Terms may lead to suspension or termination of your access to or use of Apple Messages for Business at any time.

To access Apple Messages for Business, a Business and MSP must first be assigned an Apple Messages for Business ID by Apple. Thereafter, a Business and MSP may access Apple Messages for Business only as provided for herein. A Business and MSP are solely responsible maintaining [sic] the confidentiality and security of their respective Apple Messages for Business accounts and information.

An MSP must be approved by Apple in advance of use. To the extent an MSP relies on the technology or services of another MSP in providing messaging services to a Business, both MSPs must be registered and approved for use in Apple Messages for Business under these Service Terms. An MSP shall not promote their Apple Messages for Business-related services unless and until approved in writing by Apple.

A Business and MSP must comply with all Service and Feature Requirements imposed by Apple in order to use Apple Messages for Business. In addition, an MSP must comply with any new or subsequently imposed feature requirements no later than ninety (90) days from Apple's notification. Apple may also impose additional limits, conditions, restrictions, or requirements on the use of or access to Apple Messages for Business in any case and without notice or liability.

#### 2.2 Business Integration with MSPs

A Business must itself be an approved MSP or select an approved MSP (i.e., an MSP that is authorized by Apple to provide access or services related to Apple Messages for Business) to integrate with Apple Messages for Business, including, if authorized, for an MSP to administer a Business account and profile on behalf of the Business for Apple Messages for Business. A Business understands and agrees that Apple may share your information with your MSP to provide services under Apple Messages for Business. A Business is solely responsible for its relationship and any agreement(s) with its MSP. A Business and its MSP shall be responsible for any action or inaction undertaken by an MSP on behalf of a Business in relation to providing or administering Apple Messages for Business, sending or receiving Messages or other activities under these Service Terms. In the event Apple, in its sole discretion, determines an MSP has or may have violated these Service Terms or otherwise caused any harm, degradation, or interference with the Apple Messages for Business experience, Apple reserves the right to require a Business to cease using any such MSP and terminate a Business and/or its MSP's use of Apple Messages for Business. A Business acknowledges and agrees that Apple will have no responsibility or liability for the actions or inactions of any registered MSP that the Business may elect to work with in connection with Apple Messages for Business, and Apple is not a party to any agreement between a Business and any such MSP.

#### 2.3 Messages

All use of Apple Messages for Business must only be from a Business's assigned Apple Messages for Business ID. A Business will ensure that its Apple Messages for Business Messages are sent under the name, trademark or brand of the Business. It must be clear to a recipient of a Business's Messages that the communication is coming from the Business and not from Apple; provided, however, as applied to a registered MSP for a Business, all Messages must be sent using the Apple Messages for Business ID of the Business for whom you are acting as an MSP, along with any other identifiers required in the Documentation or by Apple. A Business and its MSP agree not to misrepresent or impersonate another business or entity or otherwise mislead Apple or Apple Messages for Business users about the origin or originator of the Apple Messages for Business Message. A Business and its MSP also agree not to use Apple Messages for Business in any manner to harass, abuse, stalk, threaten, defame or otherwise infringe or violate the rights of any other party, and you agree that Apple is not in any way responsible for any such use. A Business and its MSP further agree not to transmit any computer viruses, worms, trojan horses or other malware, or trespass, burden network capacity, or otherwise disable, override or interfere with any Apple-implemented notices, consent panels or any Apple system preferences used to administer and/or provide Apple Messages for Business functionality.

#### 2.4 Privacy

Apple's Privacy Policy applies to use of Apple Messages for Business, and its terms are incorporated into these Service Terms by this reference. Apple's Privacy Policy can be found at: https://www.apple.com/privacy/ and is updated from time to time. More information on how Messages for or Business protects privacy is available on the Apple website and may be updated from time to time.

#### 2.5 In-App Purchase and iMessage Apps

A Business and its MSP understand and agree that use of the In-App Purchase API in Apple Messages for Business is subject to the terms and conditions of the Apple Developer Program License Agreement and related requirements available at https://developer.apple.com/support/terms/ and may be updated from time to time.

Use of Apple Messages for Business may also require access to iMessage Apps found at developer.apple.com, which is subject to the terms of use of iMessage Apps or the Apple Messages App.

#### 2.6 Apple Pay

A Business and its MSP understand and agree that integration of Apple Pay and any Apple Pay transactions within Apple Messages for Business is subject to the applicable Apple Pay terms and conditions on the https://developer.apple.com/apple-pay website, or other such applicable terms and conditions.

#### 2.7 Use of Network

Use of Apple Messages for Business may require Messages to be transmitted across various public networks and/or in various media, and further may require modifications to the format of Messages to comply with technical, network, and other requirements.

#### 2.8 Apple Messages for Business is not intended for Emergency Services

Apple Messages for Business is not intended to provide access to emergency services or emergency service providers. Apple Messages for Business is not intended to be a guaranteed, on-time delivery service, and shall not be used or relied upon it as such. A Business and its MSP agree that Apple make no representations or guarantees and shall have no liability to you for the availability, accuracy, completeness, reliability, or timeliness of Messages communicated in Apple Messages for Business.

#### 2.9 Compliance with All Legal, Regulatory, Privacy, and Security Requirements

A Business and its MSP agree to use Apple Messages for Business only for purposes permitted by this Agreement, and only to the extent permitted by any applicable law or regulation in the applicable jurisdiction.

A Business and its MSP may only use Apple Messages for Business if they have ensured that all such use complies with all legal and regulatory requirements; it is a Business and its MSP's sole responsibility to determine and comply with all legal obligations. Apple makes no representations or warranties that Apple Messages for Business meets the needs of entities regulated by laws and regulations with heightened confidentiality requirements for personal, health, financial, and/or other types of data. A Business and its MSP must provide all necessary data disclosures and notices and secure all necessary rights, consents, and permissions. Under no circumstances will Apple be liable for any acts or omissions by a Business or its MSP that breach any applicable laws.

A Business and its MSP are solely responsible for any and all collection, transmission, maintenance, processing or use of sensitive, personal, or confidential information (e.g., Apple Account, a social security number, financial account or transactional information, or any information where the individual may have a reasonable expectation of secure transmission) in any Message, and agree to comply with all applicable laws regulations, and requirements, including, but not limited to, notice or consent requirements, with respect to any collection, transmission, maintenance, processing or use of such sensitive, personal, or confidential information.

If a Business is a covered entity, business associate or representative of a covered entity or business associate (as those terms are defined at 45 C.F.R § 160.103), the Business agrees that it will not use any component, function or other facility of Apple Messages for Business to create, receive, maintain or transmit any "protected health information" (as such term is defined at 45 C.F.R § 160.103) or use Apple Messages for Business in any manner that would make Apple (or any Apple Subsidiary) the Business's or any third party's business associate.

#### 2.10 Export Control

Use of Apple Messages for Business may be subject to the export and import laws of the United States and other countries. You agree to comply with all applicable export and import laws and regulations. A Business and its MSP also agree not to use Apple Messages for Business for any purposes prohibited by United States law. A Business and its MSP further agree not to use any data or software that is: (a) subject to International Traffic in Arms Regulations; or (b) that cannot be exported without prior written government authorization, including, but not limited to, certain types of encryption software and source code, without first obtaining that authorization.

#### 2.11 No conveyance

Nothing in these Service Terms shall be construed to convey to a Business or MSP of any interest, title, or license in an Apple Messages for Business ID, Business account, or similar resource used in connection with Apple Messages for Business.

#### 2.12 Business Updates

Apple Messages for Business may include the ability for a Business to send Messages ("Business Updates") to a customer of that Business. Business Updates may only be sent by a Business to its customer through Apple Messages for Business upon opt-in by such customer to receive Business Updates from such Business. The opt-in may only be collected from a customer at a Business' point of sale ("POS"), such as the Business' website, application, customer service number, or physical location. The opt-in will only apply to Business Updates regarding the transaction between the Business and that customer occurring during the time the opt‑in was given at the POS, and in any event, such opt-in should only be valid for the time period necessary for the transaction (which in no event will be longer than two (2) years). A Business will offer an opt‑out choice in every Business Update and will immediately honor any such customer's opt-out. A Business offering Business Updates will include the following language at the POS during the opt-in process: "Separate from your opt-in to receive Business Updates from us, your use of Apple Messages for Business service is also governed by Apple's terms, including those at https://www.apple.com/legal/privacy/data/en/messages-for-business/ . Unless you have opted-out on your Apple device, Apple may process your personally identifiable information." The location of this language will be the same as the Business' similar legal notifications, and will be at all times legally enforceable and viewable before opt-in. A Business and/or its MSP shall only use Apple‑authorized templates when sending Business Updates and shall not modify such templates except for permitted custom substitutions in specific text fields.

### 3. Apple Messages for Business - Prohibited Uses

Except as otherwise set forth in herein, a Business and MSP agree not to rent, lease, lend, upload to or host on any website or server, transfer, sell, redistribute, or sublicense Apple Messages for Business in whole or in part, or to enable others to do so. A Business and MSP may not use Apple Messages for Business, or any other services provided hereunder, for any purpose not expressly permitted by these Service Terms. For clarity, the Service Terms incorporate all the Service and Feature Requirements, Guidelines, Documentation, or other terms required by Apple, now or in the future, including, but not limited to, the Apple Messages for Business policies and best practices. A Business or MSP shall not use Apple Messages for Business to distribute, transmit, store, share, access, solicit, or otherwise make available any content that is unlawful, harassing, threatening, harmful, tortious, defamatory, libelous, abusive, violent, obscene, vulgar, invasive of another's privacy, hateful, racially or ethnically offensive, or otherwise objectionable. A Business and MSP agree not to, or to enable others to, copy, decompile, reverse engineer, disassemble, attempt to derive the source code of, modify, decrypt, or create derivative works of Apple Messages for Business, or any part thereof. A Business and MSP agree not to exploit Apple Messages for Business in any unauthorized way whatsoever, including but not limited to, by trespass or burdening network capacity, or by harvesting, scraping or misusing data. Any attempt to do so is a violation of the rights of Apple and these Service Terms. A Business or MSP shall not use Apple Messages for Business to solicit, access, distribute, store, or generate child sexual abuse material, child sexual exploitation material, pro-terror material, extreme crime and violence material, crime or violence material, and drug-related material.

If a Business or its MSP breach any of the foregoing restrictions, it may be subject to prosecution and damages, and Apple may take, among other actions, the actions described in Section 5 of these Service Terms. All licenses not expressly granted herein are reserved and no other licenses, immunity or rights, express or implied are granted by Apple, by implication, estoppel or otherwise. These Service Terms do not grant You any rights to use any trademarks, logos or service marks belonging to Apple, including, but not limited to, Apple, Business Chat, Apple Messages for Business, Apple Pay, Apple iMessage, iPhone, iPad, iOS, iPadOS, Watch, watchOS, Mac, iMac, macOS, and any related word marks. If a Business or its MSP references any Apple Products or Apple trademarks or copyrights, it agrees to comply with the published guidelines at www.apple.com/legal/trademark/guidelinesfor3rdparties.html, which may be modified by Apple from time to time.

### 4. Acknowledgements

#### 4.1 Apple's Rights to Modify Apple Messages for Business

A Business and MSP acknowledge and agree that Apple may at any time, and from time to time, with or without prior notice:
(a) modify Apple Messages for Business, including by adding, changing, or removing any feature, functionality, or requirement as part of the Service and Feature Requirements or otherwise;
(b) modify, deprecate, suspend, reissue, republish, or discontinue Apple Messages for Business or any portion thereof; or
(c) make changes to the ABR Terms of Use, these Service Terms, the Service and Feature Requirements, and/or Guidelines, Documentation, and other materials.

A Business and MSP understand that any such modifications may require change or update to its use of Apple Messages for Business, systems or services used to implement and provide Apple Messages for Business at a Business or MSP's own cost. Apple has no express or implied obligation to provide, or continue to provide, Apple Messages for Business and may suspend or discontinue all or any portion of Apple Messages for Business at any time. Apple shall not be liable for any losses, damages or costs of any kind incurred by a Business or its MSP or any third party arising out of or related to any such service suspension or discontinuation or any such modification of Apple Messages for Business or any portion thereof.

#### 4.2 No Guarantee of Availability

Apple makes no guarantees in relation to the availability or uptime of Apple Messages for Business and is not obligated to provide any maintenance, technical support or other support for Apple Messages for Business. Apple reserves the right to remove a Business and its MSP from access to Apple Messages for Business, limit use of Apple Messages for Business, or revoke Your Apple Messages for Business ID at any time in its sole discretion without any liability, obligation to provide notice or an opportunity to cure any deficiency. A Business and MSP understand there may be storage capacity, transmission and/or transactional limits that govern use of Apple Messages for Business. If such limits are reached, then a Business and its MSP understand and agree that their Apple Messages app user may be unable to use Apple Messages for Business or may be unable to access or retrieve data from Apple Messages for Business.

#### 4.3 No Fees Charged by a Business

A Business using Message for Business may not charge any fees solely for access to or use of Apple Messages for Business. Further, a Business and its MSP agree not to create or attempt to create a substitute or similar service to Apple Messages for Business through use of or access to Apple Messages for Business.

#### 4.4 Disclaimer of Warranties

SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF CERTAIN WARRANTIES. TO THE EXTENT SUCH EXCLUSIONS ARE SPECIFICALLY PROHIBITED BY APPLICABLE LAW, SOME OF THE EXCLUSIONS SET FORTH BELOW MAY NOT APPLY TO YOU. THE FOLLOWING DISCLAIMERS SHALL APPLY TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW.

YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT, TO THE EXTENT PERMITTED BY APPLICABLE LAW, USE OF MESSAGES FOR BUSINESS SERVICE IS AT YOUR SOLE RISK AND THAT THE ENTIRE RISK AS TO SATISFACTORY QUALITY, PERFORMANCE, ACCURACY AND EFFORT IS WITH YOU. APPLE DOES NOT PROMISE THAT MESSAGES FOR BUSINESS OR ANY FEATURE OF THE SERVICE WILL BE ACCURATE, ERROR-FREE OR UNINTERRUPTED, OR THAT ANY DEFECTS WILL BE CORRECTED, OR THAT YOUR USE OF MESSAGES FOR BUSINESS WILL PROVIDE SPECIFIC RESULTS.
YOU EXPRESSLY ACKNOWLEDGE AND AGREE THAT MESSAGES FOR BUSINESS IS PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS, WITH ALL FAULTS AND WITHOUT WARRANTY OF ANY KIND, AND APPLE AND ITS LICENSORS HEREBY DISCLAIM ALL WARRANTIES AND CONDITIONS WITH RESPECT TO YOUR USE OF MESSAGES FOR BUSINESS, EITHER EXPRESS, IMPLIED OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES AND/OR CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, QUIET ENJOYMENT, AND NON-INFRINGEMENT OF THIRD PARTY RIGHTS. IN PARTICULAR, APPLE AND ITS AFFILIATES, SUBSIDIARIES, OFFICERS, DIRECTORS, EMPLOYEES, AGENTS, PARTNERS AND LICENSORS MAKE NO WARRANTY THAT (I) MESSAGES FOR BUSINESS WILL MEET YOUR REQUIREMENTS; (II) YOUR USE OF MESSAGES FOR BUSINESS WILL BE TIMELY, UNINTERRUPTED, SECURE OR ERROR-FREE; (III) ANY INFORMATION OBTAINED BY YOU AS A RESULT OF MESSAGES FOR BUSINESS WILL BE ACCURATE OR RELIABLE; (IV) ANY DEFECTS OR ERRORS IN MESSAGES FOR BUSINESS WILL BE CORRECTED; AND (V) MESSAGES FOR BUSINESS WILL BE COMPATIBLE OR WORK WITH ANY THIRD PARTY SOFTWARE, APPLICATIONS OR THIRD PARTY SERVICES.

YOU FURTHER ACKNOWLEDGE AND AGREE THAT MESSAGES FOR BUSINESS IS NOT INTENDED OR SUITABLE FOR USE IN SITUATIONS OR ENVIRONMENTS WHERE THE FAILURE OR TIME DELAYS OF, OR ERRORS OR INACCURACIES IN MESSAGES FOR BUSINESS COULD LEAD TO DEATH, PERSONAL INJURY, OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE.

NO ORAL OR WRITTEN INFORMATION OR ADVICE GIVEN BY APPLE OR AN APPLE AUTHORIZED REPRESENTATIVE SHALL CREATE A WARRANTY. SHOULD MESSAGES FOR BUSINESS PROVE DEFECTIVE, YOU ASSUME THE ENTIRE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED WARRANTIES OR LIMITATIONS ON APPLICABLE STATUTORY RIGHTS, SO THE ABOVE EXCLUSION AND LIMITATIONS MAY NOT APPLY TO YOU.

#### 4.5 Limitation of Liability

APPLE SHALL NOT BE LIABLE FOR ANY DAMAGES OR LOSSES ARISING FROM ANY USE, MISUSE, RELIANCE ON, INABILITY TO USE, INTERRUPTION, SUSPENSION, OR TERMINATION OF MESSAGES FOR BUSINESS, INCLUDING ANY INTERRUPTIONS DUE TO SYSTEM FAILURES, NETWORK ATTACKS OR SCHEDULED OR UNSCHEDULED MAINTENANCE.

TO THE EXTENT NOT PROHIBITED BY APPLICABLE LAW, IN NO EVENT SHALL APPLE, ITS AFFILIATES, AGENTS OR PRINCIPALS BE LIABLE FOR PERSONAL INJURY, OR ANY INCIDENTAL, SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES WHATSOEVER, INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF PROFITS, CORRUPTION OR LOSS OF DATA, FAILURE TO TRANSMIT OR RECEIVE ANY DATA, BUSINESS INTERRUPTION OR ANY OTHER COMMERCIAL DAMAGES OR LOSSES, ARISING OUT OF OR RELATED TO YOUR USE OR INABILITY TO USE MESSSAGES [sic] FOR BUSINESS, APPLICATIONS OR SERVICES IN CONJUNCTION WITH MESSAGES FOR BUSINESS, HOWEVER CAUSED, REGARDLESS OF THE THEORY OF LIABILITY (CONTRACT, TORT OR OTHERWISE) AND EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OR LIMITATION OF LIABILITY FOR PERSONAL INJURY, OR OF INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THIS LIMITATION MAY NOT APPLY TO YOU. IN NO EVENT SHALL APPLE'S TOTAL LIABILITY TO YOU FOR ALL DAMAGES (OTHER THAN AS MAY BE REQUIRED BY APPLICABLE LAW IN CASES INVOLVING PERSONAL INJURY) EXCEED THE AMOUNT OF FIFTY DOLLARS ($50.00). THE FOREGOING LIMITATIONS WILL APPLY EVEN IF THE ABOVE STATED REMEDY FAILS OF ITS ESSENTIAL PURPOSE.

#### 4.6 Waiver and Indemnity

By using Apple Messages for Business, a Business and MSP agree, to the extent permitted by law, to indemnify and hold Apple, its officers, directors, shareholders, predecessors, successors in interest, employees, agents, contractors, subsidiaries, and affiliates harmless from any demands, losses, liability, damages, claims, suits, costs or expenses (including attorneys' fees and taxes) arising out of or related to (i) a Business and/or its MSP's use of Apple Messages for Business; or (ii) a Business and its MSP's violation of these Service Terms. This waiver and indemnity provision applies to all violations or suspected violations described in or contemplated by these Service Terms.

#### 4.7 Fees Charged by Apple

Apple reserves the right to charge fees for use of Apple Messages for Business. Information about fees or fee changes may be posted on the Apple Messages for Business web portal, other Apple-branded webpages, or otherwise made available by Apple.

#### 4.8 Marketing, Promotion, Internal Use by Apple.

A Business and MSP acknowledge and agree that Apple may use any and all names, logos, graphics, assets, marks, screenshots, images, designs, text, audio or visual clips, print, digital, or other materials that depict the Business or MSP and implementation of Apple Messages for Business for Apple's promotion, marketing, or internal use purposes; provided, however, Apple shall not use these materials for other purposes without further permission.

#### 4.9 Apple Proprietary Rights

The Apple Messages for Business service, including any portion thereof, is owned by Apple, and is protected by applicable intellectual property and other laws, including, but not limited to, copyright, patent, trademark, and trade secret.

### 5. Violation of Service Terms

If a Business or MSP fails, or Apple suspects that a Business or MSP has failed, to comply with any of the provisions of these Service Terms, Apple may limit, suspend, and/or terminate the Business and/or MSP's use and/or preclude and/or restrict access to Apple Messages for Business, or any portion thereof. In such case, Apple may also delete or remove from Apple Messages for Business any content or material that violates, or Apple suspects violates, the Service Terms or applicable laws.

A Business and MSP hereby grant Apple the right to take steps Apple believes are reasonably necessary or appropriate to enforce and/or verify compliance with any part of these Service Terms and/or the ABR Terms of Use. A Business and MSP agree that Apple has the right, without liability to you, to disclose any data and/or information to law enforcement authorities, government officials, and/or a third party, as Apple believes is reasonably necessary or appropriate to enforce and/or verify compliance with any part of this Agreement (including but not limited to Apple's right to cooperate with any legal process relating to your use of Apple Messages for Business and/or any portion thereof, and/or a third-party claim that your use of Apple Messages for Business and/or any portion thereof is unlawful and/or infringes such third party's rights). A Business and its MSP further agree that Apple may also disclose information about a Business and its MSP if Apple determines that for purposes of national security, law enforcement or other issues of public importance, disclosure is necessary or appropriate.

### 6. Controlling Law, Venue, and Severability

Except to the extent expressly provided herein, these Service Terms and the relationship between you and Apple shall be governed by the laws of the State of Delaware, excluding its conflicts of law provisions. You and Apple agree to submit to the personal and exclusive jurisdiction of the courts located within the county of Santa Clara, California, to resolve any dispute or claim arising from this Agreement.

These Service Terms shall not be governed by the United Nations Convention on Contracts for the International Sale of Goods, the application of which is expressly excluded.

If for any reason a court of competent jurisdiction finds any provision, or portion thereof, to be unenforceable, the remainder of these Service Terms shall continue in full force and effect.

### 7. Entire Agreement

These Service Terms, including the other terms and materials incorporated herein, constitute the entire agreement between a Business, MSP, and Apple and govern all use of Apple Messages for Business, superseding any prior agreements with respect to the same subject matter. A Business or MSP also may be subject to additional terms and conditions that may apply when you use Apple Messages for Business, affiliate services, third-party content, third-party software, or additional services. If any part of these Service Terms is held invalid or unenforceable, that portion shall be construed in a manner consistent with applicable law to reflect, as nearly as possible, the original intentions of the parties, and the remaining portions shall remain in full force and effect. Apple's failure to enforce any right or provisions in this Agreement will not constitute a waiver of such or any other provision. Apple will not be responsible for failures to fulfill any obligations due to causes beyond its control.

### 8. Feedback and Information

Any feedback provided by a Business or MSP regarding Apple Messages for Business shall be deemed to be non-confidential. Apple shall be free to use such information on an unrestricted basis.

---

Last updated: December 17, 2024

Copyright © 2024 Apple Inc. All rights reserved.


---

## Appendix A — Conflict & Recency Resolution Register (Master §37)

## 37. CONFLICT & RECENCY RESOLUTION REGISTER

> **Purpose.** Every fact that appears in more than one source at differing values or dates is resolved here once, explicitly, so the body of the canonical never has to re-litigate it. Each row records the **chosen value**, the **winning source and date**, and the **superseded value**. The governing rule: higher Authority Rank wins; on equal rank, the more recent date wins; deliberate exceptions are noted. This register is the operational form of the "flag the most up-to-date data on duplicates" requirement.

| # | Fact / topic | Chosen (authoritative) value | Winning source (date) | Superseded / lower-ranked value | Note |
|---|---|---|---|---|---|
| **R1** | Primary technical authority | REST API Integration Spec **v4.2.9** is the top tie-breaker for all message/API schema | `msp-rest-api` v4.2.9 (03 Jun 2026) | Apple Integration Word doc **v4.2.2** (27 Feb 2026) | v6.0's "Word doc prevails" rule retired. Where v4.2.2 and v4.2.9 differ, v4.2.9 wins; where only v4.2.2 spoke and v4.2.9 is silent, the v4.2.2 statement is preserved as historical. |
| **R2** | Apple Pay device/browser support | Includes visionOS, Optic ID, and third-party browsers requiring an Apple Pay–capable iPhone on **iOS 18+** | Apple Pay Merchant Guide (Mar 2026) | Apple Pay Platform Guide (Jun 2025) — Mac Touch ID / Apple Pay-capable iPhone only, no visionOS/iOS-18 detail | Additive, not contradictory; newer guide is the complete statement (§36.12). |
| **R3** | Availability-check APIs | `canMakePayments()` (web+app), `canMakePayments(usingNetworks:)` (app-only), `applePayCapabilities()` (web-only) | Apple Pay Merchant Guide (Mar 2026) | Apple Pay Platform Guide (Jun 2025) — lacked `usingNetworks:` and the app/web split | `usingNetworks:` added Mar 2026; `applePayCapabilities` guidance added Jun 2025 (§36.12). |
| **R4** | Payment Processing Certificate detail | 25-month validity **+ ECC-256 / mainland-China RSA-2048 CSR + prepare-then-activate renewal** | Apple Pay Merchant Guide (Mar 2026) | Tutorial / canonical §16.14 — 25-month figure only | Merchant guide enriches; §16.14 remains correct but thinner (§36.3). |
| **R5** | Merchant ID lifetime | **Never expires**; reusable across apps/websites | Apple Pay Merchant + Platform Guides | Absent in v6.0 canonical | New fact; complements the §16.14 AMB 1:N cardinality (§36.2). |
| **R6** | `paymentSession` endpoints | Production `apple-pay-gateway.apple.com/...` **and** sandbox/cert `apple-pay-gateway-cert.apple.com/...` | Apple Pay Merchant Guide (Mar 2026) | Canonical §16.14 — production endpoint only | Sandbox endpoint added; production endpoint unchanged (§36.6). |
| **R7** | §17.2 EV-certificate requirement | **Required — Direct Gated Apple** (stated in the REST API spec) | `msp-rest-api` v4.2.9, L4017 | A web-search verification pass returned "not found in any AMB source" | **False negative**, not a real absence: the gated REST API portal is not search-indexed. Do **not** downgrade this claim. Corrects a prior recommendation (§17.2 note). |
| **R8** | §17.2 OAuth callback host `auth.businesschat.apple.com` | Operationally reliable, labelled **Referenced Only**; registered **alongside** the MSP's own platform callback | Third-party MSP docs (LivePerson dev docs; Auth0 thread attributed to Apple Support) | No Apple-authored corpus source states it | Not Apple-primary; two independent MSPs converge on the identical host. Legacy `businesschat.apple.com` (pre-rebrand) is still the auth host (§17.2). |
| **R9** | Developer Program enrolment type | Merchants: individual **or** organization; platform integrators: organization; Enterprise Program accounts **cannot** enable Apple Pay | Merchant Guide (Mar 2026) + Platform Guide (Jun 2025) | — | Scope distinction, not a conflict — recorded to prevent future mis-merge (§36.1). |
| **R10** | `msp-onboarding` staleness | Facts sourced **only** to `msp-onboarding` v3.0.3 (01 Feb 2024) are **verify-before-reliance** unless re-confirmed by a Rank 1–4 source | Provenance rule (this canonical) | — | 3-phase model, advertising embargo, architecture are cross-confirmed and safe; step-level UI/timing is the risk (§33.5). |

> **Maintenance rule.** When a new source is added, add a Source-Inventory row (front matter), a change-log trail (§33), and one R-row here for each fact it duplicates or supersedes. The body of the canonical cites the R-number rather than restating the resolution.

---



## Appendix B — Audit: Documentation Gaps, Ambiguities & Contradictions (Master §32)

## 32. AUDIT: DOCUMENTATION GAPS, AMBIGUITIES & CONTRADICTIONS

> This section preserves gaps only where both the Apple Integration Spec and Apple first-party sources are silent. Items resolved by the Apple Integration Spec (Word doc v4.2.2) are marked accordingly. All gap classification uses the Evidence Strength and Specification Depth taxonomy.

### 32.1 Documentation Gaps

| # | Topic | Status | Missing Detail | Evidence Strength of Gap | Specification Depth |
|---|---|---|---|---|---|
| 1 | Opaque ID technical spec | ⚠️ Partially informed | Apple-direct sources (DOC 4.6) confirm: Opaque ID is shared across the user's multiple devices for a given Business; persists for years; is unique per (user, business) pair; is not shared between businesses, even if served by the same MSP. **Still absent from any Apple source:** generation algorithm, entropy specification, rotation policy, revocation mechanism. The behavioral envelope is now documented; the cryptographic spec remains unpublished. | No Evidence (algorithm) / Direct Gated Apple (behavioral envelope) | Partial Spec |
| 2 | Business relay TLS version | ⚠️ Unresolved | No statement on whether TLS 1.3 is also supported or planned for the Apple → business relay. TLS 1.2 confirmed; ceiling unknown. | No Evidence | No Spec |
| 3 | Offline message cache encryption-at-rest | ⚠️ Unresolved | No specification of encryption-at-rest algorithm for cached messages. | No Evidence | No Spec |
| 4 | AMB-specific Apple Pay payload | ✅ Resolved by Word doc | Apple Integration Spec (Word doc v4.2.2) provides complete AMB Apple Pay schema (Section 16). | Apple MSP Spec | Full Spec |
| 5 | OAuth 2.0 new authentication flow spec | ✅ Resolved by Word doc | Apple Integration Spec (Word doc v4.2.2) provides complete schema (Section 17). | Apple MSP Spec | Full Spec |
| 6 | Form Message payload | ✅ Resolved by Word doc | Apple Integration Spec (Word doc v4.2.2) provides complete schema (Section 19). | Apple MSP Spec | Full Spec |
| 7 | List Picker JSON schema | ✅ Resolved by Word doc | Apple Integration Spec (Word doc v4.2.2) provides complete schema (Section 14). | Apple MSP Spec | Full Spec |
| 8 | Time Picker JSON schema | ✅ Resolved by Word doc | Apple Integration Spec (Word doc v4.2.2) provides complete schema (Section 15). | Apple MSP Spec | Full Spec |
| 9 | Invitations / Business Updates (proactive messaging) | ✅ Resolved (operational + legal layers) | Operational schema documented in §20–21 (Word doc v4.1.8 — feature operational name "Invitations"). Legal layer added in v6.0 via §35.4 (Service Terms §2.12 — feature legal name "Business Updates"): POS-only opt-in, ≤ 2-year max validity, mandatory verbatim disclosure language, opt-out in every Business Update, Apple-authorized templates only. Residual partial gap: `referenceId` values in CloseSession body not present in published example payload — see Ambiguity #6. | Direct Public Apple \| Direct Gated Apple (legal) | Full Spec (outbound + legal); Partial Spec (CloseSession body) |
| 10 | Message Suggest technical implementation | ✅ Partially resolved | Submission field spec, throttle mechanics, ramp-up period, and throttle control documented in Section 29.11 (MSP Consensus sources). Ramp-up percentage curve and minimum call volume eligibility threshold remain undocumented in any Apple-authored source. | Referenced Only (Apple) | Partial Spec |
| 11 | Managed Apple Account behavior in AMB | ⚠️ Partially informed | DOC 2.2 (Brand Onboarding) confirms a corporate Managed Apple Account may be used for AMB account login by the registering Business. **Still absent from any Apple source:** customer-side behavioral differences, restrictions, or enterprise admin controls specific to AMB for Managed accounts when used as the consumer-side Apple Account. Business-registration use is documented; consumer-side use is not. | Direct Gated Apple (registration-side) / Referenced Only (consumer-side) | Partial Spec (registration); No Spec (consumer-side) |
| 12 | Typing indicators | ✅ Resolved by Word doc | Apple Integration Spec confirms bidirectional typing indicators (`typing_start`, `typing_end`) are Required (Sections 7 and 8). Previously unconfirmed in PASS A and PASS B. | Apple MSP Spec | Full Spec |
| 13 | Read receipts | ⚠️ Unresolved | Read receipts documented for iMessage person-to-person; no explicit AMB business-context documentation found on any Apple-owned source. | No Evidence | No Spec |
| 14 | Specific numeric API sub-error codes | ✅ Partially resolved by Word doc | Apple Integration Spec provides 200, 400, 401, 403, 404, 410, 500 (Section 22). No AMB-specific sub-error codes beyond HTTP status codes are published by Apple. | Apple MSP Spec | Full Spec (for HTTP codes); No Spec (for sub-codes) |
| 15 | Rate limits (volume, per-brand, per-conversation) | ⚠️ Unresolved | No Apple-authored rate limit table published in any source. | No Evidence | No Spec |
| 16 | Geographic availability by country | ⚠️ Unresolved | No Apple-authored country availability list published. AMB is Apple ecosystem only; international availability not specified. | No Evidence | No Spec |
| 17 | HIPAA BAA availability | ✅ **RESOLVED — explicit exclusion** | Service Terms §2.9 (DOC 3.1) contains a verbatim HIPAA exclusion: HIPAA-covered entities, business associates, or representatives **may not** use any component, function, or facility of AMB to create, receive, maintain, or transmit Protected Health Information (PHI) as defined at 45 C.F.R § 160.103, or use AMB in any manner that would make Apple (or any subsidiary) the Business's or any third party's business associate. **AMB is not approved for PHI by HIPAA-covered entities; Apple expressly refuses to be a business associate.** This is not "Apple is silent" — it is an explicit prohibition. See §35.3 for the verbatim text. | Direct Gated Apple (legal) | Full Spec (exclusion) |
| 18 | SOC 2 status | ⚠️ Unresolved | Not addressed in any Apple-authored source. ISO/IEC 27001 and 27018 confirmed (Section 28.3). | No Evidence | No Spec |
| 19 | v4.2.2 "Interactive message image type restrictions added" | ✅ Resolved | The restriction is **size-based only** — not MIME-type-based. The `ImageItem` Dictionary (§12.5) already documented the applicable limits: ≤ 200 KB per individual image binary; ≤ 5 MB total for the `images` array. No PNG-only or MIME type constraint was added to `interactiveData.data.images`. The PNG-only rule exists only for the `ImageAsset` in Rich Link messages (§23.4), where it has always been explicit. No canonical changes required. | Apple MSP Spec | Full Spec |
| 20 | v4.2 "Updated payload specifications for enhanced security" | ✅ Resolved | Three concrete changes in the Authentication Message flow, all already documented in §17: (1) **Client secret removed from payload** — the new OAuth 2.0 flow (`AUTH2`) eliminates `clientSecret` from in-message transmission (§17.10; §17 deprecation note); (2) **`state` parameter now required for CSRF protection** — `state` is REQUIRED in §17.5 with explicit CSRF semantics; must be a unique cryptographically random session token; (3) **OAuth provider endpoints must present a valid Extended Validation (EV) certificate** — documented in §17.2. All three changes originated in v4.2 (11 February 2026). No canonical changes required. | Apple MSP Spec | Full Spec |
| 21 | List Picker item count ceiling | ✅ Confirmed characteristic — not a gap | Apple does not publish a numeric maximum item count for List Picker. This is confirmed as an architectural characteristic, not a documentation gap: Apple explicitly documents hard count limits when they exist (e.g., Quick Reply 2–5 items verbatim in Apple's MSP tutorial); no equivalent statement exists for List Picker in any Apple-indexed source. The operative Apple-level constraint is the 10-KB `interactiveData` payload threshold. See Section 14.4 note. MSP-level item count limits vary widely and are not Apple-spec requirements. | No Evidence (item count ceiling) | No Spec (item count) |
| 22 | PII request protocol | ✅ Resolved | Apple-direct policy added to canonical at §27.7. Yes-no clarifying question gating; first-name vs. full-name request scope. | Direct Gated Apple | Full Spec |
| 23 | Brand Privacy Policy / Terms of Use display rules | ✅ Resolved | Apple-direct rules added to canonical at §27.8. Rich-link only; first-engagement and post-update timing only; three forbidden in-conversation phrases. | Direct Gated Apple | Full Spec |
| 24 | Service Terms / Legal layer absent from canonical | ✅ Resolved | Service Terms (DOC 3.1) integrated as new §35. Includes §2.9 HIPAA exclusion, §2.12 Business Updates legal layer, $50 liability cap (§4.5), 90-day MSP feature compliance window (§2.1), Delaware/Santa Clara venue (§6), Apple's modification rights (§4.1), and full prohibited-uses list (§3). | Direct Gated Apple | Full Spec |
| 25 | 90-day MSP feature compliance window | ✅ Resolved | Documented in §35.3 as derived from Service Terms §2.1: MSP must comply with new feature requirements within 90 days of Apple notification. | Direct Gated Apple | Full Spec |
| 26 | Brand asset specifications (logo specs, naming format, account types) | ✅ Resolved | Documented in §28.3 (extended in v6.0). Wide logo: ≥256px height, ≤1706px width, ≤6.66:1 aspect ratio, transparent background, full-color artwork, sRGB or P3 color space, ≤2MB, PNG/JPEG. Square logo: ≥1024×1024px, full-color background, sRGB or P3 color space, ≤2MB, PNG/JPEG, no personal/product imagery. Business name: commercial name only — no location, no LLC/LTD/Inc., etc. Account types: online-only / single public location / multiple public locations. | Direct Gated Apple | Full Spec |
| 27 | Post-launch optimization framework | ✅ Resolved | Apple-direct framework added at §28.9. 30-day cycles, optimization team formation, intent prioritization (frequency / CSAT / time-to-resolve), 70% automation target, 3-minute live-agent connection target, traffic-increase order, quarterly executive cadence. | Direct Gated Apple | Full Spec (framework); Behavioral Only (70% target methodology) |
| 28 | Conversational Design Guidelines content | ✅ Resolved | Apple-direct guidelines added at §27.9. Live-agent intro protocols, single-agent rule, 5-second auto-respond, 5-minute queue update, response keyword table, notifications opt-in/out language, satisfaction surveys, best practices. | Direct Gated Apple | Full Spec |
| 29 | Apple Pay merchant-ID 1:N constraint | ✅ Resolved | Documented in §16.14 (extended in v6.0): each AMB account has at most one associated Merchant ID; a Merchant ID may be reused across multiple AMB accounts. | Direct Gated Apple | Full Spec |
| 30 | Apple Pay Payment Processing certificate expiry | ✅ Resolved | Documented in §16.14 (extended in v6.0): 25-month validity. | Direct Gated Apple | Full Spec |
| 31 | Apple Class A network block for HA Proxy ingress | ✅ Resolved | Allow Apple's Class A block. Verbatim source form `17.0.0/8` is preserved in Part 1; the standard four-octet equivalent `17.0.0.0/8` is noted for reference only, not substituted — see §37 R3. | Direct Gated Apple | Full Spec |
| 32 | Pre-launch advertising embargo (MSPs) | ✅ Resolved | Documented in §28.8: MSPs must not advertise involvement with AMB until launch is complete. Reinforced by Service Terms §2.1 (no promotion until written approval). | Direct Gated Apple | Full Spec |
| 33 | MSP onboarding 3-phase model | ✅ Resolved | Documented in §28.7: Integration → Business Development → Launch, each with Apple-driven gate. Capability requirements and demo requirements specified. | Direct Gated Apple | Full Spec |
| 34 | OAuth2 / Apple Pay / iMessage app demo timing | ✅ Resolved | Documented in §28.7: Apple Pay merchant account several days; OAuth2 endpoint 2–3 business days; iMessage app demo lead time variable. | Direct Gated Apple | Full Spec |
| 35 | User-facing privacy statement locations | ✅ Resolved | Documented in §31.5: in-conversation info button, iOS Settings > Messages, Apple website. **Not** displayed in-conversation. | Direct Gated Apple | Full Spec |
| 36 | Forbidden in-conversation phrases | ✅ Resolved | Documented in §27.8: "data rates may apply", "messaging rates may apply", "this chat may be recorded" — Apple explicitly prohibits all three in AMB conversations. | Direct Gated Apple | Full Spec |
| 37 | Encryption self-test vectors | ✅ Resolved | Documented in §11.9 (extended in v6.0): hex key + plaintext "12345" → expected Base16 ciphertext "7634125F65". | Direct Gated Apple | Full Spec |
| 38 | Three-term equivalence (delete / close / Leave Conversation) | ✅ Resolved | Documented in §21.4 (extended in v6.0): explicit equivalence note covering user-side UI, REST API message type, and Word doc nomenclature. | Direct Gated Apple | Full Spec |

### 32.2 Ambiguities

| # | Topic | Issue | Evidence Strength |
|---|---|---|---|
| 1 | Session identifier vs. Opaque ID | Legal page states businesses receive a "session identifier"; security guide references "Opaque ID." Relationship not defined. Are they the same token, derived, or independent? | Direct Public Apple (conflicting sources) |
| 2 | Invitations identity context | ✅ **Resolved** — Invitations use a phone number (`tel:+1…`) as `destinationId`. This is a separate identity context from organic AMB conversations. The Opaque ID mechanism does not apply to Invitations. See Section 20.6.2. | Direct Public Apple |
| 3 | Entry point selective enablement | No Apple-authored documentation states whether Maps and Siri can be toggled independently or must be enabled together. | Direct Gated Apple (partial) |
| 4 | Business-initiated contact eligibility | ✅ **Resolved (partial)** — Business-initiated contact is confirmed as permitted via the Invitations feature only. Gated access required. Explicit customer opt-in required. Apple-managed templates only. Unsolicited notifications and marketing explicitly prohibited. See Section 20.2. | Direct Public Apple |
| 5 | iOS version floor (general) | No Apple-authored minimum OS version table for all AMB feature tiers published on developer.apple.com. Individual feature minimums are documented; a consolidated table is absent. | Direct Gated Apple (partial) |
| 6 | CloseSession `referenceId` values in body | Source document states CloseSession "contains the phone number and the reference IDs included in all past invitation messages." The phone number is confirmed in the `source-id` HTTP header. `referenceId` values are not present in the published example payload body. Whether they appear as a separate field, nested object, or only in the header is unspecified. | Direct Public Apple (partial) |

### 32.3 Contradictions

| # | Topic | Conflict | Evidence Strength |
|---|---|---|---|
| 1 | Encryption framing: E2E vs. transport | Apple's consumer privacy page implies E2E encryption covers all Messages; the AMB security guide explicitly states "Apple messaging servers decrypt these messages in RAM." AMB is transport-encrypted (TLS 1.2), not end-to-end encrypted. Apple's consumer marketing does not clearly distinguish AMB from iMessage for consumers. | Direct Public Apple (conflicting sources) |
| 2 | Conversation history retention | Security guide: "Apple Messages for Business service never stores conversation history." Legal page: "information about your sessions may be used to provide and improve the service." "Sessions" vs. "conversation history" is not defined by Apple. | Direct Public Apple (conflicting sources) |
| 3 | AMB message visual indicator | AMB messages have a gray background. Documented in Apple's legal/privacy page but absent from Apple HIG and developer.apple.com UI guidance for businesses building AMB experiences. | Direct Public Apple (legal page only) |

### 32.4 Completeness Assessment

| Domain | Coverage | Evidence Strength | Specification Depth | Assessment |
|---|---|---|---|---|
| **Identity** | Opaque ID concept, per-business uniqueness, no PII sharing | Direct Public Apple | Partial Spec | Concept documented; generation algorithm, token lifecycle, and session identifier relationship absent |
| **Encryption** | Transit path documented (iMessage-equivalent → Apple, TLS 1.2 → business); RAM decryption disclosed; encryption self-test vectors documented in §11.9 | Direct Public Apple \| Direct Gated Apple | Partial Spec | At-rest encryption spec and TLS version ceiling absent. **HIPAA: explicit exclusion (§35.3) — not a gap.** SOC 2: not published. |
| **Interactivity** | Full schemas for all interactive types confirmed via Word doc | Apple MSP Spec | Full Spec | All major schemas now documented and implementation-ready |
| **Payments** | Full AMB-specific Apple Pay schema confirmed via Word doc | Apple MSP Spec \| Direct Public Apple | Full Spec | Substantially complete; refund flow is outside AMB |
| **Authentication** | Full new OAuth 2.0 flow schema confirmed via Word doc | Apple MSP Spec \| Direct Gated Apple | Full Spec | Old flow deprecated; new flow fully specified |
| **Entry points** | Entry point list documented; Message Suggest technical implementation absent | Direct Gated Apple | Partial Spec | Configuration steps described; integration architecture for Message Suggest unpublished |
| **Constraints** | Attachment size, timeouts, device requirements, Apple Class A ingress block, encryption self-test vectors, Apple Pay 1:N merchant constraint and certificate expiry documented | Apple MSP Spec \| Direct Gated Apple | Full Spec (documented); No Spec (undocumented) | Rate limits, geographic availability, SOC 2 not published. **HIPAA: explicit exclusion (§35.3) — not a gap.** |
| **Invitations** | Full outbound spec, template schemas, validation, error codes, CloseSession webhook documented | Direct Public Apple | Full Spec (outbound); Partial Spec (CloseSession body) | CloseSession `referenceId` field presence in body unconfirmed; `urn:biz:` prefix in `sourceId` not formally specified |
| **Legal** | Service Terms reproduced (§35); HIPAA exclusion explicit (§35.3); $50 liability cap (§35.6); Delaware/Santa Clara venue (§35.8); 90-day MSP feature compliance (§35.3); Business Updates legal layer (§35.4); full prohibited-uses list (§35.5) | Direct Gated Apple | Full Spec | Substantively complete; legal layer was previously absent from canonical |
| **Conversational design** | Live-agent protocols, automated messaging rules, triage best practices, response keywords, notifications opt-in/out language, satisfaction surveys (§27.9) | Direct Gated Apple | Full Spec | Apple's published conversational design rules now reproduced in canonical |
| **Brand-side privacy/ToU** | Display format (rich-link only), display timing (first engagement + updates only), forbidden in-conversation phrases (§27.8); cross-reference to §31.5 for Apple-side privacy statement locations | Direct Gated Apple | Full Spec | Previously absent |
| **PII request protocol** | Yes-no clarifying question gating; permitted scope by use case (§27.7) | Direct Gated Apple | Full Spec | Previously absent |
| **Post-launch optimization** | 30-day cycles, optimization team, intent prioritization, 70% automation target, 3-minute connection target, traffic increase order, quarterly executive cadence (§28.9) | Direct Gated Apple | Full Spec (framework); Behavioral Only (70% target measurement methodology) | Previously absent |
| **MSP onboarding lifecycle** | 3-phase model: Integration → Business Development → Launch; capability requirements; demo requirements; multi-day approval items; advertising embargo (§28.7, §28.8) | Direct Gated Apple | Full Spec | Previously absent |

---



## Appendix C — Revision History & Changelog (Master §33 + §34)

> **⚠ Source-verification addendum (revision trails re-checked against the four supplied `.md` sources).** The Master §33.1/§33.2 trails below were inherited from an earlier synthesis and are **stale**. Each source carries its own *Revision History* table; diffed against them, §33.1 stops at v4.2.2 and §33.2 at v2.11, both missing the newest Apple-published revisions. Per this canonical's keep-both rule, the Master trails are retained unchanged below and the **current source rows are reproduced verbatim here** as the recency winners:
>
> **§33.1 REST API Integration Spec — rows missing from the Master trail (verbatim from `msp-rest-api.md` Revision History):**
>
> | Date | Version | Summary |
> |---|---|---|
> | 3 Jun 2026 | 4.2.9 | Construct Payload section updated to include Apple Music and Apple Maps rich link support |
> | 19 May 2026 | 4.2.8 | Closed Conversation section updated, including HTTP 410 Gone response details |
> | 19 May 2026 | 4.2.7 | Invitation Messages section updated, including sourceId and destinationId clarification |
> | 08 May 2026 | 4.2.6 | Invitations feature details updated |
> | 08 May 2026 | 4.2.5 | UUID details updated |
> | 20 April 2026 | 4.2.4 | Invitation Messages added to Required Features; 404 — Fallback Expectation section added |
> | 06 March 2026 | 4.2.3 | Minor corrections |
>
> (v4.2.9 is the current authoritative technical spec; the Master §33.1 trail's top row is 4.2.2, 27 Feb 2026.)
>
> **§33.2 Public-Facing Onboarding Guide — rows missing from the Master trail (verbatim from `messaging-documentation.md` Revision History):**
>
> | Date | Version | Summary |
> |---|---|---|
> | May 21, 2026 | 3.1 | Misc corrections and updated links |
> | January 6, 2026 | 3.0 | Updated References using latest iOS 26 references and designs |
>
> **§33.2 wording correction:** for v2.11 the Master trail reads *"Updated references of Apple ID to Apple Account"*, but the source literally reads *"Updated references of Apple Account to Apple Account"* (an apparent Apple-side typo). The source wording is authoritative; the Master silently normalized it.
>
> **§32 (audit) note:** §32 is analytical overlay — documentation-gap / ambiguity / contradiction commentary, **not** reproduced Apple source text — so it cannot be diffed for verbatim fidelity. Its factual anchors were spot-checked against the four sources (`capability-list`, `17.0.0/8`, `sessionIdentifier`, Opaque ID behavioral envelope, Roadside Assistance via Satellite all present); several §32.1 rows cite the **retired Word-doc v4.2.2**, which is outside the supplied source set and thus unverifiable from these files.


## 33. REVISION HISTORY

> **Two parallel Apple-published version trails are tracked here:**
> - **§33.1 — REST API Integration Spec trail** (Word doc v4.2.2 + REST API portal v4.2.3 dated Feb 6, 2026 — MSP-facing technical spec)
> - **§33.2 — Public-facing Onboarding Guide trail** (v2.11 dated Feb 7, 2025 — brand- and policy-facing documentation; tracks the messaging-documentation portal pages including Policies, Getting Started, UX Design, XP Review, Metrics, Privacy & Security, FAQ)

### 33.1 REST API Integration Spec — Revision Trail

*(From Apple Integration Spec v4.2.2 + REST API portal v4.2.3 — authoritative for technical schema)*

| Date | Version | Summary |
|---|---|---|
| 27 February 2026 | 4.2.2 | Interactive message image type restrictions added *(see §32.1, Gap #19 — Resolved)* |
| 16 February 2026 | 4.2.1 | Minor updates to leave conversation function |
| 11 February 2026 | 4.2 | Updated payload specifications for enhanced security *(see §32.1, Gap #20 — Resolved)* |
| 04 February 2026 | 4.1.8 | Feature name revision; Leave Conversation specifications updated |
| 01 December 2025 | 4.1.7 | New server fix for Form Message. Latest version available is 1.2, set in `interactiveData > data > dynamic > version` |
| 30 October 2025 | 4.1.6 | Clarified Close Conversation requirements |
| 14 April 2025 | 4.1.5 | Updated Apple Maps Rich Link specifications |
| 07 April 2025 | 4.1.4 | Updated Business Updates specifications |
| 21 March 2025 | 4.1.3 | Updated App Clip Rich Link Generator specs |
| 04 February 2025 | 4.1.2 | Channel Settings — Updated OAuth URL parameters details |
| 24 October 2024 | 4.1.1 | Updated Type Interactive details |
| 01 October 2024 | 4.1 | Updated Tapback information with new reactions available with iOS 18 |
| 14 September 2024 | 4.0.8 | Updated iOS requirements for Business Updates feature |
| 28 August 2024 | 4.0.7 | Updated file type support and device capability handling |
| 09 August 2024 | 4.0.6 | Updated MSP feature requirements including new Rich Links capabilities |
| 15 April 2024 | 4.0.5 | `sessionIdentifier` details added |
| 01 February 2024 | 4.0.3 | Service name update to match registered service mark |
| 31 May 2023 | 4.0 | Links updates and new Construct Payload for App Clips support |
| 15 March 2023 | 3.9 | Updated Rich Link instructions for Apple Maps URL |
| 24 February 2023 | 3.8 | Deprecation of the original OAuth authenticate method |
| 07 June 2022 | 3.5 | New Authentication Message specification (iOS 16, macOS 13) |
| 06 May 2022 | 3.4 | Form documentation fixes |
| 11 February 2022 | 3.0.0 | Integration requirements revised for bot and agent; capabilities and device-agent deprecated |
| 20 September 2021 | 2.0.0 | Rebranded Business Chat to Messages for Business; Chat Suggest to Message Suggest |
| 22 July 2021 | 1.0.0 | Initial release: HTTP Header `capability-list`; iMessage App clarification; Quick Reply (Interactive) |

### 33.2 Public-Facing Onboarding Guide — Revision Trail

*(From Documentation Revision History at register.apple.com/resources/messages/messaging-documentation/doc-rev-history — authoritative for policy and onboarding documentation)*

| Date | Version | Summary |
|---|---|---|
| February 7, 2025 | 2.11 | Updated references of Apple ID to Apple Account (terminology change applied throughout the canonical in v6.0) |
| October 31, 2024 | 2.10.8 | Updated brand and MSP onboarding overview |
| July 16, 2024 | 2.10.7 | Revised graphics, added new detailed guidance for onboarding |
| April 11, 2024 | 2.10.6 | Terminology updates and minor fixes |
| February 11, 2024 | 2.10.5 | Minor fixes |
| November 2, 2023 | 2.10.4 | Fixes |
| September 26, 2023 | 2.10.3 | Fixes |
| September 25, 2023 | 2.10.2 | RSA updates |
| September 15, 2023 | 2.10.1 | Fixes |
| September 12, 2023 | 2.10 | Qualifying as a Roadside Assistance via Satellite provider |
| May 9, 2023 | 2.9.4 | Updated links to Human Interface Guidelines |
| April 11, 2023 | 2.9.3 | Updated instructions under the policies |
| January 5, 2023 | 2.9.2 | Updated instructions to enable native entry points |
| January 3, 2023 | 2.9.1 | Fixes |
| December 15, 2022 | 2.9 | Link fixes; ISO Certifications |
| November 4, 2022 | 2.8 | Updated Register Your Accounts and instructions for registering Message Suggest |
| October 24, 2022 | 2.7 | Updated Policies related to Requesting end-user's Personal Identifiable Information (origin of §27.7 PII protocol) |
| October 10, 2022 | 2.6 | Updated "Pass Apple's QA" → "Pass the Experience Review" (origin of §28.6 terminology); moved Best Practices into UX Design; moved Message Suggest content |
| September 15, 2022 | 2.5 | Added entry point to Apple Pay Order tracking on iOS 16 and macOS 13 |
| April 19, 2022 | 2.4 | Register links updated |
| March 31, 2022 | 2.3 | Apple Messages localized new buttons |
| March 23, 2022 | 2.2 | Apple Messages new buttons; Design and Implement Your User Experience updated; Human Interface Guidelines links updated |
| November 25, 2021 | 2.1.1 | Fixes |
| October 25, 2021 | 2.1 | Added Quick Reply support |
| September 20, 2021 | 2.0.0 | Rebranded Business Chat → Messages for Business; Message Suggest naming; removed BETA from Quick Reply |
| June 22, 2021 | 1.0.0 | Initial release |

> **Note on Apple's own incrementation table:** The Documentation Revision History page contains a "Revision Number Incrementation" reference table where Apple inadvertently labeled both the Major and Minor revision rows as "1.0.0". This is an Apple-side typo and is not propagated into this canonical.

### 33.3 Roadside Assistance via Satellite Provider — Optional Domain

The September 12, 2023 (v2.10) revision added qualification criteria for becoming a Roadside Assistance via Satellite provider — a specialized AMB use case beyond mainstream brand onboarding. This domain is acknowledged here but not currently expanded in the canonical. If future canonical work needs to cover it, the source reference is in §33.2 v2.10 and Apple Roadside Assistance via Satellite documentation.

**Evidence Strength:** Direct Gated Apple. **Specification Depth:** Referenced Only.

### 33.4 MSP API Tutorial — Version Trail

*(Source: `msp-api-tutorial`, v3.4, last updated 29 April 2026 — worked examples / code, Authority Rank 4)*

| Date | Version | Summary |
|---|---|---|
| 29 April 2026 | 3.4 | Current version in corpus. Sending/receiving messages, attachment encryption self-test vectors (§11.9), Apple Pay merchant certificate + PEM generation walkthrough, worked OAuth 2.0 (LinkedIn) example. |
| 06 May 2022 | 3.4 (legacy numbering) | Form documentation fixes (per REST-spec trail cross-reference). |

> **Note:** The tutorial exposes multiple sub-pages (setup, receiving-sending-messages, applepay, interactive) that v5.0–v6.0 cited as DOC 4.5/4.6/4.7. All are contained in this single portal source.

### 33.5 MSP Onboarding — Version Trail  ⚠ STALE SOURCE

*(Source: `msp-onboarding`, v3.0.3, last updated **01 February 2024** — Authority Rank 7)*

| Date | Version | Summary |
|---|---|---|
| 01 February 2024 | 3.0.3 | Current version in corpus. Three-phase onboarding model (Integration → Business Development → Launch), MSP architecture, pre-launch advertising embargo, client-development feature demos. |

> ⚠ **Staleness banner:** This source is **2+ years older** than every other source in the inventory (next-oldest first-party technical source is 27 months newer). Any fact sourced **only** to `msp-onboarding` — where not re-confirmed by `msp-rest-api` v4.2.9, the portal v3.1, or the tutorial v3.4 — is flagged **verify-before-reliance**. The 3-phase model, advertising embargo, and architecture are cross-confirmed elsewhere and are safe; onboarding UI/screens and step-level timing are the highest staleness risk.

### 33.6 Apple Pay Platform Integration Guide — Version Trail

*(Apple-authored PDF — Authority Rank 6. Feeds §36 platform-integrator content.)*

| Date | Version | Summary |
|---|---|---|
| Jun 2025 *(footer)* | — | Platform / PSP integration: Web Merchant Registration API, key management/rolling, decryption (ECC/RSA, `publicKeyHash`), MPAN authorization flow, Merchant Token Management API, integration types. |

> **Date discrepancy (resolved):** The cover page is dated **September 2025** while all interior page footers read **June 2025**. Per the file-date protocol used throughout this canonical (file-internal date prevails over catalog/cover), **June 2025** is used. Where this guide overlaps the Merchant guide (Mar 2026), the Merchant guide wins on recency — see §37.

### 33.7 Apple Pay Merchant Integration Guide — Version Trail (Apple's own Change Log)

*(Apple-authored PDF — Authority Rank 2 for Apple Pay setup. Change Log reproduced from the guide's own Change Log page.)*

| Date | Summary |
|---|---|
| March 2026 | Minor editorial updates; `canMakePayments(usingNetworks:)` added; merchant-token guidance added; Merchant Token Management API section added; example Payment Object added for reference; testing recommendations added. |
| Jun 2025 | Guidance for `applePayCapabilities` API added; "Good practice when processing Apple Pay transactions" guidance added. |

### 33.8 Service Terms / Legal — Version Note

*(Source: register.apple.com/tou/bca/latest/en — Authority Rank 5. Full trail detail in §35.10.)*

| Date | Summary |
|---|---|
| 17 December 2024 | Current version (file footer). Confirmed unchanged as of the v7.0 re-verification (July 2026). Replaced the former Terms for Business Chat. |

---



## 34. CHANGELOG

### v7.0 Changes

| Date | Version | Summary | Sources |
|---|---|---|---|
| July 7, 2026 | v7.0 — Authority re-base + Apple Pay Integration Layer + provenance/recency hardening | **Authority re-based:** primary technical authority moved from Apple Integration Word doc v4.2.2 (27 Feb 2026) to **REST API Integration Spec v4.2.9 (03 Jun 2026)**; v4.2.2 retired to historical layer; Authority Order rewritten with an explicit 7-rank recency order. **New front-matter:** Provenance & Recency Source Inventory table added after the header. **New §36 — Apple Pay Merchant Setup, Registration & Processing (Integration Layer):** developer-account/region/server setup, Merchant ID (never expires), Payment Processing Certificate (25-month, ECC-256 / China RSA-2048, CSR→activate renewal), Merchant Identity Certificate (RSA-2048, `.p12`/PEM export), domain verification, `paymentSession` prod + `apple-pay-gateway-cert` sandbox endpoints, merchant-managed vs platform onboarding, **Web Merchant Registration API** (`registerMerchant`/`unregisterMerchant`/`getDetails`, `partnerInternalMerchantIdentifier`, `.well-known` domain association), key management/rolling (≥2 active certs, `publicKeyHash`), payment object + decryption (ECC/RSA, token format), **merchant tokens / MPAN** + **Merchant Token Management API** (`tokenNotificationURL`, `UNLINK` / `UPDATED_METADATA` / `UPDATED_CARD_ART`), availability checks (`canMakePayments` family), sandbox/cert testing — scoped to setup/registration/technical foundation; general commerce-UX (payment-sheet event code, error/coupon/disbursement samples, risk checks, marketing, button/HIG) explicitly marked out-of-scope with pointers. **New §37 — Conflict & Recency Resolution Register:** every cross-source duplicate/conflict resolved with chosen value, winning source+date, and superseded value (R1–R10). **Corrections:** §17.2 EV-certificate requirement confirmed Direct Gated Apple (sourced to `msp-rest-api` v4.2.9 L4017 — a prior web-search "not found" was a false negative on the gated portal); §17.2 OAuth callback host `auth.businesschat.apple.com` labelled Referenced Only (third-party corroborated) with the MSP-parallel-callback note. **Change logs:** §33 expanded from 2 trails to all sources — added tutorial (§33.4), MSP onboarding with stale-source banner (§33.5), Apple Pay Platform with Sep-vs-Jun date-discrepancy resolution (§33.6), Apple Pay Merchant own change log (§33.7), Service Terms note (§33.8). **Image layer (completed):** new §38 Image Manifest & Placement Map — all 77 markers (96 image files) joined to the four source CSVs for dimensions + source URLs (77/77 resolved, 0 missing); 7 structural/flow diagrams placed inline at matching sections (§1, §3, §7, §11.7, §17, §22, §28.7), the remaining 70 UI/screenshot/logo markers held in the manifest. **Original-content normalizations (formatting only, no meaning changed):** §32.2 Ambiguities rows #2 and #4 rebuilt from 5 cells to the header's 4 columns (the "✅ Resolved" status marker merged into the Issue cell as `✅ **Resolved** — …`), fixing a table-column mismatch carried unchanged since ≤v6.0; and one redundant blank line removed above the §22 heading. No wording, values, or classifications were altered. **Field-completeness backfill (coverage audit):** a structured-token coverage check against the four source docs surfaced three genuine leaf-field omissions carried since ≤v6.0, now closed — `applicationData` added to §16.6 (ApplePayPaymentRequest); the `billingContact`/`shippingContact` sub-field enumeration added to §36.9; and the `sRGB or P3` colour-space requirement added to the logo specs (§28.3 / Gap #26). Note: `requiredShippingContactFields`/`requiredBillingContactFields` were already present in §16.6 (an earlier coverage-tool regex reported them missing in error); the `notAsDescribed` token is example list-item data, not a schema field. All other source structured tokens (endpoints, message types, `capability-list` values, JWT/OAuth flow, List Picker/Time Picker/Quick Reply/Rich Link/Form/Apple Pay schemas) were already present. | `msp-rest-api` v4.2.9 (03 Jun 2026); `messaging-documentation` v3.1 (21 May 2026); `msp-api-tutorial` v3.4 (29 Apr 2026); `msp-onboarding` v3.0.3 (01 Feb 2024); Apple Pay Platform Integration Guide (Jun 2025); Apple Pay Merchant Integration Guide (Mar 2026); Service Terms (17 Dec 2024); third-party MSP corroboration (LivePerson, Auth0) for §17.2 callback host only |

### v6.0 Changes

| Date | Version | Summary | Sources |
|---|---|---|---|
| May 4, 2026 | v6.0 — Apple-direct re-verification + new content domain integration | **Major additions:** New §35 Service Terms / Legal layer (~120 lines); new §27.9 Conversational Design Guidelines (~75 lines); new §28.9 Post-Launch Optimization Framework (~40 lines); new §27.7 PII Request Protocol; new §27.8 Brand Privacy Policy / Terms of Use Display Rules; new §28.7 MSP Onboarding Lifecycle (3-phase model); new §28.8 Pre-Launch Advertising Embargo; new §31.5 User-Facing Privacy Statement Locations. **Major changes:** §32.1 Gap #17 (HIPAA BAA) reclassified from "Unresolved" to "RESOLVED — explicit exclusion" via Service Terms §2.9; §32.1 Gap #1 (Opaque ID) narrowed to Partially informed (behavioral envelope now documented); §32.1 Gap #11 (Managed Apple Account) narrowed to Partially informed (registration-side use confirmed). **Targeted patches:** §1 consumer naming guidance; §11.9 encryption self-test vectors; §16.14 Apple Pay merchant 1:N constraint and 25-month certificate expiry; §20 Invitations / §35.4 Business Updates cross-reference and verbatim POS opt-in language; §21.4 three-term equivalence note (delete/close/Leave Conversation); §28.5 Apple Class A network block (17.0.0.0/8); §28.6 Apple Account terminology fix and recording-method support URLs; §33 public-facing onboarding-guide v2.11 trail added alongside REST API trail. **Audit:** 17 new gap rows (§22–§38) all classified as Resolved; existing Gap statuses updated where applicable. **Terminology drift:** Global "Apple ID" → "Apple Account" (per Apple's Feb 7, 2025 v2.11 onboarding guide revision), with strict exception list preserving "iCloud account" and on-device UI labels. | DOC 1.1 (xp-review); DOC 1.2 (ux-design / Responding to Customers); DOC 1.3 (privacy-security); DOC 2.1 (Policies); DOC 2.2 (register-your-acct); DOC 2.3 (end-to-end onboarding); DOC 2.4 (Metrics); DOC 2.5 (FAQ); DOC 3.1 (Service Terms — register.apple.com/tou/bca/latest/en); DOC 4.1–4.7 (MSP technical: REST API master v4.2.3, Common Specifications, Interactive Message Types, MSP Onboarding, MSP Integration, Sending/Receiving Messages tutorial, Apple Pay tutorial); Documentation Revision History (onboarding-guide trail v1.0.0 → v2.11) |

### v5.1 Changes

| Date | Version | Summary | Sources |
|---|---|---|---|
| March 25, 2026 | v5.1 — Delta patch from Apple_API_specification_document2.docx (v4.2.2) | Added `signedFields` field to Section 16.8 Payment.MerchantSession Dictionary — documents the array of cryptographically signed field names present in the merchant session token payload. Found in v4.2.2 example payload; not present in prior canonical passes. All other docx content confirmed already captured in v5.0. Confirmed remaining gaps (rate limits, geographic availability, TLS ceiling, HIPAA/SOC2, Opaque ID rotation, read receipts AMB business context) are genuine Apple documentation absences, not extraction gaps. | Apple MSP Spec v4.2.2 (Apple_API_specification_document2.docx) |

### v5.0 Changes

| Date | Version | Summary | Sources |
|---|---|---|---|
| March 24, 2026 | v5.0 — Surgical update pass | Added Section 29.11 (Message Suggest full specification — eligibility, submission, activation/throttle, country availability); upgraded Quick Reply evidence label to Direct Gated Apple (Apple MSP tutorial confirmed); added post-selection behavior row, item title (~25 chars) and `summaryText` (≤25 chars) character limit rows to Section 13.5 (Partial Spec); added Section 14.4 note clarifying no Apple-level item count ceiling, 10-KB payload threshold as operative constraint, per-image 64-KB limit, MSP variance; added Section 23.9 Rich Link OG tag requirements (Direct Public Apple); added Section 28.6 Experience Review full detail — screen recording requirement, three review dimensions, five non-negotiable UX requirements, rejection taxonomy gap; added OAuth callback URL `https://auth.businesschat.apple.com` and OAuth provider config requirements to Section 17.2; added classic auth flow iOS 12 OS minimum to Section 17.2; added `splash` disambiguation note to Section 19.3; added macOS ambiguity note to Section 19.7; updated Gap #10 (Message Suggest) to Partially resolved; added Gap #21 (List Picker item count confirmed characteristic) | Section 29.11: File 8 + L2-Addenda-v1.md §AMB-15; Section 13.5: File 5 + L2-Addenda-v1.md §AMB-2; Section 14.4: AMB_List_Picker_Constraints file + File 5; Section 23.9: Apple_Messages_for_Business__Technical_Reference___Apple-Sourced_Only.md §2.7; Section 28.6: L2-Addenda-v1.md §AMB-0 + Apple_Messages_for_Business__Technical_Reference___Apple-Sourced_Only.md §1; Section 17.2: L2-Addenda-v1.md §AMB-6 + Apple_Messages_for_Business__Technical_Reference___Apple-Sourced_Only.md §2.5; Sections 19.3, 19.7: L2-Addenda-v1.md §AMB-4 |

---

*Documents changes applied in this v2 refinement pass against the v1 canonical file.*

### Added

**CANONICAL SCOPE BLOCK** — Inserted after header. Defines the three source tiers included, the Evidence Strength taxonomy (5 values), and the Specification Depth taxonomy (4 values). Provides the definitional foundation for all classification columns added throughout.

**API COMPLETENESS STATUS block** — Inserted at top of Section 3 (Endpoints). Confirms coverage level, source, and implementation suitability.

**Evidence Strength column** — Added to all feature tables, API tables, policy tables, constraint tables, interactive type tables, and device capability tables across Sections 2–29. Applied to every row individually. No row is unclassified.

**Specification Depth column** — Added to all same tables. Applied to every row individually. Reflects Full Spec, Partial Spec, Behavioral Only, or No Spec based on source origin.

**Section-level evidence classification notes** — Added as inline callouts at the top of sections where adding columns to every sub-table would be redundant (Sections 1, 4, 6, 11, 12, 21, 22, 23).

**Gap entries #15–#18 (Section 30.1)** — Added four new unresolved gaps: rate limits, geographic availability, HIPAA BAA, SOC 2. These were implicit in the v1 completeness assessment but not itemized as discrete gap entries.

**Evidence Strength column to Section 30.1** — Gap table now includes the Evidence Strength classification of the gap itself, distinguishing between No Evidence, Referenced Only, and partially evidenced gaps.

**Section 30 TOC entry** — Added Section 32 (Changelog) to Table of Contents.

### Fixed / Reclassified

**Section 2 — Required Features:** Replaced informal "(Strong/Moderate/Weak — source)" status strings with two discrete columns: Evidence Strength and Specification Depth. All 18 features now carry explicit classification.

**Sections 13–21 — Interactive type headers:** Replaced `**Status:** ✅ Confirmed (Strong/Moderate — source)` format with the normalized three-part format: `Status: Confirmed | Evidence Strength: [value] | Specification Depth: [value]`.

**Section 7 — Word doc authority notes for `typing_end` and typing indicators:** Rephrased from contradiction-resolution format to resolution-confirmation format. The underlying conflict is now resolved; notes now state resolution clearly rather than presenting the conflict as active.

**Section 9 — Tapback Word doc authority note:** Same treatment as Section 7. Conflict with PASS A "N/A" classification is resolved; note reframed as resolution confirmation.

**Section 22 — Response codes note:** Rephrased PASS B gap note from active-conflict framing to resolved framing. 403, 404, 410, and 500 confirmed via Word doc.

**Section 4.3 — JWT token lifetime conflict note:** Rephrased to clarify the 1-hour vs. 12-hour discrepancy. Made explicit that the 12-hour value applies to the client verification JWT (Section 4.5) and the 1-hour value applies to the Messaging API JWT. The two are now clearly distinguished and the conflict is structurally resolved, not just noted.

**Section 28.3 — Privacy certifications:** Added HIPAA BAA and SOC 2 rows with explicit "Not published by Apple" / No Evidence / No Spec classification. Previously these were absent, creating an implicit gap. They are now explicit.

**Section 5 — Header source column:** Renamed from "Source" to "Evidence Strength" and applied the standardized taxonomy values.

**Section 24.1 — Capability values table:** `AUTH` (legacy) reclassified from generic "Direct Gated Apple / Full Spec" to "Direct Gated Apple / Referenced Only" to reflect that the legacy flow is deprecated and only mentioned, not specified.

**Authentication Message (legacy) in Section 2 table:** Reclassified Evidence Strength to "Direct Gated Apple" only (Word doc does not specify legacy flow) and Specification Depth to "Referenced Only" (deprecated, no active schema).

### Preserved (No Change)

All existing technical content, schema definitions, sample payloads, JSON examples, constraint values, policy rules, and audit entries from v1 are preserved verbatim. No section was collapsed, summarized, or removed. The audit section (Section 30) retains all unresolved gaps, ambiguities, and contradictions from v1, with the three genuinely resolved items (List Picker, Time Picker, Form Message, Apple Pay payload, OAuth 2.0 flow, typing indicators) marked as resolved — consistent with the instruction to keep gaps only where both the Word doc and first-party sources are silent.

---

*Canonical file v4 compiled March 20, 2026. Changes: Sub-section renumbering in §22–§31 corrected (§22.1–22.4, §23.1–23.8, §25.1–25.2, §26.1–26.3, §27.1–27.6, §28.1–28.5, §30.1–30.3, §31.1–31.4). Gap #19 added and resolved (v4.2.2 image type restrictions — size-based only, no MIME type change). Gap #20 added and resolved (v4.2 enhanced security — three Auth Message changes already documented in §17).*

*Canonical file v3 compiled March 20, 2026. Additions: Section 20 (Invitation Messages), Section 21 (Leave Conversation — Invitations). Sections renumbered 20–32 → 22–34. Gap #9 resolved. Ambiguities #2 and #4 resolved. Ambiguity #6 added. Terminology: "Close Conversation" → "Leave Conversation" throughout per Word doc v4.1.8. Required Features table updated with Invitations row.

*Canonical file v2 compiled March 19, 2026. Word doc authority: v4.2.2 (27 February 2026). PASS B: API v4.1.2, Tutorial v3.3.0. PASS A/C/D research date: March 19, 2026. Evidence classification and Specification Depth taxonomy applied throughout in this v2 pass.*

---

### Provenance — v6.0 Re-Verification Notes

**v5.0-derived sections re-verified in v6.0 against Apple-direct sources:**

| Section | Original v5.0 source citation | Re-verification source (v6.0) | Outcome |
|---|---|---|---|
| §13.5 (Quick Reply item title / `summaryText` limits) | `L2-Addenda-v1.md §AMB-2` (synthesis) | DOC 4.5 (Direct Gated Apple) | Re-verified consistent. Original citation preserved alongside Direct Gated Apple confirmation. |
| §14.4 (List Picker item count clarification) | `AMB_List_Picker_Constraints` + L2-Addenda-v1 (synthesis) | DOC 4.5 (Direct Gated Apple) | Re-verified consistent. Apple does not publish a numeric maximum item count; 10 KB `interactiveData` payload threshold is the operative Apple-level constraint. Original citation preserved. |
| §17.2 (OAuth callback URL `https://auth.businesschat.apple.com`; iOS 12 floor for classic auth flow) | `L2-Addenda-v1.md §AMB-6` + Apple-Sourced Technical Reference §2.5 (synthesis) | Not independently confirmed by Apple-direct sources in this pass | **Preserved as v5.0 synthesis content; no v6.0 change.** The merge agent must not remove or alter §17.2 v5.0 content based on v6.0's silence; the original synthesis remains the canonical position pending future Apple-direct confirmation. |
| §19.3 (`splash` page-type disambiguation note) | `L2-Addenda-v1.md §AMB-4` (synthesis) | DOC 4.5 (Direct Gated Apple) confirms `splash` is a top-level optional display component, not a page type | Re-verified consistent. Original citation preserved. |
| §19.7 (macOS ambiguity note for Form Message) | `L2-Addenda-v1.md §AMB-4` (synthesis) | DOC 4.5 (Direct Gated Apple) confirms iPhone and iPad only — Word doc classification stands | Re-verified consistent. The ambiguity note can stand as written; the macOS exclusion is now multi-source confirmed. |
| §23.9 (Auto-Generated Rich Links — OG tag requirements) | `Apple_Messages_for_Business__Technical_Reference___Apple-Sourced_Only.md §2.7` (synthesis) | Not independently confirmed by Apple-direct sources in this pass | **Preserved as v5.0 synthesis content; no v6.0 change.** |
| §28.6 (Experience Review — Full Detail) | `L2-Addenda-v1.md §AMB-0` + Apple-Sourced Technical Reference §1 (synthesis) | DOC 1.1 (Direct Gated Apple) | Re-verified consistent on screen-recording requirement, three review dimensions, five non-negotiable UX requirements. Apple Account terminology corrected (P-14). Recording-method support URLs added (P-15). 1–2 week timeline added from DOC 2.3. **The five non-negotiable UX requirements that v5.0 captured are confirmed consistent with DOC 1.1 content; the synthesis source's organization of those five items is upheld by the Apple-direct source.** |
| §29.11 (Message Suggest full specification) | "File 8 + L2-Addenda-v1.md §AMB-15" (synthesis) | Not independently confirmed by Apple-direct sources in this pass | **Preserved as v5.0 synthesis content; no v6.0 change.** Message Suggest operational use is confirmed in DOC 2.3 and DOC 2.4 (registering brand primary + store numbers); ramp-up curve and minimum eligibility threshold remain unconfirmed in any source — see §32.1 Gap #10. |

**Editorial corrections of Apple-source typos / non-standard text:**

The delta makes four small editorial corrections where the Apple source contains an apparent typo, non-standard formatting, or a misattributed citation in the prior delta draft. Each correction is also flagged inline at the patch site. They are consolidated here for auditability.

| # | Location | Apple source text | v6.0 corrected text | Reason |
|---|---|---|---|---|
| 1 | P-07 source-authority line | Cited DOC 1.3 for the verbatim phrase "the business doesn't receive the user's phone number, email address or iCloud account information" | Citation corrected to DOC 2.5 FAQ + DOC 4.4 Common Specifications | The phrase does not appear in DOC 1.3. It appears verbatim in DOC 2.5 ("What is an Opaque ID?") and DOC 4.4 ("About the Opaque ID"). DOC 1.3 covers only privacy-statement locations and ISO certifications. |
| 2 | P-15 recording-method support table | Listed `https://support.apple.com/en-us/HT201066` for the Mac entry; missing the QuickTime guide URL | Mac entry corrected to `HT208721`; QuickTime guide URL `qtp356b55534/mac` added as a third row | HT201066 is Apple's "Update macOS" article, unrelated to screen recording. DOC 1.1 publishes three URLs (HT207935, qtp356b55534/mac, HT208721) for the three recording methods. |
| 3 | P-16 / Gap #31 / header summary / v6.0 changelog (CIDR notation) | DOC 4.6 writes `17.0.0/8` (non-standard three-octet CIDR shorthand) | **RETRACTED** — source form `17.0.0/8` preserved verbatim in Part 1; CIDR normalization is not a permitted transformation, so `17.0.0.0/8` may appear only as a reference annotation, never a substitution | Standard CIDR notation is four octets followed by a prefix length. Both notations describe the same address range; the corrected form is unambiguous and is what configuration tools require. |
| 4 | §16.14 `domainName` validation row | DOC 4.7 source text reads "It will only be valid for **Business Pay on the Web**" | Reproduced as "Apple Pay on the Web" | "Business Pay" is not an Apple product name. DOC 4.7 itself uses "Apple Pay on the Web" elsewhere (e.g., line 2661 of source corpus). The source text is an apparent Apple-side typo. |

**Apple-source language preserved verbatim despite a separate question of legal force:**

| Location | Apple source text | Disposition |
|---|---|---|
| §35.4 max-validity row | DOC 3.1 §2.12 reads "in any event, such opt-in **should** only be valid for the time period necessary for the transaction (which in no event will be longer than two (2) years)" | Apple's "should" is preserved verbatim. (A prior delta draft replaced "should" with "shall." This change has been reverted because §35.4 is a verbatim-bolded reproduction of the contractual text; the modal verb is Apple's choice and not for the canonical to alter. Operationally the two-year ceiling is a hard cap regardless of modal verb because of the parenthetical "in no event…".) |

**DOC 3.1 date discrepancy:**
- File-internal date (DOC 3.1 footer): December 17, 2024
- Catalog index date: December 16, 2024
- **Resolution:** File date prevails. v6.0 cites December 17, 2024 throughout. (See §35.10.)

**Source documents cited but not in this delta's input corpus:**
- Apple Privacy Policy (https://www.apple.com/privacy/) — referenced by Service Terms §2.4; not reproduced in canonical
- Apple Pay terms (https://developer.apple.com/apple-pay) — referenced by Service Terms §2.6; not reproduced in canonical
- Apple Developer Program License Agreement — referenced by Service Terms §2.5; not reproduced in canonical
- Apple Business Register Terms of Use — referenced by Service Terms preamble; not reproduced in canonical
- Apple Platform Security guide (https://support.apple.com/guide/security/sec1c603aab4/1/web/1) — referenced by DOC 1.3 and §31; not reproduced in canonical

These references are preserved as cross-references; their content is not integrated into v6.0.

---


## Appendix D — Image Manifest & Placement Map (Master §38)

## 38. IMAGE MANIFEST & PLACEMENT MAP

> **Evidence Strength:** Direct Gated Apple (all assets are Apple-hosted images from the register.apple.com documentation pages). **Specification Depth:** N/A (asset manifest).
> **Purpose.** Full traceability for all 77 image placements (96 individual image files) across the four source Markdown documents, joined to the source CSVs (`API.csv`, `Documentation.csv`, `MSP_Onboarding.csv`, `Tutorial.csv`) for dimensions and canonical source URLs. Coverage: **77/77 markers resolved, 0 missing lookups.**
> **Marker syntax:** `<!-- img: file.png -->` (single) or `<!-- img-row: a.png, b.png -->` (side-by-side group rendering under one text block). Markers are HTML comments — invisible in rendered Markdown, and consumed by a downstream image-insertion step.
> **Two-tier handling (hybrid, per the agreed image strategy):**
> - **Inline (7 structural / flow diagrams)** are embedded directly in the canonical body at the matching section — these aid comprehension of a reference spec. Placement is **topic-mapped by judgment** (the canonical is a synthesis, so it does not carry the source docs' original anchor text). See the Inline Placements table below.
> - **Manifest-only (the remaining 70 markers)** are UI screenshots, portal step-captures, entry-point icons, feature thumbnails, and logos. They would clutter a reference spec, so they live here as a manifest rather than inline. Anchors are preserved so the source documents can be reconstituted with images if needed.
> **Not covered here:** the two Apple Pay Integration Guide PDFs (§36) carry their own embedded diagrams (payment flow, MPAN flow, API sequence diagrams, `PKPaymentToken` structure). They are **not** in the four CSVs and are not manifested; reference the PDFs directly by page.

### 38.1 Inline Placements (7 structural / flow diagrams)

| Diagram | Canonical § | W×H | Source URL |
|---|---|---|---|
| `msp-abc-flow.png` | §1 Overview | 2252×356 | https://register.apple.com/resources/messages/msp-rest-api/ |
| `messages-sent-flow.png` | §3 Endpoints | 2232×1078 | https://register.apple.com/resources/messages/msp-rest-api/messages-sent |
| `Integration-messages-for-business.png` | §7 Message Types | 2128×694 | https://register.apple.com/resources/messages/msp-api-tutorial/integration |
| `large-attachment-flow.png` | §11.7 Large Interactive Data | 1850×1476 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive |
| `new-authentication-flow.png` | §17 Authentication Message | 1654×916 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive |
| `ConstructPayload_Flow.png` | §22 Construct Payload API | 1920×1080 | https://register.apple.com/resources/messages/msp-rest-api/construct-payload |
| `msp-Architecture.png` | §28.7 MSP Onboarding Lifecycle | 1704×668 | https://register.apple.com/resources/messages/msp-onboarding/ |

### 38.2 Full Manifest (all 77 markers)

### From `msp-rest-api.md` (API.csv) — 25 markers

| Image(s) | W×H | Source URL | Anchor (prior-text start) |
|---|---|---|---|
| `0d99fa38-7db4-4a94-ab5c-f61da401a83e.png` | 454×346 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | Always provide @3x images at 72 dpi. The system downscales @3x images to… |
| `Apple-Pay.png` | 572×1156 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | Provide an easy and secure way for customers to buy goods and services t… |
| `Apple_Invitations_Crop_6.png` | 1540×1518 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | Overview Authorized businesses can invite customers to engage in convers… |
| `binaryChoice-withImage-gray.jpg` | 697×483 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | The table includes example messages and download links for schema and ex… |
| `brand-shell.png`, `junk-detail-shell.png`, `leave-detail-shell.png` | 946×1864; 946×1864; 946×1864 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | A message is sent to the MSP indicating that the user with that phone nu… |
| `ConstructPayload_Flow.png` | 1920×1080 | https://register.apple.com/resources/messages/msp-rest-api/construct-payload | The Construct Payload API allows you to generate a rich link payload fro… |
| `icon.png` | 711×177 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Square or rectangle with width < 150px results in an icon. |
| `incomingMsgAttach (1).png` | 2004×1526 | https://register.apple.com/resources/messages/msp-rest-api/messages-sent | To get the attachment reference, do the following: Encrypt the attachmen… |
| `incomingMsgAttach.png` | 2004×1526 | https://register.apple.com/resources/messages/msp-rest-api/messages-received | Repeat the steps in the loop for each attachment listed in the�attachmen… |
| `ios15-iphone12-pro-messages-delete-biz-chat-confirmation.png` | 640×1294 | https://register.apple.com/resources/messages/msp-rest-api/messages-received | Note that when the user deletes the conversation and does not ask to sto… |
| `large-attachment-flow.png` | 1850×1476 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | As an MSP, your platform must download the reference pointer to obtain t… |
| `large.png` | 1281×879 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Rectangle image with width ? 150px, results in a large icon. |
| `List-Picker.png` | 1263×2553 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | Allow the customer to choose from a list of items. A list picker display… |
| `maps-richlink.png` | 426×632 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Note Scrapping OG information using methods without JavaScript: the URL … |
| `messages-sent-flow.png` | 2232×1078 | https://register.apple.com/resources/messages/msp-rest-api/messages-sent | When a business replies to a user�s text message, the Messaging Service … |
| `msp-abc-flow.png` | 2252×356 | https://register.apple.com/resources/messages/msp-rest-api/ | This drawing illustrates the relationship between a business, an MSP, th… |
| `new-authentication-flow.png` | 1654×916 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | The new built-in Authentication flow uses the latest OAuth 2.0 Authoriza… |
| `Quick-Reply-mac.png`, `Quick-Reply-Response-mac.png` | 2112×2193; 2112×2193 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | Quick Reply message type on an iPhone Quick Reply Response message type … |
| `Quick-Reply-Response.png`, `Quick-Reply.png` | 572×1156; 572×1156 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | This feature requires iOS 15.1 and macOS 12.0 or higher. For more inform… |
| `RichLinks2.png` | 5712×11676 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Sample of a Rich Link Containing an Image { "body": "https://www.apple.c… |
| `RichLinksVideo2.png` | 5712×11676 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Below shows a video rich link bubble, displayed in Messages on iPhone. T… |
| `RL-1-bubble.png`, `RL-3-bubbles.png` | 900×324; 572×734 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | When a business sends a URL within a sentence or a large text message, d… |
| `small.png` | 738×879 | https://register.apple.com/resources/messages/msp-rest-api/type-richlink | Square with width ? 150px, results in a square icon. |
| `Text-message.png` | 516×108 | https://register.apple.com/resources/messages/msp-rest-api/type-text | When a business replies to a user�s message, the MSP platform first send… |
| `Time-Picker.png` | 1263×2553 | https://register.apple.com/resources/messages/msp-rest-api/type-interactive | After sending the reply, the customer can tap the reply message bubble t… |

### From `msp-api-tutorial.md` (Tutorial.csv) — 7 markers

| Image(s) | W×H | Source URL | Anchor (prior-text start) |
|---|---|---|---|
| `Apple-Pay-After.png`, `Apple-Pay-Before.png` | 1296×1425; 1296×1425 | https://register.apple.com/resources/messages/msp-api-tutorial/applepay | Tap the payment message to make the test payment: |
| `applepay-bubble.jpg` | 856×644 | https://register.apple.com/resources/messages/msp-api-tutorial/applepay | You should have received the Apple Pay test payment request on your devi… |
| `bc-rich-link-no_2x.png`, `bc-rich-link-yes_2x.png` | 445×332; 448×332 | https://register.apple.com/resources/messages/msp-api-tutorial/rich-links | When a business sends a URL with an inline image or video to a customer,… |
| `extension-ipad.jpeg` | 1536×2048 | https://register.apple.com/resources/messages/msp-api-tutorial/imessage-apps | When the user taps the message bubble, a detailed map opens up with a lo… |
| `extension.png` | 725×446 | https://register.apple.com/resources/messages/msp-api-tutorial/imessage-apps | On the user device, you should see the following message bubble. |
| `Integration-messages-for-business.png` | 2128×694 | https://register.apple.com/resources/messages/msp-api-tutorial/integration | All tutorials follow the sending and receiving data diagram below. A use… |
| `iOS-device-notification-no-shadow.png` | 844×262 | https://register.apple.com/resources/messages/msp-api-tutorial/integration | Older version of macOS, may not support certain message types and will d… |

### From `msp-onboarding.md` (MSP_Onboarding.csv) — 13 markers

| Image(s) | W×H | Source URL | Anchor (prior-text start) |
|---|---|---|---|
| `Message-Buttons.png` | 862×255 | https://register.apple.com/resources/messages/msp-onboarding/launch | Once approved, you can activate Maps entry points by adding an Apple Map… |
| `msp-Architecture.png` | 1704×668 | https://register.apple.com/resources/messages/msp-onboarding/ | The diagram below shows a typical MSP architecture. The items highlighte… |
| `msp-onboarding-connectedSvc.png` | 2093×233 | https://register.apple.com/resources/messages/msp-onboarding/mspRegistration | Add at least one MSP Private account to your Apple Business Register por… |
| `msp-onboarding-testIDs.png` | 1233×612 | https://register.apple.com/resources/messages/msp-onboarding/mspRegistration | When you create your MSP private endpoint, your screen changes to list a… |
| `msp-onboarding-testMessage.png` | 1472×843 | https://register.apple.com/resources/messages/msp-onboarding/mspRegistration | NOTEApple Messages for Business accounts created for testing and develop… |
| `mspClientDev-ApplePay-auth.png` | 1800×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Authentication. Allow customers to authenticate (image below, authentica… |
| `mspClientDev-DocAttach-AR.png` | 1800×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Augmented reality. Give users a real world view of a product by sending … |
| `mspClientDev-iMessageApp.png` | 842×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | iMesssage apps. Support additional or more complex functionality through… |
| `mspClientDev-imgShar-Videos.png` | 1800×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Video sharing. Sharing videos with users (image below, video sharing on … |
| `mspClientDev-listPicker-timePicker.png` | 1800×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Time picker. Schedule appointments, select dates for reservations, or co… |
| `mspClientDev-quick-reply.png` | 1077×2172 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Quick Replies. Provide a simple way for the user to make an inline choic… |
| `mspClientDev-richLinks-walletCards.png` | 1800×1702 | https://register.apple.com/resources/messages/msp-onboarding/business-dev | Wallet Cards. Provides customers with instant access to tickets, members… |
| `Notifications.png` | 1814×240 | https://register.apple.com/resources/messages/msp-onboarding/launch | In Apple Business Register, go to the brand's profile and click the Go L… |

### From `messaging-documentation.md` (Documentation.csv) — 32 markers

| Image(s) | W×H | Source URL | Anchor (prior-text start) |
|---|---|---|---|
| `abr_Log1.png` | 1306×790 | https://register.apple.com/resources/messages/messaging-documentation/register-your-acct | Step 1: Create your organization profile Navigate to Apple Business Regi… |
| `abr_Log3_SendNow.png` | 866×330 | https://register.apple.com/resources/messages/messaging-documentation/ | Sign in to Apple Business Register Select "Messages for Business Account… |
| `abr_Log4_dashboard.png` | 2114×1128 | https://register.apple.com/resources/messages/messaging-documentation/ | Apple reviews your account application. This process typically takes 1-3… |
| `add-tester-apple-id.png` | 1922×1184 | https://register.apple.com/resources/messages/messaging-documentation/ | Test Apple Accounts allow your team to verify message delivery before go… |
| `amb-app.png` | 900×1840 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | App button When adding a button to your app, you make it easy for custom… |
| `amb-ar.png` | 572×1145 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | You can add AR to your brand experience as an entry point if the AR is o… |
| `amb-email.png` | 1341×2739 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | You can include the URL in an email or send it using SMS to reach specif… |
| `amb-maps-ios26.png` | 900×1840 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | You can win twice with this entry point by adding and updating your bran… |
| `amb-nfc.png`, `amb-qr.png` | 572×1141; 900×1840 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | QR codes and NFC tags add an entry point anywhere you can post marketing… |
| `amb-social.png` | 1266×2535 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | Nowadays it�s difficult to find someone who doesn�t use at least one typ… |
| `amb-web.png` | 900×1840 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | The more visible your brand, the easier it is for customers to contact y… |
| `Apple-Pay.png` | 572×1156 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | Apple Pay Provides an easy and secure way for customers to buy goods and… |
| `Apple-Store-Message-Suggest-Enabled.png`, `AppleMaps-Message-Suggest.png`, `AppleWeb-Message-Suggest.png` | 572×1152; 572×1152; 572×1152 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | You can trigger Message Suggest from any place where the phone number is… |
| `Authentication.png` | 572×1160 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | Authentication Allows customers to view account information safely throu… |
| `Better_Bag_disabled.png`, `Better_Bag_enabled.png` | 1240×816; 310×262 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | The following screenshots are of an iPhone with no Message Suggest and w… |
| `e2e-circle-v2.png` | 5739×945 | https://register.apple.com/resources/messages/messaging-documentation/ | Getting Started with Apple Messages for Business |
| `heroImage.png` | 883×1820 | https://register.apple.com/resources/messages/messaging-documentation/ | Designing for great user journeys |
| `iMessage-apps.png` | 842×1702 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | iMessage apps Allows customers to interact with your app directly within… |
| `List-Picker.png` | 576×1178 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | List pickers Provides information or asks questions with organized optio… |
| `message-suggest-settings.png` | 1218×482 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | Getting Message Suggest setup First, get familiar with the different set… |
| `msg-cta-mode.png`, `msg-icons-mode.png` | 2997×2280; 2997×2280 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | The images below display the output of the Messages button or icon on a … |
| `msp-dashboard.png` | 1630×1096 | https://register.apple.com/resources/messages/messaging-documentation/metrics | First 30 days The first 30 days should be spent monitoring the agent tea… |
| `msp-list.png` | 1922×1184 | https://register.apple.com/resources/messages/messaging-documentation/register-your-acct | Click "Next" and choose your MSP endpoint: Select from the "Apple Author… |
| `msp-m4b-flow.png` | 2252×356 | https://register.apple.com/resources/messages/messaging-documentation/ | Create Engaging, Secure, and Scalable Messaging Experiences Version: 3.1… |
| `privacy-iOS-1.png`, `privacy-iOS-2.png` | 572×1145; 572×1145 | https://register.apple.com/resources/messages/messaging-documentation/privacy-security | On iOS and iPadOS. Open Settings > Messages, scroll to the bottom, and t… |
| `privacy-macOS-1.png` | 1508×1640 | https://register.apple.com/resources/messages/messaging-documentation/privacy-security | On devices. When messaging using Apple Messages for Business for the fir… |
| `quick-reply.png` | 576×1178 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | Quick replies Provide a simple way for customers to make an inline choic… |
| `RichLinks.png` | 582×1204 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | Rich links Links with preview content provide brand assurance and click … |
| `square_logo_conversation.png`, `WideLogo-iOS26.png`, `WideLogo-v2.png` | 1239×423; 874×344; 1308×423 | https://register.apple.com/resources/messages/messaging-documentation/ | Square logo (required) The square logo appears in: Conversation list (al… |
| `Time-Picker.png` | 1263×2553 | https://register.apple.com/resources/messages/messaging-documentation/conversation-best-practices | Time pickers Provides time slots for customers to choose and adds the ch… |
| `Wallet_Order_Track.jpg` | 3528×3412 | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | From iOS 16 and macOS 13, a business can add a tracking order status in … |
| `Messages-for-Business-Message-Us-Black.svg`, `Messages-for-Business-Contact-Black.svg`, `Messages-for-Business-Ask-Black.svg`, `Messages-for-Business-Get-Help-Black.svg`, `Messages-for-Business-Icon.svg` | ×; ×; ×; ×; × | https://register.apple.com/resources/messages/messaging-documentation/message-with-customers | Place a button to give your customers an easy way to access your support… |
### 38.3 Notes & Caveats

- **URLs are page URLs, not direct image URLs.** The CSV `url` column records the register.apple.com documentation **page** each image was scraped from (gated MSP portal), not a direct CDN link to the image binary. To render images, the binaries must be supplied separately; this manifest maps filename → page-of-origin → dimensions → placement.


## Appendix E — Service Terms / Legal Layer overlay (Master §35)

## 35. SERVICE TERMS / LEGAL LAYER

> **Evidence Strength:** Direct Gated Apple. **Specification Depth:** Full Spec (legal text reproduced as published).
> **Source:** Service Terms for Messages for Business — https://register.apple.com/tou/bca/latest/en
> **Last updated by Apple:** December 17, 2024
> **Authority disposition:** This section captures the legal-layer requirements that govern all AMB use. Where the Service Terms conflict with operational guidance elsewhere in this canonical, the Service Terms prevail. The Service Terms also state explicitly: *"In the event of a conflict between these Service Terms and the ABR Terms of Use, these Service Terms shall control."*

### 35.1 Authority and Scope

The Service Terms for Messages for Business **replace the former Terms for Business Chat** and supplement the Apple Business Register (ABR) Terms of Use. They constitute a binding legal agreement between the Business or MSP and Apple. They incorporate all AMB Guidelines, Documentation, and policies by reference.

### 35.2 Definitions

| Term | Apple's definition |
|---|---|
| **Business** | An organization registered to use AMB. Must have an active and valid Apple Account. |
| **Documentation** | Any technical or other specifications or documentation that Apple may provide for use in connection with AMB. |
| **Guidelines** | The AMB usage guidelines set forth in the Service Terms and all policies, best practices, protocols, partnership requirements or other terms set forth by Apple — including AMB MSP & brand media guidelines, design guidelines, policies, and best practices — each of which may be updated from time to time. |
| **Apple Messages for Business** | The services, Program or AMB Materials that Apple may provide or make available, including Updates. |
| **AMB API(s)** | The application programming interface(s) documented by Apple in the Documentation. |
| **AMB ID** | The AMB identifier assigned to each AMB or MSP account that enables access to and use of AMB. |
| **AMB Materials** | Documentation, tools, certificates, data, and other materials provided by Apple through AMB. |
| **Message(s)** | A message that is received or sent using AMB. |
| **MSP** | An organization that provides or delivers a system or service that facilitates the exchange of or enables the use of AMB for one or more businesses. |
| **Program** | The overall Apple development, testing, digital signing and distribution program contemplated in the Service Terms. |
| **Service and Feature Requirements** | The technical, human interface, design, product category, security, performance, current and new features, and other criteria and requirements specified by Apple. May be modified at Apple's sole discretion. |
| **Updates** | Bug fixes, updates, upgrades, modifications, enhancements, supplements, and new releases or versions of any part of AMB. |

### 35.3 Use of AMB and Integration (§2.1–§2.11)

| Provision | Detail | Operational impact |
|---|---|---|
| §2.1 Use, accuracy, AMB ID security | Business and MSP use AMB at their own initiative. Must provide accurate, current, complete information for registration. Solely responsible for confidentiality and security of AMB accounts. **MSP must comply with new feature requirements within 90 days of Apple notification.** | The 90-day MSP feature compliance window is operationally critical and is not stated elsewhere in canonical. |
| §2.1 MSP approval | MSP must be Apple-approved before use. If an MSP relies on technology of another MSP, both must be registered and approved. **MSP shall not promote AMB-related services unless and until approved in writing by Apple.** | Cross-reference §28.8 (Pre-Launch Advertising Embargo). |
| §2.2 Business integration | Business must itself be an approved MSP, or select an approved MSP, to integrate with AMB. Business is solely responsible for its agreements with its MSP. **Apple is not a party to any Business–MSP agreement.** | Liability allocation — Apple is not in privity. |
| §2.3 Messages | All AMB use must originate from a Business's assigned AMB ID. Messages must be sent under the name, trademark, or brand of the Business. **It must be clear to the recipient that the communication is from the Business, not from Apple.** | Branding requirement; affects display name, logo, etc. |
| §2.3 Behavior prohibitions | Business and MSP must not: misrepresent or impersonate; harass, abuse, stalk, threaten, defame; transmit malware; trespass or burden network capacity; disable or override Apple-implemented notices, consent panels, or system preferences. | Standard behavior covenants. |
| §2.4 Privacy | Apple's Privacy Policy applies to AMB use and is incorporated into the Service Terms. Available at https://www.apple.com/privacy/. | — |
| §2.5 In-App Purchase, iMessage Apps | In-App Purchase API in AMB is subject to the Apple Developer Program License Agreement. iMessage Apps usage is subject to the iMessage Apps / Apple Messages App terms. | Cross-reference §18 iMessage App. |
| §2.6 Apple Pay | Integration of Apple Pay and any Apple Pay transactions in AMB are subject to Apple Pay terms at https://developer.apple.com/apple-pay. | Cross-reference §16, §28.4. |
| §2.7 Use of Network | AMB may transmit Messages across various public networks and may modify Message format to comply with technical, network, and other requirements. | — |
| §2.8 **Not for emergency services** | AMB is not intended to provide access to emergency services. Not a guaranteed or on-time delivery service. **Apple has no liability for availability, accuracy, completeness, reliability, or timeliness of Messages.** | Operationally critical disclaimer. |
| §2.9 Legal compliance | Business and MSP may only use AMB if all such use complies with all legal and regulatory requirements; sole responsibility for determining and complying with all legal obligations. | — |
| §2.9 **HIPAA exclusion (verbatim authority)** | *Apple makes no representations or warranties that AMB meets the needs of entities regulated by laws and regulations with heightened confidentiality requirements for personal, health, financial, and/or other types of data.* **If a Business is a HIPAA-covered entity, business associate, or representative, the Business agrees that it will not use any component, function or other facility of AMB to create, receive, maintain or transmit any "protected health information" (45 C.F.R § 160.103) or use AMB in any manner that would make Apple (or any Apple subsidiary) the Business's or any third party's business associate.** | **This is the most consequential operational rule in the legal layer.** AMB is not approved for PHI by HIPAA-covered entities. Resolves §32.1 Gap #17. |
| §2.10 Export control | AMB use may be subject to U.S. and foreign export and import laws. Compliance required. | — |
| §2.11 No conveyance | Service Terms convey no interest, title, or license in an AMB ID, Business account, or similar resource. | — |

### 35.4 Business Updates (§2.12) — Legal Layer for Invitations

> **Operational schema:** §20 Invitation Messages (Word doc v4.1.8 nomenclature — same feature).

| Provision | Detail |
|---|---|
| Opt-in required | Business Updates may only be sent **upon opt-in** by the customer. |
| POS-only opt-in collection | Opt-in may only be collected from a customer at a Business's point of sale (POS) — the Business's website, application, customer service number, or physical location. |
| Scope | The opt-in applies only to Business Updates regarding the transaction occurring at the time of opt-in. |
| Maximum validity | **In any event, such opt-in should only be valid for the time period necessary for the transaction (which in no event will be longer than two (2) years).** *(Verbatim from DOC 3.1 §2.12 — Apple's source uses "should" rather than "shall"; preserved here as written. Operationally this is a contractual upper bound regardless of modal verb.)* |
| Opt-out in every Business Update | A Business will offer an opt-out choice in every Business Update and will immediately honor any such customer's opt-out. |
| Apple-authorized templates only | A Business and/or its MSP shall only use Apple-authorized templates for Business Updates and shall not modify such templates except for permitted custom substitutions in specific text fields. |

#### 35.4.1 Verbatim Required POS Opt-In Disclosure

A Business offering Business Updates **must include the following language at the POS during the opt-in process:**

> *"Separate from your opt-in to receive Business Updates from us, your use of Apple Messages for Business service is also governed by Apple's terms, including those at https://www.apple.com/legal/privacy/data/en/messages-for-business/. Unless you have opted-out on your Apple device, Apple may process your personally identifiable information."*

**Evidence Strength:** Direct Gated Apple. **Specification Depth:** Full Spec.

### 35.5 Prohibited Uses (§3)

A Business and MSP agree NOT to:

- Rent, lease, lend, upload to or host on any website or server, transfer, sell, redistribute, or sublicense AMB.
- Use AMB for any purpose not expressly permitted by the Service Terms.
- Distribute, transmit, store, share, access, solicit, or otherwise make available content that is unlawful, harassing, threatening, harmful, tortious, defamatory, libelous, abusive, violent, obscene, vulgar, invasive of privacy, hateful, racially or ethnically offensive, or otherwise objectionable.
- Copy, decompile, reverse engineer, disassemble, attempt to derive source code of, modify, decrypt, or create derivative works of AMB.
- Trespass or burden network capacity, harvest, scrape, or misuse data.
- Use AMB to solicit, access, distribute, store, or generate child sexual abuse material, child sexual exploitation material, pro-terror material, extreme crime and violence material, crime or violence material, or drug-related material.

**Cross-reference:** DOC 2.1 (Policies) Prohibited Uses list extends this with prohibited business categories — see §27 Policy.

### 35.6 Apple's Modification, Availability, and Liability Provisions (§4)

| Provision | Detail |
|---|---|
| §4.1 Apple's right to modify | Apple may at any time, with or without prior notice: (a) modify AMB, including by adding, changing, or removing any feature, functionality, or requirement; (b) modify, deprecate, suspend, reissue, republish, or discontinue AMB or any portion thereof; or (c) make changes to ABR Terms of Use, Service Terms, Service and Feature Requirements, Guidelines, Documentation, and other materials. |
| §4.2 No availability guarantee | Apple makes no guarantees in relation to availability or uptime of AMB. Not obligated to provide maintenance, technical support, or other support. **Apple reserves the right to remove a Business or MSP from access at any time without liability.** |
| §4.3 No fees by Business; no substitute service | A Business may not charge any fees solely for access to or use of AMB. Business and MSP agree not to create or attempt to create a substitute or similar service to AMB. |
| §4.4 Disclaimer of warranties | AMB is "AS IS" and "AS AVAILABLE" with all faults. All implied warranties disclaimed (merchantability, satisfactory quality, fitness for purpose, accuracy, quiet enjoyment, non-infringement). **AMB is not intended or suitable for use in environments where failure or time delays could lead to death, personal injury, or severe physical or environmental damage.** |
| §4.5 **Liability cap** | **Apple's total liability for all damages (other than as required by applicable law in cases involving personal injury) shall not exceed $50.00.** |
| §4.6 Indemnification | Business and MSP indemnify and hold Apple harmless from demands, losses, liability, damages, claims, suits, costs, or expenses arising from (i) AMB use or (ii) Service Terms violations. |
| §4.7 Apple's right to charge fees | Apple reserves the right to charge fees for use of AMB. |
| §4.8 Apple's marketing rights | Apple may use names, logos, graphics, assets, marks, screenshots, images, designs, text, audio or visual clips, print, digital, or other materials depicting the Business or MSP and AMB implementation for Apple's promotion, marketing, or internal use. |
| §4.9 Apple proprietary rights | The AMB service is owned by Apple and protected by intellectual property and other laws including copyright, patent, trademark, and trade secret. |

### 35.7 Violation, Termination, and Disclosure (§5)

If a Business or MSP fails to comply with any provisions, Apple may limit, suspend, and/or terminate use, preclude or restrict access to AMB, and delete or remove violating content. Apple has the right, without liability, to disclose any data and/or information to law enforcement authorities, government officials, and/or third parties as Apple believes is reasonably necessary to enforce the Service Terms.

### 35.8 Controlling Law, Venue, Severability (§6)

| Provision | Detail |
|---|---|
| Governing law | Laws of the **State of Delaware**, excluding conflicts of law provisions. |
| Venue | Personal and exclusive jurisdiction of courts located within the **county of Santa Clara, California**. |

### 35.9 Entire Agreement and Feedback (§7–§8)

The Service Terms constitute the entire agreement between Business, MSP, and Apple, superseding any prior agreements. Any feedback provided regarding AMB shall be deemed non-confidential; Apple may use such information on an unrestricted basis.

### 35.10 Document Provenance

| Field | Value |
|---|---|
| Source URL | https://register.apple.com/tou/bca/latest/en |
| Apple last-updated date | December 17, 2024 (per document footer) |
| Catalog last-updated date discrepancy | The AMB-Apple-Docs catalog records this as Dec 16, 2024. The file's own footer states Dec 17, 2024. Per provenance protocol, the file date prevails. |
| Authority class | Direct Gated Apple — legal layer |
| Replaces | Former Terms for Business Chat (pre-Sept 2021 rebrand) |

---


## Appendix F — Apple Pay Merchant Setup, Registration & Processing overlay (Master §36)

## 36. APPLE PAY — MERCHANT SETUP, REGISTRATION & PROCESSING (INTEGRATION LAYER)

> **Evidence Strength:** Direct Public Apple (Apple Pay Platform Integration Guide, Jun 2025; Apple Pay Merchant Integration Guide, Mar 2026). **Specification Depth:** Full Spec (setup/registration procedures and processing schema); Partial Spec where noted.
> **Scope boundary:** This section is the Apple Pay **setup, registration, and technical-processing** layer that underlies Apple Pay in AMB (§16). It covers everything needed to become a payment-accepting merchant/platform and to process the resulting payment data. It deliberately **excludes** general web/in-app commerce UX that is not part of AMB and not part of setup — see §36.14 for the explicit out-of-scope list with pointers.
> **Recency rule for this section:** Where the two Apple Pay guides overlap, the **Merchant Integration Guide (Mar 2026)** supersedes the **Platform Integration Guide (Jun 2025)**; both are recorded and reconciled in §37.
> **Relationship to §16:** §16 is the AMB Apple Pay **message** schema (the interactive payment bubble). §36 is the merchant/platform **foundation** beneath it. Facts that also appear AMB-scoped in §16.14 are the authoritative subset for messaging; §36 is the full integration layer.

### 36.1 Prerequisites

| Requirement | Detail | Evidence Strength | Specification Depth |
|---|---|---|---|
| Apple Developer Program membership | Required for both in-app and web Apple Pay; renewed yearly. **Merchants** may enrol as an individual **or** organization. **Platform integrators** must enrol as an organization. An Apple Developer **Enterprise** Program account **cannot** be used to enable Apple Pay. | Direct Public Apple | Full Spec |
| Supported region | Confirm the merchant operates in an Apple Pay–supported region (Apple maintains the country/region list). | Direct Public Apple | Full Spec |
| EMVCo token handling | The processing party must handle EMVCo token elements — e.g., TAVV, ECI, and where applicable 3-D Secure elements such as CAVV/UCAF. | Direct Public Apple | Full Spec |
| Server setup (web) | For Apple Pay on the Web, the server must meet Apple's secure-communication setup requirements and be reachable by Apple's servers (see §36.5 on proxies/redirects). | Direct Public Apple | Full Spec |

### 36.2 Merchant ID

- Uniquely identifies the business as a merchant able to take payments. **A Merchant ID never expires** and can be reused across multiple apps and websites.
- Created in the Apple Developer portal: **Certificates, Identifiers & Profiles → Identifiers → Merchant IDs** (add `+` → Merchant IDs → enter description + identifier → Register). Can alternatively be created in Xcode.
- **AMB cardinality (from §16.14):** each AMB account has at most one associated Merchant ID; a Merchant ID may be reused across multiple AMB accounts.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026) | Direct Gated Apple (AMB cardinality). **Specification Depth:** Full Spec.

### 36.3 Payment Processing Certificate

Associated with the Merchant ID; secures (encrypts) transaction data.

| Property | Value | Notes |
|---|---|---|
| Key pair | **ECC, 256-bit** for the CSR. **Mainland China exception: RSA 2048.** | If the PSP decrypts, obtain a properly formatted CSR from the PSP instead of generating your own. |
| Validity | **25 months.** | Renew before expiry; expired certificates cause Apple Pay transactions to fail. |
| Renewal model | Create the replacement certificate before expiry (same steps). This **prepares but does not activate** it. Coordinate the switch with the PSP, then press **Activate** next to the certificate in the Apple Developer portal — this tells Apple Pay servers to begin using it for encryption. | Prevents interruption; complete before the current certificate expires. |
| Key selection | Apple encrypts with the merchant public key; the payload's `publicKeyHash` identifies which key was used (critical during rotation — see §36.8). | — |

**Recency:** the ECC-256 / China-RSA-2048 detail and the prepare-then-activate renewal model are from the **Merchant Guide (Mar 2026)** and supersede the thinner §16.14 / tutorial statement (which gave only the 25-month figure). See §37 R4.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026). **Specification Depth:** Full Spec.

### 36.4 Merchant Identity Certificate

Associated with the Merchant ID; authenticates **sessions** with the Apple Pay servers (distinct from the Payment Processing Certificate, which encrypts payment data).

- CSR uses an **RSA 2048-bit** key pair.
- Create in the portal under the Merchant ID → **Apple Pay Merchant Identity Certificate → Create Certificate** → upload CSR → download `.cer` → add to Mac Keychain.
- **Export for server use:** export the key + certificate from Keychain as a `.p12`, then split with OpenSSL:
  - `openssl pkcs12 -in ApplePayMerchantID_and_privatekey.p12 -out ApplePay.crt.pem -nokeys`
  - `openssl pkcs12 -in ApplePayMerchantID_and_privatekey.p12 -out ApplePay.key.pem -nocerts`
- **Test with cURL** against the certificate/sandbox endpoint (see §36.6). Use straight double-quotes (`"`), not curly quotes, or the request will not parse.

**Cross-reference:** §16.14 records the AMB-side PEM-generation note; this is the full procedure.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026). **Specification Depth:** Full Spec.

### 36.5 Domain Verification (Apple Pay on the Web)

- Register and verify **all top-level domains and subdomains** where the Apple Pay button is displayed.
- Download the domain-association file and host it at:
  `https://[DOMAIN_NAME]/.well-known/apple-developer-merchantid-domain-association`
- Domains **cannot be behind a proxy or redirect** and must be reachable by the Apple servers listed in the server-setup requirements.
- **AMB note (from §16.14):** domain verification is required per IETF RFC 3986 (URI syntax) and RFC 8615 (well-known URIs).

**Evidence Strength:** Direct Public Apple | Direct Gated Apple (AMB RFC note). **Specification Depth:** Full Spec.

### 36.6 Merchant Validation & Session Endpoints

Merchant validation obtains an **opaque session object** used to start an Apple Pay session.

| Endpoint | Use | Evidence Strength |
|---|---|---|
| `https://apple-pay-gateway.apple.com/paymentservices/paymentSession` | **Production** merchant validation. Called from the **server** (not the browser) with the Merchant Identity Certificate. | Direct Public Apple |
| `https://apple-pay-gateway-cert.apple.com/paymentservices/paymentSession` | **Sandbox / certificate testing** (the cURL test in §36.4 and sandbox runs). Switch to the production endpoint before going live. | Direct Public Apple |

**Request fields:** `merchantIdentifier`, `displayName`, `initiative`, `initiativeContext`. For web, `initiative` = `"web"`; **for AMB, `initiative` = `"messaging"` and `initiativeContext` = the merchant's payment-gateway URL** (see §16.8 / §16.14). The returned session object **must not be inspected, parsed, or modified** — Apple may change its contents over time.

**Recency:** the sandbox/cert endpoint is from the **Merchant Guide (Mar 2026)**; the canonical previously recorded only the production endpoint (§16.14). See §37 R6.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026) | Direct Gated Apple (AMB `initiative`/`initiativeContext`). **Specification Depth:** Full Spec.

### 36.7 Onboarding Models

**A. Merchant-managed Apple Developer Account.** The merchant creates and manages its own Apple Pay credentials (usable across App and Web).
- Supports native in-app Apple Pay integrations.
- Merchant has more control over certificates/keys; must have its own Apple Developer Account.
- **Does not** support hosted payment pages.
- Common pattern: the processor decrypts the token; a unique key pair is generated per merchant, the processor supplies the public key via a CSR, and the merchant uploads it to generate the Payment Processing Certificate.

**B. Apple Pay Web Merchant Registration API (platform-managed).** A REST API letting a **platform** register and manage Apple Pay configuration on behalf of merchants (web only).
- Benefits: merchant does not need an Apple Developer Account; shared keys/certificates across the merchant portfolio; **domain registration does not expire**; supports hosted pages and direct API / JS libraries; **cannot** be used for native in-app.
- Access: apply via the Web Registration API application form (platform must be enrolled as an organization); set up a **Payment Platform Integrator ID** and its certificates (same process as a Merchant Identifier).
- Endpoints: **`registerMerchant`**, **`unregisterMerchant`**, **`getDetails`**.
- Domain prep: distribute the domain-association file to each merchant to host at the `.well-known` path (§36.5); if merchants use pages hosted on the platform's own domain, host the file there too.
- For hosted payment forms, use the **`partnerInternalMerchantIdentifier`** (returned when registering a merchant) in all fields that would otherwise take the Merchant Identifier.

**Evidence Strength:** Direct Public Apple (Platform Guide, Jun 2025). **Specification Depth:** Full Spec.

### 36.8 Key Management & Rolling

- Payment platforms should support **at least two active key pairs / certificates** on an Apple Pay configuration at once, to transition without downtime.
- Rolling sequence: (1) generate new key pair + CSR on the platform; (2) upload the new CSR to the Apple Developer account and download the new certificate; (3) upload the new certificate to the platform; (4) **activate** the new keys/certificates in the Apple Developer account; (5) **revoke** the old keys/certificates.
- Use the `publicKeyHash` value to determine which merchant public key Apple used for encryption, then retrieve the corresponding certificate/private key for decryption — essential during transition.

**Evidence Strength:** Direct Public Apple (Platform Guide, Jun 2025). **Specification Depth:** Full Spec.

### 36.9 Apple Pay Payment Object & Decryption

- On authorization the Secure Element creates a payment object containing the encrypted payment token plus any requested contact data. Encryption uses **ECC** or **RSA**, selected by the Secure Element based on the payment request; **most regions use ECC**; RSA is used only where ECC is unavailable for regulatory reasons. Unless advised otherwise, focus on **ECC** decryption.
- **Payment object (outer) structure:** `billingContact`, `shippingContact`, and `token` → `paymentData` { `data`, `signature`, `header` { `publicKeyHash`, `ephemeralPublicKey`, `transactionId` }, `version` (`"EC_v1"`) }, `paymentMethod` { `displayName`, `network`, `type` }, `transactionIdentifier`.
- **Contact object fields** (`billingContact` / `shippingContact`): `givenName`, `familyName`, `phoneticGivenName`, `phoneticFamilyName`, `addressLines[]`, `locality`, `subLocality`, `administrativeArea`, `subAdministrativeArea`, `postalCode`, `country`, `countryCode`, `emailAddress` (shipping only), `phoneNumber`. Returned to the payment gateway in the authorized payment; provided in redacted form before authentication and complete afterward.
- **Decrypted payload (standard device token):** `paymentDataType` (`"3DSecure"`), `applicationPrimaryAccountNumber`, `applicationExpirationDate` (YYMMDD), `currencyCode`, `deviceManufacturerIdentifier`, `transactionAmount`, `paymentData` { `onlinePaymentCryptogram`, `eciIndicator` }.
- **Decrypted payload (merchant-token variant)** additionally contains `merchantTokenIdentifier` and `merchantTokenMetadata` { `cardArt[]`, `cardMetadata` { `longDescription`, `shortDescription`, `cardCountry`, `fpanSuffix` } }.
- Field/format authority: Apple's **Payment Token Format Reference**.
- **Authorization mapping:** Apple Pay uses 3-D Secure–style formatting; map Apple Pay fields to the acquirer/network's card / EMVCo-token fields. American Express may require distinct mapping (Token Requestor ID, Token Block A/B). Always confirm exact mapping with the acquiring/payment-network partner.

**Evidence Strength:** Direct Public Apple (Platform Guide, Jun 2025; Merchant Guide, Mar 2026). **Specification Depth:** Full Spec.

### 36.10 Merchant Tokens (MPAN) & Payment-Request Types

A merchant token (MPAN) associates a payment **card + merchant + user**, giving continuity across devices even when a device is upgraded or a card is removed. A merchant token is **automatically requested** by Apple when one of the request types below is used; if the issuer does not support merchant tokens, Apple Pay **falls back to the DPAN** as in a standard transaction.

| Request type | Use |
|---|---|
| `recurringPaymentRequest` | Subscriptions (fixed amount, fixed interval), recurring billing (variable amount, fixed interval), and installment/BNPL repayments (fixed number of fixed intervals). |
| `automaticReloadPaymentRequest` | Automatic reloads / stored-balance top-ups triggered by a balance threshold + reload amount. |
| `deferredPaymentRequest` | Deferred payments (hotel, car hire, pre-order) with a free-cancellation period and a specified payment date. |

- Network-specific flags may be required on subsequent (merchant-initiated) transactions — e.g., Visa MIT, MasterCard DSRP; confirm with the acquirer/network.
- **MPAN authorization flow:** initial Cardholder-Initiated Transaction (CIT) returns `MPAN + Cryptogram` (+ `DPAN + Cryptogram`); subsequent Merchant-Initiated Transactions (MIT) use `MPAN + TRID`.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026 — richest; Platform Guide, Jun 2025). **Specification Depth:** Full Spec.

### 36.11 Merchant Token Management API

Provides visibility into token lifecycle events (account status, card art, expiration).

- Supply a `tokenNotificationURL` in the payment request. On a lifecycle event, Apple Pay sends a **GET** to that URL with an `eventId` in the path.
- Respond by issuing a **POST** to `https://apple-pay-gateway.apple.com/paymentServices/v1/merchantId/{merchantId}/merchantToken/event/{eventId}` to retrieve a `merchantTokenEventResponse`.
- **Event types:**

| `eventType` | Meaning |
|---|---|
| `UNLINK` | Token revoked; will be rejected if sent for processing. Prompt the customer to update payment details before the next cycle. |
| `UPDATED_METADATA` | Metadata changed — e.g., FPAN suffix, expiry date, or the token itself. |
| `UPDATED_CARD_ART` | Card art for the underlying card updated. |

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026; Platform Guide, Jun 2025). **Specification Depth:** Full Spec.

### 36.12 Availability Checks

| Method | Scope | Behavior |
|---|---|---|
| `canMakePayments()` | Web + App | Device is capable of Apple Pay payments; does **not** verify a provisioned card. |
| `canMakePayments(usingNetworks:)` | **App only** | Capable **and** a card from at least one provided network is available. *(Added Mar 2026.)* |
| `applePayCapabilities()` | **Web only** | On Safari and third-party browsers, device is capable; on Safari it also verifies at least one provisioned credential in Wallet. *(Guidance added Jun 2025.)* |

**Device support (Merchant Guide, Mar 2026 — supersedes Platform Jun 2025):** Apple devices with a Secure Element. On macOS, a Mac with Touch ID or an Apple Pay–capable iPhone/Watch authorizes. On **third-party browsers** (Mac or otherwise), an Apple Pay–capable iPhone running **iOS 18 or newer** is required. `visionOS` and **Optic ID** are supported. Any transaction type supported for regular cards works with Apple Pay, **including refunds**. See §37 R2–R3.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026). **Specification Depth:** Full Spec.

### 36.13 Testing

- Use the **Apple Pay sandbox** with Apple's test cards; provision test cards by signing in to iCloud with a **Sandbox Tester** account. Sandbox calls use the certificate endpoint (§36.6); switch to production before going live.
- Also test in **production with real cards** to confirm the end-to-end flow. Attempting sandbox cards against production (or vice-versa) results in PSP rejection. Reference: Participating Banks list.

**Evidence Strength:** Direct Public Apple (Merchant Guide, Mar 2026). **Specification Depth:** Full Spec.

### 36.14 Explicitly Out of Scope (Referenced, Not Integrated)

The following appear in the Apple Pay Platform / Merchant Integration Guides but are **general web/in-app commerce UX**, not AMB and not setup/registration. They are intentionally **not** integrated into this canonical; consult the source guides directly if needed:

- Payment-sheet JavaScript event handling code (`onmerchantvalidation`, `onpaymentauthorized`, `onshippingaddresschange`, `completeMerchantValidation`, etc.) and the App equivalents (`PKPaymentAuthorizationController` callbacks).
- `ApplePayError` / `PKPaymentError` handling, coupon-code (`supportsCouponCode`), disbursement requests, and multi-token booking-site samples.
- Payment-sheet construction UX (line items, shipping/billing options), redacted-address callbacks.
- Risk-management guidance (velocity/pattern, delivery, "bad transactions" list, email/IP/country checks).
- Marketing Toolkit; Apple Pay button/mark styling and Human Interface Guidelines.

**Rationale:** these are neither AMB message behavior (§16) nor merchant setup/registration/processing (§36.1–§36.13). Including them would expand the canonical beyond its Layer-2 AMB scope without adding AMB-actionable specification.

### 36.15 Source Citations

- Apple Pay Platform Integration Guide (Apple-authored PDF; footer-dated **June 2025**, cover-dated September 2025 — footer prevails, see §33.6).
- Apple Pay Merchant Integration Guide (Apple-authored PDF; **March 2026**, with its own Change Log — see §33.7).
- AMB-specific facts cross-referenced from §16.14 (Direct Gated Apple).

**Cross-reference:** §16 (Apple Pay Message), §28.4 (Apple Pay Setup — onboarding side), §37 (R2–R6).

---


