import unittest
from datetime import datetime

import sys
sys.path.insert(0,"..")

from car.car import Car

from engine.capuletengine import CapuletEngine
from engine.willoughbyengine import WilloughbyEngine
from engine.sternmanengine import SternmanEngine

from battery.spindlerbattery import SpindlerBattery
from battery.nubbinbattery import NubbinBattery


from tire.carrigan import CarriganTires
from tire.octoprime import OctoprimeTires

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        
        calliope = Car(battery, engine)
        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        calliope = Car(battery, engine)
        self.assertFalse(calliope.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        battery = SpindlerBattery(datetime.today().date(), last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        calliope = Car(battery, engine)
        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        battery = SpindlerBattery(datetime.today().date(), last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        calliope = Car(battery, engine)
        self.assertFalse(calliope.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        glissade = Car(battery, engine)
        self.assertTrue(glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        battery = SpindlerBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        glissade = Car(battery, engine)
        self.assertFalse(glissade.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        battery = SpindlerBattery(last_service_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        glissade = Car(battery, engine)
        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        battery = SpindlerBattery(last_service_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        glissade = Car(battery, engine)
        self.assertFalse(glissade.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        palindrome = Car(battery, engine)
        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        battery = SpindlerBattery(today, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        palindrome = Car(battery, engine)
        self.assertFalse(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        battery = SpindlerBattery(last_service_date, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        palindrome = Car(battery, engine)
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        battery = SpindlerBattery(last_service_date, last_service_date)
        engine = SternmanEngine(warning_light_is_on)

        palindrome = Car(battery, engine)
        self.assertFalse(palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        rorschach = Car(battery, engine)
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(today, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        rorschach = Car(battery, engine)
        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        rorschach = Car(battery, engine)
        self.assertTrue(rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        rorschach = Car(battery, engine)
        self.assertFalse(rorschach.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(today, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        thovex = Car(battery, engine)
        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        thovex = Car(battery, engine)
        self.assertFalse(thovex.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        thovex = Car(battery, engine)
        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        battery = NubbinBattery(last_service_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        thovex = Car(battery, engine)
        self.assertFalse(thovex.needs_service())

class TestTires(unittest.TestCase):
    def test_carrigan_tires_need_service(self):
        c = CarriganTires({0.1, 0.4, 0.9, 0.8})
        self.assertTrue(c.needs_service())
    
    def test_carrigan_tires_dont_need_service(self):
        c = CarriganTires({0.1, 0.4, 0.7, 0.8})
        self.assertFalse(c.needs_service())

    def test_octoprime_tires_need_service(self):
        o = OctoprimeTires({1.0, 0.4, 0.9, 0.8})
        self.assertTrue(o.needs_service())

    def test_octoprime_tires_dont_need_service(self):
        o = OctoprimeTires({1.0, 0.0, 0.9, 0.8})
        self.assertFalse(o.needs_service())




if __name__ == '__main__':
    unittest.main()
