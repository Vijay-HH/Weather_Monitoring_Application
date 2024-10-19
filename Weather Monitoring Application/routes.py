from flask import render_template, jsonify
from app import app
from app.weather import get_weather_data, process_weather_data
from app.models import WeatherData

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    # Fetch processed weather data (summary of multiple cities)
    data = process_weather_data()
    return render_template('summary.html', summary=data)

@app.route('/api/weather')
def weather_api():
    weather_data = get_weather_data()
    return jsonify(weather_data)
