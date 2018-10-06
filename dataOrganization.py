# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:45:58 2018
"""

from dbfread import DBF
import csv

table = DBF('DB/Large/wwa_201801010000_201812312359.dbf')


counties = {}
tempName = ""

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

