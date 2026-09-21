# Biupiu Local Execution Gates v1.0

## Gate states

- **VERIFIED** — executable evidence exists.
- **IMPLEMENTED** — code/configuration exists but runtime evidence is incomplete.
- **BLOCKED** — execution environment/tool access prevented verification.
- **FAILED** — execution occurred and produced a failing result.
- **QUARANTINED** — candidate module isolated pending review.
- **GATED** — deliberately prevented from production execution.

## Gates

### Host/runtime
LEX-00 Repository identity
LEX-01 Host inventory
LEX-02 Linux kernel/userspace
LEX-03 C/C++ toolchain
LEX-04 Python runtime
LEX-05 Node/npm runtime

### Blockchain
LEX-06 Hardhat load
LEX-07 local EVM
LEX-08 Ganache compatibility
LEX-09 Solidity compilation
LEX-10 contract tests
LEX-11 Research Registry
LEX-12 NFT deployment/mint
LEX-13 event/read-back
LEX-14 provenance/hash linkage
LEX-15 failure/revert tests
LEX-16 deterministic replay

### OS/federation
LEX-17 OS integration
LEX-18 hardware abstraction
LEX-19 IPC/event bus
LEX-20 federation discovery
LEX-21 module sandbox
LEX-22 security controls
LEX-23 supply-chain/SBOM
LEX-24 learning/failure records
LEX-25 regression

### Release
LEX-26 full-system integration
LEX-27 reproducible local build
LEX-28 verification manifest
LEX-29 production lock

## Current repository evidence

The repository currently declares Hardhat, ethers.js, OpenZeppelin Contracts and dotenv as dependencies and already contains local deployment scripts and numerous CI/runtime workflows.

**Important:** repository configuration is not runtime proof. Gates remain IMPLEMENTED/BLOCKED until execution evidence is available.

## Production lock

Mainnet, production payment, production identity and unrestricted module execution remain explicitly gated.
