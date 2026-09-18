from dataclasses import dataclass
from threading import Lock
from time import monotonic
from typing import Dict, Optional, Tuple


@dataclass(frozen=True)
class AuditEvent:
    request_id: str
    event: str
    outcome: str


@dataclass(frozen=True)
class ReplayDecision:
    accepted: bool
    reason: str


class GatewayState:
    """Process-local abuse/replay guard.

    This is a deterministic foundation for the gateway boundary. It is not a
    distributed rate limiter and must be replaced by shared durable state
    before horizontally scaled production deployment.
    """

    def __init__(self, requests_per_minute: int = 30, replay_ttl_seconds: int = 300):
        self.requests_per_minute = requests_per_minute
        self.replay_ttl_seconds = replay_ttl_seconds
        self._lock = Lock()
        self._seen: Dict[str, float] = {}
        self._requests: Dict[str, list[float]] = {}
        self._audit: list[AuditEvent] = []

    def admit(self, client_key: str, idempotency_key: Optional[str]) -> ReplayDecision:
        now = monotonic()
        with self._lock:
            self._prune(now)
            if idempotency_key and idempotency_key in self._seen:
                return ReplayDecision(False, "replay-detected")
            times = self._requests.setdefault(client_key, [])
            if len(times) >= self.requests_per_minute:
                return ReplayDecision(False, "rate-limit-exceeded")
            times.append(now)
            if idempotency_key:
                self._seen[idempotency_key] = now
            return ReplayDecision(True, "accepted")

    def record(self, request_id: str, event: str, outcome: str) -> None:
        with self._lock:
            self._audit.append(AuditEvent(request_id, event, outcome))

    def audit_snapshot(self) -> Tuple[AuditEvent, ...]:
        with self._lock:
            return tuple(self._audit)

    def _prune(self, now: float) -> None:
        cutoff = now - 60
        for key, times in list(self._requests.items()):
            self._requests[key] = [t for t in times if t >= cutoff]
            if not self._requests[key]:
                del self._requests[key]
        replay_cutoff = now - self.replay_ttl_seconds
        self._seen = {k: t for k, t in self._seen.items() if t >= replay_cutoff}
