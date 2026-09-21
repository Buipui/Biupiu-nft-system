# Native Payment Security Verification Gates v1

G0 DESIGN — PASS: provider-neutral boundary; default deny; client cannot grant paid access; blockchain separated from entitlement authority.

G1 ANDROID — REQUIRED: Google Play Billing; purchase token sent to backend; Android Keystore/StrongBox where available; standard TLS/platform security APIs; no secrets in source.

G2 BACKEND — REQUIRED: Google Play Developer API verification; RTDN treated only as a change signal; authoritative reconciliation; idempotency; replay protection; lifecycle reconciliation; least privilege; auditable entitlement transitions.

G3 TRUST/BLOCKCHAIN — REQUIRED BEFORE ENABLEMENT: only hash/receipt metadata that is safe to anchor; never payment tokens or secrets; optional registry anchor; NFT minting cannot create subscription entitlement.

G4 ADVERSARIAL TESTS — REQUIRED: forged token, replay, duplicate event, stale event, pending purchase, expiration, cancellation, grace period, account hold, refund/revocation, tier escalation, department escalation, offline client tampering and rooted-device manipulation.

G5 PRODUCTION — REQUIRED: independent security review; Android/backend integration tests; Play Console configuration; credentials outside source control; monitoring; incident response; key rotation/revocation; signed release process.

Promotion rule: architecture status is not production verification. A gate becomes VERIFIED only after executable evidence exists.
