# filename: address_to_latlong.py
# author: kris bukovi
# last modified: July 21, 2018

from openpyxl import load_workbook
from geopy.geocoders import Nominatim

# load workbook
wb = load_workbook('test.xlsx')

# get first sheet name
first_sheet = wb.sheetnames[0]

# load worksheet
ws = wb[first_sheet]

for i in range(4,849):

    # j
    address = ws['B' + str(i)]

    print(address.value)






