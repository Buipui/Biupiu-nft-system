#!/usr/bin/env python3
"""Biupiu SF-01 Raspberry Pi gateway prototype.
Reads JSON telemetry from Arduino, validates it, logs it, and produces
an advisory payload for the Biupiu Intelligence Hub.
"""
import json, time, sqlite3, serial
from dataclasses import dataclass

SERIAL_PORT = "/dev/ttyACM0"
BAUD = 115200
DB = "sf01.db"

@dataclass
class Observation:
    ts: float
    soil_raw: int
    soil_moisture_pct: float
    light_raw: int

def valid(d):
    return (0 <= d.get("soil_raw", -1) <= 1023 and
            0 <= d.get("soil_moisture_pct", -1) <= 100 and
            0 <= d.get("light_raw", -1) <= 1023)

def init_db(c):
    c.execute("CREATE TABLE IF NOT EXISTS observations (ts REAL, soil_raw INTEGER, soil_moisture_pct REAL, light_raw INTEGER)")
    c.commit()

def advisory(obs):
    # Conservative local rule baseline; AI is not allowed to bypass this layer.
    if obs.soil_moisture_pct < 25:
        action = "REVIEW_IRRIGATION"
    elif obs.soil_moisture_pct > 80:
        action = "CHECK_OVERWATERING"
    else:
        action = "MONITOR"
    return {"action": action, "confidence": "rule-baseline", "manual_approval_required": True}

def main():
    db = sqlite3.connect(DB)
    init_db(db)
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=5)
    while True:
        raw = ser.readline().decode(errors="replace").strip()
        if not raw: continue
        try: d = json.loads(raw)
        except json.JSONDecodeError: continue
        if not valid(d): continue
        o = Observation(time.time(), int(d["soil_raw"]), float(d["soil_moisture_pct"]), int(d["light_raw"]))
        db.execute("INSERT INTO observations VALUES (?,?,?,?)", (o.ts,o.soil_raw,o.soil_moisture_pct,o.light_raw)); db.commit()
        print(json.dumps({"observation": d, "advisory": advisory(o)}))

if __name__ == "__main__": main()
