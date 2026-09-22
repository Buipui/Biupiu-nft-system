# Biupiu Federation Module Architecture v1.0

FEDERATION CORE
-> IDENTITY / CAPABILITY DISCOVERY
-> AUTHENTICATION / AUTHORIZATION
-> SCHEMA + VERSION NEGOTIATION
-> TIME / CLOCK QUALITY
-> TRACE + CORRELATION
-> TRANSPORT ADAPTER
-> DELIVERY / RETRY / BACKPRESSURE
-> REPLAY / DEDUP / CONFLICT
-> HEALTH / READINESS
-> DIGITAL TWIN
-> SIMULATOR OBSERVATION
-> LEARNING EVENT
-> VALIDATION / REGRESSION
-> POLICY / HUMAN GATE
-> VERSIONED PROMOTION

## Authority boundary
OBSERVE != SIMULATE != PROPOSE != COMMIT.

External protocol adapters can transport data; they cannot acquire native authority.

## Transport adapters
MQTT, OPC UA PubSub, HTTP/WebSocket, Kafka, AMQP, DDS/ROS 2, Modbus and automotive/service-oriented transports are adapters. Each adapter must implement the common federation contract.

## Reliability
Every event needs deterministic identity, correlation context, schema reference, provenance, delivery policy and terminal handling.

## Runtime state
The federation registry tracks:
- capability
- protocol version
- health
- queue depth
- clock skew
- delivery state
- conflict/dead-letter state

## Learning boundary
Federation observations become learning evidence only after schema/provenance/replay/numerical sanity checks. Learning may propose bounded adaptations; it cannot rewrite authoritative source.

## World boundary
Biupiu World is a consumer/visualisation/runtime adapter. It does not become the authority for simulator or OS state.
