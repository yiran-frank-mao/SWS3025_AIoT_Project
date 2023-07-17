from Sensors.Sensors import Sensor
import RPi.GPIO as GPIO


class PIRSensor(Sensor):
    def __init__(self, name="PIR", pirSensorPin=12):
        super().__init__(name)
        self.pin = pirSensorPin
        GPIO.setmode(GPIO.BCM)

    def get_value(self) -> bool:
        # Returns true if motion is detected, false otherwise
        GPIO.setup(self.pin, GPIO.IN)
        rtn = GPIO.input(self.pin)
        return rtn


def PIRTest():
    pir = PIRSensor("PIR", 12)
    while True:
        print(pir.get_value())
