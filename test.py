import requests
import time
from pathlib import Path
from tqdm import tqdm

# from Alarm import Alarm
# from Controller import Controller
# from Sensors.CameraSensor import ImageSensor, VideoSensor
# from Sensors.LightSensor import LightSensor
# from Sensors.PIRSensor import PIRSensor
# from Sensors.TemperatureSensor import TemperatureSensor
# from MicrobitCommunication import MicCom
# from Buzz import Buzz

if __name__ == '__main__':
    for item in tqdm(Path("ml/images").glob('*')):
        if item.is_file():
            item.unlink()