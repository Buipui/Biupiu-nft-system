"""EXP-001 toy model. Not a physical optical propagation simulator."""
for sigma in [0.0, 0.1, 0.2, 0.3, 0.4]:
    cross = min(0.95, 2.5 * sigma * sigma)
    conventional_ber = 0.001 + 0.12 * cross
    structured_ber = 0.002 + 0.20 * cross + 0.03 * sigma
    print(f"sigma={sigma:.1f}, cross={cross:.4f}, conventional_ber={conventional_ber:.5f}, structured_ber={structured_ber:.5f}")
