

from abc import abstractmethod

class Tires():
    @abstractmethod
    def __init__(self, tires_status):
        self.tires_status = tires_status

    @abstractmethod
    def needs_service(self):
        pass