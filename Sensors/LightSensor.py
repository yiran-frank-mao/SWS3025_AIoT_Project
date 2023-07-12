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


#调光函数：while 1 if光强>(上阈值)→led变亮 else if光强<(下阈值)→led变暗
#打开灯
class lightSensor(Sensor):
	def __init__(self):
		led = PWMLED(21)
		light = MCP3008(0)
	def ledstate(module): #每进行一次相机采样模式识别就执行一次
		if module = 'manual': #手动模式
			led.value = 0.8 #默认亮度
			led.on()
		elif module = 'reading': #阅读模式
		    led.value = 0.8  # 默认亮度
		    led.on()
            ideallight = 0.009
	        i = 0
	        while(i<100):
				adjust(ideallight)
		        i = i + 1
		elif module = 'computer':#电脑模式
	        led.value = 0.8  # 默认亮度
	        led.on()
			ideallight = 0.02
	        i = 0
	        while(i<100):
				adjust(ideallight)
		        i = i + 1
            #此处有一个循环执行adjust（ideallight）直到灯关闭/切换为手动模式但我不会写
	def ledoff():
            led.off()
	def adjust(ideallight):
		light0 = get_value()
                if light0 > ideallight + 0.001#暗
			        if led.value + 0.001 < 1 :
					    led.value = led.value + 0.001
					else led.value = 1
			    elif light0 < ideallight - 0.001#亮
					if led.value - 0.001 > 0 :
		                led.value = led.value - 0.001
			        else led.value = 0

	def get_value(self):
		self = light.value
