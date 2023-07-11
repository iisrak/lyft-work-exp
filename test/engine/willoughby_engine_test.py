from engine.willoughby_engine import WilloughbyEngine
import unittest

class WilloughbyEngineTest(unittest.TestCase):
     def __init__(self):
        self.positive_mileage = 60001
        self.negative_mileage = 60000
        self.last_service_mileage = 0

    def PositiveTest(self):
        Engine = CapuletEngine(self.positive_mileage, self.last_service_mileage)
        self.assertTrue(Engine.needs_service())

    def test_needs_service_false(self):
        Engine = CapuletEngine(self.negative_mileage, self.last_service_mileage)
        self.assertFalse(Engine.needs_service())