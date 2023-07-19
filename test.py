import requests
import time
from pathlib import Path

# from Alarm import Alarm
# from Controller import Controller
# from Sensors.CameraSensor import ImageSensor, VideoSensor
# from Sensors.LightSensor import LightSensor
# from Sensors.PIRSensor import PIRSensor
# from Sensors.TemperatureSensor import TemperatureSensor
# from MicrobitCommunication import MicCom
# from Buzz import Buzz

if __name__ == '__main__':
    # 导入tqdm模块
    from tqdm import tqdm

    # 导入time模块，用于模拟耗时操作
    import time

    # 定义一个总任务数
    total = 10

    # 使用tqdm函数包装一个可迭代对象，如range函数返回的对象
    for i in tqdm(range(total)):
        # 模拟耗时操作，每次暂停1秒
        time.sleep(1)

