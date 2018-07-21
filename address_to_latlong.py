# filename: address_to_latlong.py
# author: kris bukovi
# last modified: July 21, 2018

from openpyxl import load_workbook
from geopy.geocoders import Nominatim

# load workbook
wb = load_workbook(filename = 'wq_study_results.xlsx')

# get first sheet name
first_sheet = wb.get_sheet_names()[0]

# load worksheet
ws = wb.get_sheet_by_name(first_sheet)






