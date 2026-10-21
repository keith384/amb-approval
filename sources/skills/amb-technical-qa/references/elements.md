# Message Elements, Capability Detection & Tapbacks

Primary source: [Interactive Message Types](https://register.apple.com/resources/messages/msp-rest-api/type-interactive) and [Receiving Messages](https://register.apple.com/resources/messages/msp-rest-api/messages-received). Requires an Apple Business Register / MSP login.

## Contents

- [Capability detection](#capability-detection)
- [Fallback rules](#fallback-rules)
- [Capability and device matrix](#capability-and-device-matrix)
- [Interactive message common structure](#interactive-message-common-structure)
- [Rich links](#rich-links)
- [Quick reply](#quick-reply)
- [List picker](#list-picker)
- [Time picker](#time-picker)
- [Forms](#forms)
- [Attachments](#attachments)
- [Wallet](#wallet)
- [Maps, App Clips, iMessage apps, Apple Music, AR](#maps-app-clips-imessage-apps-apple-music-ar)
- [Tapbacks](#tapbacks)

---

## Capability detection

`capability-list` is an HTTP header Apple sends on **every inbound message**, listing what the customer's current device supports. Valid values: `QUICK`, `LIST`, `TIME`, `AUTH`, `AUTH2`, `FORM`. Case-insensitive. Read it inbound, store it against the conversation, pass it back on outbound.

Read it on every message rather than once, because the Opaque ID is stable but the device is not. A customer replying from a Mac drops `FORM` from the broadcast; replying from the phone restores it. Always use the most recent inbound value.

**Not capability-gated:** Apple Pay, rich links, attachments, and Wallet passes work on all AMB-capable devices and never appear in the capability-list. No check needed before sending.

Wallet is a nuance worth getting right: not gated, but on Mac a pass renders as a `.pkpass` file rather than a Wallet pass. Both statements are true — it sends, it just doesn't present as intended.

## Fallback rules

1. Never send an unsupported type. Block it on the send path **and** hide it in the agent console — if `FORM` is absent, the Form option must not appear in the console UI. Console gating is checked at Experience Review.
2. Detect first, then substitute. Don't send and hope; don't surface an error to the customer.
3. Preserve the interaction shape. A choice stays a choice, a date stays a date.
4. Plain text is the floor — no capability required, works everywhere.
5. Cascade. Fallback targets have their own requirements.
6. Store the `requestIdentifier` on every interactive send so the response correlates back regardless of which type was finally sent.

**Platform-wide fallback**

| Desired | Unsupported when | Fallback |
|---|---|---|
| Form Message | `FORM` absent (pre-18.4, Mac) | Per page type, below |
| List Picker | `LIST` absent (Mac) | Plain text prompt, or Quick Reply |
| Time Picker | `TIME` absent (Mac) | Plain text date/time request |
| Quick Reply | `QUICK` absent | Plain text listing the options |
| OAuth 2.0 | `AUTH2` absent (pre-iOS 16) | Do not send; legacy `AUTH` deprecated |

**Form page-type fallback**

| Page type | Condition | Fallback |
|---|---|---|
| select / picker | ≤5 options | Quick Reply |
| select / picker | >5 options | List Picker |
| datePicker | any | Time Picker |
| input | any | Plain text question, await free-text reply |

Quick Reply cannot represent multi-select, so it is never a valid substitute for a multi-select page — use List Picker and keep multi-select on.

**Worked example.** A triage form with a 6-option topic select, a callback date, and a free-text note:

- iPhone/iPad iOS 18.4+ — send the form as designed.
- iPhone iOS 16 — topic becomes a List Picker (6 options), date becomes a Time Picker, note becomes a plain text question.
- Mac — `FORM`, `LIST`, `TIME` all absent. Topic becomes a Quick Reply only if reducible to 5 options, otherwise a plain text list; date becomes a plain text request; note stays plain text.

**The gap Apple hasn't closed:** when the user is on a capable phone, a form is delivered to *all* their devices, producing a broken render on their Mac. The send-side check can't prevent it because the broadcast reflects the device that last replied. Refusing the send when capability is unannounced is correct MSP behavior; the multi-device delivery problem is Apple's.

## Capability and device matrix

| Type | Value | Min OS | Devices | Key limit |
|---|---|---|---|---|
| Quick Reply | `QUICK` | iOS 15.1 / macOS 12.0 | iPhone, iPad, Mac | 2–5 items |
| List Picker | `LIST` | iOS 11.3 | iPhone, iPad | >10 KB → `interactiveDataRef` |
| Time Picker | `TIME` | iOS 11.3 | iPhone, iPad | Shows local calendar conflicts |
| Form Message | `FORM` | iOS 18.4 | iPhone, iPad | Fallback required below 18.4 |
| OAuth 2.0 | `AUTH2` | iOS 16 / macOS 13 | iPhone, iPad, Mac | `AUTH` deprecated |
| Rich Links | not gated | iOS 11.3 / macOS 10.13.4 | iPhone, iPad, Mac | Title max 200 chars (MA note) |
| Apple Pay | not gated | iOS 11.3 / macOS 10.13.4 | Apple Pay-capable | Only `large` style supported |
| iMessage apps | not gated | iOS 11.3 | iPhone, iPad | Not on Mac |
| Attachments | not gated | — | iPhone, iPad, Mac | 100 MB |
| AR Quick Look (USDZ) | not gated | — | iPhone, iPad, Mac | — |

## Interactive message common structure

Message `type` is `interactive`, carrying `interactiveData`:

- `bid` — identifies the extension. Standard AMB: `com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension`. Custom iMessage app: substitute team ID and extension bundle ID.
- `data` — feature payload, containing `requestIdentifier` (required) and `version` (required).
- `receivedMessage` / `replyMessage` — control the bubble before and after the user responds.

**Bubble styles and image sizes**

| Style | Bubble (@3x) | Image (@3x) |
|---|---|---|
| `icon` (default) | 280 × 65 pt | 40 × 40 pt |
| `small` | 280 × 85 pt | 60 × 60 pt |
| `large` | 280 × 210 pt | 263 × 150 pt |

Supply @3x at 72 dpi; the system downscales. Apple Pay supports only `large`.

Title, subtitle, imageTitle, imageSubtitle, secondarySubtitle, tertiarySubtitle are each capped at **512 characters**.

**Payloads over 10 KB.** Apple uploads the original and sends an `interactiveDataRef` pointer. Call `/preDownload` for the URL, `GET` it, decrypt, then `POST` to `/decodePayload` to recover the `interactiveData` dictionary. A send-side reference can be reused for identical content (30-day expiry, same as any attachment); a received `interactiveDataRef` must be processed immediately and cannot be reused.

**`v` vs `version`.** `v` is the REST API version (integer), matching `https://mspgw.push.apple.com/v1`. `version` inside an interactive message is the message extension schema version (string). Apple explicitly calls out the confusion.

## Rich links

Apple does not permit plain links. The platform must convert every link into a rich link, and Apple auto-converts user-sent links inbound. A rich link carries a title and a URL, and Messages renders the real URL rather than custom display text — the destination cannot be masked.

Images are always required. Resolution chain (MA): payload image → Open Graph tag → largest image on the page → brand default. Images optimize to 240 × 240 px; small is 150 × 150 px; width ≥150 px produces the large icon treatment. Video is supported.

A URL appearing mid-sentence renders as bare text rather than a rich link payload. This is spec-conformant, has been debated with Apple before, and is not a bug to fix.

Why this matters more than it sounds: a plain URL rendering as "Tap to Load Preview" is an explicit Experience Review rejection criterion and the single most common cause of review failure.

## Quick reply

→ [Quick Reply Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#quick-reply-message)

Two to five choices, single selection only, iOS 15.1 / macOS 12.0. No `receivedMessage` or `replyMessage` fields — the structure is deliberately simple.

`summaryText` is required. It drives the device notification and appears in the transcript after the user chooses. **Apple is explicit that it is not the introduction message** — send a separate text message to pose the question. Apple's feedback on Linq's demo video was that summary labels must be short, not repeated sentences.

Items carry `identifier` and `title` (max one line of text). Order follows JSON order. Response returns `selectedIndex` and `selectedIdentifier`.

Best for triage, yes/no, routing, escalation choices, simple next-step menus.

## List picker

→ [List Picker Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#list-picker-message)

Sectioned and graphical. Sections carry `title` (required), `order`, and `multipleSelection` (defaults false). Items carry `identifier` (required), `title` (required), `subtitle`, `imageIdentifier`, `order`.

Item images render at 60 × 60 points — supply @3x (180 × 180 px).

Apple publishes no maximum item count. The operative limit is the 10 KB `interactiveData` threshold, above which the payload converts to `interactiveDataRef`. Keep lists short enough that items don't fall below the fold.

A multi-select response returns each selected title on its own line.

Apple's demo feedback: show subtitles and secondary text, not titles alone.

## Time picker

→ [Time Picker Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#time-picker-message)

Presents time slots and displays conflicts found on the customer's local calendar. After replying, the customer can tap the bubble to view location information, get directions, or add the event to their calendar.

`event` dictionary:

- `identifier` (required), `title`, `imageIdentifier`
- `timeslots` — each requires `identifier`, `startTime` (ISO-8601 UTC, e.g. `2017-05-26T08:27:55Z`), and `duration` in seconds
- `location` — `latitude`, `longitude`, `radius` (meters), `title`. Apple ignores `radius` when lat/long are missing
- `timezoneOffset` — minutes from GMT. Unset, times show in the customer's current timezone; set, in the event's timezone regardless of where they are
- Reply bubble image — @3x at 375 × 208 points (1125 × 624 px)

Apple's demo feedback: include appointment location details, which is what unlocks Get Directions and Add to Calendar.

## Forms

→ [Form Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#form-message)

Multi-page interactive flows from a single JSON payload — triage, CSAT, account creation, sign-up. iOS and iPadOS only, 18.4+.

The initiating `interactiveMessage` type is `dynamic`, requiring `version`, `template` (`messageForms`), and `data`. **Apple's spec states version should be 1.1.** MA's fallback primer says 1.2 — an unresolved conflict; confirm before shipping.

`data` contains:

- `startPageIdentifier` (required) — must match a configured page
- `pages` (required) — at least one page is needed to trigger the experience
- `splash` — optional opening page: `header`, `splashtext`, `buttonTitle` (required if splash is used), `imageIdentifier`. Missing `buttonTitle` means the splash doesn't display and the form proceeds to the first module
- `showSummary` — defaults false
- `private` — defaults false; when true the response carries the flag so the MSP can apply per-brand special handling

**Page types**

| Type | Notable fields |
|---|---|
| `select` | `multipleSelection` (default false), `items` with `title`, `value`, `identifier`, `imageIdentifier`, `nextPageIdentifier` |
| `picker` | `pickerTitle`, `selectedItemIndex` (zero-indexed, default 0), `items` |
| `datePicker` | `hintText`, `options`: `dateFormat` (default `MM/dd/yyyy`), `startDate`, `minimumDate`, `maximumDate`, `labelText` |
| `input` | `hintText`, `options`: `regex`, `placeholder`, `required`, `inputType` (`singleline`/`multiline`), `labelText`, `prefixText`, `maximumCharacterCount`, `keyboardType`, `textContentType` |

Input defaults: `singleline` 30 characters, `multiline` 300. `keyboardType` accepts the UIKit range including `numberPad`, `phonePad`, `emailAddress`, `decimalPad`, `URL`. `textContentType` accepts semantic values like `givenName`, `postalCode`, `telephoneNumber`, `creditCardNumber`, `oneTimeCode`.

**Branching.** `nextPageIdentifier` is required on every page **except** single-select pages, where it is set per item — that's how a select routes to different follow-ups by answer. A page without it is treated as final. `submitForm` marks an end page and can appear on multiple pages.

**Review step goes at the end, only.** Mid-form review is a known Apple failure point they specifically check.

**Documented known issue:** if the user task-switches to another app and returns to Messages, the form closes, resets, and all responses are lost. Apple's own recommendation is to keep form use cases short and quickly answerable rather than building long flows. This is Apple-documented, not a Linq bug.

**Response.** A `selections` array under `interactiveData > data > dynamic`, each object carrying `pageIdentifier`, `title`, `subtitle`, `items`. For `datePicker`, `value` returns UTC as `yyyy-MM-dd'T'HH:mm:ss'Z'` while `title` carries the formatted display date. For `input` with `prefixText`, the title contains prefix plus input.

Build priority (MA): forms are not on the Experience Review critical path. Get text, rich links, quick reply, and list picker working first.

## Attachments

100 MB, covering images, video, and documents including fillable PDFs.

Apple's documentation surfaces no error for oversized attachments — the message simply doesn't send — so the guardrail must be MSP-side. Linq has empirically observed a 400 response when exceeding the limit, a logged disparity with Apple's docs. Gate at 100 MB regardless of which behavior is current.

For very large documents, host externally and send a rich link rather than embedding.

Do not request highly sensitive PII in plain chat. Authentication is the sanctioned path for anything requiring verified identity.

## Wallet

Loyalty cards, tickets, coupons, boarding passes, store cards, gift cards. Wallet also functions as an entry point back into a Messages conversation, and Apple Pay Order Tracking can link Wallet order status back to Messages.

On Mac, a pass renders as a `.pkpass` file.

## Maps, App Clips, iMessage apps, Apple Music, AR

**Maps.** The agent sends a location rendered through the Construct Payload API. A map can also be generated as a rich link, but the interaction is more limited. Verify the render isn't a featureless green area — a pin in the middle of a park produces exactly that. **MapsLink** is the inverse: user-triggered location sharing, invoked via the "+" and share-location action.

**App Clips.** For a lightweight app experience from a rich link without a full install. The Construct Payload API generates App Clip payloads from supported URLs, but the URL must actually support App Clips or construction fails. Executes outside the Messages app, so the user must navigate back to resume.

App Clip or iMessage app? No app installed and you don't want to force one → App Clip. App installed and you want functionality inline or want to drive app engagement → iMessage app.

**iMessage apps.** → [iMessage App](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#imessage-app)

App Extensions letting customers interact inside the conversation with custom UI and app-specific data. App must be installed. iPhone and iPad only, not Mac.

Payload requires `appId` (App Store identifier), `appName`, `appIcon` (Base64, **under 15 KB** — shown when the recipient lacks the extension), `URL` (data passed to the app), `useLiveLayout` (defaults true), and a `bid` with your team ID and extension bundle ID.

`sessionIdentifier`: if your interactive data includes one, Apple reuses it in the payload to the device; otherwise Apple generates a random UUID. (Linq has an open issue where in-place updates fail despite the session identifier.)

Building one requires an Apple Developer account, an iPhone, and a Mac running Xcode.

**Apple Music.** All `music.apple.com` URLs — song, album, artist, playlist, music video, radio station. The country code in the URL (`/us/`, `/gb/`) must match the user's storefront for full rendering including the play button.

**AR Quick Look (USDZ).** 3D product previews, size comparison, placement previews. Furniture, retail, hardware, "see it in your space." Can also act as an entry point from web or app experiences.

## Tapbacks

→ [Receiving Messages](https://register.apple.com/resources/messages/msp-rest-api/messages-received)

The five facts that drive everything:

1. A tapback is **not a special message type**. It arrives as an ordinary inbound `type: "text"` message. No reaction object, no reaction flag.
2. Each tapback has its own new `id`, identifying *that text message* — not the message reacted to.
3. **No field points back to the original.** No `parentId`, `replyTo`, `inReplyTo`, `threadId`, or `originalMessage`. Attribution must be derived from `body` alone.
4. The only signal is the body string, and its meaning is locale and text-direction dependent.
5. Apple's guidance is to display the text as received, not convert it into a structured reaction on the agent console.

Tapbacks are **inbound only**. The platform detects them; it never sends them.

**What can be recovered**

| Reaction to | Body shape | Original text? | Original id? |
|---|---|---|---|
| Plain text | `Liked "<text>"` | Yes, echoed | No |
| Image | `Liked an image` | No | No |
| Interactive message | `Liked 1 Business Message` | No | No |
| Emoji | `Reacted <emoji> to "<text>"` | Yes | No |
| Sticker / Memoji | `Reacted with a sticker to "<text>"` + attachment | Yes | No |

**The interactive case is the trap.** An interactive message is not just the buttons — it carries a prompt bubble whose text is the message's `receivedMessage.title`. A Yes/No choice is one bubble, not two. So reacting to a visible question like "Do you want to do this?" collapses to `Liked 1 Business Message`, discarding both the prompt text and any reference. The same words sent as standalone plain text *would* be recoverable.

This is the C.3 correction: an earlier checklist item implied reactions to a rich element's prompt could be threaded back. They cannot. Do not implement or advertise it. The only fallback is a recency guess (most recent interactive message sent to that user), which must be labeled a guess and breaks when more than one is outstanding.

**Localization.** Bodies are locale and text-direction dependent — the same reaction in Japanese renders with reversed word order, and RTL locales reorder the string. Match on the presence of the quote structure, not position. Treat English regexes as a fast path only. The reaction set was last expanded in iOS 18, so the verb list is not closed; don't hard-code an exhaustive enum as your only gate.

**Fail open.** A genuine user message like `Liked "your last email"` will trip a naive detector. Anything not confidently matching a tapback pattern is a normal message. A missed tapback shown as plain text is fine; a real message swallowed as a reaction is a bug.

Sticker and Memoji images arrive as standard attachments and must be downloaded and decrypted through the normal `/preDownload` flow.

Apple's demo feedback: tapback reactions must be visible in the human agent console.
