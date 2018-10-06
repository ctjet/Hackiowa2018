# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:19:23 2018
"""

#Nut sack please work
import pandas as pd
import gmplot
# For improved table display in the notebook
from IPython.display import display

raw_data = pd.read_csv("Addresses_in_the_City_of_Los_Angeles.csv")

# Success! Display the first 5 rows of the dataset
display(raw_data.head(n=5))
display(raw_data.info())
latitudes = raw_data["LAT"]
longitudes = raw_data["LON"]
# Creating the location we would like to initialize the focus on. 
# Parameters: Lattitude, Longitude, Zoom
gmap = gmplot.GoogleMapPlotter(41.8780, 93.0977, 5)

# Overlay our datapoints onto the map
gmap.heatmap(latitudes, longitudes)