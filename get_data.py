import requests
import csv
from datetime import datetime
import pytz

def get_vehicle_data():

    #API call
    url = "https://feeds.transloc.com/3/vehicle_statuses?agencies=100,104&include_arrivals=true" 
    querystring = {"callback":"call","agencies":"100", "routes":"8006606"} #agency = Uchicago, route = Downtown campus connector
    #querystring = {"callback":"call","agencies":"100", "routes":"8000548"} #agency = Uchicago, route = Central
    response = requests.get(url, params=querystring).json() #json to dictionary
    print(response)
    
    #create timestamp info
    current_time = datetime.now() #UTC datetime
    current_local_time = current_time.astimezone(pytz.timezone('America/Chicago')) #CST datetime
    timestamp = current_local_time.strftime("%d-%m-%Y %H %M %S") #Format as string

    vehicles = [] #intialize list to hold data

    if not response["vehicles"]:
        print("No vehicles found")


    for item in response["vehicles"]:
            current_lat, current_long = item.pop("position") #remove position from dictionaty and assign to variables
            flattened_item = {**item, "current_lat" : current_lat, "current_long": current_long, "timestamp" : timestamp} #add coords to existing dict 
            vehicles.append(flattened_item) #append to list

    filepath = "Transloc Data/"
    filename = filepath + timestamp +".csv" 

    #Write to csv
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = vehicles[0].keys())
        writer.writeheader()    # Writing headers (field names)
        for row in vehicles:      # Writing data rows
            writer.writerow(row)