import json
import requests
import datetime
from datetime import timedelta

# Obtain data from API
def fetch_data(url, headers):
    datas = []
    while True:
        data = requests.get(url, params={'$skip':len(datas)}, headers=headers).json()['value']
        if len(data) == 0:
            break
        datas += data
    return datas

# Obtain timing from arrival API
def arrival(BusStopCode, headers):
    timing = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
                    , params={'BusStopCode':BusStopCode}, headers=headers).json()['Services']
    return timing

# Update json from API
def write(data, filename):
    with open(filename + ".json", "w") as f:
        f.write(json.dumps(data))

# time functions
def time_format(time_string):
    x = datetime.datetime.strptime(time_string[0:-9], "%Y-%m-%dT%H:%M")
    return x

# Obtain next bus timing from time difference
def time_diff(next_time, current_time):
    try:
        current_time = time_format(current_time)
        next_time = time_format(next_time)
        diff = next_time - current_time
        diff = (diff/timedelta(minutes=1))
        if int(diff) == 0:
            return "Arr"
        elif int(diff) < 0:
            return "Left"
        diff = str(diff)[:-2]
        return "{} mins".format(diff)
    except:
        return "-"
