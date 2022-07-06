from FurnituerFactory import ModernCoffeeTable, ModernChair
from FurnituerFactory.furniture import Chair, CoffeeTable
from FurnituerFactory.furniture_factory import FurnitureFactory

__all__ = ['ModernFactory']


class ModernFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> CoffeeTable:
        return ModernCoffeeTable()
