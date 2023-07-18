#!/usr/bin/python
# encoding:utf-8
import RPi.GPIO as GPIO
import time

trig = 27


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


init()
# beep(0.1)
beepBatch(0.2, 0.5, 30)

GPIO.cleanup()