from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        #super().__init__(last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on