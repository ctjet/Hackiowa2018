import shapefile as shp
import matplotlib.pyplot as plt
from dbfread import DBF


def draw(magnitudeDictionary):
  sf = shp.Reader("Shape/county.shp",)
  table = DBF('Shape/county.dbf')

  maxVal = max(magnitudeDictionary.values())



  names = []
  for record in table:
    names.append(record["COUNTY"])

  plt.figure()

  # numShapes = len(sf.shapeRecords())

  step = 1/maxVal

  current = 0
  for shape in sf.shapeRecords():
    curMag = magnitudeDictionary[names[current]]


    c = (curMag*step,1-curMag*step,0)
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.fill(x,y,color = c)
    current +=1

  plt.show()

# draw()