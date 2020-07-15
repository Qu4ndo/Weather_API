import configparser
import requests
from pprint import pprint

#read the config.txt
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))
API_key = config.get('Basic-Configuration', 'API_key')
city_name = config.get('Basic-Configuration', 'city_name')

# URL for API call
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# API call
Final_url = base_url + "q=" + city_name + "&appid=" + API_key
print(Final_url)
weather_data = requests.get(Final_url).json()

# Callback
pprint(weather_data)
