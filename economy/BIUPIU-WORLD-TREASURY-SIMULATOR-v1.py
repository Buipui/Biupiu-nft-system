"""Biupiu World Treasury Simulator v1.0
Virtual educational ledger only. No real funds or blockchain access.
"""

from dataclasses import dataclass, field

@dataclass
class Treasury:
    balances: dict = field(default_factory=lambda: {
        "operating": 0.0,
        "ecosystem": 0.0,
        "research_education": 0.0,
        "marketplace": 0.0,
        "creator_community": 0.0,
        "liquidity_research": 0.0,
        "emergency": 0.0,
    })
    ledger: list = field(default_factory=list)

    def allocate(self, amount, percentages):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if abs(sum(percentages.values()) - 100.0) > 1e-9:
            raise ValueError("Allocation percentages must total 100%.")
        for bucket, pct in percentages.items():
            value = amount * pct / 100.0
            self.balances[bucket] += value
            self.ledger.append({
                "type": "allocation",
                "bucket": bucket,
                "amount": value,
            })

    def spend(self, bucket, amount, purpose):
        if bucket not in self.balances:
            raise KeyError(bucket)
        if amount < 0 or amount > self.balances[bucket]:
            raise ValueError("Insufficient simulated treasury balance.")
        self.balances[bucket] -= amount
        self.ledger.append({
            "type": "spend",
            "bucket": bucket,
            "amount": amount,
            "purpose": purpose,
        })

    def total(self):
        return sum(self.balances.values())

    def report(self):
        return {"balances": dict(self.balances), "total": self.total(),
                "events": len(self.ledger)}


if __name__ == "__main__":
    treasury = Treasury()
    treasury.allocate(100_000, {
        "operating": 20, "ecosystem": 15, "research_education": 20,
        "marketplace": 15, "creator_community": 10,
        "liquidity_research": 10, "emergency": 10,
    })
    treasury.spend("research_education", 5_000, "digital lab programme")
    print(treasury.report())
