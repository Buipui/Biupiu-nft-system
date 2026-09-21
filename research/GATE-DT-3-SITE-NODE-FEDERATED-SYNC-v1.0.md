# Gate DT-3 — Controlled Site Node Federated Synchronization

## Executed scope
Added a repository-level Site Node synchronization adapter on top of the Digital Twin federation contract.

### Implemented
- Site Node queue boundary.
- Queue -> send -> acknowledgement transition.
- Retryable failure preservation and later replay.
- Conflict state preservation.
- Reuse of the same deterministic Digital Twin event identity across Site Node and federation layers.
- Transport remains injected through a sender interface, so HTTPS, IPC, CAN/CAN-FD gateways or device-specific transports can be added without changing the Twin contract.

## Federation coverage
The same Site Node contract can represent Android, Linux, Windows, Raspberry Pi, Arduino, JVM, server and connected-device nodes. Platform support is a contract property; it is not a claim that every platform has been physically connected.

## Verification boundary
- Source implementation: IMPLEMENTED
- Site Node contract tests: REGISTERED
- Live DMS endpoint: OPEN
- Durable persistent queue: OPEN
- Authenticated transport execution: OPEN
- Physical device synchronization: OPEN
- HIL/production actuation: OPEN
- GitHub Actions execution: PENDING because no workflow run/status is currently exposed for the new commits
