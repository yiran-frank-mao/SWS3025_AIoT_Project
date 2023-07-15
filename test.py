import requests
import time
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

# def PIRtest():
#     light = LightController()
#     print(light.get_led())
#     if light.get_led() == 0:
#         light.dark()
def PIRTest():
    pir = PIRSensor()
    lightSensor = LightSensor()
    lightController = LightController(lightSensor, pir)
    while True:
        if lightController.PIRSensor.get_value() == 1:
            lightController.led_on()
            print(lightController.get_led())
            input("Press Enter to continue...")



if __name__ == '__main__':
   #lightControllerTest()
    # testMicrobit()
    PIRTest()
