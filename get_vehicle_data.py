import requests
import csv
from datetime import datetime

def save_vehicle_data():

    url = "https://feeds.transloc.com/3/vehicle_statuses?agencies=100,104&include_arrivals=true" 
    querystring = {"callback":"call","agencies":"100", "routes":"8006606"} #agency = Uchicago, route = Downtown campus connector
    response = requests.get(url, params=querystring).json() #json to dictionary
    
    vehicles = [] #intialize list to hold data

    for item in response["vehicles"]:
            current_lat, current_long = item.pop("position") #remove position from dictionaty and assign to variables
            flattened_item = {**item, "current_lat" : current_lat, "current_long": current_long} #add coords to existing dict 
            vehicles.append(flattened_item) #append to list

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    filename = "vehicle data " + timestamp
    print(filename)


save_vehicle_data()

