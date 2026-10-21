# Decision Record DR-15: Rate limits (volume, per-brand, per-conversation)

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #15._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Rate limits (volume, per-brand, per-conversation)
- **Apple's silence:** No Apple-authored rate limit table published in any source.
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **No self-imposed limits** — Rejected: unbounded send risks 5xx storms and brand-level throttling Apple may apply without publishing thresholds.
- **Static conservative caps** — Per-brand and per-conversation ceilings set well below any plausible Apple limit; predictable but may under-utilize.
- **Adaptive backoff + conservative caps (recommended)** — Honor the documented 5xx retry behavior (Apple retries 4x with exponential backoff from 100ms), add 429-aware client-side throttling, and cap per-brand/per-conversation.

## Recommended default

Adaptive: conservative per-brand + per-conversation caps, exponential backoff on 5xx/429 (start 100ms, ~4 retries, matching Apple's documented server retry), and a global send budget with circuit-breaking.

## Notes

Apple publishes no rate-limit table (gap #15). The only documented timing signal is the 5xx retry policy in the Response Codes section; anchor client behavior to it.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
