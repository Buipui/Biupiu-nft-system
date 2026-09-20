# Biupiu OPC UA Adapter Gate v1.0

**Status:** Repository implementation complete; live OPC UA execution pending.

The adapter maps the canonical Machine Capability contract onto an OPC UA endpoint.

## Controls
- Physical connection is explicit and opt-in.
- Missing asyncua dependency fails closed.
- Disconnected reads/writes fail closed.
- READ_ONLY capabilities cannot actuate.
- Node IDs require an explicit mapping and are never inferred.
- Physical readings are not labelled as simulated evidence.

## Live evidence required
Endpoint identity, server/application identity, security mode, node mapping, timestamps, returned values, quality/status, errors and reproducible test conditions.

No physical OPC UA server was available during this repository execution, so no live connection or hardware result is claimed.
