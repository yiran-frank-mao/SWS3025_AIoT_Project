import time
from Sensors.Sensors import Sensor
from gpiozero import MCP3008
from gpiozero import PWMLED

# light = MCP3008(0)
# led = PWMLED(21) # GPIO 21 or Pin 40
# led.on() # test - the led should be lit
# time.sleep(1)
#
# try:
#
# 	while True:
# 		print("the light value = ", light.value)
# 		time.sleep(0.1)
#
# except KeyboardInterrupt:
# 	print("Program terminated!")


#调光函数：while 1 if光强>(上阈值)→led变亮 else if光强<(下阈值)→led变暗
#打开灯
class LightSensor(Sensor):
	def __init__(self):
		led = PWMLED(21)
		light = MCP3008(0)

	def get_value(self):
		self = light.value
