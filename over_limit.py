# filename: over_limit.py
# author: kris bukovi
# last modified: July 24, 2018

from openpyxl import load_workbook
from geopy.geocoders import Nominatim

# create Nominatim object
geolocator = Nominatim()

# load workbook
wb = load_workbook('test.xlsx')

# get first sheet name
first_sheet = wb.sheetnames[0]

# load worksheet
ws = wb[first_sheet]

for i in range(4,849):

    try:

        # store first draw
        first_draw = ws['G' + str(i)]

        # store fourth draw
        fourth_draw = ws['H' + str(i)]

        # store sixth draw
        sixth_draw = ws['I' + str(i)]

        # get the average 
        average = (first_draw + fourth_draw + sixth_draw) / 3

        # write average to file
        ws['L' + str(i)] = average

        # write yes/no for over limit column to file
        if average > 5.0:
            ws['M' + str(i)] = "Yes"
        else:
            ws['M' + str(i)] = "No"

        # save file
        wb.save('test.xlsx')

    except:
        print("Can't calculate average, skipping...")
        








