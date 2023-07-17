from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.starr_recording('/home/pi/videos/train1.mp4')
sleep(5)
camera.stop_recording()
camera.stop_preview()