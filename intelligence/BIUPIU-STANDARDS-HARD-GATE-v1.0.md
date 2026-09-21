# Biupiu Standards Hard Gate v1.0
Date: 2026-09-21
Status: IMPLEMENTED AS ENGINEERING GOVERNANCE — CERTIFICATION NOT CLAIMED

## Rule
All Biupiu systems shall be designed against applicable current international standards. A standard is a hard engineering requirement only where its scope applies. Compliance/certification may only be claimed after documented conformity assessment or accredited certification where required.

## Core standards matrix
- ISO 9001:2026 — quality-management process baseline
- ISO/IEC 27001:2022 — information-security management
- ISO/IEC 42001:2023 — AI-management governance
- ISO 14001:2026 — environmental-management baseline where applicable
- ISO 11783 series — agricultural machinery communications/ISOBUS
- ISO 11898 series — CAN
- IEC 61131-3 — PLC programming
- IEC 62443 series — industrial automation/control cybersecurity where applicable
- ISO 26262 — road-vehicle functional safety where applicable
- ISO/SAE 21434 — road-vehicle cybersecurity where applicable
- ISO 13849 / IEC 62061 — machinery safety where applicable
- Domain-specific standards shall be added through the same applicability review.

## Enforcement
Every subsystem requires:
1. applicable-standard declaration
2. version/edition recorded
3. requirements traceability
4. design evidence
5. implementation evidence
6. automated/static tests where possible
7. SIL/HIL or equivalent validation where applicable
8. fault/safety/security testing
9. deviation/exception record
10. verification status
11. certification status kept separate from engineering compliance status

## Prohibited claims
"ISO certified", "ISO compliant", or equivalent certification claims are prohibited unless the relevant formal assessment/certification has actually occurred.

## Smart Systems priority
ISO 11783 is the default reference family for applicable agricultural machine networks. ISO 11783-3:2026 is the current published Part 3. ISO 11783-12:2019 remains current while ISO/FDIS 11783-12 is in approval; the FDIS must not be represented as the published standard until ISO publishes it.

## Promotion states
REFERENCE → DESIGNED-TO → IMPLEMENTED → VERIFIED → CONFORMITY-ASSESSED → CERTIFIED (only where formally certified).

## AI learning integration
The learning system records standard, edition, applicability, evidence, test result, deviations and promotion state. It must never infer certification from passing internal tests.

## Gate result
Architecture governance: PASS
Standards applicability gate: ACTIVE
Certification claim: NOT AUTHORIZED
Runtime conformity: PENDING per subsystem
