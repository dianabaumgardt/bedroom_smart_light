import requests
import json, re, sys, argparse, os
import time
from datetime import datetime



# Build up a root path to the creds.txt file in the credentials folder
cur_path = os.path.dirname(__file__)
new_path = os.path.relpath('credentials/creds.txt', cur_path)

# open the creds.txt file and read out the API_KEY
f = open(new_path, 'r')
API_KEY = f.read()

# Accuweather locationid - 339529 is for River Edge, NJ
location = "339529"



# method for hitting a get endpoint and returning json object
def getJSONfromUrl(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data

def getCurrentConditions():
    url = "http://dataservice.accuweather.com/currentconditions/v1/" + location + "?apikey=" + API_KEY + "&details=true"
    json_data = getJSONfromUrl(url)
    if json_data == []:
        sys.exit("No location found for '{location}' from AccuWeather API")
    return json_data


def get1DayForecast():
    url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + location + "?apikey=" API_KEY "&details=true&metric=true"
    json_data = getJSONfromUrl(url)
    if json_data == []:
        sys.exit("No location found for '{location}' from AccuWeather API")
    return json_data


# Main logic
start_time = datetime.now()
current_hour = start_time.hour
current_hour -= 1 # set this for the first loop to force an API update

while True:
    now = datetime.now()
    if now.hour != current_hour:
        current_hour = now.hour
        parsed_json = getCurrentConditions()
        print "Current Conditions: ", parsed_json[0]['WeatherText']
        print "Current Temp: ", parsed_json[0]['Temperature']['Metric']['Value']
        print "Current Wind: ", parsed_json[0]['Wind']['Speed']['Metric']['Value']
    time.sleep(60)