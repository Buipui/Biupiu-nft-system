# Biupiu Foreign-Language Automation & Robotics Research Register v1.0

**Date:** 20 September 2026  
**Priority languages:** Italian and German  
**Priority industrial references:** Siemens and Fujitsu

## Research protocol
Retain original-language source, original terminology, translated interpretation, source type, licence/access status and intended Biupiu subsystem. Translation is for understanding and does not change evidence status.

## Italian priority
- Robotica industriale — Giovanni Legnani / Irene Fassi: https://www.perlego.com/it/book/2818091/robotica-industriale-pdf
- Let's Program a PLC — Marco Gottardo: https://openlibrary.org/works/OL29024760W/Let%27s_Program_a_Plc_%28Edizione_2016%29
- CNR-ITIA / COMAU ROS-Industrial: https://github.com/CNR-STIIMA-IRAS/comau-experimental

## German priority
- Systemintegration in Industrie 4.0 und IoT: Vom Ethernet bis hin zum Internet und OPC UA — Wolfgang Babel: https://link.springer.com/book/10.1007/978-3-658-42987-4
- Automatisieren mit SPS Theorie und Praxis — Wellenreuther/Zastrow: https://link.springer.com/book/10.1007/978-3-663-05705-5
- OPC — Von Data Access bis Unified Architecture — VDE Verlag: https://www.vde-verlag.de/books/483506/opc.html
- Speicherprogrammierbare Steuerungen im Industrial IoT: https://www.hanserpublications.com/Speicherprogrammierbare-Steuerungen-im-Industrial-IoT/978-3-446-48243-2

## Siemens cross-link
https://www.siemens.com/en-us/products/opc-ua/
Route: ELECTROMAG -> ROBOTICS -> DIGITAL-TWIN -> COMPUTE -> AI -> MACHINE-CAPABILITY -> DMS

https://www.siemens.com/en-gb/content/architecture-hub/industrial-ai-orchestration-layer/
Route: TELEMETRY -> EDGE -> OPC UA/MQTT/REST -> DATA -> AI -> HUMAN/CONTROLLED DECISION

## Fujitsu cross-link
https://github.com/FujitsuResearch
Route: AI -> OPTIMISATION -> QUBO -> ANOMALY DETECTION -> AGENT EVALUATION -> INTELLIGENCE LAYER

## Open-source cross-link
- ROS-Industrial: https://github.com/ros-industrial
- PLCnext ROS bridge: https://github.com/PLCnext/PLCnext-ROS-bridge
- HumaRobotics Modbus: https://github.com/HumaRobotics/modbus
- Serial Studio: https://github.com/Serial-Studio/Serial-Studio

These are references/adapters, not uncontrolled dependency imports.

## Open-book/literature routing
German sources are prioritised for SPS/PLC, fieldbus, OPC UA, Industrie 4.0, SCADA/HMI/MES/ERP, safety and mechatronics. Italian sources are prioritised for industrial robotics, manipulator modelling, robot control, PLC programming and automation terminology.

## Integration status
Harvest complete at research-register level.
Next: SOURCE CLASSIFICATION -> LICENCE CHECK -> TERMINOLOGY NORMALISATION -> CAPABILITY MAPPING -> ADAPTER DESIGN -> UNIT TEST -> SIMULATION -> HARDWARE-IN-LOOP -> SECURITY/SAFETY -> PROMOTION
