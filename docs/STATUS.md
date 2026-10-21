# Status & source inventory

_Last updated: 2026-10-21_

## Phase tracker (build sequence from the plan)

- [x] **Phase 0 — Rule set foundation.** `packages/rules/build_rules.py` normalizes the
  MA 114-case checklist → `rules.json` (114 rules: 23 Non-negotiable, 83 Apple standard,
  8 Field). Test asserts source anchors, severity, gate items. _Remaining in Phase 0:_
  letter-ID aliases from the Ramp report; applies-when → `scope.json` key normalization;
  stage tagging (doc/storyboard/video) beyond the default; regression-corpus + versioning
  harness; fold in Standards 2.1–2.18 anchors and the AMB-kit element limits.
- [ ] **Phase 1 — Video Review tool (Tool 3).** ffmpeg 5fps → OCR → event detection →
  rule eval (deterministic + LLM) → Ramp-format report. Test pair = Ramp recording + MA report.
- [ ] **Phase 2 — Brand Approval Doc generator (Tool 1).**
- [ ] **Phase 3 — UX Storyboard tool (Tool 2).**
- [ ] **Phase 4 — Slack bot + feedback ingest/reconcile.**
- [ ] **Phase 5 — Pipeline board (Vercel + SSO, blob upload, worker).**
- [ ] **Phase 6 (scoped, unscheduled) — HubSpot one-way sync.**

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

## Still NEEDED from Keith
1. **Apple onboarding email (9 Sep 2026)** — naming/embargo/PR rules the terminology lint
   enforces. The 21 Oct drive-download zip contained only the two Apple forms, not the email.
   → Paste into `sources/apple-onboarding-2026-09-09.md`.
2. **Walmart brand nomination doc** — the Tool 1 narrative template. Shared as a Google Doc
   link (needs export; I can't fetch an authed Google Doc). → Export to PDF/markdown into
   `sources/examples/walmart-brand-nomination.*`. Ramp's doc is in `sources/examples/` as fallback.
3. **First real Apple feedback reply** (whenever one exists) — decides how much of the
   `/amb feedback` ingest can be parsed automatically (open question in the plan).
