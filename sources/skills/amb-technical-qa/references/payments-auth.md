# Apple Pay & Authentication

Primary source: [Apple Pay Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#apple-pay-message) and [Authentication Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#authentication-message).

## Contents

- [Apple Pay: division of responsibility](#apple-pay-division-of-responsibility)
- [The three domains](#the-three-domains)
- [Merchant ID cardinality and merchant of record](#merchant-id-cardinality-and-merchant-of-record)
- [Certificates](#certificates)
- [The payment flow](#the-payment-flow)
- [Fields that cause most failures](#fields-that-cause-most-failures)
- [Endpoints dictionary](#endpoints-dictionary)
- [merchantSession and paymentRequest](#merchantsession-and-paymentrequest)
- [Refunds, fees, errors](#refunds-fees-errors)
- [The brand-subdomain design](#the-brand-subdomain-design)
- [OAuth 2.0](#oauth-20)

---

## Apple Pay: division of responsibility

Apple handles tokenization and the merchant session. The brand's own gateway and PSP process the actual payment. The MSP carries and authenticates the Apple Pay messages and routes the encrypted token to the brand's gateway.

Apple Pay is a **mandatory MSP platform capability** — it must be built and demonstrated before any brand goes live, even if no launch brand intends to use it.

## The three domains

Most integration pain comes from treating these as one system.

| Domain | What lives there | Owner |
|---|---|---|
| [Apple Developer portal](https://developer.apple.com/apple-pay) | Apple Pay Merchant ID, Payment Processing Certificate, Merchant Identity Certificate, domain association and verification | Merchant of record — normally the brand's Apple Developer account |
| [Apple Business Register](https://register.apple.com) | AMB account, branding, response hours, MSP selection, End User Authentication fields, Merchant ID association under Optional Integrations, Experience Review | The brand's organization, with the MSP selected |
| MSP platform | `/message` endpoint, client landing page, payment-session request, the Apple Pay interactive message, gateway endpoint receiving the token, OAuth callback endpoints, per-brand channel settings | The MSP |

The first two are configuration and approval work. The third is where the code lives. The MSP stores Merchant ID, verified domain, merchant name, PEM certificate, and payment gateway URL per brand in channel settings.

Registration requires three named roles on the brand side: an administrator who registers the organization and approves the terms, a technical contact using an alias email at the brand domain, and a sponsoring executive who agrees to the terms. **Those three cannot be the MSP.** What stays with the brand regardless: account ownership, terms approval, MSP selection from the Register list, and submitting the account to go online.

MA operational note (not Apple-documented either way): an MSP team member can be added to the brand's Business Register team and configure on the brand's behalf, including entering End User Authentication values. Apple documents brand ownership and the three roles but doesn't address delegated team members. Not common practice, but it works.

## Merchant ID cardinality and merchant of record

Apple's rule is directional rather than restrictive: **each AMB account holds exactly one associated Merchant ID, and a single Merchant ID may be used across more than one AMB account.** You can never point one AMB account at two Merchant IDs.

So pooling isn't forbidden by cardinality. What actually constrains it (MA reading): the Merchant ID belongs to whoever holds the Apple Developer account, and the `domainName` you send must match a domain verified on that merchant account. You cannot point a brand's account at your own Merchant ID unless you are genuinely the merchant of record and the verified domain matches.

**The two models**

| | Model A: merchant managed | Model B: Web Merchant Registration API |
|---|---|---|
| Brand needs Apple Developer account | Yes | No |
| Merchant ID held by | The brand | The MSP, as Payment Platform Integrator |
| Decryption key held by | The brand's PSP | The MSP, shared across portfolio |
| Domain registration expiry | Standard, per brand | Does not expire |
| Certificate maintenance | Per brand, every 25 months | Once, on shared config |
| Native in-app Apple Pay | Supported | Not supported, web only |
| Hosted payment pages | Not supported | Supported |
| Compliance perimeter | Outside the MSP | Through the MSP |

Under Model B, per-merchant values are still required for every brand: domain name, merchant name, PEM file, payment gateway URL, base domain URL. It removes setup overhead per brand, not per-brand configuration.

**The trade, stated plainly:** the model that removes onboarding friction is the model that moves the keys onto the MSP, which is exactly what puts the MSP inside the compliance perimeter it's trying to stay out of.

**Where the compliance line actually falls** (MA interpretation, not an Apple statement, and not legal advice): hosting a static domain association file does not place anyone inside the payment perimeter — the file is a public proof-of-control artifact. What determines exposure is **custody of the Payment Processing Certificate private key**, because that key decrypts the payment token. If the MSP never generates and never holds that key, it never sees a card credential while still creating the merchant session and observing every transaction event.

## Certificates

| Certificate | Purpose | Lifetime |
|---|---|---|
| Payment Processing Certificate | Encrypts and decrypts the Apple Pay payment token | **25 months** — transactions fail the moment it expires |
| Merchant Identity Certificate | Authenticates your server to Apple when requesting a payment session | — |

Both are issued after the Merchant ID exists. Renewal is a prepare-then-activate sequence coordinated with the PSP; under the merchant-managed model that clock runs per brand, and it is the most commonly missed operational item at scale. Track expiry from day one.

The portal-issued `.cer` must be converted to PEM for server use (keytool ECC-256 plus openssl).

**Lead times.** Apple Developer Program access up front. Merchant account approval: plan several days. AMB account approval including Experience Review: 2–4 weeks. Start the merchant account before the first sprint that touches payments.

## The payment flow

1. Request a new Apple Pay payment session from Apple, server-side, at `https://apple-pay-gateway.apple.com/paymentservices/paymentSession`
2. Add the returned `merchantSession` object to the payment dictionary
3. Add `paymentRequest` (transaction details) and `endpoints` dictionaries
4. Send as an interactive message to AMB
5. Apple forwards to the customer's device
6. Customer authorizes with Touch ID / Face ID
7. The device sends the encrypted payment token plus contact info to your `paymentGatewayUrl`
8. Your system processes and returns the transaction result

The session endpoint is not reachable from a private network.

## Fields that cause most failures

- **`initiative`** must be `"messaging"`. No other value is accepted for AMB.
- **`initiativeContext`** must be the full HTTPS URL of your payment gateway endpoint, must match `endpoints.paymentGatewayUrl` **exactly**, and must be publicly exposed.
- **`domainName`** must be included in the session request. Omit it and the token is valid only for Apple Pay on the Web, not Apple Pay in Messages. It is the base host with no prefix or punctuation (e.g. `developer.apple.com`) and must match the merchant account's verified domain.

## Endpoints dictionary

| Endpoint | Required | Purpose | Timeout |
|---|---|---|---|
| `paymentGatewayUrl` | Yes | Apple Pay calls this to process the payment | 30 s |
| `fallbackUrl` | No | Opens in a browser if the device can't pay via Apple Pay | — |
| `orderTrackingUrl` | No | Called after order completion to update order info | — |
| `paymentMethodUpdateUrl` | No | Called when the customer changes payment method | 30 s |
| `shippingContactUpdateUrl` | No | Called when the customer changes shipping address | 30 s |
| `shippingMethodUpdateUrl` | No | Called when the customer changes shipping method | 30 s |

**The trap:** including an optional key without implementing the endpoint surfaces an error to the customer mid-checkout. Only send keys you have actually built. Each callback times out at 30 seconds.

Prior to authorization you receive *redacted* shipping contact information — only what's needed for tax or shipping calculation.

## merchantSession and paymentRequest

**merchantSession** (required fields): `displayName` (canonical store name, ≤64 UTF-8 characters, **do not localize**), `epochTimestamp`, `expiresAt`, `initiative`, `initiativeContext`, `merchantIdentifier`, `merchantSessionIdentifier`. Optional: `nonce` (single-use integrity string), `signature`. `signedFields` is recommended practice.

**paymentRequest** (required): 

- `applePay` — `merchantIdentifier` (required), `merchantCapabilities` (must include `supports3DS`; optionally `supportsCredit`, `supportsDebit`, `supportsEMV`), `supportedNetworks` (one or more of `amex`, `discover`, `jcb`, `masterCard`, `privateLabel`, `visa`)
- `countryCode` — two-letter ISO 3166
- `currencyCode` — three-letter ISO 4217
- `lineItems` — each with `amount` and `label` (required) and optional `type` (`final`/`pending`). Not required, but **cannot be empty if the key is present**
- `total` — **must be greater than zero** to pass validation. Its label appears on the payment sheet; use the brand's doing-business-as name

Optional: `requiredBillingContactFields` (from `email`, `name`, `phone`, `phoneticName`, `post`), `requiredShippingContactFields`, `shippingMethods` (first item is the default), `supportedCountries`.

Request only the contact fields you need — unnecessary fields add complexity and increase cancellation.

## Refunds, fees, errors

**Refunds:** there is no refund message type. Apple Pay refunds must be handled entirely outside AMB.

**Fees:** Apple does not charge for Apple Pay within AMB. It charges elsewhere (web and other surfaces) but not in this channel. Subscriptions are supported, also with no Apple fee.

**A 400 on the interactive Apple Pay message** almost always means the Merchant ID is not registered on that Business Register account.

**Instrumentation:** request sent → sheet opened → authorized → fulfilled. Abandonment between sheet-open and authorize reveals friction — too many required fields, unsupported network, wrong currency.

**Device support:** works on all Apple Pay-capable iPhone and iPad devices. No capability-list flag, so no check before sending. Still consider `fallbackUrl` for devices that can't complete a payment.

## The brand-subdomain design

Linq's proposal: add a brand-specific subdomain (e.g. `doordash.pay.linqapp.com`), have the brand register that domain on its own Apple account, let Apple issue the domain association file, have the brand pass it to Linq, and have Linq host it. Goal: avoid becoming the payment compliance party while still observing that payments occurred.

MA's assessment — viable, with support from three points in Apple's material:

1. Subdomains are explicitly in scope; Apple instructs merchants to register and verify all top-level domains and subdomains where Apple Pay is used.
2. Verification is a proof-of-control test, not proof of ownership. Nothing in the documented flow requires the merchant to be the party physically hosting the file.
3. Apple's Platform Integration Guide already contemplates a platform hosting the file, including on its own domain.

Caveat: Apple's explicit sanction for platform-hosted domains sits in the Web Merchant Registration API context, where the association file belongs to the platform's Payment Platform Integrator ID. Linq's design is merchant-managed with delegated hosting — mechanically identical, nothing prohibits it, but not the exact configuration Apple wrote down.

**Constraints that will actually bite**

- **No proxy, no redirect.** Apple requires the well-known path reachable directly by Apple's servers. A CDN or edge proxy in front of the origin is the single most likely cause of failed verification. It fails at setup rather than silently at runtime.
- **One file per fully qualified domain name.** Each association file is tied to the Merchant ID that issued it, so a single shared host serving several brands will not work. The per-brand subdomain is load-bearing, not cosmetic.
- **Hosted payment pages.** Apple states the merchant-managed model doesn't support them. Terminating a gateway call on the subdomain is not the same as rendering a checkout page there — if you ever render one, the design has drifted into Model B.

## OAuth 2.0

→ [Authentication Message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#authentication-message)

OAuth 2.0 authorization code flow, OpenID Connect compatible. The device initiates; the business or MSP completes. Requires iOS 16 / iPadOS 16 / macOS 13 and the `AUTH2` capability. Legacy `AUTH` is deprecated — if `AUTH2` is absent, do not send and handle it gracefully.

Changed from the legacy flow: no private/public key generation, and no client secret in the payload.

**Endpoint:** `POST https://mspgw.push.apple.com/v1/authenticate`, `version` set to `2.0`, with an `authenticate.oauth2` object containing:

| Field | Notes |
|---|---|
| `responseType` | Required. `code` for authorization flow |
| `scope` | Required. Array specifying exactly what data the provider returns |
| `state` | Required. See below |
| `redirectURI` | Required. Where the provider redirects the user |
| `additionalParameters` | Optional query parameters for custom providers |

**Constructing `state`.** This prevents request forgery, so it matters. Build a session token unique to that session from a high-quality random number, combined with the Opaque ID — Apple's example format is `<cryptographic random string> & <OpaqueID>`. That gives anti-forgery protection and, with `requestIdentifier`, a link back to the user. A static value an attacker could predict defeats the purpose.

**Certificate:** the OAuth endpoints must present a valid Extended Validation certificate when the request is sent to the provider.

**Closing the flow:** redirect to `messages-auth://?status=success` (or `failure`, `cancel`, `unknown`, with optional `error_code`). This closes the window and the bubble. Send a welcome message afterward. A webhook event fires carrying that status.

**Required UX:** the user must be given context about what they are authenticating into before the flow begins. Apple checks for this. An agent bubble explaining the step is the pattern.

**Who configures what**

- MSP side: register the application, capture the Client ID, set the authorized redirect URL to match the `redirectURI` your platform sends, enable the right sign-in product and scopes, host the callback on a publicly reachable HTTPS endpoint with a valid certificate.
- Brand side in Apple Business Register: the OAuth URL and Client Identifier go in the End User Authentication section, and the brand requests the **security audit** that unlocks the provider. Apple typically approves in 2–3 business days.
- MSP platform stores per-brand channel settings: title, response type, scope, client secret, OAuth URL, token URL.

Key pairs can be generated by either the MSP or the brand, for either flow.

**Sequencing:** have the brand request the authentication security audit early, in parallel with your build, since it gates OAuth go-live. Along with settling the Apple Pay model and Merchant ID registration, these are the only genuinely serial items — everything else runs alongside.

**Password AutoFill** is supported. Annotate the authorization input with `autocomplete` values `username`, `current-password`, `new-password`, or `one-time-code`.

**Use cases:** order history, account profile, billing, claims — anything needing verified identity. Integrates with iOS authentication including Face ID.
