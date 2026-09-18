# Gate 5 — Subscriber Entitlement Engine

The OS now contains a client-side reference implementation of the Gate 4 subscriber model.

Decision order: account status -> tier capability -> department entitlement -> resource policy -> audit event.

The module is not the production security boundary. The server/API must independently enforce authorization before production deployment.

Department access is explicit through department entitlements and is not implied by subscription tier.
