# AMB Conformance Checklist

_Generated 2026-07-09T04:36:45.179940+00:00 from Apple's Required Features table (canonical L101–124)._

Each of Apple's required features mapped to the schema(s), endpoint(s), and fixture group(s) in this kit. Associations are **keyword-derived** from the extracted artifacts (not an official Apple mapping); `integrator-owned` rows have no direct spec artifact and must be built and demonstrated for approval.

- Features: **19**  ·  spec-linked: **14**  ·  integrator-owned: **5**


| Feature | Bot/API | Agent | Schemas | Endpoints | Fixtures | Status |
|---|:---:|:---:|---|---|---|---|
| Receiving and Sending Messages | Required | Required | `http-body`<br>`receivedmessage-dictionary`<br>`replymessage-dictionary` | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | text(6) | spec-linked |
| Receiving and Sending attachments | Required | Required | `imageitem-dictionary` | /preDownload<br>https://mspgw.push.apple.com/v1/preDownload<br>https://mspgw.push.apple.com/v1/preUpload | — | spec-linked |
| Tapback Reactions | N/A | Required | — | — | — | integrator-owned |
| Receiving Closed Conversation Messages | Required | Required | — | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | close-session(4) | spec-linked |
| Rich Link Messages | Required | Required | — | https://mspgw.push.apple.com/v1/constructPayload | — | spec-linked |
| Quick Reply Messages | Required | Optional | `dataquick-reply-dictionary`<br>`dataquick-reply-dictionary-1`<br>`quick-replyitems-dictionary` | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | — | spec-linked |
| List Picker Message | Required | Optional | `datalistpickersection-dictionary`<br>`listpickermessage-dictionary`<br>`listpickersectionlistpickeritem-dictionary` | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | — | spec-linked |
| Time Picker Message | Required | Optional | `dataevent-dictionary`<br>`eventitemlocationitem-dictionary`<br>`locationtimeitem-dictionary`<br>`timepickermessage-dictionary` | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | — | spec-linked |
| Apple Pay Message | Required | Optional | `applepayinteractivedata-dictionary`<br>`applepayitem-dictionary`<br>`applepaylineitems-dictionary`<br>`applepaymerchantcapabilities-dictionary`<br>+16 | /message<br>https://msp.example.com/message<br>https://msp.example.com/paymentGateway | apple-pay(8) | spec-linked |
| Authentication Message | Required | Optional | `dataauthenticate-dictionary`<br>`dataauthenticateoauth2-dictionary`<br>`interactivedatadataauthenticate-dictionary` | https://mspgw.push.apple.com/v1/authenticate | authentication(3) | spec-linked |
| Authentication Message | Deprecated | Deprecated | `dataauthenticate-dictionary`<br>`dataauthenticateoauth2-dictionary`<br>`interactivedatadataauthenticate-dictionary` | https://mspgw.push.apple.com/v1/authenticate | authentication(3) | spec-linked |
| iMessage Apps | Required | Optional | `applepayinteractivedata-dictionary`<br>`baseinteractivemessage-dictionary`<br>`interactivedata-dictionary`<br>`interactivedata-dictionary-1`<br>+6 | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | — | spec-linked |
| Form Message | Required | Required | — | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | form(6) | spec-linked |
| Construct Payload API | Required | Required | — | https://mspgw.push.apple.com/v1/constructPayload | — | spec-linked |
| Invitation Messages | Required | Required | — | — | — | integrator-owned |
| Typing Indicator Message | Required | Required | `http-body` | /message<br>https://msp.example.com/message<br>https://mspgw.push.apple.com/v1/message | — | spec-linked |
| Routing based on entrypoint parameters | Required | Required | — | — | — | integrator-owned |
| Channel settings and Landing Page | Required | Required | — | — | — | integrator-owned |
| Device capabilities | Required | Required | — | — | — | integrator-owned |

## Integrator-owned features (no direct spec artifact)

- **Tapback Reactions** — Detect user tapbacks.
- **Invitation Messages** — Send invitation messages to opted-in customers to initiate a conversation via Apple Messages for Business using their provided mobile number.
- **Routing based on entrypoint parameters** — Route new conversations using intentID and groupID attributes.
- **Channel settings and Landing Page** — Centrally host channel settings and provide a landing page with account linking
- **Device capabilities** — Support alternate handling for devices with different capabilities.