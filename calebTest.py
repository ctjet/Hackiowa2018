from dbfread import dbf

"""
Created on Sat Oct  6 10:19:23 2018
"""

#Nut sack please work
import pandas as pd
import random
import gmplot
import gmaps
import gmaps.datasets
import csv

# For improved table display in the notebook
from IPython.display import display





# def gmapDraw():
#     print("hi")

#     raw_data = pd.read_csv("DB\\IowaCountyData.csv")

#     # Success! Display the first 5 rows of the dataset
#     # display(raw_data.head(n=5))
#     # display(raw_data.info())
#     latitudes = raw_data["Lat"]
#     longitudes = raw_data["Long"]
    
#     test = [(1,2,3),(2,2,6)]
#     earthquake_data = gmaps.datasets.load_dataset("earthquakes")

#     print(earthquake_data[:4]) # first four rows

#     m = gmaps.Map();
#     # m.add_layer(gmaps.WeightedHeatmap(data = earthquake_data))
#     m

# gmapDraw()

def draw(magnitudes):

    latitudes = []
    longitudes = []

    with open('./DB//IowaCountyData.csv', 'r') as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        i = 0;
        for row in csv_file_reader:
            for times in range(0,magnitudes[i]):
                latitudes.append(float( row['Lat']))
                longitudes.append(float(row['Long']))
            i+=1

            # Do something here
            # print(row['Lat'])
            # print(row['Long'])
    

    # raw_data = pd.read_csv("DB\\IowaCountyData.csv",names = ['Lat','Long'])
    

    # latitudes = raw_data.Lat.ix[:,0].toList();
    # longitudes = raw_data.Long.ix[:,0].toList();

    # Success! Display the first 5 rows of the dataset
    # display(raw_data.head(n=5))
    # display(raw_data.info())
    # latitudes = raw_data["Lat"].toList()
    # longitudes = raw_data["Long"].toList()
    # latitudes = [1,2]
    # longitudes = [3,4]

    


    # Creating the location we would like to initialize the focus on. 
    # Parameters: Lattitude, Longitude, Zoom
    gmap = gmplot.GoogleMapPlotter(41.8780, -93.0977, 7)

    # Overlay our datapoints onto the map
    #gmap.heatmap(latitudes, longitudes,magnitudes)

    gmap.heatmap(lats = latitudes,lngs = longitudes,radius=20,opacity=.8)
    

    gmap.draw("my_heatmap.html")
    print("Drawn")

