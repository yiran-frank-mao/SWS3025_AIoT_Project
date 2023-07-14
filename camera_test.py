from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
while True:
    sleep(1)