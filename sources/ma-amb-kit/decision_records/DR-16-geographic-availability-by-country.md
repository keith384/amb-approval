# Decision Record DR-16: Geographic availability by country

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #16._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Geographic availability by country
- **Apple's silence:** No Apple-authored country availability list published. AMB is Apple ecosystem only; international availability not specified.
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **Allow all regions** — Rejected: AMB availability is Apple-ecosystem and country-gated; sending into unsupported regions yields silent failures.
- **Allowlist from onboarding (recommended)** — Maintain a supported-country allowlist sourced from Apple Business Register brand onboarding; deny/queue elsewhere with a clear fallback.
- **Geo-gate at the edge** — Acceptable as an enforcement mechanism layered on the allowlist.

## Recommended default

Maintain a per-brand supported-region allowlist derived from Apple Business Register onboarding; on out-of-region targets, fail gracefully with a documented fallback channel.

## Notes

No Apple-authored country list exists (gap #16); availability is confirmed only as Apple-ecosystem-only. Treat the allowlist as living config.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
