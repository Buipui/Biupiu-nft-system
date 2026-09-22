# BuildPui Architecture Simulator Schema v1.0

Status: IMPLEMENTED — SCHEMA DRAFT / AUTOMATED RUNTIME TESTS OPEN
Contract: buildpui/architecture/BUILDPUI-DT-INTEGRATION-CONTRACT-v1.0.md

## Canonical JSON object envelope

Every BuildPui object uses:

- object_id: stable string
- object_type: enum
- schema_version: string
- evidence_state: enum
- provenance: array of ProvenanceRecord references
- licence: LicensingRecord reference
- created_at: ISO-8601 timestamp
- assumptions: array
- uncertainties: array
- open_questions: array
- relations: array of typed links
- payload: type-specific data

## State machine

UNREVIEWED -> CATALOGUED -> RESEARCH-SUPPORTED -> SIMULATION-READY -> SIMULATION-EXECUTED -> PHYSICALLY-TESTED -> VALIDATED

Any state may transition to REJECTED. Contradictions force an OPEN question and block automatic promotion.

## DigitalTwinRef

Required: twin_id, object_type, state, timestamp, source_ref, quality_flag.

Allowed state: observed | desired | computed | simulated | validated | actuated.

Actuated is disabled unless a separate runtime/safety gate explicitly authorises it.

## CompositeMaterialCard

Required: material_id, constituents, manufacturing_process, properties, source_refs, licence_ref, limitations.

Properties are records containing name, value, unit, condition, value_state, test_method, uncertainty. value_state must be measured | assumed | simulated | unknown.

## SimulationRun

Required: run_id, model_ref, input_refs, solver, configuration_ref, assumptions, outputs, convergence, reproducibility_ref, status.

No output may be labelled validated without a corresponding ValidationRecord.

## EvidenceRecord

Required: evidence_id, source_type, title, authors, date, doi_or_url, licence_state, relevance_tags, evidence_state, notes.

Default source types: researchgate | emerald_insight | house_and_home | standards | patent | repository | experiment | other.

## ValidationRecord

Required: validation_id, target_ref, validation_type, test_or_benchmark_ref, method, result, reviewer, date, limitations.

## LicensingRecord

Required: licence_id, source_url, licence_state, permitted_use, restrictions, checked_at.

Protected full text, images, tables, proprietary datasets and product copy remain excluded unless explicit permission/licence allows reuse.

## Machine-readable example

~~~json
{
  "object_id": "BP-COMP-EXAMPLE-001",
  "object_type": "CompositeMaterialCard",
  "schema_version": "1.0",
  "evidence_state": "RESEARCH-SUPPORTED",
  "provenance": ["EVID-EXAMPLE-001"],
  "licence": "LIC-EXAMPLE-001",
  "created_at": "2026-09-22T18:03:00+02:00",
  "assumptions": [],
  "uncertainties": ["Physical properties require project-specific testing"],
  "open_questions": ["Fire and long-term durability performance"],
  "relations": [],
  "payload": {
    "material_id": "BP-COMP-EXAMPLE-001",
    "constituents": [],
    "manufacturing_process": "UNKNOWN",
    "properties": [],
    "source_refs": ["EVID-EXAMPLE-001"],
    "licence_ref": "LIC-EXAMPLE-001",
    "limitations": ["Illustrative record only"]
  }
}
~~~

## Verification gates

COMPLETED: schema contract drafted and linked to v1.0 integration contract.
VERIFIED: state separation, provenance, licensing, uncertainty, and validation references are explicitly represented.
OPEN: JSON Schema formalisation, schema linting, executable tests, simulator runtime, IFC/OpenUSD interoperability, numerical/physical validation.