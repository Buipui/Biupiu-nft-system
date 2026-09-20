# Biupiu Cannabis/Hemp Smart-Farming Open-Resource Adapter Protocol v1.0

**Purpose:** Connect harvested open-source agricultural resources to Biupiu Smart Farming without copying third-party repositories into the core product.

## Adapter layers
1. PERCEPTION — camera/RGB-D/LiDAR/thermal/multispectral inputs.
2. LOCALISATION — GNSS/IMU/SLAM/row-map interfaces.
3. EDGE — Raspberry Pi/Jetson/ESP32 processing and sensor gateways.
4. CONTROL — abstract actuator/control interfaces; safety-critical actuation remains independently validated.
5. DATA — timestamps, provenance, calibration, quality flags and telemetry.
6. INTELLIGENCE — Biupiu AI/ML decision-support interface.
7. DMS — farm/site/equipment/task/maintenance records.
8. DIGITAL TWIN — geometry, field map, plant observations and machine state.

## Priority adapters
### SF-ADP-01 — OpenWeedLocator
Licence: MIT. Use: perception/edge-node reference. Promotion: implementation-candidate. Required checks: dependency scan, Python compatibility, hardware abstraction, false-positive/false-negative testing and fail-safe relay behaviour.

### SF-ADP-02 — Open-PhenoLiDAR
Licence: MIT. Use: LiDAR/GNSS/IMU phenotyping and mapping reference. Promotion: implementation-candidate. Required checks: ROS version compatibility, sensor-driver compatibility, Docker reproducibility, coordinate-frame validation, timestamp integrity and field-test comparison.

### FL-ADP-DE-01 — cannaUNITY
Licence: MIT; archived. Use: German-language architecture reference for traceability, grow-control, access-control and DMS concepts. Promotion: research-only until codebase health and jurisdictional applicability are established.

### FL-ADP-ZH-01 — WeedBuster
Licence: MIT. Use: Chinese-language edge-AI/ROS2 perception architecture reference. Promotion: research-only; no safety-critical actuation code promoted by this checkpoint.

## Software-sharing rule
**Share concepts/interfaces first. Share executable code only after licence + security + dependency + compatibility + test approval.**

This preserves Biupiu's proprietary intelligence layer while allowing lawful reuse of compatible open-source components.

## Status
REGISTERED: adapter contract  
IMPLEMENTATION-CANDIDATES: SF-ADP-01, SF-ADP-02  
FOREIGN-LANGUAGE CANDIDATES: FL-ADP-DE-01, FL-ADP-ZH-01  
PRODUCTION INTEGRATION: NOT VERIFIED  
HARDWARE-IN-LOOP: PENDING