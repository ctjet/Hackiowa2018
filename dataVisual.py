import shapefile as shp
import matplotlib.pyplot as plt
from dbfread import DBF


def draw(magnitudeDictionary, title):
  plt.close()

  sf = shp.Reader("Shape/county.shp",)
  table = DBF('Shape/county.dbf')

  maxVal = max(magnitudeDictionary.values())



  names = []
  for record in table:
    names.append(record["COUNTY"])

  plt.figure()
  plt.suptitle(title)

  # numShapes = len(sf.shapeRecords())
  if maxVal != 0:
      step = 1/maxVal
  else:
      step = 0

  current = 0
  for shape in sf.shapeRecords():
    curMag = magnitudeDictionary[names[current]]


    c = (curMag*step,1-curMag*step,0)
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.fill(x,y,color = c)
    plt.plot(x,y,color = 'black')
    current +=1
  plt.show()

# draw()