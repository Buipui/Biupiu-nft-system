# BIUPIU CORE GOVERNANCE INDEX — AI-74

AI-74 closes the audited learning -> evidence -> provenance -> trust boundary.

## Status
IMPLEMENTED / STATIC VERIFIED / RUNTIME EVIDENCE PENDING

## Canonical flow
Learning -> Evidence Promotion -> DMS Provenance -> Trust Event -> Merkle Checkpoint -> Optional External Anchor -> Verification -> Regression.

## Federation harvest integration
Reference patterns harvested from NIST TEVV/AI RMF, SLSA provenance and Sigstore/Rekor transparency-log practice are mapped into Biupiu without replacing Biupiu authorities.

## Security boundaries
- Learning may propose and record; it cannot silently promote itself.
- Historical events are append-only.
- Blockchain is an optional anchoring layer, not the learning engine.
- Payloads remain off-chain by default.
- Live transaction/inclusion proof is not claimed.
- Production signing and hardware-rooted trust remain open verification gates.

## Next verification gate
Execute the AI-74 deterministic audit in an approved host/CI environment, then add real signing and external-anchor verification only after the local trust chain passes.
