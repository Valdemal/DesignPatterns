from abstract import Component, Mediator


class Button(Component):
    def click(self):
        self._mediator.notify(self, "click")


class Textbox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.content = ""


class Checkbox(Component):
    def __init__(self, mediator: Mediator, state: bool = False):
        super().__init__(mediator)
        self.state = state

    def check(self):
        self.state = not self.state
        self._mediator.notify(self, 'check')

