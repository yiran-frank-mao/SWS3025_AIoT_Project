import time
from gpiozero import PWMLED

#指定亮度开灯/暗处用/默认亮度/手动调节指定亮度
def light(I):
    led = PWMLED(17)
    led.value = I
    led.on()

#调节到固定亮度
def adjust(A):
    #if A == 1
    #Todo

#关灯
def off():
    led = PWMLED(17)
    led.off()

def test_light():
    led = PWMLED(17)
    led.value = 0.5
    led.on()  # test - the LED should be lit
    time.sleep(1)
    led.off()  # test - the LED should go off

if __name__ == '__main__':
    test_light()