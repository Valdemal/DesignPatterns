from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: 'Component', event: str):
        pass


class Component(ABC):
    def __init__(self, mediator: Mediator):
        self._mediator = mediator

