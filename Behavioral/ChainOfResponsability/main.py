from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence


@dataclass
class Request:
    data: str
    login: str
    password: str


@dataclass
class Response:
    text: str
    code: int

    def __str__(self):
        return f"{self.code} {self.text}"


class Handler(ABC):
    @abstractmethod
    def set_hext(self, handler: 'Handler'):
        pass

    @abstractmethod
    def handle(self, request: Request) -> Response or None:
        pass


class BaseHandler(Handler):
    def __init__(self):
        self.__next: Handler = None

    def set_hext(self, handler: 'Handler') -> Response or None:
        self.__next = handler

    def handle(self, request: Request):
        if self.__next is not None:
            return self.__next.handle(request)

    @staticmethod
    def make_chain(handlers: Sequence[Handler]) -> Handler:
        res = current = BaseHandler()

        for handler in handlers:
            current.set_hext(handler)
            current = current.__next

        return res


class Authentication(BaseHandler):
    def handle(self, request: Request) -> Response or None:
        print('Аутентификация')
        if request.login != 'admin' or request.password != '12345':
            return Response('Forbidden', 403)

        return super().handle(request)


class Validation(BaseHandler):
    def handle(self, request: Request):
        print('Валидация')
        if len(request.data) > 10:
            return Response('Bad Request', 400)

        return super().handle(request)


class Caching(BaseHandler):
    def __init__(self):
        super().__init__()
        self.__cache = []

    def handle(self, request: Request):
        print('Кеширование')
        self.__cache.append(request.data)
        return super().handle(request)


class Processor(BaseHandler):
    def handle(self, request: Request):
        print('Обработка')
        return Response('OK', 200)


if __name__ == '__main__':
    authentication = Authentication()
    validation = Validation()
    caching = Caching()
    processor = Processor()

    # authentication.set_hext(validation)
    # validation.set_hext(caching)
    # caching.set_hext(processor)
    chain = BaseHandler.make_chain((authentication, validation, caching, processor))

    request = Request('dat124asadsd', 'admin', '12345')
    response = authentication.handle(request)

    print(response)


