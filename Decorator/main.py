from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier = None):
        self.__wrapped = wrapped

    def send(self, message):
        if self.__wrapped is not None:
            self.__wrapped.send(message)


class EmailNotifier(NotifierDecorator):
    def __init__(self, email: str, wrapped: Notifier = None):
        super().__init__(wrapped)
        self.__email = email

    def send(self, message):
        super().send(message)
        self.__send_on_email(message)

    def __send_on_email(self, message: str):
        print(f'{message} отправлено на email:{self.__email}')


class VKNotifier(NotifierDecorator):
    def __init__(self, user_id: int, wrapped: Notifier = None):
        super().__init__(wrapped)
        self.__id = user_id

    def send(self, message):
        super().send(message)
        self.__send_on_vk(message)

    def __send_on_vk(self, message: str):
        print(f'Сообщение: {message} отправлено по VK пользователю с id:{self.__id}')


class SMSNotifier(NotifierDecorator):
    def __init__(self, phone_number: str, wrapped: Notifier = None):
        super(SMSNotifier, self).__init__(wrapped)
        self.__phone_number = phone_number

    def send(self, message):
        super().send(message)
        self.__send_on_phone(message)

    def __send_on_phone(self, message):
        print(f"Сообщение: {message} отправлено на номер телефона: {self.__phone_number}")


if __name__ == '__main__':
    vk_and_sms_notifier = VKNotifier(12, SMSNotifier("89205894983"))
    vk_and_sms_notifier.send("Здравствуйте, Владимир!")

    print("Усовершенствование...")
    email_vk_and_sms_notifier = EmailNotifier('vovanex12@gmail.com', vk_and_sms_notifier)
    email_vk_and_sms_notifier.send('Вам поступило уникальное предложение')
