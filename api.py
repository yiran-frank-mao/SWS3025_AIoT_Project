from flask import Flask, request
from flask_cors import CORS, cross_origin

from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from Sensors.CameraSensor import ImageSensor, VideoSensor
from LightController import LightController

app = Flask(__name__, template_folder='web')
cors = CORS(app)

image_sensor = ImageSensor("Image")
video_sensor = VideoSensor("Video")
temperature_sensor = TemperatureSensor()
pir = PIRSensor()
lightSensor = LightSensor()
lightController = LightController(lightSensor, pir)

@app.route('/api/sensors/temperature')
def get_temperature():
    return str(temperature_sensor.get_value()[0])


@app.route('/api/sensors/humidity')
def get_humidity():
    return str(temperature_sensor.get_value()[1])


@app.route('/api/light/on', methods=['POST'])
@cross_origin()
def light_on():
    lightController.led_on()
    return "Set LED on"


@app.route('/api/light/off', methods=['POST'])
@cross_origin()
def light_off():
    lightController.led_off()
    return "Set LED off"


@app.route('/api/light/set', methods=['POST'])
@cross_origin()
def set_light():
    val = int(request.args.get('value'))
    lightController.set_led(val / 100)
    return "Set LED to " + str(val)


@app.route('/api/light/get')
def get_light():
    return str(int(lightController.get_led() * 100))


@app.route('/api/camera/capture_photo')
def camera_capture_photo():
    return image_sensor.get_value()