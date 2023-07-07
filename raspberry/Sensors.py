from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_value(self):
        pass

class TemperatureSensor(Sensor):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def get_value(self):
        return self.temperature