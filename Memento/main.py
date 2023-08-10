from typing import List


class Originator:
    def __init__(self):
        self.__state = "Состояние"

    class Memento:
        def __init__(self, state):
            self.__state = state

        @property
        def state(self):
            return self.__state

    def save(self) -> Memento:
        return self.Memento(self.__state)

    def restore(self, memento: Memento):
        self.__state = memento.state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state


class Caretaker:
    def __init__(self, originator: Originator):
        self.__originator = originator
        self.__history: List[Originator.Memento] = []

    def undo(self):
        if len(self.__history) == 0:
            return

        memento = self.__history.pop()
        self.__originator.restore(memento)

    def do_something(self):
        self.__history.append(self.__originator.save())


if __name__ == '__main__':
    originator = Originator()
    caretaker = Caretaker(originator)

    caretaker.do_something()
    print(originator.state)

    originator.state = "Состояние2"
    print(originator.state)

    caretaker.undo()
    print(originator.state)

