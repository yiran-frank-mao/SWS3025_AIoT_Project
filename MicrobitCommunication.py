# 树莓派串口输出module----microbit显示
# microbit按按钮----树莓派接受某一字符串----关灯/开灯
from Controller import Controller
import serial
import time


class MicCom:
    def __init__(self):
        ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)
        a = Controller()
        while True:
            msg = ser.readline()
            smsg = msg.decode('utf-8').strip()

            if len(smsg) > 0:
                print('RX:{}'.format(smsg))
                print(a.get_led())
                if a.get_led() == 0:
                    a.led_on()
                else:
                    a.led_off()

    def send(self, module):
        response = module + '\r\n'
        # 		ser.write(str.encode(response))
        time.sleep(5)
