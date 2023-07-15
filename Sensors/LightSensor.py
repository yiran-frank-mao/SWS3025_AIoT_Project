from Sensors.Sensors import Sensor
from gpiozero import MCP3008


class LightSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)
        self.lightSensor = MCP3008(0)

    def get_value(self) -> float:
        # Returns a value in (0, 1) representing the light intensity
        return self.lightSensor.value
