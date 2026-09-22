"""Controlled material screening module for OS pipeline tests."""
def run(modulus_GPa=10.0, density_kg_m3=1000.0):
    if modulus_GPa <= 0 or density_kg_m3 <= 0: raise ValueError("material properties must be positive")
    return {"specific_modulus_MPa_per_kg_m3": (modulus_GPa*1000.0)/density_kg_m3}
