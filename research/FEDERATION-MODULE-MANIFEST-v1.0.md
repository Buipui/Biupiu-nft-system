# Biupiu Federation Module Manifest v1.0

**Status:** INTEGRATION BASELINE — candidate modules remain quarantined until runtime verification.
**Repository:** Buipui/Biupiu-nft-system
**Principle:** discover -> isolate -> licence/security review -> build -> test -> integrate -> regression -> verify.

## Accepted core modules already present

| Module | Function | Current integration | Verification |
|---|---|---|---|
| Hardhat | Local EVM / Solidity build & test | package.json + hardhat.config.js | Runtime pending |
| ethers.js | EVM client/deployment interaction | package.json | Runtime pending |
| OpenZeppelin Contracts | ERC-721 / ownership / royalty primitives | contracts/ | Runtime pending |
| dotenv | local configuration boundary | hardhat.config.js | Runtime pending |
| Linux/C++ CI layer | OS/runtime validation | .github/workflows | CI evidence required |
| Python | research/algorithm layer | repository research/release paths | Runtime pending |

## Federation candidates

| Candidate | Intended role | Decision |
|---|---|---|
| Foundry/Anvil | independent EVM cross-validation | QUARANTINED |
| Sigstore/Cosign | artifact signing/provenance | QUARANTINED |
| OSV tooling | dependency vulnerability intelligence | QUARANTINED |
| seccomp/namespaces/cgroups | module sandboxing | QUARANTINED |
| eBPF/LSM | runtime observability/security | QUARANTINED |
| Boost/Asio | C++ systems/network layer | QUARANTINED |
| ROS 2/Gazebo | robotics/simulation interfaces | QUARANTINED |

No candidate is treated as trusted merely because it was discovered.

## Integration boundary

`Biupiu Intelligence -> Federation Registry -> Quarantine -> Module Adapter -> Test Harness -> Biupiu OS/API -> Regression -> Approved Module`

External source code must remain attributable to its source, version, commit/hash and licence.

## Security rules

1. Never execute harvested code with production credentials.
2. Never copy private keys into CI or module sandboxes.
3. No module receives unrestricted host/network access by default.
4. Dependencies are pinned before production use.
5. Licence/IP status is recorded independently of technical compatibility.
6. A passing build is not equivalent to security approval.
7. Failed modules remain quarantined with evidence.
8. Historical manifests are immutable; new harvests create new manifest versions.

## Current integration conclusion

The repository already contains the primary blockchain modules required for the local execution path. The federation layer therefore adds **discovery, quarantine and independent validation**, rather than duplicating the existing EVM stack.


## OpenDroid deep harvest — 2026-09-22

OpenDroid is registered as an external Android-agent family rather than a standalone UI engine.

| Candidate | Intended role | Decision |
|---|---|---|
| OpenDroid Android agent | accessibility/actions/agent/LLM/memory/security/service/voice | QUARANTINED / ADAPTER_ONLY |
| OpenDroid Compose UI | presentation surface reference | QUARANTINED / ADAPTER_ONLY |
| OpenDroid Room/DataStore | persistence reference | QUARANTINED / ADAPTER_ONLY |
| OpenDroid Hilt | dependency-injection reference | QUARANTINED / ADAPTER_ONLY |
| `opendroid.ui-engine` | legacy ambiguous identity | BLOCKED / UNRESOLVED |

Canonical harvest: `research/BIUPIU-OPENDROID-DEEP-EXTERNAL-FEDERATION-HARVEST-20260922.md`.

