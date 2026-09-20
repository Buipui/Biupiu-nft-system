# BIUPIU CANNABIS & HEMP SMART-AGRICULTURE RESEARCH HARVEST v1.0

**Date:** 20 September 2026  
**Harvest ID:** BPU-RES-SF-CANNHEMP-2026-09-20  
**Status:** HARVESTED / CROSS-LINKED / LICENCE-SCREENED / INTEGRATION-CANDIDATES ISOLATED

## 1. Harvest objective
Extend the existing Biupiu Smart Farming + Intelligence + DMS research stack for regulated hemp and cannabis cultivation, while preserving the established rule:

DISCOVER -> SOURCE-VERIFY -> LICENCE -> SECURITY -> DEPENDENCY -> COMPATIBILITY -> TEST -> INTEGRATE -> PROVENANCE

Third-party repositories are not treated as Biupiu-owned code merely because they are indexed. Production integration requires an independent compatibility/security/runtime checkpoint.

## 2. ResearchGate cross-link

### RG-SF-01 — Visual Feedback System Supporting Robotic Manipulation of Hemp Plants
ResearchGate / Journal of Natural Fibers (2025), DOI 10.1080/15440478.2025.2454261. Relevance: RGB-D perception, robotic manipulation, hemp-plant detection and grasping, indoor/outdoor annotated datasets. Route: ROBOTICS -> COMPUTER VISION -> DIGITAL TWIN -> HEMP -> EDGE AI. Status: RESEARCH-REFERENCE / IMPLEMENTATION-INSPIRATION; source-code licence not established from the paper record.

### RG-SF-02 — Automated IoT-Based Monitoring of Industrial Hemp in Greenhouses Using Open-Source Systems and Computer Vision
ResearchGate / AgriEngineering (2025), CC BY 4.0 publication record. Relevance: single-board computer, temperature/humidity sensors, cameras, image analysis and deep-learning growth monitoring for industrial hemp. Route: SMART-FARMING -> IOT -> COMPUTER VISION -> PLANT PHENOTYPING. Status: VALIDATED-REFERENCE / OPEN-LITERATURE.

### RG-SF-03 — SmartGrow DataControl
ResearchGate, Cannabis sativa indoor-cultivation IoT architecture. Relevance: MVC/layered software, environmental sensing, cloud/data integration and cultivation control architecture. Route: FARM-OS -> IOT -> SOFTWARE -> INTELLIGENCE -> DMS. Status: RESEARCH-REFERENCE; implementation licence must be independently checked before code reuse.

### RG-SF-04 — UAV multisensor industrial-cannabis monitoring
ResearchGate / Data in Brief (2026), DOI 10.1016/j.dib.2026.112463, CC BY-NC 4.0. Relevance: RGB, multispectral, thermal, optional hyperspectral/LiDAR, field phenotyping, stress detection and compliance-oriented monitoring. Route: UAV -> PHENOTYPING -> COMPLIANCE-DATA -> AI -> DIGITAL-TWIN. Status: RESEARCH-REFERENCE; NC licence means not a direct commercial-code/data integration licence.

## 3. Emerald Insight cross-link

### EM-SF-01 — AGRI-FOOD 4.0 resource family
Emerald resource record identifies chapters on IoT in the agroecosystem, smart irrigation using IoT, AI-based agritech transformation, robotics and automation for Agri-Food 4.0, drone-based crop-quality monitoring, and Industry 4.0 supply-chain KPIs. Route: IOT -> IRRIGATION -> AI -> ROBOTICS -> DATA/KPI -> DMS. Status: SCHOLARLY-REFERENCE / PRINCIPLE-EXTRACTION. Copyrighted chapters remain citation/reference material unless an explicit reuse licence permits otherwise.

## 4. Open-book cross-link

### OTB-SF-01 — Introduction to Biosystems Engineering
Open Textbook Library. Topics directly relevant to Biupiu include sensors/control, microcontrollers, data processing, machinery/mechatronics, controlled-environment production, biomass processing and water systems. Status: OPEN-EDUCATIONAL-REFERENCE.

### OTB-SF-02 — Introduction to Autonomous Robots
Open Textbook Library, CC BY-NC. Covers locomotion, manipulation, kinematics, path planning, sensors, vision, uncertainty, localization, grasping and SLAM. Status: RESEARCH/TRAINING REFERENCE; NC restriction blocks direct commercial redistribution without separate permission.

### OTB-SF-03 — Measurement and Instrumentation
Open Textbook Library, CC BY-NC-SA. Relevant to sensor selection, signal conditioning, sampling, dynamic range, data acquisition and measurement error. Status: RESEARCH/TRAINING REFERENCE; NC-SA restriction prevents treating it as commercial software/code input.

## 5. GitHub open-source isolation

### Priority A — implementation candidates

GH-SF-01 — OpenWeedLocator. Repository: https://github.com/geezacoleman/OpenWeedLocator. Licence: MIT. Architecture: Raspberry Pi + camera + image-based detection + relay/solenoid interface. Potential use: vision-perception adapter, low-cost edge node, camera/relay abstraction and field-test scaffold. Status: IMPLEMENTATION-CANDIDATE / LICENCE-PASS / SECURITY+COMPATIBILITY+TEST PENDING.

GH-SF-02 — Open-PhenoLiDAR. Repository: https://github.com/OpenAgriTech/Open-PhenoLiDAR. Licence: MIT. Architecture: ROS, LiDAR, GNSS/IMU, PX4, HDF5/ROS bags, Python/Plotly-Dash dashboard, Docker and Raspberry Pi/Jetson compatibility. Potential use: plant phenotyping, mapping, digital-twin capture, sensor fusion and robotics telemetry adapter. Status: IMPLEMENTATION-CANDIDATE / LICENCE-PASS / MODERN ROS COMPATIBILITY+TEST PENDING.

### Priority B — foreign-language / architecture candidates

GH-FL-DE-01 — cannaUNITY. Repository: https://github.com/saschadaemgen/cannaUNITY. Language: German/English. Licence: MIT. Repository status: archived. Architecture includes task management, grow controller, access control, monitoring, track-and-trace, MQTT/SIMATIC integration and touch/mobile UI. Potential use: architecture reference for controlled-access, traceability, controller and DMS modules. Status: FOREIGN-LANGUAGE / MIT / ARCHIVED / RESEARCH-ONLY ADAPTER CANDIDATE. Germany-specific legal logic is not to be transplanted into US/Spain operations.

GH-FL-ZH-01 — WeedBuster. Language context: Chinese-language repository documentation. Licence: MIT. Architecture includes stereo/RGB sensing, computer vision, ROS 2, edge inference and closed-loop visual servoing. Potential use: perception/edge-AI architecture study only. Status: FOREIGN-LANGUAGE / MIT / RESEARCH-ONLY / SAFETY-CRITICAL ACTUATION NOT PROMOTED.

GH-SF-03 — SuperGreenOS. Licence: GPL-3.0. Architecture: ESP32, MQTT, sensors, alerts, dashboards and farming automation. Status: LICENCE-ISOLATED. Reuse is subject to GPL obligations and Biupiu closed-source/product architecture; no direct code import approved in this harvest.

## 6. Foreign-language protocol execution

Native terminology routes were executed for German, Italian, Japanese, Chinese, Korean and Spanish research discovery.

Required rule: preserve original-language title/terms; map native terminology to English concepts; retain source identity; translate only for understanding; never treat translation as validation; route code through licence/security/dependency gates.

Priority terms:
- German: Hanf, Cannabis, Präzisionslandwirtschaft, Agrarrobotik, Sensorik, Gewächshausautomation, Pflanzenphänotypisierung.
- Italian: canapa, cannabis, agricoltura di precisione, robotica agricola, sensoristica, serre.
- Japanese: 農業ロボット, センサー, 精密農業, 植物フェノタイピング, 大麻, 産業用ヘンプ.
- Chinese: 农业机器人, 传感器, 精准农业, 植物表型, 工业大麻.
- Korean: 농업 로봇, 센서, 정밀농업, 식물 표현형, 산업용 대마.
- Spanish: agricultura de precisión, robótica agrícola, sensores, fenotipado vegetal, cáñamo, cannabis.

## 7. Priority software-sharing protocol

### P0 — Safe architectural sharing
Share interfaces, schemas, terminology, algorithms, data models and adapter contracts across Biupiu departments.

### P1 — Licence-compatible reusable code
MIT/BSD/Apache resources may become implementation candidates after security, dependency and compatibility checks.

### P2 — Copyleft isolation
GPL/AGPL and other reciprocal licences remain isolated until legal/IP architecture explicitly permits their use.

### P3 — Non-commercial / restricted research
CC BY-NC, CC BY-NC-SA and similar sources remain research/reference material unless separate permission is obtained.

### P4 — Unknown/no licence
Reference only. No code copying or commercial integration.

## 8. Biupiu integration targets
Cross-link to smart-farming/, smart-farming/software/, smart-farming/online-platform/, simulators/, software/rnd-os-ai/, research/BIUPIU-OS-DMS-SUBSYSTEM-MASTER-INDEX-v1.0.md, research/BIUPIU-INSTRUMENTATION-MACHINE-INTERFACE-RESEARCH-v1.0.md, research/BIUPIU-GLOBAL-MULTILINGUAL-RESEARCH-INTELLIGENCE-PROTOCOL-v1.0.md, research/BIUPIU-INSTRUMENTATION-AUTOMATION-ROBOTICS-AI-GATE-v1.0.md and research/BIUPIU-GATE-LEARNING-ARCHITECTURE-v1.0.md.

## 9. Promotion boundary
This harvest does not claim that external code has been copied, compiled, tested, production-integrated or made Biupiu-owned.

The first implementation checkpoint is: OpenWeedLocator + Open-PhenoLiDAR -> isolated adapters -> dependency audit -> ROS/Python compatibility test -> hardware-in-loop test -> Biupiu Intelligence telemetry contract -> promotion decision.

## 10. Harvest result
RESEARCH HARVEST: COMPLETE  
CROSS-LINKING: COMPLETE  
FOREIGN-LANGUAGE DISCOVERY: COMPLETE  
OPEN-SOURCE LICENCE SCREEN: COMPLETE for identified GitHub candidates  
COMMERCIAL CODE INTEGRATION: NOT YET PROMOTED  
RUNTIME VALIDATION: PENDING  
REPOSITORY INDEX UPDATE: SAME CHECKPOINT