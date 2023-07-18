import requests
import time

from Alarm import Alarm
from Controller import Controller
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from MicrobitCommunication import MicCom

if __name__ == '__main__':
    alarm = Alarm()
    time.sleep(10)
