from flask import Flask, request
from flask_cors import CORS
from Sensors.TemperatureSensor import TemperatureSensor
from Sensors.CameraSensor import ImageSensor, VideoSensor
from lightController import Light

app = Flask(__name__, template_folder='web')
cors = CORS(app)

temperature_sensor = TemperatureSensor()
light = Light()
image_sensor = ImageSensor("Image")
video_sensor = VideoSensor("Video")

@app.route('/api/sensors/temperature')
def get_temperature():
    return str(temperature_sensor.get_value()[0])


@app.route('/api/sensors/humidity')
def get_humidity():
    return str(temperature_sensor.get_value()[1])


@app.route('/api/light/on', methods=['POST'])
def light_on():
    light.led_on()
    return "Set LED on"


@app.route('/api/light/off', methods=['POST'])
def light_off():
    light.led_off()
    return "Set LED off"


@app.route('/api/light/set', methods=['POST'])
def set_light():
    # http://raspberrypi4.local:8080/api/light/set?value=0.5
    print(request.args.get('value'))
    val = float(request.args.get('value'))
    light.set_led(val)
    return "Set LED to " + str(val)


@app.route('/api/camera/capture_photo')
def camera_capture_photo():
    return image_sensor.get_value()