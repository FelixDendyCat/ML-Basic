from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self,
                 weight:int = 0, started:bool = False,
                 fuel:int = 0, fuel_consumption:int = 0):
        self._weight = weight
        self._started = started
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def start(self):
        if self._started == False:
            if self._fuel > 0:
                self._started = True
            else:
                raise LowFuelError

    def move(self, fuel_consumption:int):
        # возможно, подразумевается принять параметр distance,
        # а fuel_consumption = distance * _fuel_consumption
        if self._fuel >= fuel_consumption:
            self._fuel = self._fuel - fuel_consumption
        else:
            raise NotEnoughFuel