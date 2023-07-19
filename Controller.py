import time
from gpiozero import PWMLED

from Alarm import Alarm
from Sensors.CameraSensor import ImageSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from ModeDetector import ModeDetector
import numpy as np
import threading
from datetime import time as dtime
from datetime import datetime

from Buzz import Buzz


class Controller:
    def __init__(self, lightSensor: LightSensor, pirSensor: PIRSensor, imageSensor: ImageSensor,
                 modeDetector: ModeDetector, alarm: Alarm, buzzer: Buzz,
                 adjustFunc=np.sin, invAdjustFunc=np.arcsin, adjustDuration=0.5, adjustTotalSteps=15,
                 mode="reading",
                 ):
        self.lightSensor = lightSensor
        self.PIRSensor = pirSensor
        self.imageSensor = imageSensor
        self.modeDetector = modeDetector

        self.alarm = alarm
        self.led = PWMLED(21)
        self.buzzer = buzzer

        self.adjustFunc = adjustFunc
        self.invAdjustFunc = invAdjustFunc
        self.adjustDuration = adjustDuration
        self.adjustTotalSteps = adjustTotalSteps
        self.timerecord = time.time()
        self.mode = mode
        self.state = 'auto'

    def led_off(self):
        self.led.off()

    def led_on(self):
        self.led.on()

    def get_led(self):
        # return the value of led in [0,1]
        return self.led.value

    def set_led(self, value: float):
        self.led.value = value

    def set_mode(self, mode: str):
        self.mode = mode

    def adjustTo(self, targetBrightness):
        currentBrightness = self.get_led()
        if currentBrightness != targetBrightness:
            startX = self.invAdjustFunc(currentBrightness)
            # print('currentBrightness =', currentBrightness)
            endX = self.invAdjustFunc(targetBrightness)
            step = (endX - startX) / self.adjustTotalSteps
            for i in range(self.adjustTotalSteps):
                self.set_led(self.adjustFunc(startX + step * i))
                time.sleep(self.adjustDuration / self.adjustTotalSteps)

    def targetBrightness(self, mode: str) -> float:
        currentBrightness = self.get_led()
        # print('currentBrightness =', currentBrightness)
        currentLightIntensity = self.lightSensor.get_value()
        # print('currentLight =', currentLightIntensity)
        brightness = 0
        if mode == 'reading':
            targetLI1 = 0.2
            difference = currentLightIntensity - targetLI1
            # print('difference =', difference)
            if currentLightIntensity < 0:
                print('There is no need for the light.')
                brightness = 0
            elif 0.15 > currentLightIntensity >= 0:
                brightness = currentBrightness + 0.5 * difference
            elif 0.25 >= currentLightIntensity >= 0.15:
                brightness = currentBrightness
            elif 0.25 < currentLightIntensity < 0.5:
                brightness = currentBrightness + 1.2 * difference
            elif 0.5 <= currentLightIntensity <= 1:
                brightness = currentBrightness + 0.7 * difference

        elif mode == 'computer':
            targetLI2 = 0.4
            difference = currentLightIntensity - targetLI2
            # print('difference =', difference)
            if currentLightIntensity <= 0:
                print('There is no need for the light.')
                brightness = 0
            elif 0.2 > currentLightIntensity > 0:
                brightness = currentBrightness + 0.3 * difference
            elif 0.35 > currentLightIntensity >= 0.2:
                brightness = currentBrightness + 0.6 * difference
            elif 0.35 <= currentLightIntensity <= 0.45:
                brightness = currentBrightness
            elif 0.6 > currentLightIntensity > 0.45:
                brightness = currentBrightness + 0.8 * difference
            elif 1 >= currentLightIntensity >= 0.6:
                brightness = currentBrightness + 0.5 * difference
        elif mode == 'night':
            brightness = 0.2

        if brightness >= 1:
            print('Environment is too dark!')
            return 1
        elif 0 < brightness < 1:
            return brightness

        elif brightness <= 0:
            print('There is no need for the light.')
            return 0

    def capture_thread(self):
        self.imageSensor.capture("ml/images")
        timer_capture = threading.Timer(20, self.capture_thread)
        timer_capture.start()

    def detect_thread(self):
        if self.state == 'auto':
            pred, self.mode = self.modeDetector.detect_all(numerical_output=True)
            print("Detection result: ", pred, "Current mode changes to ", self.mode)
        timer_detect = threading.Timer(30, self.detect_thread)
        timer_detect.start()

    def mode_thread(self):
        if self.mode == 'night':
            if self.PIRSensor.get_value():
                self.set_led(0.2)
                time.sleep(10)
                self.led_off()
        elif self.mode == 'none':
            pass
        elif self.mode == 'reading':
            targetBrightness = self.targetBrightness(self.mode)
            self.adjustTo(targetBrightness)
        elif self.mode == 'computer':
            targetBrightness = self.targetBrightness(self.mode)
            self.adjustTo(targetBrightness)
        timer_mode = threading.Timer(30, self.mode_thread)
        timer_mode.start()

    # def sedentaryReminder_thread(self):

    def alarm_thread(self):
        time_now = datetime.now()
        if self.alarm.activated and \
                self.alarm.alarmTime.hour == time_now.hour and \
                self.alarm.alarmTime.minute == time_now.minute:
            self.buzzer.beep(2)
            self.alarm.clear()
        timer_alarm = threading.Timer(60, self.alarm_thread)
        timer_alarm.start()

    def start(self):
        timer_capture = threading.Timer(20, self.capture_thread)
        timer_detect = threading.Timer(30, self.detect_thread)
        timer_mode = threading.Timer(30, self.mode_thread)
        timer_alarm = threading.Timer(60, self.alarm_thread)

        timer_capture.start()
        timer_detect.start()
        timer_mode.start()
        timer_alarm.start()
