import requests
from pprint import pprint

# basic informations
API_key = "API KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "City Name"

# API call
Final_url = base_url + "q=" + city_name + "&appid=" + API_key
print(Final_url)
weather_data = requests.get(Final_url).json()

# Callback
pprint(weather_data)
