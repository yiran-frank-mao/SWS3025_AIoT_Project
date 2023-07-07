from Sensors import Sensor

class PIRSensor(Sensor):
    def __init__(self, name, motion):
        super().__init__(name)

    def get_value(self):
        #TODO: Implement this method
        raise NotImplementedError