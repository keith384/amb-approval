# Decision Record DR-13: Read receipts

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #13._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Read receipts
- **Apple's silence:** Read receipts documented for iMessage person-to-person; no explicit AMB business-context documentation found on any Apple-owned source.
- **Evidence strength (per canonical):** No Evidence
- **Specification depth:** No Spec

## Options

- **Do not surface read receipts (recommended)** — Apple documents read receipts for person-to-person iMessage, not AMB business context. Treat delivery (200 OK) as the only confirmed signal.
- **Surface optimistically** — Rejected: would assert a 'read' state Apple does not confirm delivering for AMB — misleading to agents.
- **Make it a per-brand toggle** — Acceptable if defaulted OFF and clearly labeled 'delivery, not read'.

## Recommended default

Do not display 'read' status in the agent console for AMB. Map the 200-OK response to 'delivered'. Revisit if Apple documents AMB read receipts.

## Notes

No AMB business-context read-receipt spec exists (gap #13). Delivery ≠ read.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
