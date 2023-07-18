import time
from gpiozero import PWMLED
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from ModeDetector import ModeDetector
import numpy as np


class LightController:
    def __init__(self, lightSensor: LightSensor, pirSensor: PIRSensor, modeDetector: ModeDetector,
                 adjustFunc=np.sin, invAdjustFunc=np.arcsin, adjustDuration=0.5, adjustTotalSteps=15,
                 mode="night",
                 ):
        self.led = PWMLED(21)
        self.lightSensor = lightSensor
        self.PIRSensor = pirSensor
        self.adjustFunc = adjustFunc
        self.invAdjustFunc = invAdjustFunc
        self.adjustDuration = adjustDuration
        self.adjustTotalSteps = adjustTotalSteps
        self.mode = mode
        self.state = 'auto'
        self.modeDetector = modeDetector

    def led_off(self):
        self.led.off()

    def led_on(self):
        self.led.on()

    def get_led(self):
        # return the value of led in [0,1]
        return self.led.value

    def set_led(self, value):
        self.led.value = value

    def set_mode(self, mode):
        self.mode = mode

    def adjustTo(self, targetBrightness):
        currentBrightness = self.get_led()
        if currentBrightness != targetBrightness:
            startX = self.invAdjustFunc(currentBrightness)
            print('currentBrightness =', currentBrightness)
            endX = self.invAdjustFunc(targetBrightness)
            step = (endX - startX) / self.adjustTotalSteps
            for i in range(self.adjustTotalSteps):
                self.set_led(self.adjustFunc(startX + step * i))
                time.sleep(self.adjustDuration / self.adjustTotalSteps)

    def targetBrightness(self, mode: str) -> float:
        currentBrightness = self.get_led()
        print('currentBrightness =', currentBrightness)
        currentLightIntensity = self.lightSensor.get_value()
        print('currentLight =', currentLightIntensity)
        brightness = 0
        if mode == 'reading':
            targetLI1 = 0.25
            difference = currentLightIntensity - targetLI1
            print('difference =', difference)
            if currentLightIntensity < 0:
                print('There is no need for the light.')
                brightness = 0
            elif 0.2 > currentLightIntensity >= 0:
                brightness = currentBrightness + 0.5 * difference
            elif 0.3 >= currentLightIntensity >= 0.2:
                brightness = currentBrightness
            elif 0.3 < currentLightIntensity < 0.5:
                brightness = currentBrightness + 1.2 * difference
            elif 0.5 <= currentLightIntensity <= 1:
                brightness = currentBrightness + 0.7 * difference

        elif mode == 'computer':
            targetLI2 = 0.55
            difference = currentLightIntensity - targetLI2
            print('difference =', difference)
            if currentLightIntensity < 0:
                print('There is no need for the light.')
                brightness = 0
            elif 0.5 > currentLightIntensity >= 0:
                brightness = currentBrightness + 0.5 * difference
            elif 0.6 >= currentLightIntensity >= 0.5:
                brightness = currentBrightness
            elif 0.6 < currentLightIntensity < 0.8:
                brightness = currentBrightness + 1.2 * difference
            elif 0.8 <= currentLightIntensity <= 1:
                brightness = currentBrightness + 0.7 * difference
        elif mode == 'night':
            return 0.2

        if brightness > 1:
            print('Environment is too dark!')
            return 1
        elif brightness >= 0 and brightness <= 1:
            print('The targrtbrightness =', brightness)
            return brightness

        elif brightness < 0:
            print('There is no need for the light.')
            return 0

    def start(self):
        while True:
            if self.state == 'auto':
                self.mode = self.modeDetector.detect_batch()
                print("Current mode changes to ", self.mode)

            if self.mode == 'night':
                if self.PIRSensor.get_value():
                    self.set_led(0.2)
                    time.sleep(10)
            elif self.mode == 'none':
                pass
            elif self.mode == 'reading':
                targetBrightness = self.targetBrightness(self.mode)
                self.adjustTo(targetBrightness)
            elif self.mode == 'computer':
                targetBrightness = self.targetBrightness(self.mode)
                self.adjustTo(targetBrightness)
            time.sleep(1)
