"""EXP-002: Olla irrigation sensitivity analysis.

This is a transparent scenario model, not a field experiment.
It varies open-soil evaporative demand, olla delivery, and reduction factor.
Units: litres over 30 days for a 1 m^2 test area.
"""

AREA_M2 = 1.0
DAYS = 30
MM_TO_L_PER_M2 = 1.0

for evaporation_mm_day in (3, 5, 7):
    for reduction_factor in (0.40, 0.65, 0.85):
        open_loss_l = evaporation_mm_day * DAYS * AREA_M2 * MM_TO_L_PER_M2
        reduced_loss_l = open_loss_l * (1 - reduction_factor)
        for olla_l_day in (1, 2, 3):
            olla_delivery_l = olla_l_day * DAYS
            balance_l = olla_delivery_l - reduced_loss_l
            print(
                f"evap_mm_day={evaporation_mm_day}, "
                f"reduction={reduction_factor:.2f}, "
                f"olla_l_day={olla_l_day}, "
                f"reduced_loss_l={reduced_loss_l:.1f}, "
                f"olla_delivery_l={olla_delivery_l:.1f}, "
                f"balance_l={balance_l:.1f}"
            )
