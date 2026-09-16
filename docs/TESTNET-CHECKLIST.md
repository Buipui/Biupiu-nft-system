# 🚀 BIU NFT Testnet Deployment Checklist

## Pre-Deployment Validation

Complete this checklist before deploying to Ethereum Sepolia (Testnet).

---

## Phase 1: Contract Preparation

### Smart Contracts
- [ ] `BIUArtwork.sol` compiles without errors
- [ ] `BIUCertificate.sol` compiles without errors
- [ ] `BIUProvenanceRegistry.sol` compiles without errors
- [ ] All contracts follow ERC-721 standard
- [ ] Dual-asset bonding logic implemented
- [ ] Metadata URI resolution working
- [ ] Royalty enforcement enabled (10%)

### Contract Functions
- [ ] `mint()` - Creates new artwork tokens
- [ ] `mintCertificate()` - Creates paired certificates
- [ ] `bondAssets()` - Establishes dual-asset link
- [ ] `transferWithCertificate()` - Moves both assets together
- [ ] `burn()` - Certificate burn mechanism
- [ ] `verify()` - Authenticity proof validation

---

## Phase 2: Metadata Validation

### File Structure
- [ ] `/nft-metadata/BIU-ART-0001-A.json` exists
- [ ] `/nft-metadata/BIU-COA-0001.json` exists
- [ ] Both files are valid JSON (no syntax errors)
- [ ] `/nft-metadata/README.md` documents standards

### BIU-ART-0001-A.json
- [ ] `name` field present (max 100 chars)
- [ ] `description` includes dual-asset reference
- [ ] `image` IPFS URL is resolvable
- [ ] `external_url` points to correct artist page
- [ ] `attributes` array complete with 8+ traits
- [ ] `dual_asset.paired_token` = "BIU-COA-0001"
- [ ] `dual_asset.bond_status` = "Active"
- [ ] `provenance.contract` = "BIUArtwork.sol"
- [ ] `provenance.chain_id` = 11155111 (Sepolia)

### BIU-COA-0001.json
- [ ] `name` field present
- [ ] `description` includes dual-asset reference
- [ ] `image` IPFS URL is resolvable
- [ ] `external_url` points to verification page
- [ ] `attributes` array complete with 8+ traits
- [ ] `dual_asset.paired_token` = "BIU-ART-0001-A"
- [ ] `certificate.proof_hash` is valid Keccak256 format
- [ ] `governance.voting_enabled` = true
- [ ] `governance.voting_weight` = 1
- [ ] `provenance.contract` = "BIUCertificate.sol"

### IPFS Resources
- [ ] Preview images pinned to IPFS (Pinata)
- [ ] Full resolution files backed up on IPFS
- [ ] IPFS hashes documented in metadata
- [ ] Gateway URLs tested and resolving
- [ ] Backup pinning configured

---

## Phase 3: IPFS & Hosting

### IPFS Pinning
- [ ] Account created on Pinata.cloud
- [ ] API keys configured
- [ ] `biu-art-0001-a-preview.png` pinned (IPFS hash: QmPlaceholder)
- [ ] `biu-coa-0001-preview.png` pinned (IPFS hash: QmPlaceholder)
- [ ] Full resolution files pinned
- [ ] Pin retention: 1 year minimum

### Public Gateway Testing
```bash
# Test artwork preview
curl https://gateway.pinata.cloud/ipfs/QmPlaceholder/biu-art-0001-a-preview.png

# Test certificate preview
curl https://gateway.pinata.cloud/ipfs/QmPlaceholder/biu-coa-0001-preview.png
```
- [ ] All IPFS links return 200 status
- [ ] Images load correctly in browser
- [ ] No CORS errors

---

## Phase 4: Local Testing

### Unit Tests
```bash
npm test
```
- [ ] All tests passing (>90% coverage)
- [ ] `testMintArtwork()` - Artwork creation works
- [ ] `testMintCertificate()` - Certificate creation works
- [ ] `testBondAssets()` - Dual-asset bonding works
- [ ] `testMetadataResolution()` - URI resolution correct
- [ ] `testTransferWithCertificate()` - Combined transfer works
- [ ] `testBurnCertificate()` - Certificate burn works
- [ ] `testGovernanceVoting()` - Certificate voting enabled

### Gas Estimation
- [ ] `mint()` gas cost < 200,000 (reasonable)
- [ ] `bondAssets()` gas cost < 150,000 (reasonable)
- [ ] `transferWithCertificate()` gas cost < 250,000 (reasonable)

---

## Phase 5: Testnet Deployment

### Environment Setup
```bash
# Configure testnet variables
export TESTNET_RPC_URL="https://sepolia.infura.io/v3/YOUR_KEY"
export PRIVATE_KEY="0x..."
export ETHERSCAN_API_KEY="..."
```
- [ ] RPC endpoint configured (Sepolia)
- [ ] Private key secured (never commit)
- [ ] Etherscan API key configured
- [ ] Sufficient testnet ETH in deployer account (>1 ETH)

### Smart Contract Deployment
```bash
npm run deploy:testnet
```
- [ ] BIUArtwork.sol deployed successfully
  - Address: `0x...` (save this)
  - Tx Hash: `0x...`
  - Verified on Etherscan

- [ ] BIUCertificate.sol deployed successfully
  - Address: `0x...` (save this)
  - Tx Hash: `0x...`
  - Verified on Etherscan

- [ ] BIUProvenanceRegistry.sol deployed successfully
  - Address: `0x...` (save this)
  - Tx Hash: `0x...`
  - Verified on Etherscan

### Contract Verification
```bash
npm run verify:contracts
```
- [ ] All contracts verified on Etherscan
- [ ] Source code matches deployed bytecode
- [ ] ABI readable on Etherscan
- [ ] Constructor arguments logged

---

## Phase 6: Genesis Mint

### Mint Artwork
```bash
npm run mint:artwork BIU-ART-0001-A ipfs://QmPlaceholder/biu-art-0001-a-preview.png
```
- [ ] BIU-ART-0001-A minted successfully
  - Token ID: 1
  - Owner: (your address)
  - Tx Hash: `0x...`
  - Metadata URI resolves correctly

### Mint Certificate
```bash
npm run mint:certificate BIU-COA-0001 1 ipfs://QmPlaceholder/biu-coa-0001-preview.png
```
- [ ] BIU-COA-0001 minted successfully
  - Token ID: 1
  - Owner: (your address)
  - Tx Hash: `0x...`
  - Metadata URI resolves correctly

### Validate Bond
```bash
npm run test:bonding
```
- [ ] Dual-asset bond established
- [ ] Both tokens linked in registry
- [ ] Proof hash matches
- [ ] Bond status: "Active"

---

## Phase 7: Metadata Validation

### On-Chain Verification
```bash
npm run verify:metadata
```
- [ ] `tokenURI(1)` for BIU-ART-0001-A returns correct metadata
- [ ] `tokenURI(1)` for BIU-COA-0001 returns correct metadata
- [ ] Metadata JSON is properly formatted
- [ ] IPFS image links resolve
- [ ] All attributes present and valid

### OpenSea Integration
- [ ] Metadata visible on OpenSea testnet
- [ ] Image displays correctly
- [ ] Attributes show on marketplace
- [ ] Dual-asset relationship visible
- [ ] No collection warnings

---

## Phase 8: Functionality Testing

### Transfer Tests
```bash
npm run test:transfer
```
- [ ] Artwork can be transferred to new address
- [ ] Certificate follows artwork transfer (if enabled)
- [ ] Both assets show new owner on Etherscan
- [ ] Metadata accessible from new owner address

### Governance Tests
```bash
npm run test:governance
```
- [ ] Certificate holder can initiate vote
- [ ] Voting weight = 1 per certificate
- [ ] Votes tallied correctly
- [ ] Vote results stored on-chain

### Burn Tests
```bash
npm run test:burn
```
- [ ] Certificate can be burned
- [ ] Burn transaction successful
- [ ] Token no longer in circulation
- [ ] Burn is irreversible
- [ ] Artwork authenticity status updated

---

## Phase 9: Security Review

### Smart Contract Audit
- [ ] Internal security review completed
- [ ] No obvious vulnerabilities found
- [ ] Reentrancy guards in place
- [ ] Overflow/underflow protections active
- [ ] Access controls implemented
- [ ] Event logging complete

### Best Practices
- [ ] Use of OpenZeppelin contracts
- [ ] No hardcoded addresses
- [ ] Proper error handling
- [ ] Gas optimizations applied
- [ ] Comments document logic

---

## Phase 10: Documentation

### Repository
- [ ] `LAUNCH-PLAN.md` complete and accurate
- [ ] `README.md` updated with testnet addresses
- [ ] `nft-metadata/README.md` documents standards
- [ ] `.env.example` provided (no real keys)
- [ ] Deployment instructions clear

### Technical Docs
- [ ] Smart contract source code commented
- [ ] Function signatures documented
- [ ] State variables explained
- [ ] Event logs documented

---

## Phase 11: Production Readiness

### Final Checklist
- [ ] All testnet tests passing
- [ ] Metadata complete and immutable
- [ ] IPFS backups configured
- [ ] Contract addresses documented
- [ ] Security review approved
- [ ] Launch plan finalized

### Mainnet Preparation
- [ ] Mainnet RPC configured (different from testnet)
- [ ] Private key secured in hardware wallet
- [ ] Gas estimates calculated for mainnet
- [ ] Sufficient ETH for deployment + gas
- [ ] Backup plan documented

---

## Deployment Commands

### Quick Start Testnet Deployment
```bash
# 1. Install dependencies
npm install

# 2. Compile contracts
npx hardhat compile

# 3. Run tests
npm test

# 4. Deploy to Sepolia
npm run deploy:testnet

# 5. Mint genesis pair
npm run mint:genesis

# 6. Verify everything
npm run verify:metadata
```

### Testnet Network Details
- **Network:** Ethereum Sepolia
- **Chain ID:** 11155111
- **RPC:** https://sepolia.infura.io/v3/YOUR_KEY
- **Block Explorer:** https://sepolia.etherscan.io
- **Faucet:** https://sepoliafaucet.com

---

## Troubleshooting

### IPFS Issues
- **Images not loading:** Check Pinata pin status, re-pin if needed
- **Timeout errors:** Use different IPFS gateway
- **404 errors:** Verify hash in metadata matches pinned file

### Smart Contract Issues
- **Compilation fails:** Update Solidity version to 0.8.20+
- **Deployment gas too high:** Optimize contract code
- **Verification fails:** Ensure constructor args match deployment

### Metadata Issues
- **URI returns 404:** Verify metadata file location
- **JSON invalid:** Use online validator (jsonschemavalidator.net)
- **Attributes wrong:** Cross-reference metadata standards document

---

## Sign-Off

**Testnet Deployment By:** ________________  
**Date:** ________________  
**Approved By:** ________________  
**Ready for Mainnet:** ☐ YES ☐ NO

---

**Last Updated:** September 16, 2026  
**Maintainer:** BIU Studio
