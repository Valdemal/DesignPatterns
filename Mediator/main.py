from Mediator.abstract import Mediator, Component

from components import Button, Textbox, Checkbox


class AuthenticationForm(Mediator):
    def __init__(self):
        self.login = Textbox(self)
        self.password = Textbox(self)
        self.ok = Button(self)
        self.cancel = Button(self)
        self.remember_me = Checkbox(self)

    def notify(self, sender: Component, event: str):
        if sender == self.cancel and event == 'click':
            print("Переадресация на главную страницу")
            return

        if sender == self.ok and event == 'click':
            print("Отправка данных")
            print("Логин:", self.login.content)
            print("Пароль:", self.password.content)

            if self.remember_me.state:
                print("Запись данных в cookie")


if __name__ == '__main__':
    form = AuthenticationForm()

    # заполнение формы
    form.login.content = 'vovan'
    form.password.content = '12345'
    form.remember_me.check()

    form.ok.click()
