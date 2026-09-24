"""Deterministic Digital Twin benchmark fixture for later physical correlation.
Screening-only synthetic material cards; not measured material allowables.
"""
import hashlib, json, math, time

L=1.0
B=0.1
T=0.01
SAFETY_FACTOR=2.5
LOADS_N=(50.0,100.0,150.0)
CARDS={
    "BMG-H01":{"E_Pa":25e9,"density_kg_m3":1250.0},
    "BMG-F01":{"E_Pa":30e9,"density_kg_m3":1200.0},
    "BMG-HF01":{"E_Pa":32e9,"density_kg_m3":1220.0},
    "BMG-HFB01":{"E_Pa":40e9,"density_kg_m3":1350.0},
}
def simulate(E,rho,P=100.0):
    I=B*T**3/12.0
    A=B*T
    return {
        "mass_kg":rho*A*L,
        "tip_deflection_mm":P*L**3/(3.0*E*I)*1000.0,
        "max_stress_MPa":6.0*P*L/(B*T**2)/1e6,
        "first_frequency_Hz":(1.875104**2/(2.0*math.pi*L**2))*math.sqrt(E*I/(rho*A)),
        "buckling_margin":(math.pi**2*E*I/(4.0*L**2))/(SAFETY_FACTOR*P),
    }
def main():
    evidence={}
    for mid,c in CARDS.items():
        hashes=[]
        start=time.perf_counter_ns()
        first=None
        for _ in range(10000):
            r=simulate(c["E_Pa"],c["density_kg_m3"])
            if first is None: first=r
            hashes.append(hashlib.sha256(json.dumps(r,sort_keys=True).encode()).hexdigest())
        elapsed=time.perf_counter_ns()-start
        evidence[mid]={
            "iterations":10000,
            "elapsed_ns":elapsed,
            "mean_us":elapsed/10_000/1000.0,
            "deterministic":len(set(hashes))==1,
            "result":first,
        }
    return evidence
if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
