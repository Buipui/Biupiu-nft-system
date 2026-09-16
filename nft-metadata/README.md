# BIU NFT Metadata Standards

## Overview

This directory contains the JSON metadata files for all BIU dual-asset NFT pairs. Each asset follows the ERC-721 metadata standard with extended properties for the dual-asset model.

## Naming Convention

```
BIU-[TYPE]-[NUMBER]-[VARIANT].json

BIU-ART-0001-A.json      # Artwork (primary)
BIU-COA-0001.json        # Certificate of Authenticity (supporting)
```

- **TYPE**: `ART` (artwork) or `COA` (certificate)
- **NUMBER**: Sequential collection number (0001, 0002, etc.)
- **VARIANT**: Optional variant identifier (A, B, C for different editions)

## File Structure

### BIU-ART (Provenance Artwork)

```json
{
  "name": "Human-readable title",
  "description": "Detailed description with dual-asset context",
  "image": "ipfs://hash/preview.png",
  "external_url": "https://biu-nft.studio/artworks/BIU-ART-XXXX-X",
  "attributes": [...],
  "dual_asset": {
    "paired_token": "BIU-COA-XXXX",
    "bond_status": "Active|Severed|Pending"
  },
  "provenance": {
    "minter": "0x...",
    "mint_date": "ISO8601",
    "contract": "BIUArtwork.sol"
  }
}
```

### BIU-COA (Certificate of Authenticity)

```json
{
  "name": "BIU Certificate of Authenticity #XXXX",
  "description": "Detailed description with dual-asset context",
  "image": "ipfs://hash/preview.png",
  "attributes": [...],
  "dual_asset": {
    "paired_token": "BIU-ART-XXXX-X",
    "bond_status": "Active"
  },
  "certificate": {
    "proof_hash": "0x...",
    "authenticity_guarantee": "Verified by BIU Provenance Registry"
  },
  "governance": {
    "voting_enabled": true,
    "voting_weight": 1
  }
}
```

## Required Fields

All metadata files MUST include:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Asset name (max 100 chars) |
| `description` | string | Full description (max 500 chars) |
| `image` | string | IPFS URL or HTTP URL |
| `external_url` | string | Official website link |
| `attributes` | array | Trait array (see below) |
| `dual_asset` | object | Dual-asset relationship |
| `provenance` | object | Minting/issuing information |

## Attributes Standard

All assets use a consistent attribute structure:

```json
"attributes": [
  {
    "trait_type": "Collection",
    "value": "Genesis"
  },
  {
    "trait_type": "Asset Type",
    "value": "Provenance Artwork | Certificate of Authenticity"
  },
  {
    "trait_type": "Creator",
    "value": "Studio BIU"
  }
]
```

### Standard Trait Types

**Universal Traits:**
- Collection
- Asset Type
- Creator
- Edition

**Artwork-Specific Traits:**
- Medium (Digital, Physical, Hybrid)
- Dimensions
- Certification Status
- Bonded Certificate
- Royalty Percentage

**Certificate-Specific Traits:**
- Artwork Bonded
- Proof Type
- Issuer
- Governance Weight
- Burnable

## Dual-Asset Bonding

Every artwork and certificate pair maintains a cryptographic bond:

```json
"dual_asset": {
  "model": "BIU Dual-Asset Bond",
  "paired_token": "BIU-ART-0001-A | BIU-COA-0001",
  "relationship": "Artwork to Certificate | Certificate to Artwork",
  "bond_type": "Keccak256 Hash Chain",
  "bond_status": "Active",
  "bond_created_at": "2026-09-16T00:00:00Z"
}
```

### Bond States

- **Active**: Both tokens exist and are cryptographically bonded
- **Severed**: Certificate burned or artwork transferred without certificate
- **Pending**: Certificate awaiting proof verification

## Provenance Tracking

All metadata includes complete provenance chain:

```json
"provenance": {
  "minter": "0x...",
  "mint_date": "ISO8601",
  "contract": "BIUArtwork.sol | BIUCertificate.sol",
  "blockchain": "Ethereum Testnet (Sepolia)",
  "chain_id": 11155111,
  "provenance_hash": "0xkeccak256(...)"
}
```

## IPFS Hosting

All image and document files are stored on IPFS:

1. **Preview Images** (PNG, 1200x800px)
   ```
   ipfs://QmPlaceholder/biu-art-0001-a-preview.png
   ipfs://QmPlaceholder/biu-coa-0001-preview.png
   ```

2. **Full Resolution** (PNG/PDF, high-res)
   ```
   ipfs://QmPlaceholder/biu-art-0001-a-fullres.png
   ipfs://QmPlaceholder/biu-coa-0001-fullres.pdf
   ```

3. **Pinning Service**: Pinata (automatic backup)

## Validation Checklist

Before deploying metadata to production:

- [ ] All required fields present
- [ ] IPFS URLs resolve correctly
- [ ] Dual-asset pairs match (`BIU-ART-XXXX` ↔ `BIU-COA-XXXX`)
- [ ] Attributes are valid and complete
- [ ] Provenance hashes are correct
- [ ] External URLs return 200 status
- [ ] JSON validates against schema
- [ ] No duplicate token IDs
- [ ] Metadata immutable (IPFS pinned)

## Example Metadata Files

- `BIU-ART-0001-A.json` - Genesis artwork
- `BIU-COA-0001.json` - Genesis certificate

## References

- [ERC-721 Metadata Standard](https://docs.opensea.io/docs/contract-level-metadata)
- [JSON Schema Validator](https://www.jsonschemavalidator.net/)
- [IPFS Documentation](https://docs.ipfs.io/)

---

**Last Updated:** September 16, 2026  
**Maintainer:** BIU Studio