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
    url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + location + "?apikey=" + API_KEY + "&details=true&metric=true"
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
        current_temp = parsed_json[0]['Temperature']['Metric']['Value']

        if current_temp < -15:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 147, 240, 250)
            uh.show()

        if current_temp < -10:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 102, 235, 250)
            uh.show()
        if current_temp < -5 :
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 45, 232, 252)
            uh.show()

        if current_temp < 0:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 7, 226, 250)
            uh.show()

        if current_temp < 5:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 7, 250, 230)
            uh.show()
        if current_temp < 10:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 116, 247, 223)
            uh.show()

        if current_temp < 15:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 127, 250, 209)
            uh.show()

        if current_temp < 20:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 5, 247, 167)
            uh.show()
        if current_temp < 25:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 247, 247, 5)
            uh.show()

        if current_temp < 30:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 247, 199, 5)
            uh.show()

        if current_temp < 35:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 247, 134, 5)
            uh.show()
        if current_temp < 40:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 247, 53, 5)
            uh.show()
        if current_temp >= 40:
            uh.clear()
            uh.show()

            for x in range(8):
                for y in range(4):
                    uh.set_pixel(x, y, 247, 5, 5)
            uh.show()


    time.sleep(60)