import math
from abc import ABC, abstractmethod
from typing import List


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Picture(Drawable):
    def __init__(self):
        self.__components: List[Drawable] = []

    @property
    def components(self) -> List[Drawable]:
        return self.__components

    @components.setter
    def components(self, value: List[Drawable]):
        self.__components = value

    def draw(self):
        print('Отрисовка картинки:')
        for component in self.__components:
            component.draw()


class Figure(Drawable, ABC):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @abstractmethod
    def get_square(self) -> float:
        pass

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @x.setter
    def x(self, value: float):
        self.__x = value

    @y.setter
    def y(self, value: float):
        self.__y = value


class Rectangle(Figure):
    def __init__(self, x: float, y: float, a: float, b: float):
        super().__init__(x, y)
        self.__a = a
        self.__b = b

    def get_square(self) -> float:
        return self.a * self.b

    @property
    def a(self) -> float:
        return self.__a

    @property
    def b(self) -> float:
        return self.__b

    def draw(self):
        print(f'Отрисовывается прямоугольник со размера {self.__a} на {self.__b} в точке ({self.x}, {self.y})')


class Cicle(Figure):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.__radius = radius

    def draw(self):
        print(f'Отрисовывается окружность с радиусом {self.__radius} в точке ({self.x}, {self.y})')

    def get_square(self) -> float:
        return math.pi * self.__radius ** 2


class Square(Rectangle):

    def __init__(self, x: float, y: float, a: float):
        super().__init__(x, y, a, a)

    def draw(self):
        print(f'Отрисовывается квадрат со стороной {self.a} в точке ({self.x}, {self.y})')


if __name__ == '__main__':
    picture = Picture()
    picture.components = [Square(1, 2, 3), Rectangle(3, 4, 3, 5), Cicle(0, 0, 4)]

    bigger_picture = Picture()
    bigger_picture.components = [Cicle(5, 5, 5), picture]

    bigger_picture.draw()
