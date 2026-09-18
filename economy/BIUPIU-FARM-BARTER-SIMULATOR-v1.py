"""Biupiu World Farm Barter Simulator v1.0
Virtual crop/barter economy for educational use.
"""

from dataclasses import dataclass, field

@dataclass
class Farm:
    name: str
    crops: dict
    needs: dict
    barter_log: list = field(default_factory=list)

    def can_offer(self, crop, quantity):
        return self.crops.get(crop, 0) >= quantity

    def trade(self, other, offer_crop, offer_qty, want_crop, want_qty):
        if not self.can_offer(offer_crop, offer_qty):
            raise ValueError(f"{self.name} lacks {offer_qty} {offer_crop}")
        if not other.can_offer(want_crop, want_qty):
            raise ValueError(f"{other.name} lacks {want_qty} {want_crop}")

        self.crops[offer_crop] -= offer_qty
        other.crops[offer_crop] = other.crops.get(offer_crop, 0) + offer_qty
        other.crops[want_crop] -= want_qty
        self.crops[want_crop] = self.crops.get(want_crop, 0) + want_qty

        event = {
            "from": self.name,
            "to": other.name,
            "offer": {offer_crop: offer_qty},
            "receive": {want_crop: want_qty},
        }
        self.barter_log.append(event)
        other.barter_log.append(event)
        return event

if __name__ == "__main__":
    farm_a = Farm("Regenerative Farm A", {"maize": 100, "beans": 20}, {"beans": 10})
    farm_b = Farm("Community Farm B", {"maize": 30, "beans": 80}, {"maize": 20})
    event = farm_a.trade(farm_b, "maize", 20, "beans", 10)
    print(event)
    print(farm_a.crops)
    print(farm_b.crops)
