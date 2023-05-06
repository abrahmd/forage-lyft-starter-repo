from abc import abstractmethod

class Serviceable:
    @abstractmethod
    def needs_service() -> bool:
        pass