from flask import Flask
from flask_cors import CORS
from Sensors.TemperatureSensor import TemperatureSensor

app = Flask(__name__, template_folder='web')
cors = CORS(app)

@app.route('/api/sensors/temperature')
def get_temperature():
    return str(TemperatureSensor().get_value()[0])

@app.route('/api/sensors/humidity')
def get_humidity():
    return str(TemperatureSensor().get_value()[1])