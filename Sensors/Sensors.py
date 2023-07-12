from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_value(self):
        pass