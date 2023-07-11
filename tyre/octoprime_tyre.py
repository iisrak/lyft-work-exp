from tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, Tyres):
        self.Tyres = Tyres

    def needs_service(self) -> bool:
        return sum(self.Tyres) > 3.0