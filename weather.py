import configparser
import requests
import json

def get_callback():
    #read the config.txt
    config = configparser.ConfigParser()
    config.read_file(open(r'config.txt'))
    API_key = config.get('Basic-Configuration', 'API_key')
    city_name = config.get('Basic-Configuration', 'city_name')

    # API call
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    Final_url = base_url + "q=" + city_name + "&appid=" + API_key

    # Callback
    weather_data = requests.get(Final_url).json()

    return weather_data


weather_data = get_callback()
print(weather_data)

ktemp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]
wind_ms = weather_data["wind"]["speed"]

#Convert Kelvin to Celsius
ctemp = ktemp - 273.15
#Convert Windspeed to km/h
wind = wind_ms * 3.6

#Print Data
print(int(ctemp), "C°")
print(humidity, "%")
print(int(wind), "km/h")
