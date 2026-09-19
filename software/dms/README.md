# Biupiu DMS Runtime v0.1

First executable DMS authorization service derived from the DMS v1.0 architecture.

Implemented: central policy engine; role-based access; subscription entitlements; explicit entitlement/revocation overrides; site/product scope; MFA gates; account status; feature registry and safety classification; automatic effective-access calculation; in-memory authorization audit stream; fail-closed unknown-feature handling.

Decision order: feature registration -> active account -> role -> subscription -> explicit entitlement/revocation -> MFA -> scope -> grant + audit.

Essential functions are not disabled merely because an optional subscription entitlement is missing. Experimental functions return an explicit consent obligation.

This is an executable authorization foundation, not yet a production identity provider, payment system or distributed database.
