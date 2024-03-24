import requests

api_key = '2cf6f6c8723d9456cd83a63323862c12'

city = input("Enter the name of the city: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    Celsius = round(float(temp) - 273.15, 2)
    print(f'Temperature: {temp} K or {Celsius} C')
    print(f'Description: {desc.title()}')
else:
    print('Unable to fetch weather data')