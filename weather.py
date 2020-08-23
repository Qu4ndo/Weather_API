import configparser
import requests
from pprint import pprint
import json

#read the config.txt
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))
API_key = config.get('Basic-Configuration', 'API_key')
city_name = config.get('Basic-Configuration', 'city_name')

# URL for API call
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# API call
Final_url = base_url + "q=" + city_name + "&appid=" + API_key
#print(Final_url)

# Callback
weather_data = requests.get(Final_url).json()
ktemp = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]


#Convert Fahrenheit to Celsius
ctemp = ktemp - 273.15

print(int(ctemp), "C°")
print(humidity, "%")

# Parse JSON
#parsed_data = (json.loads(weather_data))
#print(parsed_data)
#for x in parsed_data:
#	print("%s: %s" % (x, parsed_data[x]))
