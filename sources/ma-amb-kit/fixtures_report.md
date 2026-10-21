# AMB Fixtures — Extraction Report

_Generated 2026-07-09T04:36:43.893381+00:00 from `AMB_Layer2_Canonical_v7_0.md`._

Worked payloads extracted from the code-example sections. Apple's examples are illustrative JSON with placeholders; normalization fixes only placeholder **syntax** (logged per fixture in `manifest.json`), never field values. Type evidence is taken only from genuine literals.

- Valid fixtures: **74**  ·  Unparsed (kept raw): **34**

## By group

- `apple-pay`: 8
- `authentication`: 3
- `close-session`: 4
- `form`: 6
- `interactive-common`: 3
- `rest-api-reference`: 37
- `text`: 6
- `tutorial`: 7

## Fixture-evidenced type enrichments

| Schema | Field | Inferred type | Observations |
|---|---|---|---|
| `payment-dictionary` | `billingContact` | object | 2 |
| `payment-dictionary` | `shippingContact` | object | 2 |
| `payment-dictionary` | `paymentToken` | object | 2 |
| `payment-dictionary-3` | `shippingMethod` | object | 4 |
| `payment-dictionary-2` | `paymentMethod` | object | 2 |
| `payment-method-dictionary` | `type` | string | 4 |
| `replymessage-dictionary` | `title` | string | 8 |
| `replymessage-dictionary` | `subtitle` | string | 4 |
| `replymessage-dictionary` | `style` | string | 5 |
| `replymessage-dictionary` | `imageIdentifier` | string | 4 |

Enrichments are applied to the schemas by `extract_schemas.py` (marked `x-amb-enriched-from-fixture`) and re-listed in `schema_coverage_report.md`.