from abc import ABC, abstractmethod
from LightController import LightController


class Mode(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def run(self, lightController: LightController):
        pass


class ManualMode(Mode):
    def __init__(self, name="manual"):
        super().__init__(name)

    def run(self, lightController: LightController):
        print("Running at Manual Mode ...")


class ComputerMode(Mode):
    def __init__(self, name):
        super().__init__(name)

    def run(self, lightController: LightController):
        print("Running at Computer Mode ...")
