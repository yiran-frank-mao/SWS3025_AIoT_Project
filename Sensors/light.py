import time
from Sensors import Sensor
from gpiozero import PWMLED
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor

class light:
    def __init__(self):
        led = PWMLED(21)
    def ledstate(self,module):  # 每进行一次相机采样模式识别就执行一次
        if module == 'manual':  # 手动模式
            led.value = 0.8  # 默认亮度
            led.on()
        elif module == 'reading':  # 阅读模式
            led.value = 0.8  # 默认亮度
            led.on()
            ideallight = 0.009
            i = 0
            while (i < 100):
                adjust(ideallight)
                i = i + 1
        elif module == 'computer':  # 电脑模式
            led.value = 0.8  # 默认亮度
            led.on()
            ideallight = 0.02
            i = 0
            while (i < 100):
                adjust(ideallight)
                i = i + 1
    def ledoff(self):
        led.off()
    def adjust(self,ideallight):
        light0 = LightSensor.get_value()
        if light0 > ideallight + 0.001:  # 暗
            if led.value + 0.001 < 1:
                led.value = led.value + 0.001
            else:
                led.value = 1
        elif light0 < ideallight - 0.001:  # 亮
            if led.value - 0.001 > 0:
                led.value = led.value - 0.001
        else:
            led.value = 0
    def dark(self):
        if PIRSensor.get_value() == 1 and LightSensor.get_value() > 0.8 :
            led.value = 0.4  # 夜灯亮度
            led.on()
            time.sleep(30)
            led.off()

if __name__ == '__main__':
    test_light()
