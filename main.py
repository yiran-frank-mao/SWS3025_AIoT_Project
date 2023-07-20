import DataManager
from Alarm import Alarm
from MicrobitCommunication import MicCom
from ModeDetector import ModeDetector
from Sensors.LightSensor import LightSensor
from Sensors.PIRSensor import PIRSensor
from Sensors.TemperatureSensor import TemperatureSensor
from Sensors.CameraSensor import ImageSensor, VideoSensor
from Buzz import Buzz
from Controller import Controller
from flask import Flask, request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
import numpy as np
import threading

image_sensor = ImageSensor("Image")
video_sensor = VideoSensor("Video")
temperature_sensor = TemperatureSensor()
pir = PIRSensor()
buzz = Buzz()
alarm = Alarm()
microbit = MicCom()
lightSensor = LightSensor()
modeDetector = ModeDetector()

controller = Controller(
    lightSensor=lightSensor,
    pirSensor=pir,
    imageSensor=image_sensor,
    modeDetector=modeDetector,
    alarm=alarm,
    buzzer=buzz,
    microbit=microbit)

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
    controller.led_on()
    return "Set LED on"


@app.route('/api/light/off', methods=['POST'])
def light_off():
    controller.led_off()
    controller.state = "off"
    return "Set lamp off"


@app.route('/api/light/set', methods=['POST'])
def set_light():
    val = np.round(float(request.args.get('value')))
    controller.set_led(val / 100)
    controller.state = "manual"
    controller.set_mode("manual")
    return "Set LED to " + str(val)


@app.route('/api/light/get')
def get_light():
    return str(int(controller.get_led() * 100))


@app.route('/api/light/get_state')
def get_state():
    return controller.state


@app.route('/api/light/set_state', methods=['POST'])
def set_state():
    state = request.args.get('state')
    controller.state = state
    return "Set mode to " + state


@app.route('/api/light/get_mode')
def get_mode():
    return controller.mode


@app.route('/api/light/set_mode', methods=['POST'])
def set_mode():
    mode = request.args.get('mode')
    controller.set_mode(mode)
    return "Set mode to " + mode


@app.route('/api/alarm/get')
def get_alarm():
    if alarm.activated:
        return "{" + "hour: {}, minute: {}, second: {}". \
            format(alarm.alarmTime.hour, alarm.alarmTime.minute, alarm.alarmTime.second) + "}"
    else:
        return "Alarm is not activated"


@app.route('/api/alarm/set', methods=['POST'])
def set_alarm():
    hour = int(request.args.get('hour'))
    minute = int(request.args.get('minute'))
    second = int(request.args.get('second'))
    alarm.set_alarm(hour, minute, second)
    alarm.activate()
    return "Set alarm to " + str(hour) + ":" + str(minute) + ":" + str(second)


@app.route('/api/sr/set', methods=['POST'])
def sedentaryReminder():
    val = request.args.get('sr')
    controller.sedentaryReminder = val == "on"
    print("******* Sedentary reminder is " + val + "*******")
    return "Set sedentary reminder to " + val


if __name__ == '__main__':
    controller.start()
    dataManageThread = threading.Thread(target=DataManager.dataManage(tempSensor=temperature_sensor))
    app.run(host='0.0.0.0', port=80)
