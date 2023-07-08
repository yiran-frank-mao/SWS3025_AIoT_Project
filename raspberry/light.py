import time
from gpiozero import MCP3008
from gpiozero import PWMLED

pot = MCP3008(0)
led = PWMLED(21) # GPIO 21 or Pin 40
led.on() # test - the led should be lit
time.sleep(1)
led.off() # test - the led should go off
time.sleep(1)
led.value = 0.5 # test - the led should be lit at half brightness
time.sleep(1)
led.off()
time.sleep(1)

led.source = pot.values # actual connecting of the LED to the potentiometer

print("Program running... Press CTRL+C to exit")

try:

	while True:
		time.sleep(0.1)

except KeyboardInterrupt:
	print("Program terminated!")
