from battery import NubbinBattery, SpindlerBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from car import Car

class CarFactory():
    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    def create_glissage(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_is_on)
        return Car(battery, engine)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)


