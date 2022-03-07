import json
from flask import Flask, flash, redirect, render_template, request
from func import *
import API_file
import pytz

# Load data
stops = json.loads(open("stops.json").read())
services = json.loads(open("services.json").read())
routes = json.loads(open("routes.json").read())

# Configure application
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bus")
def bus():
    bus_stop_code = request.args.get("service")
    if (bus_stop_code):
        service = bus_stop_code
    else:
        service = request.args.get("service")
    service = str(service.upper())

    # Get current time
    currenttime = datetime.datetime.now(pytz.timezone('Asia/Singapore')).replace(microsecond=0).isoformat()

    # Check if user submitted bus service or bus stop code
    if len(service) == 5:

        # Obtain description of bus stop code
        description = [desc["Description"] for desc in stops if desc["BusStopCode"] == service]

        # If there is no such bus stop code
        if len(description) == 0:

            # Show incorrect bus stop
            flash("Incorrect Bus Stop")

            # Return to homepage
            return redirect("/")

        # Obtain timing of buses
        arrive = arrival(int(service), API_file.headers)

        # List to hold dictionary of bus service and bus timing
        bus_list = []

        for res in arrive:
            bus_dict = {}
            nextbus = time_diff(res["NextBus"]["EstimatedArrival"], currenttime)
            nextbus2 = time_diff(res["NextBus2"]["EstimatedArrival"], currenttime)
            nextbus3 = time_diff(res["NextBus3"]["EstimatedArrival"], currenttime)
            bus_dict["ServiceNo"] = res["ServiceNo"]
            bus_dict["NextBus"] = nextbus
            bus_dict["NextBus2"] = nextbus2
            bus_dict["NextBus3"] = nextbus3
            bus_list.append(bus_dict)

        # Show bus timing
        return render_template("bustime.html", description=description, bus_list=bus_list)

    # Else obtain bus stop code based on bus service number
    busStopCode1 = [res["BusStopCode"] for res in routes if res["ServiceNo"] == service and res["Direction"] == 1]
    busStopCode2 = [res["BusStopCode"] for res in routes if res["ServiceNo"] == service and res["Direction"] == 2]

    # If not a proper bus service
    if len(busStopCode1) == 0:

        # Show incorrect bus service
        flash("Incorrect Bus Service")

        return redirect("/")

    # Creating a list to hold dictionaries of bus stop code and description
    bus_description1 = []
    bus_description2 = []

    # Obtaining dictionary of bus stop code, description and bus timing
    for stop in busStopCode1:

        # Creating dictionary variable
        stop_dict = {}

        # Adding bus stop code to dictionary
        stop_dict["BusStopCode"] = stop

        # Adding description to dictionary by looping through stops.json
        for desc in stops:
            if desc["BusStopCode"] == stop:
                stop_dict["Description"] = desc["Description"]

        # Obtaining bus timing based on stop
        arrive = arrival(int(stop), API_file.headers)

        # Loop through arrive and adding next bus timing into dictionary for stop and service number
        for res in arrive:
            if res["ServiceNo"] == service:
                stop_dict["nextbus"] = time_diff(res["NextBus"]["EstimatedArrival"], currenttime)
                stop_dict["nextbus2"] = time_diff(res["NextBus2"]["EstimatedArrival"], currenttime)
                stop_dict["nextbus3"] = time_diff(res["NextBus3"]["EstimatedArrival"], currenttime)

        # Adding dictionary to list
        bus_description1.append(stop_dict)

    for stop in busStopCode2:
        stop_dict = {}
        stop_dict["BusStopCode"] = stop
        for desc in stops:
            if desc["BusStopCode"] == stop:
                stop_dict["Description"] = desc["Description"]

        arrive = arrival(int(stop), API_file.headers)

        # Loop through arrive and adding next bus timing into dictionary for stop and service number
        for res in arrive:
            if res["ServiceNo"] == service:
                stop_dict["nextbus"] = time_diff(res["NextBus"]["EstimatedArrival"], currenttime)
                stop_dict["nextbus2"] = time_diff(res["NextBus2"]["EstimatedArrival"], currenttime)
                stop_dict["nextbus3"] = time_diff(res["NextBus3"]["EstimatedArrival"], currenttime)

        # Adding dictionary to list
        bus_description2.append(stop_dict)

    # Go to bus service page
    return render_template("busService.html", service=service, bus_description1=bus_description1, bus_description2=bus_description2)

# Show all bus services
@app.route("/stops")
def service():

    info = []

    for stop in stops:
        temp_dict = {}
        temp_dict["BusStopCode"] = stop["BusStopCode"]
        temp_dict["Description"] = stop["Description"]
        temp_dict["Latitude"] = stop["Latitude"]
        temp_dict["Longitude"] = stop["Longitude"]

        info.append(temp_dict)

    return render_template("stops.html", temp_dict=temp_dict)



