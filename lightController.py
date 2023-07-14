import time
from gpiozero import PWMLED
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor


class Light:
    def __init__(self):
        self.led = PWMLED(21)

    def led_off(self):
        self.led.off()

    def led_on(self):
        self.led.on()

    def set_led(self, value):
        self.led.value = value

    def ledstate(self, module):  # 每进行一次相机采样模式识别就执行一次
        if module == 'manual':  # 手动模式
            self.led.value = 0.8  # 默认亮度
            self.led.on()
        elif module == 'reading':  # 阅读模式
            self.led.value = 0.8  # 默认亮度
            self.led.on()
            ideallight = 0.009
            i = 0
            while (i < 100):
                self.adjust(ideallight)
                i = i + 1
        elif module == 'computer':  # 电脑模式
            self.led.value = 0.8  # 默认亮度
            self.led.on()
            ideallight = 0.02
            i = 0
            while (i < 100):
                self.adjust(ideallight)
                i = i + 1



    def adjust(self, ideallight):
        light0 = LightSensor.get_value()
        if light0 > ideallight + 0.001:  # 暗
            if self.led.value + 0.001 < 1:
                self.led.value = self.led.value + 0.001
            else:
                self.led.value = 1
        elif light0 < ideallight - 0.001:  # 亮
            if self.led.value - 0.001 > 0:
                self.led.value = self.led.value - 0.001
        else:
            self.led.value = 0

    def dark(self):
        if PIRSensor.get_value() == 1 and LightSensor.get_value() > 0.8:
            self.led.value = 0.4  # 夜灯亮度
            self.led.on()
            time.sleep(30)
            self.led.off()
