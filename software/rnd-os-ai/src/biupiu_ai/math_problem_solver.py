"""Deterministic mathematics/problem-solving boundary for Biupiu Intelligence."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Mapping, Sequence

class VerificationLevel(str, Enum):
    FORMAL = "formal"
    DETERMINISTIC = "deterministic"
    NUMERICAL = "numerical"
    SIMULATION = "simulation"
    HEURISTIC = "heuristic"

@dataclass(frozen=True)
class Problem:
    problem_id: str
    statement: str
    domain: str
    constraints: tuple[str, ...] = ()

@dataclass(frozen=True)
class VerificationResult:
    problem_id: str
    level: VerificationLevel
    passed: bool
    residual: float | None = None
    tolerance: float | None = None
    evidence: Mapping[str, str] = field(default_factory=dict)

    def accepted(self) -> bool:
        return self.passed and self.level in {VerificationLevel.FORMAL, VerificationLevel.DETERMINISTIC, VerificationLevel.NUMERICAL, VerificationLevel.SIMULATION}

def classify_problem(problem: Problem) -> tuple[str, ...]:
    text = (problem.statement + ' ' + ' '.join(problem.constraints)).lower()
    tags = []
    keywords = {
        'geometry': ('geometry', 'polygon', 'triangle', 'circle', 'mesh', 'transform'),
        'biology': ('biology', 'biological', 'genome', 'genomics', 'dna', 'rna', 'gene', 'cell', 'microorganism'),
        'molecular': ('molecular', 'protein', 'peptide', 'enzyme', 'ligand', 'folding'),
        'multi_omics': ('multi-omics', 'omics', 'transcriptome', 'proteome', 'metabolome', 'epigenome'),
        'quantum_algorithm': ('quantum algorithm', 'qaoa', 'vqe', 'grover', 'quantum annealing', 'quantum optimization'),
        'optimization': ('optim', 'minimize', 'maximize', 'constraint'),
        'algebra': ('equation', 'polynomial', 'matrix', 'linear'),
        'calculus': ('derivative', 'integral', 'gradient', 'differential'),
        'probability': ('probability', 'distribution', 'random', 'stochastic'),
        'numerical': ('numeric', 'residual', 'tolerance', 'approx'),
    }
    for tag, words in keywords.items():
        if any(word in text for word in words): tags.append(tag)
    return tuple(sorted(set(tags)))

def verify_residual(problem_id: str, residual: float, tolerance: float, evidence: Mapping[str, str] | None = None) -> VerificationResult:
    if tolerance < 0 or residual < 0: raise ValueError('residual and tolerance must be non-negative')
    return VerificationResult(problem_id, VerificationLevel.NUMERICAL, residual <= tolerance, residual, tolerance, evidence or {})

def verify_invariants(problem_id: str, values: Mapping[str, float], invariants: Sequence[Callable[[Mapping[str, float]], bool]], evidence: Mapping[str, str] | None = None) -> VerificationResult:
    return VerificationResult(problem_id, VerificationLevel.DETERMINISTIC, all(bool(rule(values)) for rule in invariants), evidence=evidence or {})
