# Decision Record DR-2: Business relay TLS version

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #2._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Business relay TLS version
- **Apple's silence:** No statement on whether TLS 1.3 is also supported or planned for the Apple → business relay. TLS 1.2 confirmed; ceiling unknown.
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **TLS 1.2 only** — Matches the one version Apple documents as required. Simplest to certify; forgoes 1.3's latency/security gains.
- **TLS 1.2 + 1.3 (recommended)** — Negotiate 1.3, fall back to 1.2. Apple documents 1.2 as the floor and is silent on 1.3, so offering both is safe and forward-compatible.
- **Require TLS 1.3** — Rejected: Apple only guarantees 1.2 on the relay; forcing 1.3 risks handshake failures.

## Recommended default

Support TLS 1.3 and 1.2; disable everything below 1.2. Pin the documented 1.2 requirement as the hard floor.

## Notes

Re-check on each Apple relay change; the 1.3 question is unresolved upstream (gap #2).

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
