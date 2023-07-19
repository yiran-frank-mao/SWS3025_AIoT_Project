import serial
import time


class MicCom:
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)

    def button_pressed(self):
        msg = self.ser.readline()
        strip_msg = msg.decode('utf-8').strip()
        return len(strip_msg) > 0

    def send(self, mode):
        response = mode + '\r\n'
        self.ser.write(str.encode(response))
        time.sleep(3)
