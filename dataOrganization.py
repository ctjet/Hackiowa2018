# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:45:58 2018
"""

from dbfread import DBF

table = DBF('wwa_201801010000_201812312359.dbf')

counties = {}
tempDict = {}

countyCounter = 0

for record in table:
    
    if record["NWS_UGC"].startswith("IA"):
        tempDict["County"] = record["NWS_UGC"]
        tempDict["Phenom"] = record["PHENOM"]
        tempDict["Issued"] = record["ISSUED"]
    
    counties["warning{}".format(countyCounter)] = tempDict
    
    countyCounter = countyCounter + 1
    
print(counties['warning1'])