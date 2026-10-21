# Decision Record DR-18: SOC 2 status

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #18._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** SOC 2 status
- **Apple's silence:** Not addressed in any Apple-authored source. ISO/IEC 27001 and 27018 confirmed (Section 28.3).
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **Rely on ISO 27001/27018 only** — Apple cites ISO 27001 and 27018 for its own posture; an MSP may inherit that framing but it is not SOC 2.
- **Pursue SOC 2 Type II (recommended where enterprise-required)** — Independent attestation many enterprise brands demand from an MSP; complements ISO.
- **Both ISO + SOC 2** — Strongest assurance story; higher audit cost.

## Recommended default

Document the ISO 27001/27018 baseline Apple references; pursue SOC 2 Type II if your target brands require it in procurement. State clearly that AMB itself carries no Apple-published SOC 2 claim.

## Notes

SOC 2 is not addressed in any Apple source (gap #18); ISO 27001/27018 are confirmed. This is an MSP business/compliance decision.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
