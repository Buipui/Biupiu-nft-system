# Biupiu MQTT Adapter Gate v1.0

**Status:** Repository implementation complete; live broker execution pending.

The adapter maps MQTT transport onto the canonical Machine Capability contract.

Controls:
- explicit broker/port and topic mapping;
- missing paho-mqtt dependency fails closed;
- disconnected commands fail closed;
- READ_ONLY capabilities cannot publish actuation;
- no topic inference;
- live broker evidence remains distinct from simulation.

Live evidence must record broker identity, authentication/TLS configuration, topic mapping, QoS, timestamps, payload schema, connection/retry behaviour and reproducible test conditions.

No physical MQTT broker or machine was connected during this repository execution.
