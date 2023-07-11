from engine.sterman_engine import SternmanEngine
import unittest

class SternmanEngineTest(unittest.TestCase):
    def PositiveTest(self):
        Engine = SternmanEngine(True)
        self.assertTrue(Engine.needs_service())

    def NegativeTest(self):
        Engine = SternmanEngine(False)
        self.assertFalse(Engine.needs_service())