#树莓派串口输出module----microbit显示
#microbit按按钮----树莓派接受某一字符串----关灯/开灯
from lightController import Light
import serial
import time


class MicCom:
	def __init__(self):
		self.ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
		while True:
			com_input = self.ser.read()
			if com_input:  # 如果读取结果非空，则输出
				if Light.get_led() == 0: Light.led_on()
				else: Light.led_off()
	def send(self,module):
		response = module + '\r\n'
# 		ser.write(str.encode(response))
		time.sleep(5)