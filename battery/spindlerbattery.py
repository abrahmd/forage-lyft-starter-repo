from battery.battery import Battery
from datetime import timedelta

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)

    def needs_service(self):
        return self.current_date - self.last_service_date >= timedelta(days=730) #2 years
    
