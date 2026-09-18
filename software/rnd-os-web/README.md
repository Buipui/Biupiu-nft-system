# Biupiu R&D OS Web Prototype v1.0

A usable offline-first prototype for Windows and Android browsers/PWA installation.

## Included
- Dashboard
- Research-object registry with evidence classification
- Digital experiment logger
- Audit-event log
- Digital Asset & NFT provenance console
- Deterministic SHA-256 mint payload generation
- Local JSON workspace export
- Installable PWA/offline cache

## NFT safety boundary
This prototype prepares a canonical mint payload and provenance hash. It does not store private keys, sign transactions, or claim that an asset is minted on-chain. Real testnet minting remains behind the existing Hardhat/EVM workflow and release gates.

## Testing
Serve this folder from a local HTTP server or GitHub Pages. Open the hosted origin, then use the browser install option on Windows/Android. LocalStorage is used for the prototype workspace.

## Next production gates
API/backend persistence → authentication/roles → server-side audit log → encrypted object storage → GitHub integration → AI service → simulation runners → wallet/testnet integration → automated security tests.


## Gate 2 — Shared control architecture
The next gate formalizes the prototype as a shared OS contract for Windows/PWA and Android: the same record IDs, evidence classes, experiment lifecycle, audit events, asset provenance fields and NFT release states must be preserved across clients. Local clients are test interfaces only; production authority belongs in the future server/API layer.

### Canonical entities
- ResearchObject
- Experiment
- EvidenceRecord
- AuditEvent
- DigitalAsset
- MintPayload
- ReleaseGate

### Release gates
DRAFT → REVIEW → TESTNET → VERIFIED → RELEASED. No client is permitted to bypass the gate in production.

### Security requirements
No private keys, seed phrases or production credentials in the repository. Server-side authorization, append-only audit storage, encryption, backup and wallet separation are required before production use.
