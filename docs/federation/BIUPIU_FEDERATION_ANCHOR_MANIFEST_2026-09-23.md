# BIUPIU FEDERATION ANCHOR MANIFEST — 2026-09-23

## Anchor purpose
Content-addressable manifest for the federated compatibility-learning record. This manifest is designed to be anchored to an authorized blockchain transaction later.

## Repository records
- UE 5.8.3 harvest: docs/unreal/BIUPIU_UE_5.8.3_FEDERATION_HARVEST_2026-09-23.md
- Compatibility learning record: docs/federation/BIUPIU_FEDERATED_COMPATIBILITY_LEARNING_2026-09-23.md
- Repository: Buipui/Biupiu-nft-system
- Branch: main
- UE harvest commit: a7b11db1d426b03cbfd5c59c243575421e340635
- Learning-record commit: 4b8c3900f6398f6e72ad4454d8330215d79e0ec2

## Anchor payload
The intended blockchain payload is a cryptographic digest of the canonical learning record plus its source/provenance manifest. The transaction itself is NOT claimed as completed here.

## Integrity rules
- Store immutable digest + repository commit + retrieval date.
- Keep source URLs/licences separate from Biupiu-owned IP.
- Never place confidential invention details or private credentials on-chain.
- Blockchain status values: PREPARED -> SUBMITTED -> CONFIRMED.
- Current status: PREPARED ONLY.

## Verification
An authorized anchoring service/wallet must independently calculate the digest from the canonical repository files before submitting any transaction. The resulting transaction ID and network must be recorded only after independent confirmation.
