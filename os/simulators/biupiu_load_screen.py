"""Controlled structural load screening module for OS pipeline tests."""
def run(specific_modulus_MPa_per_kg_m3=1.0, load_N=1000.0):
    if load_N < 0: raise ValueError("load_N must be non-negative")
    return {"screening_index": specific_modulus_MPa_per_kg_m3/load_N if load_N else 0.0}
