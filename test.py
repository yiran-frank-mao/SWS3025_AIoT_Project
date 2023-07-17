#import requests
import time
from LightController import LightController
#from Sensors.CameraSensor import ImageSensor, VideoSensor
#from Sensors.LightSensor import LightSensor
#from Sensors.PIRSensor import PIRSensor
#from Sensors.TemperatureSensor import TemperatureSensor
#from MicrobitCommunication import MicCom



if __name__ == '__main__':
    mode = 'reading'
    lightController = LightController()
    i = 0

    for i in range(10):
        print('i =',i)
        lightController.set_state(mode)
        time.sleep(2)
