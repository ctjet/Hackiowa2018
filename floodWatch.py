# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 09:31:44 2018
"""

import requests
from xml.etree import ElementTree
import smtplib
import time

starttime=time.time()

while True:
    response = requests.get('http://ifis.iowafloodcenter.org/ifis/ws/sites.php?format=xml')
    
    root = ElementTree.fromstring(response.content)
    
    sensorDict = {}
    index = 1
    
    
    for sensor in root:
        
        
        if sensor[6].text == "Iowa City" and sensor[4].text == "Ralston Creek":
            IFC_code = sensor[0].text
            IFC_Id = sensor[1].text
            depth = sensor[9].text
            Unit = sensor[10].text
            
            sensorDict["Ralston_Sensor".format(index)] = [IFC_code,IFC_Id,depth,Unit]
            
            index += 1
            
            
    #print(sensorDict)
            
    sensorResponse = requests.get("http://ifis.iowafloodcenter.org/ifis/ws/sites.php?site={}&period=1&format=xml".format(sensorDict["Ralston_Sensor"][0]))
    
    sensorResponseRoot = ElementTree.fromstring(sensorResponse.content)
    
    river_depth = float(sensorResponseRoot[1][0][1].text)
    
    print("Depth of {} feet, on {}".format(river_depth, time.ctime()))
    
    
    if river_depth > 8.0:
        
        print("High River Levels")
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("hackathoniniowa@gmail.com", "JungleH@ckathon")
        server.sendmail(
          "Flood Alert Ralston-Creek", 
          "hogan-myers@uiowa.edu", #EMAIL GOES HERE
          "Ralston creek at flooding levels! {} feet!".format(river_depth))
          #"Ralston creek at flooding levels! {} feet at {}".format(river_depth,time.ctime()))
        server.quit()
    
    
    #THIS IS USALLY 15 MIN or 900 SEC but decreased time refresh to show examples quicker
    time.sleep(300.0 - ((time.time() - starttime) % 300.0))
    
