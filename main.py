import time
from datetime import datetime
import pytz
import sys
from get_data import get_vehicle_data
 
#this bus route runs M-F, 6:30AM to 10PM 
def main():

    cst_timezone = pytz.timezone('America/Chicago') 
    current_date = datetime.now(cst_timezone).date() #get current date
    stop_time = cst_timezone.localize(datetime.combine(current_date, datetime.min.time())) 
    stop_time = stop_time.replace(hour=23, minute=00)  #set stop at 11PM on current date

    get_vehicle_data()
    current_time_cst = datetime.now(cst_timezone) #get current time
    print("Successfully run at:")
    print(current_time_cst)

"""     while True:

        get_vehicle_data()
        current_time_cst = datetime.now(cst_timezone) #get current time
        print(current_time_cst)
        
        if current_time_cst > stop_time:
            print("The current time is past 11:00 PM CST. Exiting the script.")
            sys.exit(0)  # Success!

        else:
            time.sleep(180) #wait 3 minute
 """

main()