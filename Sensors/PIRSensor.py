from Sensors import Sensor
import RPi.GPIO as GPIO

class PIRSensor(Sensor):
    def __init__(self, name, pirSensorPin):
        super().__init__(name)
        self.pin = pirSensorPin

    def get_value(self) -> bool:
        # Returns true if motion is detected, false otherwise
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        rtn = GPIO.input(self.pin)
        GPIO.cleanup()
        return rtn

def PIRTest():
    pir = PIRSensor("PIR", 12)
    while True:
        print(pir.get_value())

if __name__ == "__main__":
    PIRTest()