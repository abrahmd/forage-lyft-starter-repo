from abc import ABC, abstractmethod
from serviceable import Serviceable

class Engine(Serviceable):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def should_be_serviced():
        pass