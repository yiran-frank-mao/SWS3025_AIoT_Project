from flask import Flask
from flask import request, session, redirect, url_for
from flask import send_from_directory
from flask import render_template
from Sensors.TemperatureSensor import TemperatureSensor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web/index.html')

@app.route('/welcome')
def welcome():
    return 'Welcome to smart hub'

@app.route('/api/sensors/temperature')
def get_temperature():
    return TemperatureSensor().get_value()[0]

@app.route('/api/sensors/humidity')
def get_humidity():
    return TemperatureSensor().get_value()[1]

if __name__ == '__main__':
    app.run(port=8080)