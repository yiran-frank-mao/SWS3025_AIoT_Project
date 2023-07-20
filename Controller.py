import time
from gpiozero import PWMLED

from Alarm import Alarm
from MicrobitCommunication import MicCom
from Sensors.CameraSensor import ImageSensor
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from ModeDetector import ModeDetector
import numpy as np
import threading
from datetime import time as dtime
from datetime import datetime, timedelta

from Buzz import Buzz


class Controller:
    def __init__(self, lightSensor: LightSensor, pirSensor: PIRSensor, imageSensor: ImageSensor,
                 modeDetector: ModeDetector, alarm: Alarm, buzzer: Buzz, microbit: MicCom,
                 adjustFunc=np.sin, invAdjustFunc=np.arcsin, adjustDuration=0.5, adjustTotalSteps=15,
                 mode="none"
                 ):
        self.lightSensor = lightSensor
        self.PIRSensor = pirSensor
        self.imageSensor = imageSensor
        self.modeDetector = modeDetector

        self.alarm = alarm
        self.led = PWMLED(21)
        self.buzzer = buzzer
        self.microbit = microbit

        self.adjustFunc = adjustFunc
        self.invAdjustFunc = invAdjustFunc
        self.adjustDuration = adjustDuration
        self.adjustTotalSteps = adjustTotalSteps
        self.timeRecord = datetime.now()
        self.sedentaryReminder = True
        self.mode = mode  # 'reading', 'computer', 'manual', 'night'
        self.state = 'auto'  # 'auto', 'manual', 'off'

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
            endX = self.invAdjustFunc(targetBrightness)
            step = (endX - startX) / self.adjustTotalSteps
            for i in range(self.adjustTotalSteps):
                self.set_led(self.adjustFunc(startX + step * i))
                time.sleep(self.adjustDuration / self.adjustTotalSteps)

    def targetBrightness(self, mode: str) -> float:
        currentBrightness = self.get_led()
        currentLightIntensity = self.lightSensor.get_value()
        brightness = 0
        if mode == 'reading':
            # targetLI1 = 0.2
            # difference = currentLightIntensity - targetLI1
            # # print('difference =', difference)
            # if currentLightIntensity < 0:
            #     print('No need for light.')
            #     brightness = 0
            # elif 0.15 > currentLightIntensity >= 0:
            #     brightness = 0.9
            # elif 0.25 >= currentLightIntensity >= 0.15:
            #     brightness = 0.75
            # elif 0.25 < currentLightIntensity < 0.3:
            #     brightness = currentBrightness + 1.2 * difference
            # elif 0.3 <= currentLightIntensity <= 0.4:
            #     brightness = currentBrightness + difference
            # elif 0.4 < currentLightIntensity < 0.5:
            #     brightness = currentBrightness + 0.8 * difference
            # elif 0.5 <= currentLightIntensity <= 0.7:
            #     brightness = currentBrightness + 0.5 * difference
            # elif 0.7 <= currentLightIntensity <= 1:
            #     brightness = currentBrightness + 0.3 * difference
            brightness = min(0.9, 0.5 + 0.5 * currentLightIntensity)

        elif mode == 'computer':
            # targetLI2 = 0.38
            # difference = currentLightIntensity - targetLI2
            # # print('difference =', difference)
            # if currentLightIntensity <= 0:
            #     print('No need for light.')
            #     brightness = 0
            # elif 0.2 > currentLightIntensity > 0:
            #     brightness = currentBrightness + 0.3 * difference
            # elif 0.32 > currentLightIntensity >= 0.2:
            #     brightness = currentBrightness + 0.6 * difference
            # elif 0.32 <= currentLightIntensity <= 0.4:
            #     brightness = currentBrightness
            # elif 0.5 > currentLightIntensity > 0.4:
            #     brightness = currentBrightness + difference
            # elif 0.6 > currentLightIntensity >= 0.5:
            #     brightness = currentBrightness + 0.8 * difference
            # elif 1 >= currentLightIntensity >= 0.6:
            #     brightness = currentBrightness + 0.35 * difference
            brightness = min(0.45, 0.3 + 0.5 * currentLightIntensity)
        if brightness >= 1:
            print('Environment is too dark!')
            return 1
        elif 0 < brightness < 1:
            return brightness

        elif brightness <= 0:
            print('No need for light.')
            return 0

    def capture_thread(self):
        self.imageSensor.capture("ml/images")
        timer_capture = threading.Timer(20, self.capture_thread)
        timer_capture.start()

    def detect_thread(self):
        if self.state == 'auto':
            self.modeDetector.detect_new()
            newMode = self.modeDetector.get_detection()
            if newMode == "none":
                if self.lightSensor.get_value() > 0.8:
                    self.mode = "night"
                else:
                    self.mode = "manual"
            elif newMode == "any":
                pass
            else:
                self.mode = newMode
                print("Current mode changes to ", self.mode)
                self.modeDetector.clear()
        timer_detect = threading.Timer(10, self.detect_thread)
        timer_detect.start()

    def mode_thread(self):
        if self.state == 'off':
            print("off")
            self.led_off()
            self.timeRecord = datetime.now()
        elif self.state == 'manual':
            print("Manual state:", self.mode, "mode")
            self.timeRecord = datetime.now()
        else:
            if self.mode == 'night':
                self.timeRecord = datetime.now()
                self.led_off()
                if self.PIRSensor.get_value():
                    print(self.mode, "mode: ***Someone is detected***")
                    self.set_led(0.2)
                    time.sleep(10)
                    self.led_off()
                else:
                    print(self.mode, "mode")
            elif self.mode == 'reading' or self.mode == 'computer':
                if self.sedentaryReminder and datetime.now() - self.timeRecord > timedelta(minutes=40):
                    self.buzzer.beep(2)
                    print("Time to have rest!")
                    self.timeRecord = datetime.now()
                targetBrightness = self.targetBrightness(self.mode)
                print(self.mode, "mode: adjusting to", targetBrightness, "...")
                self.adjustTo(targetBrightness)
            elif self.mode == 'manual':
                print("Manual mode")
                self.timeRecord = datetime.now()
        timer_mode = threading.Timer(0.5, self.mode_thread)
        timer_mode.start()

    def alarm_thread(self):
        time_now = datetime.now()
        if self.alarm.activated and \
                self.alarm.alarmTime.hour == time_now.hour and \
                self.alarm.alarmTime.minute == time_now.minute:
            print("******** alarm: Time over ********")
            self.buzzer.beep(2)
            self.alarm.clear()
        timer_alarm = threading.Timer(60, self.alarm_thread)
        timer_alarm.start()

    def microbit_thread(self):
        while True:
            if self.microbit.button_pressed():
                print("******** microbit: Button pressed ********")
                self.mode = 'manual'
                if self.get_led() > 0:
                    self.led_off()
                else:
                    self.led_on()

    def start(self):
        timer_capture = threading.Timer(25, self.capture_thread)
        timer_detect = threading.Thread(target=self.detect_thread)
        timer_mode = threading.Thread(target=self.mode_thread)
        timer_alarm = threading.Thread(target=self.alarm_thread)
        microbit_thread = threading.Thread(target=self.microbit_thread)

        timer_capture.start()
        timer_detect.start()
        timer_mode.start()
        timer_alarm.start()
        microbit_thread.start()
