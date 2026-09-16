# 🚀 BIU NFT Dual-Asset Launch Plan

## Vision
A revolutionary NFT framework that pairs **provenance artwork** with **certificates of authenticity** as standalone, tradeable assets. Each artwork generates two complementary NFTs with unique economic and governance properties.

---

## 📋 Launch Architecture

### Dual-Asset Model
```
BIU-ART-XXXX-A (Primary Artwork Asset)
    ↔ Cryptographic Bond ↔
BIU-COA-XXXX (Certificate of Authenticity)
```

**Example Launch Pair:**
- **BIU-ART-0001-A**: Provenance artwork NFT
- **BIU-COA-0001**: Standalone certificate NFT

### Key Properties

| Property | BIU-ART | BIU-COA |
|----------|---------|---------|
| Primary Asset | Yes | No (Support) |
| Transferable | Yes | Yes |
| Burnable | No | Yes (revokes proof) |
| Composable | Yes | Yes |
| Standalone Value | High | Authentication + Governance |

---

## 🎨 Example Assets

### Asset 1: Digital Genesis
**BIU-ART-0001-A**
- Type: Digital Artwork (PNG, 4000x3000px)
- Theme: Genesis collection launch
- Creator: Studio BIU
- Edition: 1/1 (Unique)

![Genesis Artwork Placeholder](docs/imagery/biu-art-0001-a-preview.png)

**Metadata Anchor:** `/nft-metadata/BIU-ART-0001-A.json`

---

### Asset 2: Authentication Certificate
**BIU-COA-0001**
- Type: Certificate of Authenticity
- Bonded To: BIU-ART-0001-A
- Proof Type: Keccak256 hash chain
- Governance: Holder vote weight on authenticity disputes

![Certificate Placeholder](docs/imagery/biu-coa-0001-preview.png)

**Metadata Anchor:** `/nft-metadata/BIU-COA-0001.json`

---

## 📦 Repository Structure

```
biupiu-nft-system/
├── LAUNCH-PLAN.md                 # This file
├── README.md                       # Project overview
├── contracts/
│   ├── BIUArtwork.sol             # Primary artwork token
│   ├── BIUCertificate.sol         # Certificate token
│   └── BIUProvenanceRegistry.sol   # Dual-asset bonding
├── nft-metadata/
│   ├── BIU-ART-0001-A.json       # Artwork metadata
│   ├── BIU-COA-0001.json         # Certificate metadata
│   └── README.md                  # Metadata standards
├── docs/
│   ├── DUAL-ASSET-MODEL.md       # Technical specification
│   ├── TESTNET-CHECKLIST.md      # Deployment validation
│   ├── imagery/
│   │   ├── biu-art-0001-a-preview.png
│   │   └── biu-coa-0001-preview.png
│   └── landing/
│       └── index.html             # Landing page
├── tests/
│   ├── BIUArtwork.test.js
│   └── BIUCertificate.test.js
└── deploy/
    └── deploymentConfig.json
```

---

## 🎯 Launch Milestones

### Phase 1: Foundation (Week 1-2)
- [x] Define dual-asset model
- [ ] Create metadata specifications
- [ ] Generate example imagery
- [ ] Build landing page
- [ ] Write smart contracts

### Phase 2: Testing (Week 3)
- [ ] Unit test coverage >90%
- [ ] Testnet deployment
- [ ] Validate metadata resolution
- [ ] Security audit (internal)

### Phase 3: Genesis Launch (Week 4)
- [ ] Deploy to mainnet
- [ ] Mint BIU-ART-0001-A + BIU-COA-0001
- [ ] Announce launch
- [ ] Community onboarding

---

## 🔗 Dual-Asset Bonding Mechanism

### Smart Contract Logic
```solidity
// When artwork is minted
emit ArtworkMinted(tokenId, metadataURI, artist);

// Certificate automatically bonds
emit CertificateMinted(certId, artworkTokenId, provenanceHash);

// Dual-asset pair created
emit DualAssetPairCreated(artworkTokenId, certId, bondedAt);
```

### Economic Model

1. **Artwork Transfer** → Certificate follows or requires authorization
2. **Certificate Burn** → Optionally revokes authenticity proof
3. **Both Tradeable** → Independent liquidity pools possible
4. **Value Composition** → Combined utility exceeds individual assets

---

## 📊 Genesis Collection Details

### BIU-ART-0001-A Specifications
- **Contract:** BIUArtwork.sol
- **Token Standard:** ERC-721
- **Metadata:** IPFS hash
- **Royalty:** 10% (creator)
- **Unlock Condition:** Bound certificate must exist

### BIU-COA-0001 Specifications
- **Contract:** BIUCertificate.sol
- **Token Standard:** ERC-721
- **Proof Chain:** Keccak256(artwork_hash + timestamp + metadata)
- **Governance Weight:** 1 vote per certificate held
- **Special Power:** Can dispute authenticity within 90-day window

---

## 🚦 Testnet Deployment Checklist

See `docs/TESTNET-CHECKLIST.md` for complete validation steps.

**Quick Start:**
```bash
# 1. Deploy contracts
npm run deploy:testnet

# 2. Mint genesis pair
npm run mint:genesis

# 3. Verify metadata
npm run verify:metadata

# 4. Validate dual-asset bond
npm run test:bonding
```

---

## 🔐 Security Considerations

- Smart contracts undergo internal audit before mainnet
- Metadata immutability via IPFS pinning
- Dual-asset bond cannot be broken without explicit transaction
- Certificate holder dispute mechanism protects authenticity

---

## 📞 Questions?

- **Dual-Asset Model:** See `docs/DUAL-ASSET-MODEL.md`
- **Metadata Format:** See `nft-metadata/README.md`
- **Deployment:** See `docs/TESTNET-CHECKLIST.md`
- **Landing Page:** See `docs/landing/index.html`

---

**Launch Status:** 🚀 Ready for testnet validation  
**Last Updated:** September 16, 2026  
**Maintainer:** BIU Studio
