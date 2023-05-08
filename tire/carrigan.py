from tire.tire import Tires

class CarriganTires(Tires):
    def __init__(self, tires_status):
        super().__init__(tires_status)

    def needs_service(self):
        for tire in self.tires_status:
            if tire >= 0.9:
                return True
        return False