"""Bounded ML self-diagnostics and self-healing coordinator.

Diagnostics are deterministic and evidence-producing. "Self-healing" here means
detect -> quarantine -> propose reversible repair -> validate -> regress -> approve.
It never rewrites authoritative code, silently changes model policy, or actuates
hardware. Core OS/DMS and human promotion remain authoritative.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Mapping, Sequence
import hashlib
import json
import math

from .learning import FailureObservation, fingerprint_failure, summarize_failure_pattern
from .ml.backends import BACKENDS, probe_backend
from .ml.continual_adaptation import reference_anchored_parameter_update
from .ml.quantum_ml import fidelity_quantum_kernel


@dataclass(frozen=True)
class DiagnosticFinding:
    check_id: str
    target: str
    state: str
    severity: str
    detail: str
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class RepairProposal:
    repair_id: str
    target: str
    action: str
    prior_state: str
    candidate_state: str
    rollback_state: str
    requires_validation: bool = True
    requires_regression: bool = True
    requires_human_approval: bool = True
    promotion_allowed: bool = False


@dataclass(frozen=True)
class MLHealthReport:
    report_id: str
    findings: tuple[DiagnosticFinding, ...]
    repairs: tuple[RepairProposal, ...]
    backend_inventory: tuple[dict, ...]
    overall_state: str
    promotion_allowed: bool = False


def _hash(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


def diagnose_learning_integrity(records: Sequence[object]) -> DiagnosticFinding:
    failures = []
    for record in records:
        try:
            from .learning import verify_learning_record
            if not verify_learning_record(record):
                failures.append(getattr(record, "learning_id", "unknown"))
        except Exception as exc:
            failures.append(f"exception:{type(exc).__name__}")
    return DiagnosticFinding(
        "ML-LEARNING-INTEGRITY", "learning-records",
        "PASS" if not failures else "FAIL", "HIGH" if failures else "INFO",
        "learning provenance hashes verified" if not failures else "learning provenance mismatch detected",
        tuple(failures),
    )


def diagnose_adaptation_bounds() -> DiagnosticFinding:
    current={"w": 1.0}; reference={"w": 1.0}; gradient={"w": 100.0}
    updated=reference_anchored_parameter_update(
        current, reference, gradient, learning_rate=1.0, anchor_strength=0.0, max_step=0.05
    )
    safe=abs(updated["w"]-current["w"]) <= 0.05 and math.isfinite(updated["w"])
    return DiagnosticFinding(
        "ML-ADAPTATION-BOUNDS", "continual-adaptation",
        "PASS" if safe else "FAIL", "HIGH" if not safe else "INFO",
        "reference-anchored update remains within configured step bound",
    )


def diagnose_quantum_baseline() -> DiagnosticFinding:
    a=(0.1,0.4); b=(0.7,-0.2)
    k1=fidelity_quantum_kernel(a,b); k2=fidelity_quantum_kernel(b,a)
    safe=0.0 <= k1 <= 1.0 and abs(k1-k2) < 1e-12
    return DiagnosticFinding(
        "ML-QUANTUM-CLASSICAL-BASELINE", "quantum-ml",
        "PASS" if safe else "FAIL", "HIGH" if not safe else "INFO",
        "classical-safe fidelity-kernel baseline is bounded and symmetric",
    )


def diagnose_backend_registry() -> tuple[DiagnosticFinding, tuple[dict, ...]]:
    inventory=[]
    failures=[]
    for spec in BACKENDS:
        try:
            available=probe_backend(spec.backend_id)
            state="AVAILABLE" if available else "NOT_AVAILABLE"
        except Exception as exc:
            available=False
            state="ERROR"
            failures.append(f"{spec.backend_id}:{type(exc).__name__}")
        inventory.append({
            "backend_id":spec.backend_id, "package":spec.package,
            "capabilities":spec.capabilities, "integration_mode":spec.integration_mode,
            "license":spec.license, "available":available, "state":state
        })
    finding=DiagnosticFinding(
        "ML-BACKEND-REGISTRY", "ml-backends",
        "PASS" if not failures else "FAIL", "HIGH" if failures else "INFO",
        "optional backend availability was probed fail-closed",
        tuple(failures),
    )
    return finding, tuple(inventory)


def propose_repair(target: str, action: str, prior_state: str) -> RepairProposal:
    repair_id=f"repair_{_hash((target,action,prior_state))[:24]}"
    return RepairProposal(
        repair_id, target, action, prior_state, "candidate",
        prior_state, True, True, True, False
    )


def diagnose_and_propose(records: Sequence[object] = ()) -> MLHealthReport:
    findings=[
        diagnose_learning_integrity(records),
        diagnose_adaptation_bounds(),
        diagnose_quantum_baseline(),
    ]
    backend_finding, inventory=diagnose_backend_registry()
    findings.append(backend_finding)

    repairs=[]
    for finding in findings:
        if finding.state == "FAIL":
            repairs.append(propose_repair(
                finding.target,
                "quarantine affected path, capture evidence, apply smallest reversible repair, then validate/regress",
                "FAILED",
            ))

    overall="HEALTHY" if not repairs else "DEGRADED_REPAIR_PROPOSED"
    payload={
        "findings":[asdict(f) for f in findings],
        "repairs":[asdict(r) for r in repairs],
        "backend_inventory":inventory,
        "overall_state":overall,
    }
    return MLHealthReport(
        report_id=f"mlhealth_{_hash(payload)[:24]}",
        findings=tuple(findings),
        repairs=tuple(repairs),
        backend_inventory=inventory,
        overall_state=overall,
        promotion_allowed=False,
    )


def apply_validated_repair(proposal: RepairProposal, *,
                           validation_passed: bool,
                           regression_passed: bool,
                           human_approved: bool) -> RepairProposal:
    if not (validation_passed and regression_passed and human_approved):
        return proposal
    return RepairProposal(**{
        **asdict(proposal),
        "candidate_state":"validated",
        "promotion_allowed":True,
    })
