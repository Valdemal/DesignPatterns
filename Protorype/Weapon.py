from abc import ABC, abstractmethod


class Weapon(ABC):
    """Реализация шаблона "Прототип" """

    def __init__(self, damage: int, strength: int, name: str):
        self.__damage = damage
        self.__strength = strength
        self.__name = name

    @abstractmethod
    def clone(self) -> 'Weapon':
        pass

    @property
    def damage(self) -> int:
        return self.__damage

    @damage.setter
    def damage(self, value: int):
        self.__damage = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def strength(self) -> int:
        return self.__strength

    @strength.setter
    def strength(self, value: int):
        self.__strength = value


class MeleeWeapon(Weapon):
    def __init__(self, damage: int, strength: int, name: str):
        super().__init__(damage, strength, name)

    def clone(self) -> 'Weapon':
        return MeleeWeapon(self.damage, self.strength, self.name)


class Recharge:
    """Какой-то сложный класс с кучей полей"""
    

    def clone(self) -> 'Recharge':
        return Recharge()


class RangeWeapon(Weapon):
    def __init__(self, damage: int, strength: int, name: str, recharge: Recharge):
        super().__init__(damage, strength, name)
        self.__recharge = recharge

    def clone(self) -> 'Weapon':
        return RangeWeapon(self.damage, self.strength, self.name, self.__recharge.clone())
