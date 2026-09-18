from math import exp
from dataclasses import dataclass, asdict
R=287.05; G=1.4; CP=1005.0
@dataclass
class Cycle:
    pressure_ratio: float
    compressor_eff: float
    turbine_eff: float
    recuperator_eff: float
    cold_dp_frac: float
    hot_dp_frac: float
    turbine_inlet_K: float
    generator_eff: float
    accessory_kw: float

def isa(h):
    if h<=11000:
        T=288.15-0.0065*h
        P=101325*(T/288.15)**(9.80665/(R*0.0065))
    else:
        T=216.65; P=22632.06*exp(-9.80665*(h-11000)/(R*T))
    return T,P

def screen(c, target_kw, altitude_m=0, lhv_kjkg=43000):
    T0,P0=isa(altitude_m)
    pc=P0*c.pressure_ratio*(1-c.cold_dp_frac)
    pt=P0*(1-c.hot_dp_frac)
    T2s=T0*(pc/P0)**((G-1)/G)
    T2=T0+(T2s-T0)/c.compressor_eff
    T4=c.turbine_inlet_K
    T5s=T4*(pt/pc)**((G-1)/G)
    T5=T4-c.turbine_eff*(T4-T5s)
    T3=T2+c.recuperator_eff*max(0,T5-T2)
    q=max(1e-6,CP*(T4-T3))
    wt=CP*(T4-T5)
    wc=CP*(T2-T0)
    wnet=max(1e-6,wt-wc)
    air_kg_s=(target_kw+c.accessory_kw)/(wnet*c.generator_eff)
    fuel_kg_s=air_kg_s*q/lhv_kjkg
    return {'altitude_m':altitude_m,'ambient_K':round(T0,2),'ambient_kPa':round(P0/1000,2),'air_kg_s':round(air_kg_s,5),'fuel_kg_h':round(fuel_kg_s*3600,3),'target_net_kw':target_kw,'specific_electric_work_kj_kg':round(wnet*c.generator_eff,2),'T2_K':round(T2,1),'T3_K':round(T3,1),'T5_K':round(T5,1)}

if __name__=='__main__':
    c=Cycle(5.0,.78,.80,.70,.03,.03,1100,.94,3.0)
    for h in (0,2000,5000):
        for kw in (70,140,200,300): print(screen(c,kw,h))