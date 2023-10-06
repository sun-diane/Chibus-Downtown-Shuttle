import time
from get_data import get_vehicle_data
 
#this bus route runs M-F, 6:30AM to 10PM 
def main():

    while True:

        get_vehicle_data()
        time.sleep(180) #wait 3 minute
        i = i + 1

main()