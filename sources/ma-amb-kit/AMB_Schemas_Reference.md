# Apple Messages for Business — Consolidated Schema Reference

_Reference only. Generated 2026-07-09T04:36:45.238069+00:00 from `AMB_Layer2_Canonical_v7_0.md` (v7.0-verbatim-consolidated) via the extracted schema bundle._

> **Scope.** Covers the 47 `"Dictionary"`-headed tables plus 2 explicitly-added structural object schemas (HTTP Body, JWT claims). Everything else in the canonical remains prose and is not modelled here — this is not the complete AMB object model.

Each entry asserts only what Apple's source table states; `→` marks a resolved cross-reference, italic notes mark places the source was silent (see `schema_coverage_report.md` for the full verify-before-relying list, including the Required Features and Response Codes tables). For the machine-consumable form, use `amb_schemas_bundle.json` / `schemas/<anchor>.json`.

**49 object schemas · 149 properties · 68 required**

## Contents

- **msp-rest-api — Part 1A — MSP REST API Reference (verbatim)**
  - [InteractiveData](#interactivedata-dictionary)
  - [InteractiveData.Data](#interactivedatadata-dictionary)
  - [BaseInteractiveMessage](#baseinteractivemessage-dictionary)
  - [InteractiveResponse](#interactiveresponse-dictionary)
  - [InteractiveMessageData](#interactivemessagedata-dictionary)
  - [ImageItem](#imageitem-dictionary)
  - [InteractiveMessageResponse](#interactivemessageresponse-dictionary)
  - [ReceivedMessage](#receivedmessage-dictionary)
  - [ReplyMessage](#replymessage-dictionary)
  - [InteractiveData.Data](#interactivedatadata-dictionary-1)
  - [Data.Quick-Reply](#dataquick-reply-dictionary)
  - [Quick-Reply.Items](#quick-replyitems-dictionary)
  - [Data.Quick-Reply](#dataquick-reply-dictionary-1)
  - [ListPickerMessage](#listpickermessage-dictionary)
  - [InteractiveData.data](#interactivedatadata-dictionary-2)
  - [Data.ListPickerSection](#datalistpickersection-dictionary)
  - [ListPickerSection.ListPickerItem](#listpickersectionlistpickeritem-dictionary)
  - [TimePickerMessage](#timepickermessage-dictionary)
  - [Data.Event](#dataevent-dictionary)
  - [EventItem.LocationItem](#eventitemlocationitem-dictionary)
  - [Location.TimeItem](#locationtimeitem-dictionary)
  - [ApplePayMessage](#applepaymessage-dictionary)
  - [ApplePay.InteractiveData](#applepayinteractivedata-dictionary)
  - [Data.Payment](#datapayment-dictionary)
  - [PaymentRequest.requiredBillingContactFields](#paymentrequestrequiredbillingcontactfields-dictionary)
  - [Payment.ApplePayEndpoints](#paymentapplepayendpoints-dictionary)
  - [PaymentRequest.ApplePay](#paymentrequestapplepay-dictionary)
  - [ApplePay.MerchantCapabilities](#applepaymerchantcapabilities-dictionary)
  - [ApplePay.SupportedNetworks](#applepaysupportednetworks-dictionary)
  - [ApplePay.lineItems](#applepaylineitems-dictionary)
  - [Payment.MerchantSession](#paymentmerchantsession-dictionary)
  - [PaymentRequest](#paymentrequest-dictionary)
  - [PaymentRequest.supportedCountries](#paymentrequestsupportedcountries-dictionary)
  - [PaymentRequest.shippingMethodItem](#paymentrequestshippingmethoditem-dictionary)
  - [Payment](#payment-dictionary)
  - [ApplePayItem](#applepayitem-dictionary)
  - [Payment](#payment-dictionary-1)
  - [Payment](#payment-dictionary-2)
  - [Payment Method](#payment-method-dictionary)
  - [Payment](#payment-dictionary-3)
  - [Payment](#payment-dictionary-4)
  - [InteractiveData](#interactivedata-dictionary-1)
  - [InteractiveData.Data](#interactivedatadata-dictionary-3)
  - [InteractiveData.Data.Authenticate](#interactivedatadataauthenticate-dictionary)
  - [Data.Authenticate.Oauth2](#dataauthenticateoauth2-dictionary)
  - [InteractiveData.Data](#interactivedatadata-dictionary-4)
  - [Data.authenticate](#dataauthenticate-dictionary)
- **msp-rest-api**
  - [HTTP Body](#http-body)
  - [JWT Authorization Fields (JOSE header + claims)](#jwt-claims)


---

## msp-rest-api — Part 1A — MSP REST API Reference (verbatim)

<a id="interactivedata-dictionary"></a>
### InteractiveData

`interactivedata-dictionary` · canonical L1564–1572 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `bid` | string |  | com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension |
| `data` | object |  | A collection of name and values used for interactive message types. |
| `sessionIdentifier` | string |  | sessionIdentifier is related to generic iMessage app sessions. If the interactive data in the message from MSP contains sessionIdentifier, Apple Messages for Business server will use the same sessionIdentifier in the payload to device. Otherwise, Apple will generate a random session identifier (UUID) and use it in the bp payload to device. |

<a id="interactivedatadata-dictionary"></a>
### InteractiveData.Data

`interactivedatadata-dictionary` · canonical L1573–1581 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `images` | array |  | An array of image dictionaries. The image size must be 200kB or smaller, and the format is restricted to PNG only. |
| `requestIdentifier` | string (uuid, src:UUID) | ✓ | REQUIRED. An unique identifier for the authenticate request. Value must be UUID: uuid. |
| `version` | string | ✓ | REQUIRED. A numerical version number of the message extension schema. |

<a id="baseinteractivemessage-dictionary"></a>
### BaseInteractiveMessage

`baseinteractivemessage-dictionary` · canonical L1582–1596 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `bid` | string | ✓ | REQUIRED. A string identifying the iMessage extension that the user interacts with while using Messages. The bid value format is: com.apple.messages.MSMessageExtensionBalloonPlugin:team-id:extension-id When using your custom interactive message, replace team-id and extension-id with your team and extension IDs. When using an Apple Messages for Business interactive message, set team-id to 0000000000 and the extension-id to com.apple.icloud.apps.messages.business.extension. For example: com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension |
| `receivedMessage` | → [`receivedmessage-dictionary`](#receivedmessage-dictionary) | ✓ | REQUIRED. A dictionary with information telling the Messages app how and what content to display the received message bubble. See ReceivedMessage Dictionary. |
| `replyMessage` | → [`replymessage-dictionary`](#replymessage-dictionary) | ✓ | REQUIRED. A dictionary with information telling the Messages app how and what to display in the reply message bubble. See ReplyMessage Dictionary. |

<a id="interactiveresponse-dictionary"></a>
### InteractiveResponse

`interactiveresponse-dictionary` · canonical L1597–1615 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

> **Enum in prose:** possible values. This key is optional. Default: icon Possible values:

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `imageSubtitle` | string |  | The attached image's subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| `imageTitle` | string |  | The attached image's title. Limited to 512 characters. Only custom interactive messages use this key. |
| `secondarySubtitle` | string |  | A right-aligned title. Limited to 512 characters. Only custom interactive messages use this key. |
| `style` | string |  | A style that controls the size of the view rendered by Live Layout. The default is icon. Depending if the message is a reply or response, see Reply Message Style Values or Received Message Style Values for the list of possible values. This key is optional. Default: icon Possible values: icon,small,large |
| `subtitle` | string |  | The subtitle that appears under the main title in the reply message bubble. When the user taps the reply message bubble, Messages displays the subtitle in the header. Limited to 512 characters. |
| `tertiarySubtitle` | string |  | A right-aligned subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| `title` | string | ✓ | REQUIRED. The main title that Messages shows in the header of the reply message bubble. When the user taps the reply message bubble, Messages replaces the title with the user’s selection. Limited to 512 characters. |

<a id="interactivemessagedata-dictionary"></a>
### InteractiveMessageData

`interactivemessagedata-dictionary` · canonical L1616–1630 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `images` | array (of imageitem-dictionary) |  | An array of image dictionaries. For the list of keys in the image dictionary, see ImageItem dictionary. |
| `requestIdentifier` | string (uuid, src:UUID) | ✓ | REQUIRED. A string representing a unique identifier for the request. Apple Messages for Business returns the ID in the response it sends back to the MSP platform. Value must be UUID: uuid. |
| `version` | string | ✓ | REQUIRED. A string representing the version number of the message extension schema. Should be 1.0. |

<a id="imageitem-dictionary"></a>
### ImageItem

`imageitem-dictionary` · canonical L1631–1672 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `data` | string (base64, src:byte) | ✓ | REQUIRED. A Base64-encoded string representing the image file data. Always provide @3x images at 72 dpi. The system downscales the @3x images to generate @2x and @1x versions for use on lower-resolution devices. |
| `description` | string |  | Description of the image that the systems reads aloud to users who have VoiceOver enabled on their device. If the value is null, VoiceOver ignores the image. This key is optional. |
| `identifier` | string | ✓ | REQUIRED.A string containing the image identifier, which must be unique within the list of images. The list picker items and other dictionaries, such as receiveMessage and replyMessage, refer to identifier as imageIdentifier. |

<a id="interactivemessageresponse-dictionary"></a>
### InteractiveMessageResponse

`interactivemessageresponse-dictionary` · canonical L1673–1686 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `bid` | string | ✓ | REQUIRED. A string identifying the iMessage extension that the user interacts with while using the Messages app. |
| `data` | → [`interactivemessagedata-dictionary`](#interactivemessagedata-dictionary) |  | A dictionary containing additional information for Apple Messages for Business interactive messages |
| `receivedMessage` | → [`receivedmessage-dictionary`](#receivedmessage-dictionary) |  | A dictionary with information telling the Messages app what content and how to display it in the received message bubble. |
| `replyMessage` | → [`replymessage-dictionary`](#replymessage-dictionary) |  | A dictionary with information telling the Messages app what and how to display it in the reply message bubble. |

<a id="receivedmessage-dictionary"></a>
### ReceivedMessage

`receivedmessage-dictionary` · canonical L1687–1724 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

> **Enum in prose:** possible string values for the receivedMessage style are:

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `title` | string | ✓ | REQUIRED. The main title that the Messages app shows in the header of the received message bubble. |
| `subtitle` | string | ✓ | REQUIRED. The subtitle that appears under the main title in the received message bubble. |
| `imageIdentifier` | integer | ✓ | REQUIRED. The identifier for one of the images specified in interactiveData.data.images. |
| `style` | string |  | A style that controls the size of the view rendered by Live Layout. The default is icon. |

<a id="replymessage-dictionary"></a>
### ReplyMessage

`replymessage-dictionary` · canonical L1725–1958 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

> **Enum in prose:** possible reply message style values are:

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `title` | string |  | The main title that the Messages app shows in the header of the reply message bubble. When the user taps the reply message bubble, the Messages app replaces the title with the user’s selection. Limited to 512 characters. |
| `subtitle` | string |  | The subtitle that appears under the main title in the reply message bubble. When the user taps the reply message bubble, the Messages app displays the subtitle in the header. Limited to 512 characters. |
| `imageTitle` | _(unspecified — 2-col table)_ |  | The attached image's title. Limited to 512 characters. Only custom interactive messages use this key. |
| `imageSubtitle` | _(unspecified — 2-col table)_ |  | The attached image's subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| `secondarySubtitle` | _(unspecified — 2-col table)_ |  | A right-aligned title. Limited to 512 characters. Only custom interactive messages use this key. |
| `tertiarySubtitle` | _(unspecified — 2-col table)_ |  | A right-aligned subtitle. Limited to 512 characters. Only custom interactive messages use this key. |
| `imageIdentifier` | string |  | The identifier for one of the images specified in interactiveData.data.images. |
| `style` | string |  | A style that controls the size of the view rendered by Live Layout. The default is icon. See Reply Message Style Values for the list of possible values. |

<a id="interactivedatadata-dictionary-1"></a>
### InteractiveData.Data

`interactivedatadata-dictionary-1` · canonical L1959–1965 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `quick-reply` | object | ✓ | REQUIRED. An array of objects. |

<a id="dataquick-reply-dictionary"></a>
### Data.Quick-Reply

`dataquick-reply-dictionary` · canonical L1966–1973 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `summaryText` | string | ✓ | REQUIRED. A summary text that will be used for device notification but also shown in the transcript after user makes a choice. |
| `items` | object | ✓ | REQUIRED. An array of section items. |

<a id="quick-replyitems-dictionary"></a>
### Quick-Reply.Items

`quick-replyitems-dictionary` · canonical L1974–1987 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `identifier` | string | ✓ | REQUIRED. An identifier to identify the item. |
| `title` | string | ✓ | REQUIRED. Title of the quick reply item. Max 1 line of text. |

<a id="dataquick-reply-dictionary-1"></a>
### Data.Quick-Reply

`dataquick-reply-dictionary-1` · canonical L1988–2002 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `selectedIndex` | integer |  | The selected item number from top order. |
| `selectedIdentifier` | string |  | The selected identifier of the item. |
| `items` | object |  | The array of section items, max of 5 items allowed. |

<a id="listpickermessage-dictionary"></a>
### ListPickerMessage

`listpickermessage-dictionary` · canonical L2015–2018 · source `msp-rest-api` (rank 1, 2026-06-03) · none table

> No property table in source span; this dictionary is described in prose only. Verify against canonical.

_No property table in source (prose-only dictionary)._

<a id="interactivedatadata-dictionary-2"></a>
### InteractiveData.data

`interactivedatadata-dictionary-2` · canonical L2019–2027 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `listPicker` | → [`datalistpickersection-dictionary`](#datalistpickersection-dictionary) | ✓ | REQUIRED. An array of objects. See ListPickerSection.<br>_source prose says 'an array of ...' but Type cell = object_ |

<a id="datalistpickersection-dictionary"></a>
### Data.ListPickerSection

`datalistpickersection-dictionary` · canonical L2028–2039 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `listPickerItem` | → [`listpickersectionlistpickeritem-dictionary`](#listpickersectionlistpickeritem-dictionary) |  | An array of section items. See ListPickerItem.<br>_source prose says 'an array of ...' but Type cell = object_ |
| `multipleSelection` | boolean |  | A Boolean that indicates whether the customer can make multiple selections within the section. Defaults to false. |
| `order` | integer |  | An integer containing the ordinal pn the sections array. |
| `title` | string | ✓ | REQUIRED. A string field of the section title. |

<a id="listpickersectionlistpickeritem-dictionary"></a>
### ListPickerSection.ListPickerItem

`listpickersectionlistpickeritem-dictionary` · canonical L2040–2052 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `identifier` | string | ✓ | REQUIRED. A string field identifying the item. |
| `imageIdentifier` | string |  | A string field of the item title. |
| `order` | integer |  | An integer representing the ordinal position for the item. If this key is missing, the item isn't sorted within the items array. |
| `subtitle` | string |  | A string field of the item's subtitle. |
| `title` | string | ✓ | REQUIRED. A string field of the section title. |

<a id="timepickermessage-dictionary"></a>
### TimePickerMessage

`timepickermessage-dictionary` · canonical L2073–2085 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `event` | → [`dataevent-dictionary`](#dataevent-dictionary) | ✓ | REQUIRED. A dictionary containing specific information for the user. See Event |

<a id="dataevent-dictionary"></a>
### Data.Event

`dataevent-dictionary` · canonical L2086–2099 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `identifier` | string | ✓ | REQUIRED. A string field identifying the event that must be unique within the payload, if more than one exists. |
| `imageIdentifier` | string |  | An identifier for the image to show when the user taps a reply message bubble. The image should be a @3x image sized at 375 x 208 points (that is, 1125 x 624 pixels). |
| `location` | → [`eventitemlocationitem-dictionary`](#eventitemlocationitem-dictionary) |  | A dictionary describing a location. For the list of location dictionary keys, see LocationItem dictionary. |
| `timeslots` | array (of locationtimeitem-dictionary) |  | An array of time slots. For the list of time slot dictionary keys, see TimeItem dictionary. |
| `timezoneOffset` | integer |  | An integer representing the number of minutes from GMT, specifying the timezone of the event’s location. If not set, times are shown according to the customer’s current time zone. If set, the times are shown according to the event’s time zone, regardless of the customer’s location. |
| `title` | string |  | A string field of the event title. |

<a id="eventitemlocationitem-dictionary"></a>
### EventItem.LocationItem

`eventitemlocationitem-dictionary` · canonical L2100–2115 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `latitude` | number |  | A double representing the latitude of the location. |
| `longitude` | number |  | A double representing the longitude of the location. |
| `radius` | number |  | A double representing the location radius, in meters. Apple Messages for Business ignores this field when latitude and longitude are missing. |
| `title` | string |  | A string field of the location title. |

<a id="locationtimeitem-dictionary"></a>
### Location.TimeItem

`locationtimeitem-dictionary` · canonical L2116–2130 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `duration` | integer | ✓ | REQUIRED. An integer representing the duration of the time slot, in seconds. |
| `identifier` | string | ✓ | REQUIRED. A string field identifying the time item that must be unique within the payload, if more than one exists. |
| `startTime` | string | ✓ | REQUIRED. A UTC date string, represented by a valid date in ISO-8601 format and specified as absolute GMT +0000 date; for example, 2017-05-26T08:27+0000 or 2025-07-10T17:00+0000; the API does not accept seconds (:ss) or the Z notation (2025-07-10T17:00:00Z is invalid). The timezoneOffset, from the EventItem dictionary, determines whether the startTime is in a specific time zone or in the customer's current time zone. |

<a id="applepaymessage-dictionary"></a>
### ApplePayMessage

`applepaymessage-dictionary` · canonical L2143–2153 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `InteractiveData` | object | ✓ | REQUIRED. Fields that contain all the data needed to submit an Apple Pay payment request. See Sending an Apple Pay Payment Request.<br>_references 'Sending' (unresolved)_ |

<a id="applepayinteractivedata-dictionary"></a>
### ApplePay.InteractiveData

`applepayinteractivedata-dictionary` · canonical L2154–2169 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `receivedMessage` | object | ✓ | REQUIRED. Contains fields giving the specifics of an Apple Pay request |

<a id="datapayment-dictionary"></a>
### Data.Payment

`datapayment-dictionary` · canonical L2170–2178 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `endpoints` | object | ✓ | REQUIRED. A dictionary containing the endpoints for payment processing, contact updates, and order tracking. For the list of dictionary keys, see ApplePayEndpoints dictionary. |
| `merchantSession` | object | ✓ | REQUIRED. A dictionary containing the payment session provided by Apple Pay after requesting a new payment session. For more information, see Requesting an Apple Pay Payment Session. |
| `paymentRequest` | object | ✓ | REQUIRED. A dictionary with information about the payment request. For the list of dictionary keys, see ApplePayPaymentRequest dictionary. |

<a id="paymentrequestrequiredbillingcontactfields-dictionary"></a>
### PaymentRequest.requiredBillingContactFields

`paymentrequestrequiredbillingcontactfields-dictionary` · canonical L2179–2191 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `email` | string | ✓ | REQUIRED. Email address of the Apple Pay contact. |
| `name` | string | ✓ | REQUIRED. Full name of the Apple Pay contact. |
| `phone` | string | ✓ | REQUIRED. Phone number of the Apple Pay contact. |
| `phoneticName` | string | ✓ | REQUIRED. Phonetic spelling of the Apple Pay contact. |
| `post` | string | ✓ | REQUIRED. Postal address of the Apple Pay contact. |

<a id="paymentapplepayendpoints-dictionary"></a>
### Payment.ApplePayEndpoints

`paymentapplepayendpoints-dictionary` · canonical L2192–2205 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `fallbackUrl` | string |  | A URL that opens in a web browser so the customer can complete the purchase if their device is unable to make payments using Apple Pay. |
| `orderTrackingUrl` | string |  | Called by Apple Messages for Business after completing the order; provides you with an opportunity to update the order information in your system. For more information, see Tracking Orders. |
| `paymentGatewayUrl` | string | ✓ | REQUIRED. Called by Apple Pay to process the payment through the payment provider. The URL should match the URL in the initiativeContext field of the payment session. For more information, see Processing Payment Requests. |
| `paymentMethodUpdateUrl` | string |  | Called by Apple Pay when the customer changes the payment method. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Payment Methods. |
| `shippingContactUpdateUrl` | string |  | Called by Apple Pay when the customer changes their shipping address information. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Shipping Contacts. |
| `shippingMethodUpdateUrl` | string |  | Called by Apple Pay when the customer changes the shipping method. If you don’t implement this endpoint and you include this key in the dictionary, the customer sees an error message. For more information, see Updating Shipping Methods. |

<a id="paymentrequestapplepay-dictionary"></a>
### PaymentRequest.ApplePay

`paymentrequestapplepay-dictionary` · canonical L2206–2216 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `merchantCapabilities` | → [`applepaymerchantcapabilities-dictionary`](#applepaymerchantcapabilities-dictionary) |  | An array of payment capabilities supported by the merchant. The array must include supports3DS, and may optionally include supportsCredit, supportsDebit, and supportsEMV. For more information, see [merchantCapabilities. |
| `merchantIdentifier` | string | ✓ | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| `supportedNetworks` | → [`applepaysupportednetworks-dictionary`](#applepaysupportednetworks-dictionary) |  | An array of payment networks supported by the merchant. The array must include one or more of the following values: amex, discover, jcb, masterCard, privateLabel, or visa. For more information, see [supportedNetworks. |

<a id="applepaymerchantcapabilities-dictionary"></a>
### ApplePay.MerchantCapabilities

`applepaymerchantcapabilities-dictionary` · canonical L2217–2222 · source `msp-rest-api` (rank 1, 2026-06-03) · none table

> No property table in source span; this dictionary is described in prose only. Verify against canonical.

_No property table in source (prose-only dictionary)._

<a id="applepaysupportednetworks-dictionary"></a>
### ApplePay.SupportedNetworks

`applepaysupportednetworks-dictionary` · canonical L2223–2228 · source `msp-rest-api` (rank 1, 2026-06-03) · none table

> No property table in source span; this dictionary is described in prose only. Verify against canonical.

_No property table in source (prose-only dictionary)._

<a id="applepaylineitems-dictionary"></a>
### ApplePay.lineItems

`applepaylineitems-dictionary` · canonical L2229–2241 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `amount` | string | ✓ | REQUIRED. The monetary amount of the line item. |
| `label` | string | ✓ | REQUIRED. A short, localized description of the line item. |
| `type` | string |  | A value that indicates whether the line item is final or pending. |

<a id="paymentmerchantsession-dictionary"></a>
### Payment.MerchantSession

`paymentmerchantsession-dictionary` · canonical L2242–2260 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `displayName` | string | ✓ | REQUIRED. The canonical name for your store, suitable for display and consisting of 64 or fewer UTF-8 characters. Do not localize the name. |
| `epochTimestamp` | string | ✓ | REQUIRED. The time representation in number of seconds that have elapsed since 00:00:00 UTC, Thursday, January 1, 1970. |
| `expiresAt` | string | ✓ | REQUIRED. The exipiration time representation in number of seconds that have elapsed since 00:00:00 UTC, Thursday, January 1, 1970. |
| `initiative` | string | ✓ | REQUIRED. A predefined value that identifies the e-commerce application making the request. |
| `initiativeContext` | string | ✓ | REQUIRED. A value you provide based on the initiative. The values for initiative and initiativeContext depend on the kind of application you're building. For Apple Messages for Business, use "messaging"for the initiative parameter. For the initiativeContextparameter, pass your payment gateway URL. See Processing Payment Requests for more information. |
| `merchantIdentifier` | string | ✓ | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| `merchantSessionIdentifier` | string | ✓ | REQUIRED. A unique identifier that represents a merchant's session for Apple Pay. |
| `nonce` | string (src:binary) |  | A single-use string that checks the integrity of the interaction. |
| `signature` | string (src:binary) |  | A hash of the public key used to sign the interactions. |

<a id="paymentrequest-dictionary"></a>
### PaymentRequest

`paymentrequest-dictionary` · canonical L2261–2264 · source `msp-rest-api` (rank 1, 2026-06-03) · none table

> No property table in source span; this dictionary is described in prose only. Verify against canonical.

_No property table in source (prose-only dictionary)._

<a id="paymentrequestsupportedcountries-dictionary"></a>
### PaymentRequest.supportedCountries

`paymentrequestsupportedcountries-dictionary` · canonical L2265–2272 · source `msp-rest-api` (rank 1, 2026-06-03) · none table

> No property table in source span; this dictionary is described in prose only. Verify against canonical.

_No property table in source (prose-only dictionary)._

<a id="paymentrequestshippingmethoditem-dictionary"></a>
### PaymentRequest.shippingMethodItem

`paymentrequestshippingmethoditem-dictionary` · canonical L2273–2315 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `amount` | string | ✓ | REQUIRED. The nonnegative cost associated with this shipping method. |
| `detail` | string | ✓ | REQUIRED. Additional description of the shipping method. |
| `identifier` | string | ✓ | REQUIRED. A client-defined value used to identify this shipping method. |
| `label` | string | ✓ | REQUIRED. A short description of the shipping method. |

<a id="payment-dictionary"></a>
### Payment

`payment-dictionary` · canonical L2316–2432 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `billingContact` | object |  | The customer's billing contact information. For more information, see billingContact. |
| `paymentToken` | object |  | The payment token. For more information, see Payment Token Format Reference for more information. |
| `shippingContact` | object |  | The customer's shipping address information. For more information, see shippingContact. |

<a id="applepayitem-dictionary"></a>
### ApplePayItem

`applepayitem-dictionary` · canonical L2433–2445 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `merchantCapabilities` | → [`applepaymerchantcapabilities-dictionary`](#applepaymerchantcapabilities-dictionary) |  | An array of payment capabilities supported by the merchant. The array must include supports3DS, and may optionally include supportsCredit, supportsDebit, and supportsEMV. For more information, see merchantCapabilities. |
| `merchantIdentifier` | string | ✓ | REQUIRED. A unique identifier that represents a merchant for Apple Pay. |
| `supportedNetworks` | → [`applepaysupportednetworks-dictionary`](#applepaysupportednetworks-dictionary) |  | An array of payment networks supported by the merchant. The array must include one or more of the following values: amex, discover, jcb, masterCard, privateLabel, or visa. For more information, see supportedNetworks. |

<a id="payment-dictionary-1"></a>
### Payment

`payment-dictionary-1` · canonical L2600–2635 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `shippingContact` | _(unspecified — 2-col table)_ |  | A dictionary with the customer's updated shipping address information. For more information, see shippingContact.<br>_type not specified in source (2-column Name\|Description table); prose ref 'shippingContact.' unresolved: 'shippingContact.'_ |

<a id="payment-dictionary-2"></a>
### Payment

`payment-dictionary-2` · canonical L2636–2644 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `paymentMethod` | object |  | A dictionary with payment method information. For the list of dictionary keys, see Payment Method Dictionary. |

<a id="payment-method-dictionary"></a>
### Payment Method

`payment-method-dictionary` · canonical L2645–2743 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `type` | string |  | Indicates the payment method type. For more information, see ApplePayPaymentMethodType. |

<a id="payment-dictionary-3"></a>
### Payment

`payment-dictionary-3` · canonical L2744–2836 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `shippingMethod` | object |  | The shipping method selected by the customer. For more information, see shippingMethod. |

<a id="payment-dictionary-4"></a>
### Payment

`payment-dictionary-4` · canonical L2837–2853 · source `msp-rest-api` (rank 1, 2026-06-03) · 2col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `billingContact` | _(unspecified — 2-col table)_ |  | The customer's billing contact information. For more information, see billingContact.<br>_type not specified in source (2-column Name\|Description table); prose ref 'billingContact.' unresolved: 'billingContact.'_ |
| `errors` | _(unspecified — 2-col table)_ |  | An array of ApplePayError types. This field is present only when the payment processing request detects errors. |
| `shippingContact` | _(unspecified — 2-col table)_ |  | The customer's shipping address information. For more information, see shippingContact.<br>_type not specified in source (2-column Name\|Description table); prose ref 'shippingContact.' unresolved: 'shippingContact.'_ |
| `shippingMethod` | _(unspecified — 2-col table)_ |  | The shipping method selected by the customer. For more information, see ApplePayShippingMethodItem.<br>_type not specified in source (2-column Name\|Description table); prose ref 'ApplePayShippingMethodItem.' unresolved: 'ApplePayShippingMethodItem.'_ |
| `summaryItems` | _(unspecified — 2-col table)_ |  | An array of ApplePayLineItem dictionaries. |

<a id="interactivedata-dictionary-1"></a>
### InteractiveData

`interactivedata-dictionary-1` · canonical L2939–2953 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `bid` | string | ✓ | REQUIRED. com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000: |

<a id="interactivedatadata-dictionary-3"></a>
### InteractiveData.Data

`interactivedatadata-dictionary-3` · canonical L2954–2963 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `images` | array |  | An array of image dictionaries. |
| `requestIdentifier` | string (uuid, src:UUID) | ✓ | REQUIRED. An unique identifier for the authentication request. Value must be UUID: uuid. |
| `version` | string | ✓ | REQUIRED. A numerical version number of the message extension schema. Set 2.0 for the New Authentication Message. |
| `authenticate` | object | ✓ | REQUIRED. An object to construct the authorization URL. |

<a id="interactivedatadataauthenticate-dictionary"></a>
### InteractiveData.Data.Authenticate

`interactivedatadataauthenticate-dictionary` · canonical L2964–2970 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `oauth2` | object | ✓ | REQUIRED. A dictionary that describes the authentication request. |

<a id="dataauthenticateoauth2-dictionary"></a>
### Data.Authenticate.Oauth2

`dataauthenticateoauth2-dictionary` · canonical L2971–3041 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `responseType` | string | ✓ | REQUIRED. A string indicating the type of authentication request. Set code for authorization flow. |
| `scope` | array | ✓ | REQUIRED. An array of scope items that specifies the scope of the request.This dictionary entry gives the exact fields of data that the authentication service provides to the client requesting the authentication. |
| `state` | string | ✓ | REQUIRED. A string indicating the state of the authentication request. |
| `redirectURI` | string | ✓ | REQUIRED. A string representing the redirect URL that the OAuth provider redirects the user. |
| `additionalParameters` | string |  | A string value that you can add on the authorization URL query parameter. |

<a id="interactivedatadata-dictionary-4"></a>
### InteractiveData.Data

`interactivedatadata-dictionary-4` · canonical L3042–3050 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `requestIdentifier` | string (uuid, src:UUID) |  | An unique identifier for the authentication request. Value must be UUID: uuid. |
| `version` | string |  | A numerical version number of the message extension schema. 2.0 for the New Authentication Message. |
| `authenticate` | array |  | An array object to construct the authorization URL. |

<a id="dataauthenticate-dictionary"></a>
### Data.authenticate

`dataauthenticate-dictionary` · canonical L3051–3174 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

> **Enum in prose:** Possible values for the autocomplete attribute are

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `status` | string |  | success, failure, cancel, unknown is returned as a value, which indicates that the authentication flow was closed. |
| `error_code` | string |  | A numeric number of the error_code sent from |


---

## msp-rest-api

<a id="http-body"></a>
### HTTP Body

`http-body` · canonical L322–343 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

> **Enum in prose:** possible values and their meanings, see Message Type Values. Possible values:

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `attachments` | _(unspecified)_ |  | An array of attachment dictionaries. For more information, see Attachments.<br>_source Type cell = 'attachments' (not a known primitive)_ |
| `destinationId` | string | ✓ | REQUIRED. Identifies the message recipient. When the MSP platform receives a message from Apple Messages for Business, the value is the business ID. When the MSP platform sends a reply to Apple Messages for Business, the value is the user’s opaque ID. |
| `group` | string |  | The group identifier for the message as specified by the business, such as the department name. For more information, see About Intent, Group, and Body Values. |
| `id` | string (uuid, src:UUID) | ✓ | REQUIRED. A UUID string that identifies the message. |
| `intent` | string |  | The intention, or purpose, of the chat as specified by the business, such as account_question. For more information, see About Intent, Group, and Body Values. |
| `locale` | string |  | User's device locale settings. For example, en_AU specifies the language as English and the region as Australia. For more information, see Internationalization and Localization Guide - Locale ID. |
| `sourceId` | string | ✓ | REQUIRED. A string that identifies the message sender. When a user sends a message, the source-id is the user’s opaque ID. When a business sends a reply to the customer, the source-id is the business ID. |
| `type` | string | ✓ | REQUIRED. A string that identifies the message type. For the list of possible values and their meanings, see Message Type Values. Possible values: interactive, typing_start, typing_end, text. |
| `v` | integer | ✓ | REQUIRED. The message payload version number. This value must be 1, which is the current version of the message JSON. |

<a id="jwt-claims"></a>
### JWT Authorization Fields (JOSE header + claims)

`jwt-claims` · canonical L136–145 · source `msp-rest-api` (rank 1, 2026-06-03) · 3col table

| Field | Type | Req | Description / note |
|---|---|:---:|---|
| `alg` | string |  | A string used in the header, identifying the algorithm used to encode the payload. The alg value is always HS256 when exchanging messages with Apple Messages for Business. |
| `aud` | string |  | A claim that is a string, or array of strings, identifying the recipients of the JWT. The value should be a string when the JWT has one recipient; otherwise, it should be an array of strings where each string represents a recipient. The aud value is always the MSP ID when exchanging messages with Apple Messages for Business. This value is used when sending messages from the business to the MSP platform |
| `iss` | string |  | A claim that is a string identifying the principal that issued the JWT. The value is always the MSP ID when exchanging messages with Apple Messages for Business. This value is used with traffic coming from the MSP platform to the business. |
| `iat` | _(unspecified)_ |  | A claim that is a numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519.<br>_source Type cell = 'dateTime' (not a known primitive)_ |
