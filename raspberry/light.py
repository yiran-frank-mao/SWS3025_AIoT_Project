import time
from gpiozero import PWMLED

#测试
led = PWMLED(17) 
led.value = 0.5
led.on() # test - the led should be lit
time.sleep(1)
led.off() # test - the led should go off

#指定亮度开灯/暗处用/默认亮度/手动调节指定亮度
def light(double: I):
    led = PWMLED(17)
    led.value = I
    led.on()

#调节到固定亮度
def adjust(int: A):
    if A == 1#待补充

#关灯
def off():
    led = PWMLED(17)
    led.off()
