# Biupiu Native Payment Gate v1

Status: ARCHITECTURE INTEGRATED — PROVIDER IMPLEMENTATION GATED

Purpose: one payment boundary for Biupiu OS, Biupiu World and DMS. Paid access is never granted by the client.

Authoritative flow:
Android/client -> Payment Gate -> provider verification backend -> DMS entitlement core -> audit/trust layer -> optional blockchain anchor.

Rules:
- Google Play Billing is the Android digital-subscription provider when Play distribution requires it.
- Purchase tokens are verified by the secure backend before entitlement is granted.
- RTDN is an event signal; authoritative state is re-read from Google Play Developer API.
- DMS remains authoritative for capability access.
- Existing BPU/NFT/blockchain architecture is an optional settlement/provenance layer, never proof of a Google Play subscription.
- Default deny and fail closed.
- No card data, provider credentials, private keys, seed phrases or signing secrets in the client or repository.
- Android Keystore/StrongBox is used for local device-bound key material where available.
- Payment operations are idempotent and replay-resistant.
- Pending, expired, canceled, held, refunded and revoked states never retain paid access unless the authoritative entitlement state says so.
- Undeployed BPU remains disabled/non-spendable.

Provider adapters:
- NATIVE_GOOGLE_PLAY: enabled for Android Play distribution after backend verification is deployed.
- BPU_CHAIN: design-compatible but disabled until asset/network, custody, issuance, compliance and security gates pass.
- EXTERNAL_PROVIDER: future adapter only.

This boundary deliberately reuses the existing subscriber-tier, DMS entitlement, BPU coin and NFT/provenance architecture instead of creating a second entitlement system.
