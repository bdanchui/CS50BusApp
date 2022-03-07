from func import *
import datetime
import pytz
from datetime import timedelta

# Default headers
headers = {'AccountKey' : 'LEUlOjGPTySbMnSBBrj/aA==',
        'accept' : 'application/json'}

# time functions
def time_format(time_string):
    x = datetime.datetime.strptime(time_string[0:-9], "%Y-%m-%dT%H:%M")
    return x

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

# arrival = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
#                     , params={'BusStopCode':83139}, headers=headers).json()['Services']

# print(arrival)

# types = set(map(type, arrival))
# print(types)

# attributes = set(key for dicts in arrival for key in dicts.keys())
# print(attributes)

# Next Bus Timing
# for info in arrival:
#     print("Bus Service:", info['ServiceNo'])
#     print("Next Bus:", info['NextBus']['EstimatedArrival'])
#     print("Subsequent Bus:", info['NextBus2']['EstimatedArrival'])
#     print("Subsequent Bus:", info['NextBus3']['EstimatedArrival'], end="\n\n")

stops = json.loads(open("stops.json").read())
services = json.loads(open("services.json").read())
routes = json.loads(open("routes.json").read())

service = "44709"
if len(service) == 5:
    description = [desc["Description"] for desc in stops if desc["BusStopCode"] == service]
    print(description)
    if len(description) == 0:
        print("No such bus stop")
arrive = arrival(int(service), headers)
print(arrive)

# Get current time
currenttime = datetime.datetime.now(pytz.timezone('Asia/Singapore')).replace(microsecond=0).isoformat()
# print("current time", currenttime, end="\n\n")

bus_list = []

for res in arrive:
    bus_dict = {}
    nextbus = time_diff(res["NextBus"]["EstimatedArrival"], currenttime)
    nextbus2 = time_diff(res["NextBus2"]["EstimatedArrival"], currenttime)
    bus_dict["ServiceNo"] = res["ServiceNo"]
    bus_dict["NextBus"] = nextbus
    bus_dict["NextBus2"] = nextbus2
    bus_list.append(bus_dict)
    # print("Bus Number:", res["ServiceNo"])
    # print("Next Bus: {}".format(nextbus))
    # print("Subsequent Bus: {}\n".format(nextbus2))

# make into a dict

for keys in bus_list:
    print(keys)
