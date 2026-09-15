# BIUPIU NFT MINTING ARCHITECTURE v2.0

## Complete release lifecycle

`Research → Evidence → Research ID → Computational Model → Algorithm → Stand-alone Image + Provenance Image → Asset Hashes → Metadata → IP/Licence Gate → Contract → Testnet Deployment → Test Mint → Metadata Resolution → Contract Verification → Production Authorisation → Mint → Blockchain Record`

## Contract layer

`contracts/BiupiuNFT.sol` is the current reference ERC-721 contract. It provides capped supply, owner-controlled single/batch minting, immutable token URI assignment at mint, ERC-2981 royalty signalling and mint events.

This is a reference implementation and requires independent testing/security review before production deployment.

## Web3 tooling

Hardhat + ethers.js + OpenZeppelin Contracts are used for the current EVM implementation. Environment variables hold RPC endpoints and local signing credentials.

## Networks

Development/testnet targets:

- Ethereum Sepolia — 11155111
- Polygon Amoy — 80002

The repository does not automatically select a production mainnet. Mainnet/network selection is a release-governance decision.

## Wallet architecture

1. Development/deployer wallet — used only for deployment/testing.
2. Mint/operational wallet — separate from personal accounts where practical.
3. Treasury wallet — separate custody; production should consider multisig.
4. Private keys/seed phrases — never stored in repository files.

## Metadata architecture

Token URI points to frozen metadata. Recommended production arrangement:

`metadata.json → provenance image + stand-alone image + research/provenance references`

Artwork and metadata should be content-addressed/pinned before production minting. The blockchain record then anchors the token to the frozen metadata URI and deployment/mint transaction.

## Two-image standard

Every release contains:

- `01_PROVENANCE` — branded research/provenance presentation.
- `02_STANDALONE` — collector-facing artwork.

Each receives an independent version and SHA-256 hash. Both reference the same NFT ID and Research ID(s).

## IP boundary

The token is not an automatic assignment of Biupiu patents, inventions, trademarks, confidential information, source code, datasets or commercial rights. Rights are defined by the release licence.

## Final mint checklist

- [ ] Research source genealogy frozen
- [ ] Evidence class confirmed
- [ ] Stand-alone artwork approved
- [ ] Provenance artwork approved
- [ ] Both artwork hashes recorded
- [ ] Metadata frozen and hashed
- [ ] Third-party licences cleared
- [ ] IP/patent sensitivity review completed
- [ ] Contract tested
- [ ] Testnet deployment completed
- [ ] Test mint completed
- [ ] Metadata/artwork resolve correctly
- [ ] Contract source verified where supported
- [ ] Contract address/chain ID recorded
- [ ] Wallet/custody record completed securely
- [ ] NFT licence approved
- [ ] Production mint authorised
- [ ] Mint transaction/token ID recorded

**Status:** Web3 development layer added; production mint remains gated.
