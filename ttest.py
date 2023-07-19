import requests
import time
from pathlib import Path
from tqdm import tqdm

from Alarm import Alarm
from Controller import Controller
from ModeDetector import ModeDetector
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from MicrobitCommunication import MicCom
from Buzz import Buzz

if __name__ == '__main__':
    image_sensor = ImageSensor("Image")
    video_sensor = VideoSensor("Video")
    temperature_sensor = TemperatureSensor()
    pir = PIRSensor()
    buzz = Buzz()
    alarm = Alarm()
    microbit = MicCom()
    lightSensor = LightSensor()
    modeDetector = ModeDetector(skipInit=True)

    controller = Controller(
        lightSensor=lightSensor,
        pirSensor=pir,
        imageSensor=image_sensor,
        modeDetector=modeDetector,
        alarm=alarm,
        buzzer=buzz,
        microbit=microbit)

    controller.led_off()
    for i in range(10):
        target = controller.targetBrightness('reading')
        current = controller.get_led()
        print('currentBrightness1',current)  #调整之前led光

        currentLightIntensity = lightSensor.get_value()
        print('currentLightIntensity1 = ', currentLightIntensity)  #在调整之前的室内光强
        print('targetBrightness =',target)   #目标光强

        controller.adjustTo(target)
        current = controller.get_led()
        print('currentBrightness2 =', current)  #调整后得到的led光

        currentLightIntensity = lightSensor.get_value()
        print('currentLightIntensity = ',currentLightIntensity) #调整后的室内光强
    input("Press Enter to continue...")
