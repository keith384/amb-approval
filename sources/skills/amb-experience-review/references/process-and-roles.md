# AMB Experience Review — Process, Roles, QA Bar, Recording

Source: MA's *AMB Experience Review Process* overview.

**Contents**
1. Roles and ownership
2. The eight steps
3. Pre-submission QA bar
4. What the screen recording must show
5. After submission
6. Framing this for a client

---

## 1. Roles and ownership

One rule sits above everything: **MA owns this workstream and is the single point of contact with Apple for the first brand review**, until MSP status becomes public. Apple's feedback reaches Linq through MA.

| Party | Owns |
|---|---|
| **MA** | Process orchestration, checklist and guidance, internal validation, all Apple communication and submission |
| **Client (MSP — Linq)** | Building the AI-generated / AI agent experience, internal testing, addressing feedback, brand and use-case content |
| **Apple** | Final experience review, approval decision, feedback on submitted recordings |

Two facts shape why the process is structured this way:
- The MSP builds the experience, agent, and conversational flows with its own tools and content.
- Most AMB experiences today are **AI-generated rather than fixed conversational flows**, which makes structured, checklist-based validation before submission more important, not less. A deterministic flow can be inspected; a generative agent has to be probed.

---

## 2. The eight steps

| # | Step | Client (Linq) | MA | Apple |
|---|---|---|---|---|
| 1 | **Use case & scope alignment** | Prepares the brand, use case, and design to go live with | Confirms use case, UX and scope; loops in Apple for pre-approval if the use case is non-standard | Pre-approves non-standard use cases when required |
| 2 | **Build & internal testing** | Builds the AI agent experience; tests internally against the use-case checklist | Provides the checklist (standard, adapted to agreed scope) and technical guidance; available during build | — |
| 3 | **MA validation** | Shares the live experience; addresses MA's feedback | Validates the live experience against the same checklist; issues feedback until clean | — |
| 4 | **Review prep** | Reviews the Apple recording guide | Shares the Apple experience-review guide and recording instructions | — |
| 5 | **Recording & feedback** | Records the required video(s); re-records after feedback | Reviews video(s) against the checklist and Apple's guidelines; feedback until ready | — |
| 6 | **Submission** | — | Submits video(s) and any additional materials to Apple on the client's behalf | Receives the submission |
| 7 | **Apple review** | Supports fixes if Apple requests changes | Relays Apple's feedback; coordinates re-submission | Reviews; approves or returns feedback |
| 8 | **Go-live** | Launches the approved experience; supports post-launch monitoring | Supports go/no-go coordination and post-launch monitoring | — |

**Step 1 is where the expensive surprise lives.** A non-standard use case needs Apple pre-approval, and that gets flagged at Step 1 or it derails the timeline later.

**Step 3 is the internal gate.** MA validates against the same bar Apple uses, so nothing new should surface once the submission is with Apple. Treat MA validation as the real deadline — Apple review is just confirmation of work already done.

---

## 3. Pre-submission QA bar

Apple expects this quality bar before any experience review begins. MA validates against it at Step 3.

- Apple Messages for Business account is connected and message delivery is confirmed.
- Commercial account access is restricted to authorized Apple IDs used for testing (Account Testing > Advanced).
- The test environment is fully stable before submission — all entry points, automated responses, live agent handoffs, and edge cases fully implemented.
- Both automation and live-agent interactions are configured, activated, and tested end to end.
- Every use case has been tested from the end user's perspective, with all features and content reviewed and errors fixed.
- **Tested on real devices.** Never rely solely on simulators. Test every flow on a physical, supported Apple device using the test environment. iOS is the priority — it's the primary platform.
- Agents are prepared and trained to handle AMB traffic and the relevant use cases.

The agent-readiness item is the one that gets skipped, because it's a people problem rather than a build problem. Video #2 puts a live agent on camera; an untrained agent shows.

---

## 4. What the screen recording must show

The recording at Step 5 is the artifact Apple actually reviews. The build is only visible to Apple through the video.

General requirements:
- Reflect the real production user journey(s) on an iOS device, from the user's point of view.
- The agent console and backend bot logs do not need to be shown.

Three videos:

| Video | Must demonstrate |
|---|---|
| **#1 — Main use case(s)** | Rich Features integrated into the experience, showcasing the main use case(s) — the entire customer journey including success paths. Long journeys may be split into multiple parts for clarity. |
| **#2 — Live agent** | The live-agent interaction: user escalates, agent replies, a short sample conversation happens. |
| **#3 — Out-of-hours** | Out-of-hours messages and fallback. |

MA shares a recording guide before recording (Step 4), so format and content expectations are settled in advance. Don't record without it.

---

## 5. After submission

Apple reviews the recording(s) and sends feedback to MA. If Apple identifies issues, MA relays them, Linq addresses them, MA re-submits. **The loop can repeat until approved.** Once approved: go-live and post-launch monitoring.

Feedback management:
- On resubmission, include a summary that explicitly references **each feedback item by its ID or description** and explains how it was resolved. This lets Apple's reviewers verify fixes faster.
- **Partial fixes equal rejection.** Address all feedback items. A partial fix usually produces another review round and delays launch.

---

## 6. Framing this for a client

The reason MA aligns everyone to this process at project kickoff is so roles, hand-offs, and the definition of "done" at each stage are clear before any build work starts.

When briefing a brand, lead with what's expected of them and when — Steps 1, 2, 3, 5, 8 are where they have work. Be honest about the two things outside anyone's control: Apple's review turnaround, and the possibility of a feedback round. Framing the loop as normal rather than as a failure keeps a first-round return from becoming an escalation.
