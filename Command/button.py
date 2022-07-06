from command import Command


class Button:
    """Отправитель"""
    def __init__(self, text: str, command: Command = None):
        self.__text = text
        self.__command = command

    def set_command(self, command: Command):
        self.__command = command

    def click(self):
        self.__command.execute()
