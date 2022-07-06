from FurnituerFactory.furniture import Chair, CoffeeTable

__all__ = ['VictorianChair', 'VictorianCoffeeTable']


class VictorianChair(Chair):

    def has_legs(self):
        print("Have victorian legs")

    def sit_on(self):
        print("You sit down on victorian chair")


class VictorianCoffeeTable(CoffeeTable):
    def stand(self):
        print("Victorian table stands")
