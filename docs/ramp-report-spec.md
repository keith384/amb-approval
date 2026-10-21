# Ramp Report Letter-ID Scheme (Tool 3 output spec)

**Source:** `sources/examples/ramp-review-report.pdf` — "Ramp: Apple Messages for Business, Issues to Fix". Prepared by Messaging Advisory (MA), built 9 October 2026. Consolidated view of the MA review + a second internal review of the Ramp recording (18 September 2026). Everything below is extracted verbatim from that PDF; nothing is invented. Uncertain items are flagged inline.

---

## 1. Five-bucket report structure

The report sorts every finding into exactly five buckets. Header line (verbatim counts):

> **6 Fail · 20 Caveat · 8 Not shown: Mandatory · 9 Not shown: Recommended · 5 Apple will ask**

| # | Bucket | Header count | Meaning (as used in the report) |
|---|--------|-------------:|---------------------------------|
| 1 | **Fail** | 6 | A requirement is demonstrably broken on camera; must be fixed. |
| 2 | **Caveat** | 20 | Shown, but with a problem or a risk MA is flagging. |
| 3 | **Not shown in recording: Mandatory** | 8 | A mandatory element was never demonstrated; must be added to the next recording. |
| 4 | **Not shown in recording: Recommended** | 9 | An in-scope-but-optional element was not demonstrated; add if in the feature list. |
| 5 | **Apple will ask** | 5 | Open question Ramp must answer for Apple (not a pass/fail yet). |

> **Count note (flag):** the header says **20 Caveat**, but the Caveat table lists **21 rows** (19 on page 1 + A2 and B6 on page 2). The extracted row count (21) is one higher than the stated header count (20). Treat the header number as MA's intended total and reconcile before reuse.

---

## 2. Report layout — columns per finding (Tool 3 output spec)

The report uses **two column layouts** depending on the bucket:

### Layout 1 — Fail and Caveat buckets
Four columns, one row per finding:

| Column | Content | Example |
|--------|---------|---------|
| **TIME** | Timestamp or timestamp range in the recording (`m:ss` or `m:ss to m:ss`), or the word **Whole** for whole-recording findings | `0:06 to 0:13`, `3:53`, `Whole` |
| **TEST** | `<letter-id>: <one-line test name>` | `C1: First reply in 5 seconds` |
| **ISSUE** | One-line statement of what is wrong | `First reply is over 5 s by either measure (7 s from send, 5.3 s from delivery); no indicator for the first 4 s` |
| **FIX** | One-line corrective action | `Send the indicator and greeting at once on the first message; target under 3 s` |

### Layout 2 — "Not shown" buckets (Mandatory + Recommended)
Three columns (no timestamp, because the item is absent):

| Column | Content |
|--------|---------|
| **TEST** | `<letter-id or range>: <name>` (ranges like `RL1 to RL4`, pairs like `A4 / G9`) |
| **NOT SHOWN** | What was missing / what was seen instead |
| **WHAT TO ADD** | Instruction for the next recording |

### Layout 3 — "Apple will ask" bucket
Three columns:

| Column | Content |
|--------|---------|
| **QUESTION** | `<letter-id or label>: <question topic>` |
| **WHAT WE SAW** | Evidence observed, with timestamp |
| **WHAT RAMP NEEDS TO TELL US** | The answer Apple will require |

**Canonical Tool 3 finding record** (superset for machine output):
```
{
  time: "<m:ss | m:ss to m:ss | Whole | null>",   // null for "Apple will ask" / not-shown
  test_id: "<letter id, e.g. C1>",
  test_name: "<one-line name>",
  bucket: "Fail | Caveat | Not shown: Mandatory | Not shown: Recommended | Apple will ask",
  issue: "<one line>",       // or 'not shown' / 'what we saw'
  fix:   "<one line>"        // or 'what to add' / 'what Ramp needs to tell us'
}
```

---

## 3. Letter-ID scheme — every distinct test ID in the report

58 distinct letter-IDs appear across the five buckets. The scheme is **letter-prefix + number**, where the prefix groups the area (A = recording authenticity, B = entry point / brand, C = first response, D = indicators / latency, E = copy, G = agents / escalation, H = data & consent / keywords, I = resolution, X0 = out-of-plan, and the two-letter feature prefixes RL/AT/LP/TP/FM/AP/AU/IA for the rich features). Numbers are **not contiguous** — the report only uses the IDs it needs (e.g. A1, A2, A4, A5, A6 with no A3).

### 3.1 Fail (6)
| ID | Name | Issue (verbatim) | Fix (verbatim) |
|----|------|------------------|----------------|
| B1 | Approved button | Entry point is a text suggestion, not Apple's button | Use Apple's Message Us button and record the tap on it |
| C1 | First reply in 5 seconds | First reply is over 5 s by either measure (7 s from send, 5.3 s from delivery); no indicator for the first 4 s | Send the indicator and greeting at once on the first message; target under 3 s |
| B3 | Service naming | Ramp settings screen labels the channel iMessage | Rename it Apple Messages and keep that screen out of the take |
| G11 | Agent uses rich features | Agent asks yes or no questions as plain text | Use a Quick Reply: Yes, lock it / No, keep it active |
| D1 | Indicator before every message | No typing indicator before the MUTE, pause, START and STOP replies (confirmed at 5 fps) | Add a 1 s indicator in the keyword handler |
| E4 | Escape option | Pause picker has no way out | Add Keep messages on as a fourth option |

### 3.2 Caveat (21 rows; header says 20 — see flag above)
| ID | Name | Time |
|----|------|------|
| A1 | Real journey | 0:00 to 0:03 |
| B2 | Call to action | 0:02 |
| B4 | Prominence | 0:02 |
| E10 | Clear copy | 0:16, 0:49, 4:02 to 4:13 (appears 3×) |
| X0 | Outside the plan | 0:20 to 1:38, 1:21 (appears 2×) |
| D3 | Reply latency | 0:21 to 3:47 |
| D2 | Bot indicator length | 0:46 to 0:48 |
| I5 | Silence after close | 1:01 to 1:09 |
| A6 | Clean screen | 1:14 to 1:22 |
| G3 | Transfer announced | 2:02 |
| G4 | Wait time | 2:02 to 2:15 |
| H2 | Clarifying question first | 2:25 |
| A5 | Continuous take | 2:36 to 3:31 |
| I1 | Clear resolution | 3:10 |
| H7 | Trigger words | 4:23 |
| A2 | Rich features | Whole |
| B6 | Brand header | Whole |

Example issue/fix wording (Caveat):
- **A1 Real journey** — issue: "Starts on qa.ramp.com, then a blank redirect page"; fix: "Record from the live Ramp web app or mobile app".
- **G4 Wait time** — issue: "Shortly, then in just a moment; no wait time"; fix: "Give a wait time in the first message; keep the queue position".
- **H2 Clarifying question first** — issue: "No yes or no question before asking for card digits"; fix: "Ask Is this about a card on your Ramp account? first".

### 3.3 Not shown: Mandatory (8 rows; several share an ID or pair IDs)
| TEST label (verbatim) | Letter IDs | What to add (verbatim) |
|-----------------------|-----------|------------------------|
| A4 / G9: Out of hours | A4, G9 | Ask for a person outside hours and show the stated reply time |
| B8: Always available | B8 | Show the entry point in the out of hours clip |
| C6: Handles misunderstanding | C6 | Send one off topic message and show the fallback |
| G2: Keywords | G2 | Type each once and show the result |
| H7: Trigger words | H7 | Type MENU and RESUME once and show the result |
| H7: Opt out and return | H7 | Send STOP, show silence, then START |
| RL1 to RL4: Rich links | RL1, RL2, RL3, RL4 | Send one link and show the rich link preview |
| Security codes | *(no letter ID)* | Show the security code flow, or drop it from the welcome |

> **Flag:** "Security codes" has **no letter-ID** in the report. It is a named mandatory gap but outside the letter scheme.

### 3.4 Not shown: Recommended (9 rows)
| TEST label (verbatim) | Letter IDs | What to add (verbatim) |
|-----------------------|-----------|------------------------|
| Options not tapped | *(no letter ID)* | Tap Talk to a person from a menu at least |
| AT1 / AT2: Business attachments | AT1, AT2 | Send one image or file from Ramp if attachments are in the feature list |
| G8: Agent to agent transfer | G8 | Show one if Ramp uses it |
| LP1 to LP4: List Picker | LP1–LP4 | Show it if in the feature list |
| TP1 to TP4: Time Picker | TP1–TP4 | Show it if in the feature list |
| FM1 to FM6: Form | FM1–FM6 | Show it if in the feature list |
| AP1 to AP4: Apple Pay | AP1–AP4 | Show it if in the feature list |
| AU1 to AU3: Authentication | AU1–AU3 | Show it, or explain the verification Apple will ask about |
| IA1: iMessage app | IA1 | Show it if in the feature list |

> **Flag:** The feature families (RL, AT, LP, TP, FM, AP, AU) are cited only as **ranges** ("RL1 to RL4"). The report does **not** define each sub-ID individually, so the per-item meaning of RL2/RL3/LP3/TP4 etc. is inferred, not stated. "Options not tapped" has no letter-ID.

### 3.5 Apple will ask (5)
| QUESTION label | Letter ID | What Ramp needs to tell us (verbatim) |
|----------------|-----------|---------------------------------------|
| H6: Card alert consent | H6 | How customers opt in to card alerts in Messages |
| Live agent response time | *(no letter ID)* | The target first response time for live agents |
| Verification for card actions | *(no letter ID)* | How customers are verified, and whether the app session is signed in |
| Expense policy source | *(no letter ID)* | Whether these are Ramp defaults or the customer's company policy |
| Replacement card | *(no letter ID)* | Delivery details and how consent is captured |

> **Flag:** Only **H6** in this bucket carries a letter-ID; the other four are labelled by topic only.

---

## 4. Letter-ID → numeric rule mapping

The machine-readable map lives in `packages/rules/sources/letter-id-aliases.json`. It is a **documentation-only** best-effort map; it does **not** modify `rules.json`.

- **Numeric ref** = the `id` field of a rule in `packages/rules/rules.json` (e.g. `3.1`), matched on test name / meaning.
- **Shape:** `{ "<letter_id>": { "ref": "<numeric id|null>", "name": "<ramp name>", "rule_name": "<rules.json name|null>", "confidence": "high|low" } }`.
- `ref: null` = no existing numeric rule matched. These are **candidate NEW rules** sourced to the Ramp report. They are recorded only; they are **not** added to `rules.json`.

**Totals:** 58 distinct letter-IDs → **42 mapped** to an existing numeric ref, **16 unmatched** (candidate new rules).

**Unmatched (candidate new rules):** `G11` (agent should use rich features, not plain-text yes/no), `A1` (record the real live journey, not QA/redirect), `B2` (entry CTA must say what the customer can do), `B4` (entry prominence — visible without a tap), `X0` (nothing outside the submitted plan; consistent labels, no test data), `A5` (one continuous take), `I1` (confirm resolution / consent before acting), `B6` (brand name + logo set in Apple Business Register), `G8` (agent-to-agent transfer), `LP4`, `TP3`, `TP4`, `AP3`, `AP4`, `AU3`, `IA1` (iMessage app / App Extension). The trailing feature sub-IDs are unmatched largely because the Ramp report cites them only as ranges without per-item definitions.

**High-confidence anchors** (clear 1:1 meaning match) include: B1→12.4, C1→3.1, B3→0.3, D1→3.5, G3→9.1, G4→9.2, H2→7.4, A4→3.18, G9→3.19, B8→12.6, C6→3.14, G2→3.13, RL1→4.1, AT1→6.1, LP1→5.4, FM1→5.6, AP1→7.3, AU1→7.1, H6→10.1. All other mappings are marked `low` (family/approximate/uncertain).
