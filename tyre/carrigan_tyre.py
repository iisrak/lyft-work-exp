from tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, Tyres):
        self.Tyres = Tyres

    def needs_service(self) -> bool:
        return any(x >= 0.9 for x in self.Tyres)