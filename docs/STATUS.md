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

## Sources NEEDED from Keith (blocking later phases)
1. **Ramp recording** — `~/Downloads/iMessage demo sep 10.mp4` (7:34, 592×1280, 30fps).
   Present on disk but **git-ignored** (large media). Tool 3's test input + the MA report's
   ground-truth take. _Confirm this file is the 18 Sep take the MA report was written against._
2. **The two Claude skills** — `amb-experience-review` and `amb-technical-qa` (+ their 7
   reference files). Not in the cerebro zip; they live in the Claude workspace / `/mnt/skills`.
   Needed for: distilled severity buckets (Blocker/Fix/Polish), the 14-question fast triage,
   element capability limits & common-wrong-claim corrections, and the human-readable layer.
   → Export both skill folders into `sources/skills/`.
3. **Apple onboarding email (9 Sep 2026)** — naming/embargo/PR rules the terminology lint
   enforces. → Paste into `sources/apple-onboarding-2026-09-09.md`.
4. **Walmart brand nomination doc** — the Tool 1 narrative template ("the format Apple
   receives"). We have Ramp's as a fallback. → Drop into `sources/examples/`.
5. **First real Apple feedback reply** (whenever one exists) — decides how much of the
   `/amb feedback` ingest can be parsed automatically (open question in the plan).
