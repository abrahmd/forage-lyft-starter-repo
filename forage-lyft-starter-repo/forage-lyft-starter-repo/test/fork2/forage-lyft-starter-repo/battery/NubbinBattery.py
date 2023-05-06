from battery import Battery
from datetime import datetime, timedelta

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)

    def should_be_serviced(self):
        return self.current_date - self.last_service_date >= timedelta(years=4)