"""Biupiu Farming System OS — touchscreen/HMI function prototype."""
from dataclasses import dataclass, field
from time import time

@dataclass
class Zone:
    zone_id: str
    name: str
    telemetry: dict = field(default_factory=dict)
    recommendation: dict = field(default_factory=dict)

class FarmingOS:
    def __init__(self):
        self.zones = {}
        self.events = []
        self.hub_online = False

    def register_zone(self, zone_id, name):
        self.zones[zone_id] = Zone(zone_id, name)

    def update_telemetry(self, zone_id, data):
        self.zones[zone_id].telemetry = data
        self.events.append({"ts": time(), "type": "telemetry", "zone": zone_id, "data": data})

    def queue_advisory(self, zone_id, advisory):
        # Advisory only: no actuator is driven here.
        self.zones[zone_id].recommendation = advisory
        self.events.append({"ts": time(), "type": "ai_advisory", "zone": zone_id, "advisory": advisory})

    def approve_action(self, zone_id, action):
        event = {"ts": time(), "type": "human_approval", "zone": zone_id, "action": action}
        self.events.append(event)
        return event

    def dashboard(self):
        return {
            "hub_online": self.hub_online,
            "zones": [{"id": z.zone_id, "name": z.name,
                       "telemetry": z.telemetry,
                       "recommendation": z.recommendation}
                      for z in self.zones.values()],
            "event_count": len(self.events)
        }

if __name__ == "__main__":
    os = FarmingOS()
    os.register_zone("Z01", "Regenerative Pilot Zone")
    os.update_telemetry("Z01", {"soil_moisture_pct": 54.2, "air_temp_c": 22.4})
    os.queue_advisory("Z01", {"recommendation": "MONITOR", "requires_human_approval": True})
    print(os.dashboard())
