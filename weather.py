import configparser
import requests
import json

def get_callback():
    #read the config.txt
    config = configparser.ConfigParser()
    config.read_file(open(r'config.txt'))
    API_key = config.get('Basic-Configuration', 'API_key')
    city_name = config.get('Basic-Configuration', 'city_name')

    # API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    Final_url = base_url + "q=" + city_name + "&appid=" + API_key

    # API call
    return requests.get(Final_url).json()


def convert_kelvin(ktemp):
    # Convert Kelvin to Celsius
    return ktemp - 273.15


def convert_kmh(wind_ms):
    # Convert Windspeed to km/h
    return wind_ms * 3.6


def values():
    # Get Values from API
    weather_data = get_callback()

    # Parsing different values
    ktemp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_ms = weather_data["wind"]["speed"]

    # Convert Values
    ctemp = convert_kelvin(ktemp)
    wind = convert_kmh(wind_ms)

    return ctemp, humidity, wind


if __name__=="__main__":
    temp, humidity, wind = values()

    # Print Data
    print(int(temp), "C°")
    print(humidity, "%")
    print(int(wind), "km/h")
