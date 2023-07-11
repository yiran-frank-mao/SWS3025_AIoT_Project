from Sensors.Sensors import Sensor
import Adafruit_DHT

class TemperatureSensor(Sensor):
    def __init__(self, name="DHT11", GPIO_Pin=17):
        super().__init__(name)
        self.sensor_type = Adafruit_DHT.DHT11
        self.pin = GPIO_Pin

    def get_value(self) -> (float, float):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
        return temperature, humidity

def TemperatureSensor_test():
    sensor = TemperatureSensor("DHT11")
    temperature, humidity = sensor.get_value()
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

TemperatureSensor_test()