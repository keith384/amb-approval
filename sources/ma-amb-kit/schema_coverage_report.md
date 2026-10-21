# AMB Schema Extraction — Coverage Report

_Generated 2026-07-09T04:36:44.262762+00:00 from `AMB_Layer2_Canonical_v7_0.md` (v7.0-verbatim-consolidated)._

> **Scope.** This covers the 47 `"Dictionary"`-headed tables plus the explicitly-added structural tables (HTTP Body, JWT claims, Required Features, Response Codes — see the Structural section below). Everything else in the canonical remains prose and is **not** modelled here: the 47+ dictionaries are not the complete AMB object model.

This report is the honesty layer over the extraction. Every item below is a place where Apple's source table was silent or ambiguous and the extractor **declined to guess**. Treat each as a verify-before-relying task.

## Totals

- Dictionary schemas emitted: **47**
- Structural tables added (A3): **4** (2 object schemas, 2 data tables)
- Properties extracted (dictionaries): **136**
- Required properties (dictionaries): **63**
- Schemas with no property table (prose-only): **5**
- Schemas with unresolved `See X` refs: **1**
- Schemas with empty Type cells: **0**
- Schemas using 2-column (Name|Description, no Type) tables: **3**
- Schemas with non-primitive Type cells: **0**
- Array-in-prose / object-in-type mismatches: **2**
- Enum-in-prose blocks detected (not auto-encoded): **4**
- Emitted schemas failing draft-2020-12 validation: **0**


## Structural tables (A3)

| id | title | kind | lines | size |
|---|---|---|---|---|
| `http-body` | HTTP Body | object | 322-343 | 9 props / 5 req |
| `jwt-claims` | JWT Authorization Fields (JOSE header + claims) | object | 136-145 | 4 props / 0 req |
| `required-features` | Required Features | matrix | 101-125 | 19 rows |
| `response-codes` | Response Codes | code_table | 345-398 | 7 rows |

Object-kind structural schemas (`http-body`, `jwt-claims`) are in the bundle and `schemas/`; matrix/code tables (`required-features`, `response-codes`) are in `structural/`. `http-body` is the real `/message` request body (fixes the previously over-deep mapping).


## Per-schema coverage

| Anchor | Name | Source | Lines | Props | Req | Table |
|---|---|---|---|---|---|---|
| `interactivedata-dictionary` | InteractiveData | msp-rest-api | 1564-1572 | 3 | 0 | yes |
| `interactivedatadata-dictionary` | InteractiveData.Data | msp-rest-api | 1573-1581 | 3 | 2 | yes |
| `baseinteractivemessage-dictionary` | BaseInteractiveMessage | msp-rest-api | 1582-1596 | 3 | 3 | yes |
| `interactiveresponse-dictionary` | InteractiveResponse | msp-rest-api | 1597-1615 | 7 | 1 | yes |
| `interactivemessagedata-dictionary` | InteractiveMessageData | msp-rest-api | 1616-1630 | 3 | 2 | yes |
| `imageitem-dictionary` | ImageItem | msp-rest-api | 1631-1672 | 3 | 2 | yes |
| `interactivemessageresponse-dictionary` | InteractiveMessageResponse | msp-rest-api | 1673-1686 | 4 | 1 | yes |
| `receivedmessage-dictionary` | ReceivedMessage | msp-rest-api | 1687-1724 | 4 | 3 | yes |
| `replymessage-dictionary` | ReplyMessage | msp-rest-api | 1725-1958 | 8 | 0 | yes |
| `interactivedatadata-dictionary-1` | InteractiveData.Data | msp-rest-api | 1959-1965 | 1 | 1 | yes |
| `dataquick-reply-dictionary` | Data.Quick-Reply | msp-rest-api | 1966-1973 | 2 | 2 | yes |
| `quick-replyitems-dictionary` | Quick-Reply.Items | msp-rest-api | 1974-1987 | 2 | 2 | yes |
| `dataquick-reply-dictionary-1` | Data.Quick-Reply | msp-rest-api | 1988-2002 | 3 | 0 | yes |
| `listpickermessage-dictionary` | ListPickerMessage | msp-rest-api | 2015-2018 | 0 | 0 | NO |
| `interactivedatadata-dictionary-2` | InteractiveData.data | msp-rest-api | 2019-2027 | 1 | 1 | yes |
| `datalistpickersection-dictionary` | Data.ListPickerSection | msp-rest-api | 2028-2039 | 4 | 1 | yes |
| `listpickersectionlistpickeritem-dictionary` | ListPickerSection.ListPickerItem | msp-rest-api | 2040-2052 | 5 | 2 | yes |
| `timepickermessage-dictionary` | TimePickerMessage | msp-rest-api | 2073-2085 | 1 | 1 | yes |
| `dataevent-dictionary` | Data.Event | msp-rest-api | 2086-2099 | 6 | 1 | yes |
| `eventitemlocationitem-dictionary` | EventItem.LocationItem | msp-rest-api | 2100-2115 | 4 | 0 | yes |
| `locationtimeitem-dictionary` | Location.TimeItem | msp-rest-api | 2116-2130 | 3 | 3 | yes |
| `applepaymessage-dictionary` | ApplePayMessage | msp-rest-api | 2143-2153 | 1 | 1 | yes |
| `applepayinteractivedata-dictionary` | ApplePay.InteractiveData | msp-rest-api | 2154-2169 | 1 | 1 | yes |
| `datapayment-dictionary` | Data.Payment | msp-rest-api | 2170-2178 | 3 | 3 | yes |
| `paymentrequestrequiredbillingcontactfields-dictionary` | PaymentRequest.requiredBillingContactFields | msp-rest-api | 2179-2191 | 5 | 5 | yes |
| `paymentapplepayendpoints-dictionary` | Payment.ApplePayEndpoints | msp-rest-api | 2192-2205 | 6 | 1 | yes |
| `paymentrequestapplepay-dictionary` | PaymentRequest.ApplePay | msp-rest-api | 2206-2216 | 3 | 1 | yes |
| `applepaymerchantcapabilities-dictionary` | ApplePay.MerchantCapabilities | msp-rest-api | 2217-2222 | 0 | 0 | NO |
| `applepaysupportednetworks-dictionary` | ApplePay.SupportedNetworks | msp-rest-api | 2223-2228 | 0 | 0 | NO |
| `applepaylineitems-dictionary` | ApplePay.lineItems | msp-rest-api | 2229-2241 | 3 | 2 | yes |
| `paymentmerchantsession-dictionary` | Payment.MerchantSession | msp-rest-api | 2242-2260 | 9 | 7 | yes |
| `paymentrequest-dictionary` | PaymentRequest | msp-rest-api | 2261-2264 | 0 | 0 | NO |
| `paymentrequestsupportedcountries-dictionary` | PaymentRequest.supportedCountries | msp-rest-api | 2265-2272 | 0 | 0 | NO |
| `paymentrequestshippingmethoditem-dictionary` | PaymentRequest.shippingMethodItem | msp-rest-api | 2273-2315 | 4 | 4 | yes |
| `payment-dictionary` | Payment | msp-rest-api | 2316-2432 | 3 | 0 | yes |
| `applepayitem-dictionary` | ApplePayItem | msp-rest-api | 2433-2445 | 3 | 1 | yes |
| `payment-dictionary-1` | Payment | msp-rest-api | 2600-2635 | 1 | 0 | yes |
| `payment-dictionary-2` | Payment | msp-rest-api | 2636-2644 | 1 | 0 | yes |
| `payment-method-dictionary` | Payment Method | msp-rest-api | 2645-2743 | 1 | 0 | yes |
| `payment-dictionary-3` | Payment | msp-rest-api | 2744-2836 | 1 | 0 | yes |
| `payment-dictionary-4` | Payment | msp-rest-api | 2837-2853 | 5 | 0 | yes |
| `interactivedata-dictionary-1` | InteractiveData | msp-rest-api | 2939-2953 | 1 | 1 | yes |
| `interactivedatadata-dictionary-3` | InteractiveData.Data | msp-rest-api | 2954-2963 | 4 | 3 | yes |
| `interactivedatadataauthenticate-dictionary` | InteractiveData.Data.Authenticate | msp-rest-api | 2964-2970 | 1 | 1 | yes |
| `dataauthenticateoauth2-dictionary` | Data.Authenticate.Oauth2 | msp-rest-api | 2971-3041 | 5 | 4 | yes |
| `interactivedatadata-dictionary-4` | InteractiveData.Data | msp-rest-api | 3042-3050 | 3 | 0 | yes |
| `dataauthenticate-dictionary` | Data.authenticate | msp-rest-api | 3051-3174 | 2 | 0 | yes |

### Prose-only dictionaries (no table to extract)

- `listpickermessage-dictionary` (ListPickerMessage, L2015-2018) — described in prose; model it by hand from the canonical.
- `applepaymerchantcapabilities-dictionary` (ApplePay.MerchantCapabilities, L2217-2222) — described in prose; model it by hand from the canonical.
- `applepaysupportednetworks-dictionary` (ApplePay.SupportedNetworks, L2223-2228) — described in prose; model it by hand from the canonical.
- `paymentrequest-dictionary` (PaymentRequest, L2261-2264) — described in prose; model it by hand from the canonical.
- `paymentrequestsupportedcountries-dictionary` (PaymentRequest.supportedCountries, L2265-2272) — described in prose; model it by hand from the canonical.


### Unresolved / ambiguous references

- `applepaymessage-dictionary`: InteractiveData: unresolved: 'Sending'


### Empty Type cells (left open, not guessed)

_None._

### 2-column tables — fields with no machine type in source

- `replymessage-dictionary`: fields ['imageTitle', 'imageSubtitle', 'secondarySubtitle', 'tertiarySubtitle'] (Apple gives description only; assign types by hand or from worked examples)
- `payment-dictionary-1`: fields ['shippingContact'] (Apple gives description only; assign types by hand or from worked examples)
- `payment-dictionary-4`: fields ['billingContact', 'errors', 'shippingContact', 'shippingMethod', 'summaryItems'] (Apple gives description only; assign types by hand or from worked examples)


### Fixture-evidenced type enrichments applied (C1)

- `replymessage-dictionary`.`title` -> **string** (8 fixture observations, all agree)
- `replymessage-dictionary`.`subtitle` -> **string** (4 fixture observations, all agree)
- `replymessage-dictionary`.`style` -> **string** (5 fixture observations, all agree)
- `replymessage-dictionary`.`imageIdentifier` -> **string** (4 fixture observations, all agree)
- `payment-dictionary`.`billingContact` -> **object** (2 fixture observations, all agree)
- `payment-dictionary`.`shippingContact` -> **object** (2 fixture observations, all agree)
- `payment-dictionary`.`paymentToken` -> **object** (2 fixture observations, all agree)
- `payment-dictionary-2`.`paymentMethod` -> **object** (2 fixture observations, all agree)
- `payment-method-dictionary`.`type` -> **string** (4 fixture observations, all agree)
- `payment-dictionary-3`.`shippingMethod` -> **object** (4 fixture observations, all agree)


### Non-primitive Type cells

_None._

### Array-in-prose vs object-in-Type mismatches

- `interactivedatadata-dictionary-2`: fields ['listPicker'] (kept as source; verify intended shape)
- `datalistpickersection-dictionary`: fields ['listPickerItem'] (kept as source; verify intended shape)


### Enum-in-prose detected (encode by hand if desired)

- `interactiveresponse-dictionary`: possible values. This key is optional. Default: icon Possible values:
- `receivedmessage-dictionary`: possible string values for the receivedMessage style are:
- `replymessage-dictionary`: possible reply message style values are:
- `dataauthenticate-dictionary`: Possible values for the autocomplete attribute are

