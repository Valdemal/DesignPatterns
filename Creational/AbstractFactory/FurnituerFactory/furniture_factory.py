from abc import ABC, abstractmethod

from FurnituerFactory.furniture import Chair, CoffeeTable

__all__ = ['FurnitureFactory']

class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> CoffeeTable:
        pass


