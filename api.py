from flask import Flask
from flask_cors import CORS
from Sensors.TemperatureSensor import TemperatureSensor
from lightController import Light

app = Flask(__name__, template_folder='web')
cors = CORS(app)

temperature_sensor = TemperatureSensor()
light = Light()

@app.route('/api/sensors/temperature')
def get_temperature():
    return str(temperature_sensor.get_value()[0])


@app.route('/api/sensors/humidity')
def get_humidity():
    return str(temperature_sensor.get_value()[1])


@app.route('/api/light/on')
def light_on():
    light.led_on()
    return "Set LED on"


@app.route('/api/light/off')
def light_off():
    light.led_off()
    return "Set LED off"


@app.route('/api/light/set?=value')
def set_light():
    # TODO
    raise NotImplementedError
