from tire.tire import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires_status):
        super().__init__(tires_status)

    def needs_service(self):
        sum = 0.0
        for tire in self.tires_status:
            sum += tire
        return sum >= 3.0