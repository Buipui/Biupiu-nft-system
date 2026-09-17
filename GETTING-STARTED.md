# BIU NFT System — Getting Started

This repository is a research-to-publication system. It records research, algorithms, artwork provenance, metadata, release manifests, and optional blockchain anchors.

## Current workflow

1. Create a research record and assign a Research ID.
2. Classify evidence: DOCUMENTED, RECONSTRUCTED, EXPERIMENTAL, HYPOTHESIS, or SPECULATIVE.
3. Record the algorithm family, version, parameters, seed, software, and source commit.
4. Create the artwork pair: `01_PROVENANCE` and `02_STANDALONE`.
5. Create and review metadata and rights information.
6. Create a release manifest and hashes.
7. Run local tests and security review.
8. Deploy only to a testnet first.
9. Anchor approved hashes in `BiupiuResearchRegistry`.
10. Mint only after the release gate is approved.

## Important distinction

The repository is currently a strong documentation and provenance framework, not yet a fully automated research platform. Some folders and commands described in planning documents still need implementation.

## Safety rules

- Never commit private keys, seed phrases, `.env` files, or confidential research.
- Do not use placeholder IPFS hashes for a real release.
- Do not describe NFT ownership as transfer of patents, copyright, equity, or investment rights unless a separate legal document says so.
- Treat the smart contracts as experimental until they compile, pass tests, and receive review.

## First practical milestone

Before any real deployment, complete one local end-to-end record using the Master Template, real artwork files, real hashes, tests, and a documented testnet transaction.

See `QUICK-START.md`, `docs/TESTNET-CHECKLIST.md`, and `MASTER-TEMPLATE.md`.
