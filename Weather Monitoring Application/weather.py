import requests
from app.models import WeatherData
from app import db

API_KEY = 'your_openweathermap_api_key'

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data():
    weather_data = []
    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url).json()
        weather_data.append({
            'city': city,
            'temp': kelvin_to_celsius(response['main']['temp']),
            'feels_like': kelvin_to_celsius(response['main']['feels_like']),
            'condition': response['weather'][0]['main'],
            'dt': response['dt']
        })
    return weather_data

def process_weather_data():
    weather_data = get_weather_data()
    # Process the data: calculate averages, find dominant weather, etc.
    processed_data = []
    for data in weather_data:
        # Process the city's data, this is where you apply rollups/aggregates
        processed_data.append({
            'city': data['city'],
            'avg_temp': data['temp'],  # Example processing
            'max_temp': data['temp'],
            'min_temp': data['temp'],
            'dominant_condition': data['condition']
        })
        store_in_db(data)
    return processed_data

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def store_in_db(data):
    weather_entry = WeatherData(
        city=data['city'],
        avg_temp=data['temp'],
        max_temp=data['temp'],
        min_temp=data['temp'],
        dominant_condition=data['condition']
    )
    db.session.add(weather_entry)
    db.session.commit()
