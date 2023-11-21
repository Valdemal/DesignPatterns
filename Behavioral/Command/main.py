from button import Button
from command import Command


class PrintCommand(Command):
    def __init__(self, printer: 'Printer', *args):
        self.__printer = printer
        self.__args = args

    def execute(self):
        self.__printer.print(*self.__args)


"""
Обычно команда не делает всю работу самостоятельно, а лишь передает вызов
получателю.

В ряде случаев, когда логика простая, ее можно оставить команде
"""


class Printer:
    """Получатель"""

    def print(self, filename: str, text: str):
        with open(filename, 'w') as file:
            file.write(text)


if __name__ == '__main__':
    """Клиент"""

    printer = Printer()
    command = PrintCommand(printer, "text3.txt", "Hello, its refactored printer.")
    button = Button("print button", command)
    button.click()
