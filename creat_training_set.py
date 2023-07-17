from picamera import PiCamera
from time import sleep
from datetime import datetime


camera = PiCamera()
filePath = '/home/pi/videos'
fileName = datetime.now().strftime("%Y%m%d%H%M%S") + '.h264'
camera.start_recording(filePath + '/' + fileName)
sleep(10)
camera.stop_recording()