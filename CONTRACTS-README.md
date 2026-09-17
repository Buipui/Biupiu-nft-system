# Smart Contract Documentation

## Contracts

### `contracts/BiupiuNFT.sol`

Reference ERC-721 contract for controlled NFT minting. It provides capped supply, owner-controlled single and batch minting, token URI storage, and ERC-2981 royalty signalling.

### `contracts/BiupiuCertificate.sol`

Experimental certificate NFT design. It is intended to provide certificate minting, artwork bonding, certificate burning, governance-vote events, and royalties.

### `contracts/BiupiuProvenanceRegistry.sol`

Experimental dual-asset registry. It records artwork/certificate bond commitments, research and algorithm identifiers, metadata hashes, and bond verification results.

### `contracts/BiupiuResearchRegistry.sol`

Research-release registry that anchors approved release commitments and can link a release to an NFT contract and token ID.

## Before deployment

These contracts must be treated as prototypes until all of the following are complete:

- [ ] Solidity compilation succeeds with the repository's installed OpenZeppelin version.
- [ ] Unit tests cover access control, supply limits, URI handling, royalties, bonding, burning, and registry records.
- [ ] The certificate contract's ownership/approval and burn behavior is tested against the exact OpenZeppelin version.
- [ ] Events and error behavior are tested.
- [ ] Testnet deployment succeeds.
- [ ] Source code is verified on the block explorer.
- [ ] An independent security review is completed before mainnet use.

## Design boundary

The contracts store ownership and cryptographic commitments. They do not automatically transfer underlying research, patents, copyright, confidential information, or commercial rights.

## Suggested testing order

1. Compile.
2. Run existing tests.
3. Add certificate tests.
4. Add dual-asset registry tests.
5. Deploy locally.
6. Deploy to Sepolia.
7. Record addresses and transaction hashes under `deploy/`.
