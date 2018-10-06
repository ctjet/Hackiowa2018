from dbfread import dbf

"""
Created on Sat Oct  6 10:19:23 2018
"""

#Nut sack please work
import pandas as pd
import random
import gmplot
# For improved table display in the notebook
from IPython.display import display

def draw(magnitudes):

    raw_data = pd.read_csv("DB\\IowaCountyData.csv")

    # Success! Display the first 5 rows of the dataset
    # display(raw_data.head(n=5))
    # display(raw_data.info())
    latitudes = raw_data["Lat"]
    longitudes = raw_data["Long"]

    # Creating the location we would like to initialize the focus on. 
    # Parameters: Lattitude, Longitude, Zoom
    gmap = gmplot.GoogleMapPlotter(41.8780, -93.0977, 7)

    # Overlay our datapoints onto the map
    gmap.heatmap(latitudes, longitudes,magnitudes)

    gmap.draw("my_heatmap.html")
    print("Drawn")

