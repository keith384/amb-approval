# Apple UX Standards — Experience Review Checklist

The six categories of feedback Apple returns on AMB experience submissions, restated as checks. Each entry gives the requirement, the failure mode, and where relevant the fix.

Source: MA's *AMB Experience Review Process* overview, derived from Apple's design standards and observed reviewer feedback.

**Contents**
1. Onboarding & triage
2. Conversational flow & navigation
3. Visual UX & component usage
4. Human escalation & support
5. Satisfaction & feedback
6. Copy & style
7. Fast triage list

---

## 1. Onboarding & triage

**Automated agent disclosure**
The bot must tell the user it is automated within the first interaction — e.g. "I'm an automated agent." Transparency here is mandatory, not stylistic.
*Failure mode:* the experience opens with a warm branded greeting and never discloses. This is a blocker and one of the most common returns.

**Initial triage menu**
When user intent is unclear at entry, Apple expects a triage menu immediately. A Quick Reply with up to 5 options is preferred over making the user type a free-form request or read through a text prompt to figure out what to do.
*Failure mode:* an open "How can I help you today?" with no options.

**Opt-in / opt-out transparency**
Notifications must never be enabled automatically. The user actively opts in — e.g. choosing a "Subscribe" option. The conversation must also state how to opt out, e.g. "Reply 'unsubscribe' at any time to opt out."
*Failure mode:* subscription assumed on first contact, or opt-out buried in a link or never mentioned.

---

## 2. Conversational flow & navigation

**"Anything else?" prompt**
End a completed use case by asking whether the user needs further help, rather than terminating. Follow it with a triage menu or relevant next options.

**Fallback handling**
When the bot can't assist or doesn't understand, it must not stay silent or ignore the message. A clear, polite fallback is required — e.g. "Sorry, I didn't quite understand that. Please select an option below."
*Failure mode:* unrecognized input produces nothing, or the bot repeats its last message verbatim. Blocker.

**No dead ends**
Every path needs a clear next step. Even when the bot can't answer, it must offer a fallback or an escalation route. Never a terminal state with nothing to do.
*Failure mode:* an FAQ answer that just ends. Blocker.

**Conversational logic for simple inputs**
For one or two fields — name and email, say — Apple discourages a formal Form object and prefers plain-text conversational collection: "What's your full name?" then "What's your work email address?" Less friction.
*Failure mode:* a two-field Form. Fix before submission.

**Concise phrasing**
Keep prompts short, natural, and QuickType-friendly, especially when asking for data.

**No repetition**
Never ask the user to repeat information already given earlier in the thread. Worth specifically probing on AI-generated experiences, where state gets dropped across handoffs.

---

## 3. Visual UX & component usage

**Rich Links for all URLs**
Every URL goes out as a Rich Link. Plain-text links and "tap-to-load" text links are not acceptable. The image in the Rich Link must accurately reflect the target page.
*Failure mode:* the bot pastes a URL. Blocker.

**Iconography**
Every interactive feature — including text messages and each individual option inside a List Picker — needs a contextually relevant thumbnail or icon so it reads as tappable.
*Failure mode:* List Picker rows with no images. Fix before submission.

**Form UX**
- Splash screens are best practice, plus a title, an introductory description, and a final review screen, so the user knows what they're filling out.
- Put the form's context — the "why" — in a conversational message bubble *before* the form, not in the form's subtitle. Subtitles get cropped and missed.

**Conciseness in feature bubbles**
Long text belongs outside feature bubbles. The first line of a feature bubble should be the title, because long text gets cropped and becomes unreadable before the user decides.

**List Picker vs Quick Reply**
Only use a List Picker when there is genuine variation in categories. With 5 or fewer options, use a Quick Reply — faster and less intrusive.
*Failure mode:* a four-item List Picker. Fix before submission.

---

## 4. Human escalation & support

**Out-of-hours handling**
When the support team is offline, state the operating hours clearly and let the user leave an asynchronous message directly in the thread.
*Failure mode:* "we're closed" with no way to leave a message.

**Contextual escalation**
Escalation should be transparent and stay in-channel. If an email to support is being drafted, the bot should help compose it within the conversation rather than abruptly pushing the user out to another channel.

**Transparent escalation**
State the handoff explicitly — e.g. "A live agent will join the chat shortly" — and have the agent introduce themselves on joining.
*Failure mode:* a human silently takes over mid-thread.

**Wait time communication**
If an agent isn't immediately available, communicate the expected wait time. Manage the expectation rather than leaving dead air.

**Prohibited phrasing**
Never use "This conversation has been closed" or similar. It reads as abrupt and dismissive. Close with friendly language that leaves the door open.

---

## 5. Satisfaction & feedback

**CSAT survey timing**
Trigger satisfaction surveys only after the entire experience is complete — never after each individual FAQ interaction. Per-interaction surveys saturate the inbox and degrade the experience.

---

## 6. Copy & style

**Professionalism**
Proper casing throughout. Messages sent entirely in lowercase get flagged as poor UX. Worth an explicit pass on AI-generated copy, which drifts casual.

**Quick Reply summaries**
Summary text in a Quick Reply should be concise and label-based — "Option selected" — rather than restating the full previous message, which bloats the chat history.

---

## 7. Fast triage list

For a quick pass before a full audit. Any "no" here is at least a fix-before-submission item, and the first five are blockers.

1. Does the bot disclose it's automated in the first interaction?
2. Is every URL a Rich Link with an accurate image?
3. Does unrecognized input get a polite fallback, never silence?
4. Is every path free of dead ends?
5. Are notifications opt-in, with opt-out stated?
6. Is there a triage menu at entry when intent is unclear?
7. Are 5-or-fewer-option choices Quick Replies rather than List Pickers?
8. Does every interactive element have an icon?
9. Do completed use cases ask "anything else?"
10. Is the live-agent handoff announced, with the agent introducing themselves?
11. Is there an out-of-hours path that accepts an async message?
12. Is CSAT fired once, at the end?
13. Is the copy properly cased?
14. Is the user ever asked to repeat something?
