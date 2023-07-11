from battery.spindler_battery import SpindlerBattery
from datetime import *
import unittest

class SpindlerBatteryTest(unittest.TestCase):
    def __init__(self):
        self.current_date = datetime.today().date()
        self.positive_service_date = current_date.replace(year=current_date.year - 3)
        self.negative_service_date = current_date.replace(year=current_date.year - 1)

    def PositiveTest(self):
        Battery = SpindlerBattery(current_date, positive_service_date)
        self.assertTrue(Battery.needs_service())
    
    def NegativeTest(self):
        Battery = SpindlerBattery(current_date, negative_service_date)
        self.assertFalse(Battery.needs_service())