from abc import ABC, abstractmethod
from Person import Person
from ClosedClass import Service


class AdapterInterface(ABC):
    @abstractmethod
    def parse(self, person: Person):
        pass


class AggregatedAdapter(AdapterInterface):
    def __init__(self, service: Service):
        self.__service = service

    def parse(self, person: Person):
        self.__service.method(f"{person.name} {person.surname} {person.age}")


class GeneralizedAdapter(AdapterInterface, Service):
    def parse(self, person: Person):
        super().method(f"{person.name} {person.surname} {person.age}")
