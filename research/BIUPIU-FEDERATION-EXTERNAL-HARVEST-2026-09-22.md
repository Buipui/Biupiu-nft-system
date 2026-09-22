# Biupiu Federation External Harvest — 2026-09-22

## Purpose
Identify missing federation capabilities and integrate only architecture/contracts that are compatible with Biupiu's fail-closed, provenance-first native architecture.

## Harvested patterns

### OpenUSD
OpenUSD separates core scene foundations, composition, imaging and plugins and exposes explicit extension points such as asset resolution and file-format plugins. This maps to a Biupiu rule: **core contracts stay stable; World/renderer/import/export integrations are adapters**. citeturn0search0turn0search6

### Eclipse Ditto
Ditto provides a stable twin protocol while transport bindings vary, and supports MQTT, AMQP, HTTP, Kafka and WebSocket connectivity. Its protocol also distinguishes persisted twin communication from live device communication. Biupiu therefore needs explicit transport-neutral envelopes, twin/live separation, correlation IDs, payload mapping and delivery policy. citeturn0search9turn0search10turn0search19

### OPC UA PubSub
OPC UA PubSub provides publisher/subscriber data distribution and information-modelled configuration. Biupiu can use this as an industrial adapter pattern for site/DMS federation, without making OPC UA authoritative over the native OS. citeturn1search13turn1search17

### AUTOSAR Adaptive
AUTOSAR's current Adaptive Platform organizes communication, storage, security, safety, diagnostics, cryptography, health management, execution, state management and update/configuration around services/APIs. These are identified as missing/shared concerns for Biupiu federation, but AUTOSAR material is not copied into the codebase; it remains a standards adapter/reference boundary. citeturn1search9turn1search37

### OpenTelemetry
OpenTelemetry supplies cross-language semantic conventions and context propagation for correlated traces/events/metrics/logs. Biupiu federation now adopts the *pattern* of immutable propagated context and common semantic event attributes, without importing an OTel SDK into the core. citeturn1search0turn1search2turn1search3

## Foreign-language/OEM lane
Existing repository research already routes Chinese, Japanese, Korean, German, French, Italian, Spanish, Portuguese and Russian discovery through provenance/licence gates. This pass preserves that architecture: translation is discovery assistance, never evidence or permission.

OEM/industrial candidates are classified as adapter references:
- CAN/CAN-FD
- SOME/IP/service discovery
- AUTOSAR Adaptive service/state/diagnostic patterns
- OPC UA information model/PubSub
- MQTT
- Modbus
- FMI/co-simulation
- DDS/ROS 2
- STEP/AP242/PLM interoperability

No proprietary OEM implementation, firmware, ripped library or restricted specification was copied.

## Missing federation modules now formalised
1. Capability discovery/version negotiation
2. Health/readiness and queue-depth telemetry
3. Trace/correlation context
4. Schema/content-type/hash references
5. Delivery/retry/TTL policy
6. Explicit twin-vs-live boundary
7. Security/authorization boundary
8. Clock-skew/time-quality observation
9. Backpressure/dead-letter handling
10. Adapter lifecycle and graceful close
11. Cross-simulator observation schema
12. Placement/provenance registry

## Native integration
Added:
- `packages/biupiu-rnd-os/src/federation-contracts.ts`
- federation gates F17–F22
- repository placement/consolidation audit
- external harvest registry

## Promotion rule
DISCOVER -> PROVENANCE -> LICENCE/IP -> NORMALISE -> CONTRACT -> STATIC TEST -> BUILD -> SECURITY -> REGRESSION -> RUNTIME -> PROMOTE

External patterns never become authoritative merely because they are popular, OEM-derived, foreign-language, or open-source.
