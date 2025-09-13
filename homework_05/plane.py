from homework_05.exceptions import CargoOverload
from homework_05.base import Vehicle


class Plane(Vehicle):
    def __init__(self, max_cargo:int):
        super().__init__()
        self._max_cargo = max_cargo
        self._cargo = 0

    def load_cargo(self, cargo:int):
        if self._max_cargo >= self._cargo + cargo:
            self._cargo = self._cargo + cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self)->int:
        result = self._cargo
        self._cargo = 0
        return result