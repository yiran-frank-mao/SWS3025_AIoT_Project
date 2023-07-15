#树莓派串口输出module----microbit显示
#microbit按按钮----树莓派接受某一字符串----关灯/开灯
from LightController import LightController
import serial
import time


class MicCom:
	def __init__(self):
		ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
		while True:
			msg = ser.readline()
			smsg = msg.decode('utf-8').strip()

			if len(smsg) > 0:

				print('RX:{}'.format(smsg))
				a = LightController()
				if a.get_led() == 0: a.led_on()
				else: LightController.led_off()
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