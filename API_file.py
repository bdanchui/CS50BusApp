from func import *

headers = {'AccountKey' : 'LEUlOjGPTySbMnSBBrj/aA==',
        'accept' : 'application/json'}

services = fetch_data("http://datamall2.mytransport.sg/ltaodataservice/BusServices", headers)
routes = fetch_data("http://datamall2.mytransport.sg/ltaodataservice/BusRoutes", headers)
stops = fetch_data("http://datamall2.mytransport.sg/ltaodataservice/BusStops", headers)

write(services, "services")
write(routes, "routes")
write(stops, "stops")

