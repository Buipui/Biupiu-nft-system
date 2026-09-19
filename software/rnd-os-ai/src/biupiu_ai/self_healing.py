"""Bounded self-healing orchestration for Biupiu Intelligence.

The core planner does not expose arbitrary shell execution. Host environments
provide an injected executor with their own allowlist and privilege boundary.
"""

from dataclasses import dataclass
from typing import Callable, Dict, FrozenSet, Optional, Sequence, Tuple
import hashlib
import json

from .learning import make_learning_record, LearningRecord


RISK_LEVELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}


def failure_signature(component: str, error_type: str, message: str) -> str:
    raw = f"{component}|{error_type}|{message}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


@dataclass(frozen=True)
class FailureEvent:
    failure_id: str
    component: str
    error_type: str
    message: str
    environment: str = "development"
    signature: str = ""

    def normalized(self) -> "FailureEvent":
        sig = self.signature or failure_signature(self.component, self.error_type, self.message)
        return FailureEvent(self.failure_id, self.component, self.error_type, self.message, self.environment, sig)


@dataclass(frozen=True)
class RemediationRule:
    rule_id: str
    signature: str
    action: str
    risk: str
    allowed_components: FrozenSet[str]
    max_files: int = 5
    max_attempts: int = 3
    requires_approval: bool = True

    def __post_init__(self) -> None:
        if self.risk not in RISK_LEVELS:
            raise ValueError(f"invalid risk: {self.risk}")
        if self.max_files < 1 or self.max_attempts < 1:
            raise ValueError("repair limits must be positive")


@dataclass(frozen=True)
class RepairResult:
    failure_id: str
    state: str
    rule_id: Optional[str]
    attempt: int
    changed_files: Tuple[str, ...]
    tests_passed: bool
    regression_test_added: bool
    rolled_back: bool
    reason: str
    learning_record: Optional[LearningRecord]


Executor = Callable[[RemediationRule, FailureEvent], Sequence[str]]
Verifier = Callable[[FailureEvent, Sequence[str]], bool]
Rollback = Callable[[Sequence[str]], None]


class SelfHealingController:
    """Closed-loop controller with bounded scope and a circuit breaker."""

    def __init__(self, rules: Sequence[RemediationRule], *, protected_files: FrozenSet[str] = frozenset(), max_attempts: int = 3) -> None:
        self.rules: Dict[str, RemediationRule] = {r.rule_id: r for r in rules}
        self.protected_files = protected_files
        self.max_attempts = max_attempts
        self.attempts: Dict[str, int] = {}
        self.learned: Dict[str, str] = {}

    def choose_rule(self, event: FailureEvent) -> Optional[RemediationRule]:
        event = event.normalized()
        for rule in self.rules.values():
            if rule.signature == event.signature and event.component in rule.allowed_components:
                return rule
        return None

    def attempt(self, event: FailureEvent, *, executor: Executor, verifier: Verifier, rollback: Rollback, regression_test_added: bool = False, approval: bool = False) -> RepairResult:
        event = event.normalized()
        rule = self.choose_rule(event)
        if rule is None:
            return self._learn(event, "ESCALATED", None, 0, (), False, regression_test_added, False, "no approved remediation rule")

        count = self.attempts.get(event.signature, 0) + 1
        self.attempts[event.signature] = count
        limit = min(self.max_attempts, rule.max_attempts)
        if count > limit:
            return self._learn(event, "ESCALATED", rule, count, (), False, regression_test_added, False, "circuit breaker reached")
        if rule.requires_approval and event.environment == "production" and not approval:
            return self._learn(event, "PROMOTION_PENDING", rule, count, (), False, regression_test_added, False, "production approval required")

        changed = tuple(executor(rule, event))
        if len(changed) > rule.max_files:
            rollback(changed)
            return self._learn(event, "ROLLED_BACK", rule, count, changed, False, regression_test_added, True, "repair exceeded file-scope limit")
        if set(changed) & self.protected_files:
            rollback(changed)
            return self._learn(event, "ROLLED_BACK", rule, count, changed, False, regression_test_added, True, "protected file touched")
        if rule.action == "PATCH_CODE" and not regression_test_added:
            rollback(changed)
            return self._learn(event, "ROLLED_BACK", rule, count, changed, False, regression_test_added, True, "missing regression test")

        passed = verifier(event, changed)
        if not passed:
            rollback(changed)
            state = "ESCALATED" if count >= limit else "ROLLED_BACK"
            return self._learn(event, state, rule, count, changed, False, regression_test_added, True, "verification failed")

        self.learned[event.signature] = rule.rule_id
        state = "PROMOTION_PENDING" if rule.requires_approval else "LEARNED"
        return self._learn(event, state, rule, count, changed, True, regression_test_added, False, "repair verified")

    def _learn(self, event: FailureEvent, state: str, rule: Optional[RemediationRule], attempt: int, changed: Sequence[str], tests_passed: bool, regression_test_added: bool, rolled_back: bool, reason: str) -> RepairResult:
        record = make_learning_record(
            learning_id=f"FAIL-{event.failure_id}-A{attempt}",
            target_type="SELF_HEALING",
            target_id=event.failure_id,
            input_refs=[f"failure-signature:{event.signature}"],
            evidence_state="SUPPORTED" if tests_passed else "INCONCLUSIVE",
            knowledge_class="REPOSITORY_CHANGE" if tests_passed else "FAILURE",
            result_version=rule.rule_id if rule else "none",
            observed_outcome=json.dumps({"state": state, "reason": reason, "changed_files": list(changed), "tests_passed": tests_passed, "rolled_back": rolled_back}, sort_keys=True),
            next_action="REVIEW" if state in {"ESCALATED", "PROMOTION_PENDING"} else "REPLICATE",
            human_decision="PENDING",
        )
        return RepairResult(event.failure_id, state, rule.rule_id if rule else None, attempt, tuple(changed), tests_passed, regression_test_added, rolled_back, reason, record)