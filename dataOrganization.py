# -*- coding: utf-8 -*-
import webbrowser

"""
Created on Sat Oct  6 10:45:58 2018
"""

from dbfread import DBF
from calebTest import draw
import csv

table = DBF('DB/Large/wwa_201801010000_201812312359.dbf')


counties = {}


with open('DB/IowaCountyData.csv', 'r') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',', quotechar='"')
    
    rowCount = 0
    
    for row in csv_file:
        if rowCount != 0:
            counties[row[0]] = {"County_Name":row[1], "Lat":row[2], "Long":row[3], "numSV":0, "numFF":0}
        
        rowCount += 1

for record in table:
    
    if record["NWS_UGC"].startswith("IA"):
        
        if record["PHENOM"] == "SV":
            counties[record["NWS_UGC"]]["numSV"] += 1
        elif record["PHENOM"] == "FF":
            counties[record["NWS_UGC"]]["numFF"] += 1


with open('DB/merged_data.csv', 'w') as write_file:
    writer = csv.writer(write_file)
    for key, line in counties.items():
        writer.writerow([key, line])

arrSV = []
arrFF = []
i = 0
for county in counties:
    print(county)
    # arrSV[i] = county["numSV"]
    # arrFF[i] = county["numFF"]
    i += 1

draw(arrSV)
webbrowser.open("my_heatmap.html")