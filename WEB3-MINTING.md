# BIUPIU Web3 Minting Layer v1.0

The repository now contains the minimum EVM development stack needed to compile, deploy and mint the reference Biupiu NFT contract.

## Components

- `contracts/BiupiuNFT.sol` — ERC-721 contract with capped supply, owner-controlled minting, batch minting, token URI storage and ERC-2981 royalty signalling.
- `hardhat.config.js` — Solidity/network configuration.
- `package.json` — Node/Hardhat/ethers/OpenZeppelin dependencies and commands.
- `.env.example` — local secret/configuration template.
- `deploy-nft.js` — deployment script.
- `mint-nft.js` — mint script.

## Test networks

- Ethereum Sepolia: chain ID 11155111.
- Polygon Amoy: chain ID 80002.

## Local setup

```text
cp .env.example .env
npm install
npm run compile
```

Configure an RPC endpoint and a dedicated testnet deployer private key in the local `.env`. Never commit `.env`, a private key or a seed phrase.

## Deploy

```text
npm run deploy:sepolia
```

or

```text
npm run deploy:amoy
```

Record the contract address, chain ID and deployment transaction in the relevant NFT provenance record.

## Mint

Set `NFT_CONTRACT_ADDRESS`, `RECIPIENT` and `TOKEN_URI` in local `.env`, then run the network-specific mint command.

The token URI should resolve to frozen, content-addressed metadata containing the NFT ID, Research ID(s), evidence class, artwork/provenance references, algorithm/version and licence.

## Production gate

The presence of deployment code does not authorise a public mint. Final artwork, paired provenance/stand-alone assets, hashes, metadata, licence, IP review, contract tests, testnet mint and source verification must be completed first.

## Security

Use a dedicated deployment wallet. Keep treasury custody separate. Consider multisig for production treasury/control functions. Do not place secrets in GitHub.

Royalty signalling through ERC-2981 is a standard interface; marketplace enforcement may vary.
