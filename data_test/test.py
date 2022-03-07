import requests

headers = {'AccountKey' : 'LEUlOjGPTySbMnSBBrj/aA==',
        'accept' : 'application/json'}

stops = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip=0", headers=headers)
# print(stops.json())
print(stops.json()['value'])

total_stops = []

while True:
    stops = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusStops", params={'$skip': len(total_stops)}, headers=headers)
    if len(stops.json()['value']) == 0:
        break
    else:
        total_stops += stops

print(len(total_stops))

for res in total_stops:
    for key in res.keys():
        print(key)