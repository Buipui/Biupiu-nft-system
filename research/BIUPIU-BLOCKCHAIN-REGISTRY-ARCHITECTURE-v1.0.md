# Biupiu Blockchain Registry Architecture v1.0

**Date:** 16 September 2026  
**Status:** Architecture / implementation specification — no production deployment

## Objective

Create a durable blockchain anchoring layer for the Biupiu computational-art and research network. The blockchain records approved commitments to research-linked releases; GitHub remains the detailed source and development record.

## Network model

```text
GitHub canonical record
       │
       ├── research ID
       ├── algorithm ID/version
       ├── parameters + seed
       ├── artwork pair
       ├── metadata
       └── SHA-256 / manifest hash
                │
                ▼
      Biupiu Research Registry
                │
                ├── release ID
                ├── research hash
                ├── algorithm hash
                ├── asset/manifest hash
                └── timestamp / submitter
                │
                ▼
          Biupiu NFT Contract
                │
                └── token URI + token ID
```

## Contract roles

### 1. BiupiuNFT
Existing ERC-721 ownership/minting contract. It should remain focused on NFT ownership and token metadata.

### 2. BiupiuResearchRegistry
Planned registry contract. Its purpose is to anchor approved research/algorithm/release commitments without exposing confidential material.

Suggested record fields:

- release ID
- research ID
- algorithm ID
- algorithm version
- release manifest hash
- artwork hash(es)
- metadata hash
- Git commit identifier
- optional NFT contract address
- optional token ID
- timestamp
- registrar address

## On-chain vs off-chain

**Off-chain:** source code, full research files, large artwork files, private datasets, confidential IP, working notes and detailed computational inputs where publication is not approved.

**On-chain:** identifiers, cryptographic hashes, approved release status and links/URIs where appropriate.

## Integrity model

For each approved release:

`source + parameters + artwork + metadata → manifest → SHA-256 → registry anchor`

A later observer can retrieve the public GitHub release, recompute the expected digest and compare it with the anchored commitment.

## Network progression

### Phase 1 — Current
Ethereum Sepolia and Polygon Amoy testnet targets; existing NFT contract and mint scripts.

### Phase 2 — Registry prototype
Implement and test `BiupiuResearchRegistry` locally, then testnet.

### Phase 3 — Integrated release pipeline
Automatically generate a release manifest and registry transaction payload after IP/licence approval.

### Phase 4 — Production governance
Select production chain, custody model, contract verification procedure and operational controls separately from the artistic algorithm pipeline.

## Security

No private key, seed phrase or `.env` file is stored in the repository. Registry writes should be performed only by an authorised release wallet. Consider multisig/role separation before production.

## Important distinction

This is a blockchain **registry/anchoring architecture**, not a claim that Biupiu has launched its own independent Layer-1 blockchain. An independent chain could be considered later if scale and governance justify it.
