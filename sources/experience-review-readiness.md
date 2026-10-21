# Experience Review readiness (checklist G.1, G.2, G.3)

Apple's Experience Review is the gate between staging and production: *"The
experience review is where Apple reviews the user experience of interacting with
a brand before you launch to the public"* (kit L9713), and *"Apple shares all
review results with you and your brand, including details of any items that must
be corrected prior to launch"* (kit L9717). Reviewers give feedback on three
dimensions (kit L9721–L9725): interactive features work correctly; ability and
ease of completing a use case; agent interaction.

This document is the **readiness inventory** — the standing list of what must be
true before we book that review, and what is actually true today. It is not a
claim of readiness. `proofs/policy/G.1.sh`, `proofs/policy/G.2.sh` and
`proofs/policy/G.3.sh` each re-derive their own section's "today" column below —
G.1's and G.2's from `proofs/checklist.yaml` and `proofs/gates.yaml`, G.3's from
the source tree itself — and fail if this document and what they derive
disagree, so the inventory cannot drift into optimism.

Kit references are canonical line numbers in
`planning/reference/ma-amb-kit/AMB_Layer2_Canonical_v7_0.md`.

---

## G.1 — pre-review preconditions (internal validation)

Before we book the Experience Review, four things must be true (MA workbook,
week 7 START / week 8 COMPLETE): all required Section C features implemented, a
sandbox brand provisioned, the demo script rehearsed, and both agent and bot
operational. MA's key consideration: *Apple will reject incomplete submissions
outright — run a full internal dress rehearsal first, including a deliberate
device-capability fallback.*

A precondition is **MET** only when its check below passes outright.

| # | Precondition | How it is checked | Today |
|---|---|---|---|
| 1 | All Section C features implemented | every Section C item that is the platform's `green`/`done` in `proofs/checklist.yaml` (`na` is the partner's and is neither counted nor excused) | UNMET |
| 2 | Sandbox brand provisioned | `abr-connect` gate `granted` in `proofs/gates.yaml` | MET |
| 3 | Demo script rehearsed | G.3 and G.4 (recording + production method) `green`/`done` | UNMET |
| 4 | Agent and bot operational | `scripts/curbfare-dir.sh` (resolves the extracted agent repo), `make prove-agent`; the bot IS the partner agent since W-556 deleted the platform flow engine | MET |

**2 of 4 met.**

Section C today: 16 green, 2 done, 3 in_progress, 0 not_started, 0 blocked, 1 na (22 items).

**Precondition 1 is the long pole and — since the last Apple gate flipped on
2026-07-28 — it is ours for every item that is the platform's; C.15 is the
partner's since 2026-09-17 and is counted as neither.** Sixteen of the 22
Section C items are green: C.1 (UTF-8/emoji, the first to clear both planes); as
of 2026-07-25, C.6 (quick reply), C.7 (list picker), C.8 (time picker),
C.19 (close/send-block), C.4 (receiving the close) and C.17
(capability gating) — all six closed in one sitting with a person and a phone,
not by more code; as of 2026-07-26, C.12 (Form Message), whose human
render+submit leg was discharged on the FORM-announcing iPhone the same way;
C.3 (reactions/tapbacks); C.10 (the OAuth
Authentication Message), green on 2026-07-28 when the assisted device session
completed the whole send→tap→sign-in→callback→journal chain on the staging
brand — which is why it sits in this green list rather than the blocked-list
history below; and as of 2026-07-27, C.11 (App Extensions), all three live legs run with the
shipped Agent Apps extension installed from the App Store — the live render
observed, the no-composable-reply design measured rather than assumed —
C.18 (Invitations), whose live plane was rewritten on 2026-07-27 to DRIVE its
repeatable legs rather than describe them — it had been passing while sending
nothing — and whose sixth and final staging leg, the literal No tap,
was measured the same night (tel-side, structured, our requestIdentifier
echoed; the clean-account residue stays register-tracked in D-030), and
C.2 (attachments and wallet passes), whose armed run passed all three legs
the same day — a signed .pkpass delivered and rendered on the iPhone, an
inbound attachment decrypted and webhooked, an 11 MB upload refused 413.
Each had every machine plane passing for a day or more and was
held open by something the rig cannot reach: a typing bubble chat.db has no column
for, quick-reply and picker layout, a calendar conflict that depends on the
customer's own calendar, a tap no driver can perform (C.19, C.4), and — C.17 — a
capability the driver itself cannot announce. That is the shape of most of what is
left here; see *What actually gates the rest* below.
And as of 2026-07-29, C.16 (landing page + channel settings, W-083): the
fixed post-W-103 sign-in journey — the last thing its checklist note held it
open on — was witnessed on the deployed `connect-staging` host running the
fixed image, the Business ID surviving the OIDC round trip and the link CTA
rendering with no second hand-off, terminating in the D4-correct
cross_brand_conflict refusal recorded in the append-only audit; the owner
accepted that refusal terminal as the journey's proof (per its checklist
note); and, the same day, C.9 (Apple Pay), whose live leg had never once
passed because it asserted an agent behavior no tool backs — driving the
send through the Partner API with an apple_pay fixture put a real payment
request on the device with a fresh production merchant session.
And as of 2026-07-30, C.13 (Construct Payload API, W-116): all three payload
types — Music, Maps and App Clip — demonstrated in one attended armed run, with
the owner confirming on-device that the Music bubble drew album artwork and a
play affordance, Maps drew an actual embedded map image, and the App Clip drew
an actual App Clip card. That run also refuted the intuition the item was built
on: an identical set of sends made *without* a constructed ref rendered the
same, so the render is evidence about the PAGE and never about the endpoint —
construct use is evidenced by the wire shape and by the runner's own
`richlink.construct_ok` line, both of which the flow now asserts positively
(the earlier absence-based assertion passed vacuously against a stale binary).

C.15 (entry-point routing on intentID/groupID) was green from 2026-07-30 —
two entry URLs took two different actions off one brand matrix, driven with
no person at all — until W-556 deleted the matrix and the flows it routed
into; it reads `na` since 2026-09-17 by owner decision: the platform forwards
`intent`/`group_id` on the inbound and on `message.received` (pinned by an
edge test) and the partner's agent does the routing, so a green here is the
partner's to earn, not this board's.
Three are in progress. **C.14 (typing indicator) moved green → in_progress on
2026-09-07** when W-529 made the typing indicator opt-in per message on the
owner's directive: the platform emits none it was not asked for, so the
workbook's "must be displayed before every message type" is the sender's
conduct rather than a platform guarantee, and MA verifies C.14 by Postman where
a bare send now shows nothing. The mechanism is still proven end to end (a
requested indicator precedes its message, including back to back; a suppressed
send types at nobody; a failed send drops its indicator; an unrequested send
reaches Apple alone) — what is owed is a conversation with Messaging Advisory
about whether an MSP that gives brands the choice satisfies the clause. The
other two are C.5, with proofs landed, and C.21, credited its START pass
on 2026-07-29 (W-115: the then-console's builder composed all ten part types, and
`brand_message_templates` plus the five `/v1/message_templates` routes now make a
composed rich object savable and editable; the week-6 FINISH demo dry-run is
still owed). **No Section C row is untouched any more**: C.20 and C.22, the last
two, terminated at `done` on 2026-07-30 — C.20 on the owner's manual walkthrough
of Channel Settings (its proof class is `human`, so an owner walkthrough IS its
proof mechanism and `prove.sh` can only ever answer SKIP-HUMAN), and C.22 on his
end-to-end live verification of the Connect journey plus his explicit decision
that it suffices without an executable flow. They read `done` rather than `green`
because `checklistcheck` requires an evidence manifest for `green` and neither
has a harness bundle to cite; gate 1 counts `green` OR `done`, and no bundle was
hand-authored to manufacture the stronger word. This paragraph used to say
"two are untouched (C.20, C.22)". As of 2026-07-28 **none is
blocked on Apple**: C.22 (Connect button) left the blocked list that day when
`abr-connect` was measured granted (test-account scope, `cerebro-staging` —
see precondition 2 above); what remained there was our own UX demonstration
behind J.3 (its other gate, C.16, went green 2026-07-29), not an Apple grant. C.10 (OAuth) left the blocked list on 2026-07-27, when
`make gateprobe` measured the endpoint approval GRANTED for the staging brand
— what remains there is our own proving rig, not Apple. The dev brand is still
unapproved on the wire, so C.10's live legs run against staging. C.2 (wallet passes) left the blocked list on 2026-07-26 and went
GREEN on 2026-07-27: its `dev-account-pass-type-cert` gate turned out to be
self-service portal work, not an Apple approval — the Pass Type ID + cert were
issued and measured the same day — and the armed run then passed all three legs
(signed pass delivered and rendered on the iPhone, inbound attachment decrypted,
oversize refused 413), which is why it sits in the green list above. C.18 (Invitations) left the blocked list on 2026-07-26:
the eligibility gate was granted on the 2026-07-25 gateprobe measurement
(STAGING-scoped — dev measured ineligible) and W-072 slice 2 landed the
route; its live legs ran against staging (proofs W-072 slices 3–4) and it
went GREEN on 2026-07-27 with the No-tap leg, which is why it sits in the
green list above. C.11 (App Extension) left the blocked list on 2026-07-25 —
Linq owns a real App Extension, so the `imessage-app-bid` gate is granted —
moved to in_progress when W-067's inbound contract plane landed, and went
GREEN on 2026-07-27 when the device leg ran with the App-Store-installed
extension (which is why it sits in the green list above, not here). C.9
(Apple Pay) went GREEN on 2026-07-29: its live leg used to assert the partner
agent would answer a purchase-intent phrase with an apple_pay part, which the
example agent has no tool to do, so the leg had never once passed; driving the
send through the Partner API instead put a real payment request on the device
with a fresh per-send merchant session. The
blocked list is now empty — the last gate flipped in `proofs/gates.yaml` on
2026-07-28 — so from here the G.1 completion date is a function of our own
work, not of Apple lead times.

**Precondition 2 is murkier than the workbook makes it sound.** There is no
Apple sandbox — every live send from this repo hits production Apple infra,
which is why `proofs/AGENT.md` rate-limits live sends rather than pointing at a
test environment. What we have is an MSP-level test business (`AMB_BIZ_ID`, ABR
platform `cerebro-dev`) that the dev loop drives end to end from a real iPhone.
**Precondition 2 flipped to MET on 2026-07-28** when `abr-connect` was granted:
the Connect flow was driven end to end from a real ABR-initiated journey on the
`cerebro-staging` MSP — Apple's Connect link, our landing page, an operator OIDC
sign-in, and a `linked` outcome asserted in the database, not just on screen
(`proofs/gates.yaml` § `abr-connect`).
**Read the scope before treating this as review-ready:** the grant is
TEST-ACCOUNT-SCOPED, on an MSP registered **Private**. Broad availability — the
Connect link a brand finds without a test-connection screen — is NOT claimed and
remains a launch item under `apple-approvals-final`. What "sandbox brand" means
for the review is still worth clarifying with MA rather than assuming a linked
test business satisfies it; that question is now narrower, not answered.

**Precondition 3 has no artifact yet.** No demo-script document exists under
`docs/`, and no rehearsal has happened. The nearest things that exist are
`scripts/breadth-sweep.sh` (which walked 6 of 7 canonical part types on a real
device) and the `work/W-026` draft for a full 74-item live sweep. The check
above is deliberately routed through G.3/G.4 rather than through file existence:
writing a script is not rehearsing one, and the recording items are what produce
evidence that it was actually run. The rehearsal must include the deliberate
capability fallback MA calls for — which is currently impossible, because D.4
does not exist (see G.2 requirement 5).

**Precondition 4 is genuinely met**, with a scope caveat. The demo agent runs on
our rails: `make prove-agent` drives inbound → journal → signed webhook →
the demo partner agent (linq-team/cerebro-brand-curbfare, real Claude Opus) → Partner API send → delivery machine
→ Apple. The bot side is the partner agent itself: W-556 deleted the platform's
deterministic flow engine, because cerebro is the rails and the partner's agent
is the bot. "Operational" here means operational on the dev loop against our test
business — not operational against a provisioned review brand, which is
precondition 2's problem.

### What actually gates the rest

Measured 2026-07-25 over the `in_progress` set as it stood then, and it was not
what the burn-down rate suggested: **the large majority were not waiting on
code** — their contract planes passed, their live planes passed, and what held
them open was a fact a person has to witness on a screen or a decision a person
has to make. C.6 and C.14 both went green in a single sitting with a phone, on
work that had been finished for a day or more. C.21 is the exception on today's
board: it took its START credit on 2026-07-29 and is waiting on code *as well as*
a witness — its remaining GUI slice lands in zero-web (`linq-team/zero-web`,
the first-party desk over the zero listener; the console it first landed in was
retired by W-571) under that repo's loop, and no `proofs/flows/C.21.sh` is
authored, so its live plane reports `no_proof` rather than passing.

The remaining debt, per item note:

| Item | Owed |
|---|---|
| C.5 | An **auto-promoted** URL card on-device, plus enrichment / Maps POI / video — the last three ride on W-059 slices 3 and 5, still `implementing` |
| C.21 | The week-6 FINISH pass: the templates screen (zero-web's `useAmbTemplates`, slice B; the cerebro-console screen it replaced was retired by W-571), then the demo dry-run — List/Time Picker, Quick Reply and Form composed in the GUI, sent, and screen-recorded. No live send has run for this row |

C.3 turns on its own reply-normalization work rather than a render glance, so it
is not cleared by a device session. (C.9 used to sit here for the same reason —
a manual human-witnessed send rather than a harness bundle — and no longer does:
it has an armed bundle as of 2026-07-29.)

Two consequences worth stating plainly, because both are cheap to get wrong:

- **`live: PASS` is not the same claim as "a human saw it."** It means Apple
  accepted the payload. An item whose only remaining debt is a render witness can
  sit green-on-every-plane for weeks and still be honestly `in_progress`. That is
  the rig working, not the rig being pedantic.
- **The glance has to be scheduled, not recovered.** Typing indicators are
  ephemeral and interactive renders scroll away; chat.db cannot reconstruct
  either. Arm the flow with the observer already watching. On 2026-07-25 the
  first armed C.14 run passed both planes and had to be re-run purely because
  nobody was looking at the phone when it fired.

**Know which view you are looking at before you call something missing.** C.8's
event artwork and its map both render only when the customer *taps the reply
bubble* their selection created — not in the picker, which is the obvious place to
look. Looking in the picker produced, twice in one session, a confident report
that Apple had ignored coordinates we demonstrably put on the wire. The check that
prevented it becoming a filed finding was verifying our own bytes first
(`TestProof_C8` asserts them against recorded applesim wire bytes), then asking
*where* the observer had looked. Both are cheap; a wrong entry in the MA-facing
discrepancy register is not.

**Check whether a stated blocker is still true before planning around it.** C.17
sat open on a premise written into two places — its own note and
`proofs/gates.yaml` — that the only FORM-announcing device lived on the staging
brand and was therefore "unreachable from the prove stack by construction". One
query disproved it: the same Apple ID is signed in on an iPhone that announces
FORM to the *dev* brand, on the chat the flows already use. The real
constraint was that the DRIVER is Messages.app on a Mac, and macOS has no Form
Message. The cost of not checking was a form part that had never once rendered in
this repo's history, and a C.12 plan scoped around a staging flow it does not
need. A blocker recorded once tends to be read forever; re-measure the cheap ones.

**"No driver can do it" is not "it cannot be done."** C.19 spent months recorded
as undrivable — and the investigation behind that was sound: AppleScript cannot
tap "delete this chat", the QA line's `/leave` publishes a group-chat
leave a 1:1 DM has nothing to do with, wisp's soft-delete produced no
CloseSession. All true, and all about *drivers*. MA verifies C.19 by UX Testing,
which is to say by a person, and a person was always able to perform the tap. The
flow now blocks on a human with a bounded wait instead of writing a marker that
excuses the leg. Before recording anything as undrivable, ask whether it is
undrivable *by a machine* or genuinely impossible — the two get written down the
same way and mean completely different things.

**A device session runs on a shared, long-lived fixture chat, and
assertions on it must be scoped to the run.** C.4's first armed attempt reported
that the API had accepted a send to a *closed* chat — a proof crying wolf
about a customer-safety gate. The product was right; the assertion was wrong. It
counted every close the chat had ever seen, so it passed instantly on the
close C.19 had produced minutes earlier, against a chat that had since
reopened. Two consequences worth internalising before the next batch: an
assertion that would pass on history rather than on this run is not an assertion,
and a proof failure touching a safety gate deserves five minutes of verification
before it is written up — the false alarm and the real thing look identical.

A third thing the 2026-07-25 session established, and it is not a scheduling
point: **an item can owe a render its own flow cannot produce.** C.6's only
quick-reply fixture had three items, so it could never have discharged a debt
stated as "a 2-item and a 5-item picker"; C.7's flow sent one picker and its
header still claimed cerebro could not emit images at all, which W-043 had made
false. Both were fixed by strengthening the flow — never by reading the existing
render as good enough. Before booking a device session for an item, check that
its flow actually sends the thing the note says is owed.

The practical read: these items are cleared in **batched device sessions**, not by
the autonomous loop, and scheduling one is the highest-leverage thing available
for precondition 1. Engineering effort spent elsewhere does not move this number.

### What G.1's lint does and does not assert

It asserts the precondition inventory exists, that its four verdicts and the
Section C tally are recomputed from `proofs/checklist.yaml` and
`proofs/gates.yaml` and match, and that G.1 is not `green`/`done` while any
precondition is unmet. It does **not** assert we are close to review-ready; the
numbers above are the answer to that, and the answer is no.

---

## G.2 — the five non-negotiable UX requirements

The MA workbook (Apple Master Guide p. 11, §2.4 Non-Negotiable Requirements)
names five things the submission must demonstrate. The kit's provenance register
confirms the set at §28.6: *"Re-verified consistent on screen-recording
requirement, three review dimensions, five non-negotiable UX requirements … The
five non-negotiable UX requirements that v5.0 captured are confirmed consistent
with DOC 1.1 content"* (kit L13047). MA's own note: these are tested every
review, and skipping one is the most common failure mode.

G.2's week-7 pass is **START** — stand the inventory up and make it honest. The
week-8 pass is sign-off, and that one requires all five green.

Each requirement is backed by the checklist items that actually implement it. A
requirement is **MET** only when every backing item is `green` or `done`;
**PARTIAL** when some are; **UNMET** when none are.

| # | Requirement | Backing items | Today |
|---|---|---|---|
| 1 | Live agent escalation reachable | E.1, F.1, F.2 | PARTIAL |
| 2 | Opt-out works end to end | E.5, E.6 | PARTIAL |
| 3 | No PII requested in plain chat | E.7 | MET |
| 4 | Consent captured before any opt-in notification | E.4 | UNMET |
| 5 | Capability-aware fallback shown live | D.1, C.17, D.4, D.5 | MET |

**2 of 5 met as of 2026-09-21** (3 of 5 on 2026-09-18; 4 of 5 on 2026-09-17:
row 2 went PARTIAL when W-590 moved E.5 to `blocked` pending MA, and row 4
went UNMET when W-599 retired the consent model by owner direction, E.4 now
`na`; see the opt-out and consent paragraphs below). W-556 deleted the platform flow engine on
2026-09-14 and withdrew the proofs that cited its copy (the table read 1 of 5
for three days); slice 4 re-proved E.4, E.6, E.7 and F.1 against what cerebro
still owns — the consent model, the trigger-word matrix and the pause, the
platform's own copy surfaces, detection plus the informational event (W-570
slice 1, the same day, retired the managed seize) — and they are green again
on zero-send policy planes. Row 1 is
PARTIAL by owner decision rather than by a gap: E.1 (a staffed live-agent
desk) and F.2 (the callback-or-email choice) are the PARTNER's to prove, so
they read `na` on the board; the platform's half of the requirement, F.1, is
green. A reviewer sees the partner agent (linq-team/cerebro-brand-curbfare)
on camera, and that agent's desk and its escalation copy are what would close
row 1. G.2 cannot be green and must not be reported as ready.

**Opt-out (2): the partial-stop layer moved to the partner (W-556).** Until
2026-09-14 a customer who asked only the automation to stop ("stop the bot")
got a platform Quick Reply asking what they meant (W-091, on MA's guidance of
2026-07-27 that Apple defines no partial opt-out). The platform still pauses
the automation before anything renders and still delivers the match
(`chat.trigger_word{stop_automation}`); the question is now the partner
agent's to ask (`docs/partner-api.md` § Recipes). A bare STOP is different
since W-590 (owner decision 2026-09-18): the platform records it, delivers it
to the partner, and itself blocks `marketing` and `account_notification`, but no
longer refuses the in-conversation reply, which is the partner's to stop and
which is journaled when sent (`send_after_opt_out`; D-050). Leave Chat is still
enforced by the platform for every send. The honest limit,
stated here because an Experience Review reviewer may ask: the platform cannot
see who typed an outbound message, so "a human agent may continue" is enforced
as "only the accepted-handoff owner may speak" (D-033).

**Opt-out (2) is PARTIAL since 2026-09-18, by owner decision rather than by a
regression (W-590).** E.5's verbatim row ("both bot and live agent must stop
sending immediately") was enforced literally from 2026-07-23: every send after
a typed STOP was refused, the in-conversation reply included. W-590 reversed
that for `transactional` sends on Apple's own text, which scopes a typed
unsubscribe to message preferences and reserves the platform-level block for
the `close` event. What the platform does now: it detects the word, delivers it
to the partner, blocks `marketing` and `account_notification` itself, and
journals every send accepted while the opt-out stands (`send_after_opt_out`);
stopping the reply is the partner's. Whether MA's row requires more of a typed
word is a spec dispute, so E.5 is `blocked` on the board with that reasoning
(D-050) instead of green, and its proof still runs against what ships. E.6 is
green. A reviewer should hear this plainly rather than discover it.

**How row 2 got to MET in the first place (2026-07-24).** E.5 (brand-scoped
stop, including `QUIT`) and E.6 (the full HELP/STOP/AGENT/REPRESENTATIVE matrix,
each mapped to a defined behaviour) were both `green` on the board. W-046 built the standardized
trigger-word matrix plus brand-scoped opt-out capture; W-047 enforced consent on
the send path with an accept-time gate and delivery-time suppression, so an
opt-out stops an in-flight chat rather than only recording state — which
was the specific gap an earlier revision of this section described. The *in-band*
half (Apple's Leave Chat / close event) is separately proven under C.4.

**What MET does not mean here**: it means every
backing item is `green`, not that the behaviour has been rehearsed in front of a
reviewer. E.5/E.6's live planes carry their own residue — see their checklist
notes — and the keyword matrix is English-only (kit L8396).

**Escalation (1) is PARTIAL: F.1's deterministic floor is green, E.1 and
F.2 are the partner's.** F.1 first flipped `green` on 2026-07-24 (W-048) and
again on 2026-09-17: a standardized trigger-word table matched on every
inbound with no flow-state condition (`internal/domain/triggers.go`), and —
since W-570 slice 1, the same day — the platform HANDLES nothing past the
match: a partner-owned escalate is told to the partner as an informational
`chat.trigger_word` (`handled_by: "partner"`, no delegation block), nothing
is queued, no acknowledgement is promised, and one latency watch pages if the
partner's path stays silent. (W-048's seize into `human_pending` and its
`ack_by` deadline were retired with the managed mode.) What F.1's green does
**not** claim is the free-text *NLU* half of MA F.1 (`this isn't helping`) —
cerebro has no LLM in the serving path (D12), so that half is the partner's
NLU calling `POST /v1/chats/{chat}/handoff`, argued to MA as the
compositional answer (`docs/escalation-intent.md`). The requirement stays
PARTIAL by owner decision (2026-09-17): F.2 (a structured callback-or-email
choice) and E.1 (a live agent to receive the handoff) read `na` — the
partner's to build and to prove — and the platform's half cannot make them
green. E.1 is a backing item rather than a footnote precisely because without
a person at the other end escalation remains untestable end to end.
Apple is explicit that a live agent must be available for escalation testing: *"once testing of the automated agent is complete, you'll need a live
agent available to test any use cases that would escalate to a live agent"*
(kit L9715).

**Fallback (5) flipped to MET on 2026-07-27 — the live demonstration now
exists.** This paragraph used to read "the switcher exists, the live
demonstration does not." D.4 (send-time capability switcher) and D.5
(documented fallback decision tree) landed with W-044 (`amb.Degrade` in both
send paths). C.17 went green 2026-07-25 (the identical `form` part refused
`409 capability_unsupported` on the FORM-less Mac and delivered `sent` to the
FORM-announcing iPhone in the same minute), and D.1 went green 2026-07-27 with
the real two-device switch run armed on one chat: the iPhone's
announced set persisted, a Mac inbound replaced it (FORM gone), a second
iPhone inbound restored it — most-recent-wins observed live in both
directions, no leg simulated. Apple's expectation of an end-to-end downgrade
demonstration (Form floor iOS 18.4, kit L3177; fallback strategy guide §5.3 /
§17.5) and G.1's *"deliberate device-capability fallback"* dress-rehearsal
beat now have their live witness on the board.
That rehearsal is the remaining work, not the mechanism.

**The two met requirements are met by policy proof, not by live demo.** Read
them that way.

**PII (3).** E.7 is green on `proofs/policy/E.7.sh` — no chat copy
requests sensitive PII, and the demo agent's prompt routes collection to
Authentication / Apple Pay / Form messages. A reviewer asking to *see* PII
handling live would be exercising C.10 or C.12. Neither is gate-blocked any
more — C.12 is already green (2026-07-26, matching this document's own
Precondition 1 paragraph and C.12's checklist note; its evidence bundle is
stamped 20260727T012344Z because the run landed just after midnight UTC) and
C.10's OAuth gate was measured granted for staging on 2026-07-27 — but C.10
has no live proof plane yet, so the honest answer to that request today is
C.12.

**Consent (4) is UNMET by owner direction (W-599, 2026-09-21).** From
2026-07-21 (W-032) to 2026-09-21 cerebro held a consent model end to end:
`consents` keyed per brand + category + subject with append-only
`consent_events`, the pure decision and Apple's two-year ceiling, an
accept-time gate and a delivery-time re-check, capture by inbound keyword and
by brand attestation (`POST /v1/consent`), lifecycle webhooks and the expiry
sweep. The owner retired it: the opt-in is the brand's under Apple's Service
Terms § 2.12 (its opt-in, POS-collection, two-year cap and per-update opt-out
duties are written on *"a Business"*, and the only clause reaching the MSP is
*"A Business and/or its MSP shall only use Apple-authorized templates"*), a
copy of the brand's own claim held by us is evidence of nothing, and no send
is refused for its absence. What cerebro records instead is what the customer
typed (the chat's standing opt-out, delivered as `chat.trigger_word`) and
every send accepted over it (`send_after_opt_out`), both proven under E.5.
E.4 is MA's workbook line and reads `na` on the board with the decision in
its note; `proofs/policy/E.4.sh` is deleted with the gate it pinned. The
owner also directed that accreditation is not a constraint on this change, so
no question is raised with MA. A reviewer who asks to *see* consent captured
before an opt-in notification will be shown the partner's point of sale and
the platform's record of the customer's keywords, not a platform gate.

### What G.2's lint does and does not assert

It asserts the five are **tracked and accurately reported** — the mapping above
exists, every backing item resolves to a real checklist item, each `Today`
verdict is recomputed from the board and matches, and G.2's own status is not
`green`/`done` while any requirement is short. That is what a START pass can
honestly prove.

It does **not** assert the requirements are satisfied. It cannot: two of five
are still short, and capability-aware fallback is a *live* demonstration
requirement that no offline lint can stand in for. When the backing items go
green the lint's verdict flips on its own, which is the point — G.2 cannot
report ready while its constituents are gaps.

---

## G.3 — capability readiness for the three Experience Review recordings

**What this section is, and what it is not.** G.3 asks for three unedited screen
recordings. Making them is a *human* act with a camera, and this document does
not track it, claim it happened, or stand in for it. What this section inventories
is the other half: **can the platform actually perform, on demand, each flow those
recordings have to show?** A precondition discovered missing here costs an
afternoon; the same one discovered mid-take costs the take, and G.4 forbids
stitching a second one in (*"If two takes are needed, submit the second take in
full, not a stitched composite"*).

MA's requirement, verbatim: record a **bot flow** (entry point through resolution
or escalation), an **agent flow** (entry point through agent resolution), and a
**capability flow** showing the same use case on a device that supports the
feature and on one that does not, *"demonstrating the fallback to Quick Reply,
List Picker, Time Picker, or plain text in place of Form Message"*. Each take
must include **the entry point and a Leave Chat**, and must be one
continuous take. Its key considerations add: *"Ensure inivitations can be
demonstrated in bulk. When it cmes to real traffic, no more than 1000
messages/second (for the time being)"* [sic, both typos are the workbook's].

That is six distinct capabilities. `proofs/policy/G.3.sh` re-derives each row's
verdict **from the source tree** — routes from the mux's own route table, the
fallback tree from the rule ids in `amb.degradeOne`, the rate ceiling from the
migration that seeds it — not from this prose, and fails when the two disagree.

A row is **READY** only when everything it needs is present and reachable today.
**PARTIAL** means the machinery exists but something the recording actually shows
is missing or off by default. **MISSING** means the capability is not built.

**One layer is settled and must not be confused with another.** The **capability
matrix is fully approved** for the `cerebro_dev_jonathan` and
`cerebro_staging_jonathan` brands — Apple permits these brands to use FORM, Pay,
App Extension and Auth. That is the owner's own verification, dated 2026-07-30,
recorded here as his rather than as anything this repo measured. It settles the
**brand grant**. It says nothing at all about the **device announcement**, which
is a different layer: capability lists arrive per inbound and the most recent one
wins (D.1), and a Mac cannot announce a capability macOS does not have — Form is
iOS/iPadOS 18.4 and later (kit L3177), which is why C.17 stalled until the same
whitelisted Apple ID sent from an iPhone. G.3's capability flow lives entirely in
that second layer. A fully approved brand still meets a device that cannot render
a form, and the only question that matters is what the platform does at that
moment. Row 4 is that question. The useful consequence of the grant is that a
genuine two-device demonstration is now performable on either brand — so
whatever row 4 is short on is **ours to fix, not Apple's**.

| # | What a take has to perform | How it is checked | Today |
|---|---|---|---|
| 1 | Entry point on camera — a `bcrw.apple.com` link carrying `biz-intent-id`/`biz-group-id`, routed by the partner's agent | the edge journals both parameters on the inbound and `message.received` carries them as `intent`/`group_id`; the platform records no routing decision since W-556, so the routing shown on camera is the partner agent's; C.15 reads `na` (the partner's, 2026-09-17) and the forwarding is pinned by `TestEntryPointParamsForwardedWithoutRouting` | READY |
| 2 | Bot flow, entry point through resolution **or escalation** | the partner agent (linq-team/cerebro-brand-curbfare) is the bot since W-556; `domain.TriggerEscalate` is the platform's floor and F.1 is `green` again on it (re-proven 2026-09-17); F.2, F.3, F.5 are the partner's (`na`, owner decision 2026-09-17) and F.4 is deleted, so what the take shows past detection is the partner agent's own copy | READY |
| 3 | Agent flow, entry point through **agent resolution** | the two D18 routes (`/handoff`, `/handoff/accept`; `/resolve` left with the flow engine, W-556) in the mux route table + the ownership transition table; but E.1 is `na` (a staffed desk is the partner's, 2026-09-17) and the first-party desk is zero-web over the zero listener, not a cerebro surface (C.21 `in_progress`; the console was retired by W-571) | PARTIAL |
| 4 | Capability flow — the fallback that replaces a Form Message on a device without FORM | `amb.Degrade` (`internal/channel/amb/fallback.go`) and its `guide-17.5-*` rule ids; but the tree never emits a Time Picker (D-023) and the Partner API default is a `409` refusal, not a fallback | PARTIAL |
| 5 | Leave Chat, in every one of the three takes | the edge maps Apple's `close` to `domain.EventChatClosed`; `PhaseClosed` + the `chat.closed` webhook; C.4 and C.19 `green`; **no programmatic driver exists** — it is a human thumb, which is what a recording is | READY |
| 6 | Invitations demonstrable in bulk, real traffic ≤ 1000 msg/s | the four `/v1/invitation_batches` routes + the fan-out writer; `send_rate_buckets` seeds the global scope's `configured_rate` at exactly 1000; but W-090's slice 6, *"The G.3 bulk demonstration + a `proofs/` artifact for it"*, is unbuilt | PARTIAL |

**3 of 6 ready.**

### The gaps, stated plainly

**Row 4 is the one that would break a take, and it is worth reading twice.** An
automatic platform-side fallback *does* exist — `amb.Degrade` rewrites a
FORM-only part into a Quick Reply, a List Picker or plain text, and D.4 proved it
end to end on a real device. But two properties of it decide what a camera can
actually record:

1. **On the Partner API the tree is opt-in and off by default.** A send with no
   `degrade` field — or `"degrade":"reject"` — is refused `409
   capability_unsupported`, exactly as it always was. Only `"degrade":"auto"`
   (or `"acknowledged"`) runs the tree. **A 409 is not a fallback**; on camera it
   is a message that never arrives. Bot flows are the exception: `flowSendGate`
   degrades unconditionally, because a flow has no synchronous caller to hand a
   409 to.
2. ~~**The staging agent that would be on camera does not pass the flag.**~~
   **CORRECTED 2026-07-30 — THIS WAS WRONG, and it was the audit's headline gap.**
   The deployed staging agent handles the refusal properly: `staging/agent.mjs`'s
   single `send` path posts the full-fidelity part first, and on
   `capability_unsupported` **re-sends the same part with `degrade: "auto"`**,
   then reports what the customer actually saw back to the model — *"sent, but
   their device could not render form — the customer saw a quick_reply instead"*,
   read from the response's own `fallbacks[0].to`. D.4's note (*"sends forms
   without degrade and takes the 409"*) describes the FIRST attempt and omits the
   retry; this section repeated it without reading the agent.

   So a capability-flow take driven by the deployed CurbFare agent shows a real
   downgrade today, and needs no code change. The try-then-degrade shape is also
   better than defaulting the flag: the richest form is attempted first, and the
   degradation is observed and narrated rather than silent. The `409` is not a
   dead end — it is the documented signal, which is what `service.go`'s own
   comment calls it. (The local dev example, `partner-agent/agent.mjs`, does NOT
   retry; it tells the model to choose different content. That is a legitimate
   second strategy, and it is not the agent that would be recorded.)

**Row 4, second gap: we cannot demonstrate a Time Picker fallback at all.** MA
names four acceptable substitutes for a Form Message — Quick Reply, List Picker,
Time Picker, plain text. The tree produces three of them. A `datePicker` page
degrades to **plain text**, unconditionally, under rule
`guide-17.5-datepicker-to-text`; nothing in the FORM-absent arm ever emits a
`time_slots` part. That is deliberate and disclosed — Apple's Time Picker offers
future appointment slots while a `datePicker` asks for an arbitrary date, so the
literal reading of §17.5 would silently drop past dates — and it is filed as
**D-023** in `docs/spec-discrepancies.md`, open, to report. The consequence for
the recording is concrete: choose Quick Reply or List Picker as the demonstrated
fallback. A take built around "and here is the Time Picker instead of the form"
cannot be produced by this platform, and finding that out with the camera running
is the expensive way to learn it.

**Row 3: the agent side of the agent flow has an API, not a desk.** `/handoff`
and `/handoff/accept` exist (`/resolve` left with the flow engine, W-556) and the D18 ownership table moves
`partner → human_pending → human → partner` correctly. What does not exist is a
human-facing surface — **CORRECTED 2026-07-30: that is also wrong.** A console
existed (`../cerebro-console`) and was deployed to staging, the `console` and
`console-server` Deployments both 1/1 Ready. **CORRECTED AGAIN 2026-09-21 (W-571):
that console is retired; the human-facing surface is zero-web, over the zero
listener, which honours `X-Cerebro-Operator` on its own key kind.** What survives
from E.1's note is the auth half on the partner API — the partner key wearing the
human role, with no per-operator identity there (D.3) — and C.21 (the GUI row) is
still `in_progress`. An agent-flow take on cerebro's own surfaces therefore has
to show the agent's half as API calls — the proofboard's console, or curl — or
be shot in zero-web. That is honest and it is recordable, but it is
worth deciding on purpose rather than discovering it while framing the shot,
because Apple's third review dimension is literally *"Agent interaction"*
(kit L9725).

**Row 6: the bulk-invitation demonstration is the one piece nobody has built.**
The pipeline underneath it is merged and real — submit, screen, admit, fan out,
poll, cancel — and the ≤1000/s ceiling is not a promise but a row:
`send_rate_buckets` seeds `('global','*', …, configured_rate 1000, …)`, applied
as a cap, with an operator `UPDATE` (no deploy) as the way to move it. But
W-090's own slice table has a slice 6, *"The G.3 bulk demonstration + a `proofs/`
artifact for it"*, and it is unbuilt; W-090 is still `implementing`. There is
today no scripted way to stand up a bulk run for a camera and no artifact
describing what such a run should show.

**Row 5, the constraint that is not a gap.** A customer-initiated Leave
Chat is fully visible to us: Apple sends a `close` envelope in the
`notification` header class, the edge journals `chat_closed`, the fold
moves the chat to `PhaseClosed`, the partner gets `chat.closed`,
and a later send is refused `409 chat_closed`. C.4 and C.19 are `green`
on real hardware for both documented `sourceId` shapes (D-029). What does *not*
exist is any way to **cause** one programmatically: synapse's
`/v3/internal/amb/chats/{biz}/leave` returns 202 and does nothing (group-chat
semantics against a `style=45` DM), wisp's soft-delete produces no CloseSession,
and AppleScript cannot reach the Messages info menu. Every proof flow that needs
a close blocks on a person. For G.3 specifically this is fine — the requirement
*is* a person tapping it on camera — but it means the takes cannot be rehearsed
by automation, and it is why row 5 reads READY with a driver caveat rather than
READY without one.

### What G.3's lint does and does not assert

It asserts that the six capabilities above are present and reachable in this
tree, that each verdict here is recomputed from the source rather than read from
this prose, and that G.3 is not `green`/`done` while any row is short or while
its declared dependencies (G.1, G.2) are.

It does **not** assert that any recording exists, was made, was made in one take,
or was accepted. It cannot: no lint can watch a screen. G.3 stays `not_started`
until the recordings themselves are the evidence. A PASS from
`proofs/policy/G.3.sh` means exactly one thing — **the platform can perform the
flows the recordings require** — and today it means that with three rows short.
