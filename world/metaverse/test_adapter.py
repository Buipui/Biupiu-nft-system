import unittest
from adapter import EntityState, MetaverseAdapter, WorldState


class MetaverseAdapterTests(unittest.TestCase):
    def test_register_and_snapshot(self):
        world = WorldState("biupiu-world")
        world.register(EntityState("farm-01","farm",{"position":[0,0,0]}))
        snap = world.snapshot()
        self.assertEqual(snap["worldId"],"biupiu-world")
        self.assertEqual(len(snap["entities"]),1)

    def test_duplicate_rejected(self):
        world = WorldState("biupiu-world")
        world.register(EntityState("e1","vehicle",{"position":[0,0,0]}))
        with self.assertRaises(ValueError):
            world.register(EntityState("e1","vehicle",{"position":[1,0,0]}))

    def test_client_input_is_not_authority(self):
        world = WorldState("biupiu-world")
        world.register(EntityState("e1","vehicle",{"position":[0,0,0]}))
        result = MetaverseAdapter(world).propose_interaction("e1","inspect")
        self.assertTrue(result["accepted_for_validation"])
        self.assertEqual(world.version,1)
