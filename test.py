import requests
import time
from LightController import LightController
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from MicrobitCommunication import MicCom



if __name__ == '__main__':
    mode = 'reading'
    lightController = LightController()
    i = 0

    #for i in range(15):
        #print('i =',i)
        #lightController.set_state(mode)
        #time.sleep(2)
    mode2 = 'computer'
    j = 0
    for j in range(15):
        print('j =',j)
        lightController.set_state(mode2)
        time.sleep(2)

    lightController.led_off()

    mode3 = 'night'
    k = 0
    for k in range(10):
        lightController.mode_thresd(mode3)