# AMB Fixtures — Validation Report

_Validated 74 fixtures against the schema bundle._

- **Pass:** 38
- **Fail:** 3
- **No confident schema mapping (skipped, not a failure):** 33


## Passing (fixture -> schema)

- `msp-rest-api-77-6` -> `http-body`
- `msp-rest-api-77-8` -> `http-body`
- `msp-rest-api-77-9` -> `http-body`
- `msp-rest-api-77-10` -> `http-body`
- `msp-rest-api-77-12` -> `http-body`
- `msp-rest-api-77-13` -> `http-body`
- `msp-rest-api-77-14` -> `http-body`
- `msp-rest-api-77-18` -> `http-body`
- `msp-rest-api-77-20` -> `http-body`
- `msp-rest-api-77-21` -> `http-body`
- `msp-rest-api-77-22` -> `http-body`
- `msp-rest-api-77-23` -> `http-body`
- `msp-rest-api-77-26` -> `http-body`
- `msp-rest-api-77-36` -> `http-body`
- `msp-rest-api-77-37` -> `http-body`
- `msp-rest-api-77-40` -> `http-body`
- `msp-rest-api-77-43` -> `http-body`
- `example-closesession-message-752-0` -> `http-body`
- `example-closesession-message-752-1` -> `http-body`
- `example-of-a-text-message-997-0` -> `http-body`
- `example-of-a-text-message-997-2` -> `http-body`
- `example-of-a-text-message-997-3` -> `http-body`
- `example-of-a-text-message-997-4` -> `http-body`
- `example-of-a-text-message-997-5` -> `http-body`
- `replymessage-dictionary-1725-1` -> `replymessage-dictionary`
- `replymessage-dictionary-1725-2` -> `replymessage-dictionary`
- `payment-dictionary-2316-0` -> `payment-dictionary`
- `payment-dictionary-2316-1` -> `payment-dictionary`
- `payment-method-dictionary-2645-0` -> `payment-method-dictionary`
- `payment-method-dictionary-2645-1` -> `payment-method-dictionary`
- `payment-dictionary-2744-0` -> `payment-dictionary`
- `payment-dictionary-2744-1` -> `payment-dictionary`
- `data-authenticate-dictionary-3051-0` -> `http-body`
- `data-authenticate-dictionary-3051-1` -> `http-body`
- `form-message-3175-2` -> `http-body`
- `form-message-3175-5` -> `http-body`
- `msp-api-tutorial-4265-0` -> `http-body`
- `msp-api-tutorial-4265-9` -> `http-body`

## Failing

_A failure here means a fixture that maps to a schema violates it — usually a genuine **spec-vs-example discrepancy** in Apple's docs (e.g. worked examples that omit a field the table marks REQUIRED), not a schema bug. Worth an integrator's attention._

- `msp-rest-api-77-35` -> `http-body`
  - []: 'id' is a required property
- `authentication-message-2854-0` -> `http-body`
  - []: 'id' is a required property
- `msp-api-tutorial-4265-7` -> `http-body`
  - []: 'id' is a required property

## No mapping (sub-fragments or need a human to assign a schema)

`msp-rest-api-77-1`, `msp-rest-api-77-3`, `msp-rest-api-77-4`, `msp-rest-api-77-5`, `msp-rest-api-77-15`, `msp-rest-api-77-17`, `msp-rest-api-77-19`, `msp-rest-api-77-24`, `msp-rest-api-77-27`, `msp-rest-api-77-28`, `msp-rest-api-77-29`, `msp-rest-api-77-31`, `msp-rest-api-77-32`, `msp-rest-api-77-33`, `msp-rest-api-77-34`, `msp-rest-api-77-38`, `msp-rest-api-77-39`, `msp-rest-api-77-41`, `msp-rest-api-77-42`, `example-closesession-message-752-2`, `example-closesession-message-752-4`, `example-of-a-text-message-997-1`, `imageitem-dictionary-1631-0`, `form-message-3175-0`, `form-message-3175-1`, `form-message-3175-3`, `form-message-3175-4`, `msp-api-tutorial-4265-1`, `msp-api-tutorial-4265-2`, `msp-api-tutorial-4265-3`, `msp-api-tutorial-4265-8`, `apple-pay-payment-object-10523-2`, `authorize-payment-and-map-customer-information-12065-2`