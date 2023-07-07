from Sensors import Sensor

class LightSensor(Sensor):
    def __init__(self, name, light):
        super().__init__(name)
        self.light = light

    def get_value(self):
        return self.light