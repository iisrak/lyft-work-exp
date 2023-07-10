from engine import Engine
from battery import Battery

class Car():
    def __init__(self, engine: Engine, battery: Battery):
        self.Engine = engine
        self.Battery = battery

    def needs_service(self) -> bool:
        return self.Engine.needs_service() or self.Battery.needs_service()