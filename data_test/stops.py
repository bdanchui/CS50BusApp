import requests

headers = {'AccountKey' : 'LEUlOjGPTySbMnSBBrj/aA==',
        'accept' : 'application/json'}

# stops = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip=0",
#                 headers=headers)
# print(stops.json())
# print(stops.json()['value'])

# Variable to hold total_stops
total_stops = []

# Creating loop to get all Data from API
while True:
    stops = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops",
                    params={'$skip': len(total_stops)}, headers=headers).json()['value']
    if len(stops) == 0:
        break
    else:
        total_stops += stops

print(len(total_stops))

# Checking unique datatype in API
# print(set(map(type,total_stops)))

# Checking unique attributes of keys in API
# print(set(key for stop in total_stops for key in stop.keys()))

# Checking if description of stops make sense
# print([stop['Description'] for stop in total_stops if stop['RoadName'] == "Netheravon Rd"])

# Checking longitude and latitude of bus stops
# print(max(stop['Latitude'] for stop in total_stops))
# print(max(stop['Longitude'] for stop in total_stops))
# print(min(stop['Latitude'] for stop in total_stops))
# print(min(stop['Longitude'] for stop in total_stops))