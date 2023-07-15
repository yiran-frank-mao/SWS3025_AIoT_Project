import requests

from LightController import LightController
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor


def lightControllerTest():
    pir = PIRSensor()
    lightSensor = LightSensor()
    lightController = LightController(lightSensor, pir)
    lightController.led_off()
    # lightController.set_led(0.2)
    # lightController.adjustTo(0.8)
    print(lightController.lightSensor.get_value())
    input("Press Enter to continue...")


if __name__ == '__main__':
    lightControllerTest()