import time
from gpiozero import PWMLED

led = PWMLED(17) 
led.value = 0.5
led.on() # test - the led should be lit
time.sleep(1)
led.off() # test - the led should go off



