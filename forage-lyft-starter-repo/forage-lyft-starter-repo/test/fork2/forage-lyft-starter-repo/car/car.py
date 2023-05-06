from abc import ABC, abstractmethod
from serviceable import Serviceable

class Car(ABC, Serviceable):
    def __init__(self, battery, engine):
         self.battery = battery
         self.engine = engine

    def needs_service(self):
        return self.battery.should_be_serviced() or self.engine.should_be_serviced()
