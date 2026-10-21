# Video / Recording Spec (Tool 3 video rules)

**Sources (extracted, not invented):**
- `sources/ma-experience-review/04_2026_08_31_apple_messages_for_business_brand_experience_review_video_recording_guide_v1_0.pdf` — MA "Brand Experience Review: Recording Guide", v1.0, 1 September 2026.
- `sources/ma-experience-review/00_MD_FILE_apple_messages_for_business_experience_review_package_combined_v1_1.md` — combined package, v1.1.

Uncertain / cross-referenced items are flagged inline. Rule IDs in brackets (e.g. `[3.1]`) refer to `packages/rules/rules.json`.

---

## 1. The three flows

The guide defines one spine (Flow A) plus two conditional flows (B, C). "What changes between archetypes is which extension blocks you drop in at Step 5, and nothing else."

### Flow A — "The use case, end to end"
The spine; holds for all five archetypes. **One continuous take, customer side, entry point to close.** Steps:

| Step | Must show |
|------|-----------|
| 1. Entry point | Start from a real entry point (QR, website button, app, email link); routing context carried so the conversation lands in the right flow. If the entry point carries intent, film a **second** entry point with a *different* intent landing somewhere visibly different. |
| 2. Greeting, disclosure & scope | Short typing indicator, then a greeting **inside 5 seconds** that plainly states it is automated, gives the assistant's name, and says what it can help with. Pattern: "I am [NAME], here to help with [A], [B] and [C]". Disclosure alone is not enough. |
| 3. The opening choice | Where the entry point didn't carry intent, offer a Quick Reply of up to **five** real top intents, most common first. If the customer already wrote a clear intent, answer it rather than overriding with the menu. If an AI layer replaces the fixed menu, show it doing better than a menu would. |
| 4. Confirm what you already know | Reflect back held context (order, store, booking) rather than re-asking. |
| 5. The task | Archetype-specific; extension blocks go here. **Two to four steps, no more.** Each rich element is preceded by a framing bubble and followed by a confirmation of what the customer chose. |
| 6. Resolution | State the outcome plainly — what was booked/ordered/changed/answered/sent and what happens next. |
| 7. Anything else | Ask whether there is anything else, as a Quick Reply (single tap answers). |
| 8. Leave Conversation + post-close | Customer ends via **Leave Conversation**; the business side then **attempts to send, on camera, and is blocked**. Show the blocked attempt, do not assert it. |

### Flow B — "When a person is needed"
**Filmed side by side (agent console + customer device).** A second take; may start from the same entry point.

1. Customer asks for a person — both ways if possible: a trigger word (e.g. `AGENT`) **and** free text ("this isn't helping" / "can I talk to someone"). Bot classifies both and errs toward escalating.
2. Collect what the agent will need before routing (no re-asking on the other side).
3. Announce the handoff and **why**; give an estimated wait + queue position where response isn't immediate.
4. The person arrives — introduces themselves by name, picks up the thread without asking the customer to repeat; typing indicator visible while composing; **type it live** (no scripted paste).
5. Close — human agent confirms outcome and offers more help; customer ends; both bot and agent are blocked afterwards.
- **No live connection available:** film the agreed alternative — in-conversation message offered **first** with a stated response window, then callback/email after; details collected in-channel; acknowledgement states specifically what happens next and when ("…within two business hours" passes; "Someone will be in touch" does not).

### Flow C — "When conditions are not ideal"
Short; can be one take. Proves the experience holds outside the happy path.

- **Part 1 — Out of hours:** customer reaches the brand outside stated hours and asks for a person. Bot states the hours, says when a reply will come, and offers to take a message **inside the conversation as the first option**. Customer leaves the message — film that. Never pretend a person is available.
- **Part 2 — Capability-aware fallback:** on a second, more limited device (a Mac or an iOS 18 device), run the same use case. The bot **swaps the unsupported element for a supported alternative at send time**, and the journey continues to completion. Two things must be visible: **the swap happening** and **the fallback path still finishing the task**. Narration does not count.

---

## 2. Timestamp index format

"Submit a timestamp list alongside the videos. One line per demonstrated item: the video, the time, and what it shows."

**Format:** `V<n>  <mm:ss>   <what it shows>`

Verbatim example index from the guide:
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
Note: `V1` = Flow A take, `V2` = Flow B take, `V3` = Flow C take. The guide adds: "If you filled in the Evidence column of Document 3 while testing, this list already exists. Export it." (maps to rule `[11.6]` Timestamp index submitted alongside the videos.)

---

## 3. "Why recordings come back" — the first 10 video rules

Verbatim, **in MA's stated order** ("In rough order of how often we see each one"). These are the first 10 video rules for Tool 3:

1. A typing indicator missing on a back-to-back sequence
2. The rich card filmed without its own image, showing only the row thumbnails
3. Leave Conversation asserted rather than demonstrated, with no blocked send on screen
4. A bare URL or a "tap to load" link visible in the thread
5. Capability fallback described in narration instead of filmed
6. Placeholder content, grey boxes and "Product 1" in shot
7. Rehearsal threads visible in the conversation list
8. Restricted platform wording spoken in the voiceover
9. Out of hours filmed as a generic greeting rather than as a live agent request outside hours
10. Features included because they were on a list, making the whole thing read as a demo

Cross-reference to numeric rules (best-effort): 1→`[3.5]`, 2→`[5.2]`, 3→`[0.2]`, 4→`[4.1]`, 5→`[8.1]`, 6→(real-content; candidate / `[11.x]`), 7→`[11.2]`, 8→`[0.3]`, 9→`[3.18/3.19]`, 10→(use-what-the-task-needs; candidate new).

---

## 4. Apple's five non-negotiables and where each is tested

From the guide's section **"The five points checked every time"** ("the most common reasons a recording is sent back. All five must be visible somewhere across the three flows"). These correspond to the Section 0 Final Gate ("Apple's five") in Document 3.

| # | Non-negotiable (verbatim gist) | Where it is tested (flow/step) | Numeric rule |
|---|-------------------------------|-------------------------------|--------------|
| 1 | **Reachable escalation** — a live agent connection is reached, or the agreed alternative is offered and acknowledged with a specific commitment | Flow B (live agent handoff) or Flow B / Flow C Part 1 alternative (in-conversation message with stated response window) | `[0.1]` |
| 2 | **Honest automation** — the automation identifies itself as automated and never implies a person is present when one is not | Flow A Step 2 (greeting / disclosure); reinforced by truthful "are you a bot?" answers | `[3.2]`, `[3.4]` |
| 3 | **Leave Conversation respected** — the close is honoured and a send attempt afterwards is shown being blocked | Flow A Step 8 (post-close block) and Flow B Step 5 (same block applies to agents) | `[0.2]` |
| 4 | **Capability-aware fallback** — the swap to a supported alternative happens at send time, on device, and the journey still completes | Flow C Part 2 | `[8.1]`, `[8.2]` |
| 5 | **Clean language** — none of the prohibited wording appears on screen or in narration | All flows (console, narration, templates, labels) — not only message copy | `[0.3]` |

> **Flag:** the guide calls these "the five points checked every time," while Document 3's "Section 0. Final Gate" lists **four** rows (0.1–0.4). The recording guide's five map to 0.1, (3.2/3.4), 0.2, 8.1, 0.3 — i.e. "Honest automation" and "Capability-aware fallback" are pulled in from Sections 3 and 8 rather than both living in Section 0. Reconcile the "five vs four" framing before treating Section 0 as the canonical five.

### Prohibited wording (verbatim, from the guide)
- "iMessage" as the name of the channel
- "Apple Business" as the name of the channel
- "iMessage app" as the name of an App Extension
- "Messaging rates may apply"
- "Data rates may apply"

Approved naming: "Apple Messages for Business" wherever it fits; "Apple Messages" where the full name does not fit a label; "Apple Messages contact" (never "Apple Business Contact") for an unknown contact. The naming rule governs the console, narration and templates, not only message copy `[0.3]`.
