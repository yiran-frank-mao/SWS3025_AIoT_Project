import time
from gpiozero import PWMLED
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
import numpy as np


class LightController:
    def __init__(self, lightSensor: LightSensor = LightSensor("lightSensor"),
                 pirSensor: PIRSensor = PIRSensor("PIRSensor"), adjustFunc=np.sin,
                 invAdjustFunc=np.arcsin, adjustDuration=0.5, adjustTotalSteps=15):
        self.led = PWMLED(21)
        self.lightSensor = lightSensor
        self.PIRSensor = pirSensor
        self.adjustFunc = adjustFunc
        self.invAdjustFunc = invAdjustFunc
        self.adjustDuration = adjustDuration
        self.adjustTotalSteps = adjustTotalSteps

    def led_off(self):
        self.led.off()

    def led_on(self):
        self.led.on()

    def get_led(self):
        # return the value of led in [0,1]
        return self.led.value

    def set_led(self, value):
        self.led.value = value

    def set_state(self, mode):
        if mode == 'manual':  # 手动模式
            self.led.value = 0.8  # 默认亮度
            self.led.on()
        elif mode == 'reading':  # 阅读模式
            #self.led.value = 0.8  # 默认亮度
            #self.led.on()
            #targetBrightness = self.targetBrightness(mode)
            targetBrightness = 0.25
            print('targetbright =',targetBrightness)
            #i = 0
            #while (i < 100):
            self.adjustTo(targetBrightness)
                #i = i + 1
        elif mode == 'computer':  # 电脑模式
            self.led.value = 0.8  # 默认亮度
            self.led.on()
            targetBrightness = 0.02
            i = 0
            while (i < 100):
                self.adjustTo(targetBrightness)
                i = i + 1

    def adjustTo(self, targetBrightness):
        currentBrightness = self.get_led()
        if currentBrightness != targetBrightness:
            startX = self.invAdjustFunc(currentBrightness)
            endX = self.invAdjustFunc(targetBrightness)
            step = (endX - startX) / self.adjustTotalSteps
            for i in range(self.adjustTotalSteps):
                self.set_led(self.adjustFunc(startX + step * i))
                time.sleep(self.adjustDuration / self.adjustTotalSteps)

    def targetBrightness(self, mode: str) -> float:
        currentBrightness = self.get_led()
        print('currentBrightness =',currentBrightness)
        currentLightIntensity = self.lightSensor.get_value()
        print('currentLight =', currentLightIntensity)
        brightness = 0
        if mode == 'reading':
            targetLI1 = 0.25
            difference =  currentLightIntensity - targetLI1
            print('difference =',difference)
            if currentLightIntensity < 0:
                print('There is no need for the light.')
                brightness = 0
            elif currentLightIntensity < 0.2 and currentLightIntensity>=0:
                brightness = currentBrightness+0.2*difference
            elif currentLightIntensity <= 0.3 and currentLightIntensity >= 0.2 :
                brightness = currentBrightness
            elif currentLightIntensity >0.3 and currentLightIntensity <0.5:
                brightness = currentBrightness+0.5*difference
            elif currentLightIntensity >=0.5 and currentLightIntensity <=1:
                brightness = currentBrightness+0.7*difference


        elif mode == 'computer':
            targetLI2 = 0.65
            if currentLightIntensity < 0.6:
                brightness = currentBrightness - 0.5*(targetLI2 - currentLightIntensity)
            elif currentLightIntensity >=0.6 and currentLightIntensity <= 0.7:
                brightness = currentBrightness
            elif currentLightIntensity > 0.7 :
                brightness = currentBrightness + 0.5*(currentLightIntensity-targetLI2)

        elif mode == 'night':
            return 0.2

        if brightness>=0 and brightness<=1:
            return brightness
        else:
            print('There is no need for the light.')
            return 0



    def night_light_mode(self):
        if self.PIRSensor.get_value():
            self.set_led(0.2)
            time.sleep(10)

    def start(self):
        while True:
            self.night_light_mode()
            time.sleep(1)
