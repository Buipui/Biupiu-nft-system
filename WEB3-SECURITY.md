# BIUPIU Web3 Security Rules

1. Never commit private keys, seed phrases, wallet backups or `.env` files.
2. `.env.example` contains placeholders only.
3. Use a dedicated testnet deployment wallet.
4. Keep production treasury custody separate from deployment operations.
5. Consider multisig custody for production treasury/admin control.
6. Never paste a private key into chat or repository files.
7. Test contracts on a local chain and testnet before production.
8. Verify deployed contract source where the target explorer supports it.
9. Freeze and hash NFT metadata/assets before production minting.
10. Treat ERC-2981 as royalty signalling, not guaranteed marketplace enforcement.
11. Record contract address, chain ID, deployment transaction and mint transaction in provenance records after deployment.
12. A deployed contract does not itself establish ownership or licensing of underlying Biupiu IP.
