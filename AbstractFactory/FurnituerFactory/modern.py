from FurnituerFactory.furniture import Chair, CoffeeTable

__all__ = ['ModernChair', 'ModernCoffeeTable']


class ModernChair(Chair):

    def sit_on(self):
        print("You sit down on modern chair.")

    def has_legs(self):
        print("Has a modern legs.")


class ModernCoffeeTable(CoffeeTable):

    def stand(self):
        print("Modern table stands.")
