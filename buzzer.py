#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


class Buzzer(self):
    def __init__(self, name="Buzzer", pirSensorPin=27):
        super().__init__(name)
        self.pin = pirSensorPin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(BuzzerPin, GPIO.OUT)
        GPIO.output(BuzzerPin, GPIO.HIGH)

    def on(self):
        GPIO.output(BuzzerPin, GPIO.LOW)
        #低电平是响
    def off(self):
        GPIO.output(BuzzerPin, GPIO.HIGH)
         #高电平是停止响
    def beep(x):    #响3秒后停止3秒
        on()
        time.sleep(x)
        off()
        time.sleep(x)

    def loop(self):
        while True:
            beep(3)

    def destroy(self):
        GPIO.output(BuzzerPin, GPIO.HIGH)
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    a=Buzzer()
    try:
        a.loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        a.destroy()
