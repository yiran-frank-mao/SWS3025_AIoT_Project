import requests

from LightController import LightController
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from MicrobitCommunication import MicCom

def lightControllerTest():
    pir = PIRSensor()
    lightSensor = LightSensor()
    lightController = LightController(lightSensor, pir)
    lightController.led_on()
    lightController.set_led(1)
    # lightController.adjustTo(0.8)
    print(lightController.lightSensor.get_value())
    input("Press Enter to continue...")

def testMicrobit():
    micro = MicCom()

def PIRtest():
    light = LightController
    print(light.get_value())
    if light.get_value() == 0:
        light.dark()

if __name__ == '__main__':
    # lightControllerTest()
    # testMicrobit()
    PIRtest()