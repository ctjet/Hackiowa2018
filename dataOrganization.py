# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:45:58 2018
"""

from dbfread import DBF

table = DBF('wwa_201801010000_201812312359.dbf')

for record in table:
    print (record)
    
