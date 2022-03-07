import requests

# Default headers
headers = {'AccountKey' : 'LEUlOjGPTySbMnSBBrj/aA==',
        'accept' : 'application/json'}

# Checking json data from API
# print(services.json())

# print(services.json()['value'])

# Checking number of data parse into variable
# print(len(services.json()['value']))

# Creating loop to obtain all data
results = []
while True:
    data = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusRoutes",
                        params={'$skip':len(results)}, headers=headers).json()['value']
    if len(data) == 0:
        break
    results += data

# Checking data types in results
# types = set(map(type, results))
# print(types)

# Checking keys in results
# print(set(key for res in results for key in res.keys()))
# print(set([res['Operator'] for res in results]))
# print([res['ServiceNo'] for res in results])
# print(len(set([res['ServiceNo'] for res in results]))) # 553
# print([res['StopSequence'] for res in results if res['ServiceNo'] == '976'])
bus_stop_code = [res["BusStopCode"] for res in results if res["ServiceNo"] == "922" and res["Direction"] == 1]
print(bus_stop_code)