#树莓派串口输出module----microbit显示
#microbit按按钮----树莓派接受某一字符串----关灯/开灯
from lightController import Light
from microbit import serial
import time


class MicCom:
	def __init__(self):
		ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
		while True:
			com_input = ser.read(10)
			if com_input:  # 如果读取结果非空，则输出
				if Light.get_led() == 0: Light.led_on()
				else: Light.led_off()
	def send(self,module):
		response = module + '\r\n'
# 		ser.write(str.encode(response))
		time.sleep(5)

# try:
#
# 	print("Listening on /dev/ttyACM0... Press CTRL+C to exit")
#
# 	ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
#
# 	while True:
#
# 		msg = ser.readline()
# 		smsg = msg.decode('utf-8').strip()
#
# 		if len(smsg) > 0:
#
# 			print('RX:{}'.format(smsg))
#
# 			response = input('Enter Response = ')
# 			response = response + '\r\n'
# 			ser.write(str.encode(response))
# 			print('Response sent...')
#
# 		time.sleep(1)
#
# except KeyboardInterrupt:
#
# 	if ser.is_open:
# 		ser.close()
#
# 	print("Program terminated!")