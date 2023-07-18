import time
from gpiozero import PWMLED

class Buzzer:
    def __init__(self):
        self.led = PWMLED(27)
    def led_off(self):
        self.led.off()

    def led_on(self):
        self.led.on()