from Sensors import Sensor
from picamera import PiCamera
from datetime import datetime

class CameraSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def get_value(self) -> str:
        camera = PiCamera()
        filePath = '/home/pi/images'
        fileName = datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        camera.capture(filePath + '/' + fileName)
        return filePath + '/' + fileName

def camera_sensor_test():
    camera = CameraSensor("Camera")
    print(camera.get_value())

if __name__ == "__main__":
    camera_sensor_test()