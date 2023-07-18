from ModeDetector import ModeDetector
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from Sensors.CameraSensor import ImageSensor, VideoSensor
from buz import Buzz
from LightController import LightController
from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin

image_sensor = ImageSensor("Image")
video_sensor = VideoSensor("Video")
temperature_sensor = TemperatureSensor()
pir = PIRSensor()
# buzz = Buzz()
lightSensor = LightSensor()
modeDetector = ModeDetector()
lightController = LightController(lightSensor, pir, image_sensor, modeDetector)

app = Flask(__name__, template_folder='web')
cors = CORS(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/web/<path:name>')
def return_flutter_doc(name):
    datalist = str(name).split('/')
    DIR_NAME = "web"
    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]
    return send_from_directory(DIR_NAME, datalist[-1])


@app.route('/api/sensors/temperature')
def get_temperature():
    return str(temperature_sensor.get_value()[0])


@app.route('/api/sensors/humidity')
def get_humidity():
    return str(temperature_sensor.get_value()[1])


@app.route('/api/light/on', methods=['POST'])
def light_on():
    lightController.led_on()
    return "Set LED on"


@app.route('/api/light/off', methods=['POST'])
def light_off():
    lightController.led_off()
    return "Set LED off"


@app.route('/api/light/set', methods=['POST'])
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


if __name__ == '__main__':
    lightController.start()
    app.run(host='0.0.0.0', port=8080)
