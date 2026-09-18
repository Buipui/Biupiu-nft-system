"""BPU-01 economic simulation model.

Local research model only.
It does not forecast or predict BPU market price and does not connect
to a live blockchain or exchange.
"""

from dataclasses import dataclass

@dataclass
class Scenario:
    users: int
    purchases_per_user: float
    average_purchase_bpu: float
    seller_pct: float
    marketplace_pct: float
    treasury_pct: float
    liquidity_pct: float

    def validate(self):
        total = self.seller_pct + self.marketplace_pct + self.treasury_pct + self.liquidity_pct
        if abs(total - 100.0) > 1e-9:
            raise ValueError("Allocation percentages must total 100%.")
        if min(self.users, self.purchases_per_user, self.average_purchase_bpu) < 0:
            raise ValueError("Activity inputs cannot be negative.")

    def run(self):
        self.validate()
        transactions = self.users * self.purchases_per_user
        gross_bpu = transactions * self.average_purchase_bpu
        return {
            "users": self.users,
            "transactions": transactions,
            "gross_bpu_settled": gross_bpu,
            "seller_bpu": gross_bpu * self.seller_pct / 100,
            "marketplace_bpu": gross_bpu * self.marketplace_pct / 100,
            "treasury_bpu": gross_bpu * self.treasury_pct / 100,
            "liquidity_network_bpu": gross_bpu * self.liquidity_pct / 100,
        }


def run_example_scenarios():
    """Illustrative scenarios; not market forecasts."""
    scenarios = {
        "pilot": Scenario(100, 2, 50, 70, 15, 10, 5),
        "growth": Scenario(1000, 3, 60, 70, 15, 10, 5),
        "scale": Scenario(10000, 4, 75, 70, 15, 10, 5),
    }
    return {name: scenario.run() for name, scenario in scenarios.items()}


if __name__ == "__main__":
    for name, result in run_example_scenarios().items():
        print(name, result)
