# AMB Kit — Apple Messages for Business, machine-usable layer

A validated, self-regenerating layer over the byte-verified AMB canonical
(`AMB_Layer2_Canonical_v7_0.md`). It turns Apple's prose into tool-consumable
schemas, an API skeleton, test fixtures, a conformance matrix, and decision
records — while preserving provenance and never inventing what Apple didn't state.

## One command regenerates everything

```bash
python3 build_all.py            # uses the kit's canonical (carries the C4 ligature fix)
python3 build_all.py /path/to/AMB_Layer2_Canonical_v7_0.md   # or point at another canonical
```

Runs, in dependency order, each step self-validating (the run **aborts** on any
failure, so a broken artifact is never emitted):

1. `build_index.py` → `amb_index.json` (navigation + overlay tables + provenance)
2. `extract_fixtures.py` → `fixtures/`, `type_enrichments.json` (worked payloads by message type)
3. `extract_schemas.py` → `schemas/`, `structural/`, `amb_schemas_bundle.json`, `schema_coverage_report.md`
4. `validate_fixtures.py` → `fixtures_validation.md` (fixtures vs schemas)
5. `build_openapi.py` → `amb.openapi.json`
6. `build_conformance.py` → `conformance_matrix.json`, `conformance_checklist.md`
7. `build_decision_records.py` → `decision_records/`
8. `generate_reference.py` → `AMB_Schemas_Reference.md`

## What's in the box

| Artifact | Use |
|---|---|
| `amb_schemas_bundle.json` · `schemas/*.json` | 49 object schemas (47 dictionaries + HTTP Body & JWT), draft 2020-12, provenance on each. Machine-consumable. |
| `structural/required-features.json` · `response-codes.json` | Apple's approval matrix + HTTP response codes as structured data. |
| `amb.openapi.json` | OpenAPI 3.1 skeleton: 9 Apple operations + 7 integrator webhooks. `/message` wired to HTTP Body. |
| `fixtures/` + `fixtures_validation.md` | Worked request/response payloads grouped by message type, validated against the schemas. |
| `conformance_checklist.md` · `conformance_matrix.json` | Each required feature → schema(s) → endpoint(s) → fixture(s). Maps to Apple's approval criteria. |
| `decision_records/` | The 7 points Apple leaves to you (rate limits, at-rest crypto, TLS, read receipts, geo, SOC 2, managed accounts) with options + a recommended default. |
| `AMB_Schemas_Reference.md` | One human-readable file: every schema, fields, types, provenance. Reference/citation copy. |
| `schema_coverage_report.md` | **The honesty layer.** Every place Apple's source was silent/ambiguous and the tool declined to guess. |

## The faithfulness contract (non-negotiable)

Schemas assert **only what Apple's tables state**. Provenance (`x-amb`: source, rank,
version, date, exact canonical line span) rides on every artifact. Where the source is
silent, the tool emits a permissive node and logs it — it never invents a type. Types
inferred from worked examples are tagged `x-amb-enriched-from-fixture` (with observation
count) so they're never confused with Apple-stated types. Enum-in-prose is detected, not
auto-encoded. Every generator refuses to emit on validation failure.

## Scope

Covers the `"Dictionary"`-headed tables plus the explicitly-added structural tables
(HTTP Body, JWT, Required Features, Response Codes). **Everything else in the canonical
remains prose** — this is not the complete AMB object model, and the coverage report says
exactly what's left to a human.

## Honest boundary

Nothing here has been exercised against Apple's live service. There is intentionally **no
hand-authored reference client** — it couldn't be validated and would ship false assurance.
The fixtures harness is the correct substitute.
