# 📋 Quick Start Guide — BIU NFT System

## What You Have Now

✅ **Documentation**
- LAUNCH-PLAN.md — Dual-asset model overview
- TESTNET-CHECKLIST.md — Deployment validation guide
- REPOSITORY-STRUCTURE.md — Folder organization
- nft-metadata/README.md — Metadata standards

✅ **Metadata Files**
- nft-metadata/BIU-ART-0001-A.json — Genesis artwork
- nft-metadata/BIU-COA-0001.json — Genesis certificate

✅ **Public Web**
- docs/landing/index.html — Dual-asset showcase

---

## Next Steps (After Testnet)

### Phase 1: Prepare Your Imagery 🎨
**What to do:**
1. Create your artwork preview image (1200x800px PNG)
   - Save as: `docs/imagery/biu-art-0001-a-preview.png`
   - This displays on marketplace listings

2. Create your certificate preview (1200x800px PNG)
   - Save as: `docs/imagery/biu-coa-0001-preview.png`
   - This displays on marketplace listings

3. Prepare high-resolution files (optional)
   - Artwork: `docs/imagery/biu-art-0001-a-fullres.png`
   - Certificate: `docs/imagery/biu-coa-0001-fullres.pdf`

**Why:** IPFS requires actual image files to pin. Metadata references these hashes.

---

### Phase 2: Pin to IPFS 📌
**What to do:**
1. Create Pinata account (free tier available)
2. Upload all preview images
3. Get IPFS hashes from Pinata
4. Update metadata files with actual hashes:
   ```json
   "image": "ipfs://QmYourActualHash/biu-art-0001-a-preview.png"
   ```

**Why:** Metadata IPFS links must resolve to actual artwork.

---

### Phase 3: Deploy Smart Contracts ⚙️
**What to do:**
1. Set up Hardhat locally
2. Deploy to Ethereum Sepolia testnet
3. Save contract addresses in `deploy/testnet-addresses.json`
4. Record transaction hashes

**Commands (future):**
```bash
npm install
npx hardhat compile
npm test
npm run deploy:testnet
```

---

### Phase 4: Mint Genesis NFT 🎁
**What to do:**
1. Mint BIU-ART-0001-A on testnet
2. Mint BIU-COA-0001 on testnet
3. Bond them together
4. Test transfer and burn mechanics

**Expected outcome:** Both NFTs live on Sepolia, visible on Etherscan

---

### Phase 5: Validate & Review ✅
**What to do:**
1. Go through TESTNET-CHECKLIST.md
2. Check all boxes
3. Get security review
4. Document any issues

**Expected outcome:** Ready for mainnet

---

## Important Files to Know

| File | Use When |
|------|----------|
| LAUNCH-PLAN.md | Need to explain your model |
| REPOSITORY-STRUCTURE.md | Need to organize your files |
| TESTNET-CHECKLIST.md | About to deploy to testnet |
| nft-metadata/README.md | Creating new metadata files |
| MASTER-TEMPLATE.md | Documenting an artwork |
| docs/landing/index.html | Showcasing your model |

---

## Common Questions

**Q: Where do I put my artwork files?**  
A: `artworks/genesis/` for documentation, `docs/imagery/` for previews

**Q: How do I version my metadata?**  
A: Never edit released metadata. Create new files with version in filename.

**Q: Can I change my smart contract after minting?**  
A: No, deployed contracts are immutable. Deploy new version if needed.

**Q: Where's the smart contract code?**  
A: Check `contracts/` folder (to be populated in Step 5)

**Q: How do I test locally?**  
A: Use Hardhat. See `deploy-nft.js` and test files.

---

## Repository Status Dashboard

| Component | Status | Ready for Testnet? |
|-----------|--------|--------------------|
| Documentation | ✅ Complete | YES |
| Metadata Files | ✅ Complete | YES |
| Landing Page | ✅ Complete | YES |
| Smart Contracts | ⏳ Next step | NO |
| Test Suite | ⏳ Next step | NO |
| Deployment Scripts | ⏳ Next step | NO |
| Imagery | ⏳ Your action | NO |

---

**Next: Step 5 — Smart Contracts Setup**  
When ready, we'll set up the Solidity contracts and tests.

---

**Last Updated:** September 16, 2026  
**Maintainer:** BIU Studio
