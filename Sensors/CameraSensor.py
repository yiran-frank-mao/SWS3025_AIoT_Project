from Sensors.Sensors import Sensor
from picamera import PiCamera
from time import sleep
from datetime import datetime

class ImageSensor(Sensor):
    def __init__(self, name):
        super().__init__(name)

    def get_value(self) -> str:
        # Returns the file path of the image
        camera = PiCamera()
        filePath = '/home/pi/images'
        fileName = datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        camera.capture(filePath + '/' + fileName)
        return filePath + '/' + fileName

class VideoSensor(Sensor):
    def __init__(self, name, duration: int = 10):
        super().__init__(name)
        self.duration = duration

    def get_value(self) -> str:
        # Returns the file path of the video
        camera = PiCamera()
        filePath = '/home/pi/videos'
        fileName = datetime.now().strftime("%Y%m%d%H%M%S") + '.h264'
        camera.start_recording(filePath + '/' + fileName)
        sleep(self.duration)
        camera.stop_recording()
        return filePath + '/' + fileName

    def set_duration(self, duration: int):
        self.duration = duration


def camera_sensor_test():
    camera = PiCamera()
    camera.start_preview()
    while True:
        sleep(1)

