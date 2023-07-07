from Sensors import Sensor
class TemperatureSensor(Sensor):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def get_value(self):
        return self.temperature