# BIUPIU TRUST ALGORITHM v1

**Status:** Specification / prototype target

1. Receive a typed record.
2. Validate required fields against its schema.
3. Canonicalize the record.
4. Compute payload_hash = SHA-256(canonical_record).
5. Build an audit event containing record ID, operation, actor ID, payload hash, previous event hash and protocol version.
6. Canonicalize the event.
7. Compute event_hash from the canonical event plus previous_event_hash.
8. Optionally sign the event hash; store the signature and public key identifier, never the private key.
9. Append the event to the local trust ledger.
10. Periodically calculate a checkpoint/root.
11. Optionally publish the checkpoint to an external blockchain.
12. Verification repeats the deterministic process and compares references.

## Future algorithm work
- Merkle checkpoints
- Signature-suite abstraction
- Replay protection and sequence numbers
- Key rotation/revocation
- Multi-party approvals
- External-chain adapters
- Biupiu-native consensus research
