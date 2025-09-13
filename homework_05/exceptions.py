

class LowFuelError(Exception):
    def __init__(self):
        super().__init__("Low fuel")

class NotEnoughFuel(Exception):
    def __init__(self):
        super().__init__("Not enough fuel")

class CargoOverload(Exception):
    def __init__(self):
        super().__init__("Cargo overload")