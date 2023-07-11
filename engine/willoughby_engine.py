from engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        #super().__init__(last_service_date)
        self.mileage = current_mileage - last_service_mileage

    def needs_service(self) -> bool:
        return self.mileage > 60000