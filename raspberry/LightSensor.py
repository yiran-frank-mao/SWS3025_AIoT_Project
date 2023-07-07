from Sensors import Sensor

class LightSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def get_value(self):
        #TODO: Implement this method
        raise NotImplementedError