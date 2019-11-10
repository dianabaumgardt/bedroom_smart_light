# attribution - https://www.codeastar.com/easy-accuweather-forecast-in-python/

import requests
import json, re, sys, argparse, os
import time
from datetime import datetime

#os.environ["ACW_API_KEY"] = "dDbV6PqtGmwn5yH1QiA4KIssgusvmS8x"

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('credentials/creds.txt', cur_path)
f = open(new_path, 'r')
API_KEY = f.read()

print API_KEY

#if "ACW_API_KEY" in os.environ:
 #   API_KEY = os.environ['ACW_API_KEY']
#else:
 #   if API_KEY == []:
  #    sys.exit("No API key found")


def getJSONfromUrl(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data

def getCurrentConditions():
    url = "http://dataservice.accuweather.com/currentconditions/v1/339529?apikey=dDbV6PqtGmwn5yH1QiA4KIssgusvmS8x&details=true"
    json_data = getJSONfromUrl(url)
    if json_data == []:
        sys.exit("No location found for '{location}' from AccuWeather API")
    else:
        for p in json_data:
            current_weather=p["WeatherText"]
            current_temp=p["Temperature"]["Metric"]["Value"]
            current_realfeel_temp=p["RealFeelTemperature"]["Metric"]["Value"]
            current_conditions=p["WeatherText"]
            wind_speed=p["Wind"]["Speed"]["Metric"]["Value"]

    print "Current temperature: ", current_temp
    return json_data


def get1DayForecast():
    url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/339529?apikey=dDbV6PqtGmwn5yH1QiA4KIssgusvmS8x&details=true&metric=true"
    json_data = getJSONfromUrl(url)
    if json_data == []:
        sys.exit("No location found for '{location}' from AccuWeather API")

start_time = datetime.now()
current_hour = start_time.hour
current_hour -= 1
print "Current hour: ", current_hour

while True:
    now = datetime.now()
    if now.hour != current_hour:
        current_hour = now.hour
        parsed_json = getCurrentConditions()
        print "Current Conditions: ", parsed_json[0]['WeatherText']
        print "Current Temp: ", parsed_json[0]['Temperature']['Metric']['Value']
        print "Current Wind: ", parsed_json[0]['Wind']['Speed']['Metric']['Value']
    time.sleep(60)