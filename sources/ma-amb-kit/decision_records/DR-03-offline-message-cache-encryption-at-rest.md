# Decision Record DR-3: Offline message cache encryption-at-rest

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #3._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Offline message cache encryption-at-rest
- **Apple's silence:** No specification of encryption-at-rest algorithm for cached messages.
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **AES-256-GCM at rest (recommended)** — Authenticated encryption for cached/queued messages; widely certifiable (FIPS 140-2/3).
- **Envelope encryption via cloud KMS** — Per-record data keys wrapped by a KMS master key; strong key rotation and audit story.
- **No at-rest encryption** — Rejected: message bodies contain user content; unencrypted cache is a compliance and breach risk.

## Recommended default

AES-256-GCM with keys held in a managed KMS; rotate master keys; encrypt any message cache, attachment blob, and queue.

## Notes

Apple specifies no at-rest algorithm (gap #3); this is entirely MSP policy. Aligns with the ISO 27001/27018 posture Apple does cite.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
