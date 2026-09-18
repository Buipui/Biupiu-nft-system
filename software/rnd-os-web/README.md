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
