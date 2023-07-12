import time
from Sensors import Sensor
from gpiozero import MCP3008
from gpiozero import PWMLED

# light = MCP3008(0)
# led = PWMLED(21) # GPIO 21 or Pin 40
# led.on() # test - the led should be lit
# time.sleep(1)
#
# led.source = light.values # actual connecting of the LED to the potentiometer
# print("Program running... Press CTRL+C to exit")
#
# try:
#
# 	while True:
# 		print("the light value = ", light.value)
# 		time.sleep(0.1)
#
# except KeyboardInterrupt:
# 	print("Program terminated!")

class lightSensor(Sensor):
	def __init__(self, name):
		self.name = name

	def get_value(self):
		pass