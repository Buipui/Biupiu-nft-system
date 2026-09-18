# AI-15 — Authenticated Gateway Transport Specification & CI Gate

## Implemented

- explicit bearer-header validation contract at the server boundary
- authorization redaction helper for logs/diagnostics
- Android gateway request/response contract remains token-injection based
- CI workflow specification for AI contract tests and credential-literal checks

## Authentication boundary

The client supplies a bearer token to the gateway contract. The repository does not choose an identity provider, issue tokens, persist tokens, or embed provider API keys. A production identity provider and token verification implementation must be selected separately.

## CI boundary

The intended workflow runs the deterministic Python AI contract tests and checks the AI/mobile source trees for common credential-like literals. It uses read-only repository permissions and no model-provider secret.

## Acceptance criteria

1. Authentication format is validated without exposing token contents.
2. Authorization material is redacted before diagnostic output.
3. CI is defined to exercise AI-12 through AI-15 contract tests.
4. CI is defined to perform a credential-literal safety check.
5. Live provider access remains disabled until identity, token verification, transport security, privacy, rate/cost controls and failure handling are validated.

## Verification status

**Implemented:** authentication contract and tests.

**Specification added:** CI contract and security-check workflow design.

**Not verified here:** GitHub Actions execution, production identity-provider integration, Android compilation/network execution, or live external model transport. The workflow file could not be committed because the GitHub contents operation returned repeated repository state conflicts; no successful CI run is being claimed.

## Next gate

AI-16: production gateway request schema, rate/cost policy and live-provider staging boundary.
