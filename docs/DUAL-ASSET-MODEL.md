# Dual-Asset Model

The BIU model separates a research-linked release into two complementary records:

- **01_PROVENANCE** — the documentary research and provenance presentation.
- **02_STANDALONE** — the independent collector-facing artwork.

They share a Research ID and Release ID, but each asset should retain its own file, hash, metadata record, and version history.

## Research boundary

The repository is primarily a research and provenance tool. NFT ownership does not automatically transfer copyright, patents, inventions, confidential research, source code, or other intellectual-property rights.

## Release record

Before minting, a release should document:

1. research source and evidence classification;
2. algorithm family and version;
3. parameters, seed, dependencies, and source commit;
4. provenance and standalone artwork files;
5. metadata and rights review;
6. release manifest and hashes;
7. optional registry anchor.

## Current status

The contracts are experimental prototypes. The no-mint smoke tests verify local contract generation and initial state only. They do not prove security, testnet deployment, metadata hosting, or production readiness.
