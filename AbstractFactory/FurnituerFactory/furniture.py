from abc import ABC, abstractmethod

__all__ = ['Chair', 'CoffeeTable']


class Chair(ABC):

    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class CoffeeTable(ABC):

    @abstractmethod
    def stand(self):
        pass

