import RPi.GPIO as GPIO
import time

trig = 16


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.HIGH)
    pass


def beep(seconds):
    GPIO.output(trig, GPIO.LOW)
    time.sleep(seconds)
    GPIO.output(trig, GPIO.HIGH)


def beepBatch(seconds, timespan, counts):
    for i in range(counts):
        beep(seconds)
        time.sleep(timespan)


#init()
#beepBatch(0.2, 0.5, 2)
#GPIO.cleanup()