import RPi.GPIO as GPIO
import time


class Buzz:
    def __init__(self, trig=16):
        self.trig = trig
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig, GPIO.OUT, initial=GPIO.HIGH)

    def beep(self, seconds):
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(seconds)
        GPIO.output(self.trig, GPIO.HIGH)

    def beepBatch(self, seconds, timespan, counts):
        for i in range(counts):
            self.beep(seconds)
            time.sleep(timespan)
