"""Repository-level Gate 03 smoke tests for the Biupiu Architecture Simulator."""
import unittest

from biupiu_architecture_simulator import (
    ArchitectureSimulator, Asset, SiteState
)


class ArchitectureSimulatorGate03Tests(unittest.TestCase):
    def setUp(self):
        self.sim = ArchitectureSimulator()

    def test_crs_required(self):
        with self.assertRaises(ValueError):
            self.sim.import_site(SiteState("", -33.9, 18.4))

    def test_green_asset_is_eligible_and_red_is_not(self):
        self.sim.register_asset(Asset("green-1", "Poly Haven", "CC0", "GREEN"))
        self.sim.register_asset(Asset("red-1", "unknown", "unknown", "RED"))
        self.assertEqual([a.asset_id for a in self.sim.eligible_assets()], ["green-1"])
        ok, errors = self.sim.validate()
        self.assertFalse(ok)
        self.assertIn("Blocked asset registered: red-1", errors)

    def test_country_filter(self):
        self.sim.register_asset(Asset("za-1", "open", "CC0", "GREEN", country_tags=["South Africa"]))
        self.sim.register_asset(Asset("jp-1", "open", "CC0", "GREEN", country_tags=["Japan"]))
        self.assertEqual([a.asset_id for a in self.sim.eligible_assets("South Africa")], ["za-1"])

    def test_deterministic_massing(self):
        result = self.sim.propose_massing(144.0, 2, 6.0)
        self.assertEqual(result["structural_bays"], 2)
        self.assertEqual(result["estimated_gfa_m2"], 288.0)

    def test_validation_requires_site(self):
        ok, errors = self.sim.validate()
        self.assertFalse(ok)
        self.assertEqual(errors, ["No GIS site imported"])

    def test_valid_site_and_assets(self):
        self.sim.import_site(SiteState("EPSG:4326", -33.9, 18.4, 20.0, "test"))
        self.sim.register_asset(Asset("green-1", "open", "CC0", "GREEN"))
        ok, errors = self.sim.validate()
        self.assertTrue(ok)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
