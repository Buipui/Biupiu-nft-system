# Biupiu R&D OS v1.0 — Implementation Gate

Date: 2026-09-18

## Scope executed
Biupiu R&D OS now has a usable cross-platform prototype layer alongside the existing Android foundation and EVM NFT stack.

### Core functions
- Research-object registry with explicit evidence classes.
- Digital laboratory experiment logging.
- Audit-event records.
- Digital Asset & Provenance console.
- Deterministic SHA-256 mint payload generation.
- NFT release gate model: READY_FOR_REVIEW → TESTNET → VERIFIED → RELEASE.
- Local JSON workspace export.
- Offline-first PWA structure for Windows and Android browsers.
- Android navigation updated to expose Research, Digital Lab, Assets/NFT and Control Centre.

## Architecture
The web prototype is under `software/rnd-os-web/`.
The Android client remains under `software/rnd-os-mobile/`.
The existing Solidity/Hardhat minting layer remains under the repository Web3 structure.

## Control boundary
The prototype does not store private keys, sign transactions, or claim that an NFT has been minted on-chain. Testnet execution remains behind the existing contract/IP/provenance/release gates.

## Production gates
1. Backend/API persistence.
2. Authentication and role-based permissions.
3. Server-side append-only audit log.
4. Encrypted object storage.
5. GitHub/repository integration.
6. AI service integration.
7. Simulation/experiment runners.
8. Wallet/testnet signing integration.
9. Automated security and integrity tests.
10. Windows packaged client and production Android build.

## Testing
For the fastest first test, serve `software/rnd-os-web/` through a local HTTP server or GitHub Pages and open it in Chrome/Edge on Windows or Android. The PWA can then be installed where browser support permits.

## Repository status
This is a functional prototype gate, not a production release. It is intentionally designed so that stronger server-side controls can replace the local prototype storage without changing the conceptual research/provenance model.
