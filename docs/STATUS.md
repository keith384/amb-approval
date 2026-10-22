# Status & source inventory

_Last updated: 2026-10-22_

## Phase tracker (build sequence from the plan)

All 7 components built end-to-end and chained (scope.json → shotlist.json → findings),
reading one versioned rule set, writing to shared brand folders the board renders.

- [x] **Phase 0 — Rule set.** `packages/rules` → `rules.json` (114 rules; 23 Non-negotiable,
  83 Apple standard, 8 Field) + Ramp letter-ID aliases; test asserts source anchors/severity/
  gate items. _Open:_ applies-when→scope normalization; regression-corpus/versioning harness.
- [x] **Phase 1 — Tool 3 (Video Review).** extract→OCR(Apple Vision)→typing detector→events→
  deterministic + LLM rule eval→Ramp-format report, with an acceptance harness vs MA's 48
  findings. _Calibration backlog: Fail 1/6 strict (latency, B3-OCR, B1/E4/G11 detectors, LLM
  caveat alignment)._
- [x] **Phase 2 — Tool 1 (Brand Doc).** intake→doc model + Walmart HTML + 2 filled Apple forms
  (57/25) + scope.json + readiness note; terminology lint; form-coverage test.
- [x] **Phase 3 — Tool 2 (UX Storyboard).** validate flow→iPhone frames→2.18 self-check→shotlist.
- [x] **Phase 4 — Slack bot.** `/amb brand-doc|storyboard|review|feedback|status` dispatcher +
  Socket-Mode wrapper. _Needs Slack app tokens to go live._
- [x] **Phase 5 — Pipeline board.** Next.js board reading brand folders; grid, artifact viewer,
  stage/owner controls, tool triggers. _Local v1; Vercel+SSO+blob is the production path._
- [x] **Phase 6 — HubSpot one-way sync.** `hubspot_sync.py` writes 4 deal props + notes; dry-run
  by default. _Needs: `ensure-props --write`, per-brand deal mapping, `AMB_HUBSPOT_WRITE`._

## Sources present (in `sources/`)
- `ma-experience-review/` — MA combined package v1.1 (MD), checklist+test-cases v2.0
  (`.xlsx` + extracted CSVs incl. Appendix A/B), Standards & Best Practices v2.1 (PDF),
  video recording guide v1.0 (PDF), process overview v2.1 (PDF), **Apple intake forms**
  (`Messages-for-Business_UseCases.pdf`, `_Readiness.pdf` — fillable AcroForms).
- `ma-amb-kit/` — Apple canonical schemas, element payload limits, `amb_index.json`.
- `experience-review-readiness.md` — what's true on Linq's platform today (G.1–G.3).
- `examples/` — Ramp review report (MA, 9 Oct, the Tool 3 reference output),
  Ramp brand-approval doc, a filled Use Cases example.

## Sources — received 2026-10-21
- [x] **Ramp recording** confirmed as the **18 Sep take** (MA report's ground truth) —
  `~/Downloads/iMessage demo sep 10.mp4` (git-ignored; reference by path).
- [x] **The two Claude skills** → `sources/skills/amb-experience-review/` (SKILL + 2 refs)
  and `sources/skills/amb-technical-qa/` (SKILL + 5 refs: approval, experience-review,
  platform, payments-auth, elements).

- [x] **Walmart brand nomination doc** → `sources/examples/walmart-brand-nomination.pdf`
  (the Tool 1 narrative template "format Apple receives").

## Decisions / still outstanding
- **Apple onboarding email — SKIPPED** (Keith, 21 Oct): the terminology/naming rules are
  already captured in rule 0.3 + the skills; the docs are the output of record, so the email
  isn't needed as a separate source. The terminology lint stands on 0.3 + the skills.
- **First real Apple feedback reply** (whenever one exists) — decides how much of the
  `/amb feedback` ingest can be parsed automatically (open question in the plan).
