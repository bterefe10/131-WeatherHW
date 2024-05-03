# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_cardinal_direction(degrees):
    if degrees >= 337.5 or degrees < 22.5:
        return 'North'
    elif 22.5 <= degrees < 67.5:
        return 'Northeast'
    elif 67.5 <= degrees < 112.5:
        return 'East'
    elif 112.5 <= degrees < 157.5:
        return 'Southeast'
    elif 157.5 <= degrees < 202.5:
        return 'South'
    elif 202.5 <= degrees < 247.5:
        return 'Southwest'
    elif 247.5 <= degrees < 292.5:
        return 'West'
    else:
        return 'Northwest'

@app.route('/weather', methods=['GET'])
def get_weather_data():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=San%20Jose,US&appid=0ea1e7a2709146d42f2260f90020d5bb')
    data = response.json()

    # Convert temperatures to integers
    current_temp_f = int((data['main']['temp'] - 273.15) * 9/5 + 32)
    min_temp_f = int((data['main']['temp_min'] - 273.15) * 9/5 + 32)
    max_temp_f = int((data['main']['temp_max'] - 273.15) * 9/5 + 32)

    weather_info = {
        'city_name': data['name'],
        'current_temperature': current_temp_f,
        'min_temperature': min_temp_f,
        'max_temperature': max_temp_f,
        'weather_conditions': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_direction': get_cardinal_direction(data['wind']['deg']),
    }

    return render_template('weather.html', weather_info=weather_info)


if __name__ == '__main__':
    app.run(debug=True)
