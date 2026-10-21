# AMB Kit — Machine Schemas & API Skeleton (Gap #1)

Derived deterministically from `AMB_Layer2_Canonical_v7_0.md` via the authoritative
line spans in `amb_index.json`. This layer turns the 47 prose "Dictionary" tables and
28 endpoint hits into validated, tool-consumable artifacts — without discarding the
corpus's byte-verified provenance.

## What's here

| Artifact | What it is |
|---|---|
| `schemas/<anchor>.json` | 47 JSON Schemas (draft 2020-12), one per dictionary, self-contained, cross-referenced by `./<anchor>.json`. Keyed by the canonical's unique **anchor**, so the 6 same-named `Payment` dictionaries stay distinct. |
| `amb_schemas_bundle.json` | All 47 in one `$defs` document (`#/$defs/<anchor>` refs) for RAG / single-file consumers. |
| `amb.openapi.json` | OpenAPI 3.1 skeleton: 9 Apple-hosted operations as `paths`, 7 integrator-implemented callbacks as `webhooks`. Validated. |
| `schema_coverage_report.md` | **Read this.** The honesty layer: every place the source was silent/ambiguous and the tool declined to guess. |
| `extract_schemas.py`, `build_openapi.py` | Regenerators. Re-run after any canonical/index revision. |

## The faithfulness contract

Every schema asserts **only what Apple's table states**. Provenance rides along on each
schema under `x-amb` (source doc, rank, version, date, exact canonical line span, the
`↳ source.md L###` citation, and the table layout). Where the source is ambiguous, the
tool emits a faithful node and logs it — it never invents a type:

- **2-column `Name|Description` tables** (e.g. `ReplyMessage`, the `Payment` family) carry
  no machine type in Apple's source. Those fields get a `$comment` saying so, not a guessed
  `string`. The coverage report lists all 7 for hand-typing (worked examples in Gap #2 will
  supply the evidence).
- **`See X` references** are wired to `$ref` only when they resolve to exactly one known
  dictionary; ambiguous/procedure references are left as `$comment` + logged.
- **Array-in-prose vs object-in-Type** mismatches are kept as the source states and flagged.
- **Enum-in-prose** (e.g. ReceivedMessage `style`: icon/small/large) is detected and reported,
  not auto-encoded.

## Current coverage (this build)

47 schemas · 136 properties · 63 required · **all pass draft-2020-12 validation** ·
0 dangling refs. Open items for human verification: 5 prose-only dictionaries, 7 typeless
2-column fields, 1 unresolved reference (a false-positive procedure name), 2 array/object
mismatches, 4 enum-in-prose blocks. All enumerated in `schema_coverage_report.md`.

## Validate / regenerate

```bash
pip install jsonschema openapi-spec-validator
python3 extract_schemas.py     # -> schemas/, bundle, coverage report (self-validates)
python3 build_openapi.py       # -> amb.openapi.json (self-validates)
```

## Honest boundary

This is derivation, not authorship: the schemas are as correct as the canonical tables and
this build's parser. The coverage report is the exact list of what a human still owns. Nothing
here has been exercised against Apple's live service.
