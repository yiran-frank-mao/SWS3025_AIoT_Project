#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Buzzer = 25    # pin25

def setup(pin):
    global BuzzerPin
    BuzzerPin = pin
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
    GPIO.output(BuzzerPin, GPIO.LOW)
    #低电平是响
def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    #高电平是停止响
def beep(x):    #响3秒后停止3秒
    on()
    time.sleep(x)
    off()
    time.sleep(x)

def loop():
    while True:
        beep(3)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup(Buzzer)
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()