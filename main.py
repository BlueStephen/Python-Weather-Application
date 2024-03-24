import requests
from hide import api_key

def get_weather_info(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = round(float(temp_kelvin) - 273.15, 2)
        desc = data['weather'][0]['description'].title()
        weather_info = f'Temperature: {temp_kelvin} K or {temp_celsius}°C\nDescription: {desc}'
        return weather_info
    else:
        return 'Unable to fetch weather data'

def display_weather_ascii(city):
    weather_info = get_weather_info(city)
    if weather_info.startswith('Unable'):
        print(weather_info)
    else:
        print("Weather Information for", city)
        print("┌" + "─" * 38 + "┐")
        print("│" + " " * 38 + "│")
        print("│" + " " * 12 + "Weather Report" + " " * 12 + "│")
        print("│" + "─" * 38 + "│")
        lines = weather_info.split('\n')
        for line in lines:
            print("│" + line.ljust(38) + "│")
        print("└" + "─" * 38 + "┘")

while True:
    city = input("Enter the name of the city: ")
    display_weather_ascii(city)
    another_city = input("Do you want to enter another city? (yes/no): ")
    if another_city.lower() != 'yes':
        break
