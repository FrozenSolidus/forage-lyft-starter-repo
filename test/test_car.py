import unittest
from datetime import datetime
import sys
from pathlib import Path

# Get the current script's directory
script_dir = Path(__file__).resolve().parent

# Get the project's root directory by going up one level
project_dir = script_dir.parent

# Add the project's root directory to the Python path
sys.path.append(str(project_dir))

# Now you can use relative imports
from CarFactory import CarFactory
    
class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0, 0, 0, 0]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0, 0, 0, 0]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [1, 0.8, 0.4, 0.5]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0, 0, 0.89, 0.3]
        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.5, 0.91, 1, 0.9]
        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires = [0.5, 0.1, 0.89, 0.1]
        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tires)
        self.assertFalse(car.needs_service()) 


if __name__ == '__main__':
    unittest.main()
