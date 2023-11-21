from abc import abstractmethod, ABC
from typing import Dict


class EventListener(ABC):
    """Подписчик"""
    @abstractmethod
    def update(self, filename: str):
        pass


class EmailAlertListener(EventListener):
    def __init__(self, email: str, message: str):
        self.__email = email
        self.__message = message

    def update(self, filename: str):
        print("Отправка на", self.__email)
        print(self.__message.replace('%s', filename))


class LoggingListener(EventListener):
    def __init__(self, log_filename: str, message: str):
        self.__log = log_filename
        self.__message = message

    def update(self, filename: str):
        print("Логирование в", self.__log)
        print(self.__message.replace('%s', filename))


class EventManager:
    """Издатель"""
    def __init__(self):
        self.__listeners: Dict[str, EventListener] = {}

    def subscribe(self, event_type: str, listener: EventListener):
        self.__listeners[event_type] = listener

    def unsubscribe(self, event_type: str):
        self.__listeners.pop(event_type)

    def notify(self, event_type: str, data):
        self.__listeners[event_type].update(data)


class Editor:
    """Клиент"""
    def __init__(self):
        self.events = EventManager()
        self.__filename = None

    def open_file(self, filename: str):
        print('Открытие файла')
        self.__filename = filename
        self.events.notify('open', filename)

    def save_file(self):
        print('Сохранение файла')
        self.events.notify('save', self.__filename)


if __name__ == '__main__':
    editor = Editor()

    logger = LoggingListener("log.txt", "Someone has opened file: %s")
    editor.events.subscribe("open", logger)

    email_alerts = EmailAlertListener("vovanex12@gmail.com", "Someone has changed the file: %s")
    editor.events.subscribe("save", email_alerts)

    editor.open_file("file.txt")
    editor.save_file()
