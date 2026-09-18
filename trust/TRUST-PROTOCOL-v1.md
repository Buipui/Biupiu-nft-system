# BIUPIU TRUST PROTOCOL v1

## Canonical record
Each durable object receives a stable ID, schema version, timestamp, issuer, payload hash and previous-event reference where applicable.

## Canonicalization
Structured data is serialized deterministically using UTF-8, stable field ordering, explicit null handling and no insignificant whitespace.

## Integrity hash
Default proposal: SHA-256 over the canonical bytes.

record_hash = SHA256(canonical_record)

## Event chaining
Each audit event references the previous event hash.

event_hash = SHA256(canonical_event || previous_event_hash)

## Authorization
Writes require an authenticated principal and authorization decision. The trust layer records decision metadata but never passwords or private keys.

## Signatures
A production implementation will use a versioned digital-signature scheme tied to public key identifiers.

## Blockchain anchoring
An anchor records the trust-stream checkpoint/root, network identifier, transaction reference and timestamp. Payloads remain off-chain by default.

## Verification
Recompute canonical data and hashes, check event links, validate signatures where present, and optionally verify the external blockchain transaction.
