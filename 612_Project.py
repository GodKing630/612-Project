# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:37:04 2018
@program: 612 Project
@author: aleew
"""
import argparse
#Worked with Will Clark
parser = argparse.ArgumentParser(description = 'Takes in filters for craigslist search (exclusively for motorcycles and cars)')
parser.add_argument("-mi", "--miles", help="Miles from zip (default: None)", action="store", dest="miles", default=None)
parser.add_argument("-z", "--zip", help="Zipcode (default: None)", action="store", dest="zip", default=None)
parser.add_argument("-minp", "--min_price", help="Minimum price of the item (default: None)", action="store", dest="minp", default=None)
parser.add_argument("-maxp", "--max_price", help="Maximum price of the item (default: None)", action="store", dest="maxp", default=None)
parser.add_argument("-ma", "--make", help="Make/Model of the item (default: None)", action="store", dest="make", default=None)
parser.add_argument("-minen", "--min_eng_disp", help="Minimum engine displacement (default: None)", action="store", dest="minen", default=None)
parser.add_argument("-maxen", "--max_eng_disp", help="Maximum engine displacement (default: None)", action="store", dest="maxen", default=None)
parser.add_argument("-miny", "--min_year", help="Minimum model year (default: None)", action="store", dest="miny", default=None)
parser.add_argument("-maxy", "--max_year", help="Maximum model year (default: None)", action="store", dest="maxy", default=None)
parser.add_argument("-mino", "--min_odo", help="Minimum odometer (default: None)", action="store", dest="mino", default=None)
parser.add_argument("-maxo", "--max_odo", help="Maximum odometer (default: None)", action="store", dest="maxo", default=None)
parser.add_argument("-con", "--condition", help="Condition of the item (Options: new, like new, excellent, good, fair, salvage) (default: None)", action="store", dest="condition", default=None)
parser.add_argument("-f", "--fuel", help="Type of fuel for item (Options: gas, diesel, hybrid, electric, other) (default: None)", action="store", dest="fuel", default=None)
parser.add_argument("-col", "--color", help="Color of the item (Options: black, blue, brown, green, grey, orange, purple, red, silver, white, yellow, custom, all) (default: None)", action="store", dest="color", default=None)
parser.add_argument("-ti", "--title", help="Title status (Options: clean, salvage, rebuilt, parts_only, lien, missing) (default: None)", action="store", dest="title", default=None)
parser.add_argument("-tr", "--trans", help="Transmission (Options: manual, automatic, other) (default: None)", action="store", dest="trans", default=None)
parser.add_argument("-l", "--location", help="Location of the item (default: None)", action="store", dest="location", default=None)
results = parser.parse_args()
baseUrl = 'https://nh.craigslist.org/search/mca'

print("results: " + str(results))

for i in results:
    print("i: " + str(i))