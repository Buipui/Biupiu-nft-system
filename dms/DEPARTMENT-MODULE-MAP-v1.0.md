# Biupiu DMS Department Module Map v1.0

| Code | Module | Primary functions |
|---|---|---|
| AGRI | Agriculture | crops, plots, irrigation, regenerative practices, farm logs |
| HEMP | Hemp Processing | intake, drying, decortication, fibre/hurd streams, batch traceability |
| MAN | Manufacturing | production orders, machines, work centres, throughput |
| MAT | Materials | formulations, composite batches, material tests, provenance |
| RND | R&D | projects, experiments, evidence, prototypes, IP gates |
| ENG | Engineering | designs, simulations, revisions, digital-twin links |
| AI | AI & Analytics | models, forecasts, inference jobs, analytics pipelines |
| ROB | Robotics | robot cells, automation jobs, device health, safety interfaces |
| INV | Inventory | stock, warehouses, suppliers, procurement, movements |
| QA | Quality | inspections, tests, non-conformance, release gates |
| MNT | Maintenance | assets, service schedules, faults, work orders |
| CRM | Customer | products, support, feedback, optional R&D participation |
| SUB | Subscription | plans, entitlements, renewals, feature access |
| DEV | Device/Site | devices, certificates, gateways, software versions |
| DTM | Digital Twin | physical asset models, state, telemetry mappings |
| AUD | Audit | security and business event history |

## Initial dependency pattern

HEMP -> MAN -> MAT -> QA -> INV/MNT
AGRI -> HEMP/MAT
RND -> ENG/AI/MAT
ENG -> DTM/ROB
CRM -> SUB/DEV
All modules -> Identity/Audit

Dependencies describe integration contracts, not shared database ownership.
