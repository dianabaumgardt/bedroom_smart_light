import json
import time
import urllib.request

API = dDbV6PqtGmwn5yH1QiA4KIssgusvmS8x
LOCATION_ID = 339529



def get_weather(api, location_id):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)
    return (data[0]['Temperature']['Imperial']['Value'],
            data[0]['RelativeHumidity'],
            data[0]['Wind']['Direction']['Degrees'],
            data[0]['Wind']['Speed']['Imperial']['Value'],
            data[0]['UVIndex'],
            data[0]['CloudCover'],
            data[0]['Pressure']['Metric']['Value'],
            data[0]['Precip1hr']['Metric']['Value'],
            data)


timestamp = time.time()

temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather(API, LOCATION_ID)