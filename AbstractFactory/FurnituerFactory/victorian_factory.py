from FurnituerFactory.furniture import Chair, CoffeeTable
from FurnituerFactory.furniture_factory import FurnitureFactory
from .victorian import VictorianChair, VictorianCoffeeTable

__all__ = ['VictorianFactory']

class VictorianFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()
