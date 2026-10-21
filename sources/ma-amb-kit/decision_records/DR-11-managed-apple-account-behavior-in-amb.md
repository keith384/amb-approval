# Decision Record DR-11: Managed Apple Account behavior in AMB

_Status: **OPEN — integrator must decide.** Generated 2026-07-09 from amb_index.json gap #11._

> **These options and the recommended default are INTEGRATOR POLICY RECOMMENDATIONS — engineering guidance, not Apple specification.** Apple is silent on this point (see Context), so the behavior becomes your platform's own policy.

## Context (what Apple does / does not say)

- **Topic:** Managed Apple Account behavior in AMB
- **Apple's silence:** DOC 2.2 (Brand Onboarding) confirms a corporate Managed Apple Account may be used for AMB account login by the registering Business. **Still absent from any Apple source:** customer-side behavioral differences, restrictions, or enterprise admin controls specific to AMB for Managed accounts when used as the consumer-side Apple Account. Business-registration use is documented; consumer-side use is not.
- **Evidence strength (per canonical):** Direct Gated Apple (registration-side) / Referenced Only (consumer-side)
- **Specification depth:** Partial Spec (registration); No Spec (consumer-side)

## Options

- **Treat like a standard Apple Account** — Simplest; assumes identical AMB message flow. Risk: Managed accounts may have org-imposed restrictions Apple hasn't documented for AMB.
- **Support with documented caveats (recommended)** — Enable, but sandbox-test the full lifecycle and surface any org-policy limitations to the brand.
- **Block Managed accounts** — Rejected without evidence they misbehave; over-restrictive.

## Recommended default

Support Managed Apple Accounts; verify opaque-ID issuance, opt-out, and attachment flows in sandbox before GA; document any observed differences.

## Notes

Onboarding docs confirm a Managed account may be used for AMB login, but per-message behavior is unspecified (gap #11). Verify, don't assume.

## Decision (fill in)

- **Chosen option:** _____
- **Owner / date:** _____
- **Rationale:** _____
- **Revisit when:** Apple publishes guidance, or the referenced canonical gap changes.
